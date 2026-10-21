# Disagreement Review: ids 35579–36900 (event test, batch 13)

700 rows labeled, 528 agreed (75.4%), 172 disagreements below. Run 1 = `claude-sonnet-5`, run 2 = `claude-opus-5`. Only non-Simplified event-test comments. 11 videos; most disagreements come from the Taiwanese-volunteers video `O0zTHiPC_r0` (59), the Azov explainer `NyOts7tERts` (26), the 蔡正元 'will Trump defend Taiwan' video `PdX_-ZCTsrw` (26) and the PLA drone drill `LsVZRR1Pcl4` (21). Disagreement rows: 106 thread_only, 66 thread_with_comment.

Both runs hit the session limit on 2026-10-12 (Sonnet stopped at 600, Opus at 650); the remaining 100 / 50 rows were labelled on 2026-10-13 by new runs with the same launch message (range and count changed only).

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion. Bold = the labels where the runs differ.

Precedent used for "Your call": your batch 1–12 decisions, `labeling_prompt.md`, and your own labels in `full_data.db` on six of these videos (`JVSaxGNZ5xQ` 83 rows, `LsVZRR1Pcl4` 80, `PwBldfM1DRg` 87, `O5kxxsdp740` 95, `PEoo6ypi0ks` 89, `MI1dwwf5m_w` 82).

My calls: 119 Opus, 51 Sonnet, 2 other. 62 marked **Borderline**.

**Main patterns.**
- **Volunteer praise** (`O0zTHiPC_r0`, ≈45 rows): Sonnet gives ST, Opus SU. Your `full_data.db` labels on the other volunteer video split the same way: plain hero praise ('真英雄', '勇士，Proud of you', '平安回家') = **SU**; praise framed as Taiwan's pride ('台灣之光', '台灣有你們引以為榮', '台堮勇士加油', '台灣有你是種驕傲') = **ST**; both parts present ('爲烏克蘭也是爲台灣') = **SU+ST**. I used that split, so most of these rows go to Opus, but 11 'Taiwan's heroes / our pride' rows go to Sonnet (ST).
- **Attacks on the volunteers** ('for money', 'fled', fighting beside Azov) → **CU**, not CT (your labels on `JVSaxGNZ5xQ`; batch 12). Rebuttals of the 'for money' claim → **SU**.
- **PLA drone drill** (`LsVZRR1Pcl4`): praise of PLA strength, Black-Bear mockery, 賴/蟾蜍 jabs → **CT**; mocking the PLA → **ST** (your labels on this video). Plain technical remarks → false.
- **蔡正元 videos** (`PdX_-ZCTsrw`, `P3M0oVkxmsI`): praise of the pundit → **CT** (batch 12 line); 'US won't protect Taiwan' → **CT+DUS**; '+1'/'讚同' to unification or 'dissolve the MND' → **CT** (parents are not in the DB, judged from the quoted text).
- **國軍 criticism** (`JVSaxGNZ5xQ`, 6 rows): mockery → **CT**, reform calls → **ST** (batch 12 line).
- **Jabs at PRC users** with no Taiwan-defence content ('go back inside the wall', CCTV mockery) → **false**, per the prompt's 牆內/VPN note. Named 五毛 → **ST**.
- **Others (2):** 36067 → CT+DUS (mocks Taiwanese as 失智 + US invasions); 36833 → ST (warning to China; the Trump line is not distrust of the US).

**Note on the runs:** both INSERT-only, exactly 700 rows each, no UPDATEs, no rows marked both critical and supportive.

---

### id 35580
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread:** 作為曾經的志願役，國軍的訓練真的超~~~級脫節不符合現代戰爭。希望國防部能虛心跟這些有實戰經驗的專家好好學習
**Translation:** As a former volunteer soldier: 國軍 training is extremely out of touch with modern war. Hope MND humbly learns from these combat-experienced experts.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Criticism, but ends with a call for MND to learn from the volunteers → reform call → ST (your '國軍要把他們倆位請益' label).

---

### id 35581
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread (context):** 作為曾經的志願役，國軍的訓練真的超~~~級脫節不符合現代戰爭。希望國防部能虛心跟這些有實戰經驗的專家好好學習
**Reply:** 我覺得跟薪水一樣，沒必要多錢軍隊裡的學長學弟制也一直被討厭，以至於訓練風氣帶不起來
**Translation:** Like pay, the senior/junior hierarchy in the army is hated, so a training culture never takes off.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Seniority culture kills training → criticism of 國軍 → CT.

---

### id 35582
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread:** 歡迎台灣戰士平安歸來
**Translation:** Welcome home safely, Taiwanese warriors.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — Welcome-back to the volunteers → SU (batch 12 '歡迎安全歸國' = SU).

---

### id 35593
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread:** 我很好奇為烏克蘭捐軀台灣政府會給多少撫恤金
**Translation:** I wonder how much compensation the Taiwan government would pay for dying for Ukraine.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Curiosity or sarcasm about compensation; direction unclear → false.

---

### id 35595
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread:** 台灣時間到 打飯班就要出列了😆
**Translation:** Taiwan's time has come — the mess-duty squad will step forward 😆

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 國軍 (打飯班 = mess-duty squad) → CT.

---

### id 35596
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread:** 我相信除了生涯規劃退役的人之外，有許多人剛從軍滿懷熱情，卻被軍中各種脫勾與不符合現代戰爭的可笑訓練狠狠澆熄，國軍再不改變真的只是一群領薪水的民兵
**Translation:** Many joined full of passion and were crushed by absurd training; if 國軍 doesn't change it's just paid militia.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Sonnet (CT) — 'Just a bunch of paid militia' → mockery of 國軍 → CT (batch 12 line).

---

### id 35599
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread:** 真的 政府要重視啊～實際戰爭跟演練是不同，不要目光短淺啊～
**Translation:** Really, the government must take this seriously — real war differs from drills.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — Government should take it seriously → reform call → ST.

---

### id 35603
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍"與實戰脫節" 法外傭步兵練彈道研析 國軍新訓僅練開槍如"民兵"│【LIVE大現場】20230523│三立新聞台)
**Thread:** 希望那些國軍將軍們醒醒⋯ 人家實際打過仗的，有用到刺槍術嗎？😢😢😢
**Translation:** Hope those 國軍 generals wake up… did the people who actually fought use bayonet drills? 😢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks the generals' bayonet drills → CT (your '刺槍術' label).

---

### id 35607
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 想象这是呆军据点😂
**Reply:** 缺乏高速運算能力，確實是呆軍，人呆，無人機自然也呆。
**Translation:** (Parent: imagine this is a 呆軍 [Taiwan army] base) Reply: Lacks computing power — truly a dumb army; dumb people, so the drones are dumb too.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Turns '呆軍' back on the PLA: 'its drones are dumb too' → mocks the PLA → ST.

---

### id 35619
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 台灣這塊遠遠落後，無人機戰爭已是未來趨勢
**Reply:** ​@kuku4629美國那個破爛玩意給的坦克被閹割了多少性能，笑死我了還指望那破坦克呢😊🤣🤣🤣
**Translation:** How much were those US junk tanks downgraded? LOL, still relying on those broken tanks.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — Mocks Taiwan relying on downgraded US tanks → CT + DUS.

---

### id 35707
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 太恐怖了，所有在室內及碉堡的敵人，完全殲滅。
**Reply:** @yong5280 兩次攻擊，第一次把網給炸了，第二機再把炸彈送進去陣地裡。再者，爆炸波足以對人員及裝備造成足夠的傷害，對戰鬥人員的心理素質，也已經造成深層的傷害。
**Translation:** Two strikes: the first blew the net, the second sent the bomb in. The blast also causes deep psychological damage.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Technical explanation of the strike; no Taiwan stance → false.

---

### id 35728
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 台湾省人何不「和平回归」更有面子？以后台湾省若是主动选择回归祖国，这件事写在中华历史上都是让人称赞的大智慧，简直光宗耀祖
**Reply:** 傻啊，共產黨政府先幫幫自已同胞吧，失業率上升，地方債惡化，經濟危機重重，一天到晚想打仗，然後呢？戰爭沒有贏家，子彈不長眼，內戰會毀滅了家園，死了自已的親人！三思吧！
**Translation:** (Parent: why doesn't Taiwan province 'peacefully return'?) Reply: Silly — CCP should help its own people first: unemployment, debt, crisis… war has no winners.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Rejects 'peaceful return' by pointing at the PRC's own problems → ST.

---

### id 35729
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 台湾省人何不「和平回归」更有面子？以后台湾省若是主动选择回归祖国，这件事写在中华历史上都是让人称赞的大智慧，简直光宗耀祖
**Reply:** 我們的清德大帝是你們永遠無法理解的存在，他的道行並非你們這些螻蟻能夠想像的，正所謂「仙人之下我無敵，仙人之上一換一」！在高的科技在我們清德大帝面前，只要雙手一揮，方圓百里之內的高科技皆化為灰燼。不信？哈哈哈，只能說你們的格局太小了！連面對什麼樣的存在都不知道！如果你們趕快認錯，我們的清德大帝或許考慮替你們留個全屍！
**Translation:** Our Great Emperor Ching-te is beyond your comprehension… if you apologise quickly he may leave your corpse whole!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Over-the-top '清德大帝' copypasta aimed back at a PRC user; sarcasm direction unclear → false.

---

### id 35773
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 大陸國防部發言人證實，解放軍已經下單，正在採購一百萬台無人機，台灣號稱40萬的黑熊部隊，每只黑熊分配到2.5台自s無人機😄😄😄……
**Reply:** @coo0007 三天一定不成，最少要4天。
**Translation:** (Parent: PLA buying 1M drones, 2.5 per Black Bear) Reply: Three days won't do it, at least four.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Joke about how many days the PLA needs to beat Taiwan → mocks Taiwan's defence → CT.

---

### id 35779
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 大陸國防部發言人證實，解放軍已經下單，正在採購一百萬台無人機，台灣號稱40萬的黑熊部隊，每只黑熊分配到2.5台自s無人機😄😄😄……
**Reply:** 只要加足馬力，台灣忍者黑熊部隊的分身術可從40萬變成4000萬，看你無人機怎麼打？
**Translation:** Taiwan's ninja Black Bears can clone from 400k to 40M — how will your drones hit them?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks the Black Bear academy → CT.

---

### id 35780
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 大陸國防部發言人證實，解放軍已經下單，正在採購一百萬台無人機，台灣號稱40萬的黑熊部隊，每只黑熊分配到2.5台自s無人機😄😄😄……
**Reply:** 這你就不懂了，黑熊部隊早已練成隱身術，一旦發功，40萬可全部隱身，別說雷達，連眼睛都看不到，還以為全部不見了。
**Translation:** The Black Bears have mastered invisibility; all 400k vanish from radar and eyes.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks the Black Bear academy → CT.

---

### id 35782
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread (context):** 大陸國防部發言人證實，解放軍已經下單，正在採購一百萬台無人機，台灣號稱40萬的黑熊部隊，每只黑熊分配到2.5台自s無人機😄😄😄……
**Reply:** 我比較感興趣的是 : 蟾蜍可以有多少配額 ?
**Translation:** What I'm more interested in: how many does the Toad get?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — 蟾蜍 = 賴 nickname → mocks 賴 → CT (your '赖蛤蟆' label on this video).

---

### id 35789
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 輸了~~輸了~~你俄爹在烏克蘭給打趴了，普京快輸了，現在可以連北韓一起消滅，真主黨又給滅黨，伊朗也快輸了，之後西方要收拾的就是終共了~~~~~~ 😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂
**Translation:** Lost! Your Russian daddy got beaten in Ukraine, Putin is about to lose… next the West deals with the CCP 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **0** | 0 | 0 |
| Opus | 0 | 1 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Mocks Russia losing and the CCP being next; no Taiwan self-defence content → SU only.

---

### id 35790
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 利害的軍事實力！
**Translation:** Impressive military strength!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Praises PLA strength under the drill video → CT (your '大陆这么厉害啊' label).

---

### id 35793
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 每次打擊目標都要犧牲一部無人機....保護無人機人人有責
**Translation:** Each strike sacrifices a drone… protecting drones is everyone's duty.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Joke about drones being used up; no clear stance → false.

---

### id 35805
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 這個讚！買來再改良一下對付高架捷運：或者是橋樑：早就說過了百姓沒辦法造反！只有軍人才有辦法判亂！
**Translation:** Great! Buy it, improve it to hit elevated MRT or bridges; civilians can't rebel, only soldiers can.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Unclear rambling (attack overpasses; only soldiers can rebel) → false.

---

### id 35806
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 😂😂😂梅國baba买的武器又打水漂
**Translation:** 😂 Weapons bought from US daddy wasted again.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — Mocks US-bought weapons as wasted ('baba') → CT + DUS.

---

### id 35826
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** Hmm.. we now need potable, easily deployed Chicken wire nets around emplacements.
**Translation:** We now need portable chicken-wire nets around emplacements.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Generic counter-drone tip, no Taiwan reference → false.

---

### id 35827
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 大陸仔開始抄襲烏克蘭無人機作戰了 笑死人🙂
**Translation:** Mainlanders started copying Ukraine's drone warfare, LOL.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | **0** | 0 | 0 |
| Opus | 0 | **0** | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Mocks the PLA for copying Ukraine → ST (your '山寨' label on this video).

---

### id 35848
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 彎彎某缺德看到......
**Translation:** When Wanwan's Que-de [Lai] sees this…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — 彎彎 + 缺德 (賴 nickname) → CT.

---

### id 35865
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** AI + 無人機，200萬大軍會double
**Translation:** AI + drones, the 2-million army doubles.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Hypes PLA drone power → CT (your '大疆…產能' label).

---

### id 35887
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 台灣省會不會是第二位（🇺🇦）🧐
**Translation:** Will Taiwan province be the second 🇺🇦?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — 'Taiwan province' next Ukraine → CT.

---

### id 35892
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 中國現在太強大了
**Translation:** China is too strong now.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35915
**Video:** `LsVZRR1Pcl4` (鎖定打擊目標，殲滅！解放軍東部戰區無人機演練#中國 #無人機 #china #東部戰區)
**Thread:** 拜託到時候速戰速決
**Translation:** Please make it quick when the time comes.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Asks the PLA to finish fast → CT (your '麻煩精準打擊' label).

---

### id 35945
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 這次戰爭中看到波蘭人對烏克蘭人大力伸出援手，但其實二戰時烏克蘭人跟波蘭人其實有發生互相屠殺，因為波蘭人當時把烏克蘭人當成下等人，所以烏克蘭民族主義者當時對波蘭人的痛恨造成了慘劇。有一部電影「沃倫」就是在講沃倫大屠殺這件事情  其實波蘭跟烏克蘭都是夾在大國之間存活的國家，本身有很多難處，大國要侵略小國，各種理由都掰的出來，最重要的還是自己國家要有足夠強大的軍事武力，才能夠確保和平永存，敵人不敢侵犯
**Reply:** @CobraBigSnake 烏克蘭以前就存在過只是被波蘭併吞過
**Translation:** Ukraine existed before; it was just annexed by Poland.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Rebuts 'Ukraine never existed' but short → false (rebuttal default).

---

### id 35951
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 下一期主題是為什麼瑞士可以保持500年的中立? 瑞士其實在歷史上以驍勇善戰著稱，瑞士傭兵非常有名，軍事如此強悍的國家，為什麼要保持中立呢? cheap頻道其實也是業配著名，該回歸到大業配時代了，俄羅斯系列還有一集【車臣】，有時間再上  便宜的cheap貼圖不買嗎 https://store.line.me/stickershop/author/1784332
**Reply:** ​@Hahahaha-v6l 大概是又共媒給你們灌輸的，這種幫中共把鍋甩得一乾二淨、責任推光光的說法，仔細想就知道有貓匿。所有媒體都有自己的立場，不管是西方媒體還是共媒都一樣，不要全部都相信。  為什麼「送中(逃犯條例)」會造成大量香港人反對，他們在擔心什麼？為什麼唐英傑審判被改使用了「有罪推定」？這些資訊共媒有沒有完整呈現？我不是一味不信共媒，也不是完全同意香港人在此的抗爭行為，西方勢力的確有可能背後煽動，但回到更基本的邏輯：「一個巴掌拍不響」。如果中共自己沒有做不完善的地方，沒有造成港人大量反對的事因，那些外國勢力煽動得起來嗎？而阻止這種狀況最好的方式，不就是把自己做得更好，讓人民對自己的政府有信心嗎？把自身可以改善的地方視而不見，卻把原因往外推諉缷責；這種無視病根只想把病症「壓下」，眼不見為淨的做法，反而會給未來穩定埋下更多隱患。而這樣的重點共媒有沒有提及，還是只幫中共甩鍋缷責？  既然已經在牆外，建議多瞭解一些共媒以外的訊息，整體去判斷合理性。和西方國家領導人一樣，中共領導人在遇到自身利益與國家人民利益衝突時，難保不會選擇前者，而被掌控的國家媒體又難保不會為了領導人利益而背棄國家人民利益，變成和西方媒體一樣選擇性報導甚至公然說謊欺騙人民。所以為了「愛國」為了「保護家人與同胞」，更需要在面對多種媒體時有更多思辨。  再說回來，數千年前的「北風與太陽」早已提醒我們，聰明的一方是要當北風還是太陽？和前面類似的基本邏輯，如果中國真的夠好，高官不是把兒女往歐美送，有足夠的繁榮、誠信、健全法治與權力結構、食安以及責任感(不會老甩鍋)，那不用說台灣，周邊國家都要爭先恐後貼過來，甚至一個個都想加入，怎麼還會有分離分裂的問題？到時那些外國勢力再怎麼煽動也不會激起任何一點波瀾！所以共媒真的愛國，就應該要把重點放在中國不足的地方，聚焦全中國人民勇敢面對處理這些問題，促使中國早日成為真正文明大國，而非老是把國民注意力往外部轉移。  最後想到電影裡蘇乞兒向皇上說的：「丐幫有多少弟子不是由我決定，而是由你決定的，如果你真的英明神武，使得國泰民安，鬼才願意當乞丐呢！」突顯出正確找出問題根源的重要。
**Translation:** Long reply: CCP media shifts blame; HK extradition; if China were really good, Taiwan and neighbours would flock to it…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Long argument against CCP media/HK repression, 'if China were good Taiwan would come' → ST.

---

### id 35956
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 下一期主題是為什麼瑞士可以保持500年的中立? 瑞士其實在歷史上以驍勇善戰著稱，瑞士傭兵非常有名，軍事如此強悍的國家，為什麼要保持中立呢? cheap頻道其實也是業配著名，該回歸到大業配時代了，俄羅斯系列還有一集【車臣】，有時間再上  便宜的cheap貼圖不買嗎 https://store.line.me/stickershop/author/1784332
**Reply:** @jackh0 老是站在自己的觀點 忽略了其他的觀點 那就看不出 整個事件的全貌。每個事件的發生 各個國家跟民族 都會針對他自己有利的事件來 宣傳。重點是 表面贏家輸家跟最後贏家輸家是誰… 俄羅斯 表面十惡不赦 烏克蘭最慘 北約歐盟 掃到颱風尾 最爽的是誰 你應該知道？
**Translation:** Russia looks evil, Ukraine suffers most, NATO/EU hit… who benefits most? You know.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 1 | 0 |
| Opus | **1** | 0 | 0 | 0 | 1 | 0 |

**Your call:** Sonnet (DUS) — 'Who benefits most? you know' → US as beneficiary → DUS; no anti-Ukraine claim.

---

### id 35957
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 下一期主題是為什麼瑞士可以保持500年的中立? 瑞士其實在歷史上以驍勇善戰著稱，瑞士傭兵非常有名，軍事如此強悍的國家，為什麼要保持中立呢? cheap頻道其實也是業配著名，該回歸到大業配時代了，俄羅斯系列還有一集【車臣】，有時間再上  便宜的cheap貼圖不買嗎 https://store.line.me/stickershop/author/1784332
**Reply:** @陳俊宏-l2d 至少台灣意識型態不封閉，你看統派黨現在還不是過好好的，而且親共媒體到現在還存在，你看對岸有辦法這樣？跟中國比起來，台灣的資訊真的比較不封閉。
**Translation:** At least Taiwan isn't ideologically closed; pro-unification parties and pro-CCP media exist; China can't do that.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Taiwan's open information vs China's closed system → ST.

---

### id 35958
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 下一期主題是為什麼瑞士可以保持500年的中立? 瑞士其實在歷史上以驍勇善戰著稱，瑞士傭兵非常有名，軍事如此強悍的國家，為什麼要保持中立呢? cheap頻道其實也是業配著名，該回歸到大業配時代了，俄羅斯系列還有一集【車臣】，有時間再上  便宜的cheap貼圖不買嗎 https://store.line.me/stickershop/author/1784332
**Reply:** @indepellew 北約存在 誰是最大的利益？… 誰是最大的損失？…
**Translation:** NATO exists — who benefits most? Who loses most?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Opus (all false) — **Borderline** — Vague rhetorical question, US not named → false.

---

### id 35970
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 其實，烏克蘭大饑荒本身就可以做一集影片了，從來龍去脈到影響就有很多可以說的，且這場饑荒不只烏克蘭，高加索和哈薩克也很慘⋯⋯
**Reply:** @high2669 你自己去查查資本主義的意思，不要只會諷刺複製我的話，不要看CCTV，你也就會複製，五毛無疑，你看著我很無知，實則不知道自己多無知啊，笑死
**Translation:** Look up capitalism yourself… don't watch CCTV… a 五毛 no doubt.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Names 五毛 → ST (prompt criterion).

---

### id 35985
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 其實，烏克蘭大饑荒本身就可以做一集影片了，從來龍去脈到影響就有很多可以說的，且這場饑荒不只烏克蘭，高加索和哈薩克也很慘⋯⋯
**Reply:** @high2669 我俄中傷害平民永遠是誤殺，你北約發展軍事是要準備入侵
**Translation:** 'When we Russia/China hurt civilians it's an accident; when you NATO arm, it's to invade.'

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — Sarcastic mimicry of Russia/China double standards → SU.

---

### id 35996
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 其實，烏克蘭大饑荒本身就可以做一集影片了，從來龍去脈到影響就有很多可以說的，且這場饑荒不只烏克蘭，高加索和哈薩克也很慘⋯⋯
**Reply:** 還是老話,洗烏克蘭大飢荒的狗不是腦殘到壞了就是賤到沒人性
**Translation:** Those who whitewash the Ukrainian famine are brain-dead or inhuman.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Condemns Holodomor deniers → SU.

---

### id 36035
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 中國官方沒有正式支持俄國入侵烏克蘭，請UP主也不要一直潑給中國髒水，中國網民有支持俄羅斯也有反對俄羅斯。
**Reply:** 俄烏戰爭開打後，微博、微信、百度所有支持烏克蘭的言論都被刪除了，中國互聯網上只剩下支持俄羅斯的言論。(我可以找到20條以上中國網民在油管說自己支持烏克蘭，結果秒被刪，更慘的還被刪號)直到大翻譯運動開始，哎，反對俄羅斯的言論可以出現了。
**Translation:** After the war began, all pro-Ukraine speech on Weibo etc. was deleted…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Describes PRC censorship of pro-Ukraine posts; no own stance → false.

---

### id 36064
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 孩子，中国没有支持任何国家，只是不干涉并进行了人道援助，如果你非要犟，弱就是原罪。
**Reply:** 香港一間餐廳叫作「東歐餐廳」， 因為早前表態支持烏克蘭人， 並曾呼籲大家以捐款方式支援烏克蘭政府。 最後，就被中共黨媒《文匯報》批評： 「有反中亂港分子企圖利用『俄烏衝突』發起各種煽惑行動。」  香港民意研究所， 早前打算就「俄烏大戰」作一項研究調查， 旨在了解香港人對此事的認知和立場。 最後，又再一次被中共黨媒《文匯報》批評： 「可能涉嫌違反憲法、基本法與國安法。」  有5名居港烏克蘭人， 在中環發起聲援烏克蘭行動。 最後，有3名被指涉嫌違反限聚令， 並將之拘捕。
**Translation:** HK restaurant backing Ukraine attacked by CCP media; survey called illegal; Ukrainians arrested.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Lists HK repression of pro-Ukraine acts; no own stance → false.

---

### id 36067
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 給我推了這位朋友，其實有耳聞，有機會就很認真聽吧，也終於為什麼灣灣的朋友會這麽失智，也沒什麼關係吧，繼續自high吧你們哈哈。不知道這位朋友有沒有講老美入侵其他國家的，想看看他怎麼洗，好期待，發個鏈接我吧
**Translation:** Now I see why Wanwan friends are so demented… does he cover the US invading other countries? Send me a link.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Other (CT+DUS) — Both parts present: mocks Taiwanese as 失智 (CT) + US invading others (DUS) → Other: CT+DUS.

---

### id 36071
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 真的 入侵就是入侵。日本人也不是什麼好東西。美帝就更不用說了。
**Translation:** Indeed, invasion is invasion. The Japanese are no good, US imperialists even less.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 1 | 0 |
| Opus | 0 | **0** | 0 | 0 | 1 | 0 |

**Your call:** Sonnet (SU+DUS) — 'Invasion is invasion' (SU) + 美帝 (DUS).

---

### id 36080
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 俄國打烏克蘭本來就是為了戰略安全而已打的，用台灣的角度去看你會容許澎湖加入中國讓後讓中國在澎湖上面放置各式武裝力量然後對着台灣嗎？  這是對國際關係敏感不敏感的問題，事實上北約美國他們不會進入這次紛爭，一但介入就是第三次世界大戰...
**Translation:** Russia attacked Ukraine for strategic security; would Taiwan accept Penghu joining China with weapons pointed at it?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | **0** | 1 |
| Opus | **1** | 0 | 0 | 0 | **1** | 1 |

**Your call:** Sonnet (BNE) — **Borderline** — Justifies Russia's attack as strategic security (BNE); no blame on Ukraine, no US distrust → BNE only.

---

### id 36092
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 唇亡齿寒，俄罗斯没有了，下一个就是中国
**Reply:** 別被共產黨騙了，美國可從來沒打過中國，倒是俄羅斯打過。
**Translation:** Don't be fooled by the CCP: the US never attacked China; Russia did.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Anti-CCP, pro-US remark, nothing on Taiwan → false.

---

### id 36096
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 支持俄罗斯，俄罗斯必胜
**Reply:** 問：霸佔中國領土最多的是誰？答：俄國。🇷🇺 問：未佔中國寸土的是誰？答：美國。🇺🇸 問：義和團時，在海蘭泡，江東六十四屯屠殺中國人，趁機單獨出兵佔領東北全境，逼清政府簽約割讓東北的誰？答：俄國。🇷🇺 問：義和團後，主動退還多餘賠款，建立清華大學，並資助高等教育和公派留學的是誰？答：美國。🇺🇸 問：除日本外，承認偽滿洲國，建立邦交的是誰？答：俄國。🇷🇺 問：堅決不承認偽滿洲國，要求日本撤出東北的是誰？答：美國。🇺🇸 問：七七事變後，1938年出兵新疆的是誰？答：俄國。🇷🇺 問：七七事變後，要求日本撤出華北，並對日本實行禁運，派出志願航空隊支援中國的誰？答：美國。🇺🇸 問：在南京大屠殺時，對割佔土地上的中國人進行大清洗的是誰？答：俄國。🇷🇺 問：反對中國當聯合國“五常”的是誰？答：俄國。🇷🇺 問：支持中國當聯合國“五常”的是誰？答：美國。🇺🇸 問：中國需要幫助時撤走專家的是誰？答：俄國。🇷🇺 問：中國發展經濟時開放市場的是誰？答：美國。🇺🇸 問：當年威脅對中國實施核打擊的是誰？答：俄國。🇷🇺 問：不惜代價，堅決阻止俄國核打擊的是誰？答：美國。🇺🇸 問：誰在中國入世談判時要求中國實行五天工作日？答：美國。🇺🇸 問：誰給中國永久最惠貿易國待遇？答：美國。🇺🇸 問：輸入中國最多先進科學技術的是誰？答：美國。🇺🇸 問：每個人的電腦裡用的CPU芯片是哪個國家的？答：美國。🇺🇸 問：中國留學生最多的國家是哪個？答：美國。🇺🇸   問：中國的朋友是誰？答：俄國。🇷🇺 問：中國的敵人是誰？答：美國。🇺🇸
**Translation:** Q&A list: who took most Chinese land? Russia. Who took none? The US…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Long Russia-vs-US list on China's history; no Ukraine/Taiwan stance → false.

---

### id 36111
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 一堆歪理，就是洗白
**Translation:** A pile of twisted logic, just whitewashing.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 0 | 0 | 0 | 0 |
| Opus | **0** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (CU) — Calls the video (Ukraine isn't neo-Nazi) whitewashing → CU.

---

### id 36121
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 哈哈哈哈哈哈哈 笑死人 又是一個看似公正卻幫忙新納粹洗地的影片 澤連斯基是猶太人就不可能支持新納粹？ 可見你完全不了解烏克蘭 段宜康不是外省人嗎？ 他還不是加入民進黨？ 種族的叛徒多了去， 這你難道不知道嗎？
**Translation:** LOL another video washing neo-Nazis… 段宜康 is a mainlander but joined the DPP — plenty of race traitors.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **0** | 0 | 0 | 0 |
| Opus | 1 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CU+CT) — Azov whitewashing (CU) + calls DPP's 段宜康 a race traitor (CT).

---

### id 36138
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 說的很好，但這場戰爭去納粹什麼的只是藉口，沒有這個理由也會找出其他的。 戰爭會發生，最簡單來說就是利益和國土的爭奪，當不可協調時就是武力解決。至於出兵的理由也不過是利益爭鬥的遮羞布而已。 這個戰爭明面上是烏克蘭和俄羅斯在打，事實上歐洲和美國都已經用非武力的方式參戰了。簡單來說就是加入利益的分割。
**Translation:** Denazification is just a pretext… the war is about interests; Europe and the US joined to share the spoils.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | **0** | 0 | 0 | 1 | 0 |
| Opus | **0** | **1** | 0 | 0 | 1 | 0 |

**Your call:** Opus (SU+DUS) — **Borderline** — 'Denazification is a pretext' (SU) + West joins to split the profits (DUS).

---

### id 36140
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 你是講美國不喜歡你，就找其他藉口入侵你，又是說廢話
**Translation:** You mean if the US dislikes you it finds an excuse to invade you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — US invades on pretexts → DUS.

---

### id 36152
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 胡说八道。俄罗斯一开始就说没要灭乌克兰，占领全乌克兰，只是说要去军事化，去纳粹化。那来的灭国战争？ 拿俄乌战争和中日比，更是不伦不类。 乌克兰在颜色革命，亲西方政府上台後，一直反俄，包括禁在公共场合说俄语，搞到乌东，克里米亚要独立，乌克兰更要加入北约这个就是对抗俄国的军事组织。在乌东亚速营有对俄裔做出可比二战时纳粹的罪行。 而中国在日本侵华前一向强调中日友好，完全没惹日本，日本却起贪念侵华，能拿来比吗？
**Reply:** @wesleylim7023 你要劃等號沒有人阻止你啊 中國人不也是不譴責俄羅斯 俄羅斯搶走中國那麼多領土還是舔得不要不要的🤣
**Translation:** Chinese don't condemn Russia either; Russia took so much Chinese land and they still lick it 🤣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Mocks pro-Russia Chinese who ignore Russia's land grabs → SU.

---

### id 36198
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 其實把戰爭只有一個目的，唇亡齒寒，哪怕烏克蘭是獨立的，並不是自己的僕從國，俄羅斯都有一個緩衝地帶，而不是敵對軍事直抵家門口。這是大國的戰略
**Translation:** The war has one aim: a buffer zone, not a hostile military at the door. Great-power strategy.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Sonnet (BNE) — Buffer-zone justification → BNE; no blame on Ukraine → BNE only (same as 36080).

---

### id 36207
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 謝謝你的普及，但是我還是對亞速營有下列疑問： 1.亞速營在頓巴斯製造各種慘案記錄片的真偽？ 2.亞速營除了類似納粹標誌外，他們軍人為什麼身上都是納粹“黑太陽”和“狼之鉤”紋身？這個不能洗吧？ 3.亞速營為什麼遲遲不願釋放亞速鋼鐵廠工人及其家屬？ 从戰場形勢亞速營已經是烏克蘭東部和南部的主力部隊了，不是你說的少數右派，他們這些做法很難讓人相信他們不是納粹。
**Reply:** 有關標誌但部分其實歐洲很多類似標誌的組織，比較搞笑但是芬蘭某空軍部隊的標誌是卍字符號，而因此近幾年被民間反彈到換掉旗幟，諷刺但是這支空軍但標誌在納粹還沒成立前就已經在使用卍字符號
**Translation:** Many European units have similar symbols; a Finnish air force unit used a swastika before the Nazis.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — Neutral fact on Finnish swastika → false.

---

### id 36215
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 笑死光聽你說 俄羅斯方面新聞一定是假訊息 就知道你一定沒腦了 我可以反問你美國以及西方盟國的消息一定是真實的嗎？如果他們的消息是真實的為什麼從戰爭開始以來放出這麼多的假消息？事實上英美在戰爭中放假消息假新聞已不是什麼新鮮事，可以自己去看看印尼930事件英國特工是如何用假新聞屠殺50萬印尼華人
**Reply:** @qiumaverick5533 930世件事實是根據近年英國國家檔案館解密的文件 當中就是有英國特工介入以及英國BBC做虛假不時的黑色宣傳所以才會導致後面的大清洗，況且我不認為烏克蘭可以稱為是實質上的一個獨立國家，從開戰到現在明顯在為烏克蘭做決策並不是澤連司機本人，追根究底俄烏戰爭爆發的原因很大一部分就是烏克蘭政府控制不了烏東地區的爭端 且放任納粹份子迫害烏東平民，8年時間無法處理俄羅斯出兵幫你處理就是這麼簡單，再來以烏克蘭政府的尿性恐怕會繼續對烏東平民秋後算帳，俄直接納入烏東兩省也是合情合理。
**Translation:** Ukraine isn't really independent; Zelensky doesn't decide; Russia annexing the east is reasonable.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | 0 | 0 | 0 | **0** |
| Opus | 1 | 0 | 0 | 0 | 0 | **1** |

**Your call:** Sonnet (CU) — Ukraine not a real country, Russia's annexation reasonable (CU); no NATO claim → CU only.

---

### id 36217
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 笑死光聽你說 俄羅斯方面新聞一定是假訊息 就知道你一定沒腦了 我可以反問你美國以及西方盟國的消息一定是真實的嗎？如果他們的消息是真實的為什麼從戰爭開始以來放出這麼多的假消息？事實上英美在戰爭中放假消息假新聞已不是什麼新鮮事，可以自己去看看印尼930事件英國特工是如何用假新聞屠殺50萬印尼華人
**Reply:** @qiumaverick5533 我只能說就是英美安排的，也是冷戰時期一貫的做法，不然為什麼那麼多國家會出現顏色革命，你對這個歐美帶領的世界秩序為免想得太天真，烏克蘭2014的電話門事件聽過沒 手都伸向整個烏克蘭政府的人事安排，烏克蘭原本就沒有這個國家也沒有烏克蘭人這個民族 都是斯拉夫人 事實也證明也不該讓他成為一個國家，你能想像如果美國旁邊的加拿大是親俄的國家 美國有可能接受嗎？要想美國也是對加拿大發動戰爭的喔 如今還能稱兄道弟，俄烏本該像美加一樣是兄弟關係，西方借入煽動顏色革命後搞成什麼樣子?俄羅斯旁邊有個烏克蘭 中國旁邊有個台灣，為什麼每個大國旁邊都有一個遏制其發展的國家地區，美國在世界的布局如此之明顯 也是破壞世界和平的元凶
**Translation:** Colour revolutions… Ukraine shouldn't be a country… would the US accept a pro-Russia Canada? Russia–Ukraine, China–Taiwan…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | 1 | 0 | 1 | **0** |
| Opus | 1 | 0 | 1 | 0 | 1 | **1** |

**Your call:** Opus (CU+CT+DUS+BNE) — Canada analogy + colour revolutions → BNE (prompt example), plus CU/CT/DUS.

---

### id 36243
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread:** 馬劣子孫。
**Translation:** Descendants of Ma-lie.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Unclear target (馬劣 = 馬列?) → false.

---

### id 36249
**Video:** `NyOts7tERts` (亞速營是什麼?  烏克蘭是新納粹大本營嗎?)
**Thread (context):** 台湾省选总统才是最可笑的伪命题
**Reply:** 台灣省不能選，那中國就可以選嗎?
**Translation:** (Parent: Taiwan province electing a president is absurd) Reply: Taiwan province can't vote — can China?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Rhetorical jab at a PRC user, no Taiwan defence content → false.

---

### id 36275
**Video:** `NySZONUsepI` (CTWANT 俄烏戰爭 / 俄補給車被烏無人機追　下秒觸發地雷全都錄！)
**Thread:** 哦耶…👍
**Translation:** Oh yeah 👍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Cheers the Russian supply truck hit (video context) → SU.

---

### id 36305
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 勇敢的台灣男兒，在希望人家幫助前，我們也幫幫人家。說得好！你們是自由的驕傲，台灣的驕傲，文明世界的驕傲
**Reply:** 好勇敢....跟亞速營並肩作戰 !!! 好勇敢....跟亞速營並肩作戰 !!! 好勇敢....跟亞速營並肩作戰 !!!
**Translation:** So brave… fighting side by side with Azov!!! (×3)

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **1** | 0 | 0 | 0 |
| Opus | 1 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (CU) — Mocks volunteers fighting beside Azov → CU (your 'attacks on volunteers' labels); no Taiwan claim.

---

### id 36307
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 每個台灣人都該看看這則報導,讓自己清醒,我們的敵人是誰,我們該如何準備與下定決心.
**Reply:** 是該好好看看決策者錯誤決定可帶给人民災難。
**Translation:** (Parent: every Taiwanese should watch this) Reply: Yes, look at the disasters wrong decisions by leaders bring.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Commenter 張富順 blames 'decision-makers' (Taiwan's); next reply reads it that way → CT.

---

### id 36309
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 每個台灣人都該看看這則報導,讓自己清醒,我們的敵人是誰,我們該如何準備與下定決心.
**Reply:** @張富順-k3u 是啊，這些戰爭都是決策者(習近平/普丁)錯誤的決定帶來的災難。
**Translation:** Yes, these wars are disasters caused by the wrong decisions of Xi Jinping / Putin.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **1** | 0 | 0 |
| Opus | 0 | 1 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (SU+ST) — **Borderline** — Retort: Xi/Putin cause the wars → SU + ST (anti-CCP retort to a PRC-side user).

---

### id 36311
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 向台灣的英雄致敬！願所有抵抗侵略的英雄都能平安歸來！
**Reply:** 台獨如有這些英雄還怕不能獨立。
**Translation:** If Taiwan independence had heroes like these, why fear not becoming independent?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — Reads as sincere: with heroes like these Taiwan can stand → ST.

---

### id 36327
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 泪目了，作为母亲能同意自己的儿子上战场，这位台湾母亲需要付出多么大的勇气与妥协。台湾一这定能捍卫自己的民主自由，同时我也不希望两岸发生战争。
**Reply:** ​@張富順-k3u跟薪水無關，跟理念
**Translation:** It's not about the pay, it's about ideals.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — Rebuts the 'for money' claim → SU (batch 12 line).

---

### id 36334
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 泪目了，作为母亲能同意自己的儿子上战场，这位台湾母亲需要付出多么大的勇气与妥协。台湾一这定能捍卫自己的民主自由，同时我也不希望两岸发生战争。
**Reply:** ​@張富順-k3u 綁上炸藥和敵人同歸於盡，這種事在反侵略戰爭中是常有的事。為錢嗎？不，應該是因理念或仇恨，為自己鄉土親人免遭入侵匪敵宰割
**Translation:** Strapping on explosives… is common in wars against invasion. For money? No — for ideals, to protect homeland.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — Rebuts 'for money': fighting for homeland against invaders → SU.

---

### id 36337
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 来自大陆百姓的祝福！孩子们！你们才是真正的中华儿女！为了自由而舍身忘死！愿你们平安归来！😢！
**Reply:** 台奴假裝華人。
**Translation:** Taiwan slaves pretending to be Chinese.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — '台奴' slur → CT (batch 12 '台彎' slur = CT).

---

### id 36338
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 来自大陆百姓的祝福！孩子们！你们才是真正的中华儿女！为了自由而舍身忘死！愿你们平安归来！😢！
**Reply:** @王爱国 但你的黨國要你死你就得死，不高興你其實能回牆內
**Translation:** But your party-state decides if you die; if unhappy go back inside the wall.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Jab at a PRC user ('go back inside the wall'); prompt says 牆內 jabs alone don't qualify → false.

---

### id 36345
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 来自大陆百姓的祝福！孩子们！你们才是真正的中华儿女！为了自由而舍身忘死！愿你们平安归来！😢！
**Reply:** @王爱国 聽我的，你只能「想」或「不想」送死而已，至於做與不做，是你黨的決定
**Translation:** You can only 'want' or 'not want' to die; whether you do is your party's decision.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Same jab at a PRC user → false.

---

### id 36347
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 来自大陆百姓的祝福！孩子们！你们才是真正的中华儿女！为了自由而舍身忘死！愿你们平安归来！😢！
**Reply:** ​@一生不羈放縱愛自由台灣榮耀，跟中華沒鳥關係關係
**Translation:** Taiwan's glory, nothing to do with Zhonghua.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — 'Taiwan's glory, nothing to do with 中華' — Taiwanese identity against the PRC framing → ST.

---

### id 36356
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 来自大陆百姓的祝福！孩子们！你们才是真正的中华儿女！为了自由而舍身忘死！愿你们平安归来！😢！
**Reply:** 誰是中華兒女   你娘咧   幹
**Translation:** Who's a son of Zhonghua — f*** your mother.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Profanity rejecting '中華兒女'; plain insult → false (batch 9 rule).

---

### id 36367
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 真到那么一天我会毫不犹豫的举起青天白日满地红的旗帜，因为那个才是我的国旗
**Reply:** 想太多，青天白日，台灣人暫時用，
**Translation:** Overthinking — Taiwanese use the blue-sky-white-sun flag only temporarily.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Unclear ('Taiwanese use the ROC flag for now') → false.

---

### id 36369
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 中华民国的英雄们，望平安归来！自由的曙光与你们同在！
**Reply:** 英雄撈過了界自己國土不因為了錢遠走他鄉可惜了。
**Translation:** The heroes overreached — left their own land for money, a pity.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — 'Left home for money' → CU (your 'money' labels).

---

### id 36373
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 中华民国的英雄们，望平安归来！自由的曙光与你们同在！
**Reply:** ​@張富順-k3u 每月薪資1000歐元 ，差不多33000台幣，你要是肯為三萬三台幣在戰場上冒死，我也覺得你算是英雄好漢，不過你不是！
**Translation:** €1,000/month ≈ NT$33,000 — if you'd risk death for that, you'd be a hero too. But you're not!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — Rebuts 'for money' (pay is tiny) → SU.

---

### id 36374
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 中华民国的英雄们，望平安归来！自由的曙光与你们同在！
**Reply:** @guoxili7050 當然不會因為知道什麼事該做死要死的其所沒腦的事不會做。
**Translation:** Of course one who knows what's worth dying for won't do brainless things.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — Going is brainless → CU.

---

### id 36389
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 中华民国的英雄们，望平安归来！自由的曙光与你们同在！
**Reply:** @張富順-k3u 呵呵 ，每個都像你要假扮智者 ，那打起仗來 ，誰上戰場啊 ？各個都裝諸葛亮在那邊羽扇綸巾的 ？沒一個要拿兵器上前 ，到時候這些扮智者的 ，全部都只能像屠宰場裡的豬鴨雞羊 ，惟有引頸就戮罷了 。古代智者尚且尊重勇士英雄 ，現在一堆扮智者的 ，在提倡怯懦 ，甚至靠貶低他人來粉飾自己的怯懦 ， 就你留言處處錯字 ，連文字語言都沒法好好處理的 ，能有多智 ？徒然給人笑柄 ！
**Translation:** Everyone pretends to be wise; when war comes who goes to the front? They'll be slaughtered like pigs…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Attacks the 'wise' coward stance: who will fight when war comes → ST.

---

### id 36390
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 中华民国的英雄们，望平安归来！自由的曙光与你们同在！
**Reply:** @guoxili7050 自認讀書比别人多，用  文字上的錯誤貶低別人，如看不懂你怎麼知道錯字，不是考試而是在溝通，因為智就不會被騙煽動而利用，沒上戰場能知誰的膽量呢？
**Translation:** The wise aren't deceived, incited and used; who knows anyone's courage without battle?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Volunteers were 'deceived and used' → CU.

---

### id 36398
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 中华民国的英雄们，望平安归来！自由的曙光与你们同在！
**Reply:** @guoxili7050 那能証明不是為錢嗎？因為庸兵都有高薪才去的，不怕纠正錯字有事說事才能達到溝通目的。
**Translation:** Can you prove it wasn't for money? Mercenaries go for high pay.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — 'Can you prove it's not for money? mercenaries are well paid' → CU.

---

### id 36401
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 中华民国的英雄们，望平安归来！自由的曙光与你们同在！
**Reply:** @張富順-k3u 一千歐元，33000元台幣，在台灣去便利店打工就能有的薪水，上面寫過，你現在還是不知道的重複？果然五毛帳號，換班了！
**Translation:** €1,000 = what a convenience-store job pays… still repeating? A 五毛 account, shift changed!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 1 | 0 | 0 |
| Opus | 0 | **1** | 0 | 1 | 0 | 0 |

**Your call:** Opus (SU+ST) — Rebuts 'for money' (SU) + calls the user 五毛 (ST).

---

### id 36411
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 我打從心裡佩服
**Translation:** I admire you from the heart.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — Generic admiration → SU.

---

### id 36412
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 聖光英雄
**Translation:** Saint-light (曾聖光) hero.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36416
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 台灣人以你們為榮
**Translation:** Taiwanese are proud of you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Taiwanese are proud of you' → ST (your full_data '台灣有你們引以為榮' = ST).

---

### id 36417
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 台灣英雄 加油 平安
**Translation:** Taiwan heroes, go, stay safe.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Taiwan's heroes, 加油' → ST (your '台堮勇士加油' = ST).

---

### id 36418
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 之前在推特上有看到一些台灣志願軍前往烏克蘭支援的情況 從這些台灣志願軍的推文字裡行間裡 看到的是戰爭的殘酷  文章裡兩三天就有人陣亡 請原諒我的私心 在看到台灣志願軍人存活下來時我的內心是慶幸的 這也了解到戰爭離我們只有一線之隔  我們能夠無憂的活著是因為有軍人的戍守 讓我們遠裡戰爭威脅  我認為正向面對戰爭準備這件事情 必須要有身體&心理做好建設及準備  面對 中共 多方的認知、資訊混淆作戰 不僅是戰機、軍.淺艦、航母、飛彈 台灣並沒有深刻的認知 中共在資訊戰、心理戰、輿論戰 是具有"策畫"及"規模"的侵略中華民國(台灣) 這些混亂的資訊讓我一度以為可以透過政治手段而避免戰爭  俄羅斯&烏克蘭戰爭後 這場力量不對等的戰爭 我看到開戰權在俄羅斯手上 而且停戰的決定權也在俄羅斯手上  面對中共戰爭威脅 打不打、打多久、打到什麼時候停、要陣亡多少人 並不是我們能夠決定的  最後 -姑息主義無法造就和平 -榮耀歸於烏克蘭
**Translation:** Long: Taiwan volunteers; war is close; CCP info war; appeasement can't make peace; glory to Ukraine.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 1 | 0 | 0 |
| Opus | 0 | **0** | 0 | 1 | 0 | 0 |

**Your call:** Sonnet (SU+ST) — Volunteers + Taiwan must prepare against CCP cognitive war, 'appeasement brings no peace, glory to Ukraine' → SU + ST.

---

### id 36420
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 應該送到最前線衝鋒陷陣 擺在後面  裝清高  回來替烏克蘭宣傳 戰爭還在打 卻臨陣逃回來   我的看法就是這樣
**Translation:** Should be sent to the front… sitting at the back, coming home to promote Ukraine, fleeing while war goes on.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | **1** | 0 | 0 | 0 |
| Opus | **1** | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (CU) — Attacks the volunteers (fled, propaganda) → CU; nothing on Taiwan's defence.

---

### id 36421
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread (context):** 應該送到最前線衝鋒陷陣 擺在後面  裝清高  回來替烏克蘭宣傳 戰爭還在打 卻臨陣逃回來   我的看法就是這樣
**Reply:** 為什麼你覺得那裡是「後面」？戰場上，每一寸土地都是最前線啊！戰況瞬息萬變！每一位戰士都配有任務在身，即使安坐在烏克蘭首都基輔，隨時都可能會遭受飛彈攻擊⋯⋯這顯現你對戰爭的無知。 裝清高？非得要像曾聖光一樣，光榮戰死才不是「裝清高」嗎？ ⋯⋯這顯現你對戰爭的無情無理。 「替烏克蘭宣傳」？烏克蘭沒有要求他們替烏克蘭宣傳，他們是自願的，自動自發的，著實無可厚非！⋯⋯這顯現你的妒忌，他們有得說的，而你沒有。 「戰爭還在打，卻臨陣逃回來」？他們都算是「外籍傭兵」，烏克蘭政府是和他們簽署合約的，以規定期程、薪資和撫恤等等，期程終止，雙方都可以決定是否續約或是結束合作。⋯⋯ 這顯現你的不明究理，不作功課，逕下批評。 這是個人對你的看法⋯⋯
**Translation:** Why 'the back'? Every inch is the front… they're contracted foreign fighters…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — Defends the volunteers → SU.

---

### id 36425
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 看到媽媽把兒子聖光刺在手上，淚水止不住的滑下來，媽媽你真的好偉大！
**Translation:** Seeing the mother tattoo her son 聖光 on her arm, tears won't stop. You're great, mom!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36427
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** Taiwan is the last hope for the Chinese civilization, and I hope you can liberate the mainland someday!
**Translation:** Taiwan is the last hope for Chinese civilization; I hope you liberate the mainland someday!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — 'Liberate the mainland someday' → ST (your '反攻大陸' label).

---

### id 36428
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 祝願及祈禱所有在烏克蘭的台灣志願軍平安 活著回到故鄉 ! 🙏
**Translation:** Praying all Taiwanese volunteers in Ukraine come home alive! 🙏

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36429
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 真男人
**Translation:** A real man.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36431
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 烏克蘭也把台灣當傻子，請相信我。
**Translation:** Ukraine treats Taiwan as fools too, believe me.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | **1** | 0 | 0 | 0 |
| Opus | **1** | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (CU) — Ukraine fools Taiwan → CU.

---

### id 36433
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 曾聖光是偉人
**Translation:** 曾聖光 is a great man.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36435
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 曾媽令人敬佩
**Translation:** Mother Tseng is admirable.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36436
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 需要多大的胸襟才能如此從容的邁出這一步！打從心裡敬佩你們這群勇敢的英雄！
**Translation:** How big a heart to take this step! I admire you brave heroes.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36437
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 願我光榮的台灣子弟兵能夠平安順利。
**Translation:** May our glorious Taiwanese soldiers be safe.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — 'Our glorious Taiwanese sons' → Taiwan-pride framing → ST.

---

### id 36439
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 只因為一個獨裁者的私利~一場戰爭死了這麼多人~這麼多人失去家園~ 經過一年多悲劇每天都還在上演~台灣必須做好備戰的準備~ 因為台灣不能用一般人的角度去看獨裁者他的下一步會做什麼~ 說一句難聽的~烏克蘭若三兩下就被普丁給拿下~ 說不定習近平已經打台灣~
**Translation:** One dictator's interest killed so many… Taiwan must prepare for war; if Ukraine had fallen fast Xi might have attacked.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 1 | 0 | 0 |
| Opus | 0 | **1** | 0 | 1 | 0 | 0 |

**Your call:** Opus (SU+ST) — Dictator's war (SU) + Taiwan must prepare (ST).

---

### id 36442
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 台灣的好漢 加油
**Translation:** Taiwan's good men, go!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Taiwan's 好漢' → ST (your '台堮勇士加油' = ST).

---

### id 36447
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 真台灣英雄!!!我們的驕傲!!!
**Translation:** True Taiwan heroes!!! Our pride!!!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Taiwan heroes, our pride' → ST (your '台灣之光' = ST).

---

### id 36448
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 反抗暴政 人人有責
**Translation:** Resisting tyranny is everyone's duty.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Resisting tyranny under the volunteer video → SU.

---

### id 36449
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 路見不平仗劍行，掃平賊寇蕩天清，扶弱本是尋常事，眾志抗暴世太平。
**Translation:** Poem: walk with a sword against injustice, help the weak, unite against tyranny.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — Poem on helping the weak → SU.

---

### id 36454
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 感謝您們, 因為有勇敢的您們..台灣沒有在這場為自由而戰的時刻缺席...台灣人不會忘記您們的付出....💕💕💕
**Translation:** Thank you — because of you Taiwan was not absent in this fight for freedom; Taiwanese won't forget.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Thanks them for Taiwan's presence in the fight for freedom → SU (your '感謝您們為台灣過去幫助烏克蘭' = SU).

---

### id 36455
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 為台灣英雄致敬 並送上祝福 成功平安歸來
**Translation:** Salute to Taiwan's heroes, return safely.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Salute Taiwan heroes' → ST (as 36417).

---

### id 36460
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 你們是台灣人的驕傲！
**Translation:** You are the pride of the Taiwanese!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Pride of the Taiwanese' → ST.

---

### id 36461
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 萬分感謝曾聖光！ 曾聖光是為了台灣而戰死在烏克蘭的！ 願天國天父的榮光照耀在曾聖光靈魂。
**Translation:** Thank you 曾聖光! He died in Ukraine fighting for Taiwan!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 1 | 0 | 0 |
| Opus | 0 | **1** | 0 | 1 | 0 | 0 |

**Your call:** Opus (SU+ST) — 'Died fighting for Taiwan in Ukraine' → SU + ST (your '爲烏克蘭也是爲台灣' = SU+ST).

---

### id 36463
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 好勇敢....跟亞速營並肩作戰 !!! 好勇敢....跟亞速營並肩作戰 !!! 好勇敢....跟亞速營並肩作戰 !!!
**Translation:** So brave… fighting side by side with Azov!!! (×3)

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **1** | 0 | 0 | 0 |
| Opus | 1 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (CU) — Same Azov mockery as 36305 → CU.

---

### id 36464
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 我们和搞屠殺的亞速營，一起反抗 我们和搞屠殺的亞速營，一起反抗 我们和亞速營，並肩作戰 ! 我们和亞速營，並肩作戰 !
**Translation:** We resist alongside the massacring Azov… (×4)

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **1** | 0 | 0 | 0 |
| Opus | 1 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (CU) — Azov mockery → CU.

---

### id 36465
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 台灣男兒一出世落土，就注定與地震、颱風，天鬥地鬥過一生 ，勇敢無比。有堅強外語能力，才能外國濟弱。陸軍步兵1456梯次，上等兵向您致敬!!
**Translation:** Taiwanese men are born brave against quakes and typhoons… salute from Army private, batch 1456!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — 'Taiwanese men brave… salute from a private' → Taiwan-pride → ST (your '學弟…台灣有你是種驕傲' = ST).

---

### id 36466
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 向勇士們致敬，曾聖光戰士致敬，台灣人要覺醒，自己國家自己救，自助人助，
**Translation:** Salute to the warriors, to 曾聖光; Taiwanese must wake up, save your own country.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 1 | 0 | 0 |
| Opus | 0 | **1** | 0 | 1 | 0 | 0 |

**Your call:** Opus (SU+ST) — Salute + 'save our own country' → SU + ST.

---

### id 36468
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 曾勝光是自願參加的，沒人想要戰爭，曾女士請你想清楚。
**Translation:** 曾聖光 volunteered; nobody wants war. Ms Tseng, please think clearly.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Addressed to the mother; target and stance unclear → false.

---

### id 36471
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 你們的義舉給台灣堅定自由民主價值的人極大的鼓舞。面對島內親中的政黨媒體作亂，是我們台灣更大的威脅
**Translation:** Your deeds inspire Taiwanese… pro-China parties and media inside are the bigger threat.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 1 | 0 | 0 |
| Opus | 0 | **1** | 0 | 1 | 0 | 0 |

**Your call:** Opus (SU+ST) — Inspires Taiwan + pro-China parties/media threat → SU + ST.

---

### id 36474
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 謝謝台灣好男兒
**Translation:** Thank you, good Taiwanese men.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Taiwan's good men' → ST (as 36442).

---

### id 36477
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 先打敗貪婪無能的國民黨跟民進黨再說吧... 自己的家事都一塌糊塗了還在那跟著起舞？！
**Translation:** First defeat the greedy, incompetent KMT and DPP… your own house is a mess.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks KMT and DPP, dismisses joining in → CT.

---

### id 36478
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 致敬他們的勇氣
**Translation:** Salute their courage.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36479
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 我很欽佩這些英雄們，戰爭是殘酷的，台灣人要清醒，入侵者才不管你是哪個政黨，老祖先造字就已經告訴我們“武＝止戈”，卑微跪求和平不如加強武裝自己，我五十幾歲，年輕時在空特當過傘兵，我願意為家人而戰。
**Translation:** I admire these heroes… better to arm ourselves than beg for peace; I'd fight for my family.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 1 | 0 | 0 |
| Opus | 0 | **1** | 0 | 1 | 0 | 0 |

**Your call:** Opus (SU+ST) — Admiration (SU) + arm ourselves rather than beg for peace (ST).

---

### id 36482
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 戰爭很可怕...  每一個家家戶戶的小孩參與戰爭.. 每一個損失都是每一個家庭的破裂..... 烏俄戰爭還要打多久?! 還要多少人死才會覺悟? 戰死很光榮.. 不是安逸而死...是為國家為了讓平民百姓過著自由的生活而戰死!! 我很敬佩去烏克蘭參加戰爭的人們... 希望世界和平不要再有戰爭....  祝福一切也希望大家能珍惜一切所擁有的...... 唉..
**Translation:** War is terrible… dying for freedom is glorious… I admire those who went… hope for world peace.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **1** | 0 | 0 |
| Opus | 0 | 1 | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Admiration + general anti-war; no Taiwan defence content → SU.

---

### id 36485
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 《聖經》 詩篇	110:3	當你行軍的日子，你的民要以"聖"潔的妝飾為衣，甘心犧牲自己；你少年時"光"耀如清晨的甘露。 約翰一書	1:7	我們若在光明中行，如同 神在光明中，就彼此相交，他兒子耶穌的血也洗淨我們一切的罪。 歌羅西書	1:12	又感謝(天)父，叫我們能與眾聖徒在光明中同得基業。   願曾聖光永遠與上帝的榮光同在，奉耶穌基督的聖名祈禱，阿們！
**Translation:** Bible verses; may 曾聖光 be with God's glory, amen.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Opus (SU) — Prayer for 曾聖光 → SU.

---

### id 36487
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 戰爭是殘酷的，但選擇投降，並放棄前人流血而得到的自由民主，是最不明智的。 謝謝這些台灣志願軍，同時也幫助了台灣。
**Translation:** War is cruel, but surrendering freedom is the least wise. Thanks to these Taiwanese volunteers.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 1 | 0 | 0 |
| Opus | 0 | **1** | 0 | 1 | 0 | 0 |

**Your call:** Opus (SU+ST) — 'Surrender is unwise' (ST) + thanks volunteers (SU).

---

### id 36488
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 你們是台灣的英雄，向你們致敬。
**Translation:** You are Taiwan's heroes, salute.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'Taiwan's heroes' → ST.

---

### id 36496
**Video:** `O0zTHiPC_r0` (台湾志愿军：我们和乌克兰一起反抗)
**Thread:** 真正的國軍英雄
**Translation:** True heroes of the national army.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | **1** | 0 | 0 |
| Opus | 0 | **1** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — 'True 國軍 heroes' → Taiwan-pride → ST.

---

### id 36502
**Video:** `O5kxxsdp740` (耿爽vs美方：要是中国真帮忙 俄乌战场就不是这样了)
**Thread (context):** 就應該這樣，懟回去。 確實，如果我們為俄羅斯提供軍事支援， 俄烏戰爭早就結束了。
**Reply:** @zhuwei455哪裡腫啊，前陣子你們說提供伊朗激光防空，攔截率99%，央視還報導，結果勒？這次不是又抓包是用2019軍演失事照片？為什麼會腫？既然擊落那麼多台戰機，巴國軍機場為何5座基地被空襲？ 用你腦子想想
**Translation:** Your CCTV claimed 99% laser interception… then what? Use your brain.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — Mocks a PRC user's CCTV claims; prompt: jabs at PRC users alone don't qualify → false.

---

### id 36507
**Video:** `O5kxxsdp740` (耿爽vs美方：要是中国真帮忙 俄乌战场就不是这样了)
**Thread (context):** 就應該這樣，懟回去。 確實，如果我們為俄羅斯提供軍事支援， 俄烏戰爭早就結束了。
**Reply:** @彭菲-s2c 幹嘛說自己?又在央視就是全世界了， 就問你 激光防空99% 央視直播 結果呢? 央視餵你啥就信啥，還翻牆跟人吵架 真是標準夾頭
**Translation:** CCTV feeds you and you believe it; climbing the wall to argue.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — Same → false.

---

### id 36514
**Video:** `O5kxxsdp740` (耿爽vs美方：要是中国真帮忙 俄乌战场就不是这样了)
**Thread (context):** 故意找个亚裔面孔来这质问，美国你恶心谁呢？
**Reply:** American side always select asian looking faces to be spoke person, African American for Israel/ Gaza related issues. Indian or middle Eastern look at like for middle Eastern issues. Where is all white faces?
**Translation:** US always picks Asian-looking spokespeople for Asian issues… where are the white faces?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Criticises US choosing ethnic faces as spokespeople → DUS (your '以華制華' label = DUS).

---

### id 36517
**Video:** `O5kxxsdp740` (耿爽vs美方：要是中国真帮忙 俄乌战场就不是这样了)
**Thread (context):** 故意找个亚裔面孔来这质问，美国你恶心谁呢？
**Reply:** 他們最會的 就是以前搞華人就是這樣
**Translation:** That's what they do best — used Chinese against Chinese before.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — → DUS.

---

### id 36518
**Video:** `O5kxxsdp740` (耿爽vs美方：要是中国真帮忙 俄乌战场就不是这样了)
**Thread (context):** 故意找个亚裔面孔来这质问，美国你恶心谁呢？
**Reply:** 還當我們是黃狗 最會互咬
**Translation:** Still treat us as yellow dogs who bite each other.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — → DUS.

---

### id 36620
**Video:** `O5kxxsdp740` (耿爽vs美方：要是中国真帮忙 俄乌战场就不是这样了)
**Thread:** 趕緊秀出中國肌肉  嘴砲是不管用的哈哈哈  用不 到14億的中國韭菜當砲灰 用搖搖欲墜的中國經濟打戰  沒錢可以找習近平拿  趙家人可有錢的
**Translation:** Show China's muscles — trash talk doesn't work; use 1.4bn leeks as cannon fodder with a tottering economy.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Mocks Xi/CCP's economy and war talk → ST (your '中國的東西都要打對折' = ST).

---

### id 36647
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread (context):** 美國現在為了世界盟主之位心胸狹隘、仇恨值太高
**Reply:** @wenwuliu6008 沒問題👍，反正中國人只敢打中國人；應該不會有想打美國領土的想法
**Translation:** No problem 👍 Chinese only dare to fight Chinese anyway.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Jab at Chinese; no Taiwan defence content → false.

---

### id 36663
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 看看高雄廠若沒蓋下去，蔡博士就說對了。美國想法太理想，台灣有台積夜鷹研發部隊
**Translation:** If the Kaohsiung fab isn't built, Dr Tsai is right. US is too idealistic; Taiwan has TSMC's night-hawk R&D.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Disputes 蔡正元 but unclear stance → false.

---

### id 36674
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 不用擔心 護國神父 拜登 說了四次會保護台灣
**Translation:** Don't worry, Godfather Biden said four times he'd protect Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — Sarcasm on US protection → CT + DUS (batch 12 line).

---

### id 36676
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 蔡博士看清了事情的真相，技術不是只存在在高階領導層腦中，高階大多只是決策方向，真正的技術都是中低階在執行，當企業解體人才各自找尋出路時，技術就外流了。
**Translation:** Dr Tsai sees the truth: when the firm is broken up, technology leaks.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Praises 蔡正元 → CT (batch 12: pundit praise = CT).

---

### id 36677
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 兩岸和平統一，最壞情況下的台灣就像今天的香港。兩岸兵戎相見，台灣最好的情況就是今天的烏克蘭。
**Translation:** Peaceful unification: worst case Taiwan is today's HK. War: best case Taiwan is today's Ukraine.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | **0** | **1** | 0 | 0 |
| Opus | **1** | 0 | **1** | **0** | 0 | 0 |

**Your call:** Opus (CU+CT) — Unification at worst = HK, war at best = Ukraine → favours unification (CT); Ukraine as bad outcome (CU).

---

### id 36681
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 跟當年漢翔一樣，武功被廢後人才被別人拉去用
**Translation:** Like AIDC back then: crippled, then its talent poached.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Agrees Taiwan's industry is gutted like AIDC → CT.

---

### id 36682
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 高雄人又被騙了。房價漲了也回不來了，通貨膨脹也回不來了，物價指數高的離譜，薪資漲幅水準跟不上通膨水準，基層人民苦哈哈，蓮池潭及愛河浮屍歷史新高，人口負成長，離婚率也創新高，民進黨難辭其咎啊～
**Translation:** Kaohsiung fooled again… prices, inflation… the DPP can't escape blame.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Blames DPP → CT.

---

### id 36685
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 火燒圓明園！肢解臺基壂！21世紀的七國聯G！
**Translation:** Burn the Summer Palace! Dismember TSMC! 21st-century eight-nation alliance!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — **Borderline** — US dismembering TSMC like the eight-nation alliance → Taiwan as victim/pawn (CT) + DUS.

---

### id 36687
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 昔日王、謝堂前燕！飛入尋常百姓家！
**Translation:** The swallows of the noble halls now fly into common homes.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Classical lament; no clear stance → false.

---

### id 36690
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 年輕人低薪只好出國當台勞甚至當詐騙犯 怎知最後自己被詐騙當豬仔賣活摘器官 而政府忙著搞假學歷 忙貪汚分贓 忙假宣傳 忙選舉 台灣人命賤如螻蟻 政府在那 最支持詐騙貪汚集團的不就是這些好儍好天真好好騙的年輕人嗎？ 可悲
**Translation:** Young people low-paid, sold as scam slaves… government busy with fake degrees and graft.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks government (fake degrees, corruption) → CT.

---

### id 36699
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 請問蔡正元先生為什麼馬英九及其羣衆都揮舞著帶有綠底的國民黨黨旗？是否想以假亂真誤以為你們也民進黨？還是和中國國民黨區分，我們不知道，怎麼可以不経黨員同意就改黨旗？什麼時候黨旗加上綠底。
**Translation:** Mr Tsai, why do 馬英九 and his crowd wave a KMT flag with a green background?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Mocks 馬英九/KMT flag → ST (prompt: mocks 馬英九).

---

### id 36702
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 是美國拆散風險在前呢，啊共全攔抱炮台在前，都有時間次序，先當解決是啊共，怎會是美國搬去也沒夜班苦夜鷹工
**Translation:** The US splitting TSMC vs the CCP threat… solve the CCP first.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Garbled, but says the CCP is the threat first, not the US → ST.

---

### id 36703
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 美國怎麽拆台積電，台灣如果拒絕台積電也拒絕，如何拆，最多投降靠中國，如果日本肯接受也不錯
**Translation:** How could the US break up TSMC… at most we surrender to China; Japan would also be fine.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — 'At most surrender to China' → CT.

---

### id 36704
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 台灣台積電在台灣美國敢來拆掉民進黨不怕死去跟美國打民進黨站出來說假話不怕死民進黨太惡劣  欺負攻擊抹黑我們好人，   台積電在台灣美國敢來拆掉民進黨不怕死去打美國敗登民進黨去打我也幫忙打美國敗登民進黨不怕死民眾去告鄭運鵬假貨民進黨不要臉殺人放火害死台灣人鄭運鵬一年四季說假話民進黨詐騙，   陳時鐘死民進黨殺人放火害死台灣人，   我的兒女沒飯吃，不幫兒女煮飯還要把兒女飯碗搶走，   我沒資格當老大去死美國敗登民進黨殺人放火害死台灣人
**Translation:** Long rant: DPP liars, killers, harm Taiwanese…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Rant against DPP → CT.

---

### id 36705
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 呂秀蓮的邏輯是因為共產黨消滅了中華民國，所以民進黨可以不承認中華民國，那民進黨和共產黨有什麼差別？
**Translation:** 呂秀蓮's logic… then how is the DPP different from the CCP?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP/呂秀蓮 logic → CT.

---

### id 36708
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 犧牲抹😂⋯想抹黑台積電？救自己的晶片安全？如果老習會信你！那明天出太陽了⋯ 我勸張董！凡事留青山不會被財燒⋯ 主導權要在自立不搖的情況之下才能生存。  簡單說商業手段的犧牲品⋯ 不過飛官這麼多離難！我想大家會說 我自己來！😮‍💨⋯⋯想保護別人！先想清楚 自己保不保的住。
**Translation:** Smearing TSMC? … a sacrifice of business tactics… before protecting others, see if you can protect yourself.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Garbled; 'sacrifice of business tactics', 'can you protect yourself' → CT.

---

### id 36711
**Video:** `P3M0oVkxmsI` (為棄台鋪路? 美國著手支解台積電? 蔡正元:窩一打散鳥到處飛恐引火燒身@中天新聞CtiNews)
**Thread:** 若中國自由民主。。台灣一定靠過去。。但中國還是中國嗎？  奴隸思想不是那麼好解除的
**Translation:** If China were free and democratic Taiwan would lean over… but is it still China? Slave mentality.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — If China were free Taiwan would join, but slave mentality → ST.

---

### id 36731
**Video:** `PEoo6ypi0ks` (真實的俄烏戰場和你想象中的差距有多大 #軍事科普 #軍事愛好者 #軍事迷 #軍迷發燒友)
**Thread (context):** 保家卫国，还被人嘲笑. 想想300万平方公里的外东北，也是这样被俄国人一口一口吃掉的.
**Reply:** 還要在華文圈自幹幫人宣傳,加工宣傳比克宮有過之而無不及..................
**Translation:** (Parent: defending homeland mocked; remember Outer Manchuria) Reply: Still self-funded Kremlin propaganda in the Chinese sphere…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Attacks those doing Kremlin propaganda in Chinese → SU.

---

### id 36734
**Video:** `PEoo6ypi0ks` (真實的俄烏戰場和你想象中的差距有多大 #軍事科普 #軍事愛好者 #軍事迷 #軍迷發燒友)
**Thread (context):** 1.食物只有罐頭跟麵包，想吃其他東西自己買。 2.水要自己搶，或自備。 3.高科技裝備要自備（我大概花了30萬）。 4.基本薪資2萬烏幣、戰鬥加給10萬（有部署才有。 5.防守跟進攻任務都有看你的運氣。 6.俄羅斯的砲彈還有自殺無人機可以炸你的陣地一整天。 7.合約一簽半年，半年後可以走或是繼續留著。 烏克蘭國家安全局服役8個月的心得。
**Reply:** 在嘛？ 願你安好 希望能看到你持續留言分享更多
**Translation:** Are you there? Hope you're well, please keep sharing.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — Wishes the Taiwanese volunteer well → SU.

---

### id 36735
**Video:** `PEoo6ypi0ks` (真實的俄烏戰場和你想象中的差距有多大 #軍事科普 #軍事愛好者 #軍事迷 #軍迷發燒友)
**Thread (context):** 1.食物只有罐頭跟麵包，想吃其他東西自己買。 2.水要自己搶，或自備。 3.高科技裝備要自備（我大概花了30萬）。 4.基本薪資2萬烏幣、戰鬥加給10萬（有部署才有。 5.防守跟進攻任務都有看你的運氣。 6.俄羅斯的砲彈還有自殺無人機可以炸你的陣地一整天。 7.合約一簽半年，半年後可以走或是繼續留著。 烏克蘭國家安全局服役8個月的心得。
**Reply:** 祝福你平安回來台灣
**Translation:** Wish you return safely to Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — → SU.

---

### id 36743
**Video:** `PEoo6ypi0ks` (真實的俄烏戰場和你想象中的差距有多大 #軍事科普 #軍事愛好者 #軍事迷 #軍迷發燒友)
**Thread (context):** 按照美國川普的做法，美國、俄羅斯及烏克蘭能和平相處，烏東四省及克里亞米半島舉行人民公投會是公平做法-東方國家、西方國家或中立國媒體全程直播，人民公投結果-國際要承認；但烏克蘭違反西元1990年的獨立宣言-中立主義及不加入任何軍事組織是事實。西元2014年烏克蘭廣場事件跟克里米亞半島是串在一起的事件-因為違反外交的中立主義，怎麼不説廣場事件是其他國家收買烏克蘭的反對勢力-違反外交的中立主義
**Reply:** 你去當地跟當地人這樣說
**Translation:** (Parent: referendums in occupied regions are fair) Reply: Go say that to the locals.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Retort to a pro-Russia referendum claim → SU.

---

### id 36749
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread (context):** 把台灣的禍害處掉
**Reply:** 十1❤
**Translation:** (Parent: get rid of Taiwan's scourge) Reply: +1 ❤

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — '+1' to 'get rid of Taiwan's scourge' — target unclear → false.

---

### id 36753
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread (context):** 蔡老師也太悲觀了！只要老共不下決心要奪取台灣，台灣還是有機會的。但，戰事一起，老共必定是下了決心的，這時，台灣的機會還真是渺茫。
**Reply:** 大陸老百姓早就不耐煩了，老共也是有壓力了
**Translation:** (Parent: Tsai too pessimistic) Reply: Mainland people are long impatient; the CCP is under pressure too.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Unclear direction → false.

---

### id 36755
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread (context):** 解散國防部，裁撤外交部 (改設外貿署專職推銷台灣產品)，把省下來的錢發展全民免費醫療。打造全民終生教育體系(針對產業需求對接，靈活開課，結業即有工作)，並實施幼稚園到大學免學費，國家統一規劃70歲後免費養老及身後安排系統。擴編警政署，警力社區化，消滅黑幫，毒品，詐騙。重塑富而好禮社會，建設台灣為世界級的幸福之島。
**Reply:** @alexhuang1734 讚同
**Translation:** (Parent: dissolve MND and MOFA, spend on welfare) Reply: Agree.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Endorses 'dissolve the defence ministry' → CT.

---

### id 36756
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread (context):** 解散國防部，裁撤外交部 (改設外貿署專職推銷台灣產品)，把省下來的錢發展全民免費醫療。打造全民終生教育體系(針對產業需求對接，靈活開課，結業即有工作)，並實施幼稚園到大學免學費，國家統一規劃70歲後免費養老及身後安排系統。擴編警政署，警力社區化，消滅黑幫，毒品，詐騙。重塑富而好禮社會，建設台灣為世界級的幸福之島。
**Reply:** 聰明👍
**Translation:** (Same parent) Reply: Smart 👍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Same endorsement → CT.

---

### id 36770
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread (context):** 兩岸早日統一，不用打架，早日安寧。✌️🎈🎈🎈
**Reply:** +1
**Translation:** (Parent: unify early, no fighting) Reply: +1

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — '+1' to early unification → CT.

---

### id 36771
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread (context):** 兩岸早日統一，不用打架，早日安寧。✌️🎈🎈🎈
**Reply:** @trouble·1256沒有吧！我看是滿渴望的啊！什麼時候打過來啊
**Translation:** (Parent: unify early) Reply: No! I see they're eager — when are you coming over?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — Defiant dare ('when are you coming?') → ST (prompt calibration).

---

### id 36797
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 台灣福建的高速公路，台灣該吃下建設費用😊
**Translation:** Taiwan–Fujian highway — Taiwan should cover construction costs 😊

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Taiwan–Fujian highway, Taiwan should pay → CT.

---

### id 36799
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 我是從台灣來的，你要找死，就想信老美！
**Translation:** I'm from Taiwan: if you want to die, trust the Americans!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — 'Trust the US and die' → CT + DUS.

---

### id 36802
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 現在的臺灣人就像戰前的烏克蘭人一樣，根本沒有感到身邊即將發生的戰爭危險。很多人還在天真地幻想美國的保護，甚至還想著靠美股發大財。台海戰爭的導火索早已被台獨分子點燃。俄羅斯無法容忍烏克蘭加入北約，難道大陸就能容忍身邊有一個敵國的堡壘嗎？忍無可忍，就無需再忍，終有一天台海會被燃爆。屍橫遍野，遍地殘垣的景象固然恐怖，但想想當今臺灣人對待美國和大陸的態度，大陸方面也就无須有半點憐憫之心了。
**Translation:** Taiwanese are like pre-war Ukrainians… fantasising about US protection… Russia can't tolerate NATO, can the mainland tolerate an enemy fortress?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | 1 | 0 | **0** | 1 |
| Opus | 1 | 0 | 1 | 0 | **1** | 1 |

**Your call:** Opus (CU+CT+DUS+BNE) — Adds DUS: 'naively fantasise about US protection'.

---

### id 36803
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 當美國是個屁！真是人間清醒
**Translation:** Treat the US as a fart! Truly clear-headed.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — Praises the pundit's view (CT) + US is nothing (DUS).

---

### id 36805
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 不對稱戰爭的意思，就是勿忘在莒的現代版啦！😅😅😅
**Translation:** Asymmetric warfare is just the modern 'remember Ju' 😅

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Sarcasm with unclear target → false.

---

### id 36810
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 中國敵人多。不要老是想打台灣。中共一對台海、南海用兵。印度就上喜馬拉雅山搶占水源。水源大家都要。巴基斯坦也一起上山搶。還有，瀾昌江的水壩卡住了湄公河水流。越南也要搶占瀾昌江水壩區。西邊還有泛土庫斯坦武裝說要拿回新疆和烏魯木齊。加上國內有討薪的，包圍銀行的，獻忠的，. . . 中共焦頭爛額了。
**Translation:** China has many enemies; don't keep wanting to attack Taiwan… India, Vietnam, Xinjiang… the CCP is in trouble.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — China has too many enemies and troubles to attack Taiwan → ST.

---

### id 36821
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 中國該強悍強力發起大復興時刻!!
**Translation:** China should launch its great rejuvenation forcefully!!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 36823
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 就問台美有再打一場韓戰越戰的決心跟籌碼嗎？
**Translation:** Do Taiwan and the US have the resolve and chips for another Korean or Vietnam War?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — Questions US resolve → CT + DUS.

---

### id 36824
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread (context):** 就問台美有再打一場韓戰越戰的決心跟籌碼嗎？
**Reply:** 美軍在那兩場戰鬥都輸中國！
**Translation:** The US lost to China in both wars!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — US lost to China → DUS.

---

### id 36833
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 不要小看川普手段毒辣,台灣乃世界的奶酪,就論大陸自己經經濟軍事政權已開始搖動,想要冒犯東方西方世界必有大難。
**Translation:** Don't underestimate Trump's ruthlessness; Taiwan is the world's cheese; China's regime is shaking — it would face disaster.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | **0** | 0 |
| Opus | 0 | 0 | 0 | **1** | **1** | 0 |

**Your call:** Other (ST) — **Borderline** — Warns China it would face disaster; Trump line is a warning to China, not distrust → Other: ST.

---

### id 36836
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 掃把
**Translation:** Broom.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — '掃把' (broom-defence meme) mockery → CT (your '掃把' labels).

---

### id 36838
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 蔡博士說得好：不要理會川普
**Translation:** Dr Tsai said it well: ignore Trump.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — Praises 蔡正元 (CT) + 'ignore Trump' (DUS).

---

### id 36846
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 我們國家已經很強強了。不用靠美國。日本啦。大陸對我們的欺壓。執政黨不要喊抗中保台了。直接跟大陸開戰。我們老百姓不會怕死
**Translation:** Our country is already strong-strong. No need for the US, Japan… ruling party stop shouting 抗中保台, just fight the mainland. We're not afraid.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | **1** | 0 | 0 |
| Opus | 0 | 0 | **1** | **0** | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Reads as sarcasm at the DPP ('just go to war with the mainland') → CT.

---

### id 36852
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 蔡博士是台灣的正義力量❤❤❤❤
**Translation:** Dr Tsai is Taiwan's force of justice ❤

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Pundit praise → CT.

---

### id 36853
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 蔡老師說的太好了😊
**Translation:** Mr Tsai said it so well 😊

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Pundit praise → CT.

---

### id 36858
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 黑熊青鳥已經去蘇家領掃把 準備跟共軍一决生死。 但是美國爸爸不會理你們的
**Translation:** Black Bears and blue birds got brooms ready… but US daddy won't care about you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — → CT + DUS.

---

### id 36862
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 台灣不用擔心外國的攻擊， 他們是在找S。台灣要擔心的是，國內的台奸，賣國賊！
**Translation:** Taiwan needn't fear foreign attack… worry about the traitors at home!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — Worry about traitors inside → ST (your '台灣內賊太多' = ST).

---

### id 36864
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 美國佬會護臺，笑話😂😂😂
**Translation:** The Yankees will protect Taiwan — a joke 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — → CT + DUS.

---

### id 36865
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 賴X頭和澤倫司機很8分像，硬頭人士，
**Translation:** Lai X-head and Zelensky the driver are 80% alike, hardheads.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 1 | 0 | 0 | 0 |
| Opus | **1** | 0 | 1 | 0 | 0 | 0 |

**Your call:** Opus (CU+CT) — 賴 = 'driver' Zelensky → CU + CT.

---

### id 36874
**Video:** `PdX_-ZCTsrw` ("解放軍"準備好了?!川普真會協防台灣?蔡正元曝"出手時機")
**Thread:** 協個P,老共只要公開宣誓，想打仗的留下來，不想打的老共安排特區和走人道走廊暫收保護，台灣立馬股匯房市大爆跌....如果癩不准台客走人，牠們會被爆怒台客拖下去打，永遠不要激怒沉默的老實人，企業和有錢人跑光光，拿甚麼錢付保護費
**Translation:** Defend my ass… Taiwan markets crash… what money to pay the protection fee?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | **0** | 0 |
| Opus | 0 | 0 | **1** | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — Dismisses US defence (協個P, protection fee) → CT + DUS.

---

### id 36882
**Video:** `PwBldfM1DRg` (🔥提防中共對台心理戰：美國棄台論 台軍無能論！｜新聞大破解 #shorts)
**Thread (context):** 支持中國政府盡快用強大的武力來消滅囂張氣焰和令人討厭的臺灣人。
**Reply:** 你都死到臨頭還剩一張嘴，無魂的鬼，還要鬼話連篇嗎？
**Translation:** (Parent: wipe out the Taiwanese) Reply: You're near death with only a mouth left, soulless ghost.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Plain insult to a PRC user → false (batch 9 rule).

---

### id 36883
**Video:** `PwBldfM1DRg` (🔥提防中共對台心理戰：美國棄台論 台軍無能論！｜新聞大破解 #shorts)
**Thread (context):** 自己都不打為什麼希望別人幫你打
**Reply:** 有道理
**Translation:** (Parent: you won't fight yourself, why want others to fight for you) Reply: Makes sense.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — 'Makes sense' to an ambiguous parent → false.

---

### id 36897
**Video:** `PwBldfM1DRg` (🔥提防中共對台心理戰：美國棄台論 台軍無能論！｜新聞大破解 #shorts)
**Thread:** 達妳馬后啊，台灣島自古以來就是台灣省，妳底類功莎洨？
**Translation:** (Insult) Taiwan island has been Taiwan province since ancient times.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Insult; '自古以來' line reads as parody, direction unclear → false.

---

### id 36900
**Video:** `PwBldfM1DRg` (🔥提防中共對台心理戰：美國棄台論 台軍無能論！｜新聞大破解 #shorts)
**Thread:** 問題是拜登親口證實不會出兵幫助台灣
**Translation:** Problem is, Biden himself confirmed he won't send troops to help Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — → CT + DUS.

---
