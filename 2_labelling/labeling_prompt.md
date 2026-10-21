# Labeling Protocol

## Run config

- `run_number` = 1
- `labeler` = `claude-sonnet-5`

## Background

This is a research project studying how the Russia-Ukraine war has shaped domestic political discourse in Taiwan. The core comparison: Taiwan-China and Ukraine-Russia are both cases of a small state facing a much larger neighboring power ("power asymmetry"). Because of that structural similarity, events in the Ukraine war routinely get imported into Taiwanese political debate as an analogy — either as a warning ("Taiwan could be the next Ukraine, so don't provoke China") or as a model to learn from ("Ukraine shows a small state can resist and deserves support").

Ukraine's image in this discourse has shifted repeatedly with events on the ground — from resistance hero, to a country blamed for provoking Russia and told it should have surrendered, to a symbol of standing up to authoritarian expansion.

In Taiwan specifically, external shocks in the war (Ukrainian setbacks, the US withdrawal from Afghanistan, the 2025 Trump/Vance–Zelensky Oval Office clash, etc.) tend to get localized into two competing domestic narratives: "distrust-of-the-US" discourse (疑美論 — the idea the US would abandon Taiwan the way it might abandon Ukraine, or that Taiwan is just being used as a proxy) versus pro-West / pro-Taiwan-US-alliance discourse that treats Ukraine as reason to strengthen collective defense.

The 6 labels operationalize this: `critical_ukraine`/`supportive_ukraine` and `critical_taiwan`/`supportive_taiwan` capture the localized "next Ukraine" analogy (resistance vs. futility/capitulation) on each side, while `disappointment_with_us` and `blame_nato_expansion` capture the specific rhetorical moves (US-abandonment framing, NATO-provocation/realist framing) used to argue against continued alliance commitments. The underlying research question is whether Ukraine's battlefield, diplomatic, and technological developments (e.g. drone warfare offsetting its numeric disadvantage against Russia) measurably shift the balance between these narratives in Taiwanese social media over time.

## Task

Classify YouTube comments (Taiwanese audiences reacting to videos about the Ukraine war and about Taiwan's own war risk) into 6 independent true/false frames. Most comments are in Chinese, but comments in other languages occur too — classify by content, not by language; don't assume or require Chinese.
Produce true/false per label only — no explanation needed. (Multiple independent labeling passes are run per comment for QA purposes; that's handled externally when results are stored and isn't something the classification itself needs to account for.)

## Which text to label

Pull rows with:

```sql
SELECT id, row_type, video_title, video_description, thread_text_original, comment_text_original
FROM yt_comment_data;
```

- `row_type = 'thread_only'` → label `thread_text_original`. This is a standalone top-level comment.
- `row_type = 'thread_with_comment'` → label `comment_text_original` (the reply). Read `thread_text_original` on the same row as **context only** — it's the comment being replied to, included so short/terse replies ("輸了吧", "笑死") are interpretable. Do not label `thread_text_original` again here; it already has its own `thread_only` row elsewhere with its own label row.
- `video_title`/`video_description` are **context only, on every row** — they identify what the comment is reacting to, which matters for terse or otherwise ambiguous comments (e.g. a comment naming a weapon or tactic only makes sense once you know which side's video it's under). Do not label the video title/description themselves.
- Write results to `yt_comment_label` keyed by `yt_data_id = id`.

## Writing the labels

For each comment, insert one row directly into `yt_comment_label`:

```sql
INSERT INTO yt_comment_label (
  run_number, labeler, yt_data_id,
  critical_ukraine, supportive_ukraine,
  critical_taiwan, supportive_taiwan,
  disappointment_with_us, blame_nato_expansion
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
```

- `run_number` and `labeler` are the fixed values from `## Run config` above — use the same values for every row in this run.
- `yt_data_id` is the `id` column from the row being labeled (see `## Which text to label`).
- The 6 label values are `true`/`false`.

## The 6 labels

The 6 labels are: `critical_ukraine`, `supportive_ukraine`, `critical_taiwan`, `supportive_taiwan`, `disappointment_with_us`, `blame_nato_expansion`. Output a `true`/`false` value for every label, for every comment. There is no null or not-applicable value.

Apply these rules in order:

1. Default every label to `false`. Only set a label to `true` if the comment clearly matches that label's definition (given below, under each label's heading).
2. `critical_ukraine` and `supportive_ukraine` are mutually exclusive: at most one of the two may be `true`. Never set both to `true` for the same comment.
3. `critical_taiwan` and `supportive_taiwan` are mutually exclusive: at most one of the two may be `true`. Never set both to `true` for the same comment.
4. `disappointment_with_us` and `blame_nato_expansion` have no exclusivity restriction. Each can independently be `true` or `false`, regardless of how the other 4 labels are set.
5. `false` is used both when the comment argues against a label's frame, and when the comment simply doesn't mention that topic. Do not try to distinguish these two cases.
6. It is valid for all 6 labels to be `false` on the same comment (e.g. the comment doesn't discuss Ukraine, Taiwan, the US, or NATO).
7. It is valid for a comment to have labels set to `true` from both the Ukraine group and the Taiwan group at once, if the comment discusses both topics.

## Calibration notes from human review

A human reviewed every disagreement between two independent model passes. These patterns came up repeatedly and should sharpen judgment on similar cases:

- **"The US benefits/profits from the war" is `disappointment_with_us`, not `blame_nato_expansion` by default.** Comments claiming the US profits from arms sales, gas sales, or postwar reconstruction contracts express distrust of US motives — that's `disappointment_with_us`. Only mark `blame_nato_expansion` when the comment actually attributes the war's *cause* to NATO's eastward expansion provoking Russia, denies the term "invasion," or argues Russia's action was a justified/understandable response to NATO encroachment. Note: the example list under `blame_nato_expansion` currently includes "美国才是俄乌战争，世界乱战的最大推手" (also listed under `disappointment_with_us`) — treat that phrase as ambiguous on its own; classify based on whether NATO-expansion-as-cause is actually argued, not just whether the US is called a beneficiary.
- **Merely mentioning NATO is not enough for `blame_nato_expansion`.** A question like "為何拜登要讓烏克蘭加入北約？" raises the topic without asserting NATO expansion caused or justified the invasion — leave false absent an actual causal/justificatory claim.
- **`supportive_taiwan`'s "mocks 五毛黨/小粉紅/馬英九/鄭麗文" criterion requires one of those specific named targets (or clear KMT-collaborator content).** Generic mockery of a pro-Russia/pro-China commenter (e.g. jabs at "牆內"/VPN users, or a one-word insult like a Xi-Putin portmanteau) does not qualify by itself — it needs actual Taiwan self-defense content or a clearly identifiable one of the named targets/groups. (Naming/critiquing the 疑美論 "distrust-of-US" narrative itself as a pro-China talking point also qualifies — that's substantive pro-alliance content, not generic mockery.)
- **Rhetorical or challenge questions default to `false` when they merely dispute a factual premise — but a *mocking* rhetorical question that specifically questions whether a side achieved its claimed success does carry a stance.** "俄羅斯何時侵略過利比亞與伊拉克的？" challenges a factual claim without asserting a position on Ukraine/Russia — leave false. By contrast, "烏東三州要解放了嗎？領土奪回了嗎？" (sarcastically asking whether Ukraine's claimed territorial gains actually happened) is incredulous mockery aimed straight at the resistance-success narrative — that's `critical_ukraine`. The test: does the question dispute a side detail, or does it sarcastically undercut the central "is this side winning/right" narrative?
- **Terse factual answers aren't automatically solidarity, but defiant dares are.** A one-word reply like "有" answering "台灣人有去嗎？" is a factual confirmation, not an expression of support — don't inherit `supportive_ukraine`/`supportive_taiwan` from the parent thread's framing when the reply itself carries no independent stance. By contrast, a short defiant challenge like "那你就來打台灣驗證看看啊" ("go ahead and try it") *does* express resolve and counts as `supportive_taiwan`/`supportive_ukraine` — the distinguishing factor is whether the reply itself asserts a stance (even briefly) versus merely confirming a fact.
- **Watch for sarcasm that impersonates the frame it's mocking.** A comment can *sound* like it's defending a side while actually being sarcastic mimicry of the opposing side's rhetoric (or vice versa) — check who the sarcasm's real target is before assuming "arguing against X" implies the opposite label. When the sarcasm's direction is genuinely ambiguous, default `false` rather than guessing a side.
- **General anti-US whataboutism (Iraq, Afghanistan, Syria — illegal invasions, civilian deaths, stolen resources, war crimes with no accountability) counts as `disappointment_with_us`, even without explicit Ukraine/Taiwan alliance-reliability framing.** Don't narrow the label to only "the US would abandon its ally" language — broader distrust/moral condemnation of the US as an actor, raised as a counterpoint in these war discussions, still qualifies. This was a repeated, consistent correction (7/7 agreement in one batch) against an overly narrow reading.
- **Battlefield/tactical assessments that clearly favor one side's narrative should be coded `critical_ukraine`/`supportive_ukraine` accordingly — don't default false just because the content is "military analysis."** A comment saying Ukraine's advance is minimal or a unit got wiped out reads as `critical_ukraine`; a comment saying Russian forces are trapped without supply/resupply, mocking Russia's failed timeline, reporting a pro-Russia commander's death, offering Ukraine-favorable resistance tactics, or predicting Russia's post-war weakness/isolation reads as `supportive_ukraine`. Only default false when the tactical claim is genuinely balanced or doesn't clearly favor either side's narrative (e.g. a rebuttal that just disputes a factual premise without praising or blaming either side).
- **Simply noting the US is a large/involved power is not, by itself, `disappointment_with_us`.** A comment like "這場戰爭就是美國跟俄羅斯在打，美國是小國嗎？" (pointing out the US is big and involved, in response to a "small country" framing) is a factual observation about power dynamics, not moral criticism or distrust of the US — leave `disappointment_with_us` false absent actual criticism, distrust, or betrayal language about the US. Contrast with the Iraq/Afghanistan/Syria whataboutism pattern above, which does qualify because it levels moral condemnation, not just notes involvement.
- **A substantive argument for why unification/capitulation would harm ordinary Taiwanese counts as `supportive_taiwan`, even without explicit defense-buildup or named-target (KMT/五毛/小粉紅) content.** A comment that concretely lays out economic or social harms of unification (job competition, exploitation, lost autonomy) is doing real work against the capitulation frame, not just briefly disagreeing — that's distinct from a short "arguing against X" rebuttal, which stays false per the general false-by-default rule.
- **Mockery of a side's weapons/equipment (primitive, obsolete, or otherwise inadequate) counts as mocking that side's military decline — check `video_title`/`video_description` before defaulting a terse joke to false.**
- **Substantively characterizing China/the CCP as expansionist or colonial (e.g. citing its control over Xinjiang/Tibet/Inner Mongolia/Manchuria) counts as `supportive_taiwan`, even without explicit Taiwan defense-buildup content or one of the named targets (五毛/小粉紅/馬英九/鄭麗文).**
- **Label by who the comment's stance is directed at, not by which country name literally appears in the text.** A comment naming "Taiwan" while offering aid, sympathy, or solidarity toward Ukraine (e.g. "台灣可以幫忙"/"taiwan can help" under a Ukraine-ammo-shortage video) is `supportive_ukraine`, not `supportive_taiwan` — check what the comment is actually offering/directed at, not just which country's name shows up in it. Applies symmetrically: a comment naming "Ukraine" while actually making a claim about Taiwan's own defense situation should be coded on the Taiwan pair instead.
- **Framing NATO itself as "the aggressor" via a historical precedent (e.g. citing the NATO bombing of Yugoslavia) and using that to warn NATO/Ukraine supporters they'll meet the same fate counts as both `blame_nato_expansion` and `critical_ukraine`.** This goes beyond "merely mentioning NATO" — it substantively argues NATO (not Russia) is the real aggressor and delivers a fatalistic warning against backing Ukraine's side, even without an explicit "NATO expansion caused this specific war" sentence.
- **Declaring a side's enemy "represents justice" (代表正义) is critical of whichever side that enemy is fighting.** Russia praised as just → `critical_ukraine`. China praised as just → `critical_taiwan`. Praising both → both labels.
- **Mocking/attacking Taiwanese news outlets as biased, untrustworthy, or "fake news" (e.g. calling out 三立/民視/自由 or "綠媒" specifically) counts as `critical_taiwan`**, even when the immediate target of the jab is a media credibility claim rather than Taiwan's defense posture directly — discrediting the domestic pro-resistance/pro-Ukraine-analogy narrative's own sources serves the same capitulation-adjacent function.
- **Framing US support as purely transactional/interest-driven (not ideological), combined with an explicit "will abandon Taiwan if the cost gets too high" claim, counts as BOTH `critical_taiwan` AND `disappointment_with_us` together.** The transactional-interest framing itself is a direct match to `critical_taiwan`'s own "Taiwan is a pawn/bargaining chip" clause; the abandonment-if-costly claim is separately a US-reliability distrust statement. Evidenced across two batches: ids 13227/13234/13637 (13018-13717) and id 16903 (16218-16917, "if the cost gets too high, the US will abandon Taiwan — everything is about interest").
### critical_ukraine
Frames Ukraine's resistance as futile, coerced, a US proxy war, blames Ukraine/Zelensky for provoking or prolonging the war, mocks conscription, questions the point of continued fighting, questions Ukraine's legitimacy as a country or calls it "fake," or argues Ukrainians are basically Russian anyway (e.g. citing that they speak Russian).

- 俄羅斯會趁機擴大佔領，最終烏克蘭在北約的壓力之下，還是得找美國，即使美國願意再次軍援，烏克蘭將難以挽回頹勢
- 烏國又死了多少呢？怎沒說？
- 俄罗斯一个国家打整个北约和欧洲
- 你在這部影片看到的這些人，可能ㄧ半以上，都不在這個世界了，為了加入北約值得嗎？大家應該反思一下
- 做了大国对抗的炮灰
- 乌克兰人迟早会认识到他们被人当枪用了，所有的牺牲都是不必要的
- 烏克蘭開打不就是為了北約東擴嗎 現在人命都幫你出了 結果武器還要用資源換 蝦仁還要豬心啊
- 北约东扩 太心急，引致俄国百姓反感，最后导致北约失败！
- 支持普丁！💪👍🙏把北约打趴！
- 如果美国接受俄罗斯在加拿大部署武器和部队我就认可，而且，乌克兰明知道普京拿这个当借口，还要加入北约？为了自由把国家拖入战争？不加入损失了什么？
- 支持俄罗斯往死里打北约
- 像烏克蘭這種從開戰一直傳捷報打勝仗的都得上街徵兵 就知道戰爭有多恐怖 一直輸的俄軍只能拉阿婆上戰場
- 烏克蘭人只是美國鬥俄羅斯的替死鬼😂
- 北約自持蘇聯瓦解，違反東擴，加上烏克蘭大屠殺烏東(克里米亞就是開端，人心嚮往蘇俄)，現實是俄國已不惜自損開戰，已收回固有烏東領土與人文順消耗西方好戰者(快聽不到西方傭兵聲音了成為沃土).......
- 確實，烏克蘭先毀約要加入北約，這其實也不能單方面怪俄羅斯
- 烏克蘭捉人當兵你們怎麼不說
- Trump 對烏克蘭的稀土已不感興趣。
- 烏克蘭想停火和平呢：北約軍在裡面呢：你烏克蘭總統管的動他們呢：北約軍不斷攻擊俄羅斯領土呢：永遠和平我看很難呢
- 烏克蘭也一堆被強迫徵兵的
- 美國要吃掉烏克蘭俄羅斯不會忍，能打多少就要打下去

### supportive_ukraine
Expresses solidarity with Ukraine/Ukrainians, hopes for their victory, condemns Russia's invasion as unjust aggression, praises Ukrainian resistance or leadership.

- 俄罗斯侵略者普京必败！
- 真不知普丁這白痴在想什麼，造孽！
- 不僅是爸爸的英雄，也是烏克蘭的英雄，我眼裏的英雄
- 勇敢的烏克蘭人，也是為了這片土地孩子的未來
- 烏克蘭要堅持下去，希望你們取得勝利，奪回領土！
- 侵占人家土地，還可以這麼大聲，布丁你要不要臉啊。
- 打的好 繼續 烏克蘭加油 讓獨裁侵略者得到報應
- 俄罗斯都快卖不出去汽油了，还能嚣张多久？
- 向这些为保护自己国土而战斗的乌克兰人致敬!
- 謝謝董事長，謝謝澤倫斯基總統。
- 勇氣總統很棒的，烏克蘭勝利加油!
- 天佑烏克蘭
- 你怕乌克兰加入北约，说是威胁安全。却不怕北约的发起、组织者美国，还和川普勾勾搭搭。俄罗斯就是侵略成性
- 俄羅斯這個地球最大的侵略者，國土都是侵略得來，現在又說烏克蘭入侵，自己發動戰爭的時候沒想到吧
- 烏克蘭🇺🇦務必再加大轟炸俄羅斯後勤跟人民民生購物重心跟煉油廠.所有港口船.讓俄羅斯莫斯科人深刻感受戰爭帶來強大痛苦.
- 烏不用割地求和、只要川普把把老婆借補釘睡一年補釘就會仃戰這可比烏國割地劃算！
- 俄國人去打，殺烏克蘭人，你都不說一句，還好意思說烏克蘭。
- 烏軍已經攻入俄羅斯領土了啦，還加油勒😂😂
- 烏克蘭必將收復所有領土！侵略者必將戰敗，正義將伸張！💙💛💙💛💙💛
- 烏克蘭必將把普特勒和俄西斯侵略者埋葬在偉大的衛國戰爭的汪洋大海之中！

### critical_taiwan
Frames Taiwan's situation as hopeless/indefensible, mocks Taiwanese defense preparedness, argues resistance is pointless or that Taiwan is a pawn/sacrifice, favors capitulation or "peaceful unification." Also mocks the DPP or 賴清德 specifically, and expresses skepticism that the US would actually intervene, pointing to precedents like Afghanistan or Ukraine as proof the US abandons its partners.

- 戰爭就是如此，戰爭就是殘酷的，台灣想嚐試看看嗎？？
- 觀看這个節目的TAIWAN仔通通家族得絕癥
- 都是被逼的 被人架在火上烤。都是政治的牺牲品。 唉
- 台灣一直在美國的菜單中，如果有一天美國邀請的一位客人中國， 大家不要大驚小怪
- 民進黨也在慢慢走烏克蘭化，從李登輝後期開始到賴清德越來越明顯
- 台湾无路可走
- 早就想得到的結果，偏偏有一堆蠢民執迷不悟信綠圾黨，台灣還因此受到拖累，悲哀！
- 和平統一，一起合作賺全世界的錢
- 台灣問題是中國內政問題，干美國人屁事
- 民進黨仍然利用綠媒放出不實宣傳，說美國會支持第二批軍售給台灣，美國會保護台灣...愚民政策
- 台獨目的根本也不在台獨 撈錢掏空台灣...最後就是逃跑海外而已 台獨根本就假議題....騙台灣人而已
- 不可能像烏克蘭打3年. 3天就結束了.
- 不知道為什麼，台灣人認為老美跨越兩大洋依然能胖揍老共，卻覺得隔條台灣海峽老共就拿台灣沒辦法。
- 美國不但從來沒說過會保護台灣，還一再強調台灣必須自己努力加強火箭防禦，以及延長兵役，要台灣自救
- 川普讓國際知道 美國沒有盟友 只有利益 台灣要用什麼換美國的保護
- 美國絕對不會來的 看看烏克蘭就知道哈
- 等掏空台灣、晶片供應鏈移轉，美國會毫不猶豫丟掉這燙手山竽，搞不好跟對岸一起談好條件做壁上觀~
- 烏克蘭都給你表演了一次了。還在幻想美國爸爸下場？台積電都搬到美國了，台灣可以別做夢了
- 人家是在表示美國要將亞洲防務交給亞洲幾個國家自己防衛。言下之義就是自己要撤退。
- 賴皇又要哭了

### supportive_taiwan
Argues Taiwan should/can defend itself, praises self-reliance or asymmetric defense buildup, expresses resolve to resist, draws motivating (not fatalistic) lessons from Ukraine. Criticizes the KMT as collaborators with China, or mocks 五毛黨, 小粉紅, 馬英九, or 鄭麗文.

- 不要忘記，台灣家人民，現在就是烏克蘭給我們的起式，台灣國家人民一定要認清楚，為何而戰為誰而戰
- 鄰國來的兵或內縱隊抓到，送醫院器官移植，幫助需要器官的人民，謝謝捐贈。
- 烏克蘭沒有跟台灣一樣的大量先進的防空反艦飛彈，沒有500架定翼作戰飛機，最重要的是沒有台灣海峽屏障
- 今日普丁，明日習近平
- 民族國家難到礙到你們了，一堆藉口，什麼台灣本來就是中國的...就算剩一口氣也要拼到最後
- 烏克蘭加油，臺灣一定要發展無人機！
- 今日俄羅斯，明日中共
- 軍民兩用，無人機訓陳入綱，開發全民舉報軟件，全民無人機製造網路，目標百萬台
- 體能和科技知識一定要加強和學習.
- 胡說：戰場還脫晚不了基本的槍技。台灣應實行全民皆兵正如以色列和瑞士的制度。
- 臺灣不幸的事情是國民黨現大在已變壞了...希望臺灣人民的選票落在為人民自專，自由的方面走的政黨
- 台灣的軍備應該跟日本密切合作,甚至可以購買日製的飛機船艦,尤其是美國無法製造的軍艦和海警船.
- 如果台灣人想要保有現在的生活方式⋯就要站岀來保衛台灣的安全
- 自強救己
- 中國（中華民國）與其購入美製軍備，倒不如投資於台澎金馬地區，開發國防軍工，臻軍備完全自供自給。
- 莊敬自強
- 一個在大陸生活了十年且疫情時都在大陸，我只能說：大陸的生活方式，對於大多數的台灣人是接受不了的。
- 美國靠不住，美國不可能協防 頂多協助而已，能軍援就不錯了 強化國防跟不對稱作戰比較重要
- 要靠自己啊！不要猜測亂多！最主要的是國防加強！為了後代子孫不在共產制度下的生活！
- 美國幫台灣容易，只要海上艦隊支援斷後，不用登台實戰，中國就慘兮兮了。

### disappointment_with_us
Expresses distrust, betrayal, or lowered expectations of US commitment/reliability as an ally or partner (to either Ukraine or Taiwan).

- 我当然知道这世界是这样，但我还是很失望！
- 说明你支持错对象了，你支持的应该是民主这个理念，而不是美国。
- 是否特朗普在俄羅斯有投資或者物業？
- 如果侵略能得到獎勵，那將不會有和平。這位官員說得好，這才是真正的洞見。
- 當你以為民主國家不會為了一己之利瓜分其他國家的時候，美國大聲告訴你：「你錯了」
- 美国外交家基辛格说过：做美国的敌人是危险的，做美国的盟友是致命的。
- 历史第一次，美国同朝鲜站在一起。
- 美国、俄罗斯、以色列、朝鲜，一个奇怪的组合
- 文明世界又一次站到了文明世界对立面
- 別演了 美共川爺
- 川普真的过分，中国都没这么舔俄罗斯
- 乌克兰要投降俄罗斯，需要通过川普？泽连斯基个人就能决定坚持跟俄作战？这个嘉宾胡说八道啥呢
- 現在還有人相信美國？
- 美軍：你們最好在總統府底下挖到石油
- 非核家園會很慘!烏克蘭放棄核武的代價!不堪一擊!
- 美国-又要赚
- 雖不得不親美，但絕不能信美！凡事靠自己，自助而後人助。
- 美國真有能力嗎？
- 把台灣自己的生死 需要靠美國幫忙 是台灣人最大的悲哀 Maga 美國 沒義務保護 其他人。
- 美国才是俄乌战争，世界乱战的最大推手

### blame_nato_expansion
Attributes the Russia-Ukraine war to NATO expansion provoking Russia, treats Russia's invasion as a justified/understandable response to NATO encroachment, refuses to call it an "invasion," quotes or praises realist commentators like John Mearsheimer or Jeffrey Sachs.

- 從北約 漫無止盡的擴張 普丁的沒安全感 油然而生 俄烏衝突就此爆發
- 美国才是俄乌战争，世界乱战的最大推手
- 北约东扩 太心急，引致俄国百姓反感，最后导致北约失败！
- 支持普丁！💪👍🙏把北约打趴！
- 如果美国接受俄罗斯在加拿大部署武器和部队我就认可，而且，乌克兰明知道普京拿这个当借口，还要加入北约？
- 支持俄罗斯往死里打北约
- 烏克蘭人只是美國鬥俄羅斯的替死鬼😂
- 北約自持蘇聯瓦解，違反東擴，加上烏克蘭大屠殺烏東(克里米亞就是開端，人心嚮往蘇俄)，現實是俄國已不惜自損開戰，已收回固有烏東領土與人文順消耗西方好戰者(快聽不到西方傭兵聲音了成為沃土).......
- 烏克蘭想停火和平呢：北約軍在裡面呢：你烏克蘭總統管的動他們呢：北約軍不斷攻擊俄羅斯領土呢
- 你在這部影片看到的這些人，可能ㄧ半以上，都不在這個世界了，為了加入北約值得嗎？
- 普丁真是俄羅斯的戰神，將庫斯克變成獵殺北約菁英的好場地，一直引誘北約軍人增兵進入庫斯克
- 烏克蘭開打不就是為了北約東擴嗎 現在人命都幫你出了 結果武器還要用資源換
- 美国才是俄乌战争，世界乱战的最大推手
- 北約不要老想著擴張就沒這些事了 說自己是防禦性組織還入侵南斯拉夫
- 為什麼 TVBS 總是說俄羅斯 "侵略" 烏克蘭, 這些傳媒人應該再看看當時普京跟北約的先後六輪會議！
- 俄罗斯一个国家打整个北约和欧洲
- 美國拱火烏克蘭為稀土？開玩笑嗎？美國主導北約東擴烏克蘭，美國集合衆邪惡軸心國支援烏克蘭
- 美國慫恿出來的戰爭，怪別國支援，真奇怪，北約一再東擴違反協議引發戰爭，一直怪敵對國
- 正常人在普京那個位置上也會這樣子干，北約步步緊逼把他們的國家安全建立在俄羅斯的不安全之上
- 用烏克蘭人民的血消耗北約歐洲與俄國國力，無疑是符合央格魯撒克遜民族與美國石油戰爭派、軍工複合體的利益。

