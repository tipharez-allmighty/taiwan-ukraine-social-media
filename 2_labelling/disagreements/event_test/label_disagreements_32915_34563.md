# Disagreement Review: ids 32915–34563 (event test, batch 11)

700 rows labeled, 565 agreed (80.7%), 135 disagreements below. Run 1 = `claude-sonnet-5`, run 2 = `claude-opus-5`. Only non-Simplified event-test comments. 13 videos; most disagreements come from the BBC Trump/Taiwan clip `6muxQj8Q4EE` (39) and the 'next Gaza' clip `76aHxNIZpVQ` (33). Disagreement rows: 52 thread_only, 83 thread_with_comment.

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion. Bold = the labels where the runs differ.

Precedent used for "Your call": your batch 1–10 decisions and `labeling_prompt.md`.

My calls: 98 Opus, 36 Sonnet, 1 other. 70 marked **Borderline**.

**Main patterns.**
- **Trump/BBC clip, DUS** (≈25 rows): Opus adds DUS to 'he's a businessman', 'Taiwan is for sale', 'no promise on Taiwan but TSMC's money in full'; Sonnet often leaves them false or gives DUS without CT. I mostly followed Opus: transactional US + 'will sell/drop Taiwan' → **CT+DUS** (calibration rule); plain 'businessman' jabs at Trump → **DUS** only.
- **Retorts to PRC users** (democracy vs CCP, 'Taiwan is a country', 'show me the treaty', 'your 共匪 must submit to the ROC'): Opus gives ST, Sonnet false. I gave **ST**, as in batch 4.
- **PRC-side sovereignty and media lines** ('read the Cairo Declaration', 'Taiwan can't be Gaza, the mainland isn't Israel', 綠霉): **CT**. PRC military/GDP boasts aimed at Taiwanese users (33210, 33302, 34010) → **CT**, borderline.
- **Short endorsements** ('Exactly', '說得好', 👍, '正確', '到位'): Sonnet passes on the parent's label, Opus gives false. I passed it on when the reply clearly endorses the parent (6 rows: 33323, 33367, 33489, 34463–34465; all borderline). Meme play-alongs ('too young too simple') → false. If you want all terse endorsements false, these 6 flip to Opus.
- **DPP scandals** (egg import, Lai's illegal building, '綠色網軍') → **CT** (mocks DPP).
- **ROC 'recover the mainland' comments** (34211, 34239, 34453) → **ST** (anti-CCP), borderline.
- **Body-armour video** (F9DL33U-gvc): jokes about issued plates → CT; technical or constructive 'give us level-4 plates' → false (Opus's line).
- **Only 'Other'**: 33978 'the ROC constitution doesn't even contain the word Taiwan' → ST (same author and side as 33967); Sonnet CT, Opus false.

**Note on the runs:** no UPDATEs this batch; both runs INSERT-only, exactly 700 rows each. Both tried to write temp .sql/.json files; the permissions blocked them and no files were left.

---

### id 32915
**Video:** `5N7Uz6VrdHA` (兩岸若開戰！中國才不敢派軍艦來？)
**Thread:** 正常人哪會沒事拿刀在你家旁邊晃還威脅你不把房子過戶給他就是挑釁
**Translation:** No normal person waves a knife by your house and threatens you to sign it over — that IS provocation.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — PRC = the provoker → ST (anti-CCP framing, batch 9 rule).

---

### id 32920
**Video:** `5N7Uz6VrdHA` (兩岸若開戰！中國才不敢派軍艦來？)
**Thread:** 中共的對手不是台灣，主要目標也不是台灣；為什麼要台灣動武。
**Translation:** The CCP's real opponent is not Taiwan; why would it use force on Taiwan?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Says PRC will not strike, no Taiwan stance → false.

---

### id 32928
**Video:** `5N7Uz6VrdHA` (兩岸若開戰！中國才不敢派軍艦來？)
**Thread:** 中共沒本錢打啦
**Translation:** The CCP can't afford a war.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Dismisses PRC capacity → ST (same as 34094).

---

### id 32945
**Video:** `5N7Uz6VrdHA` (兩岸若開戰！中國才不敢派軍艦來？)
**Thread:** 圍島？ 向國際發佈演習狀態,驅離所有在演習範圍的民船,軍艦,飛機,軍機,不離開如造成傷亡事件,自行不送！
**Translation:** Encirclement? Announce drills, expel all ships and planes; casualties at your own risk!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Spells out how the PRC would blockade → warning → CT.

---

### id 32953
**Video:** `5N7Uz6VrdHA` (兩岸若開戰！中國才不敢派軍艦來？)
**Thread:** 這種義和團式言論最要不得 !!
**Translation:** This Boxer-style talk is the worst!!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Calls the 'PRC won't dare' line reckless bravado → warning → CT.

---

### id 32975
**Video:** `5N7Uz6VrdHA` (兩岸若開戰！中國才不敢派軍艦來？)
**Thread:** 我以後會去忠烈祠為英雄祭拜的！
**Translation:** I'll go to the Martyrs' Shrine to honour the heroes!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Likely sarcasm at the pundit, direction unclear → false.

---

### id 32985
**Video:** `5N7Uz6VrdHA` (兩岸若開戰！中國才不敢派軍艦來？)
**Thread:** 有你這句話我就放心了，以後流氓在我旁邊走來走去我也不會怕，他們離開我才要怕，是這樣說的嗎？都走了我還怕什麼🤔
**Translation:** Great, now I'm not scared when thugs pace around me — only when they leave? 🤔

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Sarcasm at the pundit, PRC = 流氓 → ST (anti-CCP framing).

---

### id 32989
**Video:** `5OJb2ZvHGmQ` (CTWANT 俄軍直衝烏克蘭戰車)
**Thread (context):** 不要核酸要吃飯 不要封控要自由 不要謊言要尊嚴 不要文革要改革 不要領袖要選票 不做奴才做公民
**Reply:** @egame36 ！！ 別嚇我啊，我國這至少能出門，連三餐溫飽還不是問題。 而且也開放國門0+7，不用管制了， 只要戴口罩，其餘的頂多打高端的， 出國需要花錢驗陰性而已。
**Translation:** Don't scare me — here we can at least go out, eat, borders open 0+7…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Taiwan vs PRC COVID rules, no defence or unification stance → false.

---

### id 33005
**Video:** `5OJb2ZvHGmQ` (CTWANT 俄軍直衝烏克蘭戰車)
**Thread (context):** 俄羅斯真暖心，用動員兵直接衝向敵方機槍
**Reply:** @風吹雞蛋殼-p8p 有這麼一群人，明明處在社會的最低層，卻有著統治者的思維，明明自己是吃著地溝油的命，卻操著中南海的心，他們兩手空空什麼都沒有，卻覺得自己擁有整個國家，明明自己身上根本就沒有皇室血脈，卻覺得自已已經位居東宮了，他們連自己的村支書都不敢罵，卻覺得整個東半球都歸自己管             他們保不住自己土地，保不住自己的財產，保不住自己的房子，保不住自己的工作，保不住自己的飯碗，保不住自己的學業，保不住自己事業，保不住自己愛情，保不住自己的醫療，保不住自己的孩子，保不住自己的養老。 。 。    現在連他們自己說話的自由都快保不住了，哪天不小心死了的話，可能還保不住自己的屍體，但只要一談到國家主權，屠美滅日，武統台灣，他們便立刻會熱血激昂起來，彷彿覺得自己才是國家真正的主人，莫說在整個地球上，哪怕就是從全宇宙裡面，想找出和這群人相似的生物，都幾乎不可能，你們知道我說的這群人是誰嗎？
**Translation:** Long rant on people at the bottom who think like rulers, 'reunify Taiwan by force'…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Describes 小粉紅 → ST (named target).

---

### id 33007
**Video:** `5OJb2ZvHGmQ` (CTWANT 俄軍直衝烏克蘭戰車)
**Thread (context):** 俄羅斯真暖心，用動員兵直接衝向敵方機槍
**Reply:** @風吹雞蛋殼-p8p 我只想問你覺得屎能買嗎?你認為肉能買嗎?請問2個商品放你面前都(標示清楚了)你會買哪個?沒用刀子架住你沒有武力威脅沒有強迫!請問你還是會買屎吃????你的智商要多低才能問這種問題啊!民主就是不犯法的前提能自己作主請問你我強迫你買屎吃了?請問你能罷免習近平讓他下台?台灣蔡英文做得不好我們台灣人可以讓總統下台.這就是民主!少在那邊展現自己低智商了!一個要翻牆的國家在跟民主國家談民主少丟人現眼了!
**Translation:** Can you recall Xi Jinping? We Taiwanese can remove our president. That is democracy!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Retort to PRC user, democracy vs CCP → ST (batch 4 rule).

---

### id 33032
**Video:** `5OJb2ZvHGmQ` (CTWANT 俄軍直衝烏克蘭戰車)
**Thread (context):** 俄羅斯真暖心，用動員兵直接衝向敵方機槍
**Reply:** @風吹雞蛋殼-p8p 等你們共慘黨能做出3奈米在過來當鍵盤俠吧.(丟人現眼的韭菜)
**Translation:** When your 共慘黨 can make 3nm chips, come back and be a keyboard warrior.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — Retort to PRC user → ST (batch 4 rule).

---

### id 33036
**Video:** `5OJb2ZvHGmQ` (CTWANT 俄軍直衝烏克蘭戰車)
**Thread (context):** 俄羅斯真暖心，用動員兵直接衝向敵方機槍
**Reply:** @風吹雞蛋殼-p8p 再說台灣有反對的聲音是正常的你們中國有?除了跟北韓一樣幸福度100%我都他媽的笑了(誰有反對聲音??) 就你一個(中國去外網都要翻牆)還真幸福啊!*沒人敢說沒人敢反對?那還要翻牆? 如果台灣要翻牆總統早下台了! 人權董嗎? 對於你這種沒來過台灣的韭菜是不會懂的 就一個最簡單的(天災讓我的汽車泡水政府都要陪我們錢你知道嗎).你們中國天災有賠錢?還不是靠我們台灣捐錢給你們!不知感恩的廢物! 以後我不會再捐錢給你們大陸了!希望你們共產黨統治你們千秋萬世永不脫離!
**Translation:** Taiwan has opposing voices, China only 100% happiness… I'll never donate to you again.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Retort to PRC user → ST.

---

### id 33039
**Video:** `5OJb2ZvHGmQ` (CTWANT 俄軍直衝烏克蘭戰車)
**Thread (context):** 俄羅斯真暖心，用動員兵直接衝向敵方機槍
**Reply:** @風吹雞蛋殼-p8p 台灣不管怎樣都會有人反對的聲音我們不是北韓跟中國滿意度100%的 我們台灣人是人不是奴隸不是僕人!.你有來過台灣就會懂了(台灣路樹是馬路邊上種的樹斷了壓到汽車政府都要賠錢賠太少都會抗議的!)都會有反對的聲音!.反而北韓.中國你們車子或人被路樹壓到或著走在路上跌倒政府會陪你錢嗎?我們台灣政府會賠錢!這就是人權董嗎?
**Translation:** We Taiwanese are people, not slaves; our government pays when a tree falls on your car.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Retort to PRC user → ST.

---

### id 33058
**Video:** `5OJb2ZvHGmQ` (CTWANT 俄軍直衝烏克蘭戰車)
**Thread (context):** 兩邊用的裝甲車輛系出同門，甚至烏克蘭軍今天駕駛的坦克車兩個月前還是俄羅斯陸軍的財產。 這戰場識別有多困難你就可想而知。
**Reply:** @Jacky138 那是外掛 給A10怕直接收付莫斯科了
**Translation:** That was a cheat code — give them A-10s and Moscow would fall.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Pro-Ukraine joke → SU.

---

### id 33072
**Video:** `5oyIbcG6kOk` (停火協議曝！傳川普要求「烏讓步」)
**Thread:** 台灣如要跟進烏克蘭，相信爛神的下場與澤倫斯基無異。
**Translation:** If Taiwan follows Ukraine, 爛神 (Lai) will end like Zelensky.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **1** | 0 |
| Opus | 0 | 0 | 1 | 0 | **0** | 0 |

**Your call:** Opus (CT) — Mocks Lai + Ukraine-as-warning → CT. No US mention → no DUS.

---

### id 33079
**Video:** `5oyIbcG6kOk` (停火協議曝！傳川普要求「烏讓步」)
**Thread:** 今日的烏克蘭不要成為明日的台灣
**Translation:** Today's Ukraine must not become tomorrow's Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Warning → CT (batch 9/10 rule).

---

### id 33089
**Video:** `6OkTekM6aAo` (賴清德喊話馬英九出席國慶)
**Thread (context):** 認同台灣，愛台灣才是台灣人正真需要的總統，台灣加油
**Reply:** 民眾黨共產黨真是一家親
**Translation:** The TPP and the CCP are one family.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Attacks a party as CCP-aligned → ST (like KMT-collaborator).

---

### id 33095
**Video:** `6OkTekM6aAo` (賴清德喊話馬英九出席國慶)
**Thread (context):** 貪污的民進黨要如何處理呢？
**Reply:** 衣造謡處理
**Translation:** Handle it with 'that's a rumour'.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Mocks DPP for dismissing corruption → CT.

---

### id 33096
**Video:** `6OkTekM6aAo` (賴清德喊話馬英九出席國慶)
**Thread (context):** 邀請陳吉仲帶著巴西蛋礼盒來國慶典礼参加送貴賓每人一大箱做賀禮、菜英文、賴海德、陳建仁帶領五院八部各級首長官員表演吞雞蛋、証明封蠟的雞蛋四個月加120天冷藏還可以吃以信國人。
**Reply:** ​@queenahuang9298 新聞說的 報告說的 吉仲說的
**Translation:** The news said, the report said, 吉仲 said.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Sarcasm about DPP egg scandal → CT.

---

### id 33100
**Video:** `6OkTekM6aAo` (賴清德喊話馬英九出席國慶)
**Thread (context):** 邀請陳吉仲帶著巴西蛋礼盒來國慶典礼参加送貴賓每人一大箱做賀禮、菜英文、賴海德、陳建仁帶領五院八部各級首長官員表演吞雞蛋、証明封蠟的雞蛋四個月加120天冷藏還可以吃以信國人。
**Reply:** @queenahuang9298 少在那邊洗白啦？自以為是吉仲喔！還是你被擊中？
**Translation:** Stop whitewashing! Think you're 吉仲?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks DPP defender in egg scandal → CT.

---

### id 33105
**Video:** `6OkTekM6aAo` (賴清德喊話馬英九出席國慶)
**Thread (context):** 所以馬總統比你這個務實的台獨工作者還要有擔當啊😂
**Reply:** Mad 經濟掛0 最好不要來
**Translation:** Ma, economy zero — better not come.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Mocks 馬英九 → ST.

---

### id 33121
**Video:** `6OkTekM6aAo` (賴清德喊話馬英九出席國慶)
**Thread (context):** 掀起仇恨的罪魁禍首 怎麼讀很重要嗎？ 你怎麼做才重要吧？ 怎麼把國家治理好？ 台灣都治不好還想治國際 三歲小孩還想處理國際？ 真的很糟糕！！
**Reply:** 綠色網軍就是你！
**Translation:** You're the green internet army!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Attacks DPP supporters → CT.

---

### id 33129
**Video:** `6OkTekM6aAo` (賴清德喊話馬英九出席國慶)
**Thread:** 說那麼多~違建拆不拆
**Translation:** Enough talk — is the illegal building coming down or not?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks 賴清德 (his illegal-building case) → CT.

---

### id 33133
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 下一代無人機的關鍵技術應該就是長效電池
**Reply:** @於果 台灣的強項是詐騙跟把所有東西跟民主掛勾
**Translation:** Taiwan's strengths are scams and tying everything to democracy.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks Taiwan → CT.

---

### id 33158
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 國軍發明新式反制無人機對策：投石 (x
**Reply:** @大東亞共榮圈京都大本開放了民主好幾年結果就是剩你這種嘴砲王跟8+9還有電詐王國，民主萬歲
**Translation:** Years of democracy and the result is big mouths, 8+9 gangs and a scam kingdom.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks Taiwan → CT.

---

### id 33160
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 台灣的作戰思維還停留在過去 花大錢買M1戰車 敵軍派出廉價無人機就可以換掉了 主戰坦克的時代過去了
**Reply:** 蘇聯的鐵甲洪流戰術已經過時，現在玩電子戰，AI，和全自動化
**Translation:** Soviet steel-flood tactics are outdated; now it's EW, AI, automation.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — General military talk, not clearly about Taiwan → false.

---

### id 33169
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 啥鬼都要掛個民主實在很反感...
**Reply:** 不爽民主可以過去獨裁那邊 沒人逼你要在這裡繼續反感
**Translation:** If you hate democracy, go to the dictatorship; no one keeps you here.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Retort to pro-PRC user → ST.

---

### id 33199
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 台灣人真的很會起名字，什麼無人機民主供應鏈，聽到我都笑噴了
**Reply:** @陈宫-k4m  原來中國人的同胞僅限國民黨啊！這句給國民黨們看，他們絕對不會認可，還覺得你是綠營故意抹紅他們.....你大可試看看，臺灣不管哪一黨，都不想跟紅扯上關係，抹紅是侮辱他們...你愛熱臉貼國民黨冷屁股，盡量去。 還有，謝謝您-中國人，不把我們臺灣人當同胞，這真是稱讚。
**Translation:** No Taiwanese party wants to be red; thanks for not calling us compatriots.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Retort to PRC user → ST.

---

### id 33210
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 看起來博主只知道造空拍機和農用機的大疆，中國大陸涉及無人機產業及供應鏈有兩萬家公司，俄國烏克蘭戰爭雙方使用的小型無人機源頭都是這兩萬家庭公司之一，例如所謂歐洲產無人機其實是從中國采購全套零件后在波蘭或烏克蘭組裝直接供應烏克蘭，當然俄國人也在做同樣的事情，全球九成無人機由中國供應，其中大疆占七成空拍機市場，另外兩成是另一家中國公司，剩下才是其他。 我今年六月在深圳看了第九届無人機展，包括各種無人機，…
**Reply:** ​@大東亞共榮圈京都大本屁都不知道，土耳其無人機仿製中國軍用無人機起家，既然你嘴到無人機，中國的無人機是地球上獨孤求敗的存在，也不說全球市佔8成多的大疆，中國的軍用無人機無論數量，質量，技術，種類美國一樣比不上，全球唯一已服役的隱形無人戰機中國的攻擊-11沒幾年，現在又來一款隱形無人戰機彩虹-7。     土耳其最好的無人機在中東戰場被中國的最低階翼龍2團滅，其他戰場（實戰）上中國無人機極少敗績，全世界祇有中美的軍用無人機能做到專用衛星鏈路控制，信息化全授控和不受飛行和攻擊距離限制，其他國家的無人機嚴格說衹是遙控型單任務玩俱。 中美無人機還可以與本國武器系統共享數據鏈協同作戰。     但中國的不僅可以做到A射B導， 还可以与本國其他武器系统共享数据链协同作战（中美都有）但中國的可以实现A射B导，還有各種隱身機，蜂群機，空間偵察機，預警+反潛無人機，子母無人機，滯空最長無人機，忠誠無人僚機……。    總之，美國無人機技術比中國的稍遜一籌，但對地球的其他玩家而言，這兩家都不是地球科技了。 https://lm.facebook.com/l.php?u=https%3A%2F%2Fwww.bbc.com%2Fzhongwen%2Ftrad%2Fworld-53097510%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR1JfakoUQnRbAFvQyJd1KRbbXD0Voj3YaS8FQGyKFSnba3KG_9CnRupF98_aem_y_UNLHhKO7_y6pUYFtPbdw&h=AT2MwqHbzV9U9r_k__RwoSz691rkAv7m2N18cL0dESyjTBkNlYbYhyncdmTIwLkXYS54Om-Rw9JMh8qMjihDZ-mu-yBO4U5oA3AfHDQEG18iSVMyazY8F5gUoxiynPYUFUDB
**Translation:** China's military drones are unbeatable, the US can't match them…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — PRC military boast vs Taiwanese user → CT (PRC 'stronger').

---

### id 33216
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 雖然我很討厭中國 但說真的台灣的空拍機法規爛的可以 根本圖利法人  一堆超智障限制就算了 罰款甚至比酒駕還高
**Reply:** 沒關係我們有民主
**Translation:** Never mind, we have democracy.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Sarcasm at Taiwan's government → CT.

---

### id 33222
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 大疆成功的是他的軟體實力，飛控，圖傳，避障，精準定位。都在無人機領域數一數二。而且可以針對不同產業修改的靈活性，從民用到工業用農用甚至最近飛聖母峰大本營的。都是在軟體上的領先，不是單純硬體好壞。這點才是台灣目前欠缺的軟體要燒錢而且是很難量化成果。產品要有足夠多的數據去分析，足夠多的軟體人才去寫去做。這幾年在一些熱門產業看到中國企業都是類似狀況，我們在講台灣硬體如何強，結果人家用低一階的硬體做出更好…
**Reply:** @usieho5184 剛開戰時有買中國大疆，後來發現無人機頻頻被俄羅斯鎖死掉下來，所以烏龍蘭決定自己生產，當然很多外國都介入幫助。
**Translation:** Ukraine bought DJI, Russia jammed them, so Ukraine built its own with foreign help.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Factual account → false.

---

### id 33286
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 3:43 台湾不是国家，不要偷换概念。
**Reply:** 台灣是啊
**Translation:** Taiwan IS (a country).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Sovereignty claim vs PRC user → ST.

---

### id 33288
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** DJI为啥在深圳想过没有，那是一整条上下游产业链。就台湾的那点工业基础，产业链不完整，财政收入一省都比不过深圳一市，还要拿钱买老美武器。更何况大陆制电磁权老美出手都搞不掂，用无人机暴露飞手位置，接着火炮就给你扬了。还是别想太多了，打打选战，小确信就好，每天晚上早点睡，梦里啥都有。。。
**Reply:** 佩服佩服
**Translation:** Very impressive, very impressive.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | **0** | 0 |
| Opus | 0 | 0 | **1** | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Reply to PRC mockery; sarcasm direction unclear → false.

---

### id 33302
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread:** 不怕偷偷告訴你們，解放軍看不上大疆的無人機，覺得它們太落後了。
**Translation:** Secretly: the PLA thinks DJI drones are too backward.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — PRC military boast → CT (same as 33210).

---

### id 33303
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 不怕偷偷告訴你們，解放軍看不上大疆的無人機，覺得它們太落後了。
**Reply:** 嗯，入侵者應該有更多選擇
**Translation:** Sure, an invader should have more options.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — Calls PLA invaders → ST.

---

### id 33321
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread:** 台灣是這個星球上科技最發達的國家，只要想無人機隨時可以造出世界最先進的
**Translation:** Taiwan is the most advanced tech nation on the planet; it can build the best drones any time.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Sarcasm mocking Taiwan → CT.

---

### id 33322
**Video:** `6XwV-p6wmRw` (稱霸天空的無人機，竟有七成來自中國)
**Thread (context):** 台灣是這個星球上科技最發達的國家，只要想無人機隨時可以造出世界最先進的
**Reply:** 還不是
**Translation:** Isn't it?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Too terse, direction unclear → false.

---

### id 33323
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 你们啊总想搞个大新闻，然后把我批判一番。我和习主席谈笑风生，我们还准备谈点生意呢。🤓
**Reply:** @IdeoCon 到位。
**Translation:** Spot on.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — Explicit endorsement of the Trump-Xi satire → inherits DUS.

---

### id 33334
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 你们啊总想搞个大新闻，然后把我批判一番。我和习主席谈笑风生，我们还准备谈点生意呢。🤓
**Reply:** 圖樣，圖森破😂
**Translation:** Too young, too simple 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Opus (all false) — **Borderline** — Plays along with the meme, no stance → false.

---

### id 33349
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 你们啊总想搞个大新闻，然后把我批判一番。我和习主席谈笑风生，我们还准备谈点生意呢。🤓
**Reply:** 台灣是獨立國家
**Translation:** Taiwan is an independent country.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Sovereignty claim → ST.

---

### id 33351
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 你们啊总想搞个大新闻，然后把我批判一番。我和习主席谈笑风生，我们还准备谈点生意呢。🤓
**Reply:** To young to simple😂
**Translation:** To young to simple 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Opus (all false) — **Borderline** — Plays along with the meme → false.

---

### id 33365
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 生意人就是生意人，說話特別好聽，做又是另一個風格
**Reply:** ​@llooo5666怎樣？ 難得美國跟中國同調 要不要抱美國大腿啊
**Translation:** For once the US agrees with China — still want to hug America's thigh?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — Mocks Taiwan relying on the US → CT+DUS.

---

### id 33367
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 生意人就是生意人，說話特別好聽，做又是另一個風格
**Reply:** Exactly
**Translation:** Exactly.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — Endorses 'businessman talks nice, acts otherwise' (Trump) → inherits DUS.

---

### id 33388
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 但是中共從來都沒有說要武統台灣 都是美國和台灣自己在害怕
**Reply:** @飞鸟-ini那也得是你共匪歸順於我中華民國啊😂
**Translation:** Then your 共匪 must first submit to our Republic of China 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Retort to PRC user → ST.

---

### id 33431
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 川普：天要下雨，娘要嫁人，台湾怎么办？只有天知道😂
**Reply:** @andys9423 你怎麼可以如此天真
**Translation:** How can you be so naive?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Opus (all false) — **Borderline** — Target unclear → false.

---

### id 33439
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 川普：天要下雨，娘要嫁人，台湾怎么办？只有天知道😂
**Reply:** @mfs6682  我跟習近平很好，所以關稅我只提高20%而已，非常好👍
**Translation:** 'I'm great with Xi, so tariffs only up 20%, very good 👍'

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Mocks Trump's China dealing → DUS.

---

### id 33459
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 台灣是用來賣的，店主永遠不會告訴你他的成本和最低價是多少
**Reply:** @jasonchang705很多鳥不知道，甚至已經當美國人了
**Translation:** Many birds don't know; some are already Americans.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Agrees Taiwan is for sale, elites escape → CT.

---

### id 33460
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 台灣是用來賣的，店主永遠不會告訴你他的成本和最低價是多少
**Reply:** @阿春不乖你不懂 这叫倒賣 倒賣才大賺！😂
**Translation:** You don't get it — it's resale, resale makes big money 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | **0** | 0 |
| Opus | 0 | 0 | **1** | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — Taiwan sold by/through the US → CT+DUS.

---

### id 33483
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 台灣是用來賣的，店主永遠不會告訴你他的成本和最低價是多少
**Reply:** ​@jims1529你太瞧得起台灣了！賴清德們除了被白嫖，還倒貼；目的是轉移資產去美力奸，繼續以中華民國的國號，做美力奸的走狗，這群台獨隨時可以丟掉這國號，同時也可以佔盡中華民國的便宜。
**Translation:** Lai's people get used for free and pay extra, to be America's running dog.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — Mocks DPP + US uses Taiwan → CT+DUS.

---

### id 33489
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 台灣是用來賣的，店主永遠不會告訴你他的成本和最低價是多少
**Reply:** 正確
**Translation:** Correct.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | **1** | 0 |
| Opus | 0 | 0 | **0** | 0 | **0** | 0 |

**Your call:** Sonnet (CT+DUS) — **Borderline** — Endorses 'Taiwan is for sale' → inherits CT+DUS.

---

### id 33492
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 台灣是用來賣的，店主永遠不會告訴你他的成本和最低價是多少
**Reply:** ​@idnexdesign烏克蘭這種真正的主權國家都能被賣掉🌝
**Translation:** Even Ukraine, a real sovereign state, can be sold 🌝

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — Taiwan can be sold like Ukraine → CT+DUS.

---

### id 33537
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 永遠別期待美國保衛台灣，是憑什麼？
**Reply:** 青鳥的信仰很可怕
**Translation:** The blue-birds' faith is scary.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks DPP supporters (青鳥) → CT.

---

### id 33539
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 永遠別期待美國保衛台灣，是憑什麼？
**Reply:** 所以是要正名的時機了​@niniangjibagun9225
**Translation:** So it's time for name rectification.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Pro-independence → ST.

---

### id 33558
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread (context):** 台積電技術搬到大陸，他嘴就秋不起來了
**Reply:** 🇨🇳沒🇹🇼積電？@石榴宮分
**Translation:** 🇨🇳 without 🇹🇼SMC?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — Retort to PRC user → ST.

---

### id 33566
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 已從台灣拿走~~世界各國垂涎「護國神山」了~~~ 台灣.......................還有什麽~~能掠奪的？？...................“民進黨真誠掏心掏肺的友情”................................
**Translation:** The 'sacred mountain' already taken from Taiwan… what's left to plunder? 'The DPP's sincere friendship'.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — US plunders Taiwan + mocks DPP → CT+DUS.

---

### id 33577
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 中美建交的氛圍又要上演了。 中美貿易戰又如何？？  當初可是韓戰背景下的合作，相比之下現在的阻力小太多了，只要磨合到雙方利益達成共識，這都是自然會發展過程。  一切都是利益，沒有那麼多的仇恨值，還好台商夠爭氣，多年深耕的海外產業佈局，應該經的起這種變局。  川的選前承諾就是美國利益第一，這是他對他的國民承諾，能不能使美國再偉大，解決不斷攀升的美國國債，還是全世界期待美國總統是會違反選前承諾的這類人？？  客觀有時候很殘忍，總有人會不能接受，這都是人之常情。
**Translation:** US-China ties again; all about interests; Trump puts America first.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Lowered expectations of US → DUS.

---

### id 33581
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 你永遠都不知道這貨下一步怎麼走？
**Translation:** You never know what this guy will do next.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Trump unreliable → DUS.

---

### id 33585
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 在商言商，傻子都選中國
**Translation:** In business terms, only a fool wouldn't pick China.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — **Borderline** — Transactional US will drop Taiwan → CT+DUS (calibration rule).

---

### id 33586
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 完啦下一個台灣
**Translation:** It's over, next is Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **1** | 0 |
| Opus | 0 | 0 | 1 | 0 | **0** | 0 |

**Your call:** Sonnet (CT+DUS) — **Borderline** — Taiwan next to be abandoned, under Trump-China video → CT+DUS.

---

### id 33590
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 為什麼聽起來像是「中國只要給美國錢，打不打台灣我就不這麼在意了。」
**Translation:** Sounds like: 'China pays the US, and I don't care if Taiwan gets hit.'

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — CT+DUS.

---

### id 33595
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 呢個魏哲家真係冇撚用😡 斷送咗台灣嘅一張好牌
**Translation:** (Cantonese) C.C. Wei is useless — threw away Taiwan's good card.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Taiwan lost its leverage → CT.

---

### id 33597
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 他上次訪中爭取中國投資，說自己跟中國關係很好。結果回到美國不到一星期就開始對中國關稅制裁。  他說自己跟誰很好，那個人大概就要很小心了。
**Translation:** Whoever he says he's close to had better be careful.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Trump unreliable → DUS.

---

### id 33599
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 幫大家總結一下：中國人不用進來，中國錢進來就好的意思
**Translation:** Summary: Chinese people stay out, Chinese money welcome.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Mocks Trump's transactional line → DUS.

---

### id 33602
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 關於台灣國土安全問題什麼都不敢保證，連口頭都不願意承諾  但是逼迫台積電赴美投資設新廠的1000億美金，1塊錢都不能少😂
**Translation:** No guarantee on Taiwan's security, not even verbal, but not $1 less of TSMC's $100bn 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 1 | 0 |
| Opus | 0 | 0 | **1** | 0 | 1 | 0 |

**Your call:** Opus (CT+DUS) — CT+DUS.

---

### id 33618
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 遇強則弱，美中俄聯盟
**Translation:** Weak before the strong; US-China-Russia alliance.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Distrust of US → DUS.

---

### id 33620
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 搭配昨天的台積電擴大美國設廠一起服用，有沒有滿滿的烏克蘭即視感？
**Translation:** With TSMC's US expansion yesterday — full Ukraine déjà vu?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — CT+DUS.

---

### id 33635
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 一邊是有牌的土匪 一邊是沒牌的土匪 台灣只能靠自己壯大  有實力了才不怕看別人臉色
**Translation:** One bandit with a licence, one without; Taiwan can only rely on itself and grow strong.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 1 | **0** | 0 |
| Opus | 0 | 0 | 0 | 1 | **1** | 0 |

**Your call:** Opus (ST+DUS) — Self-reliance → ST; US = bandit → DUS.

---

### id 33639
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 川普是生意人，就是不提台灣
**Translation:** Trump is a businessman; he just won't mention Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — DUS.

---

### id 33640
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 我還很期待他把台灣賣了。 他會完完全全失去亞太地區的掌權 等到台灣回歸最難受會是南韓跟日本。菲律賓什麼卡小哈哈
**Translation:** I look forward to him selling Taiwan… after Taiwan returns, South Korea and Japan suffer.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — Wants unification + US sells Taiwan → CT+DUS.

---

### id 33654
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 商人本色😂
**Translation:** True businessman 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Mocks Trump's transactional stance → DUS.

---

### id 33656
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 商人當了總統，三句不離生意話題
**Translation:** A businessman as president, can't stop talking business.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — DUS (same as 33654).

---

### id 33675
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 就商人的角度來說，他的想法是非常正確的。意識型態是最廉價的政治商品。
**Translation:** As a businessman he's right. Ideology is the cheapest political commodity.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — US won't back Taiwan on ideology → lowered expectations → DUS.

---

### id 33680
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 哇草上任後完全變一個人
**Translation:** Wow, he became a totally different person after taking office.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Trump changed → DUS.

---

### id 33687
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** 沒事 呆丸有愛呆丸a狼
**Translation:** Don't worry, Taiwan has people who love Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Resolve → ST.

---

### id 33738
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** Sooner or later ,  America will buy over Taiwan or Taiwan will sold to America like Greenland, Canada ....
**Translation:** Sooner or later America will buy Taiwan, like Greenland, Canada…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | **0** | 0 |
| Opus | 0 | 0 | **1** | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — CT+DUS.

---

### id 33767
**Video:** `6muxQj8Q4EE` (特朗普稱會與中國合作 拒答台灣問題－BBC)
**Thread:** This planet earth just like belong to your father's property ..
**Translation:** The planet is like your father's property.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Aimed at Trump → DUS.

---

### id 33781
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 确实看不到和平解决的希望，并且越来越危险😢
**Reply:** ​@吳明聰-l1d你要不看看憲法台灣屬不屬於中國
**Translation:** Read the constitution — does Taiwan belong to China?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — PRC-side legal claim → CT.

---

### id 33783
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 确实看不到和平解决的希望，并且越来越危险😢
**Reply:** @吳明聰-l1d 不是中國？自己看看開羅宣言，蔣介石是不是和羅斯福、丘吉爾坐在一起。你這種話放戒嚴時期早槍斃了
**Translation:** Read the Cairo Declaration… under martial law you'd have been shot.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — CT.

---

### id 33784
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 确实看不到和平解决的希望，并且越来越危险😢
**Reply:** @吳明聰-l1d 是盟軍打敗了日本，英美中蘇共同接受日本投降。不是中國打敗了日本？難道是你這種台籍日本兵的野種？
**Translation:** …Or are you the bastard of a Taiwanese Japanese soldier?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — PRC-side history + insult → CT.

---

### id 33786
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 确实看不到和平解决的希望，并且越来越危险😢
**Reply:** @喔-k6b 我承認啊，臺灣是中華民國，對岸是中華人民共和國，都是中國一中兩表，目前中國還在內戰階段，兩方的行政範圍都包括了台灣和大陸。
**Translation:** ROC and PRC are both China; the civil war goes on; both cover Taiwan and the mainland.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — One-China framing → CT.

---

### id 33789
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 确实看不到和平解决的希望，并且越来越危险😢
**Reply:** @喔-k6b 目前的情況就是兩個中國啊，而且現實是國際上說到中國通常都指中華人民共和國而不是中華民國，只希望早點修憲吧，把中華民國的行政範圍去掉大陸那一部分，再改國號為臺灣，這樣我們在外面就可以名正言順的說臺灣國臺灣人了，是憲法賦予我們的權利，也不會被對面中國人抓把柄說行政範圍包含大陸所以是中國內戰這種話。
**Translation:** Amend the constitution, drop the mainland, rename the country Taiwan.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — ST.

---

### id 33790
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 确实看不到和平解决的希望，并且越来越危险😢
**Reply:** @喔-k6b 根源就在於我們的憲法，我們憲法不改，那目前就是兩個中國，臺灣就是中國的一個省
**Translation:** The root is our constitution; unless it changes, Taiwan is a Chinese province.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Same author as 33789, arguing for change → false.

---

### id 33795
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** "激進派小朋友"?     台灣是有誰激進了?       台灣有哪個檯面上的頭頭在講台獨了? 民進黨蔡英文早就進階更新到台灣本就是主權獨立的國家， 哪需再獨立了， 你們還在踽踽獨行，擁抱台獨的幽靈? 台灣維持現狀的火車頭早嘟嘟開走了，狗兒拼命狂吠，是吠什麼勁呢?     但是  難道台灣沒有台獨，中國就不統一嗎?     台灣承認九二共識，中國就不統一嗎?     放下武器，非軍事化，或主張…
**Reply:** 唉唉唉，幻想症這麼嚴重還要出來丢人現眼，真是可憐的孩子！
**Translation:** Such bad delusions, and you still come out to embarrass yourself.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — Plain insult → false (batch 10 rule).

---

### id 33798
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** "激進派小朋友"?     台灣是有誰激進了?       台灣有哪個檯面上的頭頭在講台獨了? 民進黨蔡英文早就進階更新到台灣本就是主權獨立的國家， 哪需再獨立了， 你們還在踽踽獨行，擁抱台獨的幽靈? 台灣維持現狀的火車頭早嘟嘟開走了，狗兒拼命狂吠，是吠什麼勁呢?     但是  難道台灣沒有台獨，中國就不統一嗎?     台灣承認九二共識，中國就不統一嗎?     放下武器，非軍事化，或主張…
**Reply:** @qqqqqqqq1111 說一堆「誰被屏蔽」說謊不打草稿，是吧？！要不要讓全世界看看台獨是什麼嘴臉？！
**Translation:** Lying without a draft! Let the world see the face of Taiwan independence!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — Attacks Taiwan independence → CT.

---

### id 33805
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 台湾的极端从火烧车事件开始我就开始极度反感
**Reply:** @死扛着 你們可能誤會!死者為大!身為總統他的發言都很慎重!時間太久我不清楚!而且中國搞一言堂及言論審查!有時常搞認知作戰!要得到真實新聞還是要翻牆看!
**Translation:** China has one voice, censorship, cognitive warfare; you need a VPN for real news.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Anti-CCP framing → ST.

---

### id 33825
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 感觉没意义，解放军各种口径的枪支都有，我离开之前是7.62，不是电视上拍的那样一个小洞，而是飞出时后面一个大洞。如果开战台湾最后只剩巷战。战局开始，封锁所有进入台湾的海上通道，台湾只出不进。守滩的8个旅就是解放军火箭弹➕炮弹的活靶子实施地毯式攻击（放心一下子就结束了，人没有痛苦的），精确制导飞弹打击军事，防空，网络，电力，及斩首行动。直至完全取得制海，制空权。以上设施完全瘫痪后，解放军才会安全登陆…
**Reply:** @吳明聰-l1d 飛單有機會其起飛幾個？
**Translation:** How many planes would even get to take off?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Doubts Taiwan's defence → CT.

---

### id 33827
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 感觉没意义，解放军各种口径的枪支都有，我离开之前是7.62，不是电视上拍的那样一个小洞，而是飞出时后面一个大洞。如果开战台湾最后只剩巷战。战局开始，封锁所有进入台湾的海上通道，台湾只出不进。守滩的8个旅就是解放军火箭弹➕炮弹的活靶子实施地毯式攻击（放心一下子就结束了，人没有痛苦的），精确制导飞弹打击军事，防空，网络，电力，及斩首行动。直至完全取得制海，制空权。以上设施完全瘫痪后，解放军才会安全登陆…
**Reply:** @吳明聰-l1d 哈哈哈，不贏的話，政府就垮台了，所以，你認為會不會贏？
**Translation:** Haha, if it doesn't win the government falls; so do you think it will win?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Which side is meant is unclear → false.

---

### id 33829
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 感觉没意义，解放军各种口径的枪支都有，我离开之前是7.62，不是电视上拍的那样一个小洞，而是飞出时后面一个大洞。如果开战台湾最后只剩巷战。战局开始，封锁所有进入台湾的海上通道，台湾只出不进。守滩的8个旅就是解放军火箭弹➕炮弹的活靶子实施地毯式攻击（放心一下子就结束了，人没有痛苦的），精确制导飞弹打击军事，防空，网络，电力，及斩首行动。直至完全取得制海，制空权。以上设施完全瘫痪后，解放军才会安全登陆…
**Reply:** @yh3wahaha275  東北從來就不屬於日本扯進來是無知!舊金山和約去看看吧?房子是你的也要有權狀吧!1895年台灣就割讓給日本!所有的領土轉讓都要有條約簽屬!那拿出哪一條條約有寫台灣屬於中國的!智障!
**Translation:** Show me the treaty that gives Taiwan to China! Idiot!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — ST.

---

### id 33846
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 我没去过台湾, 但是我很好奇, 台湾内部真的很多激进派么? 这群激进派是只存在互联网上呢还是真的现实中这样呢, 在互联网我看着台湾都快全民激进了, 搞得好像台湾要主动跟大陆开战一样, 你们不知道大陆这边也很多激进派并且人数很多么? 真打起来最差的结果就是会有几万甚至几十万人死在战场上,  来个理性的台湾人说一下
**Reply:** @Antinonsens我在國外除了中國武漢肺炎之外可沒人在乎你們是老幾，反而大家都知道台灣是獨立國家，你說氣不氣人？
**Translation:** Abroad nobody cares about you except the Wuhan virus; everyone knows Taiwan is independent.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — ST.

---

### id 33914
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 民主和專製都是管理方法,都是中性的,各有利弊,只有運用到適當場合才最有效!要兩者結合最好！ 票選最大的前提是投票人要素質高,懂行,專業知識高!所以要精英投票選最好!所以,絕對民主,普選就會讓非專業的人壓製專業人的意見,猶如粉絲追星般非理性! 絕對專製也不行,畢竟個人知識範圍有限,要精英組成專家智庫,參考廣大群體的意見訴求,綜合決定發展方向和策略才最好！ 這麽復雜的事情,能是一群非專業的人投票能做好…
**Reply:** @国艾-v7e老百姓知道手机不好，很小的代價就可以換了，可是決定前途命運的決策怎麼能隨便試驗呢？那樣換的代價大不大呢？要知道，政治人物的决策需要监督，民意做的决策也需要监督。  大多數烏克蘭老百姓並沒有遠見，知道泽连斯基當選後一邊倒親美，不保持中立，会引起战争，导致國破家亡，民眾流離失所，不過現在的情況，把澤連斯基換了就能解決了？  政治人物做決策要參考民意，但做決定國家民族老百姓前途命運的重大決策時要有遠見，不能只看民意。可惜，就一人一票決定政治人物決策的數人頭辦法，很難做出有遠見的決策。 如果中國大陸在決策台海問題時，按照台灣的做法，按照一人一票數人頭的做法決策，恐怕台灣早就成戰場了，但目前這樣做並不符合國家的長遠利益，你怎麼看？
**Translation:** Ukrainians lacked foresight; Zelensky went pro-US, not neutral, causing war… if China decided like Taiwan, Taiwan would be a battlefield.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **1** | 0 | 0 | **0** |
| Opus | 1 | 0 | **0** | 0 | 0 | **1** |

**Your call:** Sonnet (CU+CT) — **Borderline** — Blames Zelensky → CU; PRC restraint praised → CT. No NATO cause claim → no BNE.

---

### id 33917
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 蘋果公司一人一票管理能有今天的成績嗎？一人一票不就是數人頭嗎？人多就是對的，人多一定是對的嗎？ 不是你模仿美国的制度就可以成功的，美国的成功并不可复制。 第一，美國當世界老大時並不是全民普選，1920年美國婦女獲得投票權，直到1970年後美國黑人獲得投票權！在這之前，美國早就是世界老大了！ 第二，美國是世界老大也不全憑奮鬥，而是吃了一戰二戰紅利，美國不是一戰二戰戰場，全世界人才為了躲避戰火，紛紛跑…
**Reply:** 選舉的關鍵有兩個，一個是錢，一個是媒體，民意在這兩個法寶的加持下，就像陶泥，想做什麼形狀就什麼形狀。大家想想看，如果中國真的像綠霉和輪媒說的那樣不堪，大陸十幾億人怎麼還會維護自己的政府，早就幹起來了，十幾億人那麼好管嗎？你們想想看，讀國中的時候一個班都不好管吧？可是大多數台灣人為什麼都相信大陸是個恐怖黑暗落後愚昧毫無人權的地方呢？原因很簡單因為媒體每天灌輸。1990年代到2000年代初，是大陸和台灣以及西方關係最好的年代，那時的中國更腐敗更不開放人民更貧窮，認知更落後，可那時卻是西方和台灣中國態度最好的十幾年。可見，沒有什麼是非，也沒有什麼意識形態，終究就是利益下的選擇。現在的利益之爭需要對中國不友好，需要人民仇視中國，於是資本掌控之下的政客和媒體就高速高效地運轉了，短短數年時間就把友好扭轉為防備接著成為敵視。人民要記住，只要我們都堅定不要戰爭，就沒有人能利用我們去打仗，因為政客們是不會上戰場的，他們的子女也不會。
**Translation:** …綠霉 and 輪媒 brainwash you about China…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks Taiwanese media, pro-PRC → CT.

---

### id 33935
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 战争只是最后不得已的手段，希望台湾网友也要晓得不要把大陆逼到不得已，放心，只要大家还能对话，还不至于热血上涌，铁了心要台独，宁可打仗也要台独，战争也不会发生，不要做激进派，不管是左还是右，大家要明白现实世界不是非黑即白，而是一道灰色，只要大家还能有谈话的空间即使大陆和台湾的民间交流现在很少，大陆的声音传不到台湾，台湾的一般也传不到大陆内地普通人身上，传到了就糟了，如果大家像网上一样的激进言论，被太…
**Reply:** @zplhb7631 你說傷亡十倍領土面積減少數百平方公里但是結果勝利的那場戰爭嗎？
**Translation:** You mean the war with 10x casualties and lost land that you call a win?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Mocks PRC military record → ST.

---

### id 33956
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 老共真的很仁慈，很忍耐了。如果不是因为把台湾人当同胞，早就没必要考虑和统了。
**Reply:** @PanchoZ-rl9kp 現在沒台獨也是因為攻擊性武器還沒到位，等到時機一到自然水到渠成
**Translation:** No independence now only because offensive weapons aren't ready; when they are, it will happen.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | **0** | 0 | 0 |
| Opus | 0 | 0 | **0** | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Pro-independence resolve → ST.

---

### id 33963
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 老共真的很仁慈，很忍耐了。如果不是因为把台湾人当同胞，早就没必要考虑和统了。
**Reply:** 對一個不屬於他的領土人民講話如此!是不是太離譜!太流氓!
**Translation:** Talking like this to people who don't belong to him — too thuggish!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — ST.

---

### id 33967
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 老共真的很仁慈，很忍耐了。如果不是因为把台湾人当同胞，早就没必要考虑和统了。
**Reply:** @覃西门-c4o 那台灣屬於中國的法理依據是甚麼!你可能不知道宣言或公告的意思及他們的效力!
**Translation:** What is the legal basis for Taiwan belonging to China?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — ST.

---

### id 33976
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 老共真的很仁慈，很忍耐了。如果不是因为把台湾人当同胞，早就没必要考虑和统了。
**Reply:** @吳明聰-l1d 小常識: 中華民國的英文全名就是Republic of CHINA，台灣屬於中國的法理依據是中華民國憲法，中華民國自稱中國合法政府，大陸與台澎金馬地區皆為中華民國疆域，你去圖書館翻翻中華民國憲法就知道。二戰代表中國接受日本投降的正是中華民國政府，不是中共。如果你認為中共是中國偽政權的話就去找美國爸爸理論，因為是美國主動拋棄中華民國斷了交，跑去跟中華人民共和國建交的。在國際社會承認中華民國合法性越來越少的處境下，蔡政府執政八年又斷了九個承認中華民國的國家，導致全世界195個國家只剩13個芝麻小國承認我們。台灣一群假日本人在沒有任何法理依據下就很阿Q的以台灣國已獨立自詡，卻只敢在國慶日的英譯文或護照的封面文字大小上自嗨而已。讀了閹割版的台獨史觀的後遺症就是認賊作父，邏輯顛倒。你若讀了台獨版本外的歷史紀錄(P.S.世界各地包括歐美的歷史紀錄，日本右翼不算，因為不甘心輸了二戰得把台灣吐回去)，並親身經歷媒體隱瞞你的真相，你的世界觀會先崩解，然後反彈成超級紅，這是我觀察許多發現受騙了的深綠支持者的典型反應。
**Translation:** ROC = China; the US abandoned the ROC; Tsai lost 9 allies; fake Japanese…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT+DUS) — CT; 'the US abandoned the ROC' → DUS.

---

### id 33978
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 老共真的很仁慈，很忍耐了。如果不是因为把台湾人当同胞，早就没必要考虑和统了。
**Reply:** @sophialiu333 中華民國憲法沒有台灣兩個字!
**Translation:** The ROC constitution doesn't even contain the word Taiwan!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Other (ST) — **Borderline** — Same author/side as 33967 → ST.

---

### id 33994
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 老共真的很仁慈，很忍耐了。如果不是因为把台湾人当同胞，早就没必要考虑和统了。
**Reply:** @bennyzheng5440 胡搞瞎搞沒有不崩的!只是拖到現在才崩!經濟火車頭都熄火了!地方政府欠債數十兆人民幣!還能繼續搞下去嗎?你們連利息都付不起!
**Translation:** Chaos always collapses; the economy has stalled; local debt in the trillions…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — PRC decline → ST (like 'Russia's weakness' → SU).

---

### id 34010
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 感觉台湾青年人完全不知道大陆现在的实力，大陆现在无论经济还是军事上，都已经成为一个和美国相当的角色，特别在大陆周边的战争大陆占据相当的优势，美国不是要不要干预的问题是打不打得过的问题，而且台湾这1-2代人历史观完全断层，很多人完全不知道自己的祖先从哪里来，觉得自己说的台语是台湾特色的语言，觉得只有国民党时期的外省人才是从大陆来的，自己把自己的历史阉割到了一百多年，那可不认日本做祖宗了，却又说着几千…
**Reply:** @willsung5965 世界銀行公布了2022年世界各國按購買力平價計算的全民生產總值(GDP)數據，讓我們一起來看看各大國的排名情況吧！  首先，讓我們來看看排名前五的國家。沒錯，你們猜對了，分別是中國、美國、印度、日本和俄羅斯。其中，中國的GDP達到了驚人的30.3萬億美元，自2017年以來連續六年霸占全球第一！  緊隨其後的是美國，達到了25.5萬億美元，位列全球第二。雖然略遜於中國，但美國依然是全球最強大的經濟體之一。而印度以11.8萬億美元的GDP排名第三，日本則以5.7萬億美元的GDP位列第四。
**Translation:** World Bank: China #1 GDP by PPP…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — PRC strength vs Taiwanese user → CT (same as 33210).

---

### id 34019
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 感觉台湾青年人完全不知道大陆现在的实力，大陆现在无论经济还是军事上，都已经成为一个和美国相当的角色，特别在大陆周边的战争大陆占据相当的优势，美国不是要不要干预的问题是打不打得过的问题，而且台湾这1-2代人历史观完全断层，很多人完全不知道自己的祖先从哪里来，觉得自己说的台语是台湾特色的语言，觉得只有国民党时期的外省人才是从大陆来的，自己把自己的历史阉割到了一百多年，那可不认日本做祖宗了，却又说着几千…
**Reply:** @willsung5965 不讀歷史或只讀掐頭去尾的斷裂史，結果就是台灣年輕一代的認日賊作父，或是像加拿大那樣為了反俄羅斯，鬧出把父祖輩拋頭顱灑熱血抗戰過的納粹蓋世太保請到國會當成二戰英雄鼓掌的笑話；不讀歷史只看這個月的頭條會覺得哈瑪斯是流氓，讀了歷史會發現以色列才是真流氓。
**Translation:** Young Taiwanese take the Japanese thief as father…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — CT.

---

### id 34063
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 我們台灣百姓不想死，要死自己去
**Translation:** We Taiwanese don't want to die; go die yourself.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Anti-resistance → CT.

---

### id 34079
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 兩岸是要統的， 中國是要『人民共和』的。  不是『朝鮮民主人民共和國的謊言』可以騙取大陸中國人權力。讓給共產黨 二代世襲永遠當官的。  你到是立刻打阿 。 當年中華民國共產党，不是真正的中華民國政府。 奪取騙走大陸中國人的權利的。
**Translation:** …the CCP's hereditary officials… go on, attack right now.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — Anti-CCP + dare → ST.

---

### id 34080
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 看看馬克斯主義的北韓國，朝鮮！跟大韓民國。 雖然兩個國土 一樣大。但是馬列主義的北韓國的農民工收入。遠比大韓民國少了六倍的收入。餓死人的北韓國還制下國安法！脫北者要以 顛覆國家罪行。來槍閉韓國人。恐惡韓國人。這是犯罪的。但是北韓國 還是制定 法律。來恐惡人民，槍閉人民。 雖然大韓民國的人口，是北韓國的2倍。但是大韓民國人卻，人人醫保，老了政府養。但北韓國卻據然還要跟子女拿生活費，農村還無醫保。
**Translation:** North Korea vs South Korea: Marxism means hunger and guns.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Anti-communist case → ST (harm-of-unification rule).

---

### id 34094
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 不怕 不會打啦
**Translation:** Not scared, they won't attack.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Resolve → ST (same as 32928).

---

### id 34100
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread (context):** 台湾真的要和世界第一工业国打吗。。。。还是一党领导的，如果我是台湾人我是会想办法撤了
**Reply:** 有人就堅持阿！！還不只一個，是一堆！！
**Translation:** Some people do insist! Not one, a whole lot!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — Resolve to fight → ST.

---

### id 34124
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 雖然恐嚇臺胞也許有正面效果，，，但臺灣不可能是下一個加沙，因為大陸不是以色列。
**Translation:** Taiwan can't be the next Gaza, because the mainland isn't Israel.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — PRC benevolent → CT.

---

### id 34128
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 台灣總是喜歡對號入座，一會兒是烏克蘭，一會兒又是加沙，無語了
**Translation:** Taiwan always casts itself — Ukraine one day, Gaza the next. Speechless.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks Taiwan → CT.

---

### id 34171
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 以色列可沒把巴勒斯坦當同胞?更不可能有惠台政策?
**Translation:** Israel doesn't see Palestinians as compatriots — no pro-Taiwan perks either?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — PRC benevolent → CT.

---

### id 34172
**Video:** `76aHxNIZpVQ` ((新竹暴怒哥)台灣，會不會是下一個加薩？)
**Thread:** 美國以色列給全世界反面教材性質，完全不可不需要聯合國解決領土問題?美國可以不守國際法?其他國家也可以懂不?
**Translation:** The US and Israel teach the world: no need for UN on land; others can ignore law too.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 1 | 0 |
| Opus | 0 | 0 | **0** | 0 | 1 | 0 |

**Your call:** Sonnet (CT+DUS) — **Borderline** — DUS; implies PRC may take Taiwan → CT.

---

### id 34211
**Video:** `7YAtsSfYMT4` (【台灣演義】解密 國光計畫)
**Thread (context):** 🎈反攻大陸是中國國民黨的心願，因為台灣不是他們的家，他們的家在中國，台灣只是他們暫時的【庇護所】，猶如【汽車旅館】！ 但是大陸不是台灣的人家，台灣人的家在台灣。 所以中國國民黨把【國共內戰】帶來台灣，殃及台灣人，台灣人本來就沒有反攻大陸，更不需要跟著中國國民黨去打所謂的【中國內戰】！ 台灣是被【拖下水】的！  蔣介石當年想藉由美國幫忙去反攻大陸，但是美國不會介入【中國內戰】，美國打日本是基於【國】…
**Reply:** 你們大多都是從中國大陸退到台灣的人的後代. 是百萬千萬國軍用血肉來讓你們的祖輩父母能在台灣落地生下你們. 你們不像你們祖輩一樣要力圖復國.推翻中共.解救大陸同胞. 我總覺得國軍的先烈們. 死不瞑目. 我也討厭戰爭. 但請你們這群正統的中國人記住. 光復大陸國土.是你們中華民國人世世代代都不能忘記和害怕的使命.
**Translation:** Recovering the mainland, overthrowing the CCP, is your eternal mission.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Anti-CCP → ST.

---

### id 34216
**Video:** `7YAtsSfYMT4` (【台灣演義】解密 國光計畫)
**Thread (context):** 🎈這集節目看完，真的覺得蔣介石當年真的【很天真】，只是因為他有一個不得不完成的【個人夢想】!
**Reply:** @Francis9917  歸還( 偽 )中華民國 和 屬 浙江奉化 存放臺灣( 兩具蔣氏父子殭屍 )臺灣國家正常化了。珍珠港 塞班島都已成美國 日本相互立紀念碑人民相互觀光景點。勿忘國恥 918、77 事件：那是 9 百 60 萬平方公里關著 十四億人 嚴重患( 被害 加害 )精神病！從早莫名 恨？它國 最後睡覺 恨？臺灣奇特國家。
**Translation:** (Garbled) return the ROC and the Chiang corpses; Taiwan normal country; 1.4bn mentally ill.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — ST.

---

### id 34217
**Video:** `7YAtsSfYMT4` (【台灣演義】解密 國光計畫)
**Thread (context):** 🎈這集節目看完，真的覺得蔣介石當年真的【很天真】，只是因為他有一個不得不完成的【個人夢想】!
**Reply:** 那現在天真的人變成習主席和普主席了嗎
**Translation:** So now the naive ones are Chairman Xi and Chairman Putin?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | **1** | 0 | 0 |
| Opus | 0 | **0** | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (SU+ST) — **Borderline** — Mocks Putin → SU; Xi → ST.

---

### id 34230
**Video:** `7YAtsSfYMT4` (【台灣演義】解密 國光計畫)
**Thread (context):** 唯一支持過老蔣反攻大陸的美國將領，就是美國麥克阿瑟將軍，韓戰老毛調動解放軍入朝當志願軍，都是野戰軍的精銳部隊，打得美軍壓力很大。麥克阿瑟因此計畫由老蔣發動兩棲作戰，登陸中國東南沿海省分開起第二戰場，用來分擔韓戰前線的美軍壓力。  但是杜魯門總統和繼任的艾森豪總統都反對，因為除了會使韓戰擴大之外，等同於對整個中國宣戰，加上後面蘇聯的虎視眈眈。但是老蔣仍不死心，一直堅持著反攻大陸的夢想，期望有朝一日回…
**Reply:** 習近平領天命顛覆共產黨的證據 推背44圖🆚️A.D.2015／乙未年度預算卦組 鼎之益：坐朝垂軒，據德宰民，                虞叔受命，六合和親。 益之鼎：仁德孔明，患禍不傷，                期誓不至，室人銜恤。 蠱之益：牡犧孔博，日新其德，                文君出獵，姜氏受福。 益之蠱：去危脫厄，安無怵惕，                上福喜堂，見我歡悅。 🥸44圖 + “雙羽四足” = 2015習馬新加坡會 主題卦“未濟” + 馬英九揹弓 = 臺灣以武拒統 紅朝始末41象毛澤東🔜44象習近平，其它主席沒寫↔️邏輯性習近平該是末帝❓️廿大出臺證實🤭習皇無敵三世。
**Translation:** (Prophecy) Xi is the last emperor… Taiwan rejects unification by force.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — ST.

---

### id 34239
**Video:** `7YAtsSfYMT4` (【台灣演義】解密 國光計畫)
**Thread:** 反攻大陸.收復大陸河山.解救同胞. 這是中華民國永遠不能改變的事實.
**Translation:** Counterattack the mainland, free compatriots — the ROC's unchangeable mission.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Anti-CCP → ST (same as 34211).

---

### id 34246
**Video:** `7YAtsSfYMT4` (【台灣演義】解密 國光計畫)
**Thread:** 神經錯亂的節目用詞！！那個時代台灣就是中國的合法政府，何為反攻中國？扭曲意識形態毫無下限！！
**Translation:** Absurd wording! Then Taiwan WAS China's legal government — why 'counterattack China'?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — China-identity line vs Taiwan-centric framing → CT.

---

### id 34257
**Video:** `7saPqacGY1A` (【關鍵時刻】烏克蘭只接受普丁投降書)
**Thread:** 很多人知道普丁不可能投降，烏克蘭這樣的說法就是在說“若哪天打到你家，請見諒喔~”，另一個訊息是要俄羅斯內部自行處理，若俄羅斯內部不處理的話，至少我話說在前頭了......
**Translation:** Ukraine's line means 'sorry if we hit your home'; Russia must sort itself out.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Reads Ukraine's message favourably → SU.

---

### id 34264
**Video:** `86F4d56ok1w` (《行動代號2027》EP7)
**Thread (context):** 身為國軍有人在關心國防，真的很感動！
**Reply:** 為什麼不能對洗風向的人倒讚😅 謝謝斐姨把艱深的內容講得很清楚，比較能理解我們可能的因應之道
**Translation:** Why can't I downvote the narrative-pushers 😅 Thanks for explaining what we can do.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Defence interest → ST.

---

### id 34269
**Video:** `86F4d56ok1w` (《行動代號2027》EP7)
**Thread:** 有這樣的精闢解說真棒！烏克蘭現在是全世界最會打戰的民族！希望俄烏戰後能請烏克蘭軍方來指導整體作戰方式。
**Translation:** Ukraine is now the best-fighting nation; after the war invite them to teach us.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **0** | 0 | 0 |
| Opus | 0 | 1 | 0 | **1** | 0 | 0 |

**Your call:** Opus (SU+ST) — SU + ST.

---

### id 34272
**Video:** `86F4d56ok1w` (《行動代號2027》EP7)
**Thread:** 真希望范姨，可以回溯討論，為何當初烏俄戰爭，從三天、一星期，到一個月，到現在打超過一年都還沒結束，那當初的媒體論述，為何這樣行程非常大的誤差與誤導民眾。  如果烏俄戰爭，再打半年？一年？機率有多大？  自從誤差龐大到根本是胡扯程度後，現在已經沒人再評論俄羅斯多久戰線會崩潰。
**Translation:** Why were the media's 'three days, a week' predictions so wrong? No one predicts Russian collapse now.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Mocks Ukraine-winning narrative → CU.

---

### id 34279
**Video:** `86F4d56ok1w` (《行動代號2027》EP7)
**Thread:** 只講西方愛聽的一面,並不夠客觀 比如所謂的不對稱作戰,真相是烏軍用了8倍人命及整個打殘的鳥東換來, 2022烏克蘭GDP直接少40%,而且沒有天價經費及幾10年時間都無法恢復, 反觀俄羅斯,在美國以美元霸權崩解的代價下,被整個西方制裁的俄羅斯,2022只少2%, 再說認知作戰,製造假新聞只能讓人一時興奮,是無法打贏實力懸殊的戰爭, 在讓我們回到戰爭前,普丁脅迫烏克蘭的條件, 烏東2個郡自治,宣布放棄加入歐盟北約, 如今在烏克蘭付如此慘痛的代價下,烏東4個郡被佔領,歐盟或北約還是無法加入
**Translation:** 'Asymmetric war' cost Ukraine 8x lives, GDP −40%; still no NATO/EU…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **1** | 0 | 0 | **0** |
| Opus | 1 | 0 | **0** | 0 | 0 | **1** |

**Your call:** Sonnet (CU+CT) — CU; dismisses Taiwan's asymmetric/cognitive defence → CT. No NATO-cause claim.

---

### id 34280
**Video:** `86F4d56ok1w` (《行動代號2027》EP7)
**Thread:** 修理玻璃紗窗的三輪車在戰時應該是很讚的打帶跑載具
**Translation:** The glass-repair tricycle would be a great hit-and-run vehicle in wartime.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Defence idea → ST.

---

### id 34453
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread (context):** 俄國是中國政體的先行者 社會主義走向民主路線 但是步伐又不如烏克蘭 波羅的海三小國 是不是走回鐵幕時代 就看接下來會不會有大清洗
**Reply:** 中國共產黨政府若要有天翻地覆的大改變，只有一條路，那就是 歸順中華民國，別無他途。
**Translation:** The CCP's only way: submit to the Republic of China.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — ST.

---

### id 34454
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread (context):** 很奇怪！烏克蘭也是前蘇聯聯邦國，為何中文圈媒體炮轟俄羅斯不炮轟烏克蘭？不管誰發動戰爭，為什麼譴責俄羅斯是獨裁國家，而烏克蘭不是獨裁國家？
**Reply:** @yuyuu7054你未學到俄國出兵烏克蘭是俄國全票通過授權總统執行, 83% 的支持率可有民意基礎. 俄國因北約東擴斡旋了十幾年. 俄國被逼至牆角了.
**Translation:** Russia's parliament voted, 83% support; NATO expansion pushed Russia to the wall.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Opus (CU+BNE) — CU + BNE.

---

### id 34457
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread (context):** 恭賀普丁榮獲世界邪惡軸心魔魁獎~
**Reply:** 你接受一個團體，巧立名目，投票決定你的生死嗎?這種霸凌式的說詞根本就很無聊。懶得理你!
**Translation:** Would you accept a group voting on your life? Bullying talk.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Direction unclear → false.

---

### id 34463
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread (context):** 二戰後地表最大戰爭，那伊拉克戰爭呢？阿富汗戰爭呢？波灣戰爭發動了所有的歐美國家參與，算是在家玩家家酒嗎？
**Reply:** 說的對👍👍👍
**Translation:** Right 👍👍👍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — Endorses Iraq/Afghanistan whataboutism → inherits DUS.

---

### id 34464
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread (context):** 二戰後地表最大戰爭，那伊拉克戰爭呢？阿富汗戰爭呢？波灣戰爭發動了所有的歐美國家參與，算是在家玩家家酒嗎？
**Reply:** @lixiaxu4615 👍👍👍
**Translation:** 👍👍👍

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — Same → DUS.

---

### id 34465
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread (context):** 二戰後地表最大戰爭，那伊拉克戰爭呢？阿富汗戰爭呢？波灣戰爭發動了所有的歐美國家參與，算是在家玩家家酒嗎？
**Reply:** 說得好
**Translation:** Well said.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **1** | 0 |
| Opus | 0 | 0 | 0 | 0 | **0** | 0 |

**Your call:** Sonnet (DUS) — **Borderline** — Same → DUS.

---

### id 34476
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread:** 才不是! 打烏，完全是怕民主，威脅他Putin 獨裁威權! 中共also the same!
**Translation:** No! Putin attacked out of fear of democracy; the CCP is the same!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 1 | 0 | **0** | 0 | 0 |
| Opus | 0 | 1 | 0 | **1** | 0 | 0 |

**Your call:** Opus (SU+ST) — SU + ST.

---

### id 34484
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread:** 自古至今冷熱兵器所有任何戰爭都是给人民帶來灾難与死亡！当年刘伯承元帥對子說淮海戰役及說到尤其十年內戰死來死去都是老百姓！都只是在為蔣氏王朝专权汉与毛家帝制獨裁者去賣命！就類似俄乌戰鬥同民族，普金是蘇聯政治改革成功而转變为新俄羅斯民主國家！為北約東擴遲大打不如早小打，率先阻止乌克蘭加入北約受近距離打击更險！只先用熱兵器快將淘汰坦克部隊去打击以便報廢。引來牛部隊再用牛刀！(冷兵器淘汰馬，熱兵器淘汰坦克，现用最可怕火兵器衛星導航导彈与高科技火箭及加核彈头精准打擊。最後容易造成地球人類毀滅！)最好是談判和平大同相处。再说羅馬尼亞以民主推翻前政府，这新集團中夾雜著投機份，借民主捞取巨额財富有之。到头來又是苦百姓。当年毛家发動文革運動而利用权勢！迫使全中國人民为ㄑ毛选冫与ㄑ語錄冫做違法传銷而撈取上億元人民幣稿費臉不紅！全世界民主國家仅只美國算正义！曾在第二次世界大戰时期用巨大物資与死傷兵員(而損失飛機与航母不少！)大數據來支援中國抗日倭侵略！在怕傷亡更多大人員之下百般無奈而采取核武終止戰爭！迫使日本軍國(實力超德國。)無條件投降。
**Translation:** …better a small war early than a big one later over NATO expansion…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Opus (CU+BNE) — CU + BNE.

---

### id 34487
**Video:** `EOqE1jHr694` (T觀點 普欽揮軍烏克蘭背後真相)
**Thread:** 下一個英雄習近平，中俄合擊世界無敵
**Translation:** The next hero is Xi Jinping; China and Russia together are invincible.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **0** | 0 | 0 | 0 |
| Opus | 1 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CU+CT) — CU + CT.

---

### id 34509
**Video:** `F9DL33U-gvc` (抗彈板事件 ft.軍備局205廠廠長)
**Thread (context):** 這兩位的回答真的很符合國防部標準，既沒承認也沒否定，結論是我們現在有60-70分的防彈背心，90分以上的未來才會出現！
**Reply:** 胡說，是防彈弓。@林樞
**Translation:** Nonsense, it's a bullet-proof slingshot.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Mocks Taiwan's equipment → CT.

---

### id 34523
**Video:** `F9DL33U-gvc` (抗彈板事件 ft.軍備局205廠廠長)
**Thread (context):** 提問網友在此 剛好最近對打抗彈版也小有心得，205的板子打了不少 下面小弟重點整理(吐槽)或勘誤一下  08:55 美國軍方早就不使用NIJ標準了，少將這邊真的不要以為沒人看得懂英文耶 14:15 外流甚麼的我不清楚啦，輔導長確定是有的 16:20 少將真的不要再打包票了耶 21:00 共軍2010就已經配發鋼芯彈了，2019是配發初速威力更強的，網路上都有資料 25:00 這邊斐姨的提問一針見血…
**Reply:** ​@money501st8他不會這樣說，他會說，黃埔精神與感謝指教。
**Translation:** He won't say that; he'll say 'Whampoa spirit, thanks for the advice'.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Sonnet (CT) — **Borderline** — Mocks military officials → CT.

---

### id 34541
**Video:** `F9DL33U-gvc` (抗彈板事件 ft.軍備局205廠廠長)
**Thread (context):** 其實看得出廠長要說的就是，考量到單兵背負的重量問題，所以需要取捨，讓一般兵使用3＋級抗彈板，而特戰人員因為有較高的訓練強度，也有近戰需求，所以才需要配發更重的4級板…另外一直不敢提到的應該就是大量普遍配發帶來的成本問題… 廠長終究是科研人員，平時不需要負責公關，所以問答上顯得彆扭且小心翼翼，這點也只能靠公關將軍來協助發言理順邏輯
**Reply:** 作為以本地防守為主的兵員 又不是要外地作戰，長途跋涉 很多補給和彈藥都能就近獲得 平常根本不用帶太多東西，起碼食物就不用帶太多  這樣的情況下 最好是連4級板都背不起 簡直鬼扯  到底是要輕還是要命阿？
**Translation:** Local defenders don't carry much — can't they carry level-4 plates? Rubbish.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Constructive demand for better plates → false.

---

### id 34544
**Video:** `F9DL33U-gvc` (抗彈板事件 ft.軍備局205廠廠長)
**Thread (context):** 其實看得出廠長要說的就是，考量到單兵背負的重量問題，所以需要取捨，讓一般兵使用3＋級抗彈板，而特戰人員因為有較高的訓練強度，也有近戰需求，所以才需要配發更重的4級板…另外一直不敢提到的應該就是大量普遍配發帶來的成本問題… 廠長終究是科研人員，平時不需要負責公關，所以問答上顯得彆扭且小心翼翼，這點也只能靠公關將軍來協助發言理順邏輯
**Reply:** @洪瑞宏-z7w 因為警察不太會遭遇到穿甲彈啊， 但正常三+板是能擋M855綠頭鋼芯彈的， 但國軍公發擋不了， 反而稱M855綠頭叫穿甲彈....  再來士兵用四級板這個叫基本， 一般應該要用美軍ESAPI標準抗彈板， 差別在於NIJ的標準面對的是一般持槍匪徒， 所以是六發隨機射擊沒有貫穿就可以， 而ESAPI則是用機槍掃射三十發子彈同一彈孔能承受三發未貫穿才合格。  你覺得你如果是士兵會想用一塊38000的公發三級板還是一塊45000的ESAPI板？
**Translation:** Real 3+ plates stop M855; the issued ones don't… would you choose them or ESAPI?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Technical → false.

---

### id 34549
**Video:** `F9DL33U-gvc` (抗彈板事件 ft.軍備局205廠廠長)
**Thread (context):** 兩位將軍說話真的很國軍，依然很濃厚的國軍官僚味，不過我願意支持國軍做任何嘗試性的改變👏
**Reply:** 都是發言人 說錯話讓國軍上層不爽就沒工作了
**Translation:** They're spokesmen; say the wrong thing and they're fired.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **1** | 0 | 0 | 0 |
| Opus | 0 | 0 | **0** | 0 | 0 | 0 |

**Your call:** Opus (all false) — false.

---
