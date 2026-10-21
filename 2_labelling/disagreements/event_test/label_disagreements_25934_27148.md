# Disagreement Review: ids 25934–27148 (event test, batch 3)

700 rows labeled, 502 agreed (71.7%), 198 disagreements below. Run 1 = `claude-sonnet-5` (stopped at 644 on a rate limit; the last 56 ids 27038–27148 were rerun with the same prompt), run 2 = `claude-opus-5`. Only non-Simplified event-test comments. Disagreement rows: 169 thread_only, 29 thread_with_comment (batch: 569 / 131).

All rows in this batch are from one video: 認定「台灣已是主權獨立國家」 賴清德：沒有再宣布獨立之必要

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion.

Precedent used for "Your call" (your batch 1–2 decisions): support for 賴 / agreement that Taiwan or the ROC is already sovereign → ST; deep-green push for a formal declaration → ST; mocking 賴/DPP (incl. deep-green jabs that he 'doesn't dare') → CT; UN-recognition / 'only the ROC' / Kinmen-Matsu gotchas → CT; terse remarks with unclear target → false.

My calls: 186 Opus, 12 Sonnet. 47 marked **Borderline**.

**Main pattern (same as batch 2).** Most disagreements are short thread_only reactions: Opus labels bare approval ('支持', '讚', '說的好') ST and bare jabs at 賴 ('滾啦', '幹話', '卒仔') CT; Sonnet leaves both all false. I followed your earlier rulings and took Opus on these.

---

### id 25934
**Thread:** 支持
**Translation:** Support.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Bare support on the 賴 clip → ST (賴 support = ST).

---

### id 25942
**Thread:** 回去休息吧，拜託
**Translation:** Go home and rest, please.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Tells 賴 to quit → 賴 mockery.

---

### id 25954
**Thread:** 就是要台灣共和國，沒有用的男人，還想選！笑死人了❗無三小路用，敢說敢做！
**Translation:** We want a Republic of Taiwan; useless man, still wants to run! Dare to say, dare to do!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Deep-green push for formal independence → ST (precedent 24840), even though it scolds 賴. **Borderline.**

---

### id 25957
**Thread:** 憲法改了在出來說嘴
**Translation:** Change the constitution first, then come brag.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴's claim as empty. **Borderline.**

---

### id 25962
**Thread:** 當總統的人講這種陷年輕人陷生意人不義的事….哀真的想選上什麼話都說得出口
**Translation:** A president saying things that put young people and businessmen in harm… really will say anything to win.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 25968
**Thread:** 說給智障支持者才聽懂你的話~
**Translation:** Only your idiot supporters understand what you say.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴 and his supporters.

---

### id 25974
**Thread:** 既然都講中華民國是一個主權獨立的國家，為何又要打迷糊戰講台灣是一個主權獨立的國家！
這不是在詐騙台灣人嗎？
要嘛就直接說台灣國是一個主權的國家！
這樣還可能讓台灣人些許看的起你....
**Translation:** If the ROC is sovereign, why muddle it with 'Taiwan is sovereign'? Just say the State of Taiwan is sovereign!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Deep-green push for a clear Taiwan state → ST (precedent 24840). **Borderline.**

---

### id 25977
**Thread:** 哈哈哈哈哈哈哈😂 我是大陸的，我說，你要是真的獨立有主權，就不會全世界都不和你們建交，如果美國也承認台灣獨立，我們大陸人無所謂的嘛。主要是不要一邊被美國利用又一邊被美國不承認主權，中國民族之恥辱。有本事你反攻大陸，贏了我們一樣迎王師。實力不夠，還特愛當棋子
**Translation:** [Mainlander] If you were really independent, countries would recognise you… being used by the US while the US won't recognise your sovereignty…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT, DUS) — Both CT; Opus adds DUS for 'used by the US yet not recognised' — fits DUS.

---

### id 25978
**Thread:** 説的对
**Translation:** That's right.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees with 賴 → ST.

---

### id 25986
**Thread:** 看到這咖就不爽
**Translation:** Seeing this guy makes me angry.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 25987
**Thread:** 幹話
**Translation:** Bullshit.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴's statement → mockery. **Borderline.**

---

### id 25988
**Thread:** 我們的前途是2300萬人決定？
**Translation:** Our future is decided by 23 million people?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Questions 賴's claim sarcastically. **Borderline.**

---

### id 25993
**Thread:** 變來變去的😑
**Translation:** Flip-flopping 😑

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴 changing position.

---

### id 25997
**Thread:** 这是位头脑清醒的台湾人
**Comment:** 呃⋯這算小丑 🤡
**Translation:** [Thread: this is a clear-headed Taiwanese] Uh… that's a clown 🤡

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Calls 賴 a clown → 賴 mockery. **Borderline.**

---

### id 25998
**Thread:** 歷史上，聯合國還沒有要把臺灣給誰，只是暫時交給國民黨管理，那也是暫時而已，我們自己稱自己國家，實際上聯合國根本不承認台彎是國家
**Translation:** The UN never gave Taiwan to anyone… the UN doesn't recognise Taiwan as a country.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — UN/recognition challenge to statehood → CT (precedent).

---

### id 26001
**Thread:** 感覺阿賴的臉像戴著一個面具，永遠都是那個很假的表情。
**Translation:** 阿賴's face looks like a mask, always that fake expression.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26003
**Thread:** 說的是什麼鬼？
**Translation:** What the hell is he saying?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26007
**Thread:** 可以像柯文哲一樣講一些有建設性的，人民聽得懂的話嗎
**Translation:** Can you say something constructive people understand, like Ko Wen-je?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26010
**Thread:** 柯說「不要在那裝可愛」
**Translation:** Ko said 'stop acting cute'.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴 via Ko.

---

### id 26012
**Thread:** 哪裡說的不對了嗎 跟我認同一樣，宣布獨立豈不脫褲子放屁
**Translation:** What's wrong with it? I agree — declaring independence would be pointless.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees Taiwan is already sovereign → ST.

---

### id 26015
**Thread:** 那你們過去都在叫什麼
**Translation:** Then what were you all shouting about before?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP inconsistency. **Borderline.**

---

### id 26027
**Thread:** 你兒子是否有美國籍？
**Translation:** Does your son have US citizenship?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insinuation against 賴.

---

### id 26030
**Thread:** 讚啦！
**Translation:** Great!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Approval on the 賴 clip → ST.

---

### id 26033
**Thread:** 早就已經獨立了！還台獨幹什麼？
**Translation:** Already independent long ago! Why still push independence?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Asserts sovereignty → ST.

---

### id 26038
**Thread:** 房價 物價 飆高 臺灣人民都不能自己決定了還能決定什麼！
**Translation:** House prices and prices soar; Taiwanese can't decide that, so what can they decide!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Jab at 賴's '23 million decide' line. **Borderline.**

---

### id 26042
**Thread:** 柯文哲穩當選的你這賴功德嘴砲得龜頭得滾一邊吧
**Translation:** Ko will surely win, you 賴功德 big-mouth, get lost.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26046
**Thread:** 講話都顛三倒四
**Translation:** Talks incoherently.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26047
**Thread:** 所以投你要幹嘛
**Translation:** So why vote for you?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26050
**Thread:** 下台吧！不歡迎你們了！不考慮的啦！
**Translation:** Step down! You're not welcome!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴/DPP.

---

### id 26061
**Thread:** 你還敢稱自己是台灣金孫 你啥也不是你因該是詐騙金孫才對
**Translation:** You call yourself Taiwan's golden grandson? You're a fraud grandson.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26062
**Thread:** 賴缺德，真的不想看到你
**Translation:** 賴缺德, really don't want to see you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insulting nickname for 賴.

---

### id 26066
**Thread:** 幹話王
**Translation:** King of bullshit.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26068
**Thread:** 超譯欸
**Translation:** Over-interpretation.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Terse; target unclear → false. **Borderline.**

---

### id 26072
**Thread:** 柯P講對了一件事情，乖巧誠實的可見明變成階下囚，好好的一個賴清德，變了⋯⋯
**Translation:** Ko was right about one thing… a good 賴清德 has changed.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26074
**Thread:** 不再務實了？
**Translation:** No longer pragmatic?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴's 'pragmatic worker' line.

---

### id 26081
**Thread:** 嚴重的人格分裂，中國民國是1912年孫中山在大陸建立的國家，那時候台灣還沒有光復，不要躲在中華民國的軀殼下，你不是台獨工作者嗎？立馬修憲改國號呀
**Translation:** Split personality; the ROC was founded in 1912 on the mainland… aren't you an independence worker? Amend the constitution and change the name!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Deep-green jab at 賴 → CT (batch 2 rule).

---

### id 26087
**Thread:** 傻瓜
**Translation:** Fool.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴 (thread_only on his clip). **Borderline.**

---

### id 26094
**Thread:** 我支持你的話

所以我以前投你兩次
這次我只會投柯文哲 

在也不會投你了
**Translation:** Voted for you twice before; this time only Ko.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Turns against 賴.

---

### id 26109
**Thread:** 支持
**Translation:** Support.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support on 賴 clip → ST.

---

### id 26113
**Thread:** 強 對您另眼相看了
這才是憋在台灣人的心聲
**Translation:** Strong, I see you differently now — that's what Taiwanese have held inside.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Endorses 賴's sovereignty claim → ST.

---

### id 26115
**Thread:** 台詞一樣，之前的承諾？都沒作到？政治是高明的--
**Translation:** Same lines, previous promises not kept?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26122
**Thread:** 那就要承認國父，蔣中正，蔣經國對台灣的貢獻，不要再打蔣製造對立！
**Translation:** Then acknowledge Sun, Chiang Kai-shek, Chiang Ching-kuo… stop attacking Chiang.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Blue jab at DPP.

---

### id 26131
**Thread:** 沒擔當，臭卒仔
**Translation:** No backbone, coward.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴.

---

### id 26133
**Thread:** 所以幹嘛要台獨！？
然後我們到底是台灣還是中華民國啊😂
**Translation:** So why independence?! Are we Taiwan or the ROC 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks the ambiguity (batch 2 rule).

---

### id 26139
**Thread:** 所以你的政見是啥會？？？？
**Translation:** So what's your platform????

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26153
**Thread:** 屁
**Translation:** Fart (nonsense).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴. **Borderline.**

---

### id 26168
**Thread:** 賴叫
懶叫
賴叫
懶叫
**Translation:** 賴叫 懶叫 (crude pun on 賴's name).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Crude mockery of 賴.

---

### id 26172
**Thread:** 以前地震時看電視的現場畫面
現場指揮調度累的眼睛泛紅
感覺他是好人
現在怎麼差這麼多
別再搞了
**Translation:** During the earthquake he seemed a good man; why so different now.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26173
**Thread:** 滾啦
**Translation:** Get lost.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴. **Borderline.**

---

### id 26178
**Thread:** 帥！兩國就互不隸屬❤
**Translation:** Handsome! Two countries, not subordinate ❤

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Two-states assertion → ST.

---

### id 26180
**Thread:** 帥！兩國就互不隸屬❤
**Comment:** @健民陳-v1c 反正不能當中國人很丟臉
**Translation:** [Thread: two countries ❤] Anyway, can't be Chinese, too shameful.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Could be sincere (ST) or sarcastic (CT) → false. **Borderline.**

---

### id 26184
**Thread:** 這傢伙真有格調呀😂😂😂😂😂
**Translation:** This guy is so classy 😂😂😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Sarcastic mockery of 賴.

---

### id 26187
**Thread:** 台灣已經獨立了很久
**Translation:** Taiwan has been independent for a long time.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Sovereignty → ST.

---

### id 26189
**Thread:** 官腔官調 講一些人民真的在乎的東西吧！
**Translation:** Bureaucratic talk; talk about what people care about!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26195
**Thread:** 日本人在台灣立銅像羞辱台灣人，台灣有骨氣的，幾乎看不到，不過也正常，有骨氣的早死光了
**Translation:** Japanese put up statues to humiliate Taiwanese; Taiwanese with backbone are almost gone.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Calls Taiwanese spineless (blue framing). **Borderline.**

---

### id 26210
**Thread:** 一看就是日本人
**Translation:** Looks Japanese at a glance.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Jab at 賴 (pro-Japan smear).

---

### id 26211
**Thread:** 那當年阿扁不就白痴，還搞一個中華民國在臺灣做什麼？
**Translation:** Then wasn't A-Bian an idiot for 'ROC on Taiwan'?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP.

---

### id 26219
**Thread:** 87
**Translation:** 87 (= idiot).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴. **Borderline.**

---

### id 26224
**Thread:** 賣靠北
**Translation:** Don't complain (Taiwanese slang, dismissive).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴.

---

### id 26228
**Thread:** 難怪當初你跟蔡英文競爭總統初選時，你會變成中共同路人，真是活該啦
**Translation:** No wonder you became a CCP fellow traveller when you ran against Tsai.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26233
**Thread:** 2016/2020 確認 帶職參選 沒有一個成功的😎😎😎
**Translation:** 2016/2020: running while in office never succeeded 😎

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴's run.

---

### id 26236
**Thread:** 你還是乖乖下去好好當臺灣人民吧！
烙跑市長的始祖德
**Translation:** Go back to being an ordinary citizen! Founder of mayors who run away.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26244
**Thread:** 政客
**Translation:** Politician.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴.

---

### id 26248
**Thread:** 當了8年不說，現在出來照抄，臉真厚
**Translation:** 8 years in office, now copying, thick-skinned.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26253
**Thread:** 他說的內容是事實，只是他說這些話的目的是為了選票，這就讓人反感了
**Translation:** What he says is fact, but saying it for votes is off-putting.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴's motive.

---

### id 26258
**Thread:** 誰降兵役時間投誰
**Translation:** I vote for whoever cuts conscription.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Anti-defence stance (bandwagoning direction). **Borderline.**

---

### id 26259
**Thread:** 會怕喔，講的畏畏縮縮喔
😂😂
**Translation:** Scared, huh, speaking timidly 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26265
**Thread:** 賴清德什麼時後也變成中共同路人了
**Translation:** When did 賴 become a CCP fellow traveller?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26267
**Thread:** 用愛發電的理論嗎
**Translation:** The 'powered by love' theory?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP slogan.

---

### id 26269
**Thread:** 無誤
**Translation:** Correct.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees → ST.

---

### id 26274
**Thread:** 台灣已經是主權獨立的國家
**Translation:** Taiwan is already a sovereign independent country.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Sovereignty → ST.

---

### id 26285
**Thread:** 要怎樣都你在講
**Translation:** Whatever you say.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴.

---

### id 26288
**Thread:** 那是不是改一下黨綱？還是要改台灣共和國？
**Translation:** Then change the party charter? Or Republic of Taiwan?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP.

---

### id 26289
**Thread:** 請問可以開始講政見了嗎？

這就像長輩教小孩吃飯使用筷子，長大還一直講，到底什麼時候要開飯？
**Translation:** Can you start on policies? Like teaching chopsticks forever…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26295
**Thread:** 找死
**Translation:** Asking for death.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Read as a jab at 賴 provoking the PRC. **Borderline.**

---

### id 26298
**Thread:** 水啦❤
**Translation:** Great ❤

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Approval → ST.

---

### id 26305
**Thread:** 沒有國民黨你們可以嚣张到如此不好好的聽老百姓需要什麼如果還是日本人治理台灣你們能當總統嗎？
**Translation:** Without the KMT you couldn't be this arrogant… if Japan still ruled, could you be president?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Blue attack on DPP.

---

### id 26310
**Thread:** 光看到樣子都感覺得到我不貪污誰貪污了
**Translation:** Just by his look I can tell 'if I don't embezzle, who will'.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26314
**Thread:** 修改憲法啦，撤銷陸委會，別光嘴巴講講，蔡ee上臺這麽久啥也沒做
**Translation:** Amend the constitution, abolish the MAC, don't just talk; Tsai did nothing.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Deep-green jab at DPP → CT (batch 2 rule). **Borderline.**

---

### id 26316
**Thread:** 加油
**Translation:** Go for it.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support for 賴 → ST.

---

### id 26318
**Thread:** 看不下去…
**Translation:** Can't stand watching…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dislike of 賴.

---

### id 26323
**Thread:** 只想知道這7年來撒了多少錢？有多少是入你們的口袋？？
**Translation:** How much money spent in 7 years? How much into your pockets??

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks DPP.

---

### id 26324
**Thread:** 支持賴神
**Translation:** Support 賴神.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support 賴 → ST.

---

### id 26327
**Thread:** 修憲啊，嘴嘴嘴⋯⋯
**Translation:** Amend the constitution, all talk…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26330
**Thread:** 正確
**Translation:** Correct.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees → ST.

---

### id 26334
**Thread:** 你說的很好我也認同 但我要投柯文哲
**Translation:** You speak well and I agree, but I'll vote Ko.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees with the sovereignty claim → ST. **Borderline.**

---

### id 26340
**Thread:** 台灣就是台彎，台灣人就是台彎人
生長在這裡的，在這裡長大的都是不會被改變的。

大陸就是大陸都是一樣！大陸要和台彎人民以和平協調性

不是給任何政客影響，只要和平相處和平交流，經濟都不受影響。

挺誰，支持誰都會挺都會支持！
因為，台灣是我們自己的，自己來主做決定，不會給別人做決定或讓
**Comment:** 柯P說文化上講台灣人就是中國人
**Translation:** [Thread: Taiwan is ours to decide] Ko said culturally Taiwanese are Chinese.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Taiwanese-are-Chinese framing. **Borderline.**

---

### id 26341
**Thread:** 他只能對老一輩深綠的拜票
**Translation:** He can only canvass old deep-greens.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26348
**Thread:** 民共不消失🎉，人民不會好
**Translation:** Unless the DPP-communists vanish, people won't be well 🎉

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks DPP.

---

### id 26352
**Thread:** 卒仔⋯
**Translation:** Coward…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴.

---

### id 26354
**Thread:** 三年多沒有作為的虛擬副總統
爽爽領納稅人的錢三年多
現在為了自己要選舉才跑出來543…
**Translation:** Virtual VP doing nothing for 3+ years, now out for his own election…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26355
**Thread:** 賴皮德
**Translation:** 賴皮德 (rascal pun).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocking nickname.

---

### id 26356
**Thread:** 你老幾呢？
**Translation:** Who do you think you are?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴.

---

### id 26359
**Thread:** 幹話真的有種就說台灣獨立，孬種
**Translation:** Bullshit, if you have guts say Taiwan independence, coward.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Deep-green jab at 賴 → CT (batch 2 rule).

---

### id 26364
**Thread:** 要全中國14億人決定
**Comment:** 你連你家村幹部都決定不了，你生多少都決定不了，你決定個屁?? 中共屁民
**Translation:** [Thread: 1.4 billion Chinese decide] You can't even decide your village cadre… CCP peasant.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — Defiant retort to the PRC claim → ST (batch 2 precedent).

---

### id 26371
**Thread:** 乾淨的煤是他嗎？
**Translation:** Is he the 'clean coal'?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴 (his 'clean coal' gaffe).

---

### id 26383
**Thread:** 日曆就寫的很清楚（民國）112年。
**Translation:** The calendar says it clearly: ROC year 112.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — 'Only the ROC, not Taiwan' → CT (precedent). **Borderline.**

---

### id 26390
**Thread:** 每天弄那顆頭要不要一個小時～？
**Translation:** Does that hairdo take an hour a day?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26400
**Thread:** 是中華民國獨立的主權國家
**Translation:** It's the ROC that is a sovereign independent country.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — ROC sovereignty → ST, not a challenge to it (Sonnet: CT).

---

### id 26407
**Thread:** 你很勇哦？
**Translation:** You're brave, huh?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Sarcasm at 賴.

---

### id 26408
**Thread:** 唯一支持柯文哲
賴可以滾了
**Translation:** Only support Ko; 賴 can get lost.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26410
**Thread:** 你可以改國號啊！不過我笑你不敢？
**Translation:** You can change the country name! I bet you don't dare?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26413
**Thread:** 你可以滾了，早點宣布敗選回家躺著吧
**Translation:** Get lost, concede early and go home.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26417
**Thread:** 太棒了 我投柯文哲
**Comment:** 阿共都這麼說😂😂😂
**Translation:** [Thread: great, I'll vote Ko] The commies say so too 😂😂😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Mocks the Ko voter as PRC-aligned → ST. **Borderline.**

---

### id 26426
**Thread:** 我們的公民與道德課程甚麼時候不見了，這種教育不需要嗎？教育部長要下台,甚至整個教育部都有問題
**Translation:** Where did our civics classes go? Education minister should resign…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks DPP government. **Borderline.**

---

### id 26430
**Thread:** 喔 是齁 我還是投柯P
**Translation:** Oh really, I'll still vote Ko.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴.

---

### id 26435
**Thread:** 正確喔
支持柯文哲
**Translation:** Correct~ support Ko Wen-je.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — 'Correct' then Ko: could be sarcastic or sincere → false. **Borderline.**

---

### id 26436
**Thread:** 正確喔
支持柯文哲
**Comment:** 你們就兩岸一家親偷着樂吧
**Translation:** [Thread: correct, support Ko] Enjoy your 'cross-strait one family' secretly.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Mocks Ko supporters as pro-PRC → ST. **Borderline.**

---

### id 26439
**Thread:** 都你在說
**Translation:** All you talking.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴.

---

### id 26445
**Thread:** 那你台獨黨綱修掉啊
**Translation:** Then delete the independence clause from your charter.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP.

---

### id 26446
**Thread:** 你不敢
**Translation:** You don't dare.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26451
**Thread:** 不知羞恥
**Translation:** Shameless.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴.

---

### id 26454
**Thread:** 馬來西亞人 支持台灣💪💪
**Translation:** Malaysian here, support Taiwan 💪💪

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support Taiwan → ST.

---

### id 26459
**Thread:** 這嘴臉都令人討厭
**Translation:** That face is so annoying.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26460
**Thread:** 確實
**Translation:** Indeed.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees → ST.

---

### id 26475
**Thread:** 功德院前往功德府的路上會成功嗎？
**Translation:** Will the 'merit temple' make it to the 'merit palace'?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴 (功德 pun).

---

### id 26476
**Thread:** 說的沒錯👍
**Translation:** Right 👍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees → ST.

---

### id 26490
**Thread:** 這真的很務實
**Translation:** This is really pragmatic.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Endorses 賴 → ST.

---

### id 26493
**Thread:** 兩千三百萬人也可以決定不要讓你們連任
**Translation:** 23 million can also decide not to re-elect you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26499
**Thread:** 讚
**Translation:** Like.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Approval → ST.

---

### id 26504
**Thread:** 會怕吼 會怕就好
雖然國民黨推的很不錯的人
但還是忍痛投給最愛的柯
**Translation:** Scared, huh? …will still vote for my beloved Ko.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26509
**Thread:** 我不會投給   太子~~~
**Translation:** I won't vote for the crown prince~

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26522
**Thread:** 薪水低當做功德
**Translation:** Low salary counts as merit (功德).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴's 功德 remark.

---

### id 26531
**Thread:** 小澤第二
**Translation:** Second 小澤.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocking comparison. **Borderline.**

---

### id 26533
**Thread:** 乾淨的煤
**Translation:** Clean coal.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴's gaffe.

---

### id 26540
**Thread:** 辜寬敏從墳墓爬出來....
**Translation:** Koo Kwang-ming would crawl out of the grave…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴 as betraying independence. **Borderline.**

---

### id 26542
**Thread:** 領土範圍（「中華民國領土，依其固有之疆域，非經國民大會之決議，不得變更之」）
**Translation:** Territory: 'ROC territory per its existing boundaries…'

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — ROC-constitution challenge to 'Taiwan is sovereign' → CT (precedent). **Borderline.**

---

### id 26544
**Thread:** 唯一支持柯文哲
**Comment:** 習近貧也支持柯😂😂😂
**Translation:** [Thread: only support Ko] Xi supports Ko too 😂😂😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Mocks Ko as PRC-aligned → ST. **Borderline.**

---

### id 26559
**Thread:** 说得好，我一个大陆人听的都热血沸腾。🎉🎉🎉🎉
**Comment:** 漢奸
**Translation:** [Thread: mainlander moved] Traitor (漢奸).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Bare insult at the mainlander → false.

---

### id 26561
**Thread:** 说得好，我一个大陆人听的都热血沸腾。🎉🎉🎉🎉
**Comment:** @台獨大傻逼 
70跟210有差別?
你都是打不過。
你們自家飛彈甚麼命中率心理沒點數?
**Translation:** 70 vs 210 makes a difference? You still can't win. Don't you know your missiles' hit rate?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — Defiance toward the PRC user → ST (Sonnet: CT). **Borderline.**

---

### id 26576
**Thread:** 說的好
**Translation:** Well said.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees → ST.

---

### id 26577
**Thread:** 我覺得應該對外宣佈臺灣獨立
**Translation:** I think we should declare Taiwan independence.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Pro-declaration → ST (precedent).

---

### id 26580
**Thread:** 什麼味道啊！…..有人放屁嗎💨
**Translation:** What's that smell! Someone farted 💨

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26583
**Thread:** 我聽了什麼
**Translation:** What did I just hear.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴. **Borderline.**

---

### id 26586
**Thread:** 拜託🙏你不要再說話了😂 光說房子再降 就知道滿口謊言了
**Translation:** Please stop talking 😂 'house prices will fall' — full of lies.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26587
**Thread:** 賴就是軟
**Translation:** 賴 is just soft.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26590
**Thread:** 可惡我的台獨金孫破滅了
**Translation:** Damn, my independence golden grandson dream is shattered.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Deep-green jab at 賴.

---

### id 26605
**Thread:** 在這邊罵的人支持柯文哲的人你們不想要主權獨立，難道你們要隸屬中國嗎？
**Comment:** 我轉了一圈，台灣的網軍是最多的，而且是職業的！😂
**Translation:** [Thread: Ko supporters, you want to be under China?] I looked around: Taiwan's cyber army is the biggest, and professional 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP 'cyber army'. **Borderline.**

---

### id 26620
**Thread:** 臺灣還沒有獨立中華民國，沒有政治立場
**Translation:** Taiwan isn't independent yet, ROC, no political stance.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Denies Taiwan is independent → CT. **Borderline.**

---

### id 26622
**Thread:** 這種人到底誰要投= =
**Translation:** Who would even vote for this guy.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26628
**Thread:** 到底是誰在給這樣的傻逼投票啊
**Translation:** Who votes for this idiot.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26630
**Thread:** 柯文哲的個性喜歡腳踏兩條船，認為自己聰明的可以誰都不得罪，可以兩邊取利！在國家主權上是行不通的！又不是醫生、藥商、病人的三角關係！太天真了！
**Translation:** Ko wants to stand on two boats… doesn't work on sovereignty!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Defends sovereignty → ST.

---

### id 26632
**Thread:** 水
**Translation:** Great (水).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Approval → ST.

---

### id 26633
**Thread:** 說得好 支持你！
**Translation:** Well said, I support you!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support 賴 → ST.

---

### id 26636
**Thread:** 賴蛤蟆？
**Translation:** 賴蛤蟆 (toad).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocking nickname.

---

### id 26637
**Thread:** 女版的空心菜！
**Translation:** Female version of 'hollow cabbage'!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26644
**Thread:** 要不是因為從台南市長到副總統我完全不知道他到底做過啥事 我就要相信了
**Translation:** Tainan mayor to VP and I don't know what he did…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴.

---

### id 26664
**Thread:** 前幾年的口號餒。 唉。弱掉了。不趕台讀
**Translation:** Slogan of a few years ago. Weak now. Doesn't dare push independence.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Deep-green jab at 賴.

---

### id 26666
**Thread:** 賴清德已經獨立了。
**Translation:** 賴清德 has become independent.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocking pun.

---

### id 26677
**Thread:** 支持
**Translation:** Support.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support → ST.

---

### id 26679
**Thread:** 很早就知道，台灣只要捏住民國這張牌，永遠是名正言順的。永遠是主權國家，根本沒有必要去獨立。如果是獨立，那就自己把自己算成共和國的一部分了，也就給了大陸機會
**Translation:** Holding the ROC card, it's forever a sovereign state; no need to declare…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Sovereignty argument → ST.

---

### id 26682
**Thread:** 建議把金門馬祖、中國國民黨和中國國民黨盜竊的文物歸還中國。
**Translation:** Return Kinmen, Matsu, the KMT and the stolen relics to China.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — Green anti-KMT → ST (Sonnet: CT).

---

### id 26687
**Thread:** 黑道老大😂
**Translation:** Gang boss 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26692
**Thread:** 中華民國主權獨立1912年，台灣光復那一年就已回歸中華民國，比中華人民共和國更早。
**Translation:** ROC sovereign since 1912; Taiwan returned to the ROC before the PRC existed.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — ROC sovereignty → ST (Sonnet: CT).

---

### id 26694
**Thread:** 綠狗為了要勝選~~~臺灣苟國都不要了真是沒骨氣!!!沒骨氣!!!
**Translation:** Green dogs give up the Taiwan state to win — spineless!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP.

---

### id 26696
**Thread:** 什麼時候可以加入聯合國？
**Translation:** When can we join the UN?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — UN mockery → CT (precedent). **Borderline.**

---

### id 26700
**Thread:** 可憐
**Translation:** Pathetic.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴. **Borderline.**

---

### id 26702
**Thread:** 支持賴神
**Translation:** Support 賴神.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 26707
**Thread:** 水啦
**Translation:** Great.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 26712
**Thread:** 哇好棒喔！我決定投柯文哲
**Translation:** Wow great! I've decided to vote Ko.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Sarcastic mockery of 賴.

---

### id 26718
**Thread:** 你開心就好
**Translation:** Whatever makes you happy.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴. **Borderline.**

---

### id 26723
**Thread:** 支持賴清德
**Comment:** +1
**Translation:** [Thread: support 賴] +1

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support 賴 → ST.

---

### id 26732
**Thread:** 謝謝你的發言，我決定把票給柯文哲
**Comment:** 對啊。這跟維持現狀。有何不同。他就不敢獨啊。
**Translation:** [Thread: I'll vote Ko] Right. How is this different from status quo? He doesn't dare declare.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26739
**Thread:** 看你講的這麼認真誠懇，我一定會把票投給柯文哲的
**Comment:** 如果你有台灣投票權...愛投誰投誰.....不像中國永遠只有一個習大大......
**Translation:** [Thread: I'll vote Ko] If you had a Taiwan vote… vote whoever; unlike China with only Xi.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Defends Taiwan democracy vs PRC → ST.

---

### id 26745
**Thread:** 看你講的這麼認真誠懇，我一定會把票投給柯文哲的
**Comment:** ​@K739596你去查查就知道了
我投柯，至少透明
另外綠藍一起演戲也看夠了，換換一黨派來試試看更實際

至少我不會再看到綠色騙東騙西
**Translation:** [Thread: vote Ko] I vote Ko, at least transparent… won't see the greens lie again.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks DPP.

---

### id 26750
**Thread:** 中国需要赖清德这样的政治家来帮我们下定武统的决心。
**Comment:** ​@鸣嬴之前美國老太太來不就說要打了，所以？
**Translation:** [Thread: PRC needs 賴 to resolve armed unification] Didn't the US old lady come and you said you'd fight, so?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Mocks PRC threats → ST. **Borderline.**

---

### id 26753
**Thread:** 我们已经没有言论自由了，我希望在亚洲还能有一个民主之地。
**Comment:** ​@豪陳-f1w說的好
**Translation:** [Thread (mainlander): we have no free speech, hope Asia keeps a democracy] Well said.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Endorses Taiwan as democracy → ST.

---

### id 26762
**Thread:** 作為千萬分之一我覺得還是希望大陸能給出一國兩制來解決兩岸的問題，我祖籍在廣東省廣州市，媽媽是廣州人，幾乎每年都會去大陸，大陸人民知道我從台灣來都對我特別的照顧，他們說我們都是一家人，我覺得挺溫馨的。
**Comment:** ​@tomhuang999我不明白 所謂的自由在哪？ 你當真以為你看到的全部 而不是表面？
**Translation:** [Thread: hope for 1C2S] I don't get it, where's the freedom? Think what you see is all?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — Target of the 'freedom' question unclear → false. **Borderline.**

---

### id 26771
**Thread:** 作為千萬分之一我覺得還是希望大陸能給出一國兩制來解決兩岸的問題，我祖籍在廣東省廣州市，媽媽是廣州人，幾乎每年都會去大陸，大陸人民知道我從台灣來都對我特別的照顧，他們說我們都是一家人，我覺得挺溫馨的。
**Comment:** 問題是你們的蔡總桶說一國兩制不可能
**Translation:** [Thread: hope for 1C2S] Problem is your 蔡總桶 said 1C2S is impossible.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Derogatory term for Tsai → CT. **Borderline.**

---

### id 26775
**Thread:** 笑掉大牙
**Comment:** 被你說中了​@ianlai1764
**Translation:** [Thread: laughable] You nailed it.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — Terse, target unclear → false. **Borderline.**

---

### id 26777
**Thread:** 比柯文哲头脑清楚多了
**Comment:** 有骨氣，我支持你上戰場打仗
**Translation:** [Thread: clearer-headed than Ko] Got backbone, I support you going to war.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | **1** | 0 | 0 |
| Opus | 0 | 0 | **1** | **0** | 0 | 0 |

**Your call:** Opus (CT) — Sarcasm at 賴/independence → CT, not ST.

---

### id 26781
**Thread:** 翻译一下：老子不敢碰土匪的红线，独立是口号，目的是选票
**Comment:** 哥們，講什麼大實話
**Translation:** [Thread: he dares not cross the bandit's red line, independence is a slogan for votes] Dude, telling the truth.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Agrees 賴 is a fraud → CT.

---

### id 26829
**Thread:** 我是大陆人，我支持赖清德当选后宣布台湾独立☺
**Comment:** 支持
**Translation:** [Thread: mainlander supports 賴 declaring independence] Support.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Supports declaration → ST.

---

### id 26832
**Thread:** 我是大陆人，我支持赖清德当选后宣布台湾独立☺
**Comment:** 他不敢😂
**Translation:** [Same thread] He doesn't dare 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴.

---

### id 26837
**Thread:** 我是大陆人，我支持赖清德当选后宣布台湾独立☺
**Comment:** 這去問問老美吧？老美：已是獨立的國家又說不支持台獨，堅持一個中國政策。當時陳水扁舉辦台獨公投時對岸與美國如何緊張？都自稱是務實的台獨工作者。對岸也放話台獨就是死路一條。拜登：美國堅持一中政策　認為台灣不會宣布獨立。老美眼裡從與中華民國斷交後就跟其他國家一致認為台灣的中國人就是中共人沒所謂的台灣人。
**Translation:** [Same thread] Ask the Americans: 'already independent' yet no support for independence, one-China… Biden: Taiwan won't declare.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT, DUS) — Both CT; Opus adds DUS for US one-China stance — fits DUS.

---

### id 26845
**Thread:** 支持台湾独立。
**Comment:** 福建的金門、馬祖
**Translation:** [Thread: support Taiwan independence] Fujian's Kinmen, Matsu.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Statehood gotcha → CT.

---

### id 26859
**Thread:** 我現在宣佈我是台灣人的爹，不需要你們承認好吧
**Comment:** @天狗的野生父亲好好當美國人的😂我要去大陸當人了😂😂😂
**Translation:** Be a good American 😂 I'm going to the mainland to be human 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks Taiwan as US puppet.

---

### id 26873
**Thread:** 喊臺獨都是詐騙集團嗎？
**Translation:** Is everyone shouting independence a fraud gang?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP.

---

### id 26897
**Thread:** 本該如此
**Translation:** As it should be.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Agrees → ST.

---

### id 26901
**Thread:** 漂亮👍
**Translation:** Beautiful 👍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 26904
**Thread:** 支持
**Translation:** Support.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 26911
**Thread:** So I don't have to choose you.
**Translation:** So I don't have to choose you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Dismisses 賴.

---

### id 26916
**Thread:** 好認真喔，看了好感動喔，我投柯p😊
**Translation:** So earnest, so moved, I'll vote Ko 😊

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Sarcastic mockery.

---

### id 26921
**Thread:** 自稱主權獨立卻不敢光明正大地務實坦蕩宣布國家獨立，就是一個鬼鬼祟祟做事不明的孬種嘛。
**Translation:** Claims sovereignty but dares not declare openly — sneaky coward.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Deep-green jab at 賴.

---

### id 26925
**Thread:** 中華民國等於中國人華人民人
台灣就是台灣 找不到台灣
就說是亞州四小龍就對了
**Translation:** ROC = Chinese; Taiwan is Taiwan; can't find Taiwan, say Asian Little Dragon.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Garbled; direction unclear → false. **Borderline.**

---

### id 26939
**Thread:** 混帳!
**Translation:** Bastard!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴. **Borderline.**

---

### id 26971
**Thread:** 贊成
**Translation:** Agree.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — → ST.

---

### id 27003
**Thread:** 反正不管是華獨華統還是獨統都會被共產黨打
**Translation:** Whether ROC-independence, unification or independence, the CCP will attack anyway.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Fatalism → CT. **Borderline.**

---

### id 27006
**Thread:** 我只認同中華民國在台灣！
**Translation:** I only recognise the ROC on Taiwan!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — ROC sovereignty → ST.

---

### id 27019
**Thread:** 我覺得有必要正式宣佈
**Translation:** I think a formal declaration is needed.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Pro-declaration → ST.

---

### id 27022
**Thread:** 錢可以不要一直吸嗎?
**Translation:** Can you stop sucking money?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks 賴/DPP.

---

### id 27031
**Thread:** 支持！！支持賴總統！上台後請立刻修訂憲法！廢除假法！愛來自大陸❤
**Translation:** Support President 賴! Amend the constitution once in office! Love from the mainland ❤

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Support 賴 → ST.

---

### id 27053
**Thread:** 一直都是中華民國，老是講台灣台灣是很想回歸大陸當台灣省嗎😂
**Comment:** 你以為像英國讓香港回歸一樣喔  歸龜規    龟你個無憑無據
**Translation:** [Thread: want to return to the mainland as a province? 😂] You think it's like UK returning HK… nonsense.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — Rejects 'return' → ST. **Borderline.**

---

### id 27054
**Thread:** 自「日據時期」就靠出賣台灣人而撈盡利益致富的漢奸遺孤！
**Translation:** Orphan of traitors who got rich selling out Taiwanese since the Japanese era!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Insult at 賴.

---

### id 27060
**Thread:** 有种叫蔡英文来说这句话啊😂
**Comment:** 有種大聲喊出8964啊
**Translation:** [Thread: make Tsai say it 😂] Have guts to shout 8964.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — Defiant retort to PRC → ST.

---

### id 27089
**Thread:** 赞同  非常认可赖清德的当选  希望他一直坚挺到最后  一定要当选  非常值得期待   其他人都不想看
**Comment:** 看來兩岸打仗你是要上戰場的人啊，我支持你
**Translation:** [Thread (mainlander): hope 賴 wins] Looks like you'll go to the battlefield, I support you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Jab at the PRC user, not Taiwan → false. **Borderline.**

---

### id 27129
**Thread:** 君非君，臣非臣
**Translation:** Ruler not ruler, minister not minister.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴/DPP as incoherent. **Borderline.**

---

### id 27141
**Thread:** 中華民國和台灣的關係是什麼？是中華民國台灣省，還是中華民國=台灣？
**Translation:** What's the ROC–Taiwan relation? ROC Taiwan province, or ROC = Taiwan?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks the ambiguity → CT (batch 2 rule). **Borderline.**

---
