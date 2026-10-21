# Plan for the within-video event test (RQ2b, second version)

Status: DRAFT for approval. Written on 2026-10-02 while the new comments were still being collected, before any of them were looked at, counted by date, or labelled. Once approved, this plan is fixed. Anything done differently later is reported as a change from the plan.

## Why a second test

The first event test (paper, Table 5) compares different videos before and after each event, and several events have fewer than 10 comments on one side. The 80-comment cap in the first scrape removed older comments on 122 videos. We now collect all comments on those 122 videos, so that the same video can be compared before and after an event.

## Data

- All comments on all 582 videos: the existing data for the 460 videos that did not hit the cap, and the new complete collection for the 122 that did.
- Additional videos found by the same searches for every event (see Changes 1 and 2 below).
- Main sample only: comments in Simplified Chinese are removed, as in the paper.
- Only comments posted from 10 days before to 10 days after one of the testable events are labelled. Labelling follows the paper: both models, the researcher decides every disagreement, plus a random check of agreed labels.

## Events

The 25 testable events of the paper (Supplementary Table S2, without the invasion and the two events after the data ends): 6 territorial losses, 11 US-pressure events, 8 Ukrainian successes. No events are added or removed.

## Test

For each event and each video:
- **Before:** comments posted on days −10 to −1. **After:** comments posted on days 0 to +10.
- A video counts for an event only if it was published before day −10 and has **at least 5 comments on each side**.
- For that video: difference = share of comments with the target label after minus before.

For each event: the event's effect is the **mean of its videos' differences**, each video weighted equally, so one very large video cannot decide the result. An event is included only if **at least 3 videos** qualify.

Across events: one-sample t-test of the event effects against zero, two-sided, with the Wilcoxon signed-rank test reported alongside.

The same four event–label pairs as in the paper, all on all videos (Taiwan and Ukraine), corrected together with the Holm method:
1. Territorial loss → disappointed with the US (all videos)
2. Territorial loss → critical of Taiwan (all videos)
3. US pressure → disappointed with the US (all videos)
4. Ukrainian success → supportive of Taiwan (all videos)

## Changes made before any labelling

**Change 1 (2026-10-02): more Taiwan videos around the Ukrainian successes.** After the complete scrape of the 122 capped videos, we counted (by date and script only, with no labels) how many videos meet the rules above. For test 4 (Ukrainian success → supportive of Taiwan, Taiwan videos), only 2 of the 8 events had at least 3 qualifying Taiwan videos, so the test could not be run. Tests 1–3 had 5 of 6 and 9 of 11 events. To make test 4 possible, we collect additional Taiwan videos: for each of the 8 successes, the eight Taiwan search queries of the paper, limited to videos published 10 to 30 days before the event, up to 20 videos per query, with all their comments. The rules of the test do not change.

**Change 2 (2026-10-02): the same searches for every event, and all tests on all videos.** Change 1 collected extra videos for one event group only, and test 4 was the only test limited to Taiwan videos. That restriction came from an earlier internal analysis, where the Taiwan-video version showed the largest change, so it was chosen after seeing results. "Taiwan" and "Ukraine" videos differ only in which search found them, and the test compares each video with itself. We therefore (a) run all four tests on all videos, and (b) collect extra videos in the same way for all 25 events: for each event, the eight Taiwan queries and the two general Ukraine queries of the paper (烏克蘭戰爭, 俄烏戰爭), limited to videos published 10 to 30 days before the event, up to 20 videos per query, with all their comments. The event-named Ukraine queries of the paper are not used, because each belongs to one phase. No labels had been made or seen when this change was made.

## Changes made during labelling

**Change 3 (2026-10-07): off-topic videos removed.** The extra searches (Change 2) returned five videos unrelated to the war or to Taiwan's security. Their titles have Chinese characters, so the title rule kept them:

| Video | Content | Event(s) |
|---|---|---|
| `0PioJ862GHs` | 《奇蹟 Kiseki：Dear to me》EP02, romance drama (GTV) | 2024-03-22 |
| `cUl5QYT3gks` | 開庭時千萬不能說的三個字 (law firm short) | 7 events, 2025-02-14 to 2026-02-10 |
| `xNjQosbP4vo` | 李嫣Bibo 也不是第一次死了 (music video) | 2024-03-22 |
| `iLyMdKFZuxE` | 丁噹 致遠道而來的我們 (music video) | 2024-03-22 |
| `qoUfTB6TaAI` | 鬼罵人 (ghost story) | 2025-11-23 |

They were found during labelling and deleted from both copies of `full_data_with_events.db`, with their `event_test_rows` rows and labels: 236 comments, 362 `event_test_rows` rows, 28 labels (14 BL comments had runs 1–2, all no label). None of the five is in `full_data.db`. They are still in the raw scrape (`yt_jobs/all_events_extra_storage.db`), so they must be left out again if the test data is ever rebuilt. All 25 events still have at least 4 qualifying videos.

A full check of all 102 remaining video titles (list: `labeled_data/events/video_relevance_check.md`) found 10 more unrelated videos, deleted the same way on 2026-10-07: `q2yGisSGc0M` (0050 ETF investing), `fAOVNMlnE-g` (林書豪 basketball), `sgQgkvZxNok` (館長 self-defence clip), `BHVTDM2JpK0` (Nissan crisis), `Xx0NXu9eeM8` (MUJI crisis), `dcSk6fYhIgM` (buying houses in Japan), `ffELHblqlwg` (electric-car sales), `wqw4muUDIQU` (fitness short), `O-xTfVfBjso` (JESS Law music video), `JSQKS3_hgMQ` (retired police dog). Together they had 1,839 main comments in the test. Eleven borderline videos (chips/TSMC, Taiwan identity, Hong Kong, hacking, domestic politics) were kept. All 25 events still have at least 4 qualifying videos. Two Vietnamese comments (ids 29620, 29642, on the 賴清德 video) were also deleted under the language rule; 12,314 main test comments remain.

Four of these videos (ETF, basketball, fitness, police dog; 331 comments, all labelled no label) have been in `full_data.db` since the original scrape. `full_data.db` is not changed. They are now also left out of the paper's main analysis, by a filter in `data_analysis/src/analyze_labels.py` (`OFF_TOPIC_VIDEO_IDS`, 14 videos; see `video_relevance_check_full_data.md`). In the working copy `data_analysis/full_data_with_events.db` they were deleted together with their old rows and labels (that copy now has 24,261 of the 24,592 original rows).

One more video was deleted the same way on 2026-10-07, during batch 7 of the labelling: `3Rn2T10z0uQ` (未來戰場新形態？機器狗大戰無人機, a Chinese robot-dog vs drone short; events 2025-02-14 and 2025-02-19). It had been listed as related in the title check. Deleted: 53 comments, 83 `event_test_rows` rows and 114 labels (38 comments with runs 1–3) from `labeled_data/events/full_data_with_events.db`; 126 comments, 105 `event_test_rows` rows and 255 labels from `data_analysis/full_data_with_events.db`. It is also in `full_data.db` (85 rows), which is not changed. Both events still have at least 5 videos with ≥5 main comments on each side. The 黎智英 Hong Kong video (`3_70nSb3UFA`, borderline) was kept.

## Changes made after the first results

**Change 4 (2026-10-20): event dates corrected.** A check of every event date against dated news sources (full table with sources: `article/EVENT_DATES_CHECK.md`) found seven tested events with a wrong date. Some had been dated by a later news article, one by the Taiwan date of a US event, and two came from a summary page with no event on the given day. Rule for the corrected dates: the local calendar date of the event where it happened; for an event that was secret at first, the date it was first publicly confirmed.

| Old | New | Event |
|---|---|---|
| 2022-09-11 | 2022-09-10 | Kharkiv counteroffensive retakes Izium and Kupiansk |
| 2023-10-01 | 2023-09-30 | US stopgap bill without Ukraine aid |
| 2024-10-15 | 2024-09-18 | Toropets arsenal strike (no event on 15 Oct) |
| 2025-03-15 | 2025-03-13 | Russia claims Sudzha |
| 2025-12-02 | 2025-12-01 | Kremlin claims Pokrovsk |
| 2026-01-25 | 2026-01-29 | Myrnohrad mostly lost (no event on 25 Jan) |
| 2026-02-10 | 2026-02-20 | Southern counteroffensive first confirmed by Ukraine |

Two untested events after the data ends were also changed: 2026-08-15 was removed (no such event found) and 2026-09-02 became 2026-09-15 (Operation Vivaldi first revealed). The number of testable events stays 25 (6, 11 and 8). The rules of the test do not change. Comments posted in the new windows that had no labels are labelled with the same procedure. The extra videos collected for the old dates (Change 2) are kept, and no new searches are run for the new dates.

This change was made after the results with the old dates had been seen (paper, Table 6). It corrects factual errors in the event list and does not depend on those results. The results with the old dates are reported alongside, so readers can compare.

## Reporting

- The result is reported whatever it shows, next to the first test, as a second test of RQ2b.
- The number of events and videos that qualify is reported for each pair, including events dropped by the rules above.
- Anything not in this plan (other windows, other labels, other thresholds) is labelled as exploratory.
