# Disagreement Review: ids 34564–35578 (event test, batch 12)

700 rows labeled, 503 agreed (71.9%), 197 disagreements below. Run 1 = `claude-sonnet-5`, run 2 = `claude-opus-5`. Only non-Simplified event-test comments. 12 videos; most disagreements come from the volunteers-back-from-Ukraine clip `JVSaxGNZ5xQ` (49), the 陳揮文 'US will sell Taiwan' short `J4KEi0CqiO4` (46) and the body-armour video `F9DL33U-gvc` (45). Disagreement rows: 139 thread_only, 58 thread_with_comment.

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion. Bold = the labels where the runs differ.

Precedent used for "Your call": your batch 1–11 decisions, `labeling_prompt.md`, and your own labels in `full_data.db` on two of these videos (`JVSaxGNZ5xQ` 83 rows, `Irj2hpBwH3o` 81 rows — none of the same comments).

My calls: 119 Opus, 75 Sonnet, 3 other. 105 marked **Borderline**.

**Main patterns.**
- **國軍 criticism** (body-armour + volunteer videos, ≈80 rows): Sonnet gives CT to almost every complaint, Opus often ST or false. I used your full_data labels on `JVSaxGNZ5xQ` and the batch 11 body-armour line: mockery of the army/generals/黃埔 ('只會吃飯', '狡辯', '嘴巴厲害', borrowed gear at inspections) → **CT**; reform calls or cheering ('hire them as advisers', '國軍加油', 'protect our soldiers') → **ST**; brass sold out to / bought by the CCP ('黃埔共產', '賣機密給共軍') → **ST** (as your '舔共退伍軍官' label); plain procurement/technical points → false.
- **Plate demands differ from batch 11:** 34628, 34652, 34675 (level-4 plates / self-purchase 'so soldiers live') → ST here; in batch 11 a similar plate demand was false. If you want batch 11's line, these 3 go to false (Other).
- **張亞中 / 陳揮文 (中天) videos:** praise or endorsement of the pundit → **CT** (Opus); calling the pundit or 中天 a CCP mouthpiece → **ST**; plain insults with no politics → false (batch 9 rule).
- **陳揮文 reply threads** (vote fraud, 'DPP idiots', masks/vaccines) → **CT**; retorts to PRC-side users → **ST**; 'US makes Taiwan pay more' → **DUS**; 'US will sell us' → **CT+DUS** (calibration).
- **Volunteer died / came back** (`Irj2hpBwH3o`, `JVSaxGNZ5xQ`): 'for money', 'no sympathy', 'fighting for what?' → **CU**; praise or defence of the volunteers → **SU** (your full_data labels).
- **'Taiwan is key' (民視) video:** mocking the report / Taiwan's self-hype → **CT** (Opus).
- **Others (3):** 34990 → CU+CT (both parts present); 35478 'old should retire, new blood' → ST; 35540 'better than that retired general' → SU+ST (both from your full_data labels).
- **Two Slovak comments** (34747, 34756) slipped through the language filter. I gave them labels, but by your rule (drop other languages) they should be deleted from both event DBs. Your call; nothing is changed yet.

**Note on the runs:** no UPDATEs this batch; both runs INSERT-only, exactly 700 rows each. Both tried to write temp .sql files; the permissions blocked them and no files were left.

---

### id 34567
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread (context):** 至於為什麼要標準化，這也是有原因的。部隊就是把人標準化的地方；在外面、在民間，每個人都可以有自己的特色、自己的想法，但是在部隊，形成戰鬥力的單位是「群體」，而不是「個體」。這就好像一兩隻螞蟻不同幹嘛，如果有十萬隻螞蟻，但都是鬆散分散、各自為政的，那也沒用，但如果這十萬隻螞蟻一聲令下全部團結起來、明確分工，所有螞蟻的心中想著專注去做同一件事情、完成同一個目標，那麼，那十萬隻螞蟻就能推倒一堵高牆，讓人都怕。 不知道大家有沒有看過電影星際大戰（star wars ），裡面有暴風兵團，就是全身上下白色盔甲、成千上萬都長得一樣的反派角色的軍團。 軍隊，就是要把每一個人、每一個個體訓練，或說改造成那樣子。
**Reply:** 這就跟之前有個美軍教官說的一樣，台灣國軍基層部隊的靈活性不足，只能聽從上層命令，底層士官沒辦法因時、因地制宜，練再多不放權給基層，整個指揮體系依然是僵化的。
**Translation:** Like a US instructor said: Taiwan's frontline units lack flexibility; the command system stays rigid.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Criticises the 國軍 command system as rigid → CT (same line as your full_data labels on 國軍 training).

---

### id 34573
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 國軍跨出這一步真是令人高興!希望國軍軍備能越來越好!
**Translation:** Glad the military took this step! Hope its equipment keeps getting better!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Cheers the military → ST.

---

### id 34574
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 真的蠻好笑，漏洞一堆 如果採購不知道他們怎麼測的，那就請他們出示測試報告，或者直接拿一兩片軍方自己測，之後品質穩不穩定不就更簡單，每批抽測不就好了，軍方怎麼這麼像在狡辯
**Translation:** Really funny, full of holes… why does the military sound like it's making excuses?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks the officials' 'excuses' → CT (batch 11, 34512).

---

### id 34575
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 允許自備，結果去淘寶買到假的，連保證書，外行不要領導內行
**Translation:** Allow self-purchase and people buy fakes on Taobao — amateurs shouldn't lead experts.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Mockery of the self-purchase rule → CT.

---

### id 34578
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 應該學習美軍，例如外包傘包給民企包裝，100件抽15件給民企負責人和公司高層穿來跳傘。 就叫205廠廠長和國防高層長官穿防彈衣給人打打看。 都當民眾看不懂英文喔。國防部別把民眾當白癡。
**Translation:** Make the 205 Arsenal head and top brass wear the vests and get shot at. Don't treat the public as idiots.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — 'Make the generals wear it and get shot' → CT (batch 11, 34529).

---

### id 34580
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 都是在做表面功夫應付媒體，完全還是黃埔思維，不然怎麼會退那麼多人哩
**Translation:** All surface show for the media, still Whampoa thinking.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Face projects, 黃埔 thinking → CT.

---

### id 34581
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 國外測NIJ是直接抗彈板單片上去測不是？這才是標準吧～
**Translation:** Abroad, NIJ tests the plate alone, right? That's the standard.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Technical → false.

---

### id 34582
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 台灣幾乎人人當兵，期待軍備局能多加強，保護我們的子弟兵
**Translation:** Almost everyone in Taiwan serves; hope the armaments bureau does better to protect our soldiers.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Supports the military → ST.

---

### id 34584
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 士兵要保命，重一點有差嗎！你有聽過健身的人怕重影響訓練嗎 舉例的國家是北約正規軍嗎感覺這205少將是在比爛！我們在問你為什麼沒升級 ，你一直說很重,防禦力也很好 我知道妳穿3級 我就用可以打破3級的武器打你，防護等級越高 我要打破的成本越大！這是客觀現實別再拿一堆似是而非的話來塘塞，最後國外3級賣3千多 4級賣1萬多台幣 你賣20年前標準的3級3萬多 合理嗎？全部採購很難嗎？205全部靠這種不及格的板糊口飯吃嗎
**Translation:** Soldiers want to live — is weight a problem? This general is comparing who's worse… 20-year-old level-3 for 30k+, is that reasonable?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Attacks the general and the price → CT (batch 11, 34531).

---

### id 34587
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 這兩位少校還在狡辯啊，騙不懂裝備的人
**Translation:** These two are still making excuses, fooling people who don't know gear.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — 'Still making excuses' → CT (batch 11, 34512).

---

### id 34588
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 怎感覺聽了他們的解說，我更沒信心了，范姐問問題怎也是小心翼翼.....，而且當過兵的人都知道將軍的保證是取巧的保證，很多人都知道高裝檢缺裝備會如何處理，我覺得檢測還是應該公開由第三方來檢測...你說打不穿，但若主管、採購、設計、檢測、生產都是自己人，很難讓人信服
**Translation:** After their explanation I have even less confidence; testing should be done by a third party.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Distrust of the military's tests → CT.

---

### id 34589
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 黃埔共產不除，台軍必敗。
**Translation:** Unless the Whampoa communists are purged, the army will lose.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Calls 黃埔 communist (infiltration framing) → ST, as with your '舔共退伍軍官' label.

---

### id 34590
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 建議黃埔共產部向淘寶直接採購軍品，可以節省中間人剝削，也可以發大財。
**Translation:** Suggest the Whampoa Communist Dept buy gear straight from Taobao — cut out the middleman, get rich.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Same author/line as 34589 → ST.

---

### id 34594
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 我就一個問題 怎麼昇到少將的 連個基本的溝通都講不清楚 這換到民間企業 回去大概會被老闆幹到黏在牆上三天摳不下來  做不好就先買啦 製造王國 自己做還比外面買貴 最貴的一片也是一萬 人家還要賺錢ㄟ 你軍備局是成本ㄟ 當全台灣都是傻子?沒人做過生意? 西方國家也很多安全採購途徑 烏克蘭不也是靠一堆外援 拼拼湊湊 走都走不穩還要求姿勢漂亮  雖然當過兵的都懂 還是希望國軍加油
**Translation:** How did he make major general?… Ukraine also patches together foreign aid… still, I hope the military keeps going.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | **1** | **0** | 0 | 0 |
| Opus | **0** | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Attacks the general but ends 'hope the military keeps going' → ST; no CU (Ukraine only as an example).

---

### id 34600
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 我覺得 沒外流要確定欸？  高裝檢常常借裝備檢查  很常有欸   😏  懂的都懂
**Translation:** Sure nothing leaked? Units often borrow gear for inspections — those who know, know.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Borrowed gear at inspections → CT (batch 11, 34530/34537).

---

### id 34602
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 浪費時間！勉強看了5分鐘，這些軍備局的 官員還是避重就輕的回答！鉛彈主要來打人，鋼心彈用來打裝備，所以敵人都不會用鋼心彈來打人？？
**Translation:** Waste of time! Officials still dodge the questions…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Identical to 34514, which was CT in batch 11.

---

### id 34603
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 等到明年政黨輪替，國軍又會回到黃埔系統的面子工程，長官別擔心台灣這些死老白姓。
**Translation:** After next year's change of government the army will go back to Whampoa face projects; don't worry about us dead commoners.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks 黃埔 face projects → CT.

---

### id 34606
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 問題是誰敢報缺失
**Translation:** The problem is: who dares report shortages?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Same line as batch 11 (no one reports shortages) → CT.

---

### id 34608
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 既然要換真的不想全面換還要分嗎？如果多花點錢可以保障國軍的安全，這是大家都能接受的。
**Translation:** If spending more keeps soldiers safe, everyone can accept that.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Supports spending for soldiers' safety → ST.

---

### id 34611
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 聽起來很勉強！也沒邏輯！！觀念保守又老舊！輸了戰爭算是倒霉嗎？？！！！😮
**Translation:** Sounds forced! No logic! Old, conservative ideas! Is losing a war just bad luck?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks the officials' logic → CT.

---

### id 34616
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 感謝范姊找軍方一起討論了解，目前中華民國國軍最大的問題不外乎就是大量面子工程，大量文書業務，導致壓縮各種訓練能應付就應付過去，導致不在乎裝備好壞與如何提升戰力。 談到自購方面還有個問題需自行尋找合格軍規之產品，也有機率購買到不良品與個人財力有限。 國軍加油好嗎？
**Translation:** The military's biggest problem is face projects and paperwork… Come on, military, OK?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Criticism of face projects but ends 'come on, military' → ST.

---

### id 34620
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 清點當然回報沒少，少了也不能說啊，當過兵都知道高裝檢都用借的先檢就去別營先借來用
**Translation:** Of course they report nothing missing — everyone who served knows they borrow from other battalions.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Borrowed gear at inspections → CT.

---

### id 34625
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 我都聽懂了, 斐姨還不懂, 廠長表達能力真的不太好 總之目前的抗彈板符合當時提出的需求, 那就要問問陸軍了 有關於官兵生命的裝備, 評估時完全沒考慮到未來嗎, 不到5年就落伍,  還要扣掉研發生產時間, .等於生產出來3年就落伍, 實在有點無語啊  不過最後還是要給國軍一個鼓勵, 能公開與民眾溝通, 加油啦👍
**Translation:** Plates outdated within five years… but still, encouragement to the military for talking to the public, add oil.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Criticises outdated plates but ends with encouragement → false.

---

### id 34626
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 有另外一個問題，部分官兵使用的背心，是沒辦法承受軟硬版同時使用的，撐不住，會破損  非常開心國軍接受這類談話性節目，身為現役，有注意到國軍有逐步在進步，但速度還是有點太緩慢，以及有些需要優先改變的部分都沒有動作，每天都在要求幹部要與家屬有密切的聯繫，是沒辦法增加國軍戰力的，只會降低阿  而抗彈版的部分，之前國防部記者會也有說明也會研發四級板，而國內也有有能力製作四級板的廠商，且商品也有外國軍警單位購買，甚至烏俄戰場也看得到，希望國防部可以與其做技術交流，也希望范姊的頻道邀請看看廠商，來談談抗彈版的專業技術
**Translation:** Very happy the military does talk shows; as active duty I see it improving, but too slowly…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Serving soldier: sees progress, wants level-4 plates → ST.

---

### id 34628
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 29:00為何3+ 不直接做到4級，與美軍接軌！ 32:00 目前國軍在研發4級，為何不向外採購？現在用3級有可能小命不保，那就應開放官兵自購4級。我相信大家寧願多花錢自購，再等國軍生產4級板！
**Translation:** Why not level 4 like the US? With level 3 you may die — let soldiers buy level 4 themselves.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Wants level-4 for soldiers' lives → ST (batch 11 had a similar plate demand as false).

---

### id 34629
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread (context):** 29:00為何3+ 不直接做到4級，與美軍接軌！ 32:00 目前國軍在研發4級，為何不向外採購？現在用3級有可能小命不保，那就應開放官兵自購4級。我相信大家寧願多花錢自購，再等國軍生產4級板！
**Reply:** 有看到網友說：去查查近幾年的國防標案廠商？！
**Translation:** Someone online said: go check the defence tender firms of recent years.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Hints at procurement corruption → CT.

---

### id 34630
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 就是遲遲等不到戰鬥個裝配發才會想要自己買，我就是剛好遇到下基地，單位才趕快把裝備生出來，還不是一次發整套，比龍珠還難收集，我有錢還不讓我自購，就為了愚蠢的一致性，先有裝備才會需要考慮耐久度吧？等兩年沒發配到的大有人在
**Translation:** Gear harder to collect than Dragon Balls… won't let me buy my own for stupid uniformity.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks 'stupid uniformity' and missing gear → CT.

---

### id 34632
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 防彈背心防彈板. 應該開放民間廠商研製但必須限定本土製造. 規格配料機密由國防部掌控.
**Translation:** Body armour should be opened to private local makers, specs controlled by the MND.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Procurement suggestion → false (batch 11 line).

---

### id 34633
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 民眾原本善意檢討建議而已. 不必又牽連打擊國軍士氣. 黃埔老習慣糧秣罐頭.醫院.銀行等等都要自立經營這些都是來自軍閥陋習. 應該信任台灣民間強大科技與製造能力舉世聞名. 國防部應專心於整體戰備能力與發展提出規格檢驗. 盡可能放棄廠院等管理瑣細.
**Translation:** Don't hurt military morale… drop the warlord habits, trust Taiwan's strong civilian tech.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Defends morale, wants civilian industry trusted → ST.

---

### id 34641
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 這兩位將軍的思路還是傳統戰爭的想法, 請他們多研究一下李喜明將軍的不對稱作戰. 簡單的說對岸打台灣的第一波登島部隊一定是強兵, 所以配的武器也一定是用最好的, 結果他們還用一般部隊的角度配置裝配給守備部隊, 是死是死別人的小孩, 真的是可惡!!還有現在步兵的對抗已經近到不超過五十公尺了, 還說一兩百公尺, 真的是騙主持人不懂.
**Translation:** These generals still think in old-war terms; study Gen. Lee Hsi-ming's asymmetric warfare…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Reform call (study asymmetric warfare) → ST, as with your 'old officers should step down' label.

---

### id 34643
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 既然說有這個問題，那為甚麼，不要訂定統一標準?同一標準階通用，並開放民間企業參與.
**Translation:** Why not set one common standard and open it to private firms?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Constructive procurement suggestion → false.

---

### id 34644
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 講話很慌😂
**Translation:** He sounds so panicked 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mockery → CT.

---

### id 34650
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 靠~~當過幾年兵的都知道，研發是一回事!正式撥發用在訓練上又是一回事。勤儉建軍四個字就壓死你，想穿新裝備的做訓練，門都沒有!!長官會跟你說:因為國防預算刪減，訓練時穿舊的就好，新的是正式作戰要穿的?!淦~~就是新的都不會消耗，所以軍備局的只會吃飯!!
**Translation:** The armaments bureau only knows how to eat!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — 'The armaments bureau only eats' → CT.

---

### id 34651
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 真的外流很多
**Translation:** A lot really does leak out.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Gear leaking out → CT.

---

### id 34652
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 我認為國軍裝備在自購上應該有更大的彈性 就我所知尤其在步槍瞄具上面國軍基層官兵的配發額度非常欠缺，一般基層官兵想要好瞄好打，除了鐵瞄之外就只能自購，但國軍如果不開放瞄具自購的話，實際的射擊戰力肯定有所減損 看到最新的XT-112步槍都有設計皮軌，如果可以開放瞄具自購的話，大家就可以針對自己的瞄準習慣來配置順手的瞄具
**Translation:** Allow self-purchase of sights, otherwise real combat power suffers.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Wants self-purchase for combat power → ST.

---

### id 34656
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 中華民國軍隊對話台獨母🐸？
**Translation:** The ROC military talking to the pro-independence frog-mother?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — '台獨母🐸' slur → CT.

---

### id 34657
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 願意出來受訪就讓我很改觀了（雖然給的理由還是漏洞百出
**Translation:** Agreeing to the interview changed my view (though the reasons are still full of holes).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Mixed, mostly positive → false.

---

### id 34658
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 自己 穿起來 開一槍  勝過 千言萬語
**Translation:** Put it on and fire one shot — worth a thousand words.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — 'Wear it and fire a shot' → CT (batch 11, 34529).

---

### id 34659
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 幾顆花生就能解決的事搞半天😂😂😂
**Translation:** Something a few 'peanuts' could settle, and they drag it out 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Mockery → CT.

---

### id 34660
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 組合有組合的結果， 單一組件測試有單一組件測試的結果。 國軍為何不也單一組件測試呢? 議員用單一組件測試貫穿也沒錯阿 國防部一直強調整組測試是合格的，這我也相信。 但不肯測單一組件，是否默認單一組件是會被貫穿的呢？  畢竟很少人是不合規穿戴， 但單一組件如果就可以不被貫穿， 那整組穿戴時是否更安全呢。
**Translation:** Why won't the military test single components?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Technical → false.

---

### id 34666
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 17:15 口徑比較大所以動能比較大？ 確定欸？ 所以9mm手槍彈的動能不就比5.56x45 mm的步槍彈高？  睜眼說瞎話
**Translation:** Bigger calibre = more energy? Lying through his teeth.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — 'Lying with eyes open' → CT.

---

### id 34667
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 現在是國防布，以前是國防不 雖然有進步，但以鄰居的態勢來說，還是可以再開放一點，畢竟時間真的不多
**Translation:** Was 'defence no', now 'defence cloth'; progress, but given the neighbour, open up more — time is short.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Sees progress, PRC threat, time short → ST.

---

### id 34671
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** from where am from... there is no level 3 plate,there is nothing... you get shot, so sad...
**Translation:** Where I'm from there is no level 3 plate… you get shot, so sad.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — English, no Taiwan stance → false.

---

### id 34673
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 意思就是我要自己研發,不想採購外面,但要研發國人可以接受的重量的四級版,我還沒研發出來最快明年,最慢捨麼時候不一定,這因該是國防部長久以來的問題,從知道問題到發現要解決時間通常很漫長,光是弄到潛艦就好幾十年
**Translation:** This is the MND's old problem — getting submarines took decades.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — MND's long-running slowness → CT.

---

### id 34675
**Video:** `F9DL33U-gvc` (不再國防「布」？ 首度現身新媒說明抗彈板事件 ft.軍備局205廠廠長 潘煥亞少)
**Thread:** 國防部不給的東西也不能自購也看不懂，什麼時候才要配瞄具？什麼時候才要重視單兵裝備😢
**Translation:** When will they care about individual soldier gear? 😢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Pro-soldier frustration → ST (same as 34628).

---

### id 34703
**Video:** `Ff03-l3G2io` (【精選】老美悽慘打地鼠？中國沒在怕制裁「國產3奈米」已在路上...ASML將痛失)
**Thread:** 你這反攻大陸台播、会有報应
**Translation:** You 'retake the mainland' channel, you'll get retribution.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Target unclear → false.

---

### id 34729
**Video:** `FzpV2e0f5Uc` (#烏克蘭 分裂的百年噩夢？當 #克里米亞 插上 #俄羅斯 國旗@ebcCTime)
**Thread:** 舊聞了吧？…………現在俄羅斯確定有內戰發生囉！
**Translation:** Old news? Now Russia has a civil war!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Gloats about Russia's internal trouble → SU.

---

### id 34734
**Video:** `FzpV2e0f5Uc` (#烏克蘭 分裂的百年噩夢？當 #克里米亞 插上 #俄羅斯 國旗@ebcCTime)
**Thread:** 請鬼開藥單😅😂 還好那是之前，現在情況是相反
**Translation:** Asking a ghost for a prescription 😅 — that was before, now it's the reverse.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — 'Now it's the opposite' (Russia losing) → SU.

---

### id 34747
**Video:** `G5MdTUcLUHQ` (烏克蘭戰爭三週年：美國「擁抱」俄羅斯  與歐洲盟友分道揚鑣？－ BBC News)
**Thread (context):** 贊成馬克紅說的一點  是俄羅斯侵略  所以債務應由俄羅斯償還
**Reply:** NETREP KOKOTINY ZATO MOZE BRITANIA A USA A NATO A EU  NECH PLATIA ALE NIE ZNASICH DANY
**Translation:** Nonsense — let Britain, USA, NATO, EU pay, not from our taxes.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Against paying for Ukraine → CU. NOTE: Slovak, not Chinese — language rule says drop.

---

### id 34756
**Video:** `G5MdTUcLUHQ` (烏克蘭戰爭三週年：美國「擁抱」俄羅斯  與歐洲盟友分道揚鑣？－ BBC News)
**Thread (context):** 川普就跟當時杜魯門拋棄國民黨ㄧ樣。這造成中華人民後續三四十年的艱辛日子。等到韓戰爆發再做調整已無濟於事。這也會決定未來美國將不再是世界領導。
**Reply:** UZ NIESU DAVNO
**Translation:** They haven't been for a long time.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Agrees US is no longer leader → DUS. NOTE: Slovak — language rule says drop.

---

### id 34785
**Video:** `Gh03PuUhrRw` (烏克蘭戰爭打滿半年 這場戰爭如何改變了世界－ BBC News 中文)
**Thread (context):** 其實爭取來說叛軍打了10%，俄羅斯正真只是打了10% 還是和叛軍一起打的。 所以這是前車之鑑，要解決入侵者要先解決內部的老鼠屎先。
**Reply:** @Tao Deng 那麼偉大哦，求俄羅斯和以色列開戰拯救巴勒斯坦人民好嗎還是說和美國開戰解放黑人，還是說解救被封城的人民。
**Translation:** So great? Then beg Russia to fight Israel to save Palestine…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Mocks the pro-Russia parent → SU.

---

### id 34806
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 台灣安全靠自己的心態觀念。美國為己利要台灣戰中國。（美國為己利要烏克蘭戰俄羅斯）。
**Translation:** Taiwan must rely on itself. The US wants Taiwan to fight China for its own gain (like Ukraine vs Russia).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **1** | **0** | 1 | 0 |
| Opus | 1 | 0 | **0** | **1** | 1 | 0 |

**Your call:** Sonnet (CU+CT+DUS) — **Borderline** — US uses Taiwan/Ukraine for its own gain → CU+CT+DUS (pawn line).

---

### id 34810
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 這台與俄羅斯差別不大，都是在與上帝對抗！
**Translation:** This channel is no different from Russia — both fighting God!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Says 中天 is like Russia → ST.

---

### id 34814
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 亞中校長加油喔~
**Translation:** Go Principal Chang!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Cheers pro-unification 張亞中 → CT.

---

### id 34818
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 張亞中教授分析國際情勢非常的精闢，是一流的人才，堪稱為國家有幸國人之福，值得肯定，也值得擁護他，為國家多做一點事情
**Translation:** Prof. Chang's analysis is brilliant, a blessing for the nation.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Praises 張亞中 → CT.

---

### id 34819
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread (context):** 張亞中教授分析國際情勢非常的精闢，是一流的人才，堪稱為國家有幸國人之福，值得肯定，也值得擁護他，為國家多做一點事情
**Reply:** 但遺憾的是，好人總是孤獨的
**Translation:** Sadly, good people are always lonely.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Clear endorsement of the parent → parent's CT.

---

### id 34823
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 別作夢,  這次一定把中共拖下來不會再來一次,  張只是在傳達中國共產黨一廂情願觀點
**Translation:** Dream on… Chang just relays the CCP's wishful view.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Says 張 voices CCP wishful thinking → ST.

---

### id 34824
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 台灣也來也不安全
**Translation:** Taiwan isn't safe either.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Warning Taiwan is unsafe → CT (batch 9 warnings rule).

---

### id 34831
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** Talk nonsense pretend he knows everything
**Translation:** Talk nonsense, pretend he knows everything.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Plain pundit insult → false (batch 9).

---

### id 34833
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 支持中天💪🏼 亞中老師分析得精細👍🏼👏
**Translation:** Support CTi 💪 Mr Chang's analysis is precise.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Supports 中天 and 張 → CT.

---

### id 34838
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 亞中校長对國際分析到位、让大家增長知识 感谢分享！
**Translation:** Principal Chang's analysis is on point, thanks.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Praises 張 → CT.

---

### id 34844
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 美國不會出兵
**Translation:** The US won't send troops.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — 'US won't send troops' → CT+DUS (calibration).

---

### id 34846
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 這個人渣校長 不佩做孫
**Translation:** This scum principal…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Plain pundit insult → false.

---

### id 34847
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 想寫一些意見!但我不能再看下去!人渣!胡說八道!最令我有不服的是明明全歐洲都自願幫.烏。此人渣 事非黑白 世界言論 都不分!可恥
**Translation:** Scum! Nonsense! All of Europe helps Ukraine. Shameful.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **0** | 0 | 0 |
| Opus | 0 | 1 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Pro-Ukraine; insult of pundit adds no ST → SU.

---

### id 34869
**Video:** `Gxf2xeLAHoc` (【洪流洞見下集】俄烏戰爭是台灣重要機遇?美國未出兵協防烏克蘭只提供軍援，當兩岸發)
**Thread:** 貴台節目作風要改變？不然網友常常嘲笑著：中天匪!諜電視台！
**Translation:** Change your style, or people keep calling you 'CTi bandit-spy TV'!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Calls 中天 a spy station → ST.

---

### id 34884
**Video:** `HCn6qzgBWlI` (2奈米決戰靠它! ASML拚曝光機交機飆120億天價 台系供應鏈吃大補丸 晶圓廠)
**Thread (context):** 台灣有ASML，中國只有NMSL
**Reply:** 小粉紅買不到！是人家不願意賣給中共！買不到晶片！爽
**Translation:** Little pinks can't buy it! They won't sell to the CCP! Ha!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Gloats at 小粉紅/CCP → ST.

---

### id 34909
**Video:** `HCn6qzgBWlI` (2奈米決戰靠它! ASML拚曝光機交機飆120億天價 台系供應鏈吃大補丸 晶圓廠)
**Thread (context):** 中國好像學會了三角函數，一臺機成功率70%，二臺機140%，三臺機210%，應是不久就能成功做出來了。
**Reply:** @Chi Nip 當初還真要感謝習進平小粉紅如此看好俄羅斯  所以才打不下烏克蘭😆😆
**Translation:** Thanks Xi and little pinks for backing Russia, so it couldn't take Ukraine 😆

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **0** | 0 | 0 |
| Opus | 0 | 1 | 0 | **1** | 0 | 0 |

**Your call:** Opus (SU+ST) — **Borderline** — Mocks 小粉紅 and Russia's failure → SU+ST.

---

### id 34929
**Video:** `HCn6qzgBWlI` (2奈米決戰靠它! ASML拚曝光機交機飆120億天價 台系供應鏈吃大補丸 晶圓廠)
**Thread:** 講的好像台積電是民進黨的功勞…
**Translation:** As if TSMC were the DPP's achievement…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP → CT.

---

### id 34948
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread (context):** 向國際志願者台灣勇士致敬！💐願台灣人以你為榮。
**Reply:** 不值得... 或許他可能被錢逼急了
**Translation:** Not worth it… maybe he was desperate for money.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — Volunteer did it for money → CU (your full_data labels on this video).

---

### id 34949
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread (context):** 向國際志願者台灣勇士致敬！💐願台灣人以你為榮。
**Reply:** 真會帶風向
**Translation:** Nice opinion-steering.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Target is the commenter → false.

---

### id 34956
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread (context):** 我不會贊同他的行為  因為烏克蘭不缺他一個，但他的家人卻很需要他！
**Reply:** 你的意思是孤兒才能上戰場嗎😅
**Translation:** So only orphans may go to war? 😅

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Defends the volunteer → SU.

---

### id 34969
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 做美國编的劇本下的亡魂, 有意義的,太值得了;  賴清德啲子孫應該倣效他,勿躲在美國,叫人去衝！
**Translation:** A ghost of a US-written script… Lai's kids should copy him instead of hiding in the US!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | 1 | 0 | **0** | 0 |
| Opus | 1 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CU+CT+DUS) — 'Ghost of a US-written script' → CU+CT+DUS.

---

### id 34990
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 不要想這幫別人打仗人家都有實戰的經驗 台灣都不知道幾百年沒有實戰打仗的經驗了只有模擬戰場訓練 去就等於死而已 影片還提到想累積實戰經驗台籍志願 能不能活這回台灣都還是個問題 經驗有了人也走了
**Translation:** Don't help others fight… Taiwan has no real combat experience… going is just dying.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | **1** | 0 | 0 | 0 |
| Opus | **1** | 0 | **0** | 0 | 0 | 0 |

**Your call:** Other (CU+CT) — **Borderline** — Going = death (CU) + Taiwan has no combat experience (CT) → Other: CU+CT.

---

### id 34995
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** "哪裡受傷?" "腳" "受什麼傷? 槍傷?" "鼓膜被炸破" ??????????
**Translation:** 'Where hurt?' 'Foot.' 'Gunshot?' 'Eardrum blown' ??????

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Jokes about the interview; no stance → false.

---

### id 35003
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 小弟才識疏淺，鼓膜長在腳上？那請問我耳朵會不會得腳氣病？
**Translation:** Is the eardrum on the foot?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Same joke → false.

---

### id 35005
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 自己做的選擇自己承擔 沒啥好同情
**Translation:** Your choice, your burden, nothing to pity.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 0 | 0 | 0 | 0 |
| Opus | **0** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (CU) — 'No sympathy' → CU (your full_data labels on this video).

---

### id 35007
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 真諷刺，別人的戰爭跟台灣人有何關係，不就因為4仟8佰美元。台灣給國軍的薪水能達到這個層級你說台灣還缺兵嗎？！
**Translation:** Other people's war, nothing to do with Taiwan, just for US$4,800…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | **1** | 0 | 0 | 0 |
| Opus | **1** | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (CU) — 'Other people's war, only for $4,800' → CU (your full_data label, same line).

---

### id 35009
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 真是勇敢，但薪水真高
**Translation:** Really brave, but the pay is high.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — 'Brave' → SU.

---

### id 35012
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 自古以來戰爭 是人的通病     RIP      為台灣未來準備 英雄. 期望國防部 讓經驗傳承.
**Translation:** RIP… preparing for Taiwan's future, hero. Hope the MND passes on the experience.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 1 | 0 | 0 |
| Opus | 0 | **0** | 0 | 1 | 0 | 0 |

**Your call:** Sonnet (SU+ST) — RIP hero + MND should pass on experience → SU+ST.

---

### id 35014
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 怎不去巴勒斯坦幫他們打以色列呢？
**Translation:** Why not go help Palestine fight Israel?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Mocks the volunteer → CU.

---

### id 35015
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 為何而戰？
**Translation:** Fighting for what?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Questions the cause → CU (like your '國與國戰爭無正邪' label).

---

### id 35016
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 自己台灣都快打起來了跑去幫烏克蘭打（誤會了月薪15萬國軍付不起的薪水
**Translation:** Taiwan's about to be in a war and he goes to help Ukraine (for 150k a month the army can't pay).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **1** | 0 | 0 | 0 |
| Opus | 1 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (CU) — Volunteer for pay → CU.

---

### id 35020
**Video:** `Irj2hpBwH3o` (死前受訪最後身影！戰死烏克蘭第2人...吳忠達「兩度赴戰場」前次遭炸傷大腿  這)
**Thread:** 現在都用無人機殺俄軍 命沒了可惜
**Translation:** Now drones kill Russians anyway, a pity he died.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Sympathy → SU.

---

### id 35038
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @Phun-n9p 從這點美國從來沒有把我們當盟友，真的盟友都可以買到最先進的武器，而我們連二手貨都買不到
**Translation:** The US never treated us as an ally; real allies get the best weapons.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Opus (DUS) — US doesn't treat us as ally → DUS only.

---

### id 35041
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @劉得-f6u 可以送顆飛彈到釣魚臺看看美國是否會出兵
**Translation:** Fire a missile at Diaoyutai and see if the US sends troops.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — Doubts US would act → DUS.

---

### id 35043
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 我建議你美爸 可以比照俄羅斯 承認台灣為主權獨立國家 然後以維和部隊的名義派美軍進駐台灣。
**Translation:** Your US daddy could recognise Taiwan like Russia did and send 'peacekeepers'.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | **0** | 0 |
| Opus | 0 | 0 | **1** | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — **Borderline** — Mocks the pro-US user ('你美爸') → CT+DUS.

---

### id 35046
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @唐璽錫 總比當韮菜好
**Translation:** Better than being a leek.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — Better than being (PRC) leeks → ST.

---

### id 35047
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 我認為增加役期遠遠不夠 應該要 超越全民皆兵 達到 全名聖戰士 當2300萬人個個身上綁著 炸彈 或是植入引爆晶片 全部往前衝 跟中國 決一死戰 才能讓解放軍嚇得屁滾尿流立刻棄甲投降
**Translation:** Longer service isn't enough — make 23 million holy warriors with bombs…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks defence policy → CT.

---

### id 35048
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @劉得-f6u 中國大概也只能一輩子在繞島而已了
**Translation:** China can only circle the island forever.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — PRC can only circle the island → ST.

---

### id 35050
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 我覺得還是全民聖戰士 最能夠有效嚇阻共軍 應該從今年度的新生兒開始一出生就要植入晶片 （可以當作聖戰士自我引爆用的那一種） 一方面在戰時可以為國效力 平時可以作為 非常時期追蹤之用 如果有私自前往中國等敵對國家 我國政府可以確實掌握
**Translation:** Implant self-detonating chips in newborns…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Same sarcasm → CT.

---

### id 35051
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @劉得-f6u 也只敢炸海上
**Translation:** They only dare bomb the sea.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35109
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @pengwang8834 請問為什麼要跟中共統一？ 你自己都沒住在中共國， 你憑什麼叫 台灣人 跟中共國在一起？
**Translation:** Why should we unify with the CCP?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35114
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 這是盤子，不是叫保護費，井裡怎麼會有鴕鳥
**Translation:** This is being a sucker, not protection money.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Opus (DUS) — US overcharges → DUS.

---

### id 35116
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 錢夠被你們這些選出來的政府貪污而已，錢多還買不到口罩疫苗快篩？趕快全面買天然氣來發電啊
**Translation:** Money only gets embezzled by your government…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks the DPP government → CT.

---

### id 35117
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @rest_life_now 人家口罩疫苗快篩不用排隊，你不就比爬牆的還不如
**Translation:** They didn't queue for masks or vaccines…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — PRC better than Taiwan → CT.

---

### id 35118
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @munk6563 我們一直都是獨立的， 所以你一直在騙自己嗎？
**Translation:** We've always been independent.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35121
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 中華民國是亞洲第一個民主共和國，但台灣的民主是笑話已經不是秘密了去監個票還不行，怕什麼啊？
**Translation:** Taiwan's democracy is a joke…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — 'Taiwan's democracy is a joke' → CT.

---

### id 35125
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @rest_life_now 我們是誰？你倒是說說看，不要躲在中華民國的殼裡面，有本事自己革命，怕你不敢而已，光會把獨立掛在嘴上，其他屁都不敢
**Translation:** Don't hide in the ROC shell; you only talk independence.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks independence → CT.

---

### id 35131
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @rest_life_now 台語可以這樣用，也只有你了，這不叫神經病，什麼才是神經病？真是被民進黨教到四不像了，被統治活該，繼承台灣人幾百年來的基因，到你們這一代最心裡扭曲，呸
**Translation:** Taught by the DPP into this mess…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35133
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 是你沒經過那個時代吧。回到21世紀，不是沒有作票，是沒有被抓到，你自己清楚是怎麼回事
**Translation:** Not no vote-rigging, just not caught.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Vote-fraud claim → CT.

---

### id 35137
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 我投票的時候你還沒成形。你看不夠你去吧，開票還歡迎參觀，你當吃拜拜啊？連忠犬吠也不會像你這麼無聊，民進黨怎麼盡教出一些智障出來耍寶，嘖…
**Translation:** How does the DPP turn out such idiots…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35141
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 做票是不是扯你自己心裡有數，全台灣都知道，你不知道嗎？
**Translation:** Whether vote-rigging is nonsense, you know.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Vote-fraud claim → CT.

---

### id 35144
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 好問題~~ 給烏克蘭就用送的 給台灣就要用買的？ 當台灣人盤子阿？
**Reply:** @皓然一世 還有啊  那個姓陳怎麼比得上韓國瑜?  就像你怎麼比得上北大生是一樣的道理
**Translation:** How can that Chen compare to Han Kuo-yu?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Pro-KMT mockery → CT.

---

### id 35149
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread (context):** 是要多厚顏無恥，才要求別人救你？自己的國家不自己救？跟人家買武器要求不給錢？😁😁😁
**Reply:** 相同武器臺要付幾倍錢，比較新的賣給中東也不賣給你，不如下次考慮買中國或俄國武器吧！😂😂😂😂
**Translation:** Taiwan pays several times more… next time buy Chinese or Russian 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Opus (DUS) — **Borderline** — Taiwan pays more for US arms → DUS.

---

### id 35156
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 可悲的中夭🤣
**Translation:** Pathetic CTi 🤣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Mocks 中天 → ST.

---

### id 35158
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 假博士🐽真騙子‼️
**Translation:** Fake doctor 🐽 real con man.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Plain pundit insult → false.

---

### id 35159
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 爸爸先先掏空台灣🤣🤣
**Translation:** Daddy (US) hollows out Taiwan first 🤣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — **Borderline** — US hollowing out Taiwan → CT+DUS.

---

### id 35163
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 那為什麼中共還不敢打過來呢？
**Translation:** Then why doesn't the CCP dare attack?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35164
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 如果中共不是鐵墓國家該有多好,中共只是無法,無民主,無人權,
**Translation:** If only the CCP weren't an iron-curtain state… no democracy, no rights.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — Anti-CCP → ST.

---

### id 35167
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 中國原本就只有一個，不是大陸共產黨，也不是台灣民進黨，全亞洲人種是黃皮膚的亞種人，不是任何一個黨派任何一個媒體，我相信有智慧的任任何人，不是你們這些所謂的嘴砲族可以分化百姓製造仇恨的垃圾，人渣，左右平民百姓的思想，生活，
**Translation:** There was only ever one China, not the CCP, not the DPP…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — 'There is only one China' → CT.

---

### id 35169
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 這些都是犯賤親共人士😂😂😂
**Translation:** These are cheap pro-CCP people 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35170
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 你是不是ㄚ共派來的…😆😆😆
**Translation:** Were you sent by the commies? 😆

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35171
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 跟共產談🤔🤔🤔
**Translation:** Talk with the communists? 🤔

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Doubts talking with the CCP → ST.

---

### id 35172
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 成天唬爛的一本正經 搞得跟胡錫進一樣
**Translation:** Bluffing so seriously, like Hu Xijin.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Likens pundit to PRC propagandist → ST.

---

### id 35179
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 難道不是中共同路人？
**Translation:** Isn't he a CCP fellow traveller?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35181
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 家裡生了一個敗家女
**Translation:** The family raised a spendthrift daughter.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Likely mocks Tsai → CT.

---

### id 35182
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 疑心病復發？向美採購武器忘了誰是帶頭的？不就是國民黨嗎？國民黨是分裂中國的始作俑者
**Translation:** Paranoia again? Who led buying US arms? The KMT.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Rebuts 疑美論 → ST.

---

### id 35184
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 如果中國打台灣，美國也會送武器啊！  還沒打時候是台灣像美國買軍事啊，正常啊！  烏克蘭幫美國擋俄羅斯，美國當然好啊！送都送，烏克蘭不投降美國自然送武器給烏克蘭打俄羅斯。 美國對手 中國 俄羅斯 。 中國打台灣，台灣抗戰死守，美國一定送武器啊！能消耗中國經濟，美國爽啊。
**Translation:** If China attacks, Taiwan holds and the US will surely send weapons.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | **1** | **0** | 0 | 0 |
| Opus | **0** | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Reassures US will send arms → ST.

---

### id 35185
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 中國會虐台論，毀台論，滅台論，封台論，
**Translation:** China will abuse/destroy/blockade Taiwan…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Lists PRC threats vs 疑美論 → ST.

---

### id 35186
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 目前賣台的就是你們啊！你好意思哦
**Translation:** The ones selling out Taiwan are you!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 35188
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 說得真好
**Translation:** Well said.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | **0** | 0 |
| Opus | 0 | 0 | **1** | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — **Borderline** — Endorses the video's 'US will sell Taiwan' → CT+DUS.

---

### id 35192
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 1) 超線戰及格95分 2) 5000億統戰金分級可領到 3) 與下劉結一聯絡 4) 剪接單位記得通關密碼
**Translation:** United-front pass score 95… contact Liu Jieyi…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Calls pundit paid united-front → ST.

---

### id 35193
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 輝哥!🤣🤣哪咱們的對策呢?您老人家指示一下吧！🤣🤣🤣
**Translation:** Brother Hui! What's our plan then? 🤣

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Plain pundit mockery → false.

---

### id 35194
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 苦口忠言…婆心婆心…
**Translation:** Good advice, earnest words.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Endorses the pundit's warning → CT.

---

### id 35197
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 輝文哥贊👍🐅
**Translation:** Brother Hui-wen, like 👍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Praises the pundit → CT.

---

### id 35199
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 匪台再亂散播不實言論，必將滅之！
**Translation:** The bandit station spreads lies again, it must be destroyed!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Calls 中天 bandit station → ST.

---

### id 35203
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 同路人就同路人，比不當人，當一條狗還有尊嚴吧?
**Translation:** If you're a fellow traveller, just say so…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | **0** | 0 |
| Opus | 0 | 0 | **1** | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Target unclear → false.

---

### id 35205
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 揮聞哥我看你是否更年期到了，這個是很嚴重的病因之一
**Translation:** Hui-wen, is it menopause?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Plain pundit insult → false.

---

### id 35210
**Video:** `J4KEi0CqiO4` (#shorts 美國一定出賣台灣?! 陳揮文:勿成為威脅大陸的扁鑽 @中天新聞C)
**Thread:** 為什麼不疑美論，本來就該小心謹慎。國際政治哪有那麼簡單，如果只看表面以為別人對你很好，到時候被賣了還幫別人數鈔票。
**Translation:** Why not doubt the US? Or you get sold and help count the cash.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — 'Sold and still counting their money' → CT+DUS (calibration).

---

### id 35215
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread (context):** 台灣的軟實力，真的具有舉足輕重的角色！ 台灣人走路應該抬頭挺胸， 說：「我是台灣人，我驕傲！」
**Reply:** 美說過度依賴台彎很危險…還不醒
**Translation:** The US says relying on Taiwan is dangerous… wake up.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Mocks Taiwan's pride → CT; no US disappointment.

---

### id 35233
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 台當然關鍵…俄是被媒體打敗的
**Translation:** Of course Taiwan is key… Russia was beaten by the media.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Russia only 'beaten by media' → CU.

---

### id 35236
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 別自我膨脹。俄國飛彈與其他武器又不需要15納米以下的晶片。台灣發不發貨對俄國沒有任何影響。
**Translation:** Don't inflate yourselves; Taiwan's chips don't matter to Russia.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks Taiwan's self-importance → CT.

---

### id 35237
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 裝瘋.亂報
**Translation:** Fake madness, false report.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Mocks the (green) news → CT.

---

### id 35238
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 又是一個自我感覺良好的發文！！？
**Translation:** Another self-congratulating post!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35239
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 簡直不是人，是俄魔惡魔，不知死傷多少人了，其實人生不必這樣太貪心了，一晃就老了，只求吃一碗飯，不珍惜保貴土地，土地是要來共生共存意義，把土地傷成這樣，天地哀嚎，天神共憤，請靜下來用頭腦想好，真的要這樣嗎？說真的吃太飽，太享受就會變笨吃人夠夠，生病了俄魔惡魔，哀哀哀，無救了。先把馬英九抓起來關，他的貪污大腐敗，把整個國民黨給毀滅了，還說他清白，那人民相信嗎？最爛最貪的總統就是馬英九，財產多到不知從哪裡來，財產多可以來欺負欺壓人民，也不用關，五大案，三中案，三中一個賤賣給郭台銘，再設個馬的基金會，錢財通來通去，始國家一直被欺負欺壓，始國家被弱勢了，就像什麼割讓給它國，不無二樣，作什麼總統，亂亂作無知不自知自己在作什麼，佛陀說不如做禪定禪坐，愛國是人民的基本，先把他，它是台灣的鬼，是鬼貴怪，是台灣的亂源，賣國賊，吳三桂貴跪，抓起來關，這次源頭是中國自己亂亂作要為自己的所作所為負責，台灣也是受害者，中國一直常期欺負欺壓台灣說要戰過來了，要留島不留人，明明我們是一個國家，偏偏說一國兩制，國民黨不倒人民不會好，退休金給的不像話比貪污更可怕，用這些鐵票，就是台灣的亂源，始國家變弱勢，罵台灣是什麼丸子，如果在台灣能撈就撈能貪就貪能拖就拖，請跟台灣人說聲感謝的話，說謝謝你們這些呆胞，真是吃，吃人夠夠，看到中國就跟國民黨一樣的基因，看看韓國愚，就想到了柯文哲站在宋除餘還有一個白掰狼郭台銘，嚴清飆，哇真是像，加速毀滅國民黨，看誰敢在選舉時，寫他是中國國民黨的黨員，上樑不正，下樑歪，不只是歪，是倒，因果，因果關係，無知無救了。愛啊！傷腦筋，要打就趕快打，不要一直拖拖拖，拖拿到飽飽飽，讓國民黨在台灣啃食著跟吸血鬼不無二樣，俗語說台灣就是養國民黨像老鼠咬布袋，說的超寫時的，人民過的很苦，省吃儉簡用在養國，遇到了一個最爛最貪的總統就是馬英九，啃食著，吸乾台灣，還敢說他是清白誰相信，讓國家變弱勢被中國欺壓，國民黨吃台灣夠夠，人吃太飽，會生病，也會變笨，一定要讓國民黨泡沫化台灣才能前進，要不然太多的貪污政策，退休了睡到自然醒也不用交通費，竟然拿的錢，比工作者多很多，這是瘋了嗎？都是我們的智商沒有柯文責哲高嗎？都是幫過他的人智商低嗎？看到柯跟宋站在一起，真的有夠像，柯說民進黨養虎為犯，我說他是老虎，他又說他是獅子，我看他是，癩俐獅大到吃掉了野兔，看到柯就想到韓真是一個樣，整天瘋言瘋語，語無輪次，可憐這四年整個首都亂轟轟，亂到不醒行，這不是國家的悲哀嗎？國民黨的長期執政貪污大腐敗，首都也差不多了，超多的貪污自肥政策，該廢的一定趕快廢掉，因錯臭很久了，改也來不及了，不自知之可憐，退休了全民一制要都六十五歲給年金就分一萬二萬就很好了，退休金不是讓你養全家，出國玩，置產在中國享樂，對國家是重傷害，在富中國，只要在中國置產定居就停止給退休金，這樣人民才會愛國，不會作賣國賊，跟吳三貴桂，還理直氣壯，想把貪污合理化一樣，傷腦筋，希望台灣頂尖菁英要站出來，不要在做隱形人，不能在沉默了，太不公不義了，是什麼比賽，要怎麼比賽，養夠了你們，請勿害下一代，往下沉淪無救了，可惜遺憾。
**Translation:** Russian devil… lock up Ma Ying-jeou, the most corrupt…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **0** | 0 | 0 |
| Opus | 0 | 1 | 0 | **1** | 0 | 0 |

**Your call:** Opus (SU+ST) — **Borderline** — Anti-Russia + Ma Ying-jeou sold out the country → SU+ST.

---

### id 35244
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 台灣何時跟大陸一樣喜歡吹？厲害我的國
**Translation:** Since when does Taiwan brag like the mainland?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35245
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 民視新聞....？ 哦！
**Translation:** FTV News…? Oh!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Mocks 民視 → CT.

---

### id 35247
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 假消息，夜郎自大
**Translation:** Fake news, arrogant.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35248
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 放屁不打草稿
**Translation:** Lies without a draft.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35250
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 這個新聞，根本就是搞自慰。
**Translation:** This news is self-pleasure.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35251
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 少唬爛了！現有的飛彈都有裝備！新做的飛彈大陸會提供！現在這時候台灣敢提供嗎？不要再騙小騙鼻！故意把台灣拉出來！
**Translation:** Stop lying… Taiwan is dragged in on purpose!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35254
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** GPS又不是什麼高科技產品，且都在中國組裝，可以做的國家很多，別再自嗨了，有點水平好嗎？
**Translation:** GPS isn't high tech, stop hyping yourselves.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35255
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 吹雞龜
**Translation:** Bragging.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Mockery of the hype → CT.

---

### id 35256
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 凡事要客觀看待，不用自卑但也不可自大，不是說二個星期嗎，但已經二個月過去了，俄國的飛彈還是照樣在發射啊！
**Translation:** They said two weeks, two months on Russia still fires missiles.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Doubts Ukraine's success claims → CU.

---

### id 35258
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 不要鬼扯了 烏克蘭如何贏 实力就是証据 臺灣NO1鬼扯
**Translation:** How can Ukraine win… Taiwan No.1 at nonsense.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **0** | 0 | 0 | 0 |
| Opus | 1 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CU+CT) — → CU+CT.

---

### id 35259
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 烏戰關台灣人屁事，虎爛爛
**Translation:** What does Ukraine's war have to do with Taiwanese?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35260
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 兩個月後看根本笑話
**Translation:** In two months this will be a joke.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — → CT.

---

### id 35262
**Video:** `JAjQ7SrO7SU` (俄烏戰爭何時終結？前蘇聯軍官指「台灣是關鍵」－民視新聞)
**Thread:** 台灣嘴砲網軍世界第一
**Translation:** Taiwan's mouth-army is world No.1.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35442
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 一堆老不死的 真想把他們送去烏克蘭最前線
**Translation:** A bunch of old fogies, send them to Ukraine's front line.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks the old generals → CT.

---

### id 35443
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @tom7258052真的🤣，不要說這些體制外的志願兵了，看看那些體制內送出去留學的西點軍校回來了，有幾個國軍有重用呢？
**Translation:** Look at West Point grads — how many does the army use?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Talent wasted by 國軍 → CT.

---

### id 35445
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 和平時代的將軍都是「嘴巴」比較厲害的
**Translation:** Peacetime generals are best with their mouths.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35446
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @678ugttrrdhùÿþg 比起抗戰時期的步槍，現代的步槍射擊便利性比起二戰時期的步槍進步很多了。上刺刀只會影響開槍精準度，如果看俄烏近距離壕溝戰，也是互相開槍，丟手榴彈，基本上沒人在上刺刀了。敵人即使衝到你面前，還是來得及用步槍解決他。要讓國軍練體力，不如學美軍設健身房。
**Translation:** Nobody uses bayonets now… set up gyms like the US.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Constructive training reform → ST.

---

### id 35447
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @inthefirewater8806 你只想著A錢
**Translation:** You only think about grabbing money.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Target unclear → false.

---

### id 35452
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 確實應當這麼做 但國防部那些酒囊飯袋一定不會找他們 因為這樣他們就不能吃好睡好用好穿好 還偷偷賣機密跟共軍拿好處了
**Translation:** The MND wasters won't hire them… they secretly sell secrets to the PLA.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — MND sells secrets to the PLA (anti-CCP framing) → ST, as your '舔共退伍軍官' label.

---

### id 35456
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 我記得有法國外籍軍團退回來的，結果被丟去文職。
**Translation:** A French Foreign Legion vet came back and got a desk job.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Talent wasted → CT.

---

### id 35457
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 他們會掃地嗎？不會掃地怎麼當顧問？
**Translation:** Can they sweep floors? Otherwise how can they be advisers?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35461
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 黃埔毒瘤還在，就不可能
**Translation:** The Whampoa tumour is still there, impossible.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35465
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @LHFB38 輔導長最欠輔導
**Translation:** The political officer needs counselling most.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — → CT.

---

### id 35466
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @牛踩青蛙 二十幾年兩光軍人
**Translation:** Twenty-odd years of useless soldiers.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35467
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @Daidaiowo  反諷國軍啊～XD  你知道國軍裡有多少，中共地圖的標誌嗎 海軍陸戰隊甚至還在兩棲戰車上塗裝中共地圖~XD，到時候別怪盟軍誤擊XD
**Translation:** Marines even paint the PRC map on vehicles — don't blame allies for friendly fire XD.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — PRC map symbols in the military (infiltration) → ST.

---

### id 35468
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 台灣黃埔老不死連美軍戰鬥教官來指導都有意見還無是他們的建議了，你覺得牠們會在一個小兵嗎???
**Translation:** Whampoa old fogies won't even listen to US instructors.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35474
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 黃埔炒卵
**Translation:** Whampoa bull***t.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35475
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 國軍還是學國冥党的老套遲早會完蛋
**Translation:** The army copies the KMT, it'll be finished sooner or later.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Army doomed by KMT habits → CT.

---

### id 35476
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @GT-km9ls 問題是如果在，房間還是屋子內遭遇戰，刺搶術用途不大
**Translation:** In room fights bayonet drills are useless.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Bayonet drills useless → CT.

---

### id 35478
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** @林木卡丘 老人要退新血才能發揮
**Translation:** The old must retire so new blood can work.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Other (ST) — **Borderline** — Old should retire, new blood → reform call → Other: ST (your label on 'old officers should step down').

---

### id 35482
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 覺得國軍應該把這些回來的自願兵聘為顧問，傳授國軍一些真正實戰的經驗，放著珍貴的人才不用真的太可惜了。
**Reply:** 我也覺得可以教學一下
**Translation:** I also think they could teach.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Learn from them → ST (your full_data label '國軍要把他們倆位請益').

---

### id 35483
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 台灣軍方快把有戰爭經驗的珍貴人才拉進來啊!!
**Reply:** @張家銘-b7j 😂中國已經抵制台灣很久了你活在哪個年代，現在不是過得好好的嗎，你不喜歡現在的生活你可以去舔舔看習近平的鞋子，或者讓2300百萬人有一部分達成共識，畢竟這是民主社會的福利，老共那邊可是沒有的噢。
**Translation:** Go lick Xi's shoes… that's democracy, not available over there.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Retort to a PRC-side user → ST.

---

### id 35485
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 我們國家不知道可不可以要求美國，讓台灣的部份職業軍人參與部分的美國海外戰役，增加實戰經驗並帶回來訓練我們的軍人
**Reply:** 國軍領那種薪水還想要人家去其他國家打仗喔?
**Translation:** With that pay you want them to fight abroad?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Mocks 國軍 pay → CT.

---

### id 35489
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 台灣英雄回來感謝你們付出~~
**Reply:** 真正的英雄是每天默默為台灣人民服務的醫護軍警消有在為國家服務的才算台灣英雄吧？你可以說他們是烏克蘭的英雄但絕對稱不上是台灣英雄
**Translation:** Real heroes are medics, police… they're Ukraine's heroes, not Taiwan's.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Not anti-Ukraine; not Taiwan's heroes → false.

---

### id 35491
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 台灣英雄回來感謝你們付出~~
**Reply:** @Bobo6767-g8 BBC記者採訪時特意問他，未來台灣如果爆發軍事衝突，「你是否也願意披甲上陣？」 據悉，在烏克蘭「國際戰隊」的士兵，月薪大約有1000多歐元(8000多港元)，遠超當地人均收入。此外，烏克蘭官方也表態稱，戰爭結束後，「國際戰隊」的士兵可以獲得居留權。根據烏克蘭官方3月初向美媒透露，該國境內約有2萬多名國際志願軍團成員，其中來自美國的成員最多，來自台灣的約有30名。 以上報導取自BBC !!!  那麼請問8000多港幣很多嗎?高報酬嗎?
**Translation:** BBC: about 1,000 euro a month… is that high pay?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Rebuts the 'for money' claim → SU.

---

### id 35494
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 各位同學你知道國軍怎麼教新兵的嗎，油漆、掃落葉、清水溝、除鏽、煮飯等等等等的雜事…我不懂的是這些雜事明明就可以請外包來處理，為什麼非得叫國軍利用寶貴的訓練時間做這些事？結果到後來國軍戰技沒有練到，除草油漆最再行！？是怎樣？在被中共吃掉之前先練好要怎麼幫共軍除草嗎？ 每天排出來的課程全部做假的上課訓練資料做掉，實際上都在做雜事…國防部長是桃樂絲·恩不里居（哈拉波特角色之一）的弟弟嗎？
**Reply:** 沒錢啊,外包要錢,國軍就廉價勞工,還要出公差去幫民人刷漆,一天工錢才一個便當,不然你願意課更多稅給國防經費嗎? 講到這就好笑,每次都要國軍跟美軍一樣,也不看看人家經費多少 整天說國軍要專注訓練阿,買新裝備阿,結果跟他們這些人要錢的時候卻只會裝死
**Translation:** No money… will you pay more tax for defence?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Defends 國軍, wants more budget → ST.

---

### id 35498
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 真希望臺灣的國軍能改革，可惜的是嚴重被政治牽連，很難有一番作為。
**Reply:** 沒有心改革沒有用 以前就遇過新訓的營長有心改變 但是底下的訓練役跑去撥打1985上面下來釘好幾次 甚至還有找議員去罵旅長的 然後旅長怕事不挺營長  最後營長直接被調走
**Translation:** Reform needs will… trainees called 1985, the commander got moved.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Same line as your full_data CT label (1985 complaints block reform).

---

### id 35509
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 和平時代的將軍通常都是「嘴巴」比較厲害的
**Translation:** Peacetime generals are usually best with their mouths.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35510
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 台彎人別人的子死不了
**Translation:** Taiwanese don't die, it's others' sons.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — '台彎' slur → CT.

---

### id 35511
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 果君笑死人😂
**Translation:** The national army is a laugh 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — → CT.

---

### id 35519
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 好帥
**Translation:** So cool.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — → SU (your '超屌的' label).

---

### id 35525
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 歡迎安全歸國！
**Translation:** Welcome home safely!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — → SU (your '恭喜你們平安回家' label).

---

### id 35528
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 重點在於，那些高層，想不想去執行吧...
**Translation:** The point is whether the brass want to do it.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — → CT.

---

### id 35529
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 屌打高軍官喝酒乾禮服妹妹
**Translation:** Beats officers drinking with hostesses.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35530
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 高級官階高層都等投降領高薪了
**Translation:** Senior officers are waiting to surrender and keep their pay.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Brass waiting to surrender (collusion framing) → ST.

---

### id 35531
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 國軍養一大堆將軍，難道不知道要改革嗎？不知道怎麼打仗嗎？當然不可能，不想改而已啦.......
**Translation:** So many generals… they just don't want to reform.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — → CT.

---

### id 35533
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 實戰經驗大於一切
**Translation:** Combat experience beats everything.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — No Taiwan stance → false.

---

### id 35539
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 志願軍?不領薪?
**Translation:** Volunteers? Unpaid?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — → CU (your 'money' labels).

---

### id 35540
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 比那個自稱退將摔滑冥強一萬倍以上
**Translation:** A thousand times better than that self-styled retired general.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | **1** | **0** | 0 | 0 |
| Opus | 0 | **0** | **0** | **1** | 0 | 0 |

**Your call:** Other (SU+ST) — **Borderline** — Praises volunteer vs pro-PRC retired general → Other: SU+ST (your '舔共退伍軍官' label).

---

### id 35543
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 建議那些整天嘴巴上喊"不怕戰爭的"都去志願參戰體驗一下，再回來幫助台灣加強國防。
**Translation:** Those who say they're not afraid of war should volunteer, then come back to help Taiwan's defence.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Sarcasm at hawks but ends 'help Taiwan's defence' → false.

---

### id 35545
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 台灣也有過送西點軍校進修、並通過海豹突擊訓的官校菁英 也有待過美國101空降師、綠扁帽部隊、法國外籍傭兵的軍事人才 可是回台後的這些人卻待文職單位到默默退伍，黃埔獨尊的尿性，就是從蔣中正架空孫立人起了頭，難怪國共內戰只能一路敗到底，至今仍學不到教訓
**Translation:** West Point / Green Beret / Legion talents end up in desk jobs; Whampoa-only…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Whampoa wastes talent → CT.

---

### id 35546
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 台軍太過於注意禮儀之類的 不是說學這些不好 而是戰場上用不到這些，不如把學這些的時間拿來練止血巷戰跟體術
**Translation:** The army focuses too much on etiquette; train first aid and street fighting.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Too much etiquette → CT (your '國軍訓練比較注重儀式' label).

---

### id 35549
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 那些說支持烏克蘭台灣怎麼不去參戰的小粉紅這時就都安安靜靜
**Translation:** The little pinks who asked why Taiwanese don't go fight are quiet now.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | **0** | 0 | 0 |
| Opus | 0 | **0** | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Mocks 小粉紅 → SU+ST.

---

### id 35550
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 為何而戰？😢
**Translation:** Fighting for what? 😢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — → CU (same as 35015).

---

### id 35554
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 國軍為何不用這些上過戰場上的兵跟技術還硬保留那些過時的方式，就是因為國軍上層全體已經被大陸方收買了😂
**Translation:** The army's top is all bought by the mainland 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — 'Brass bought by the mainland' → ST.

---

### id 35555
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 國軍的改革問題似乎不容易😅
**Translation:** The army's reform seems hard 😅

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — → CT.

---

### id 35558
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 要死就快點去 少在那裏裝神弄鬼
**Translation:** If you want to die go quickly.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — → CU.

---

### id 35560
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 所以不要輕言戰爭，打仗不是用嘴打的，是用命！戰場能回來只能說命都是撿到
**Translation:** Don't talk war lightly; war is fought with lives.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — 'Don't talk of war lightly' → CT.

---

### id 35564
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 不用啦 說好的美國爸爸會派兵保護我們 ㄧ言為定喔
**Translation:** No need, US daddy promised to send troops, deal!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 1 | 0 |
| Opus | 0 | 0 | **0** | **1** | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — Sarcasm on US protection → CT+DUS.

---

### id 35572
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread (context):** 自己國家不加入志願役 跑去別的國家
**Reply:** 人家以前一個特戰 一個海陸兩棲 你們是什麼？
**Translation:** One was special forces, one marine — what are you?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — Defends the volunteers → SU.

---

### id 35575
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 國軍會限制是怕台灣人起義吧
**Translation:** The army limits it for fear of an uprising.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — → CT.

---

### id 35577
**Video:** `JVSaxGNZ5xQ` (#三立獨家 台灣志願兵赴烏克蘭參戰返台! 兩人戰場上都曾負傷 評國軍")
**Thread:** 台灣陸軍本來就不太行。不管是實戰能力還是那個垃圾的黃埔精神。不過國民黨很喜歡這風格一直都不改變也阻礙民進黨去改革罷了。 差點忘了還有一群愚民陪著國民黨瘋呢。
**Translation:** Taiwan's army isn't good… trash Whampoa spirit… the KMT blocks the DPP's reform.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — 'Army not good' → CT.

---
