"""Label statistics tables from full_data.db, human labels only.

Human is treated as the final decision (the two AI labelers in the DB are
ignored). Every analysis below is generated twice: once over all
human-labeled rows, and once excluding rows whose text (comment text if
present, else the thread/post text) is detected as Simplified Chinese - the
second set is suffixed `_excl_simplified_zh` so both are available to
compare. "Simplified Chinese" detection uses zhconv.issimp(text, full=True),
which counts characters unique to the Simplification-reform character set
vs. characters unique to Traditional writing (this correctly leaves common
Taiwan-Traditional variant spellings like "台灣" alone - they are not
flagged, since they aren't mainland-simplification-specific characters).

Outputs are saved as a rendered table .png and a raw .csv under project-root
`figures/<category>/` subfolders:

  figures/label_counts/  - label_counts_human, label_counts_ukraine/taiwan:
                            how many rows have each of the 6 labels set,
                            overall and split by topic.
  figures/timeline/       - timeline_breakdown and label_counts_by_timeline
                            (matrix: labels x timeline periods, overall and
                            split by topic), each generated for both the
                            scrape-based `timeline` column and the
                            `message_timeline` column (suffixed
                            `_by_message_date` - see below), plus
                            simplified_zh_share_by_timeline.
  figures/topic/          - topic_breakdown, simplified_zh_share_by_topic.
  figures/correlation/    - label_cooccurrence: 6x6 Pearson-correlation
                            (phi coefficient) heatmap across the labels.
  figures/engagement/     - engagement_by_label: mean/median like count
                            (comment likes if the row has a comment, else
                            thread likes) for rows where each label is True
                            vs. False.

`timeline` vs `message_timeline`: the DB's `timeline` column is the era the
*video* was scraped/searched for, not when people actually commented - a
video tagged "defiance" (2022) can still collect comments in 2026.
`message_timeline` instead buckets each row by its actual message date
(comment date if it has a comment, else thread date) into the same calendar
ranges from the project's timeline.md. `timeline_breakdown` is generated for
both, the message-date version suffixed `_by_message_date`.
"""

import sqlite3
from pathlib import Path

import duckdb
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import chi2_contingency
from zhconv import issimp

SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR.parents[1] / "3_labelled_data" / "full_data.db"
FIGURES_ROOT = SCRIPT_DIR.parents[1] / "5_results" / "other_figures"

DIR_LABEL_COUNTS = FIGURES_ROOT / "label_counts"
DIR_TIMELINE = FIGURES_ROOT / "timeline"
DIR_TOPIC = FIGURES_ROOT / "topic"
DIR_CORRELATION = FIGURES_ROOT / "correlation"
DIR_ENGAGEMENT = FIGURES_ROOT / "engagement"
# Files combining both variant axes (Simplified-Chinese-excluded AND
# message-date timeline) live in one flat top-level folder instead of being
# nested inside each category folder.
DIR_MSG_EXCL = FIGURES_ROOT / "excl_simplified_zh_by_message_date"
DIR_RELIABILITY = FIGURES_ROOT / "reliability"

ALL_DIRS = [
    DIR_LABEL_COUNTS, DIR_TIMELINE, DIR_TOPIC, DIR_CORRELATION, DIR_ENGAGEMENT,
    DIR_MSG_EXCL, DIR_RELIABILITY,
]

# Videos unrelated to the war or Taiwan's security that the keyword searches
# picked up (title check of all 582 videos, 2026-10-07, see
# 2_labelling/video_relevance/main_sample_videos.md). Left out of every analysis
# view; full_data.db itself is not changed.
OFF_TOPIC_VIDEO_IDS = [
    "4gVyYKhuxcc",  # neck massage
    "q2yGisSGc0M",  # 0050 ETF investing
    "2AJFioVk6ys",  # workplace bullying news podcast
    "NPwFcCe4jtI",  # parenting tips
    "fAOVNMlnE-g",  # basketball
    "JSQKS3_hgMQ",  # retired police dog
    "Ts-WuLc2CLQ",  # knee arthritis
    "mkv_8UedJHs",  # highway driving
    "cDmV9T-beG8",  # US green cards
    "DcJc6WWsUmA",  # luggage advert
    "wGC8uG5Gujk",  # HOKA shoes
    "wqw4muUDIQU",  # fitness short
    "YZYJxzMbGxo",  # wedding dowry clip
    "EdizQwrUljs",  # self-defence law
    "3Rn2T10z0uQ",  # robot dogs vs drones (added 2026-10-20, already deleted from the event DBs)
]

LABELS = [
    "critical_ukraine",
    "supportive_ukraine",
    "critical_taiwan",
    "supportive_taiwan",
    "disappointment_with_us",
    "blame_nato_expansion",
]

TIMELINE_ORDER = [
    "defiance",
    "hope",
    "fatigue",
    "anxiety",
    "acceptance",
    "betrayal",
    "self-reliance",
]

TOPIC_BUCKETS = {
    "Ukraine": "('Ukraine', 'Taiwan and Ukraine')",
    "Taiwan": "('Taiwan', 'Taiwan and Ukraine')",
}

# Calendar ranges from the project's timeline.md - (period, start, end), end exclusive.
TIMELINE_DATE_RANGES = [
    ("defiance", "2022-02-01", "2022-12-01"),
    ("hope", "2022-12-01", "2023-06-01"),
    ("fatigue", "2023-06-01", "2024-01-01"),
    ("anxiety", "2024-01-01", "2024-11-01"),
    ("acceptance", "2024-11-01", "2025-02-01"),
    ("betrayal", "2025-02-01", "2025-11-01"),
    ("self-reliance", "2025-11-01", "2026-09-01"),
]

ALL_FALSE_SQL = " AND ".join(f"{label} = 0" for label in LABELS)

HEADER_COLOR = "#4C72B0"
ROW_COLORS = ("white", "#F2F2F2")

NO_SIMPLIFIED_SUFFIX = "_excl_simplified_zh"
NO_SIMPLIFIED_TITLE_SUFFIX = " (excluding Simplified Chinese text)"


def render_table(
    display_df, col_labels, title, out_dir, filename_stem, figsize, col_widths,
    subtitle=None, fontsize=11,
):
    """Render a dataframe of already-formatted strings as a table image."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis("off")

    table = ax.table(
        cellText=display_df.values,
        colLabels=col_labels,
        cellLoc="center",
        loc="center",
        bbox=[0, 0, 1, 1],
        colWidths=col_widths,
    )
    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)

    for (row, _col), cell in table.get_celld().items():
        cell.set_edgecolor("#CCCCCC")
        if row == 0:
            cell.set_text_props(weight="bold", color="white")
            cell.set_facecolor(HEADER_COLOR)
        else:
            cell.set_facecolor(ROW_COLORS[row % 2])

    title_text = title if not subtitle else f"{title}\n{subtitle}"
    ax.set_title(title_text, fontsize=12, pad=14, linespacing=1.8)

    fig.tight_layout()
    png_path = out_dir / f"{filename_stem}.png"
    fig.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return png_path


def connect():
    con = duckdb.connect()
    con.execute("INSTALL sqlite; LOAD sqlite;")
    con.execute(f"ATTACH '{DB_PATH}' AS db (TYPE sqlite)")
    return con


def compute_simplified_chinese_ids(con):
    """Row ids whose comment text (or thread text, if no comment) is Simplified Chinese."""
    df = con.execute(
        "SELECT id, comment_text_original, thread_text_original FROM db.yt_comment_data"
    ).fetchdf()

    def is_simplified(row):
        text = row["comment_text_original"]
        if not isinstance(text, str) or not text.strip():
            text = row["thread_text_original"]
        if not isinstance(text, str) or not text.strip():
            return False
        return issimp(text, full=True) is True

    mask = df.apply(is_simplified, axis=1)
    return df.loc[mask, ["id"]]


def compute_message_dates(db_path):
    """id -> message_date: the row's actual message timestamp (comment date
    if it has a comment, else thread date), as a UTC pandas Timestamp - as
    opposed to the `timeline` column, which reflects the video's
    scrape-assigned era, not when people actually commented.

    thread_published_at/comment_published_at are declared with SQLite's loose
    NUM affinity but actually store ISO text timestamps, which trips up
    DuckDB's sqlite-scanner type inference. Reading them via plain sqlite3
    instead avoids that (and avoids sqlite_all_varchar, which would also turn
    every numeric column elsewhere in the DB into text).
    """
    raw = sqlite3.connect(db_path)
    df = pd.read_sql_query(
        "SELECT id, row_type, thread_published_at, comment_published_at FROM yt_comment_data",
        raw,
    )
    raw.close()

    message_date = df["comment_published_at"].where(
        df["row_type"] == "thread_with_comment", df["thread_published_at"]
    )
    df["message_date"] = pd.to_datetime(message_date, utc=True, errors="coerce")
    return df[["id", "message_date"]]


def compute_message_timeline(db_path):
    """id -> message_timeline: compute_message_dates() bucketed into the
    TIMELINE_DATE_RANGES calendar periods."""
    df = compute_message_dates(db_path)

    df["message_timeline"] = pd.NA
    for period, start, end in TIMELINE_DATE_RANGES:
        mask = (df["message_date"] >= pd.Timestamp(start, tz="UTC")) & (
            df["message_date"] < pd.Timestamp(end, tz="UTC")
        )
        df.loc[mask, "message_timeline"] = period

    return df[["id", "message_timeline"]]


def build_views(con):
    """Create `human_rows` (all human-labeled rows, minus OFF_TOPIC_VIDEO_IDS)
    and `human_rows_excl_simplified_zh` (same, minus Simplified-Chinese rows)."""
    excluded_ids = compute_simplified_chinese_ids(con)
    con.register("excluded_ids", excluded_ids)

    message_timeline = compute_message_timeline(DB_PATH)
    con.register("message_timeline_lookup", message_timeline)
    con.register("off_topic_videos", pd.DataFrame({"video_id": OFF_TOPIC_VIDEO_IDS}))

    con.execute(
        """
        CREATE OR REPLACE TEMP VIEW human_rows AS
        SELECT d.id,
               CAST(d.timeline AS VARCHAR) AS timeline,
               mt.message_timeline AS message_timeline,
               CAST(d.topic AS VARCHAR) AS topic,
               l.critical_ukraine, l.supportive_ukraine, l.critical_taiwan,
               l.supportive_taiwan, l.disappointment_with_us, l.blame_nato_expansion,
               CASE WHEN CAST(d.row_type AS VARCHAR) = 'thread_with_comment'
                    THEN d.comment_like_count ELSE d.thread_like_count END AS engagement,
               d.id IN (SELECT id FROM excluded_ids) AS is_simplified_zh
        FROM db.yt_comment_data d
        JOIN db.yt_comment_label l ON d.id = l.yt_data_id
        LEFT JOIN message_timeline_lookup mt ON d.id = mt.id
        WHERE l.labeler = 'human'
          AND CAST(d.video_id AS VARCHAR) NOT IN (SELECT video_id FROM off_topic_videos)
        """
    )
    con.execute(
        """
        CREATE OR REPLACE TEMP VIEW human_rows_excl_simplified_zh AS
        SELECT * FROM human_rows WHERE id NOT IN (SELECT id FROM excluded_ids)
        """
    )
    return len(excluded_ids)


def total_rows(con, base_view):
    return con.execute(f"SELECT COUNT(*) FROM {base_view}").fetchone()[0]


def analyze_label_counts(con, base_view, total_n, out_dir, filename_stem, title):
    select_cols = ", ".join(f"SUM({label}) AS {label}" for label in LABELS)
    row = con.execute(f"SELECT {select_cols} FROM {base_view}").fetchdf().iloc[0]

    df = pd.DataFrame({"label": LABELS, "count": [int(row[label]) for label in LABELS]})
    df["pct_of_total"] = df["count"] / total_n * 100
    df = df.sort_values("count", ascending=False).reset_index(drop=True)

    csv_path = out_dir / f"{filename_stem}.csv"
    df.to_csv(csv_path, index=False)

    display_df = pd.DataFrame(
        {
            "Label": df["label"],
            "Count": df["count"].map("{:,}".format),
            "% of total": df["pct_of_total"].map("{:.1f}%".format),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=["Label", "Count", "% of total"],
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(8, 4.5),
        col_widths=[0.52, 0.24, 0.24],
    )
    return csv_path, png_path


def analyze_group_breakdown(
    con,
    total_n,
    group_query,
    order,
    group_col_label,
    secondary_col_label,
    title,
    out_dir,
    filename_stem,
    figsize,
    col_widths,
    subtitle=None,
):
    """Shared logic for tables shaped: group, N, % of total, <secondary %>.

    `group_query` must return 3 columns: group, n, n_secondary.
    """
    df = con.execute(group_query).fetchdf()
    df = df.set_index(df.columns[0]).reindex(order).fillna(0).reset_index()
    df.columns = ["group", "n", "n_secondary"]
    df["n"] = df["n"].astype(int)
    df["n_secondary"] = df["n_secondary"].astype(int)
    df["pct_of_total"] = df["n"] / total_n * 100
    df["pct_secondary"] = df.apply(
        lambda r: (r["n_secondary"] / r["n"] * 100) if r["n"] else 0.0, axis=1
    )

    csv_path = out_dir / f"{filename_stem}.csv"
    df.to_csv(csv_path, index=False)

    display_df = pd.DataFrame(
        {
            group_col_label: df["group"],
            "N": df["n"].map("{:,}".format),
            "% of total": df["pct_of_total"].map("{:.1f}%".format),
            secondary_col_label: df["pct_secondary"].map("{:.1f}%".format),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=[group_col_label, "N", "% of total", secondary_col_label],
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=figsize,
        col_widths=col_widths,
        subtitle=subtitle,
    )
    return csv_path, png_path


def analyze_timeline(con, base_view, total_n, out_dir, filename_stem, title, timeline_col="timeline"):
    query = f"""
        SELECT {timeline_col},
               COUNT(*) AS n,
               SUM(CASE WHEN {ALL_FALSE_SQL} THEN 1 ELSE 0 END) AS n_secondary
        FROM {base_view}
        GROUP BY {timeline_col}
    """
    return analyze_group_breakdown(
        con,
        total_n,
        query,
        TIMELINE_ORDER,
        group_col_label="Timeline period",
        secondary_col_label="% all-false",
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(9, 5),
        col_widths=[0.3, 0.23, 0.23, 0.24],
    )


def analyze_topic(con, base_view, total_n, out_dir, filename_stem, title):
    # "Taiwan and Ukraine" rows (matched both searches) are folded into BOTH
    # buckets below - a row can count toward Ukraine and Taiwan simultaneously.
    query = f"""
        SELECT 'Ukraine' AS topic_group,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Ukraine"]} THEN 1 ELSE 0 END) AS n,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Ukraine"]}
                         AND {ALL_FALSE_SQL} THEN 1 ELSE 0 END) AS n_secondary
        FROM {base_view}
        UNION ALL
        SELECT 'Taiwan' AS topic_group,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Taiwan"]} THEN 1 ELSE 0 END) AS n,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Taiwan"]}
                         AND {ALL_FALSE_SQL} THEN 1 ELSE 0 END) AS n_secondary
        FROM {base_view}
    """
    return analyze_group_breakdown(
        con,
        total_n,
        query,
        ["Ukraine", "Taiwan"],
        group_col_label="Topic",
        secondary_col_label="% all-false",
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(8, 2.8),
        col_widths=[0.25, 0.25, 0.25, 0.25],
        subtitle="\"Taiwan and Ukraine\" rows are counted in both buckets, so % of total sums to >100%",
    )


def analyze_simplified_share_by_timeline(con):
    total_n = total_rows(con, "human_rows")
    query = """
        SELECT timeline,
               COUNT(*) AS n,
               SUM(CASE WHEN is_simplified_zh THEN 1 ELSE 0 END) AS n_secondary
        FROM human_rows
        GROUP BY timeline
    """
    return analyze_group_breakdown(
        con,
        total_n,
        query,
        TIMELINE_ORDER,
        group_col_label="Timeline period",
        secondary_col_label="% Simplified Chinese",
        title="Data share and Simplified Chinese text share by timeline period",
        out_dir=DIR_TIMELINE,
        filename_stem="simplified_zh_share_by_timeline",
        figsize=(9, 5),
        col_widths=[0.3, 0.23, 0.23, 0.24],
    )


def analyze_simplified_share_by_topic(con):
    total_n = total_rows(con, "human_rows")
    query = f"""
        SELECT 'Ukraine' AS topic_group,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Ukraine"]} THEN 1 ELSE 0 END) AS n,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Ukraine"]}
                         AND is_simplified_zh THEN 1 ELSE 0 END) AS n_secondary
        FROM human_rows
        UNION ALL
        SELECT 'Taiwan' AS topic_group,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Taiwan"]} THEN 1 ELSE 0 END) AS n,
               SUM(CASE WHEN topic IN {TOPIC_BUCKETS["Taiwan"]}
                         AND is_simplified_zh THEN 1 ELSE 0 END) AS n_secondary
        FROM human_rows
    """
    return analyze_group_breakdown(
        con,
        total_n,
        query,
        ["Ukraine", "Taiwan"],
        group_col_label="Topic",
        secondary_col_label="% Simplified Chinese",
        title="Data share and Simplified Chinese text share by topic",
        out_dir=DIR_TOPIC,
        filename_stem="simplified_zh_share_by_topic",
        figsize=(8, 2.8),
        col_widths=[0.25, 0.25, 0.25, 0.25],
        subtitle="\"Taiwan and Ukraine\" rows are counted in both buckets, so % of total sums to >100%",
    )


def analyze_label_cooccurrence(con, base_view, out_dir, filename_stem, title):
    """6x6 Pearson correlation (phi coefficient, since labels are 0/1) matrix."""
    df = con.execute(f"SELECT {', '.join(LABELS)} FROM {base_view}").fetchdf()
    corr = df.corr()

    csv_path = out_dir / f"{filename_stem}.csv"
    corr.to_csv(csv_path)

    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(LABELS)))
    ax.set_xticklabels(LABELS, rotation=40, ha="right")
    ax.set_yticks(range(len(LABELS)))
    ax.set_yticklabels(LABELS)
    for i in range(len(LABELS)):
        for j in range(len(LABELS)):
            val = corr.values[i, j]
            color = "white" if abs(val) > 0.6 else "black"
            ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=color, fontsize=9)
    ax.set_title(title, fontsize=12, pad=14)
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Pearson correlation (φ coefficient)")

    fig.tight_layout()
    png_path = out_dir / f"{filename_stem}.png"
    fig.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return csv_path, png_path


def analyze_disappointment_taiwan_cooccurrence(con, base_view, out_dir, filename_stem, title):
    """Does disappointment_with_us co-occur, within the SAME comment, with
    critical_taiwan / supportive_taiwan - direct textual evidence for
    "US abandons Ukraine -> Taiwan is next" (rather than just both trending
    together over time, which is a separate, weaker kind of evidence)."""
    df = con.execute(
        f"SELECT disappointment_with_us, critical_taiwan, supportive_taiwan FROM {base_view}"
    ).fetchdf()

    rows = []
    for taiwan_label in ["critical_taiwan", "supportive_taiwan"]:
        with_us = df[df["disappointment_with_us"] == 1]
        without_us = df[df["disappointment_with_us"] == 0]
        rate_with = with_us[taiwan_label].mean() * 100
        rate_without = without_us[taiwan_label].mean() * 100
        overall_rate = df[taiwan_label].mean() * 100

        table = pd.crosstab(df["disappointment_with_us"], df[taiwan_label])
        chi2, p_value, _, _ = chi2_contingency(table)

        p1, p0 = rate_with / 100, rate_without / 100
        odds_with = p1 / (1 - p1) if p1 < 1 else float("inf")
        odds_without = p0 / (1 - p0) if p0 < 1 else float("inf")
        odds_ratio = odds_with / odds_without if odds_without else float("inf")

        rows.append(
            {
                "taiwan_label": taiwan_label,
                "n_disappointment_with_us": len(with_us),
                "rate_when_disappointment_with_us_true": rate_with,
                "rate_when_disappointment_with_us_false": rate_without,
                "overall_rate": overall_rate,
                "odds_ratio": odds_ratio,
                "chi2": chi2,
                "p_value": p_value,
            }
        )
    result_df = pd.DataFrame(rows)

    csv_path = out_dir / f"{filename_stem}.csv"
    result_df.to_csv(csv_path, index=False)

    def fmt_p(p):
        return f"{p:.3g}{'*' if p < 0.05 else ''}"

    display_df = pd.DataFrame(
        {
            "Taiwan label": result_df["taiwan_label"],
            "Disappointed w/ US": result_df["rate_when_disappointment_with_us_true"].map("{:.1f}%".format),
            "Not disappointed": result_df["rate_when_disappointment_with_us_false"].map("{:.1f}%".format),
            "Overall rate": result_df["overall_rate"].map("{:.1f}%".format),
            "Odds ratio": result_df["odds_ratio"].map("{:.2f}x".format),
            "Chi-sq p-value": result_df["p_value"].map(fmt_p),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=list(display_df.columns),
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(12.5, 2.4),
        col_widths=[0.18, 0.19, 0.18, 0.14, 0.13, 0.18],
        subtitle=f"N = {len(df):,} comments; * = p<0.05",
    )
    return csv_path, png_path


def analyze_inter_rater_reliability(con, out_dir, filename_stem, title):
    """Cohen's kappa between the human labeler and each of the two AI
    labelers, per label - a data-quality check on whether human labels are
    consistent with (not necessarily "correct" relative to) the AI labels."""
    pairs = [("claude-opus-5", "Human vs. claude-opus-5"), ("claude-sonnet-5", "Human vs. claude-sonnet-5")]

    def cohen_kappa(a, b):
        n = len(a)
        agreement = (a == b).mean()
        p_a1, p_b1 = a.mean(), b.mean()
        expected = p_a1 * p_b1 + (1 - p_a1) * (1 - p_b1)
        if expected == 1:
            return 1.0
        return (agreement - expected) / (1 - expected)

    human = con.execute(
        f"SELECT yt_data_id, {', '.join(LABELS)} FROM db.yt_comment_label WHERE labeler = 'human' ORDER BY yt_data_id"
    ).fetchdf()

    rows = []
    for ai_labeler, pair_title in pairs:
        ai = con.execute(
            f"SELECT yt_data_id, {', '.join(LABELS)} FROM db.yt_comment_label "
            f"WHERE labeler = '{ai_labeler}' ORDER BY yt_data_id"
        ).fetchdf()
        merged = human.merge(ai, on="yt_data_id", suffixes=("_human", "_ai"))
        for label in LABELS:
            kappa = cohen_kappa(merged[f"{label}_human"], merged[f"{label}_ai"])
            agreement_pct = (merged[f"{label}_human"] == merged[f"{label}_ai"]).mean() * 100
            rows.append(
                {
                    "comparison": pair_title,
                    "label": label,
                    "n": len(merged),
                    "agreement_pct": agreement_pct,
                    "cohen_kappa": kappa,
                }
            )
    df = pd.DataFrame(rows)

    csv_path = out_dir / f"{filename_stem}.csv"
    df.to_csv(csv_path, index=False)

    def kappa_band(k):
        if k < 0:
            return "poor"
        if k < 0.20:
            return "slight"
        if k < 0.40:
            return "fair"
        if k < 0.60:
            return "moderate"
        if k < 0.80:
            return "substantial"
        return "almost perfect"

    display_df = pd.DataFrame(
        {
            "Comparison": df["comparison"],
            "Label": df["label"],
            "Agreement": df["agreement_pct"].map("{:.1f}%".format),
            "Cohen's kappa": df["cohen_kappa"].map("{:.2f}".format),
            "Interpretation": df["cohen_kappa"].map(kappa_band),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=list(display_df.columns),
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(11, 0.9 + 0.4 * len(display_df)),
        col_widths=[0.28, 0.22, 0.15, 0.15, 0.20],
        subtitle=f"N = {len(human):,} comments per comparison",
    )
    return csv_path, png_path


def analyze_engagement_by_label(con, base_view, out_dir, filename_stem, title):
    """Mean/median like count for rows where each label is True vs. False.

    "Likes" = comment_like_count when the row has a comment, else
    thread_like_count (the `engagement` column in the views).
    """
    rows = []
    for label in LABELS:
        r = con.execute(
            f"""
            SELECT {label} AS flag, COUNT(*) AS n,
                   AVG(engagement) AS mean_likes, MEDIAN(engagement) AS median_likes
            FROM {base_view}
            WHERE engagement IS NOT NULL
            GROUP BY {label}
            """
        ).fetchdf()
        true_row = r[r["flag"] == 1]
        false_row = r[r["flag"] == 0]
        rows.append(
            {
                "label": label,
                "n_true": int(true_row["n"].iloc[0]) if len(true_row) else 0,
                "mean_likes_true": float(true_row["mean_likes"].iloc[0]) if len(true_row) else 0.0,
                "median_likes_true": float(true_row["median_likes"].iloc[0]) if len(true_row) else 0.0,
                "mean_likes_false": float(false_row["mean_likes"].iloc[0]) if len(false_row) else 0.0,
                "median_likes_false": float(false_row["median_likes"].iloc[0]) if len(false_row) else 0.0,
            }
        )
    df = pd.DataFrame(rows)

    csv_path = out_dir / f"{filename_stem}.csv"
    df.to_csv(csv_path, index=False)

    display_df = pd.DataFrame(
        {
            "Label": df["label"],
            "N (label=True)": df["n_true"].map("{:,}".format),
            "Mean likes (True)": df["mean_likes_true"].map("{:.1f}".format),
            "Median likes (True)": df["median_likes_true"].map("{:.1f}".format),
            "Mean likes (False)": df["mean_likes_false"].map("{:.1f}".format),
            "Median likes (False)": df["median_likes_false"].map("{:.1f}".format),
        }
    )
    png_path = render_table(
        display_df,
        col_labels=list(display_df.columns),
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(13, 4.5),
        col_widths=[0.22, 0.14, 0.16, 0.16, 0.16, 0.16],
        fontsize=10,
    )
    return csv_path, png_path


def analyze_label_counts_by_topic(con, base_view, out_dir, filename_prefix, title_prefix):
    outputs = []
    for topic_name, sql_in in TOPIC_BUCKETS.items():
        select_cols = ", ".join(
            f"SUM(CASE WHEN topic IN {sql_in} THEN {label} ELSE 0 END) AS {label}"
            for label in LABELS
        )
        row = con.execute(f"SELECT {select_cols} FROM {base_view}").fetchdf().iloc[0]
        n = con.execute(f"SELECT COUNT(*) FROM {base_view} WHERE topic IN {sql_in}").fetchone()[0]

        df = pd.DataFrame({"label": LABELS, "count": [int(row[label]) for label in LABELS]})
        df["pct_of_total"] = df["count"] / n * 100
        df = df.sort_values("count", ascending=False).reset_index(drop=True)

        stem = f"{filename_prefix}_{topic_name.lower()}"
        csv_path = out_dir / f"{stem}.csv"
        df.to_csv(csv_path, index=False)

        display_df = pd.DataFrame(
            {
                "Label": df["label"],
                "Count": df["count"].map("{:,}".format),
                "% of total": df["pct_of_total"].map("{:.1f}%".format),
            }
        )
        png_path = render_table(
            display_df,
            col_labels=["Label", "Count", "% of total"],
            title=f"{title_prefix} — {topic_name} (N={n:,})",
            out_dir=out_dir,
            filename_stem=stem,
            figsize=(8, 4.5),
            col_widths=[0.52, 0.24, 0.24],
        )
        outputs.append((csv_path, png_path))
    return outputs


def _label_counts_by_timeline_matrix(
    con, base_view, title, out_dir, filename_stem, topic_sql_in=None, timeline_col="timeline"
):
    """Shared matrix-table logic: labels x timeline periods."""
    select_cols = ", ".join(f"SUM({label}) AS {label}" for label in LABELS)
    topic_filter = f"WHERE topic IN {topic_sql_in}" if topic_sql_in else ""
    query = f"""
        SELECT {timeline_col} AS timeline, COUNT(*) AS n, {select_cols}
        FROM {base_view}
        {topic_filter}
        GROUP BY {timeline_col}
    """
    df = con.execute(query).fetchdf().set_index("timeline").reindex(TIMELINE_ORDER).fillna(0)
    n_per_period = df["n"]
    counts = df[LABELS]
    pct = counts.div(n_per_period, axis=0).fillna(0) * 100

    label_order = counts.sum().sort_values(ascending=False).index.tolist()

    long_df = (
        counts[label_order]
        .reset_index()
        .melt(id_vars="timeline", var_name="label", value_name="count")
    )
    pct_long = (
        pct[label_order]
        .reset_index()
        .melt(id_vars="timeline", var_name="label", value_name="pct_of_period")
    )
    merged = long_df.merge(pct_long, on=["timeline", "label"])
    csv_path = out_dir / f"{filename_stem}.csv"
    merged.to_csv(csv_path, index=False)

    cell_text = []
    for label in label_order:
        row_cells = []
        for period in TIMELINE_ORDER:
            c = int(counts.loc[period, label])
            p = pct.loc[period, label]
            row_cells.append(f"{c:,}\n({p:.1f}%)")
        cell_text.append(row_cells)
    display_df = pd.DataFrame(cell_text, columns=TIMELINE_ORDER)
    display_df.insert(0, "Label", label_order)

    col_labels = ["Label"] + TIMELINE_ORDER
    col_widths = [0.22] + [0.78 / len(TIMELINE_ORDER)] * len(TIMELINE_ORDER)
    png_path = render_table(
        display_df,
        col_labels=col_labels,
        title=title,
        out_dir=out_dir,
        filename_stem=filename_stem,
        figsize=(16, 5.5),
        col_widths=col_widths,
        fontsize=9,
    )
    return csv_path, png_path


def analyze_label_counts_by_timeline(con, base_view, out_dir, filename_stem, title, timeline_col="timeline"):
    return _label_counts_by_timeline_matrix(
        con, base_view, title, out_dir, filename_stem, timeline_col=timeline_col
    )


def analyze_label_counts_by_timeline_and_topic(
    con, base_view, out_dir, filename_prefix, title_prefix, timeline_col="timeline"
):
    outputs = []
    for topic_name, sql_in in TOPIC_BUCKETS.items():
        outputs.append(
            _label_counts_by_timeline_matrix(
                con,
                base_view,
                title=f"{title_prefix} — {topic_name}",
                out_dir=out_dir,
                filename_stem=f"{filename_prefix}_{topic_name.lower()}",
                topic_sql_in=sql_in,
                timeline_col=timeline_col,
            )
        )
    return outputs


def run_all_analyses(con, base_view, suffix, title_suffix):
    # Message-date + Simplified-Chinese-excluded is a combination of both
    # variant axes, so it gets its own top-level folder instead of cluttering
    # figures/timeline/ directly.
    msg_dir = DIR_MSG_EXCL if suffix == NO_SIMPLIFIED_SUFFIX else DIR_TIMELINE

    total_n = total_rows(con, base_view)
    outputs = [
        analyze_timeline(
            con, base_view, total_n, DIR_TIMELINE, f"timeline_breakdown{suffix}",
            f"Data share and label coverage by timeline period{title_suffix}",
        ),
        analyze_timeline(
            con, base_view, total_n, msg_dir, f"timeline_breakdown_by_message_date{suffix}",
            f"Data share and label coverage by message-date timeline period{title_suffix}",
            timeline_col="message_timeline",
        ),
        analyze_label_counts_by_timeline(
            con, base_view, DIR_TIMELINE, f"label_counts_by_timeline{suffix}",
            f"Counts by label across timeline periods{title_suffix}",
        ),
        analyze_label_counts_by_timeline(
            con, base_view, msg_dir, f"label_counts_by_timeline_by_message_date{suffix}",
            f"Counts by label across message-date timeline periods{title_suffix}",
            timeline_col="message_timeline",
        ),
        *analyze_label_counts_by_timeline_and_topic(
            con, base_view, DIR_TIMELINE, f"label_counts_by_timeline{suffix}",
            f"Counts by label across timeline periods{title_suffix}",
        ),
        *analyze_label_counts_by_timeline_and_topic(
            con, base_view, msg_dir, f"label_counts_by_timeline_by_message_date{suffix}",
            f"Counts by label across message-date timeline periods{title_suffix}",
            timeline_col="message_timeline",
        ),
        analyze_label_cooccurrence(
            con, base_view, DIR_CORRELATION, f"label_cooccurrence{suffix}",
            f"Label co-occurrence (Pearson correlation, N={total_n:,}){title_suffix}",
        ),
        analyze_disappointment_taiwan_cooccurrence(
            con, base_view, DIR_CORRELATION, f"disappointment_taiwan_cooccurrence{suffix}",
            f"Does US-disappointment co-occur with Taiwan views in the SAME comment?{title_suffix}",
        ),
        # label_counts_human/ukraine/taiwan, topic_breakdown, and
        # engagement_by_label are skipped for now (not needed right now) -
        # existing files on disk are left as-is; see analyze_label_counts,
        # analyze_topic, analyze_label_counts_by_topic,
        # analyze_engagement_by_label to re-enable.
    ]
    return total_n, outputs


def main():
    for d in ALL_DIRS:
        d.mkdir(parents=True, exist_ok=True)
    con = connect()
    n_excluded = build_views(con)

    print(f"Rows detected as Simplified Chinese text (comment, else thread): {n_excluded:,}")

    all_outputs = []
    for base_view, suffix, title_suffix in [
        ("human_rows", "", ""),
        ("human_rows_excl_simplified_zh", NO_SIMPLIFIED_SUFFIX, NO_SIMPLIFIED_TITLE_SUFFIX),
    ]:
        total_n, outputs = run_all_analyses(con, base_view, suffix, title_suffix)
        print(f"\n{base_view} (N={total_n:,}):")
        all_outputs.extend(outputs)

    all_outputs.append(analyze_simplified_share_by_timeline(con))
    # analyze_simplified_share_by_topic skipped for now (topic not needed right now)

    all_outputs.append(
        analyze_inter_rater_reliability(
            con, DIR_RELIABILITY, "inter_rater_reliability",
            "Human vs. AI labeler agreement (Cohen's kappa)",
        )
    )

    print("\nWrote:")
    for csv_path, png_path in all_outputs:
        print(f"  {png_path}")
        print(f"  {csv_path}")


if __name__ == "__main__":
    main()
