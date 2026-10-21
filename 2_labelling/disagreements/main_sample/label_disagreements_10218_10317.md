# Label disagreements: ids 10218-10317

100 rows labeled, 78 agree, 22 disagreements. All rows are `row_type='thread_with_comment'` under the same TVBS video ("今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看") except id 10220 (十點不一樣 video).

Columns: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion

For each row: fill in **Your call** with `Sonnet`, `Opus`, an explicit override (list which labels should be true), or leave `UNSURE` if genuinely undecided. I've pre-filled my best read with a one-line rationale — overwrite freely.

---

### id 10220
**Thread:** 烏克蘭國土比台灣大太多,游擊戰絕對活比台灣久
**Comment:** 国民党要是能学到中共一半的游击战功力，绝对守得住四川

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | F | **T** | F | F | F |

**Your call:** Sonnet (all false) — this is a jab at the KMT's historical military incompetence in the Chinese Civil War (losing mainland China, "couldn't even hold Sichuan"), not a statement about Taiwan's current defense preparedness or hopelessness. Doesn't fit critical_taiwan's definition cleanly.

---

### id 10228
**Thread:** 全世界99%都說俄羅斯不會打，就1%美國情報說會打證明美國在阿富汗花百億美金建立的情報網最準。
**Comment:** [garbled long rant about test-tube babies, blue-eyed genetics, and needing "white" Taiwanese to trigger the same international sanctions/sympathy response Ukraine got]

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | F | **T** | F | **T** | F |

**Your call:** 
Sonnet

---

### id 10235
**Thread:** 全世界99%都說俄羅斯不會打，就1%美國情報說會打證明美國在阿富汗花百億美金建立的情報網最準。
**Comment:** 全世界的人都知道這場仗一定會打. 是美國的情報錯了. 美國說2月16號會打. 連最笨的人都知道奧運完了才會打

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | F | F | F | **T** | F |

**Your call:** Sonnet (all false) — disputes the intelligence's accuracy on timing (Feb 16 vs. after Olympics), a factual quibble, not moral criticism or distrust of US commitment/reliability.

---

### id 10241
**Thread:** 今日普丁，明日習近平
**Comment:** 普丁快玩死欧洲了，都不敢设禁航区，也不敢制裁能源。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | **T** | F | F | F | F | F |

**Your call:** Sonnet (all false) — criticizes Europe's timidity (won't set a no-fly zone, won't sanction energy), not Ukraine's resistance or legitimacy. Off-target for critical_ukraine.

---

### id 10242
**Thread:** 笑話，俄國與中國的財力與經濟國碼是能比的？
**Comment:** 就是俄羅斯都這麼慘，中國被制裁只會更慘。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | **T** | F | F | F | F |

**Your call:** Opus (supportive_ukraine=true) — "Russia is already this miserable [under sanctions]" acknowledges Russia's sanctions-driven decline, fitting the "predicting Russia's weakness" pattern.

---

### id 10244
**Thread:** 俄國之所以侵略烏克蘭,完全是因為普丁於冬奧訪問北京時習近平表示支持俄國侵略烏克蘭而所引致的...中共是俄烏戰爭幕後原兇.
**Comment:** 中國支持開戰是元兇之一

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | **T** | F | F | F | F |

**Your call:** Opus (supportive_ukraine=true) — accepts the thread's framing of Russia's action as "侵略" (invasion) and further blames China as an accomplice culprit; condemns the aggressor side.

---

### id 10252
**Thread:** (same as 10244 — 中共是俄烏戰爭幕後原兇)
**Comment:** 再鄉土一點 劇情是用過烏國的軍資，知道小烏強大所以慫恿俄爹出征 給境外勢力遞刀子讓俄爹被世界各國看笑話，並準備收回失去的領土，中兒真是欠打

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | **T** | F | F | F | F |

**Your call:** Opus (supportive_ukraine=true) — sarcastic mockery of pro-Russia conspiracy narratives ("俄爹"/"中兒"), portrays Russia as duped/humiliated internationally and Ukraine reclaiming lost territory — fits the "predicting Russia's post-war weakness" pattern.

---

### id 10258
**Thread:** 攻不下來 普丁要腦羞變成魔人普丁(烏)了
**Comment:** 拿平民当人质，谁能想出这是人做的事

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | **T** | F | F | F | F |
| Opus | F | F | F | F | F | F |

**Your call:** Sonnet (supportive_ukraine=true) — the parent thread is already anti-Putin ("魔人普丁"), so this reply's condemnation of "taking civilians hostage" as inhuman most naturally continues condemning Putin's brutality, not accusing Ukraine of using human shields.

---

### id 10264
**Thread:** 全世界99%都說俄羅斯不會打，就1%美國情報說會打證明美國在阿富汗花百億美金建立的情報網最準。
**Comment:** 沒人要你保證你保證也沒用，經濟制裁是最基本的而已，連中國都覺得會發生你說呢?本來支持俄國現在連支持都不敢說只能說我中歷我棄權。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | **T** | F | F | F | F |
| Opus | F | F | F | F | F | F |

**Your call:** Sonnet (supportive_ukraine=true) — notes former Russia-supporters now afraid to voice support, implying growing isolation of Russia; fits the "predicting Russia's isolation" pattern.

---

### id 10266
**Thread:** 我們是無堅不摧的民主同盟，美軍會幫台灣打仗，台灣只要幫忙加油就好。
**Comment:** 基于共同的民主自由价值观，美军不单会帮台湾打仗，还会帮忙收凤梨，摘莲雾。说不定还会在街头帮忙卖槟榔。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | **T** | F | F | F |
| Opus | F | F | **T** | F | **T** | F |

**Your call:** Opus (CT+DUS=true) — extends the sarcasm to absurd lengths mocking the naive "US will fight for Taiwan" belief; the mockery itself expresses distrust that the US commitment is real, not just capitulation framing.

---

### id 10267
**Thread:** (same as 10266)
**Comment:** mm3964 對所以不會在輕易的介入戰爭，你自己沒有抵抗的想法憑甚麼美國要幫忙? 阿富汗就是例子，所以台灣人要展現自我抵抗的決心~ 別說台灣人願不願意當兵的問題，沒意義，憲法刑法寫在上面，台灣有多少人能逃兵的??

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | **T** | F | F |
| Opus | F | F | F | **T** | **T** | F |

**Your call:** Opus (ST+DUS=true) — argues Taiwan must show self-reliance/resolve (supportive_taiwan) while explicitly citing Afghanistan as proof the US "won't easily intervene" (disappointment_with_us) — both legitimately present.

---

### id 10268
**Thread:** 人死光了經濟制裁有屁用? 一句話會不會出兵就好
**Comment:** 千言万语汇成一句话：不会出兵不会出兵不会出兵

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | **T** | F |
| Opus | F | F | **T** | F | **T** | F |

**Your call:** Sonnet (DUS only) — this is about the immediate Ukraine troop question (won't send troops), doesn't explicitly extend to Taiwan's own hopelessness, so leave critical_taiwan false.

---

### id 10269
**Thread:** 東部烏克蘭打俄，西側台海對峙高漲，都是美國的如意算盤...台灣、烏克蘭皆成難民戰區,受美關懷與援助,有政府好甘心。
**Comment:** 美國是很強沒錯 但沒有必要負能量什麼鍋都讓美國背 中共習維尼 王毅那嘴臉 是美國造成的? 普丁自己英雄主義 是美國安插的? 金胖沒事發神經 也是美國弄的? 動動腦吧 在商言商 侵略別人 發擊攻擊 軍演威脅 就是王X蛋 沒本事才會動手打人殺人

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | **T** | F | **T** | **T** | F |
| Opus | F | **T** | F | **T** | F | F |

**Your call:** Opus (SU+ST, no DUS) — this comment explicitly REJECTS the parent's "blame everything on the US" framing ("沒有必要負能量什麼鍋都讓美國背") while condemning Russia/China/NK aggression. Per the established precedent (ids 7349/7352/7356), a comment that explicitly denies the US-blame framing should not get disappointment_with_us.

---

### id 10270
**Thread:** 我們是無堅不摧的民主同盟，美軍會幫台灣打仗，台灣只要幫忙加油就好。
**Comment:** 😂 how foolish this statement is

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | F | **T** | F | **T** | F |

**Your call:** Sonnet (all false) — too terse to tell whether "foolish" targets the naive pro-US belief or the cynical mockery itself; ambiguous sarcasm direction defaults false per calibration note.

---

### id 10274
**Thread:** (same as 10266/10270)
**Comment:** 台湾只要拼命吞萊豬、吃福食、喝核水、打高端...美、日就會出兵保護台灣。

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | F | **T** | F | **T** | F |

**Your call:** Opus (CT+DUS=true) — bitter mockery of DPP government concessions (US pork, Fukushima food, domestic vaccine) as a humiliating bargain that won't actually secure US/Japan protection; clear critical_taiwan + distrust of the payoff.

---

### id 10277
**Thread:** 俄國之所以侵略烏克蘭...中共是俄烏戰爭幕後原兇...
**Comment:** @王彪-x7j 請你不要把台灣獨立出去哦

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | **T** | F | F | F |
| Opus | F | F | F | F | F | F |

**Your call:** 
Opus

---

### id 10278
**Thread:** (same as 10266/10270/10274)
**Comment:** think too much man

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | F | **T** | F | **T** | F |

**Your call:** Sonnet (all false) — same ambiguity as 10270: dismissing the parent as "overthinking" could go either direction, too terse to commit.

---

### id 10280
**Thread:** 俄國之所以侵略烏克蘭...中共是俄烏戰爭幕後原兇...
**Comment:** @lizhou2379 有能力 對俄國經濟 做成嚴重打擊的國家, 極之多 加入了 制裁俄國的行列.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | **T** | F | F | F | F |

**Your call:** Opus (supportive_ukraine=true) — notes the large number of countries capable of seriously damaging Russia's economy that have joined sanctions, fitting the "predicting Russia's isolation" pattern.

---

### id 10282
**Thread:** 我們是無堅不摧的民主同盟，美軍會幫台灣打仗，台灣只要幫忙加油就好。
**Comment:** @jimmydang1602 impossible, they depend on their keyboards

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | **T** | F | F | F |
| Opus | F | F | F | F | F | F |

**Your call:** Sonnet (critical_taiwan=true) — mocking Taiwanese defenders as only "keyboard warriors," implying no real fighting capability; fits mocking defense preparedness.

---

### id 10284
**Thread:** 俄國之所以侵略烏克蘭...中共是俄烏戰爭幕後原兇...
**Comment:** Tomas Lau 你沒有留意新聞？歐盟政策已改變了. 歐盟斷絕依賴俄國能源措施 的執行時間表 也已決定了.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | **T** | F | F | F | F |

**Your call:** Sonnet (all false) — a factual news correction about EU energy policy, not an expression of solidarity/praise for Ukraine on its own.

---

### id 10302
**Thread:** 我們是無堅不摧的民主同盟，美軍會幫台灣打仗，台灣只要幫忙加油就好。
**Comment:** 腦子秀逗 美國也會像對烏一樣對我們 說這句的人 國外是不是已經有房了? 我若有 我也會說一樣的話

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | **T** | F | F | F |
| Opus | F | F | **T** | F | **T** | F |

**Your call:** Opus (CT+DUS=true) — explicit "US will treat us like it treated Ukraine" abandonment framing, citing the Ukraine precedent directly (matches critical_taiwan's own Afghanistan/Ukraine-precedent clause) plus distrust of US commitment.

---

### id 10303
**Thread:** (same as 10302)
**Comment:** 不信美國，難不成信共產黨

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | F | F | F | F | F | F |
| Opus | F | F | F | **T** | F | F |

**Your call:** Opus (supportive_taiwan=true) — pushes back against total abandonment of US trust with a reductio ("don't trust the US? then trust the CCP instead?"), implicitly defending continued reliance on the US alliance over capitulation.
