# Disagreement Review: ids 43785–44636 (event test, batch 20)

700 rows labeled, 553 agreed (79.0%), 147 disagreements below. Run 1 = `claude-sonnet-5`, run 2 = `claude-opus-5`. Only non-Simplified event-test comments. 4 videos: `ox2SixSPe6A` 台積電/郭台銘 (501 rows, the end of this video), `oyspwiplSQM` 俄烏戰爭結束的七種可能 (50), `p69gHaD88U0` 這裡就是台灣 (4), `pa52xbqjW20` 下班瀚你聊/明居正 (first 145 of 284). Disagreements by video: `ox2SixSPe6A` (117), `pa52xbqjW20` (21), `oyspwiplSQM` (8), `p69gHaD88U0` (1). Disagreement rows: 117 thread_only, 30 thread_with_comment.

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion. Bold = the labels where the runs differ.

Precedent used for "Your call": your batch 1–19 decisions (mainly the 148 batch 18–19 rows on `ox2SixSPe6A`), your 20763 in `full_data.db`, and `labeling_prompt.md`. None of the 4 videos is in `full_data.db`.

My calls: 105 Opus, 36 Sonnet, 6 other. 68 marked **Borderline**.

**Main patterns.**
- **TSMC / Gou short** (`ox2SixSPe6A`, 117 rows). Sonnet gave CT to almost every brain-drain comment; Opus gave false or DUS. I kept the batch 18–19 lines:
  - **Bare '掏空台灣' / 'talent leaves, what's left' / government complaints** with no party, 賣台, China or defence content → **false** (batch 19, 43689 '掏空台灣人才，我們政府卻無動於衷？' = false). 44 rows where Sonnet had CT and my call is all false. This is the main place you may want to flip: if bare 掏空 should be CT, tell me and I'll change them all.
  - **DPP / 綠 / 塔綠班 + US takes Taiwan's talent** → **CT+DUS** (batch 19, 43083). 'TSMC / talent given to the US' → **CT+DUS** (your 20763).
  - **US is lazy, unsafe, racist, uses and discards workers** → **DUS** only.
  - **40% / president jabs** (43829, 43856, 43919) → **CT**.
- **明居正 talk** (`pa52xbqjW20`, 21 rows): 'the US can't drop Taiwan, it would lose Japan/Korea/the dollar' → **ST** (Opus; pro-alliance, prompt example '美國幫台灣容易'). Replies arguing a US official's 'Taiwan isn't vital' post is US policy → **DUS** (Sonnet). Calling 李登輝 a Communist mole/traitor → **CT** (44021, 44463, 44465; borderline).
- **Others (6):** 43820 → DUS; 43865 → CT+DUS; 43872 → CT+DUS; 43990 → CT+DUS; 44098 → CT+DUS; 44186 → all false.

**Note on the runs:** both `claude -p` runs used only SELECT and INSERT (no UPDATE, DELETE, DROP, ALTER or CREATE), exactly 700 rows each, every id labelled once per run, no rows marked both critical and supportive. Sonnet tried twice to write a helper .sql file (/tmp and `.labeling_tmp/` in this folder), Opus once (/tmp); all were blocked and no file was created.

---

### id 43787
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣如果能夠有勇氣敢𣎴去. 美國只有挺台灣到底. 絕對不會拱手給中共。那是她自己的生死交關。一但台灣被掏空了。就不一樣了。但是政府和生意人都是腳踏兩條船.  結果可能掉落海裏.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — 'The US will back Taiwan to the end, never hand it to the CCP' — confidence in US defence of Taiwan → ST (prompt example '美國幫台灣容易…').

---

### id 43791
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 移民美國久了 就會感染變成懶惰的美國人最後還是會淪落，美國還是搞不起來的 這就是美國的文化 只會享樂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Americans lazy, US culture only enjoys itself → DUS (batch 19, 43352).

---

### id 43793
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 有人懷疑美國搞不成， 只要把人才都吸走， 怎可能搞不成。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — 'Just suck all the talent, how could the US fail' — neutral remark on US strategy, no clear distrust → false (batch 19, 43506).

---

### id 43794
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 等沒有利用價值就會被趕回去悲哀!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — 'Once no longer useful they'll be sent back' → DUS (batch 19, 43098).

---

### id 43798
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台積電沒骨氣跟軟弱無能逢美必跪舔的政府連手掏空台灣可悲可惡😢😢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — TSMC and a government that 'kneels to the US' hollow out Taiwan → CT+DUS (batch 19, 43083).

---

### id 43801
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 民進黨幫美國把台灣變成三等殖民地！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — 'DPP helps the US turn Taiwan into a 3rd-class colony' → CT+DUS (batch 19, 43083).

---

### id 43814
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台積電美國廠就當送給美國吧，錢可以再賺，你人才.經驗都給美國那就蠢了。我的意思就是拖或者只出一分力去發展美國

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Advises giving the US fab only token effort, not talent → treats the US as a taker → DUS.

---

### id 43816
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 美國希望台灣工程師能落地生根，繁衍優良基因的後代，才會希望工程師全家移民，這樣美國的未來才會更加強大，將來就會有更多的黃仁勳.蘇姿丰，聰明。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — US wants engineers to settle and raise talented children — no distrust → false.

---

### id 43820
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 如果是我我才不移民
到別人的國家你永遠只能是次等公民
講的再好聽都沒用
把自己的國家做大做強不好嗎？
國家強了誰敢看不起你
別人家對你好永遠只是在畫大餅

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | **0** | 0 |
| Opus | 0 | 0 | 0 | **1** | **1** | 0 |

**Your call:** Other (DUS) — **Borderline** — 'In someone else's country you're always a second-class citizen… just 畫大餅' → DUS; 'make your own country strong' is not defence/resolve content → no ST.

---

### id 43822
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 外籍勞工引進來，高階人才移出去，就是目前的台灣政府。愚民越多越好操控。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Generic '政府' complaint (migrant workers in, talent out); no party named → false (batch 18, 42729).

---

### id 43829
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 頂尖人才不斷往外送才可以讓政客繼續詐騙台灣40%的低智民眾

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — 'Politicians keep scamming Taiwan's 40% low-IQ people' — 40% = 賴's vote share → mocks DPP voters → CT (batch 19, 43031).

---

### id 43832
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 當中華民國臺灣長期培養
專業人才移民美國後？？
國家安全堪憂與國安危機

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Worry about national security after talent leaves — concern, not hopeless/mocking → false.

---

### id 43834
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 如果真的如此，台灣危矣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — 'If true, Taiwan is in danger' — conditional worry → false (generic talent-drain line).

---

### id 43835
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 如果真的如此，台灣危矣
**Reply:** 美國沒有什麼做不出來，若沒有其他產業補上去，幾年內就會發生

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — US can do it if other industries don't fill the gap — observation → false.

---

### id 43836
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 如果真的如此，台灣危矣
**Reply:** 技術都流出國外的還有什麼不可能

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Tech already flowing abroad, anything is possible' → false.

---

### id 43856
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 到底為什麼我們要被40%的人拖下水

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — 'Why are we dragged down by the 40%' — jab at DPP voters → CT (same as 43829).

---

### id 43862
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 還在培養美國牛馬干什麼。掏空賣台

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — **Borderline** — 'Still training US 牛馬… 掏空賣台' → 賣台 jab → CT (batch 19, 43056) + US exploitation → DUS.

---

### id 43865
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台積電送給美國🤣🤣🤣🤣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Other (CT+DUS) — **Borderline** — 'TSMC given to the US 🤣' → your 20763 ('那我們送台積電幹嘛啊？' = CT+DUS).

---

### id 43868
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 哈哈哈 把頂尖人才往外送😂
這不是掏空台灣是啥
久而久之技術自然就外流了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — 'Isn't this hollowing out Taiwan' with no party/賣台/China content → false (batch 19, 43689 '掏空台灣人才' = false).

---

### id 43872
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 呆完豬仔  就像  清朝末年  開發巴拿馬運河 的  苦力華工  用完即丟，好騙  好用  好便宜 ✌️

爆肝趣吧  🤣🤣

⚠️  人生誠可貴  莫為權貴死  不養慣老闆！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Other (CT+DUS) — Same copy-paste '呆完豬仔… coolies, used and discarded' as batch 19 43443 → CT+DUS.

---

### id 43876
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 就說乾脆成為美國的一州，這樣美國也不缺工，台灣也少污染，最好那些「慣老闆」也過去，台灣再培植一些中小企業，這次別再讓那些藍綠後人來執政了，小小的地方也不需要那麼多律師、法官（成績那麼好就該到美國競爭，看看會不會進化成人），夠用就好。以後大家用的是美金，薪水會多一點，而且以後大家頭頂著強國的名號就不會那麼自卑了。剩下願意留下來的人（應該只剩下老人了），回到自給自足的生活，台灣可能會成為養老聖地，一切都挑不出毛病。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Sarcastic 'become a US state' rant against both 藍綠; sarcasm direction unclear → false (prompt: ambiguous sarcasm → false).

---

### id 43878
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 亞洲人適合做奴工？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Opus (all false) — **Borderline** — 'Asians suited to be slave labour?' — terse question, target unclear → false (batch 19, 43547).

---

### id 43882
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣高素質的人力都去美國，台灣的錢和人才都被掏空了，台灣辛苦教育出來的人才，辛苦累積的財富，美國輕易就帶走了。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — **Borderline** — Money and talent hollowed out, the US takes them easily — Taiwan left with nothing → CT+DUS (batch 18, 42699).

---

### id 43885
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 人才送美國 然後台灣人基本給底薪 
不然就用外勞

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Talent to the US, locals get minimum wage or migrant workers — generic → false.

---

### id 43894
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 快走快走，不愛台灣一定走，效忠美國做小狗🥳🥳

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Mocks emigrants as 'US little dogs' — contempt at the emigrants, not distrust of the US → false.

---

### id 43895
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 人才都被挖走了，以後半導體？？?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Talent poached, what about semiconductors later??' → false (generic).

---

### id 43900
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 中國指定選總統的郭台銘

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — '郭台銘, the president China picked' → KMT-collaborator jab → ST (batch 19, 43028).

---

### id 43901
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 一個國家要再次偽大：即要如此的幹！
21世紀AI.偽大國家再次領先地位！
一個再次偽大：又一個跪舔哭：卑賤的：討偽大關愛眼神！
何來高低？何德何能？高不如次倒高人一等啊！
華爾街杠杆罪高合併準則！
完美！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Garbled mockery of the US as '偽大' (fake-great) → DUS.

---

### id 43910
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 挖空 掏空 撈光 ••• 剩下的人和事物和共慘黨打毀滅戰，台灣沒了，共慘國也元氣大傷毀了 😊

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — 'Hollowed out… the rest fight the CCP to mutual destruction, Taiwan gone' — fatalistic → CT.

---

### id 43915
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 對留在台灣的台積電員工情何以堪？同事可以移民美國、領美金、過美式生活，自己呢？這樣還有人才願意留在台灣嗎？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Sympathy for TSMC staff who stay — generic → false.

---

### id 43919
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 甚麼總統 
做出甚麼樣的執政能力 
甚麼政策 
顯示出總統甚麼樣的智商

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks the president's governing ability and IQ → mocks 賴 → CT.

---

### id 43920
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 錢掏空，人也掏空

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Money hollowed out, people too' — 掏空 alone → false (batch 19, 43689).

---

### id 43923
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 無能的帶領專業 中華民國悲劇

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — 'Incompetents lead the professionals, ROC tragedy' — mocks the government's leadership → CT (batch 19, 43031).

---

### id 43927
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 滅台

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — '滅台' — one word, unclear → false.

---

### id 43928
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣再過幾年就沒牌了，跟烏克蘭一樣，你覺得？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 1 | 0 | 0 | 0 |
| Opus | **0** | 0 | 1 | 0 | 0 | 0 |

**Your call:** Sonnet (CU+CT) — **Borderline** — 'In a few years Taiwan has no cards, like Ukraine' → Taiwan hopeless (CT) and Ukraine without cards (CU).

---

### id 43946
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 是我的話，一定會帶全家人去。
成為美國人，子子孫孫從此遠離「地緣戰爭風險」。
**Reply:** 去當二等公民！？動蕩時，ㄧ定先修裡你!看看各國華人血淚史！！😢😢😢😢😢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — 'Go be second-class citizens… history of Chinese blood and tears' (US racism) → DUS (batch 19, 43716).

---

### id 43954
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 千萬不要熱臉貼冷屁股，還主動跑到人家當社畜

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 'Don't press a warm face to a cold butt' (about going to the US) → DUS.

---

### id 43957
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 就是掏空台灣的人才、產業、錢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Hollowing out Taiwan's talent, industry, money' — 掏空 alone → false (batch 19, 43689).

---

### id 43979
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 綠鬼通美神,掏空台灣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — '綠鬼通美神, hollowing Taiwan' → DPP + US → CT+DUS (batch 19, 43083).

---

### id 43980
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 強摘的瓜不會甜
美國去走台積電
營運會有困難

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 'A forced melon isn't sweet' — US forcing TSMC over will fail → DUS.

---

### id 43983
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 塔綠班與塔美班同流合污，掏空台灣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — '塔綠班 and 塔美班 collude to hollow Taiwan' → CT+DUS (batch 19, 43083).

---

### id 43990
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台積電被搶連帶人才打包帶走，那台灣剩下什麼護國神山?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Other (CT+DUS) — **Borderline** — TSMC 'robbed' with its talent, 'what 護國神山 is left' → Taiwan left with nothing → CT+DUS (batch 18, 42699).

---

### id 43993
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 這就是當初老美不想讓老鍋當總統的原因

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — 'That's why the US didn't want Gou as president' — unclear claim → false.

---

### id 43994
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 小孩都在美國了 ，當然要讓美國再次偉大，

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — 'Their kids are in the US, of course they make America great' — jab at officials serving the US → CT (batch 19, 43373 was CT+DUS; no US distrust here).

---

### id 44005
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 掏空台湾让美国再次伟大😂😂😂
**Reply:** 掏空台灣，讓中國遙遙領先

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — 'Hollow out Taiwan so China leads' — sarcastic 掏空 remark, no party/China stance → false.

---

### id 44007
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 錢、技術、人才，都被美國搶去，台灣還剩下什麼😢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — **Borderline** — 'Money, tech, talent all grabbed by the US, what's left for Taiwan 😢' → Taiwan left with nothing → CT+DUS (batch 18, 42699).

---

### id 44021
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣自己不做死就不會死、跟經國號戰機一樣！當台灣有能力製造飛機時、美國就同意賣飛機、最後團隊解散、被韓國接收、不到3、5年就把飛機造出來了！李登輝就是台灣最大的賣國賊！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 1 | 0 |
| Opus | 0 | 0 | **0** | **1** | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — **Borderline** — US blocked the IDF fighter programme (DUS); '李登輝 is Taiwan's biggest traitor' → attack on the green camp's icon → CT.

---

### id 44027
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣就慢慢被掏空，人才留不住，又少子化，再過十年，滿街都是東南亞人了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Talent leaves, low birth rate, streets full of SE Asians — generic → false.

---

### id 44030
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 掏空台灣。加油

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — '掏空台灣。加油' — 掏空 alone → false.

---

### id 44034
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 郭台銘董事長說得好沒錯，美國沒那麼好移民啊，你即使今天在美國生小孩你也沒有辦法拿到真正的綠卡小孩必須住滿年滿12歲以上才開始算耶😂不要以為在美國生了小孩就有綠卡了😅！工程師也只有永久居留權取得永久居留權家人又不能依親！一個工程師拿到了永久居留權可是你的家不在那裡呀？美國社會這麼亂還是考慮考慮吧？在台灣是高級工程師，人人仰慕、去了美國就是高級勞工😂👍🏻👍🏻👍🏻👍🏻

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — US hard to immigrate, chaotic society, 'high-level labourer' → DUS (batch 19, 43233).

---

### id 44043
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 溫水煮蛙掏空台灣!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Boiling frog, hollowing Taiwan!' — 掏空 alone → false.

---

### id 44052
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 20年的牛馬訓練

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — '20 years of 牛馬 training' → false.

---

### id 44057
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣就業環境太差了，美國整完端走

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — 'Taiwan's job market is bad; the US takes everything' → DUS (no party/finished content).

---

### id 44062
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 能夠消費的，都跑出去 😑😑，美國再次偉大，台灣再次雖小😡

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 'America great again, Taiwan unlucky again 😡' → DUS.

---

### id 44065
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 川普前一任不是要在美投資設廠！地都買了川普也去剪綵了，結果……不是也曾要在高雄軟體園區找上萬工程師，現在有多少了？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — Trump's earlier US-factory promises (Foxconn Wisconsin) came to nothing → US promises unreliable → DUS.

---

### id 44066
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 臺灣缺工~
還在臺灣挖走優質的工程師！
掏空臺灣優質的工程師，還不對臺灣再好一點...！善待一點！還關稅疊加！哎..哀..癌

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — Taiwan's engineers hollowed out by the US, plus stacked tariffs → CT+DUS.

---

### id 44070
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 以後台灣高級工程師都變美國人 然後台灣剩下傳產跟低薪資工作 還有一堆外勞搶工作 政府太棒了 東南亞第一傳產外勞島
**Reply:** 沒錯，我想當初非洲也如此的，所以會跑會跳的這些人，現在都在歐美，留下來的多半是又瘦又弱。是這樣吧。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Reply comparing to African brain drain → false.

---

### id 44075
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 以後台灣高級工程師都變美國人 然後台灣剩下傳產跟低薪資工作 還有一堆外勞搶工作 政府太棒了 東南亞第一傳產外勞島
**Reply:** ​@錕天下傳產不是不好 科技業賺大錢但是晶片產業外移會對台灣長期造成影響 以後台灣好賺錢恐怕難了 傳產很難跟其他國家比較 目前台灣世界領先還是晶片 可惜賠錢送人

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Reply: chip industry moving out hurts Taiwan long-term, 'given away at a loss' — economic worry, no party → false.

---

### id 44076
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 以後台灣高級工程師都變美國人 然後台灣剩下傳產跟低薪資工作 還有一堆外勞搶工作 政府太棒了 東南亞第一傳產外勞島
**Reply:** ​過去二十年意識型態充斥，很多產業都被犧牲，發生這種結果不意外
​@彩櫻

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Reply: 'past 20 years of ideology sacrificed many industries' — standard jab at DPP ideology → CT.

---

### id 44080
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 去美國賣肝了。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Opus (all false) — **Borderline** — 'Go to the US to sell your liver' — overwork joke, no distrust → false (batch 19, 43547).

---

### id 44082
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 重點是美國有補貼台積電才有辦法給這個薪水
**Reply:** 那是拜登時代 現在還有嗎？連進口台積用的原料都要稅不是

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — Reply: subsidies were the Biden era, now even raw materials are taxed → US tariff complaint → DUS.

---

### id 44083
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣聰明人遲早出走光，有認識台積電的朋友自己問一問就知道環境是什麼樣了，錢給的多但沒有老美能給的多，職場環境要想好還真得移民，進不去的雜魚想擠進去，能進去的天才想賺夠就跑

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Smart people will all leave, TSMC work environment — generic, no party → false.

---

### id 44085
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 整包整個產業鏈拿走
同事都帶小孩過去 當然資產也過去了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — 'The whole industry chain taken' → DUS (batch 19, 43102).

---

### id 44086
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣訓練幾十年的工程師就這樣被賣到美國了，還是無償的。死美國老一點都沒錯。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — Engineers trained for decades 'sold to the US for free… 死美國' → CT+DUS (your 20763).

---

### id 44092
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 有利用價值當然會給。台灣優秀人才都被挖走剩下的，自求多福

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 'Useful, so they give; talent poached' → DUS.

---

### id 44095
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 希望郭董如果設廠，要在挺台灣的盟友設廠，不要在台灣的敵人陣地設廠，不然哪天被充公了，得不償失😅

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Hopes Gou builds plants in Taiwan's allies, not 'the enemy's territory' where they get confiscated → treats China as enemy → ST.

---

### id 44096
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 這就是淘空台灣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'This is hollowing out Taiwan' — 掏空 alone → false.

---

### id 44098
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣培養的高端人才，白白的送给美國

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Other (CT+DUS) — **Borderline** — 'Taiwan's talent given to the US for nothing' → your 20763 (TSMC given away = CT+DUS).

---

### id 44101
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 去去去，都去，最好結束營業整個搬個去

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Go, all go, close and move the whole thing' → false.

---

### id 44102
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 20年的奴性吧

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — '20 years of servility' — unclear target → false.

---

### id 44117
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 哇空台灣，台灣幾十年陪養的半導體技術和人才，全被綁架去霉國

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — 'Hollowing Taiwan… all kidnapped to 霉國' → CT+DUS (batch 19, 43674).

---

### id 44118
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** Taiwan Can Help 🤣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — 'Taiwan Can Help 🤣' — mocks the DPP-era slogan → CT.

---

### id 44131
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 人才外逃，外勞內收

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Talent out, migrant workers in' → false (generic).

---

### id 44133
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 美國晶片中國$10元店都賣不進去😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 'US chips can't even sell in a Chinese $10 store 😂' → mocks the US → DUS.

---

### id 44155
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 很好不只拿錢 拿工作
更要人😅能賺美金了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — 'Not only money and jobs, they want people too' → DUS.

---

### id 44157
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣哪天變外勞地方我也不意外

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Wouldn't be surprised if Taiwan becomes a migrant-worker place' → false (batch 19, 43665).

---

### id 44161
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 人才錢財都移民，老人有帶走嗎?一定沒有。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Talent and money emigrate, old people left — generic → false.

---

### id 44169
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 培養了20年的工程師們….移到了美國！然後，幹個5年，申請就地退休、養老！😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Engineers move to the US then retire there 😂 → false.

---

### id 44170
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣没有政治家（有心人 ）來治國！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — 'Taiwan has no statesmen' — generic, no party → false.

---

### id 44181
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 除了工程師 還有基層的作業也很重要吧，美國人那麼懶一天是能像台灣人站多久做多少事情喔！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Americans are lazy → DUS (batch 19, 43352).

---

### id 44184
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 民進黨把台灣工程師也賣掉給美國，真的悲哀！好不容易培養訓練出來的青英就這樣被美國搶走，台灣還有什麼？民進黨才真正的賣國賊⋯⋯！以前怎麼罵罵英九？民進黨非常惡劣阿霸⋯⋯

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — 'The DPP sold Taiwan's engineers to the US… the US grabbed them' → CT+DUS (batch 19, 43083).

---

### id 44186
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 鳩佔鵲巢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Other (all false) — **Borderline** — '鳩佔鵲巢' — idiom, unclear who takes whose nest → false.

---

### id 44193
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 人才出走  台灣未來在哪裏？？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Talent leaves, where is Taiwan's future??' — generic → false (batch 19, 43614).

---

### id 44194
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 這釜底抽薪之計甚妙~

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 'This 釜底抽薪 plan is clever' — sarcasm at the US taking TSMC's base → DUS.

---

### id 44200
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 淘空台灣,人才外移,技術外移

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — '淘空台灣, talent and tech move abroad' — 掏空 alone → false.

---

### id 44209
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 再高工資都沒用，那麼危險的地方，千萬不要去

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — US too dangerous, don't go → DUS (batch 19, 43401).

---

### id 44215
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 叫航母過來，想要多少載多少走，馬上就成了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 'Send a carrier, load up as many as you want' — sarcasm at the US taking people → DUS.

---

### id 44217
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 竟然現在還有人想移民美國這個亂到爆的國家。。。那就只好祝你好好活著，不會後悔。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — 'Still people want to move to this chaotic US' → DUS (batch 19, 43233).

---

### id 44221
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 別怕，我們政府有引進印度十萬勞力進來替代。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Don't worry, the government brings in 100k Indian workers' — generic government sarcasm → false (batch 19, 43665).

---

### id 44225
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 當工程師都派走了，以後呢?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'When all engineers are sent away, then what?' → false.

---

### id 44239
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 參加美式大逃殺

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — 'Join an American battle royale' — US violence → DUS (batch 19, 43401).

---

### id 44252
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 就不要生病一生病到醫院就完蛋😂😂😂😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — 'Just don't get sick, the hospital will finish you' (US healthcare) → DUS.

---

### id 44253
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 講到重點了吧！整個移走，我看台股還有多厲害。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Move it all, let's see how strong the stock market stays' → false.

---

### id 44257
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 臺勞+ 毒勞… 身心都賭上了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — '臺勞 + 毒勞… body and mind at stake' — US drugs → DUS.

---

### id 44262
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 拼命引進外勞 然後高階工程師一直外流

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Import migrant workers, engineers keep leaving' → false (generic).

---

### id 44263
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 政府三思啊，美國人懶得很，哪能像華人這樣長時效的工作，唉😮‍💨

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — 'Government think twice, Americans are lazy' → DUS (batch 19, 43352).

---

### id 44268
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 臺灣借一隻雞現在整個養雞場要被端走

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — 'Taiwan lent one chicken, now the whole farm is taken' → DUS (batch 19, 43102 '整碗捧走').

---

### id 44274
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 美國有那麼好啊。腦袋壞了才會去美國。美國治安不好。不知道那天。又被瘋子槍殺。到處都是嗑藥人。無家可歸的人

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — US unsafe, shootings, drugs, homeless → DUS (batch 19, 43401).

---

### id 44284
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** M型社會即將結束 均貧社會來臨

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'M-shaped society ends, equal poverty comes' → false.

---

### id 44287
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 民進黨 說白了 就是配合幫美國養台勞啊。 另外 那位衛先生想跟你提醒 企業錢可以賺 但危害台灣下一代永久命運的事情 亂搞會讓整個國家經濟衰敗 最後遺留臭名一輩子，自己福報跟下一代請珍惜啊。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **1** | 0 |
| Opus | 0 | 0 | 1 | 0 | **0** | 0 |

**Your call:** Sonnet (CT+DUS) — 'The DPP helps the US raise Taiwanese labourers' → CT+DUS (batch 19, 43083).

---

### id 44293
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 美國人有什麼好？K型階層？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — 'What's so good about Americans? K-shaped classes?' → DUS.

---

### id 44295
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 怎麼辦找民進黨阿!!不然國民黨只會叫他們去中國。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — 'Go to the DPP! Otherwise the KMT will just tell them to go to China' → KMT pro-China jab → ST.

---

### id 44297
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 感謝郭董說出台灣人才流失是台灣人民的悲哀呀！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Thanks Gou for saying talent loss is Taiwan's sorrow → false.

---

### id 44307
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 工廠技術產能人才全部合法挖走，好厲害的美國人。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Opus (DUS) — 'Factories, tech, capacity, talent all legally poached — clever Americans' → DUS (no party/finished content).

---

### id 44308
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 騰籠換鳥。台積電群企業，帶台灣理工人才移民美國，台灣本土企業政府開放東南亞移工，並給予居留支持😂。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — '騰籠換鳥' — TSMC takes talent to the US, the government lets in SE Asian workers 😂 → generic government sarcasm → false (batch 19, 43665).

---

### id 44309
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Parent (context):** 騰籠換鳥。台積電群企業，帶台灣理工人才移民美國，台灣本土企業政府開放東南亞移工，並給予居留支持😂。
**Reply:** 台灣直接變外勞領地，詐騙黃賭毒橫行

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Reply: Taiwan becomes migrant-worker land with fraud and drugs → false.

---

### id 44311
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台灣人移民美國，會有多少人？
在舔共賣台的內應幫忙下，到時要到美國，就沒機會了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — 'With the help of 舔共賣台 insiders, there'll be no chance to get to the US' → collaborator jab → ST.

---

### id 44314
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 好人材被連根拔起，輸出美國。技術、人材也被挖空😢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Talent 'uprooted and exported to the US', tech hollowed → DUS (no 'Taiwan finished' claim).

---

### id 44318
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 中國若打過來 會有幾萬TSMC工程師+眷屬 被撤走

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'If China attacks, tens of thousands of TSMC engineers will be evacuated' → false.

---

### id 44332
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 至少上3萬家庭移民，成為新華工，這些都是台灣的精英，將全面嚴重的影響，台灣的未來。房産，技術，學界，文化斷層…………

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **0** | 0 |
| Opus | 0 | 0 | **0** | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — 30k families become 'new Chinese coolies' (US exploitation) → DUS; future impact on Taiwan is worry, not hopelessness.

---

### id 44333
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 這2023說的，現在是一定要在美日設廠，人是一定要走了，只是多少的問題？  供應鏈也去

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Plants must be built in the US/Japan, people will go → false.

---

### id 44336
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 掏空台灣不遺余力啊！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — 'Spares no effort to hollow out Taiwan!' — 掏空 alone → false.

---

### id 44339
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台積電送走後，關稅15%有個屁用，出口大量減少後，關稅不重要了。台積電如果禁止到海外投資，才可以保護台灣，至於關稅多少？他們愛調高多少，就調多少？又不是台灣人買單。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Argues banning TSMC overseas investment would protect Taiwan — economic policy, not defence/resolve → false.

---

### id 44342
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 鳳凰飛走了，烏鴉跑進來

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'The phoenix flew away, crows came in' → false.

---

### id 44344
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 那台灣剩什麼

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'So what's left for Taiwan' → false (batch 19, 43614).

---

### id 44345
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 改善人員薪水...? 政府:那你還是先去申請移民吧

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — 'Raise salaries? Government: just apply to emigrate' — generic government sarcasm → false.

---

### id 44347
**Video:** `ox2SixSPe6A` (台積電美國廠多缺人？郭台銘爆料美國在臺協會 願助上千工程師舉家移民 #shorts)
**Thread:** 台美一家親❤台灣的優秀人才在國際上是多麼炙手可熱
反觀中共匪國的人才在國際上乏人問津，只能留在家鄉殘害自己同胞了，2025年中共國人均年收入3500美元……

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Taiwan-US family; CCP 'bandit state' talent unwanted, $3,500 income → anti-CCP retort → ST (batch 19).

---

### id 44351
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Parent (context):** 人類一直在做的事
1.正在打仗
2.正在打仗的路上
**Reply:** ​@falsetrue2932😂日本在1970年代，和中華人民共和國政府的建交友好聲明上，白紙黑字地寫明了:日本關於台灣主權的立場，堅持波茨坦公告第八條。😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Reply citing Japan's 1972 statement on Potsdam Art. 8 😂 to argue Taiwan belongs to the PRC → CT.

---

### id 44372
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Parent (context):** 看到烏克蘭的狀況，不禁對台灣的未來感到深深的擔憂。我今年40歲，認為我們離戰爭很近，65歲的爸媽卻跟我說"不可能戰爭"，我很想反問，憑什麼?
**Reply:** 歷史上的台灣，在明朝與清朝都是一直壓迫，大陸政權。
有聽過，明清的海禁嗎？
請多多認識，真實的台灣歷史，那個可以打敗美國法國西班牙荷蘭的台灣。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Reply: Taiwan historically resisted mainland regimes and 'beat the US, France, Spain, Netherlands' → resolve/pride → ST.

---

### id 44378
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Parent (context):** 可是我覺得已經算三戰了，北約支援烏克蘭的兵力，其實都是北約國派出去的僱傭兵，理論上就是北約對上俄羅斯了
**Reply:** 如果情況持續擴大就是三戰了  例如台海或兩韓也開打  我認為目前還在控制範圍 
熱武器時代 從英國登上世界霸主後  就一直沒換過  任何想挑戰世界霸主地位的國家最後都被打趴
一戰時的德國  二戰的日本與德國  冷戰時的蘇聯.....英國也只是把霸主地位交給他的小弟美國  一樣都是同民族  
這次我認為中國也是一樣  中國人想要當世界霸主讓全世界都當他們勞工  西歐 北美 澳洲一定不同意 因為不同民族  那唯有一戰而已  對美國最有利的方式是把戰爭範圍縮小到如台海 把戰爭日期縮在越快越好  這對美國來說最有利  再過二十年 三十年 解放軍軍力越強大 美國就很難打得贏這場戰爭

中國想要成為世界霸主不是武力發展這條路  而是小鄧同志規劃的那條路  帶著眾多小弟一起開心地賺錢  自然很多國家都會維護你的利益  十幾年前台灣被拋棄過這個圈圈  南韓菲律賓越南印尼印度朝鮮 巴基斯坦 新加坡 泰國 馬來西亞 柬埔寨 寮國都是他的小弟  連澳洲 德國 法國 西班牙 義大利 俄國 英國 荷蘭 烏克蘭都對他很友好  台灣幾乎是被世界各國逼著要嫁給他  不然就是麻煩製造者......如今他們致力發展武力 不顧經濟  法國把拉法葉艦與幻象2千零件補上或給圖紙了  德國瑞士捷克荷蘭則多次為台發聲 與台友好    
現在美國重返亞洲  拉了日本南韓菲律賓越南新加坡印度加上台灣  美國也聯合歐洲國家 澳洲 日韓在太平洋軍演 開啟菲律賓十多處基地  新的包圍網啟動了  全世界都在製造武器 

有人說中國造艦數量與噸位超越美國  抱歉現在日韓美一起造艦  F35材料短缺 抱歉美日德英義西一起造飛機 你250架殲20 北約盟軍的F35就有1000架以上....
F35系列這款飛機不是當代最強但是因為政治地緣時空背景關係  目前已經是史上銷售數量金額都最多的一款戰機  總訂單目前超過3500架 如果以造價 後續的武器配備 後勤保養維修 零件更新都算入  這款飛機將超過一兆美元產值 這其中還沒包括人員培訓以及薪水

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Long reply mixing 'China wants hegemony' and 'the US wants a short war in the Taiwan Strait' — no clear side → false.

---

### id 44386
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Thread:** 烏克蘭戰敗的結果是大陸打臺灣！😰然後打越南！之後暴力收回韓國😰

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | **1** | **0** | 0 | 0 |
| Opus | **0** | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — 'If Ukraine loses, China attacks Taiwan, then Vietnam, then Korea' → 今日烏克蘭明日台灣 / CCP expansionist → ST.

---

### id 44395
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Thread:** 這個問題很簡單，最後一定是歐美經濟崩潰，政治瓦解，中國和俄羅斯收復失土和重整世界。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **0** | 0 | 0 | 0 |
| Opus | 1 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CU+CT) — 'In the end the West collapses, China and Russia recover their lost lands' → CU + CT (China takes Taiwan).

---

### id 44399
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Parent (context):** 台灣=烏，中國=俄羅斯，烏東=金門，其他都可套用
**Reply:** 😂你不知道金門水都是廈門提供的嗎。想打仗的烏，烏龜是寶島的嗎

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Reply: 'Kinmen's water comes from Xiamen… war-wanting 烏龜 of the treasure island' → mocks Taiwan's war readiness → CT.

---

### id 44422
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Thread:** 我怎麼看都不覺得這些插圖可以把SAI的圖層用盡，啊這好像也是一個雞毛蒜皮的新聞吼。俄烏戰爭一開始個人就認為這是跟台海軍火產業鏈一樣，就是另一條新的俄烏軍火產業鏈，目前看起來似乎雙方各取所需，軍火產業鏈的特徵：雙方都要打不打的，每隔一段時間會有情勢急遽緊繃的情況發生，但是不會真的發生激烈衝突，最後通常不了了之，然後是下一輪，如果產業鏈可行，能夠提供收益，就會拖很久。以上從台海產業鏈已經充分得到證明，現在俄烏產業鏈也滿穩定發展中，個人正在看第三條是不是真的出現了，就是以巴軍火產業鏈，雖然說很不可思議，但是整體來看似乎真的是如此。所以俄烏產業鏈應該會持續一陣子，個人估計到普丁政權結束才有機會退場。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Russia-Ukraine as an 'arms-industry chain' like the Taiwan Strait — no named US actor, no side → false.

---

### id 44427
**Video:** `oyspwiplSQM` (俄烏戰爭會如何結束？ 俄烏戰爭結束的七種可能 【這種可能機率最高】)
**Thread:** 預計會繼續打下去，法國已打算派士兵參戰，有遠見的歐洲領導應不會容許俄國繼續吞併烏克蘭，如果俄國成功了，不出五年，下一個便是波蘭和中歐地區德奧瑞多腦河地域，或逐一擊破，或是投向俄國。俄國對土地非常有野心，而且歐洲是大平原，從古至今，主要靠陸軍進攻，近來，俄國的坦克生產量大增，法德兩國的陸軍的生產力都會跟上去。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — Europe won't let Russia swallow Ukraine; Russia is land-hungry → SU.

---

### id 44442
**Video:** `p69gHaD88U0` (烏克蘭電視台製作的10分鐘特輯節目 "這裡就是台灣")
**Parent (context):** 台灣是蹲了四十多年才有今天的一點都不僥倖!二十五年前差點被傾中勢力毀了台灣，還好天佑台灣!
**Reply:** @loliliumlee223是啊！國會與縣市政府 村里長超級多貪污綁樁案子  立委被紅統控制了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Reply: legislators 'controlled by 紅統', corruption → KMT-collaborator content → ST.

---

### id 44445
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 讚． 支持明老師的看法。也支持中華民國反共的正藍軍。
**Reply:** @徐愷輪維護中華民國正統叫台獨？
不是我變綠是你變紅，蔣中正地下有知會開除中國國民黨的黨籍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Reply: 'not me turning green, you turning red; Chiang would expel the KMT' → KMT as red → ST.

---

### id 44463
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 個人6年級生，我覺得一直以來台灣的價值觀都是如明老師今天所講述的，這也是在國民黨執政時期一脈相傳的，但就如老師所講的，現在的藍營已經大相逕庭，而為什麼國民黨裡面沒有第二種聲音出現，令人細思極恐
**Reply:** @louisvist 臥底國民黨的台獨教父李登輝就是共產黨呀！

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Reply: '台獨教父李登輝 is a Communist!' — attack on the green camp's icon → CT (same as 44021).

---

### id 44464
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 個人6年級生，我覺得一直以來台灣的價值觀都是如明老師今天所講述的，這也是在國民黨執政時期一脈相傳的，但就如老師所講的，現在的藍營已經大相逕庭，而為什麼國民黨裡面沒有第二種聲音出現，令人細思極恐
**Reply:** 被摸透，是因為有間諜。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Reply: 'figured out because there are spies' — target unclear → false.

---

### id 44465
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 個人6年級生，我覺得一直以來台灣的價值觀都是如明老師今天所講述的，這也是在國民黨執政時期一脈相傳的，但就如老師所講的，現在的藍營已經大相逕庭，而為什麼國民黨裡面沒有第二種聲音出現，令人細思極恐
**Reply:** @louisvist 台灣的老共產黨入國民黨卧底，代表人物就是李登輝呀！所以他很幫民進黨呀！  這是大家有目共睹的鐵證。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Reply: 李登輝 a Communist mole 'so he helps the DPP' → CT (same as 44463).

---

### id 44543
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 這問題我早在很多地方說過，美國一旦丟掉台灣，美元霸權，軍事霸權，國際霸權，三個霸權同時崩潰。請問中共可以用什麼代價，讓美國同意自己三方面霸權同時崩潰?
所謂美國可能會棄台，從頭到尾就是中共和其同路人的認知作戰，企圖藉此瓦解台灣對美國的信心，最終自己削減武力，讓中國能短時間攻下台灣。
國民黨和民眾黨不客氣的說，就是典型中共同路人。無論他們是被收買或是被欺騙，目前做的事就是配合中共戰略。
台灣就是有一堆人，整天以制衡民進黨為名，支持國民黨與民眾黨惡搞。我不反對制衡民進黨，但制衡民進黨就要貼近企圖消滅台灣的惡棍??你覺得你的里長幹得不好，會引進黑道勢力來制衡里長嗎??這種邏輯說得通嗎??
**Reply:** 台灣關美國什麼事，你是在自我安慰嗎？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — Reply to an anti-疑美論 comment: 'What does Taiwan matter to the US, are you consoling yourself?' → doubts US would help → CT+DUS (batch 19, 43258).

---

### id 44548
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 國民黨就是舔共，這是鐵錚錚的事實，就不用再假清高了，理由很簡單，你們在覬覦人家給你們好處嘛（因爲國民黨在中國有大量的投資）。 你們再怎麼撇清都沒用，民眾不會去聽你們所言，民眾是去觀你們所行。 而你們的行爲，就確實是在舔共沒錯。
**Reply:** @雷煷  共產你可能沒台灣人明白，你好好告訴我，共產七十多年，為什麼鄭豔良自己鉅腿，退休幹部四年ic免費，共產共成兩個世界，你還為主子抱不平？

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Reply: anti-communist retort on CCP inequality, 'you still defend your master?' → ST (anti-CCP retort line).

---

### id 44556
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 以前的國民黨跟現在的國民黨都是在飲鴆止渴，明老師的這句話好有涵義，很多東西已經不言而喻了。
**Reply:** 來自臺灣的所有民眾之枷鎖是...1949流浪海外地區的中華民國.「流浪蔣氏中國塚神主牌」。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Reply: Taiwan's shackle is the exiled ROC / Chiang legacy — anti-ROC, not KMT-collaborator content → false.

---

### id 44568
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 老師講的是真的
我有個朋友在當美軍，他直接跟我說：沒有人在意烏克蘭，但台灣重要性不一樣
**Reply:** 美放棄台灣日韓菲不組联盟就成中共小弟美退出亞洲守夏威夷連太平洋沒了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Reply: if the US drops Taiwan, Japan/Korea/PH fall to the CCP, the US retreats to Hawaii → US won't abandon Taiwan → ST (as 43787).

---

### id 44570
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 老師講的是真的
我有個朋友在當美軍，他直接跟我說：沒有人在意烏克蘭，但台灣重要性不一樣
**Reply:** 對！沖繩美軍就是為了台灣。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Reply: 'Okinawa US forces are there for Taiwan' → ST (as 44568).

---

### id 44571
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 老師講的是真的
我有個朋友在當美軍，他直接跟我說：沒有人在意烏克蘭，但台灣重要性不一樣
**Reply:** @YHTsai-kw9my 沖繩美軍其實依照2008年的國會決策有後撤，但因應台海局勢，美軍光是去年就多次進行關島趕至台海的演練，他們也跟日軍菲律賓以至於澳英等盟國一起在台海進行聯合軍演。
零日攻擊前導片出來時，我曾傳給那位海軍朋友看，他當下直接回我一句“我們怎麼可能放台灣一個國家面對解放軍。”

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Reply: US drills in the Strait, 'how could we leave Taiwan alone facing the PLA' → ST (as 44568).

---

### id 44572
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 老師講的是真的
我有個朋友在當美軍，他直接跟我說：沒有人在意烏克蘭，但台灣重要性不一樣
**Reply:** 美國如果丟了台灣  先不論半導體， 國際政治上會看到
1.韓國 日本 菲律賓往中國靠攏...
2.然後失去整個東南亞
3.然後美元優勢不在
4.美國不可能讓3.發生，格達費和海珊基本上就是碰了3.才被往死裡打的

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Reply: losing Taiwan costs the US Asia and dollar dominance → ST (as 44568).

---

### id 44586
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Thread:** 簡單的說就是美國🇺🇸要是放棄台灣、那日本人就會怕死美國、而投靠？第一島列就毀了、人呆看面對知～

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — If the US drops Taiwan, Japan defects and the first island chain breaks → ST (as 44568).

---

### id 44591
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Thread:** 100多萬觀看，藍營這下是真要完了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — '1M+ views, the blue camp is really finished now' → mocks the KMT → ST.

---

### id 44605
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Thread:** 45:28 明教授比喻不當。
川普如果出兵格陵蘭，對上的是丹麥小國；如果出兵幫台灣，對上的是核大國中共。
會一樣嗎??

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **1** | 0 |
| Opus | 0 | 0 | 1 | 0 | **0** | 0 |

**Your call:** Sonnet (CT+DUS) — 'Greenland means facing small Denmark; helping Taiwan means facing nuclear China — same??' → doubts US would intervene → CT+DUS (batch 19, 43258).

---

### id 44608
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 53:15 ~ 54:01 明教授說了很多台灣對美國多重要的論點，可是才不到一個星期，就有新聞出來:
"被任命為負責戰略事務的國防部副助理部長達默(Austin Dahmer)在社群平台X直言，台灣問題對美國並非生死攸關，即使"丟了台灣"(When Taiwan falls)，美國人照樣過好日子。"........
感覺上，像是打了明教授一臉。
**Reply:** @markchou5226 美國官員講的話，沒有被糾正或換人.....就能代表政府立場，你不知道嗎??

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — Reply: a US official saying Taiwan isn't vital counts as US policy → DUS.

---

### id 44609
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 53:15 ~ 54:01 明教授說了很多台灣對美國多重要的論點，可是才不到一個星期，就有新聞出來:
"被任命為負責戰略事務的國防部副助理部長達默(Austin Dahmer)在社群平台X直言，台灣問題對美國並非生死攸關，即使"丟了台灣"(When Taiwan falls)，美國人照樣過好日子。"........
感覺上，像是打了明教授一臉。
**Reply:** @ymk0106 X平台是社群媒體 不是政府官方網站 官員在社群媒體發言 會等同政府正式立場？ 你的認知作戰要精細一點 不要連常識都不顧

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Reply: an X post isn't official policy, 'make your cognitive warfare finer' → calls out 疑美論 → ST (prompt calibration).

---

### id 44610
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 53:15 ~ 54:01 明教授說了很多台灣對美國多重要的論點，可是才不到一個星期，就有新聞出來:
"被任命為負責戰略事務的國防部副助理部長達默(Austin Dahmer)在社群平台X直言，台灣問題對美國並非生死攸關，即使"丟了台灣"(When Taiwan falls)，美國人照樣過好日子。"........
感覺上，像是打了明教授一臉。
**Reply:** @ 川普也常在社群平台發言，那就是他的立場發言。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — Reply: Trump also speaks on social media, so it is US policy → DUS (as 44608).

---

### id 44611
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 53:15 ~ 54:01 明教授說了很多台灣對美國多重要的論點，可是才不到一個星期，就有新聞出來:
"被任命為負責戰略事務的國防部副助理部長達默(Austin Dahmer)在社群平台X直言，台灣問題對美國並非生死攸關，即使"丟了台灣"(When Taiwan falls)，美國人照樣過好日子。"........
感覺上，像是打了明教授一臉。
**Reply:** @ 政府官員在公開的社群平台發言，就是政府的立場。如果沒被糾正，或換人的話。
川普也常在公開社群平台發言，那就是政府的立場。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — Reply: same argument as 44608 → DUS.

---

### id 44615
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Parent (context):** 55:44 明教授可能弄錯了，說2027中共要打台灣，是美國印太司令最早說的，然後美國智庫都把這個當成兵推想定。
中共從來都沒這樣說，習近平還正式否認過。
**Reply:** 習 慣性 欺騙外國領導人 不是第一次了

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Reply: 'Xi habitually deceives foreign leaders' → anti-CCP → ST.

---

### id 44622
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Thread:** 明大教授我發現你的言行跟行為越來越像三國一個人物，也就是三國誌編撰作者的師傅"譙周"，還有你說烏克蘭沒台灣重要我不以置評，但是你好像忘了2022年的俄烏戰爭川建國(唐納德J川普)就說過了，其實可以避免這場戰爭，問題就在漂亮國前總統"小約瑟夫 羅比內特"身上怎麼沒有翻譯翻譯，當然台積電80%都是美國投資者的股份，甚至台積電(TSM)在華爾街目前的股價也高達210美金，所以台積電回娘家本來就跟台灣企業無關阿!!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Long rant: 明居正 like 譙周, TSMC 80% US-owned so 'returning home' is not Taiwan's business → DUS.

---

### id 44636
**Video:** `pa52xbqjW20` (【下班瀚你聊】川普重返白宮!台灣從棋子變棄子?明居正八字預言台灣命運!不解藍營為何不再反共!直言台灣不選美國難道選中共?2025-01-19 Ep.242@TheStormMedia)
**Thread:** 親共？？？阿共阿 他台語這麽爛？？！！！！ 他才親共呢！！！ 阿山仔 （台語）他懂嗎 你們主持人懂嗎

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — 'He's the pro-communist one!!!' — calls a pundit pro-CCP → ST (your 13201/13631).
