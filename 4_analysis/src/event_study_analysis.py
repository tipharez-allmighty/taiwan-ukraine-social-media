"""Event-study test of H1/H2/H3 from the research proposal, using events.csv.

These hypotheses are unrelated to, and independently numbered from, the
Ukraine<->Taiwan aggregate sentiment correlation tested in
lag_causality_analysis.py - that's a separate analysis on a separate
question (continuous monthly/weekly co-movement, not discrete dated events)
and isn't part of this script's H1/H2/H3.

The proposal's hypotheses are about SPARSE, DATED events causing a short-term
surge in specific narrative discussion volume in the days that follow. With
only 24,592 rows over ~4.5 years, daily comment counts per label are too
sparse for a Granger/CCF-style regression on daily bins. The right tool for
"does X surge after event type Y" with a handful of discrete dated events is
a pooled event study: for each event, compare a WINDOW_DAYS-day window before
vs. after, then pool across all events of that type and test whether "after"
is systematically higher.

  H1 (territorial_loss)      -> disappointment_with_us (all rows) AND
                                 critical_taiwan (Taiwan-topic rows)
  H2 (us_pressure_statement) -> disappointment_with_us (all rows) AND
                                 critical_taiwan (Taiwan-topic rows)
  H3 (military_tech_win)     -> supportive_taiwan (Taiwan-topic rows)

Each event contributes one paired (pre-mean, post-mean) daily-count
observation; the pooled test is a paired t-test and a Wilcoxon signed-rank
test (more appropriate given only 7-10 events per hypothesis). Restricted to
human_rows_excl_simplified_zh (Simplified Chinese text excluded), real
message dates (not scrape-assigned timeline).

Caveats:
  - H2's 8 events cluster tightly (5 of them within Feb 14 - Mar 5, 2025), so
    their pre/post windows overlap each other - read that result as "does
    discussion increase after this cluster," not as 8 independent trials.
  - n_events is small (7-10) for every hypothesis; even a large-looking
    percent change can fail both significance tests, and vice versa.
  - Daily counts are noisy; WINDOW_DAYS trades this off against catching
    only the true short-term reaction.

Saved under figures/event_study/:
  event_study_summary.png/csv     - one row per hypothesis/target: pre-mean,
                                     post-mean, % change, paired-t p, Wilcoxon p.
  h1_*.png, h2_*.png, h3_*.png     - per-target event-study plots: daily count
                                     averaged across events, aligned to event
                                     day (offset 0), individual events shown
                                     faint behind the pooled average.
  h1_*.csv, h2_*.csv, h3_*.csv     - the underlying per-event/per-offset data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from analyze_labels import DB_PATH, FIGURES_ROOT, build_views, compute_message_dates, connect, render_table

SCRIPT_DIR = Path(__file__).resolve().parent
EVENTS_CSV = SCRIPT_DIR.parent / "events.csv"
DIR_EVENT_STUDY = FIGURES_ROOT / "event_study"

TOPIC_BUCKETS_PY = {
    "Ukraine": ["Ukraine", "Taiwan and Ukraine"],
    "Taiwan": ["Taiwan", "Taiwan and Ukraine"],
}

WINDOW_DAYS = 10

# Each target label is run across all three topic scopes below (ALL, then
# each entry here), so we can see whether a surge is Taiwan-specific,
# Ukraine-specific, or shows up regardless of which video it's under.
TOPIC_SCOPES = [("All", None), ("Ukraine", "Ukraine"), ("Taiwan", "Taiwan")]

# (hypothesis, category in events.csv) -> list of (label, note)
HYPOTHESES = {
    "H1": {
        "category": "territorial_loss",
        "title": "H1: territorial-loss news",
        "targets": [
            ("disappointment_with_us", "\"America abandons Taiwan\" proxy"),
            ("critical_taiwan", "\"today Ukraine, tomorrow Taiwan\" proxy"),
        ],
    },
    "H2": {
        "category": "us_pressure_statement",
        "title": "H2: US-leader public pressure",
        "targets": [
            ("disappointment_with_us", "\"America abandons Taiwan\" proxy"),
            ("critical_taiwan", "\"today Ukraine, tomorrow Taiwan\" proxy"),
        ],
    },
    "H3": {
        "category": "military_tech_win",
        "title": "H3: military/tech wins",
        "targets": [
            ("supportive_taiwan", "\"Taiwan can resist China\" proxy"),
        ],
    },
}

# Display-only relabeling for rendered table images: this script's own
# hypotheses (territorial_loss/us_pressure/military_win) are H1/H2/H3
# internally, but the report/deck reserves H1 for the separate correlation
# finding, so on that side these are H2/H3/H4. Never touch HYPOTHESES,
# events.csv, or events.md to "fix" this - only the rendered label here.
REPORT_HYP_LABEL = {"H1": "H2", "H2": "H3", "H3": "H4"}


def load_events():
    df = pd.read_csv(EVENTS_CSV, parse_dates=["date"])
    return df


def load_daily_label_data(con):
    df = con.execute(
        "SELECT id, topic, critical_ukraine, supportive_ukraine, critical_taiwan, "
        "supportive_taiwan, disappointment_with_us, blame_nato_expansion "
        "FROM human_rows_excl_simplified_zh"
    ).fetchdf()
    dates = compute_message_dates(DB_PATH)
    df = df.merge(dates, on="id").dropna(subset=["message_date"])
    df["date"] = df["message_date"].dt.tz_convert(None).dt.normalize()
    return df


def daily_series(df, label, topic_bucket):
    sub = df[df["topic"].isin(TOPIC_BUCKETS_PY[topic_bucket])] if topic_bucket else df
    g = sub.groupby("date")
    n = g.size()
    count = g[label].sum()

    full_range = pd.date_range(df["date"].min(), df["date"].max(), freq="D")
    result = pd.DataFrame(index=full_range)
    result.index.name = "date"
    result["n"] = n.reindex(full_range).fillna(0).astype(int)
    result["count"] = count.reindex(full_range).fillna(0).astype(int)
    with np.errstate(invalid="ignore", divide="ignore"):
        result["share"] = (result["count"] / result["n"] * 100).replace([np.inf, -np.inf], np.nan)
    return result


def extract_event_windows(daily, event_dates, window=WINDOW_DAYS):
    rows = []
    for ev_date in event_dates:
        ev_date = pd.Timestamp(ev_date).normalize()
        for offset in range(-window, window + 1):
            d = ev_date + pd.Timedelta(days=offset)
            if d in daily.index:
                rows.append(
                    {
                        "event_date": ev_date,
                        "offset": offset,
                        "count": daily.loc[d, "count"],
                        "share": daily.loc[d, "share"],
                    }
                )
    return pd.DataFrame(rows)


def pooled_pre_post_test(window_df):
    """Paired (per-event) pre-window mean vs post-window mean, day 0 (the
    event day itself) included in 'post' since news breaks and is discussed
    same-day."""
    pre = window_df[window_df["offset"] < 0]
    post = window_df[window_df["offset"] >= 0]

    pre_by_event = pre.groupby("event_date")["count"].mean()
    post_by_event = post.groupby("event_date")["count"].mean()
    paired = pd.DataFrame({"pre": pre_by_event, "post": post_by_event}).dropna()

    if len(paired) >= 3:
        t_stat, t_p = stats.ttest_rel(paired["post"], paired["pre"])
        try:
            w_stat, w_p = stats.wilcoxon(paired["post"], paired["pre"])
        except ValueError:
            w_stat, w_p = float("nan"), float("nan")
    else:
        t_stat = t_p = w_stat = w_p = float("nan")

    return paired, t_stat, t_p, w_stat, w_p


def render_event_study_plot(window_df, title, filename_stem):
    fig, ax = plt.subplots(figsize=(10, 5.5))

    pivot = window_df.pivot(index="event_date", columns="offset", values="count")
    for _, row in pivot.iterrows():
        ax.plot(row.index, row.values, color="#4C72B0", alpha=0.25, linewidth=1)

    avg = pivot.mean(axis=0)
    ax.plot(avg.index, avg.values, color="#C44E52", linewidth=2.5, marker="o", markersize=3, label="Average across events")

    ax.axvline(0, color="#333333", linewidth=1, linestyle="--")
    ax.set_xlabel("Days relative to event (0 = event day)")
    ax.set_ylabel("Daily count of rows with this label")
    ax.set_title(title)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, linewidth=0.5, alpha=0.5)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="best")

    fig.tight_layout()
    png_path = DIR_EVENT_STUDY / f"{filename_stem}.png"
    fig.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

    csv_path = DIR_EVENT_STUDY / f"{filename_stem}.csv"
    window_df.to_csv(csv_path, index=False)
    return csv_path, png_path


def render_summary_table(summary_rows):
    def fmt_p(p):
        if pd.isna(p):
            return "n/a"
        return f"{p:.3f}{'*' if p < 0.05 else ''}"

    df = pd.DataFrame(summary_rows)
    display_df = pd.DataFrame(
        {
            "Hyp.": df["hypothesis"].map(REPORT_HYP_LABEL),
            "Target label": df["label"],
            "Topic": df["topic_scope"],
            "N events": df["n_events"],
            "Pre-mean/day": df["pre_mean"].map("{:.2f}".format),
            "Post-mean/day": df["post_mean"].map("{:.2f}".format),
            "% change": df["pct_change"].map(lambda x: f"{x:+.0f}%" if pd.notna(x) else "n/a"),
            "Paired-t p": df["t_p"].map(fmt_p),
            "Wilcoxon p": df["w_p"].map(fmt_p),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=list(display_df.columns),
        title=f"H2/H3/H4 event-study summary, by topic (±{WINDOW_DAYS}-day window; * = p<0.05)",
        out_dir=DIR_EVENT_STUDY,
        filename_stem="event_study_summary",
        figsize=(15, 0.9 + 0.4 * len(display_df)),
        col_widths=[0.06, 0.20, 0.09, 0.09, 0.12, 0.13, 0.10, 0.11, 0.11],
        fontsize=9,
    )
    csv_path = DIR_EVENT_STUDY / "event_study_summary.csv"
    df.to_csv(csv_path, index=False)
    return csv_path, png_path


WINDOW_SIZES_TO_CHECK = [5, 10, 20]

# The headline target per hypothesis, as reported in the summary/report -
# checked across several window sizes as a robustness check: does the
# verdict (and its p-value) hold up if WINDOW_DAYS had been chosen
# differently, or is it an artifact of the specific 10-day choice?
ROBUSTNESS_TARGETS = [
    ("H1", "territorial_loss", "disappointment_with_us", None),
    ("H2", "us_pressure_statement", "disappointment_with_us", None),
    ("H2", "us_pressure_statement", "critical_taiwan", "Ukraine"),
    ("H3", "military_tech_win", "supportive_taiwan", "Taiwan"),
]


def run_window_sensitivity(con, events, daily_data):
    """For each headline target, rerun the pre/post test at several window
    sizes (5/10/20 days instead of just WINDOW_DAYS=10) and record how much
    the % change and p-values move - checks whether a finding is robust to
    the window-size choice or just an artifact of picking 10 days."""
    rows = []
    for hyp, category, label, topic_bucket in ROBUSTNESS_TARGETS:
        event_dates = events.loc[events["category"] == category, "date"].tolist()
        daily = daily_series(daily_data, label, topic_bucket)
        for window in WINDOW_SIZES_TO_CHECK:
            window_df = extract_event_windows(daily, event_dates, window=window)
            paired, t_stat, t_p, w_stat, w_p = pooled_pre_post_test(window_df)
            pre_mean = paired["pre"].mean() if len(paired) else float("nan")
            post_mean = paired["post"].mean() if len(paired) else float("nan")
            pct_change = (post_mean - pre_mean) / pre_mean * 100 if pre_mean else float("nan")
            rows.append(
                {
                    "hypothesis": hyp,
                    "label": label,
                    "topic_scope": topic_bucket or "All",
                    "window_days": window,
                    "n_events": len(paired),
                    "pre_mean": pre_mean,
                    "post_mean": post_mean,
                    "pct_change": pct_change,
                    "t_p": t_p,
                    "w_p": w_p,
                }
            )
    return pd.DataFrame(rows)


def render_window_sensitivity_table(df):
    def fmt_p(p):
        if pd.isna(p):
            return "n/a"
        return f"{p:.3f}{'*' if p < 0.05 else ''}"

    display_df = pd.DataFrame(
        {
            "Hyp.": df["hypothesis"].map(REPORT_HYP_LABEL),
            "Target label": df["label"],
            "Topic": df["topic_scope"],
            "Window": df["window_days"].map(lambda d: f"{d}d"),
            "% change": df["pct_change"].map(lambda x: f"{x:+.0f}%" if pd.notna(x) else "n/a"),
            "Paired-t p": df["t_p"].map(fmt_p),
            "Wilcoxon p": df["w_p"].map(fmt_p),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=list(display_df.columns),
        title="Window-size sensitivity check: same headline results at 5/10/20-day windows\n(* = p<0.05; is the finding stable, or an artifact of the 10-day choice?)",
        out_dir=DIR_EVENT_STUDY,
        filename_stem="window_sensitivity",
        figsize=(12, 0.9 + 0.4 * len(display_df)),
        col_widths=[0.08, 0.24, 0.11, 0.11, 0.14, 0.16, 0.16],
        fontsize=9,
    )
    csv_path = DIR_EVENT_STUDY / "window_sensitivity.csv"
    df.to_csv(csv_path, index=False)
    return csv_path, png_path


def merge_close_events(event_dates, merge_gap=14):
    """Group events within merge_gap days of each other into clusters, each
    represented as (first_date, last_date) - so a burst of closely-spaced
    events (e.g. several statements during one crisis week) is treated as
    ONE data point instead of several overlapping, non-independent ones."""
    dates = sorted(pd.Timestamp(d) for d in event_dates)
    clusters = []
    cluster_start = cluster_end = dates[0]
    for d in dates[1:]:
        if (d - cluster_end).days <= merge_gap:
            cluster_end = d
        else:
            clusters.append((cluster_start, cluster_end))
            cluster_start = cluster_end = d
    clusters.append((cluster_start, cluster_end))
    return clusters


def extract_cluster_windows(daily, clusters, window=WINDOW_DAYS):
    """Like extract_event_windows, but the "before" window is measured from
    the cluster's first event and the "after" window from its last event -
    so a multi-event cluster contributes one pre/post pair, not several
    overlapping ones."""
    rows = []
    for cluster_start, cluster_end in clusters:
        for offset in range(-window, window + 1):
            d = (cluster_start if offset < 0 else cluster_end) + pd.Timedelta(days=offset)
            if d in daily.index:
                rows.append(
                    {
                        "event_date": cluster_start,
                        "cluster_end": cluster_end,
                        "offset": offset,
                        "count": daily.loc[d, "count"],
                        "share": daily.loc[d, "share"],
                    }
                )
    return pd.DataFrame(rows)


def run_cluster_correction(events, daily_data, targets, merge_gap=14):
    """For each target, rerun the pre/post test with tightly-clustered events
    merged into single data points, at window=10 and window=20 - checks
    whether a result survives once non-independent, overlapping events
    aren't double(or more)-counted as separate trials."""
    rows = []
    for hyp, category, label, topic_bucket in targets:
        event_dates = events.loc[events["category"] == category, "date"].tolist()
        clusters = merge_close_events(event_dates, merge_gap=merge_gap)
        daily = daily_series(daily_data, label, topic_bucket)
        for window in (10, 20):
            window_df = extract_cluster_windows(daily, clusters, window=window)
            paired, t_stat, t_p, w_stat, w_p = pooled_pre_post_test(window_df)
            pre_mean = paired["pre"].mean() if len(paired) else float("nan")
            post_mean = paired["post"].mean() if len(paired) else float("nan")
            pct_change = (post_mean - pre_mean) / pre_mean * 100 if pre_mean else float("nan")
            rows.append(
                {
                    "hypothesis": hyp,
                    "label": label,
                    "topic_scope": topic_bucket or "All",
                    "window_days": window,
                    "n_raw_events": len(event_dates),
                    "n_clusters": len(clusters),
                    "pre_mean": pre_mean,
                    "post_mean": post_mean,
                    "pct_change": pct_change,
                    "t_p": t_p,
                    "w_p": w_p,
                }
            )
    return pd.DataFrame(rows)


def render_cluster_correction_table(df):
    def fmt_p(p):
        if pd.isna(p):
            return "n/a"
        return f"{p:.3f}{'*' if p < 0.05 else ''}"

    display_df = pd.DataFrame(
        {
            "Hyp.": df["hypothesis"].map(REPORT_HYP_LABEL),
            "Target label": df["label"],
            "Topic": df["topic_scope"],
            "Window": df["window_days"].map(lambda d: f"{d}d"),
            "Events → clusters": df.apply(lambda r: f"{r['n_raw_events']} → {r['n_clusters']}", axis=1),
            "% change": df["pct_change"].map(lambda x: f"{x:+.0f}%" if pd.notna(x) else "n/a"),
            "Paired-t p": df["t_p"].map(fmt_p),
            "Wilcoxon p": df["w_p"].map(fmt_p),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=list(display_df.columns),
        title="Cluster-correction check: tightly-spaced events (within 14 days) merged into one\n(* = p<0.05; is a result driven by real repetition, or one crisis counted many times?)",
        out_dir=DIR_EVENT_STUDY,
        filename_stem="cluster_correction",
        figsize=(13, 0.9 + 0.4 * len(display_df)),
        col_widths=[0.07, 0.22, 0.10, 0.09, 0.14, 0.12, 0.13, 0.13],
        fontsize=9,
    )
    csv_path = DIR_EVENT_STUDY / "cluster_correction.csv"
    df.to_csv(csv_path, index=False)
    return csv_path, png_path


def main():
    DIR_EVENT_STUDY.mkdir(parents=True, exist_ok=True)
    con = connect()
    build_views(con)

    events = load_events()
    daily_data = load_daily_label_data(con)

    outputs = []
    summary_rows = []

    for hyp, spec in HYPOTHESES.items():
        category = spec["category"]
        event_dates = events.loc[events["category"] == category, "date"].tolist()
        print(f"\n{hyp} ({category}): {len(event_dates)} events")

        for label, note in spec["targets"]:
            for scope_name, topic_bucket in TOPIC_SCOPES:
                daily = daily_series(daily_data, label, topic_bucket)
                window_df = extract_event_windows(daily, event_dates)
                paired, t_stat, t_p, w_stat, w_p = pooled_pre_post_test(window_df)

                pre_mean = paired["pre"].mean() if len(paired) else float("nan")
                post_mean = paired["post"].mean() if len(paired) else float("nan")
                pct_change = (post_mean - pre_mean) / pre_mean * 100 if pre_mean else float("nan")

                summary_rows.append(
                    {
                        "hypothesis": hyp,
                        "label": label,
                        "topic_scope": scope_name,
                        "n_events": len(paired),
                        "pre_mean": pre_mean,
                        "post_mean": post_mean,
                        "pct_change": pct_change,
                        "t_p": t_p,
                        "w_p": w_p,
                    }
                )

                stem = f"{hyp.lower()}_{label}_{scope_name.lower()}"
                title = f"{spec['title']} → {label} ({scope_name} topic)\n{note}, N={len(paired)} events"
                outputs.append(render_event_study_plot(window_df, title, stem))

                print(
                    f"  {label} [{scope_name}]: "
                    f"pre={pre_mean:.2f}/day post={post_mean:.2f}/day ({pct_change:+.0f}%), "
                    f"paired-t p={t_p:.3f}, wilcoxon p={w_p:.3f} (n={len(paired)})"
                )

    outputs.append(render_summary_table(summary_rows))

    print("\nWindow-size sensitivity check (5/10/20-day windows):")
    sensitivity_df = run_window_sensitivity(con, events, daily_data)
    for _, r in sensitivity_df.iterrows():
        print(
            f"  {r['hypothesis']} {r['label']} [{r['topic_scope']}] {r['window_days']}d: "
            f"{r['pct_change']:+.0f}%, t-p={r['t_p']:.3f}, w-p={r['w_p']:.3f}"
        )
    outputs.append(render_window_sensitivity_table(sensitivity_df))

    print("\nCluster-correction check (tightly-spaced events merged, gap<=14 days):")
    cluster_df = run_cluster_correction(events, daily_data, ROBUSTNESS_TARGETS)
    for _, r in cluster_df.iterrows():
        print(
            f"  {r['hypothesis']} {r['label']} [{r['topic_scope']}] {r['window_days']}d "
            f"({r['n_raw_events']} events -> {r['n_clusters']} clusters): "
            f"{r['pct_change']:+.0f}%, t-p={r['t_p']:.3f}, w-p={r['w_p']:.3f}"
        )
    outputs.append(render_cluster_correction_table(cluster_df))

    print("\nWrote:")
    for csv_path, png_path in outputs:
        print(f"  {png_path}")
        print(f"  {csv_path}")


if __name__ == "__main__":
    main()
