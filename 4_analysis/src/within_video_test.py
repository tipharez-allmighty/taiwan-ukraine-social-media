"""Within-video event test (RQ2b, second version), as fixed in
4_analysis/EVENT_TEST_PLAN.md.

Data: 3_labelled_data/full_data_with_events.db (opened read-only), main
sample only (simplified = 0), final labels = run 3 ('human'). Video publish
dates come from the raw scrape DBs in 1_data_collection/ (also read-only).

  - before = days -10..-1, after = days 0..+10 (UTC calendar days, already
    stored as event_test_rows.side)
  - a video counts for an event if published before day -10 and it has at
    least 5 comments on each side; its difference = share after - share before
  - event effect = mean of its videos' differences (each video weighted
    equally); an event needs at least 3 videos
  - across events: one-sample t-test against 0 (two-sided) + Wilcoxon
    signed-rank; Holm over the 4 tests

Output: printed tables + CSVs in 5_results/tables/within_video_*.csv.
"""

import sqlite3
from pathlib import Path

import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "3_labelled_data" / "full_data_with_events.db"
SCRAPE_DIR = ROOT / "1_data_collection"
OUT_DIR = ROOT / "5_results" / "tables"

FINAL_RUN = 3
# Foreign-language comments found during labelling (plan: leave out).
FOREIGN_LANGUAGE_IDS = [34744, 34746, 34747, 34756, 31248]
MIN_PER_SIDE = 5
MIN_VIDEOS = 3
WINDOW_DAYS = 10

TESTS = [
    ("loss", "disappointment_with_us"),
    ("loss", "critical_taiwan"),
    ("us_pressure", "disappointment_with_us"),
    ("success", "supportive_taiwan"),
]


def connect_read_only(path):
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def load_rows():
    """One row per (comment, event) in the main sample, with its final labels."""
    con = connect_read_only(DB_PATH)
    df = pd.read_sql_query(
        f"""
        SELECT e.yt_data_id, e.event_date, e.event_group, e.side, d.video_id,
               l.disappointment_with_us, l.critical_taiwan, l.supportive_taiwan
        FROM event_test_rows e
        JOIN yt_comment_data d ON d.id = e.yt_data_id
        JOIN yt_comment_label l ON l.yt_data_id = e.yt_data_id AND l.run_number = {FINAL_RUN}
        WHERE e.simplified = 0
        """,
        con,
    )
    con.close()
    return df[~df["yt_data_id"].isin(FOREIGN_LANGUAGE_IDS)]


def load_publish_dates():
    """video_id -> publish date (UTC), from every raw scrape DB with a videos table."""
    rows = []
    for path in sorted(SCRAPE_DIR.rglob("*.db")):
        con = connect_read_only(path)
        if con.execute("SELECT 1 FROM sqlite_master WHERE name = 'videos'").fetchone():
            rows += con.execute("SELECT id, published_at FROM videos").fetchall()
        con.close()
    pub = pd.DataFrame(rows, columns=["video_id", "published_at"]).drop_duplicates("video_id")
    pub["published_at"] = pd.to_datetime(pub["published_at"], utc=True, format="ISO8601")
    return pub.set_index("video_id")["published_at"]


def video_differences(df, pub, group, label):
    """Per (event, video): comment counts, label shares and after - before."""
    sub = df[df["event_group"] == group]
    g = sub.groupby(["event_date", "video_id", "side"])[label].agg(["size", "mean"]).unstack("side")
    v = pd.DataFrame(
        {
            "n_before": g[("size", "before")],
            "n_after": g[("size", "after")],
            "share_before": g[("mean", "before")] * 100,
            "share_after": g[("mean", "after")] * 100,
        }
    ).fillna({"n_before": 0, "n_after": 0}).reset_index()
    v["published_at"] = v["video_id"].map(pub)
    window_start = pd.to_datetime(v["event_date"]).dt.tz_localize("UTC") - pd.Timedelta(days=WINDOW_DAYS)
    v["published_before_window"] = v["published_at"] < window_start
    v["qualifies"] = (
        v["published_before_window"] & (v["n_before"] >= MIN_PER_SIDE) & (v["n_after"] >= MIN_PER_SIDE)
    )
    v["difference"] = v["share_after"] - v["share_before"]
    v.insert(0, "label", label)
    v.insert(0, "event_group", group)
    return v


def event_effects(v, all_dates):
    q = v[v["qualifies"]]
    e = q.groupby("event_date").agg(
        n_videos=("video_id", "size"),
        n_comments=("n_before", "sum"),
        share_before=("share_before", "mean"),
        share_after=("share_after", "mean"),
        effect=("difference", "mean"),
    )
    e["n_comments"] += q.groupby("event_date")["n_after"].sum()
    e = e.reindex(all_dates).fillna({"n_videos": 0})
    e["included"] = e["n_videos"] >= MIN_VIDEOS
    e.index.name = "event_date"
    e = e.reset_index()
    e.insert(0, "label", v["label"].iloc[0])
    e.insert(0, "event_group", v["event_group"].iloc[0])
    return e


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df = load_rows()
    pub = load_publish_dates()
    missing = set(df["video_id"]) - set(pub.index)
    assert not missing, f"no publish date for {sorted(missing)}"

    videos, events, summary = [], [], []
    for group, label in TESTS:
        all_dates = sorted(df.loc[df["event_group"] == group, "event_date"].unique())
        v = video_differences(df, pub, group, label)
        e = event_effects(v, all_dates)
        videos.append(v)
        events.append(e)

        inc = e[e["included"]]
        t = stats.ttest_1samp(inc["effect"], 0)
        wil = stats.wilcoxon(inc["effect"]).pvalue
        summary.append(
            {
                "event_group": group,
                "label": label,
                "n_events_total": len(e),
                "n_events": len(inc),
                "n_videos": int(inc["n_videos"].sum()),
                "n_distinct_videos": v.loc[v["qualifies"] & v["event_date"].isin(inc["event_date"]), "video_id"].nunique(),
                "n_comments": int(inc["n_comments"].sum()),
                "share_before": inc["share_before"].mean(),
                "share_after": inc["share_after"].mean(),
                "mean_effect": inc["effect"].mean(),
                "sd_effect": inc["effect"].std(),
                "n_positive": int((inc["effect"] > 0).sum()),
                "t": t.statistic,
                "df": len(inc) - 1,
                "t_p": t.pvalue,
                "wilcoxon_p": wil,
            }
        )

    res = pd.DataFrame(summary)
    res["t_p_holm"] = multipletests(res["t_p"], method="holm")[1]
    res["wilcoxon_p_holm"] = multipletests(res["wilcoxon_p"], method="holm")[1]

    pd.set_option("display.float_format", "{:.3f}".format)
    pd.set_option("display.width", 200)
    ev = pd.concat(events, ignore_index=True)
    print(ev.to_string(index=False))
    print()
    print(res.to_string(index=False))

    pd.concat(videos, ignore_index=True).to_csv(OUT_DIR / "within_video_videos.csv", index=False)
    ev.to_csv(OUT_DIR / "within_video_events.csv", index=False)
    res.to_csv(OUT_DIR / "within_video_test.csv", index=False)
    print(f"\nCSVs written to {OUT_DIR}")


if __name__ == "__main__":
    main()
