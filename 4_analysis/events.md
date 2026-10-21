# Ukraine War Event Dataset & Sentiment Timeline (2022–2026)

> **Outdated (2026-10-20):** seven dates and two events in section 2 were wrong. `events.csv` is corrected; see `article/EVENT_DATES_CHECK.md` for every date with its source.

## 1. Qualitative Sentiment & Mood Timeline

| Date Range | Primary Mood | Key Driver of Sentiment | Primary Sources / Reference Context |
| :--- | :--- | :--- | :--- |
| **Feb 2022 – Nov 2022** | **Defiance** | Invasion converts into intense national unity; successful defense of Kyiv and lightning liberation of Kharkiv and Kherson. | Defense of Kyiv, Kharkiv Counteroffensive, Kherson Liberation |
| **Dec 2022 – May 2023** | **Hope** | Endurance through the first winter of massive energy grid blackouts; high anticipation of heavy Western armor arriving. | Winter Grid Attacks, Battle of Bakhmut, Western Armor Commitments |
| **Jun 2023 – Dec 2023** | **Fatigue** | Deep disappointment as the summer counteroffensive stalls against heavily mined Russian defense lines (Surovikin Line). | 2023 Counteroffensive, Zaluzhny *Economist* Assessment |
| **Jan 2024 – Oct 2024** | **Anxiety** | Critical ammunition shortages driven by U.S. congressional delays; loss of Avdiivka; exhausting war of attrition. | US Congressional Aid Freeze, Fall of Avdiivka, Kharkiv Border Offensive |
| **Nov 2024 – Jan 2025** | **Acceptance** | Escalating Russian strikes on energy infrastructure; Kursk offensive boost fades; growing openness to pragmatic diplomatic freeze. | Kursk Incursion Stabilization, Winter Infrastructure Attacks, Diplomatic Shifts |
| **Feb 2025 – Oct 2025** | **Betrayal & Despair** | Harsh Trump-Zelensky Oval Office clash; freezing of U.S. aid; rejection of long-range weapons; U.S. public approval drops to ~7% within Ukraine. | Vance Munich Speech, US Intelligence & Aid Freeze, Oval Office Clash |
| **Nov 2025 – Aug 2026** | **Self-Reliance** | Acceptance of a long conflict; pivot to European financial backing and native long-range drone/missile campaigns; over 60% prepared to endure. | "Operation Spiderweb", Pokrovsk Defensive Line, Domestic Defense Scale-Up |

---

## 2. Quantitative Event Dataset (`events.csv`)

| Date | Category | Hypothesis | Valence | Event Description | Primary Source / Reference Link |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **2022-02-24** | `territorial_loss` | H1 | -1 | Full-scale Russian invasion begins; major initial territorial losses in South and East | [Wikipedia: Invasion of Ukraine](https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine) |
| **2022-04-14** | `military_tech_win` | H3 | 1 | Sinking of the Russian flagship *Moskva* via domestic Neptune anti-ship missiles | [Wikipedia: Sinking of the Moskva](https://en.wikipedia.org/wiki/Sinking_of_the_Moskva) |
| **2022-05-31** | `us_pressure_statement` | H2 | -1 | Biden NYT Op-Ed capping long-range weapon supply & prohibiting strikes inside Russia | [NYT: Biden Op-Ed](https://www.nytimes.com/2022/05/31/opinion/biden-ukraine-russia.html) |
| **2022-09-11** | `military_tech_win` | H3 | 1 | Successful Kharkiv counteroffensive liberates major territory (Izyum, Kupiansk) | [Wikipedia: Kharkiv Counteroffensive](https://en.wikipedia.org/wiki/2022_Kharkiv_counteroffensive) |
| **2022-11-09** | `us_pressure_statement` | H2 | -1 | Gen. Mark Milley publicly urges diplomatic negotiation window following Kherson liberation | [BBC: Milley Statements](https://www.bbc.com/news/world-us-canada-63581530) |
| **2022-11-11** | `military_tech_win` | H3 | 1 | Liberation of Kherson city; Russian forces retreat across the Dnipro River | [Wikipedia: Liberation of Kherson](https://en.wikipedia.org/wiki/Liberation_of_Kherson) |
| **2023-05-20** | `territorial_loss` | H1 | -1 | Fall of Bakhmut following multi-month war of attrition | [Wikipedia: Battle of Bakhmut](https://en.wikipedia.org/wiki/Battle_of_Bakhmut) |
| **2023-06-04** | `military_tech_win` | H3 | 1 | Launch of 2023 Zaporizhzhia/Southeastern counteroffensive | [Wikipedia: 2023 Counteroffensive](https://en.wikipedia.org/wiki/2023_Ukrainian_counteroffensive) |
| **2023-10-01** | `us_pressure_statement` | H2 | -1 | US Congress drops Ukraine military funding from short-term bill, initiating 6-month aid freeze | [Reuters: US Aid Drop](https://www.reuters.com/world/us/us-congress-averts-shutdown-drops-ukraine-aid-2023-10-01/) |
| **2023-11-01** | `territorial_loss` | H1 | -1 | Zaluzhny *Economist* interview acknowledging the counteroffensive has reached a stalemate | [Economist: Zaluzhny Interview](https://www.economist.com/europe/2023/11/01/ukraines-commander-in-chief-on-the-breakthrough-he-needs) |
| **2024-02-17** | `territorial_loss` | H1 | -1 | Ukrainian forces withdraw from Avdiivka amid severe artillery ammunition shortages | [Wikipedia: Battle of Avdiivka](https://en.wikipedia.org/wiki/Battle_of_Avdiivka_(2023%E2%80%932024)) |
| **2024-03-22** | `us_pressure_statement` | H2 | -1 | US publicly warns Ukraine against long-range drone strikes on Russian oil refineries | [FT: US Warnings on Refineries](https://www.ft.com/content/98f15b60-bc4d-4d3c-9e57-cbd9fc2e00bc) |
| **2024-08-06** | `military_tech_win` | H3 | 1 | Ukraine launches surprise Kursk incursion, capturing over 1,000 sq km of Russian territory | [Wikipedia: Kursk Incursion](https://en.wikipedia.org/wiki/August_2024_Kursk_Oblast_incursion) |
| **2024-10-15** | `military_tech_win` | H3 | 1 | Major scale-up of deep-strike drone campaign against Russian ammunition depots | [Tech developments 2024-2025](https://ts2.tech/en/drone-warfare-and-developments-in-ukraine-2024-2025/) |
| **2025-02-14** | `us_pressure_statement` | H2 | -1 | VP Vance Munich Security Conference speech demanding European burden-sharing & fast talks | [Bloomberg Coverage](https://www.bloomberg.com) |
| **2025-02-19** | `us_pressure_statement` | H2 | -1 | White House social posts pressuring immediate ceasefire and criticizing Ukrainian leadership | [Bloomberg Coverage](https://www.bloomberg.com) |
| **2025-02-28** | `us_pressure_statement` | H2 | -1 | High-profile Oval Office clash resulting in diplomatic impasse and public disagreement | [Bloomberg Coverage](https://www.bloomberg.com) |
| **2025-03-03** | `us_pressure_statement` | H2 | -1 | Formal temporary pause instituted on US military assistance shipments and intelligence sharing | [Bloomberg Coverage](https://www.bloomberg.com) |
| **2025-03-15** | `territorial_loss` | H1 | -1 | Russian counter-offensive recaptures key sectors in Kursk Oblast | [Wikipedia: Kursk Incursion](https://en.wikipedia.org/wiki/August_2024_Kursk_Oblast_incursion) |
| **2025-06-01** | `military_tech_win` | H3 | 1 | "Operation Spiderweb" — SBU covert strike destroys strategic bombers at 5 airbases via truck-launched FPV drones | [Wikipedia: Operation Spiderweb](https://en.wikipedia.org/wiki/Operation_Spiderweb) |
| **2025-08-15** | `us_pressure_statement` | H2 | -1 | Trump-Putin Anchorage summit ends without ceasefire; Trump implies the onus is on Ukraine to cede territory | [CNN: Alaska Summit Takeaways](https://www.cnn.com/2025/08/15/politics/takeaways-trump-putin-summit-alaska) |
| **2025-11-23** | `us_pressure_statement` | H2 | -1 | US pressures Ukraine in Geneva over 28-point peace plan requiring territorial concessions and permanent NATO exclusion | [Washington Post: Geneva Peace Plan Talks](https://www.washingtonpost.com/world/2025/11/24/ukraine-peace-plan-europe-russia/) |
| **2025-12-02** | `territorial_loss` | H1 | -1 | Russian MoD claims full capture of Pokrovsk following multi-month urban assault (disputed by ISW into late Dec) | [Moscow Times: Pokrovsk Capture](https://www.themoscowtimes.com/2025/12/02/russian-army-claims-capture-of-key-city-of-pokrovsk-in-eastern-ukraine-a91299) |
| **2026-01-25** | `territorial_loss` | H1 | -1 | Pokrovsk offensive concludes; Myrnohrad lost to Russian forces | [Wikipedia: Pokrovsk Offensive](https://en.wikipedia.org/wiki/Pokrovsk_offensive) |
| **2026-02-10** | `military_tech_win` | H3 | 1 | Ukraine retakes ~78 sq. miles during spring offensive driven by drone-infantry tactics | [Tech developments 2024-2026](https://ts2.tech/en/drone-warfare-and-developments-in-ukraine-2024-2025/) |
| **2026-07-05** | `us_pressure_statement` | H2 | -1 | VP Vance calls the 2023 Western-pressured counteroffensive a "strategic and tactical disaster," advises Ukraine stay maximally defensive | [Ukrainska Pravda: Vance Statements](https://www.pravda.com.ua/eng/news/2026/07/05/8042501/) |
| **2026-08-15** | `military_tech_win` | H3 | 1 | Jet-powered drone mass strike campaign hits airfields, logistics, and oil hubs deep inside Russia | [Defense News & Field Reports](https://ts2.tech/en/drone-warfare-and-developments-in-ukraine-2024-2025/) |
| **2026-09-02** | `military_tech_win` | H3 | 1 | Ukrainian tactical counter-operations collapse Russian salient near Lyman, retaking >120 sq km | [Lyman Salient Analysis](https://www.youtube.com/watch?v=9dQzQ4tymOk) |
