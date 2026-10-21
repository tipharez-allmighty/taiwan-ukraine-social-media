# Event dates: check of all 28 events (2026-10-20)

**Rule for day 0:** the local calendar date on which the event happened, where it happened. If the event was not public when it happened (a secret operation), the date it was first publicly confirmed. Each date has a source that reports the event on that day.

Why this check: `data_analysis/events.csv` had dates taken from summary pages or from the date of a later news article. Six tested events had a wrong date. The fixes below are a change from `EVENT_TEST_PLAN.md` ("no events are added or removed") and are reported as such.

"Tested" = used in the event tests (Tables 5–6). Last column = comments that need new labels in the within-video test if the date changes (counted read-only from the scrape DBs; the same count reproduces the current test within a few comments).

## Changed dates

| Old | **New** | Group | Event | Source for the new date | Why | New labels |
|---|---|---|---|---|---|---|
| 2022-09-11 | **2022-09-10** | success | Kharkiv counteroffensive retakes Izium and Kupiansk | [NPR/GPB, 2022-09-10](https://www.gpb.org/news/2022/09/10/russian-forces-withdraw-the-kharkiv-region-ukraine-pushes-counteroffensive) | Russia withdrew and Ukraine entered Izium and Kupiansk on 10 Sep | 56 |
| 2023-10-01 | **2023-09-30** | US pressure | Congress passes stopgap bill without Ukraine aid | [NPR, 2023-09-30](https://www.npr.org/2023/09/30/1202839419/house-and-senate-race-to-find-agreement-ahead-shutdown-deadline) | Bill unveiled and passed on Saturday 30 Sep (US). 1 Oct was the Taiwan date | 110 |
| 2024-10-15 | **2024-09-18** | success | Drone strike destroys Toropets arsenal (largest deep strike on Russian ammunition) | [Kyiv Post](https://kyivpost.com/post/40216); [Novaya Gazeta Europe, 2024-09-19](https://novayagazeta.eu/en/articles/2024/09/19/seismic-event-en) | Old date came from a summary page; no event on 15 Oct. Tikhoretsk followed on 21 Sep | 119 |
| 2025-03-15 | **2025-03-13** | loss | Russia claims recapture of Sudzha (Kursk) | [Kyiv Independent](https://kyivindependent.com/russia-claims-to-retake-sudzha-kyiv-hasnt-confirmed/); [Novaya Gazeta Europe, 2025-03-13](https://novayagazeta.eu/en/articles/2025/03/13/putin-makes-surprise-visit-to-russias-kursk-region-as-defence-ministry-claims-recapture-of-sudzha-en-news) | 15 Mar was the date of the Euronews article, not the claim | 695 |
| 2025-12-02 | **2025-12-01** | loss | Kremlin claims capture of Pokrovsk | [Al Jazeera](https://aljazeera.com/news/2025/12/2/russia-says-it-captured-pokrovsk-a-key-logistics-hub-in-eastern-ukraine); [bne IntelliNews](https://new.intellinews.com/articles/russian-military-claims-capture-of-pokrovsk-and-vovchansk-but-ukraine-says-fighting-continues-414489) | Announced Monday 1 Dec after Gerasimov's report to Putin on 30 Nov | 7 |
| 2026-01-25 | **2026-01-29** | loss | Myrnohrad mostly lost to Russian forces | [Euromaidan Press, 2026-01-29](https://euromaidanpress.com/2026/01/29/russia-controls-most-of-myrnohrad-and-moves-its-commanders-into-the-city-ukrainian-marine-officer-says-maps/) | Nothing happened on 25 Jan. Judgement call: the city was lost over weeks; 29 Jan is the first report that most of it was Russian (ISW assessed it taken on 4 Feb) | 16 |
| 2026-02-10 | **2026-02-20 (proposed)** | success | Ukraine confirms southern counteroffensive retook about 300 km² | [Kyiv Independent (Zelensky to AFP), 2026-02-21](https://kyivindependent.com/ukraine-liberates-300-square-kilometers-in-southern-counteroffensive-zelensky-tells-afp/); [Euromaidan Press, 2026-02-22](https://euromaidanpress.com/2026/02/22/ukraines-air-assault-forces-officially-reveal-southern-counteroffensive-that-reclaimed-300-km%C2%B2-and-eight-settlements/) | Secret operation, began 29 Jan ([Euromaidan Press](https://euromaidanpress.com/2026/08/14/southeastern-counteroffensive-2/)). Reports on 9–11 Feb were Russian claims, denied by Ukraine and judged likely invented by ISW ([Euromaidan Press, 2026-02-10](https://euromaidanpress.com/2026/02/10/russia-likely-invented-a-ukrainian-counteroffensive-near-zaporizhzhia-to-cover-up-its-own-fake-advance-reports-isw-says/)). First Ukrainian confirmation: 20 Feb | 108 |

**Total new labels: about 1,110.**

## Not tested (after the data ends on 11 Aug 2026)

| Old | New | Event | Source | Note |
|---|---|---|---|---|
| 2026-08-15 | **remove** | "Jet-powered drone mass strike campaign" | none found | No such Ukrainian event found; the jet-drone reports of Aug 2026 are about Russian drones ([Al Jazeera](https://www.aljazeera.com/news/2026/9/4/russias-jet-powered-drones-overwhelm-ukraine-killing-dozens)) |
| 2026-09-02 | **2026-09-15** | Operation Vivaldi near Lyman first revealed (75 km² cleared) | [Ukrainska Pravda, 2026-09-15](https://pravda.com.ua/eng/news/2026/09/15/8053480); [Meduza, 2026-09-16](https://meduza.io/en/feature/2026/09/16/ukraine-s-third-army-corps-command-reveals-a-months-old-counteroffensive-in-northern-donetsk-region-its-ultimate-goal-remains-unknown) | Secret operation (began 22 May); old source was a YouTube video and overstated the gains |

## Unchanged dates (checked)

| Date | Group | Event | Source | Note |
|---|---|---|---|---|
| 2022-02-24 | loss (not tested) | Full-scale invasion | [Meduza, 2022-02-24](https://meduza.io/amp/en/news/2022/02/24/putin-announces-start-of-military-operation-in-eastern-ukraine) | Putin's address 5:30 Moscow time |
| 2022-04-14 | success | Moskva sinks | [NHPR (NPR), 2022-04-14](https://www.nhpr.org/2022-04-14/russia-ukraine-war-what-happened-today-april-14); [Kyiv Post](https://kyivpost.com/ukraine-politics/russia-confirms-its-flagship-black-sea-vessel-has-sunk.html) | Hit late 13 Apr; Russia confirmed the sinking 14 Apr |
| 2022-05-31 | US pressure | Biden NYT op-ed | [NYT, 2022-05-31](https://www.nytimes.com/2022/05/31/opinion/biden-ukraine-russia.html); [American Presidency Project](https://www.presidency.ucsb.edu/documents/op-ed-the-president-the-new-york-times) | Online 31 May (US), in print 1 Jun |
| 2022-11-09 | US pressure | Milley urges a window for negotiation | [Euromaidan Press, 2022-11-10](https://euromaidanpress.com/2022/11/10/us-top-general-sees-window-of-opportunity-for-russia-ukraine-negotiations-ahead-of-winter/); [The Intercept](https://theintercept.com/2022/11/30/ukraine-war-weapons-ndaa/) | Economic Club of New York, Wednesday 9 Nov |
| 2022-11-11 | success | Kherson liberated | [NPR, 2022-11-11](https://www.npr.org/2022/11/11/1135995012/ukrainian-troops-enter-kherson-russia-withdrawal-ukraine) | |
| 2023-05-20 | loss | Wagner and Russian MoD claim Bakhmut | [Novaya Gazeta Europe, 2023-05-20](https://novayagazeta.eu/en/articles/2023/05/20/wagners-prigozhin-claims-bakhmut-is-captured-in-its-entirety-en-news); [Meduza, 2023-05-20](https://meduza.io/en/news/2023/05/20/wagner-founder-prigozhin-says-his-troops-have-taken-bakhmut-kyiv-denies-it) | |
| 2023-06-04 | success | 2023 counteroffensive begins | [Al Jazeera, 2023-06-05](https://www.aljazeera.com/news/2023/6/5/russia-claims-to-have-thwarted-major-ukraine-attack); [ISW, 2023-06-05](https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-june-5-2023) | Russian MoD reported the attack on 4 Jun; ISW and Shoigu date the start to 4 Jun |
| 2023-11-01 | loss | Zaluzhny: war has reached a stalemate | [The Economist, 2023-11-01](https://www.economist.com/europe/2023/11/01/ukraines-commander-in-chief-on-the-breakthrough-he-needs) | |
| 2024-02-17 | loss | Withdrawal from Avdiivka | [Ukrainska Pravda, 2024-02-17](https://www.pravda.com.ua/eng/news/2024/02/17/7442285) | Syrskyi announced it early on 17 Feb (Kyiv); AP dated 16 Feb (US time) |
| 2024-03-22 | US pressure | FT: US urged Ukraine to stop hitting Russian refineries | [Euromaidan Press, 2024-03-22](https://euromaidanpress.com/2024/03/22/ft-sources-us-urged-ukraine-to-halt-strikes-on-russian-oil-refineries/) | |
| 2024-08-06 | success | Kursk incursion begins | [Al Jazeera](https://www.aljazeera.com/news/2024/8/13/russia-ukraine-war-list-of-key-events-day-900) (Reuters timeline: 6 Aug) | |
| 2025-02-14 | US pressure | Vance Munich speech | [Semafor, 2025-02-14](https://www.semafor.com/article/02/14/2025/jd-vance-uses-munich-security-speech-to-attack-europe-on-immigration-free-speech) | |
| 2025-02-19 | US pressure | Trump calls Zelensky "a dictator without elections" | [Eurointegration, 2025-02-19](https://www.eurointegration.com.ua/eng/news/2025/02/19/7205402/) | |
| 2025-02-28 | US pressure | Oval Office clash | [ABC News](https://abcnews.go.com/news/story/key-takeaways-tempers-flare-trump-vance-confront-ukraines-119299758); [IOL, 2025-02-28](https://iol.co.za/news/world/2025-02-28-trump-and-zelensky-in-extraordinary-oval-office-shouting-match/) | |
| 2025-03-03 | US pressure | US pauses military aid | [Bloomberg, 2025-03-03](https://bloomberg.com/news/articles/2025-03-03/trump-pauses-military-aid-to-ukraine-after-clash-with-zelenskiy) | Reported in the evening of 3 Mar (US) |
| 2025-06-01 | success | Operation Spiderweb | [Kyiv Post](https://www.kyivpost.com/amp/post/53749); [Janes](https://www.janes.com/osint-insights/defence-and-national-security-analysis/operation-spiderweb-ukraine-covert-drone-strike-inside-russia) | |
| 2025-08-15 | US pressure | Anchorage summit, no ceasefire | [Foreign Policy, 2025-08-15](https://foreignpolicy.com/2025/08/15/trump-putin-summit-press-conference-transcript-full-text-read/) | |
| 2025-11-23 | US pressure | Geneva talks on the 28-point plan | [Boise State Public Radio (AP), 2025-11-23](https://www.boisestatepublicradio.org/2025-11-23/rubio-set-to-meet-with-ukraine-european-allies-in-geneva-over-us-peace-plan) | |
| 2026-07-05 | US pressure | Vance calls 2023 counteroffensive a "strategic and tactical disaster" | [Ukrainska Pravda, 2026-07-05](https://www.pravda.com.ua/eng/news/2026/07/05/8042501/) | |

## Open question for the researcher

- **Southern counteroffensive (2026):** day 0 = **20 Feb** (first Ukrainian confirmation, proposed above, 108 labels) or **11 Feb** (first wide reports, which were Russian claims; 34 labels). The rule above gives 20 Feb.
