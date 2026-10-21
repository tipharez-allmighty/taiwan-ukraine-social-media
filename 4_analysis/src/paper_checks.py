"""Recounts behind the numbers in the paper.

Reuses the views and helpers from analyze_labels.py / event_study_analysis.py /
correlation_by_timeline.py so numbers stay comparable with REPORT.md. The DB is
attached READ_ONLY. Output: printed tables + CSVs in 5_results/tables/.

  1. Labelling: AI-vs-AI agreement, how many rows went to the human, and
     whom the human sided with.
  2. H1: Ukraine vs Taiwan net sentiment over the 7 periods - r with its p.
  3. Co-occurrence: disappointment_with_us vs critical/supportive_taiwan in
     the same comment - odds ratio with 95% CI, and a logistic regression
     controlling for topic and period. Also with AI-only labels.
  4. Event study H2-H4: count AND share (label / all comments) per window,
     with Holm and BH correction over the 4 headline tests.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.stats.multitest import multipletests

import analyze_labels as al
import correlation_by_timeline as ct
import event_study_analysis as es

OUT_DIR = Path(__file__).resolve().parents[2] / "5_results" / "tables"
LABELS = al.LABELS


def connect_read_only(db_path):
    import duckdb

    con = duckdb.connect()
    con.execute("INSTALL sqlite; LOAD sqlite;")
    con.execute(f"ATTACH '{db_path}' AS db (TYPE sqlite, READ_ONLY)")
    return con


def section(title):
    print(f"\n{'=' * 80}\n{title}\n{'=' * 80}")


def kappa(a, b):
    po = (a == b).mean()
    pe = a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean())
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def labelling_check(con):
    section("1. Labelling: AI vs AI, and the human step")
    wide = {}
    for who in ["claude-opus-5", "claude-sonnet-5", "human"]:
        wide[who] = con.execute(
            f"SELECT yt_data_id, {', '.join(LABELS)} FROM db.yt_comment_label "
            f"WHERE labeler = '{who}' ORDER BY yt_data_id"
        ).fetchdf().set_index("yt_data_id").astype(int)
    opus, sonnet, human = wide["claude-opus-5"], wide["claude-sonnet-5"], wide["human"]

    rows = []
    for label in LABELS:
        disagree = opus[label] != sonnet[label]
        rows.append(
            {
                "label": label,
                "n": len(opus),
                "opus_yes": int(opus[label].sum()),
                "sonnet_yes": int(sonnet[label].sum()),
                "agreement_pct": (~disagree).mean() * 100,
                "kappa_opus_sonnet": kappa(opus[label], sonnet[label]),
                "n_disagree": int(disagree.sum()),
                "human_sided_opus": int((human.loc[disagree, label] == opus.loc[disagree, label]).sum()),
                "human_differs_where_ais_agree": int((human.loc[~disagree, label] != opus.loc[~disagree, label]).sum()),
            }
        )
    df = pd.DataFrame(rows)
    any_disagree = (opus != sonnet).any(axis=1)
    print(df.to_string(index=False))
    print(f"\nRows where the two AIs disagree on at least one label: {int(any_disagree.sum()):,} of {len(opus):,}")
    df.to_csv(OUT_DIR / "labelling_agreement.csv", index=False)
    return wide


def h1_check(con):
    section("2. H1: Ukraine vs Taiwan net sentiment over 7 periods")
    rows = []
    for col in ["timeline", "message_timeline"]:
        net = ct.compute_net_sentiment(con, col)
        r, p = stats.pearsonr(net["ukraine_net"], net["taiwan_net"])
        rho, p_s = stats.spearmanr(net["ukraine_net"], net["taiwan_net"])
        print(f"\n[{col}]\n{net.round(1).to_string()}")
        print(f"Pearson r = {r:.3f}, p = {p:.4f} (two-sided, n = 7); Spearman rho = {rho:.3f}, p = {p_s:.4f}")
        rows.append({"period_by": col, "n": len(net), "pearson_r": r, "pearson_p": p, "spearman_rho": rho, "spearman_p": p_s})
        net.to_csv(OUT_DIR / f"h1_net_sentiment_{col}.csv")
    pd.DataFrame(rows).to_csv(OUT_DIR / "h1_correlation.csv", index=False)


def odds_ratio_ci(a, b, c, d):
    """2x2: a = both yes, b = X yes / Y no, c = X no / Y yes, d = both no."""
    or_ = (a * d) / (b * c)
    se = np.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return or_, np.exp(np.log(or_) - 1.96 * se), np.exp(np.log(or_) + 1.96 * se)


def cooccurrence_check(con, wide):
    section("3. Co-occurrence: disappointed with US vs Taiwan labels, same comment")
    df = con.execute(
        "SELECT id, topic, message_timeline, disappointment_with_us, critical_taiwan, supportive_taiwan "
        "FROM human_rows_excl_simplified_zh"
    ).fetchdf()
    df[["disappointment_with_us", "critical_taiwan", "supportive_taiwan"]] = df[
        ["disappointment_with_us", "critical_taiwan", "supportive_taiwan"]
    ].astype(int)

    rows = []

    def add(source, frame):
        for y in ["critical_taiwan", "supportive_taiwan"]:
            x = frame["disappointment_with_us"]
            a = int(((x == 1) & (frame[y] == 1)).sum())
            b = int(((x == 1) & (frame[y] == 0)).sum())
            c = int(((x == 0) & (frame[y] == 1)).sum())
            d = int(((x == 0) & (frame[y] == 0)).sum())
            or_, lo, hi = odds_ratio_ci(a, b, c, d)
            chi2, p, _, _ = stats.chi2_contingency([[a, b], [c, d]])
            rows.append(
                {
                    "labels": source,
                    "taiwan_label": y,
                    "n": len(frame),
                    "n_disappointed": a + b,
                    "rate_if_disappointed_pct": a / (a + b) * 100,
                    "rate_if_not_pct": c / (c + d) * 100,
                    "odds_ratio": or_,
                    "ci_low": lo,
                    "ci_high": hi,
                    "chi2": chi2,
                    "p": p,
                }
            )

    add("human (final)", df)
    for ai in ["claude-opus-5", "claude-sonnet-5"]:
        ai_df = wide[ai].loc[df["id"]].reset_index(drop=True)
        add(ai, ai_df)
    res = pd.DataFrame(rows)
    pd.set_option("display.float_format", "{:.3g}".format)
    print(res.to_string(index=False))
    res.to_csv(OUT_DIR / "cooccurrence.csv", index=False)

    print("\nLogistic regression (human labels), controlling for topic and period:")
    df["topic"] = df["topic"].astype(str)
    df["period"] = df["message_timeline"].astype(str)
    reg_rows = []
    for y in ["critical_taiwan", "supportive_taiwan"]:
        m = smf.logit(f"{y} ~ disappointment_with_us + C(topic) + C(period)", data=df.dropna(subset=["period"])).fit(disp=0)
        coef = m.params["disappointment_with_us"]
        lo, hi = m.conf_int().loc["disappointment_with_us"]
        p = m.pvalues["disappointment_with_us"]
        print(f"  {y}: adjusted OR = {np.exp(coef):.2f} [95% CI {np.exp(lo):.2f}-{np.exp(hi):.2f}], p = {p:.3g}, n = {int(m.nobs)}")
        reg_rows.append({"taiwan_label": y, "adj_odds_ratio": np.exp(coef), "ci_low": np.exp(lo), "ci_high": np.exp(hi), "p": p, "n": int(m.nobs)})
    pd.DataFrame(reg_rows).to_csv(OUT_DIR / "cooccurrence_logit.csv", index=False)


HEADLINE = [
    ("H2", "territorial_loss", "disappointment_with_us", None),
    ("H2", "territorial_loss", "critical_taiwan", None),
    ("H3", "us_pressure_statement", "disappointment_with_us", None),
    ("H4", "military_tech_win", "supportive_taiwan", "Taiwan"),
]


def event_check(con, window=es.WINDOW_DAYS):
    section(f"4. Event study H2-H4 ({window}-day window): count and share, corrected")
    events = es.load_events()
    data = es.load_daily_label_data(con)
    rows = []
    for hyp, cat, label, scope in HEADLINE:
        dates = events.loc[events["category"] == cat, "date"].tolist()
        daily = es.daily_series(data, label, scope)
        w = es.extract_event_windows(daily, dates, window=window)
        w["n"] = [daily.loc[d + pd.Timedelta(days=o), "n"] for d, o in zip(w["event_date"], w["offset"])]
        w["side"] = np.where(w["offset"] < 0, "pre", "post")
        g = w.groupby(["event_date", "side"])[["count", "n"]].sum().unstack("side")
        days = w.groupby(["event_date", "side"]).size().unstack("side")
        per_event = pd.DataFrame(
            {
                "count_pre": g[("count", "pre")] / days["pre"],
                "count_post": g[("count", "post")] / days["post"],
                "share_pre": g[("count", "pre")] / g[("n", "pre")] * 100,
                "share_post": g[("count", "post")] / g[("n", "post")] * 100,
            }
        )
        for metric in ["count", "share"]:
            p_ = per_event[[f"{metric}_pre", f"{metric}_post"]].dropna()
            t = stats.ttest_rel(p_.iloc[:, 1], p_.iloc[:, 0])
            wil = stats.wilcoxon(p_.iloc[:, 1], p_.iloc[:, 0]).pvalue
            rows.append(
                {
                    "hyp": hyp,
                    "label": label,
                    "scope": scope or "All",
                    "metric": metric,
                    "n_events": len(p_),
                    "pre": p_.iloc[:, 0].mean(),
                    "post": p_.iloc[:, 1].mean(),
                    "t": t.statistic,
                    "df": len(p_) - 1,
                    "t_p": t.pvalue,
                    "wilcoxon_p": wil,
                }
            )
    res = pd.DataFrame(rows)
    for metric in ["count", "share"]:
        m = res["metric"] == metric
        res.loc[m, "t_p_holm"] = multipletests(res.loc[m, "t_p"], method="holm")[1]
        res.loc[m, "t_p_bh"] = multipletests(res.loc[m, "t_p"], method="fdr_bh")[1]
    pd.set_option("display.float_format", "{:.3f}".format)
    print(res.to_string(index=False))
    res.to_csv(OUT_DIR / f"event_study_corrected_{window}d.csv", index=False)


def merged_us_pressure_check(con, gap=14):
    """US-pressure events less than `gap` days apart merged into one episode;
    "before" is measured from the first event, "after" from the last."""
    section("5. US pressure merged into episodes -> disappointed with US")
    events = es.load_events()
    dates = sorted(events.loc[events["category"] == "us_pressure_statement", "date"])
    episodes = [[dates[0]]]
    for d in dates[1:]:
        if (d - episodes[-1][-1]).days < gap:
            episodes[-1].append(d)
        else:
            episodes.append([d])
    daily = es.daily_series(es.load_daily_label_data(con), "disappointment_with_us", None)
    rows = []
    for window in (10, 20):
        pre = [daily.loc[e[0] - pd.Timedelta(days=window) : e[0] - pd.Timedelta(days=1)] for e in episodes]
        post = [daily.loc[e[-1] : e[-1] + pd.Timedelta(days=window)] for e in episodes]
        per_ep = {
            "count": ([w["count"].mean() for w in pre], [w["count"].mean() for w in post]),
            "share": ([w["count"].sum() / w["n"].sum() * 100 for w in pre], [w["count"].sum() / w["n"].sum() * 100 for w in post]),
        }
        for metric, (b, a) in per_ep.items():
            t = stats.ttest_rel(a, b)
            rows.append(
                {
                    "test": "US pressure (merged episodes) -> disappointed with US",
                    "window": window,
                    "metric": metric,
                    "n": len(episodes),
                    "pre": np.mean(b),
                    "post": np.mean(a),
                    "t": t.statistic,
                    "df": len(episodes) - 1,
                    "p": t.pvalue,
                }
            )
    res = pd.DataFrame(rows)
    print(res.to_string(index=False))
    res.to_csv(OUT_DIR / "event_study_merged_us_pressure.csv", index=False)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    db_path = Path(sys.argv[1]) if len(sys.argv) > 1 else al.DB_PATH
    al.DB_PATH = es.DB_PATH = db_path
    con = connect_read_only(db_path)
    al.build_views(con)

    wide = labelling_check(con)
    h1_check(con)
    cooccurrence_check(con, wide)
    for window in (10, 20):
        event_check(con, window)
    merged_us_pressure_check(con)
    print(f"\nCSVs written to {OUT_DIR}")


if __name__ == "__main__":
    main()
