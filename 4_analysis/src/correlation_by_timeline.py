"""Ukraine/Taiwan stance-label correlation across timeline periods.

Restricted to the human_rows_excl_simplified_zh subset (Simplified-Chinese
text excluded, see analyze_labels.py) and to the 4 "stance" labels -
critical_ukraine, supportive_ukraine, critical_taiwan, supportive_taiwan.
The question: does being critical/supportive of Ukraine track with being
critical/supportive of Taiwan, and does that relationship shift across the
7 timeline periods?

Every analysis here is generated twice: once grouped by the DB's `timeline`
column (the video's scrape-assigned era), and once by `message_timeline`
(the row's actual comment/thread date bucketed into the same calendar
ranges) - suffixed `_by_message_date`. See analyze_labels.py's module
docstring for why those two differ.

Saved under figures/correlation/ (label_correlation_by_timeline*,
ukraine_taiwan_net_sentiment_correlation*) and figures/stance_share/
(label_share_by_timeline*, overall and split by topic).
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze_labels import (
    DIR_CORRELATION,
    DIR_MSG_EXCL,
    FIGURES_ROOT,
    TIMELINE_ORDER,
    TOPIC_BUCKETS,
    build_views,
    connect,
    render_table,
)

DIR_STANCE_SHARE = FIGURES_ROOT / "stance_share"

STANCE_LABELS = [
    "critical_ukraine",
    "supportive_ukraine",
    "critical_taiwan",
    "supportive_taiwan",
]

TIMELINE_VARIANTS = [
    ("timeline", "", ""),
    ("message_timeline", "_by_message_date", " (by message date)"),
]


def compute_correlations(con, timeline_col="timeline"):
    """Per-timeline-period 4x4 correlation matrix over the stance labels."""
    results = []
    for period in TIMELINE_ORDER:
        df = con.execute(
            f"SELECT {', '.join(STANCE_LABELS)} "
            f"FROM human_rows_excl_simplified_zh WHERE {timeline_col} = ?",
            [period],
        ).fetchdf()
        results.append((period, len(df), df.corr()))
    return results


def save_csv(results, out_dir, filename_stem):
    rows = []
    for period, n, corr in results:
        for a in STANCE_LABELS:
            for b in STANCE_LABELS:
                rows.append(
                    {"timeline": period, "n": n, "label_a": a, "label_b": b, "correlation": corr.loc[a, b]}
                )
    df = pd.DataFrame(rows)
    csv_path = out_dir / f"{filename_stem}.csv"
    df.to_csv(csv_path, index=False)
    return csv_path


def render_grid(results, title, out_dir, filename_stem):
    ncols = 4
    nrows = -(-len(results) // ncols)
    fig, axes = plt.subplots(
        nrows, ncols, figsize=(4.6 * ncols, 4.8 * nrows), gridspec_kw={"wspace": 0.9, "hspace": 0.6}
    )
    axes = axes.flatten()

    im = None
    for ax, (period, n, corr) in zip(axes, results):
        im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1)
        ax.set_xticks(range(len(STANCE_LABELS)))
        ax.set_xticklabels(STANCE_LABELS, rotation=40, ha="right", fontsize=8)
        ax.set_yticks(range(len(STANCE_LABELS)))
        ax.set_yticklabels(STANCE_LABELS, fontsize=8)
        for i in range(len(STANCE_LABELS)):
            for j in range(len(STANCE_LABELS)):
                val = corr.values[i, j]
                color = "white" if abs(val) > 0.6 else "black"
                ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=color, fontsize=8)
        ax.set_title(f"{period} (N={n:,})", fontsize=11)

    for ax in axes[len(results):]:
        ax.axis("off")

    fig.suptitle(title, fontsize=14)
    cbar = fig.colorbar(im, ax=axes.tolist(), fraction=0.02, pad=0.02)
    cbar.set_label("Pearson correlation (φ coefficient)")

    png_path = out_dir / f"{filename_stem}.png"
    fig.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return png_path


def run_correlation_grid(con, timeline_col, out_dir, filename_suffix, title_suffix):
    filename_stem = f"label_correlation_by_timeline_excl_simplified_zh{filename_suffix}"
    title = (
        "Ukraine/Taiwan stance-label correlation by timeline period"
        f"{title_suffix}\n(excluding Simplified Chinese text)"
    )
    results = compute_correlations(con, timeline_col)
    csv_path = save_csv(results, out_dir, filename_stem)
    png_path = render_grid(results, title, out_dir, filename_stem)
    return csv_path, png_path


STANCE_COLORS = {
    "critical_ukraine": "#C44E52",
    "supportive_ukraine": "#4C72B0",
    "critical_taiwan": "#DD8452",
    "supportive_taiwan": "#55A868",
}

SHARE_FILENAME_STEM = "label_share_by_timeline_excl_simplified_zh"


def compute_stance_share_by_timeline(con, topic_sql_in=None, timeline_col="timeline"):
    """% of each timeline period's rows carrying each stance label.

    If topic_sql_in is given (e.g. "('Ukraine', 'Taiwan and Ukraine')"), rows
    are restricted to that topic bucket - same rows-in-both-buckets
    convention used throughout analyze_labels.py.
    """
    select_cols = ", ".join(f"SUM({label}) AS {label}" for label in STANCE_LABELS)
    topic_filter = f"WHERE topic IN {topic_sql_in}" if topic_sql_in else ""
    df = (
        con.execute(
            f"""
            SELECT {timeline_col}, COUNT(*) AS n, {select_cols}
            FROM human_rows_excl_simplified_zh
            {topic_filter}
            GROUP BY {timeline_col}
            """
        )
        .fetchdf()
        .set_index(timeline_col)
        .reindex(TIMELINE_ORDER)
        .fillna(0)
    )
    df.index.name = "timeline"
    pct = df[STANCE_LABELS].div(df["n"], axis=0).fillna(0) * 100
    pct.index.name = "timeline"
    return df["n"], pct


def save_share_csv(n_per_period, pct, out_dir, filename_stem):
    long_df = (
        pct.reset_index()
        .melt(id_vars="timeline", var_name="label", value_name="pct_of_period")
        .merge(n_per_period.rename("n").reset_index(), on="timeline")
    )
    csv_path = out_dir / f"{filename_stem}.csv"
    long_df.to_csv(csv_path, index=False)
    return csv_path


def render_share_line_chart(n_per_period, pct, title, out_dir, filename_stem):
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(TIMELINE_ORDER))

    for label in STANCE_LABELS:
        ax.plot(x, pct[label].values, marker="o", label=label, color=STANCE_COLORS[label])

    ax.set_xticks(list(x))
    ax.set_xticklabels(TIMELINE_ORDER, rotation=30, ha="right")
    ax.set_ylabel("% of rows in period")
    ax.set_title(title)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, linewidth=0.5, alpha=0.5)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="best")

    fig.tight_layout()
    png_path = out_dir / f"{filename_stem}.png"
    fig.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return png_path


def run_stance_share(
    con, out_dir, timeline_col="timeline", topic_sql_in=None, filename_stem=SHARE_FILENAME_STEM, title_suffix=""
):
    n_per_period, pct = compute_stance_share_by_timeline(con, topic_sql_in, timeline_col)
    csv_path = save_share_csv(n_per_period, pct, out_dir, filename_stem)
    title = f"Critical / supportive share by timeline period{title_suffix}\n(excluding Simplified Chinese text)"
    png_path = render_share_line_chart(n_per_period, pct, title, out_dir, filename_stem)
    return csv_path, png_path


NET_FILENAME_STEM = "ukraine_taiwan_net_sentiment_correlation"


def compute_net_sentiment(con, timeline_col="timeline"):
    """Per-period net sentiment: % supportive minus % critical, each within
    its own topic bucket (Ukraine-topic rows for ukraine_net, Taiwan-topic
    rows for taiwan_net) - i.e. "how well is Ukraine doing" vs. "how is
    Taiwan itself viewed", independent of each other's topic subset."""
    _, u_pct = compute_stance_share_by_timeline(con, TOPIC_BUCKETS["Ukraine"], timeline_col)
    _, t_pct = compute_stance_share_by_timeline(con, TOPIC_BUCKETS["Taiwan"], timeline_col)
    df = pd.DataFrame(
        {
            "ukraine_net": u_pct["supportive_ukraine"] - u_pct["critical_ukraine"],
            "taiwan_net": t_pct["supportive_taiwan"] - t_pct["critical_taiwan"],
        },
        index=TIMELINE_ORDER,
    )
    df.index.name = "timeline"
    return df


def render_net_sentiment(df, title_suffix, out_dir, filename_stem):
    r = df["ukraine_net"].corr(df["taiwan_net"])

    fig, (ax_line, ax_scatter) = plt.subplots(1, 2, figsize=(14, 5.5))
    x = range(len(df))

    ax_line.axhline(0, color="#999999", linewidth=0.8)
    ax_line.plot(x, df["ukraine_net"], marker="o", label="Ukraine net (supportive − critical)", color="#4C72B0")
    ax_line.plot(x, df["taiwan_net"], marker="o", label="Taiwan net (supportive − critical)", color="#55A868")
    ax_line.set_xticks(list(x))
    ax_line.set_xticklabels(df.index, rotation=30, ha="right")
    ax_line.set_ylabel("Net sentiment (pct. points)")
    ax_line.set_title("Net sentiment by timeline period")
    ax_line.spines["top"].set_visible(False)
    ax_line.spines["right"].set_visible(False)
    ax_line.yaxis.grid(True, linewidth=0.5, alpha=0.5)
    ax_line.set_axisbelow(True)
    ax_line.legend(frameon=False, loc="best", fontsize=9)

    ax_scatter.axhline(0, color="#999999", linewidth=0.8)
    ax_scatter.axvline(0, color="#999999", linewidth=0.8)
    ax_scatter.scatter(df["ukraine_net"], df["taiwan_net"], color="#C44E52", zorder=3)
    for period, row in df.iterrows():
        ax_scatter.annotate(
            period, (row["ukraine_net"], row["taiwan_net"]),
            textcoords="offset points", xytext=(6, 4), fontsize=8,
        )
    if df["ukraine_net"].std() > 0:
        slope, intercept = np.polyfit(df["ukraine_net"], df["taiwan_net"], 1)
        xs = np.array([df["ukraine_net"].min(), df["ukraine_net"].max()])
        ax_scatter.plot(xs, slope * xs + intercept, color="#999999", linestyle="--", linewidth=1)
    ax_scatter.set_xlabel("Ukraine net sentiment")
    ax_scatter.set_ylabel("Taiwan net sentiment")
    ax_scatter.set_title(f"Pearson r = {r:.2f} (n={len(df)} periods)")
    ax_scatter.spines["top"].set_visible(False)
    ax_scatter.spines["right"].set_visible(False)

    fig.suptitle(
        f"Does Ukraine's sentiment track with how Taiwan is viewed?{title_suffix}\n"
        "(excluding Simplified Chinese text)",
        fontsize=13,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    png_path = out_dir / f"{filename_stem}.png"
    fig.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return png_path, r


def run_net_sentiment_correlation(con, out_dir, timeline_col="timeline", filename_suffix="", title_suffix=""):
    filename_stem = f"{NET_FILENAME_STEM}{filename_suffix}"
    df = compute_net_sentiment(con, timeline_col)
    png_path, r = render_net_sentiment(df, title_suffix, out_dir, filename_stem)
    csv_path = out_dir / f"{filename_stem}.csv"
    df.assign(pearson_r_overall=r).to_csv(csv_path)
    return csv_path, png_path, r


def run_leave_one_out_check(df, full_r, out_dir, filename_stem="net_sentiment_leave_one_out"):
    """Recompute the Ukraine/Taiwan net-sentiment correlation with each
    timeline period dropped in turn - checks whether the headline r is
    propped up by one unusual period, or holds up regardless of which
    period is removed."""
    rows = []
    for period in df.index:
        sub = df.drop(index=period)
        r = sub["ukraine_net"].corr(sub["taiwan_net"])
        rows.append({"dropped_period": period, "n": len(sub), "pearson_r": r, "full_r": full_r})
    result_df = pd.DataFrame(rows)

    csv_path = out_dir / f"{filename_stem}.csv"
    result_df.to_csv(csv_path, index=False)

    display_df = pd.DataFrame(
        {
            "Period dropped": result_df["dropped_period"],
            "N (periods left)": result_df["n"],
            "Pearson r": result_df["pearson_r"].map("{:.3f}".format),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=list(display_df.columns),
        title=f"Leave-one-out check: does dropping any one period break the correlation?\nFull r (all 7 periods) = {full_r:.3f}",
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(9, 0.9 + 0.4 * len(display_df)),
        col_widths=[0.4, 0.3, 0.3],
    )
    return csv_path, png_path


def main():
    for d in (DIR_CORRELATION, DIR_STANCE_SHARE, DIR_MSG_EXCL):
        d.mkdir(parents=True, exist_ok=True)
    con = connect()
    build_views(con)

    all_outputs = []

    for timeline_col, filename_suffix, title_suffix in TIMELINE_VARIANTS:
        # message-date variants (everything here is already Simplified-
        # Chinese-excluded) go in the shared top-level DIR_MSG_EXCL folder,
        # same as analyze_labels.py.
        is_msg = timeline_col == "message_timeline"
        corr_dir = DIR_MSG_EXCL if is_msg else DIR_CORRELATION
        share_dir = DIR_MSG_EXCL if is_msg else DIR_STANCE_SHARE

        csv_path, png_path = run_correlation_grid(con, timeline_col, corr_dir, filename_suffix, title_suffix)
        all_outputs.append((csv_path, png_path))

        share_stem = f"{SHARE_FILENAME_STEM}{filename_suffix}"
        all_outputs.append(
            run_stance_share(
                con, share_dir, timeline_col=timeline_col, filename_stem=share_stem, title_suffix=title_suffix
            )
        )
        for topic_name, sql_in in TOPIC_BUCKETS.items():
            all_outputs.append(
                run_stance_share(
                    con,
                    share_dir,
                    timeline_col=timeline_col,
                    topic_sql_in=sql_in,
                    filename_stem=f"{share_stem}_{topic_name.lower()}",
                    title_suffix=f"{title_suffix} — {topic_name}",
                )
            )

        net_csv_path, net_png_path, r = run_net_sentiment_correlation(
            con, corr_dir, timeline_col=timeline_col, filename_suffix=filename_suffix, title_suffix=title_suffix
        )
        all_outputs.append((net_csv_path, net_png_path))

        net_df = compute_net_sentiment(con, timeline_col)
        loo_stem = f"net_sentiment_leave_one_out{filename_suffix}"
        loo_csv_path, loo_png_path = run_leave_one_out_check(net_df, r, corr_dir, filename_stem=loo_stem)
        all_outputs.append((loo_csv_path, loo_png_path))
        print(f"Leave-one-out check{title_suffix}: full r={r:.3f}, range across drops in {loo_csv_path.name}")
        print(
            f"Ukraine net sentiment vs Taiwan net sentiment{title_suffix}: "
            f"Pearson r = {r:.3f} (n=7 timeline periods)"
        )

    print("\nWrote:")
    for csv_path, png_path in all_outputs:
        print(f"  {png_path}")
        print(f"  {csv_path}")


if __name__ == "__main__":
    main()
