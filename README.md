# Trust in the United States and confidence in self-defence: Taiwanese YouTube comments on the war in Ukraine, 2022–2026

Data, labels and code for the paper. Everything needed to check or rerun the results is in this repository.

- **Scraper** used to collect the comments: https://anonymous.4open.science/r/youtube-scraper-88F7/

---

## Reproduce the paper's numbers (about 2 minutes)

Needs [uv](https://docs.astral.sh/uv/) and Python 3.13 or later.

```bash
cd 4_analysis
uv sync
uv run python src/paper_checks.py        # Tables 3–5, S3, RQ1, RQ2a
uv run python src/within_video_test.py   # Table 6
uv run python src/paper_figures.py       # Figures 1–3
```

The scripts only read the databases. They write CSVs to `5_results/tables/` and figures to `5_results/figures/`. The CSVs already in those folders are the ones the paper reports, so a rerun should give identical files (`git diff` shows no change).

---

## Where to find each part of the paper

| In the paper | File |
|---|---|
| Phases of the war (Table 1) | `1_data_collection/phases.md` |
| Search queries (Supp. Table S1) | `1_data_collection/configs/main_sample/` |
| Label definitions and instructions (Table 2, Supp. Note S1) | `2_labelling/labeling_prompt.md` |
| Every comment where the two models disagreed, with the researcher's decision | `2_labelling/disagreements/` |
| Random check of comments where the models agreed | `2_labelling/label_checks/` |
| Videos removed as unrelated | `2_labelling/video_relevance/` |
| All comments with all labels | `3_labelled_data/full_data.db` (main sample), `3_labelled_data/full_data_with_events.db` (second event test) |
| Agreement between the models (Table 3) | `5_results/tables/labelling_agreement.csv` |
| RQ1: co-occurrence (Table 4, Fig. 2) | `5_results/tables/cooccurrence.csv`, `cooccurrence_logit.csv` |
| RQ2a: phases (Fig. 3) | `5_results/tables/h1_correlation.csv`, `h1_net_sentiment_*.csv` |
| Events (Supp. Table S2) | `4_analysis/events.csv` |
| RQ2b first test (Table 5) | `5_results/tables/event_study_corrected_10d.csv` |
| Robustness checks (Supp. Table S3) | `5_results/tables/event_study_corrected_20d.csv`, `event_study_merged_us_pressure.csv` |
| RQ2b second test, the same video before and after (Table 6) | `5_results/tables/within_video_test.csv` (per event: `within_video_events.csv`, per video: `within_video_videos.csv`) |
| Plan of the second test, written before its comments were labelled | `4_analysis/EVENT_TEST_PLAN.md` |
| Check of the event dates, with sources | `4_analysis/EVENT_DATES_CHECK.md` |
| Results with the original event dates (Supp. Table S4) | `5_results/tables/old_dates/` |
| Figures 1–3 | `5_results/figures/` (PDF and PNG) |

---

## How the data was made

```
1. Scrape           2. Export + merge          3. Label                  4. Analyse            5. Results
YAML configs   →    one table per topic   →    2 models + researcher →   Python scripts   →    CSVs + figures
(1_data_collection)  (1_data_collection)        (2_labelling,             (4_analysis)          (5_results)
                                                 3_labelled_data)
```

### 1. Scrape (`1_data_collection/`)

Each YAML file is one job for the scraper. A job lists search queries with a date range, and limits on videos, threads and comments.

- `configs/main_sample/ukraine/`: 7 jobs, one per phase, Ukraine queries.
- `configs/main_sample/taiwan/`: 7 jobs, one per phase, Taiwan queries. All seven write to one shared state file.
- `configs/event_test/`: the extra data for the second event test.
  - `capped_videos_all_comments.yaml`: all comments on the 122 videos that hit the comment limit. This uses the scraper's `video_ids` input.
  - `success_events_taiwan.yaml` and `all_events_extra.yaml`: videos published 10–30 days before each testable event (original event dates).
- `raw/`: the scraper's SQLite state files, as left by these jobs (tables `jobs`, `tasks`, `videos`, `threads`, `comments`).

Run a job with:

```bash
cp .env.example .env    # add your own YouTube Data API key
yt-scraper run -f yaml < configs/main_sample/ukraine/ukraine_hope_2022_2023.yaml
```

A new scrape will not return exactly the same comments, because YouTube content changes over time. Use the stored databases to check the paper.

### 2. Export and merge (`1_data_collection/exports/`, `1_data_collection/merge/`)

1. `exports/<topic>/<phase>/export_*.sql` turns one job's state file into one flat table, `yt_comment_data`, with one row per comment. `SCRAPER_JOB_ID.txt` gives the job.
2. `merge/concatenate_ukraine.sql` and `merge/concatenate_taiwan.sql` join the seven phases of each topic: `*_full_before_language_filter.db`.
3. Language filter: whole videos whose title has no Chinese characters were removed (28 videos, 1,585 rows). Result: `merge/ukraine_full.db` and `merge/taiwan_full.db`.
4. `merge/concatenate.sql` joins the two topics into `full_data.db`. `merge/label_table.sql` adds the `id` column and the empty label table.

Each row is either a top-level comment (`row_type = 'thread_only'`, text in `thread_text_original`) or a reply (`row_type = 'thread_with_comment'`, text in `comment_text_original`). For a reply, the parent comment is repeated on the row only as context. It is labelled on its own row.

### 3. Label (`2_labelling/`, `3_labelled_data/`)

Each comment has six yes/no labels: `critical_ukraine`, `supportive_ukraine`, `critical_taiwan`, `supportive_taiwan`, `disappointment_with_us`, `blame_nato_expansion`.

Labels are in the table `yt_comment_label`, one row per comment per run:

| `run_number` | `labeler` | |
|---|---|---|
| 1 | `claude-sonnet-5` | model |
| 2 | `claude-opus-5` | model |
| 3 | `human` | **final labels, used in all analyses** |

Where the two models agreed on all six labels, run 3 copies them. Where they disagreed, the researcher decided all six labels. These decisions, with the comment and a short reason, are in `2_labelling/disagreements/` (main sample: 68 files by id range plus `label_disagreements_summary.md`; event test: 24 files).

- `labeling_prompt.md` is the final version of the instructions. Calibration notes were added during labelling, so `labeling_prompt_first_version.md` shows the version used for the first batches.
- `label_checks/`: the random samples of 300 agreed comments from each dataset, with the researcher's judgement of each label.
- `3_labelled_data/final_labels_main_sample.csv` and `final_labels_event_test.csv` hold the final labels with video, thread and comment IDs, for readers who do not use SQLite.

The second database, `full_data_with_events.db`, has the comments used in the second event test. Its table `event_test_rows` (also as `event_test_rows.csv`) lists, for each comment, the event, the event group and the side (`before` or `after`).

### 4. Analyse (`4_analysis/`)

| Script | What it does |
|---|---|
| `src/paper_checks.py` | Model agreement, RQ1, RQ2a, RQ2b first test and its robustness checks |
| `src/within_video_test.py` | RQ2b second test |
| `src/paper_figures.py` | Figures 1–3 |
| `src/analyze_labels.py` | Shared helpers: builds the analysed sample (see below) |
| `src/event_study_analysis.py`, `src/correlation_by_timeline.py` | Shared helpers for the event and phase tests |

The analysed sample is built in `analyze_labels.py` without changing the database:
- comments in Simplified Chinese are removed (`compute_simplified_chinese_ids`)
- comments on 15 unrelated videos are removed (`OFF_TOPIC_VIDEO_IDS`)

This leaves 15,953 comments. `within_video_test.py` also leaves out 5 comments in other languages (`FOREIGN_LANGUAGE_IDS`).

---

## Folder map

```
1_data_collection/   scrape configs, raw scraper databases, export and merge steps
2_labelling/         labelling instructions, disagreement decisions, label checks, removed videos
3_labelled_data/     the two labelled databases (+ CSV copies of the final labels)
4_analysis/          Python code, event list, test plan, event date check
5_results/           tables (CSV) and figures behind the paper
```

`EVENT_TEST_PLAN.md`, `EVENT_DATES_CHECK.md` and `events.md` are working notes kept as they were written. File paths in them refer to the original working folders, not to this layout.

---

## Note on the data

The databases contain public YouTube comments as they were collected, including comment text and author display names. They are shared so that the labels and results can be checked. Please do not use them to identify or contact commenters.
