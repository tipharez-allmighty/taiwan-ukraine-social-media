# Label disagreements: ids 10418-11017

117 disagreements out of 599 labeled rows (Sonnet run_number=1 vs Opus run_number=2).

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion. Only labels set to true are listed per model; anything not listed is false for that model.

---

### 10419
**Video:** 中國若武力犯台 拜登承諾：美國軍事協防台灣－民視新聞
**Thread:** 説真的，還是假的。美國人不可信。
**Comment:** 假的　讓中共出兵打看看不就知道 ("Fake — let the CCP send troops and see, then you'll know")
Sonnet: CT | Opus: (all false)
**Your call:** Sonnet — dismissing the US promise as "fake, let China attack and see" is skepticism the US would actually intervene = critical_taiwan.

### 10422
**Video:** 台灣能借鏡烏克蘭"國土防衛部隊"經驗？...三立iNEWS
**Thread:** 台灣自衛隊
**Comment:** @rgohoo 台灣帝國華擊團，打擊對岸中國專用的現代化濱海作戰團。("Taiwan Empire Strike Group, a modernized coastal-warfare unit dedicated to striking the mainland")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — no US content at all; Opus's DUS is unsupported. Likely just whimsical/satirical naming, not enough for ST either.

### 10433
**Video:** 【少康上線啦20220901LIVE】柯志恩主打不對稱作戰...(Kaohsiung election coverage)
**Thread:** 許采蓁口條不錯，言之有物，不像那個黃捷------
**Comment:** 那當然！...怎麼比得上論述能力超強的采蓁呢？(domestic KMT-vs-independent election sniping)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — purely domestic Kaohsiung election politics, no US content; Opus's DUS is unsupported.

### 10435
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Thread:** 本該如此。可悲的是有些投降派
**Comment:** 我絕不投降 為了台灣獨立建國大業就算台要死灣2000萬人我在所不惜 ("I will never surrender, for Taiwan independence even if 20 million Taiwanese must die")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — explicit resolve never to surrender = supportive_taiwan.

### 10439
**Video:** 借鏡烏克蘭抗戰 台灣獲澤倫斯基獨家授權出書
**Thread:** 這本由台灣出版社獲得授權...中國使館會不會又抗議
**Comment:** 中共如果抗議，就是對號入座 ("If the CCP protests, that's them admitting guilt")
Sonnet: (all false) | Opus: BNE
**Your call:** Sonnet — no NATO/war-cause content; Opus's BNE unsupported.

### 10453
**Video:** 拜登願出兵護台 白宮滅火:戰略模糊未變｜TVBS新聞
**Thread:** 我真的玻璃心碎，美國你在搞什麼啊？變來變去，毫無底線。
**Comment:** @柱子-q1f 三民自可是很認真呀，整個都高潮了，狂討論...("三民自 [pro-green media shorthand] are being so serious, everyone's all worked up...")
Sonnet: (all false) | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, all else false. "三民自" mocks the green-leaning media (三立/民視/自由) as overhyping the story, matching the "mocking Taiwanese green media as biased" calibration note. Neither model's DUS read fits — no actual US criticism here.

### 10455
**Video:** 拜登願出兵護台 白宮滅火:戰略模糊未變｜TVBS新聞
**Thread:** 我真的玻璃心碎，美國你在搞什麼啊？變來變去，毫無底線。
**Comment:** @柱子-q1f 國家領導人是會下台的，下一屆就不是拜登了，美國還不和我們恢復中美共同防御條約...我比較相信的是文字。("Leaders leave office, next term won't be Biden — why hasn't the US restored the mutual defense treaty... I trust written text more")
Sonnet: CT, DUS | Opus: DUS
**Your call:** Sonnet — distrust of a mere verbal promise vs. a formal treaty is a textbook critical_taiwan skepticism-of-US-commitment case, plus disappointment_with_us.

### 10461
**Video:** 拜登願出兵護台 白宮滅火:戰略模糊未變｜TVBS新聞
**Thread:** 哈哈，打臉了！...拜登有點怪怪的...蕭美琴雙爽不到半天
**Comment:** @Iennal 不是不敢打，是打了之後動搖國本，沒必要為了小小台灣發動戰爭，這是在國際上面子問題。(discusses China's own reluctance/face-saving calculus)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — about China's calculus, not US criticism; Opus's DUS unsupported.

### 10470
**Video:** 拜登願出兵護台 白宮滅火:戰略模糊未變｜TVBS新聞
**Thread:** 我真的玻璃心碎，美國你在搞什麼啊？變來變去，毫無底線。
**Comment:** @J. W. 小粉紅？("little pink?")
Sonnet: (all false) | Opus: BNE
**Your call:** OVERRIDE — supportive_taiwan=true, all else false. Names 小粉紅 specifically, which per the ST named-target calibration note qualifies even as a bare one-word callout. Opus's BNE is unsupported (no NATO content).

### 10475
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 还不赶紧修宪正名独立加入联合国？
**Comment:** @yunhailu9487 你只能哈哈哈 不然還能幹嘛 😋🤗 ("You can only laugh, what else can you do")
Sonnet: ST | Opus: (all false)
**Your call:** Opus — dismissive banter, no independent stance asserted (not a defiant dare, just mockery of the parent poster).

### 10485
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 还不赶紧修宪正名独立加入联合国？
**Comment:** 你們這麼想統一，可以啊!你們直接改國號叫中華民國 ("You want unification so badly? Fine, just rename yourselves ROC")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — substantive pushback asserting Taiwan/ROC's distinct identity from PRC.

### 10487
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 还不赶紧修宪正名独立加入联合国？
**Comment:** 等中華這個詞被中共弄到臭得差不多時候再換國名也不遲🤣🤣 ("Wait till CCP has ruined the term 'China' before changing the name")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — anti-CCP identity-distancing argument, fits supportive_taiwan.

### 10490
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 还不赶紧修宪正名独立加入联合国？
**Comment:** @yichengwang5644反正你们是出气筒~生气拿台湾当出气包使用可以延年益寿~ ("Anyway you're a punching bag, taking anger out on Taiwan prolongs life")
Sonnet: ST, DUS | Opus: ST
**Your call:** OVERRIDE — all false. Sarcasm direction is genuinely ambiguous (mocking Taiwan as a punching bag, or mocking the parent poster?) — default false per the ambiguous-sarcasm calibration note.

### 10492
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 一打仗就跑了
**Comment:** 根本就是来拱火的嘛 ("[The US is] basically just here to fan the flames")
Sonnet: (all false) | Opus: BNE
**Your call:** OVERRIDE — disappointment_with_us=true, all else false. "Fanning the flames" accuses the US of stoking conflict for its own interest re: Taiwan, not a NATO-expansion/Russia claim — Opus mislabeled the direction.

### 10494
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 美國果然是盟友，說到做到
**Comment:** 你們這些無知的人 美國做到了 他們做到什麼事 你叫美國有種 美軍駐在台灣 我才相信 ("What did the US actually do? Only if the US actually stations troops in Taiwan will I believe it")
Sonnet: CT, DUS | Opus: DUS
**Your call:** Sonnet — explicitly demanding proof beyond words = skepticism the US would actually intervene, textbook critical_taiwan, plus disappointment_with_us.

### 10514
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** (long PRC MOFA boilerplate condemning US arms sales/Pelosi visit, citing the three joint communiqués)
**Comment:** 中美三个联合公报 是 歷屎文件喔!! 😆🤣 ("The three joint communiqués are 'shitty [history] documents' lol")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — mocks/discredits the PRC's legalistic framework used to justify pressure on Taiwan, fits the "undermining CCP's threat/framing" pattern.

### 10515
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 一打仗就跑了
**Comment:** 不是人人都像习维尼那么龟孙 ("Not everyone is a coward like Xi Jinping")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — mocks Xi/CCP leadership as cowardly, undermining the China-threat narrative, extends the "mocking CCP threats as hollow" pattern to mocking the leader personally.

### 10520
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Thread:** (long essay praising Chinese/Singaporean authoritarian governance over Western democracy)
**Comment:** 你们的认知战太可怕，大陆除了没有选举，财富靠本事打拼，法律法规完善，真没有你们传的那样搞笑 ("Your cognitive warfare is scary, the mainland's system is actually fine")
Sonnet: (all false) | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, all else false. Defends the PRC system as legitimate against "your cognitive warfare" (i.e. Taiwan/West's framing) — pro-unification-adjacent content under a video about countering PRC psy-ops against Taiwan. No US content, so Opus's DUS is wrong.

### 10524
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 看起來是很有一回事，但是基本上我不認為匪國敢在這個時間點攻擊...有了俄羅斯的例子，我看席皇帝應該是不會硬來啦 ("Given Russia's example, I don't think Xi will act rashly")
**Comment:** 你說的很有符合邏輯和道理論點 贊成你的分析闡述 為什麼下面1個網友的話沒有顯示回覆出來哈 ("What you said is logical, I agree with your analysis. [unrelated display question]")
Sonnet: (all false) | Opus: ST
**Your call:** Opus — explicit agreement ("I agree with your analysis") with a parent comment whose core point is Russia's setback deterring China, matching the "predicting China's deterrence from Russia's example" = supportive_taiwan pattern; the terse-agreement-inherits-stance precedent applies here since it's explicit endorsement, not a bare fact-confirmation.

### 10528
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Thread:** 当年义和团和洋人也是不对称战争...就是换着法儿挨打😂
**Comment:** 現在解放軍拿東風反艦也是不對稱 解放軍等於義和團？("PLA's DF anti-ship missiles are also asymmetric, is PLA the Boxer Rebellion then?")
Sonnet: (all false) | Opus: BNE
**Your call:** Sonnet — a tu quoque about PLA's own strategy, no NATO content, doesn't clearly commit to either side's Taiwan-defense narrative.

### 10546
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Thread:** DBS呢，就是体制外野生军事"砖家"...要推翻民进党的统治
**Comment:** @DinoBrothersStudio 加油，你们已经成功一半了，但是要look out不要又选一个口花花的上台 ("Keep it up, but watch out for electing another smooth-talker")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — domestic Taiwan politics warning, no US content.

### 10559
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Thread:** 在绝对的实力面前，你们这都是浮云！😢
**Comment:** @brainding2033 和鹅蝶一样，没打之前世界第二，什么最强巡洋舰，核潜艇，五代战机，一打全露馅，战术水平思想，武器实用性停留在冷战水平 (mocks Russia's overhyped military as exposed/obsolete once fighting started)
Sonnet: SU | Opus: ST, BNE
**Your call:** Sonnet — mocking Russia's military decline is the established supportive_ukraine pattern; Opus's ST/BNE have no Taiwan/NATO content.

### 10561
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Thread:** 在绝对的实力面前，你们这都是浮云！😢
**Comment:** @brainding2033 笑死，中共党卫军建军照抄苏联俄罗斯...台湾军事实力远远强于乌克兰，号称世界第二的俄拿不下乌，中共也做不到 (mocks PLA as backward-copied-from-Russia; argues Taiwan is stronger than Ukraine so PRC can't succeed where Russia failed)
Sonnet: SU, ST | Opus: SU, BNE
**Your call:** Sonnet (full row) — both agree SU; the "Taiwan is militarily stronger than Ukraine, so PRC can't do what Russia couldn't" is a motivating lesson from Ukraine = supportive_taiwan. Opus's BNE unsupported.

### 10563
**Video:** 拜登再稱若中國攻擊 美國會防衛台灣－ BBC News 中文
**Thread:** 当时他对乌克兰也是这么说的。("He said the same about Ukraine back then")
**Comment:** @kobebryant6844所以美国会为了台湾跟中国打仗😂😂 ("So the US would fight China over Taiwan? 😂😂")
Sonnet: CT | Opus: DUS, BNE
**Your call:** Sonnet — sarcastic mockery citing the Ukraine precedent to undercut US-commitment credibility is a direct match to critical_taiwan's own definition; Opus's BNE is unsupported.

### 10571
**Video:** 拜登再稱若中國攻擊 美國會防衛台灣－ BBC News 中文
**Thread:** (long factual account of US arms-sale pace to Taiwan)
**Comment:** 美国对台湾问题从来没有真正尊重中国人民的意愿和利益...美国想利用台湾作为一个棋子 ("US never respected China's interests, wants to use Taiwan as a pawn")
Sonnet: DUS | Opus: DUS, BNE
**Your call:** Sonnet — purely US-China-Taiwan pawn framing, no NATO content; Opus's BNE unsupported.

### 10572
**Video:** 拜登再稱若中國攻擊 美國會防衛台灣－ BBC News 中文
**Thread:** 我们欢迎美国宪政...谢谢美国人民援助建立北大清华
**Comment:** The United States wants to use Taiwan Province as a breakthrough to provoke internal unity and national rejuvenation of the Chinese nation.
Sonnet: DUS | Opus: DUS, BNE
**Your call:** Sonnet — same pattern, no NATO content.

### 10574
**Video:** 拜登再稱若中國攻擊 美國會防衛台灣－ BBC News 中文
**Thread:** 為何要把台灣當棋子
**Comment:** 台湾不当美国棋子怎么活呢？("If Taiwan isn't the US's pawn how would it survive?")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — resigned/pragmatic acceptance of "pawn" status as necessary for survival, not clear distrust/betrayal language.

### 10604
**Video:** 台灣能借鏡烏克蘭"國土防衛部隊"經驗？...三立iNEWS
**Thread:** 重點是槍枝跟裝備夠嗎？還有難民疏散到哪裡去？
**Comment:** 這是形成有效嚇阻 如果盡力防守後背，還是真打到城市裏 其實也不用打了 盡人事聽天命 (deterrence framing, but fatalistic if fighting reaches cities)
Sonnet: (all false) | Opus: BNE
**Your call:** Sonnet — genuinely mixed/ambivalent (deterrence value + fatalism), no NATO content for Opus's BNE.

### 10607
**Video:** 拜登再稱若中國攻擊 美國會防衛台灣－ BBC News 中文
**Thread:** (long essay: Taiwan ≠ Ukraine, unfinished civil war framing, Ryukyu independence discussion)
**Comment:** (long historical/legal rebuttal on Ryukyu vs Taiwan status, concludes >93% of Taiwanese don't identify as Chinese)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — historical/identity argument, no NATO content, doesn't fit ST's specific criteria (no defense/self-reliance/named-target content).

### 10609
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Thread:** 要是让你当防长，我方损失会更大，但是结果不会改变
**Comment:** @鮑成海 就像台湾不敢独立...台湾真想独立，宣布新国号，也是很简单的事情。解放军想击毁几条破军舰也是很简单的事情，但他也没有那么做。 (Taiwan doesn't dare declare independence; PLA restraint noted)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — no US content; a neutral-ish observation about mutual restraint, not clearly hopeless/pawn framing.

### 10619
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 小粉紅：美帝，等著我們抵制吧
**Comment:** 现在看，是不是发现美帝、小粉红、普丁，三者是一个阵营的 ("US imperialists, little pinks, and Putin are all the same camp")
Sonnet: DUS | Opus: DUS, BNE
**Your call:** Sonnet — sarcastic collusion claim, no actual NATO-causation argument for BNE.

### 10623
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 亮哥點出重點：親美保台 ("Brother Liang nails it: pro-US, protect Taiwan")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — endorses the pro-alliance defense stance explicitly.

### 10626
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 拜登怕在任内失去台湾.中国统一！("Biden fears losing Taiwan to unification during his term")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — a political prediction, not distrust/betrayal language.

### 10630
**Video:** 台美關係堅若磐石！特定人士操作"美國棄台論"...三立新聞台
**Thread:** 美國常說堅若盤石，真的它沒有說謊，堅若盤石的意義就是如如不動的意思，也就是說你若被打，我也不會理你！("'Rock solid' actually means unmoving — if you get hit, I won't bother with you")
Sonnet: CT, DUS | Opus: BNE
**Your call:** Sonnet — mocks the "rock solid" alliance phrase as meaning US passivity, textbook critical_taiwan + disappointment_with_us; Opus's BNE unsupported.

### 10631
**Video:** 台美關係堅若磐石！特定人士操作"美國棄台論"...三立新聞台
**Thread:** 都知道美国会举国之力保台湾的，相信美国放弃本土也不会放弃台湾 ("The US would abandon its own homeland before abandoning Taiwan")
Sonnet: CT | Opus: DUS, BNE
**Your call:** Sonnet — reads as hyperbolic/sarcastic mockery of naive over-trust in the US, undermining the "rock solid" narrative; Opus's BNE/DUS don't fit (this isn't distrust language, and no NATO content).

### 10634
**Video:** 台美關係堅若磐石！特定人士操作"美國棄台論"...三立新聞台
**Thread:** 看能不能買F18 ("See if we can buy F-18s")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — defense-buildup advocacy.

### 10635
**Video:** 台美關係堅若磐石！特定人士操作"美國棄台論"...三立新聞台
**Thread:** 中國口交部氣死了 (crude pun mocking China's Foreign Ministry)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — crude joke, no US content, no substantive named-target content for ST either.

### 10636
**Video:** 台美關係堅若磐石！特定人士操作"美國棄台論"...三立新聞台
**Thread:** 美国重量级保护费收取团今天抵台，最希望他们去的乌克兰，美国人视而不见。("The US 'protection fee collection team' arrives, but the US ignores where it's most needed — Ukraine")
Sonnet: CT, DUS | Opus: BNE
**Your call:** Sonnet — "protection fee" mocking + criticizing US for ignoring Ukraine matches the established "transactional alliance" critical_taiwan pattern plus disappointment_with_us; Opus's BNE unsupported.

### 10647
**Video:** 中國若武力犯台 拜登承諾:美國軍事協防台灣－民視新聞
**Thread:** (legalistic argument that TRA outranks the joint communiqués/MOU, i.e. arguing FOR US legal obligation)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — argues the US IS legally bound, opposite direction from distrust; Opus's DUS wrong.

### 10655
**Video:** 拜登承諾出兵協防台灣　美防長:美國立場沒有改變－民視新聞
**Thread:** 好吔！只要美國兵一起打台海戰，而不是叫台灣人自己送死像烏克蘭 ("Great, as long as US troops join the fight, rather than telling Taiwanese to die alone like Ukraine")
Sonnet: ST | Opus: CT
**Your call:** OVERRIDE — critical_ukraine=true, all else false. The core content frames Ukraine as having been "told to die alone" — an unnecessary-sacrifice/proxy-war framing of Ukraine's resistance, matching critical_ukraine's own definition. Neither ST (about Taiwan's own defense) nor CT (this isn't framing Taiwan as hopeless) fit as well.

### 10658
**Video:** 拜登承諾出兵協防台灣　美防長:美國立場沒有改變－民視新聞
**Thread:** 拜登已多次表明，當台灣受中共侵略時會出兵協助，因為這是美國所作的 Commitments...真不知那些人還不斷問這些無聊問題幹啥？(affirms trust in Biden's "rock solid" commitments)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — this is pro-US-trust, opposite direction from disappointment; Opus's DUS wrong.

### 10662
**Video:** 【每日必看】拜登4度提協防台灣 彭博社:援烏已用盡美國彈藥
**Thread:** 協防等於不出兵 ("'Co-defense' equals not sending troops")
Sonnet: CT | Opus: BNE
**Your call:** Sonnet — skepticism the promise means real troop commitment, textbook critical_taiwan; Opus's BNE unsupported.

### 10663
**Video:** 【每日必看】拜登4度提協防台灣 彭博社:援烏已用盡美國彈藥
**Thread:** 協防台灣又不是直接參戰，還堅持一中原則，兩面手法 ("'Co-defense' isn't direct participation, and they still uphold One-China — double-dealing")
Sonnet: CT, DUS | Opus: BNE
**Your call:** Sonnet — same skepticism-of-empty-promise pattern plus explicit "two-faced" criticism; Opus's BNE unsupported.

### 10664
**Video:** 【每日必看】拜登4度提協防台灣 彭博社:援烏已用盡美國彈藥
**Thread:** 美日侵略台灣的話 難道中國不敢出兵抵抗？ 保衛台灣！ (inverted pro-China framing: "if US/Japan invade Taiwan, won't China resist? Defend Taiwan!")
Sonnet: CT | Opus: ST, BNE
**Your call:** Sonnet — this coopts "defend Taiwan" rhetoric for a pro-China/pro-unification framing (siding with China's narrative), matching critical_taiwan; Opus's ST misreads the sarcasm direction, and BNE is unsupported.

### 10666
**Video:** 破除美國棄台論？拜登派代表團閃電訪台
**Thread:** (long essay: US orchestrated the Russia-Ukraine conflict by refusing to rule out Ukraine's NATO membership, used Ukrainian lives to extract European submission, "US is the world's main instigator of war")
Sonnet: DUS, BNE | Opus: CU, DUS, BNE
**Your call:** Opus (full row) — clearly blame_nato_expansion (US refusing to foreclose NATO membership as the provocation) and disappointment_with_us; "used Ukrainian lives to extract European submission" also frames Ukraine as a used/sacrificed proxy = critical_ukraine.

### 10667
**Video:** 破除美國棄台論？拜登派代表團閃電訪台
**Thread:** 猪佩奥失业来台～加油 (mocks Pelosi/the delegation as "unemployed," visiting Taiwan)
Sonnet: DUS | Opus: (all false)
**Your call:** Sonnet — mocks the visit as a hollow/desperate gesture, mild disappointment_with_us framing.

### 10673
**Video:** 破除美國棄台論？拜登派代表團閃電訪台
**Thread:** 美利堅合眾國太壞了啦！害烏克蘭現在又要害台湾。("The US is too evil! Harmed Ukraine, now wants to harm Taiwan too")
Sonnet: CT, DUS | Opus: CU, CT, DUS
**Your call:** Opus (full row) — "harmed Ukraine" blames the US for Ukraine's suffering, fitting the used/sacrificed-by-the-US proxy framing of critical_ukraine, on top of the shared CT+DUS.

### 10677
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 大家眼睛看看，現在幾乎每個新聞台都舔綠到不行，實際上看到的卻是滿滿的疫情沒超前部署、加害者的保護、豆腐渣工程 ("Every news channel is fawning over green [DPP], but what we see is failed pandemic prep, protecting perpetrators, shoddy construction")
Sonnet: (all false) | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, all else false. Directly accuses Taiwanese media of excessive pro-DPP bias while attacking DPP governance — matches the "mocking Taiwanese green media as biased" pattern. No US content, so Opus's DUS is wrong.

### 10679
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 我們沒有白繳保護費，這樣懂了嗎? ("We haven't paid protection money for nothing, understand?")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — defends the alliance relationship's value.

### 10688
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 美國不幫烏克蘭..跑台灣來騙... ("The US doesn't help Ukraine, comes to deceive Taiwan instead")
Sonnet: CT, DUS | Opus: BNE
**Your call:** Sonnet — cites US non-help for Ukraine to argue the Taiwan visit is deceptive, fits CT (precedent-based skepticism) + DUS; Opus's BNE unsupported.

### 10692
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 笑死我了，派几个人过来就是不放弃台湾，那么美国也挺乌克兰...援助了6.5亿军火，就是不派兵参战，嗯，确实没放弃😂😂😂 (sarcastically compares the token visit to US aid-without-troops for Ukraine)
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. The sarcasm mocks both the hollowness of the Taiwan gesture (CT, citing the Ukraine parallel) and the general pattern of US non-committal support (DUS). Opus's BNE unsupported.

### 10694
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** (long skeptical essay citing Ma Ying-jeou's "US will sell weapons but not send troops" claim, plus Afghanistan/Vietnam withdrawal precedents)
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Explicitly cites Afghanistan/Vietnam abandonment precedents — a direct match to CT's own definition — plus general distrust language. Opus's BNE unsupported.

### 10695
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 这下台人🈶️救了！("Now Taiwanese people have hope/are saved!")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — expresses relief/positive sentiment, opposite direction from disappointment; too thin for ST either.

### 10698
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 美國說會協防台灣，有很大的可能只是站在旁邊觀看，在旁邊喊戰敲邊鼓而已，這點可由烏克蘭當中可以清楚的看出來。("The US will likely just stand by and cheer from the sidelines — clear from the Ukraine case")
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Explicit Ukraine-precedent citation for skepticism of actual intervention = textbook CT, plus general distrust = DUS. Opus's BNE unsupported.

### 10711
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 先把俄爹呑掉的拿回來再講 ("First get back what 'Russia-daddy' swallowed, then talk")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — matches the established "naming Russia but actually about Chinese irredentism/territory lost to Russia" whataboutism pattern, likely aimed at a pro-China/pro-Russia commenter; no US content for Opus's DUS.

### 10730
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 标题很有预见性，现在川普劝泽连斯基放弃领土，承诺用不加入北约，今日乌克兰明日台湾可太好玩了😅 (darkly notes Trump pressuring Zelensky to cede territory/forgo NATO)
Sonnet: CT, DUS | Opus: CU, CT
**Your call:** OVERRIDE — critical_ukraine=true, critical_taiwan=true, disappointment_with_us=true, all else false. Frames Ukraine as being pressured/coerced into capitulation (CU), both models' shared CT (skepticism about Taiwan's fate) stands, and Trump/US pressuring an ally to cave fits disappointment_with_us too.

### 10733
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 中貢國到處欺压別國。。。早晚會被反撲~今日惡羅斯，明日中貢國！("'Tribute-nation China' oppresses others everywhere, sooner or later there'll be backlash — today evil-Russia, tomorrow China")
Sonnet: SU | Opus: ST
**Your call:** Opus — the target is China/Taiwan's fate (predicting PRC's downfall parallel to Russia's), not solidarity with Ukraine directly; per the "label by who it's directed at" precedent this is supportive_taiwan.

### 10734
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 在美國看來阿富汗跟烏克蘭一樣?("In the US's view, is Afghanistan the same as Ukraine?")
Sonnet: CT | Opus: BNE
**Your call:** Sonnet — sets up the Afghanistan/Ukraine abandonment-precedent comparison central to CT's own definition; Opus's BNE unsupported.

### 10740
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 真打成廢墟守護爛轉頭，叫美國說真打派軍隊幫台灣打，記得美軍重兵來哦。(doubts Taiwan's defense would hold, sarcastically demands the US send "heavy troops")
Sonnet: CT | Opus: (all false)
**Your call:** Sonnet — skeptical/fatalistic tone about defense capability plus sarcastic doubt the US would truly commit heavy forces.

### 10746
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 真是可憐到來台灣取暖 ("Pathetic, coming to Taiwan just to 'warm up' [political theater]")
Sonnet: DUS | Opus: (all false)
**Your call:** Sonnet — dismisses the visit as hollow political theater, disappointment_with_us framing.

### 10761
**Video:** 若中國大陸武力犯台 拜登:美國會出兵防衛｜TVBS新聞
**Thread:** 很堅定的回答，很好 ("Very firm answer, good")
Sonnet: ST | Opus: (all false)
**Your call:** Opus — praising the US's answer isn't Taiwan's own self-reliance/resolve; too thin/off-target for ST.

### 10762
**Video:** 若中國大陸武力犯台 拜登:美國會出兵防衛｜TVBS新聞
**Thread:** 習近平知道你們TVBS播報這種新聞嗎😏 ("Does Xi know TVBS is broadcasting this? 😏")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — ambiguous sarcasm target (mocking TVBS's boldness or Xi's sensitivity), no US content, default false.

### 10765
**Video:** 若中國大陸武力犯台 拜登:美國會出兵防衛｜TVBS新聞
**Thread:** 喔⋯這老頭又想幹嘛了？說這話前應該把三個航母戰鬥群放在海峽中線吧⋯⋯你的【椰絲】說完後⋯然後呢？("What's this old man up to? Should put 3 carrier groups at the strait median first...after your 'talk' then what?")
Sonnet: CT | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Mocks the statement as empty words without real military backing — fits both the skepticism-of-empty-promise CT pattern and general distrust.

### 10768
**Video:** 台美關係堅若磐石！特定人士操作"美國棄台論"...三立新聞台
**Thread:** 不用什麼前前前官員來， 有種賣我們F-35或直接跟我們建交 ("No need for some former official, if you dare sell us F-35s or establish diplomatic relations directly")
Sonnet: CT | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Dismisses token visits as insufficient while demanding substantive commitment — skepticism of empty gestures.

### 10775
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 有種去跟中共直接斷交。("If you dare, go cut ties with the CCP directly")
Sonnet: CT | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Same "demand bolder action, implying current stance is hollow" pattern as 10768.

### 10784
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 修補選票 ("Repairing votes" — re: Tsai's charity visit as PR)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — domestic Taiwan politics, no US content.

### 10785
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 這一些說法是菜菜的語法有菜菜的團隊提供給美國的說法 ("These are Tsai-style talking points fed by her team")
Sonnet: (all false) | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, all else false. Mocks Tsai/DPP's messaging as scripted spin, fits the "mocks the DPP" clause of critical_taiwan; not US criticism.

### 10800
**Video:** 借鏡烏克蘭! 美只軍援不出兵 台灣除了花錢軍購 國安更得靠自己｜十點不一樣20220224
**Thread:** 美國真的不會協防只會打打嘴砲然後賣武器給你自己打 ("The US won't co-defend, just talks big then sells you weapons to fight yourself")
Sonnet: CT, DUS | Opus: BNE
**Your call:** Sonnet — direct skepticism of US intervention plus criticism of hollow talk; Opus's BNE unsupported.

### 10804
**Video:** 借鏡烏克蘭! 美只軍援不出兵 台灣除了花錢軍購 國安更得靠自己｜十點不一樣20220224
**Thread:** 台湾看好了，这是美国第二次示范坚定支持了，上次示范是阿富汗。("Taiwan take note, this is the US's second demonstration of 'firm support' — last time was Afghanistan")
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Explicit Afghanistan-precedent citation is a direct CT definition match, plus sarcastic distrust. Opus's BNE unsupported.

### 10808
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 昨日香港CIA躲在後面..今日烏克蘭CIA站在前面..明日臺灣CIA不停賣武器 (conspiratorial CIA-orchestration claim across HK/Ukraine/Taiwan)
Sonnet: DUS | Opus: SU, ST, DUS
**Your call:** Sonnet (DUS only) — purely cynical about US/CIA manipulation, no positive Ukraine/Taiwan content; Opus's SU/ST are a mismap.

### 10810
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 台灣跟烏克蘭不一樣 他們很團結 台灣太多內奸 記住台共開戰 要先殺內奸 ("Taiwan isn't like Ukraine, they're united, Taiwan has too many traitors")
Sonnet: CT | Opus: CT, ST, DUS
**Your call:** Sonnet (CT only) — note: Opus's row has both CT=true AND ST=true simultaneously, an exclusivity-rule violation (worth flagging as a labeling bug). The core content (Taiwan fractured/compromised by internal traitors, unlike unified Ukraine) is clearly critical_taiwan, not supportive_taiwan.

### 10813
**Video:** 「今日烏克蘭 明日台灣」　台大百位師生齊聲援－民視新聞
**Thread:** 今日烏克蘭，明日台灣！(bare slogan only)
Sonnet: SU | Opus: (all false)
**Your call:** Opus — bare recurrence of the "今日烏克蘭明日台灣" slogan with zero added content; per the standing note this shouldn't be flagged as notable/labeled on its own.

### 10817
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 什麼時候美國爸爸要跟台灣建交呢？("When will 'Daddy America' establish relations with Taiwan?")
Sonnet: (all false) | Opus: BNE
**Your call:** Sonnet — no NATO content; a rhetorical/sarcastic question without clear US criticism.

### 10819
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 美國！有本事你先把核武都拿掉！("America, if you dare, get rid of your own nukes first!")
Sonnet: (all false) | Opus: BNE
**Your call:** OVERRIDE — disappointment_with_us=true, all else false. Points out US nuclear hypocrisy — anti-US whataboutism, matching the general whataboutism calibration note. Opus's BNE is unsupported (no NATO content).

### 10821
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 靠北  要打就快啦裝模作樣。沒人鳥你們的。("If you're gonna fight then hurry up, quit posturing")
Sonnet: DUS | Opus: DUS, BNE
**Your call:** Sonnet — Opus's BNE has no NATO content, unsupported.

### 10824
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 美国弃了多少地方了 哪个不是坚若磐石 ("How many places has the US abandoned, weren't they all 'rock solid' too?")
Sonnet: CT, DUS | Opus: DUS, BNE
**Your call:** Sonnet — direct citation of the "abandonment despite promises" pattern; Opus's BNE unsupported.

### 10826
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 要選舉空頭支票一直開 ("Empty election promises keep getting made")
Sonnet: (all false) | Opus: BNE
**Your call:** OVERRIDE — disappointment_with_us=true, all else false. Given the video's context (Biden's pledge ahead of midterms), this reads as dismissing the promise as election-motivated and empty — no NATO content for BNE.

### 10829
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 真的打起來 美國一定跑的 ("If it really comes to blows, the US will definitely run")
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Clear skepticism the US would intervene plus general distrust; Opus's BNE unsupported.

### 10832
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 嘴巴護台真厲害👍也只有傻b才會相信 ("So great at 'mouth-defending' Taiwan, only an idiot would believe it")
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Same sarcastic-dismissal-of-verbal-commitment pattern.

### 10847
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 台灣願意作美國魁儡的只有政客和名嘴耶！("Only politicians and pundits are willing to be America's puppet")
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Frames TW politicians as US puppets (CT pawn framing) and implies US instrumentalizes Taiwan (DUS); Opus's BNE unsupported.

### 10850
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 不提軍工不提納粹。金融巨鱷作亂 ("Not mentioning military-industrial complex, not mentioning Nazis. Financial crocodiles wreaking havoc")
Sonnet: (all false) | Opus: BNE
**Your call:** Sonnet — too cryptic/conspiratorial to confidently attribute an actual NATO-expansion-caused-the-war claim.

### 10859
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Thread:** 沒辦法台灣國內很多賣台集團、每天都笑想擁抱徐老大的美腿、死掉也甘願 (mocks domestic "sell-Taiwan-out" collaborator factions)
Sonnet: CT | Opus: DUS
**Your call:** Sonnet — mocking domestic capitulation-adjacent factions fits critical_taiwan; Opus's DUS reading of the garbled phrasing is less supported.

### 10869
**Video:** 拜登：中國若武力侵台灣美國會出兵防衛　白宮澄清　台外交部回應
**Thread:** 人地叫擴張挑釁，自己就叫強化能力🤭 ("When others do it it's 'expansion/provocation,' when you do it it's 'strengthening capability'")
Sonnet: DUS | Opus: (all false)
**Your call:** Sonnet — US-hypocrisy whataboutism jab, fits disappointment_with_us.

### 10871
**Video:** 拜登：中國若武力侵台灣美國會出兵防衛　白宮澄清　台外交部回應
**Thread:** 🇺🇸🇹🇼😎🤟 (flag emojis + celebratory emojis)
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — clear positive symbolic US-Taiwan solidarity, thin but unambiguous in direction.

### 10882
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 好幾把億的韭菜們又崩潰了 ("The 'leeks' [gullible nationalist masses] are collapsing again")
Sonnet: ST | Opus: (all false)
**Your call:** Opus — "韭菜" (leeks) is generic mockery of pro-China commenters, not one of the specifically named targets (五毛黨/小粉紅/馬英九/鄭麗文) required by the ST calibration note, and no defense content either.

### 10885
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 台灣前準備好 (likely typo for "Taiwan needs to be ready")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — readiness/preparedness call fits supportive_taiwan.

### 10886
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 美國會出兵  Yes ("The US will send troops. Yes")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — consistent with the other thin alliance-affirming cases this batch.

### 10902
**Video:** 借鏡烏克蘭 台灣能靠自己？獨撐戰局VS.堅守待援#我們這麼說
**Thread:** 俄军只是想围着基辅，答应俄罗斯的条件，并不是想占领乌克兰；真不知岛上的所谓砖家都是一群什么玩意？🐷🧠😂 (minimizes Russia's war aims as limited/reasonable; mocks Taiwanese "experts")
Sonnet: CU | Opus: CT, DUS
**Your call:** OVERRIDE — critical_ukraine=true, critical_taiwan=true, all else false. Minimizing/excusing Russia's invasion as limited fits CU; separately mocking Taiwanese "island experts"/pundits fits critical_taiwan's pundit-discrediting pattern. Opus's DUS is dropped — no actual US content.

### 10903
**Video:** 借鏡烏克蘭 台灣能靠自己？獨撐戰局VS.堅守待援#我們這麼說
**Thread:** 太無知!!!不是烏克蘭挺到現在,是俄羅斯還沒發動真正攻擊!就是轟炸!像美國轟炸伊拉克......一樣! (argues Ukraine's resistance narrative is untested since Russia hasn't gone all-out)
Sonnet: CU | Opus: CT, BNE
**Your call:** Sonnet — minimizes/discredits Ukraine's resistance achievement, fits critical_ukraine; Opus's CT/BNE are unsupported (no Taiwan or NATO-causation content).

### 10905
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 議員放話完，不要拍拍屁股走人才是 ("After making statements, [the congressman] shouldn't just dust off and leave")
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Skepticism words won't be followed through; Opus's BNE unsupported.

### 10907
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 奇怪臺灣自個兒的事竟然不能自己做主?!("Strange, Taiwan can't even decide its own affairs?!")
Sonnet: CT | Opus: (all false)
**Your call:** Sonnet — frustration at lack of sovereignty/autonomy fits the pawn/hopeless framing of critical_taiwan.

### 10912
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 感謝訪問團感謝，之持我國一定要出兵協防，不賣武器，只能贈送，要啥有啥這樣才有義意 (demands actual troops and donated, not sold, weapons)
Sonnet: DUS | Opus: (all false)
**Your call:** Sonnet — implies current arrangement is insufficient, fits disappointment_with_us.

### 10914
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** Welcome~ freedom, democracy👍👍👍
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — enthusiastic pro-alliance/pro-democracy sentiment.

### 10915
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 破除棄台？ 破你香蕉芭辣！("'Break the abandonment theory'? What nonsense!")
Sonnet: CT | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Dismisses the reassurance as nonsense — skepticism it's genuine.

### 10923
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 台灣不分色彩均傾聽中肯 郭正亮國內外政治見解...是目前時事評論員之首選，希冀綠色媒體有良知延請 郭正亮受訪 (praises pundit 郭正亮 as fair/non-ideological, wishes green media would invite him)
Sonnet: (all false) | Opus: BNE
**Your call:** OVERRIDE — critical_taiwan=true, all else false. Implies green media excludes fair/balanced voices — a softer version of the "mocking green media as biased" pattern. Opus's BNE has no NATO content.

### 10924
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 建议台湾对米国的台湾政策法立即举行公投，视公投结果决定是和还是梧桐。(suggests a referendum on the Taiwan Policy Act)
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — a procedural suggestion, no explicit US criticism.

### 10927
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 去看看原视频，拜登从头到尾都没有说过出兵二字，他们还号称自己在保卫乌克兰呢，结果呢。反而是台媒这两天全都在说拜登说要出兵。(fact-checks Biden never said "send troops," notes discrepancy with Ukraine claims)
Sonnet: CT | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false. Debunks media hype about US commitment and points out the gap between claimed and actual Ukraine support — both CT (media exaggeration exposed) and DUS (US "claims" but doesn't deliver). Opus's BNE unsupported.

### 10930
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 嘴巴講跟實際行動是兩回事，依照目前美國紀錄，實際開打肯定又是經濟制裁而已 ("Talk and action are different — based on the US's track record, it'll just be sanctions again")
Sonnet: CT, DUS | Opus: BNE
**Your call:** Sonnet — direct skepticism citing track record; Opus's BNE unsupported.

### 10934
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 美國也答應烏克蘭加入北約啊，是天真還是傻，美國不可能參戰啦 ("The US also promised Ukraine NATO membership, naive or stupid, the US won't fight")
Sonnet: CU | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_ukraine=true, disappointment_with_us=true, all else false. Mocks Ukraine's reliance on the broken/unreliable NATO-membership promise as naive (CU) and states the US won't actually fight (DUS). Opus's BNE doesn't fit as well as the broken-promise/non-intervention framing does for DUS.

### 10935
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Thread:** 自己國家自己救啦，成天在那奢望美國來出兵。("Save your own country yourself, quit fantasizing about US troops")
Sonnet: ST | Opus: DUS, BNE
**Your call:** Sonnet — clear self-reliance advocacy is the primary content; Opus's BNE unsupported.

### 10938
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Thread:** 兩蔣建立的團結自信早被李陳馬蔡破壞完了。("The unity/confidence built by the two Chiangs was long ago destroyed by Lee/Chen/Ma/Tsai")
Sonnet: CT | Opus: (all false)
**Your call:** Sonnet — frames modern Taiwan as having lost unity/confidence, fits critical_taiwan's hopeless framing.

### 10939
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Thread:** 美国不帮中华民国是事实！ 国军不行是假话！ 台湾人团结一致反抗中共国是核心价值！("It's a fact the US won't help; it's a lie the military is weak; Taiwanese unity to resist the CCP is our core value!")
Sonnet: ST | Opus: DUS, BNE
**Your call:** OVERRIDE — supportive_taiwan=true, disappointment_with_us=true, all else false. Defends military competence and asserts resistance-unity as core value (ST), while separately stating "US won't help is a fact" (DUS). Opus's BNE doesn't fit.

### 10941
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Thread:** 美国佬不耒了他和巫婆要人命了 (very garbled — "the American won't come, and 'him and the witch' want lives")
Sonnet: (all false) | Opus: DUS, BNE
**Your call:** OVERRIDE — critical_taiwan=true, disappointment_with_us=true, all else false.

### 10942
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Thread:** 台湾无脑愣😬("Taiwan is brainless/reckless")
Sonnet: (all false) | Opus: DUS
**Your call:** OVERRIDE — critical_taiwan=true, all else false. A blunt blanket insult at Taiwan, matching the "blanket dehumanizing insult defaults to critical_taiwan" precedent (cf. id 7897). No US content for Opus's DUS.

### 10953
**Video:** 今日烏克蘭明日台灣？中外交部:「台人蹭熱度碰瓷」｜👍小編推新聞 20220224
**Thread:** 今日烏克蘭.明日台灣.後天外蒙？越南？印度？？？(sarcastically extends the domino-theory slogan to absurd lengths)
Sonnet: ST | Opus: (all false)
**Your call:** Opus — ambiguous sarcasm direction (could be mocking the alarmist framing itself, or something else); default false per the ambiguous-sarcasm calibration note.

### 10956
**Video:** 今日烏克蘭明日台灣？中外交部:「台人蹭熱度碰瓷」｜👍小編推新聞 20220224
**Thread:** 中国在2013年12月向乌克兰提供核安全保证...现在普京核威胁乌克兰，怎么办？ 烏克蘭準備和中國斷交 (notes China's broken nuclear-security guarantee to Ukraine)
Sonnet: ST | Opus: (all false)
**Your call:** Opus — this is about Ukraine-China dynamics, not Taiwan; mostly factual/expository without a clear Taiwan-directed stance, so ST doesn't fit.

### 10957
**Video:** 今日烏克蘭明日台灣？中外交部:「台人蹭熱度碰瓷」｜👍小編推新聞 20220224
**Thread:** 中國看俄國侵略烏克蘭，被經濟制裁及傷亡慘敗，中國肯定不敢發動侵略台灣，百分之一萬不敢。("Seeing Russia hit by sanctions and heavy losses, China definitely won't dare invade Taiwan")
Sonnet: SU, ST | Opus: ST
**Your call:** Sonnet (full row) — predicting Russia's isolation/weakness fits the established supportive_ukraine pattern, on top of the shared ST (deterrence lesson for China).

### 10964
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 大陸是什麼東西啦? 是眼鏡公司? 還是人名? 中國就是中國，大陸是什麼鬼?("What is '大陸' [Mainland]? China is China")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — rejects the "Mainland" euphemism implying unity, asserting Taiwan's distinct identity.

### 10965
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看｜TVBS新聞
**Thread:** 人死光了經濟制裁有屁用? 一句話會不會出兵就好 ("What's the use of sanctions once everyone's dead? Just say if you'll send troops")
Sonnet: CT | Opus: BNE
**Your call:** Sonnet — dismisses sanctions-only support as insufficient, demanding real commitment; fits critical_taiwan skepticism pattern. Opus's BNE unsupported.

### 10978
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 美國來的層級越來越高，跟5年前差好多。("US delegation seniority keeps rising, very different from 5 years ago")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — mild positive observation of strengthening alliance engagement.

### 10979
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 不用期待。把武器給我們就好 ("Don't expect more. Just give us the weapons")
Sonnet: ST | Opus: DUS, BNE
**Your call:** OVERRIDE — supportive_taiwan=true, disappointment_with_us=true, all else false. Pragmatic self-reliance focus (ST) plus resigned realism about limited US commitment (DUS). Opus's BNE doesn't fit.

### 10983
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Thread:** 遙遠的美國，一直來搧風點火...我要和平，不要單方面說大陸一直要武統，想想我們也是一直在挑釁...不要拿生命開玩笑 (accuses US of stoking conflict, but also acknowledges Taiwan's own provocations, wants peace)
Sonnet: DUS | Opus: CT, DUS
**Your call:** Sonnet (DUS only) — a genuinely balanced peace-appeal acknowledging both sides' provocations, matching the precedent (cf. id 5660) that a balanced appeal doesn't default to critical_taiwan just for advocating de-escalation.

### 10984
**Video:** 借鏡烏克蘭 台灣能靠自己？獨撐戰局VS.堅守待援#我們這麼說
**Thread:** 哈哈哈，俄罗斯用的可是二战武器在玩 ("Haha, Russia is playing with WWII-era weapons")
Sonnet: SU | Opus: CT
**Your call:** Sonnet — mocking Russia's equipment as obsolete = mocking its military decline, established supportive_ukraine pattern; Opus's CT is a mismap (no Taiwan content).

### 10994
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 世界 沒有 中共 世界會 更美好！("World without the CCP, the world would be better!")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — direct anti-CCP sentiment in a Taiwan-defense-context video.

### 10995
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 搞這些也是沒實質意義因為都是說說沒有任何協議 主要就是要挑撥地區 跟網內互打。這套老美常做的事情 ("This has no substance, just talk with no agreement, mainly to stir discord — this is what the US often does")
Sonnet: CT, DUS | Opus: BNE
**Your call:** Sonnet — explicit accusation the US stirs discord (DUS) plus dismissing the gesture as empty (CT); Opus's BNE unsupported.

### 10997
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習｜TVBS新聞
**Thread:** 美國出兵嗎，沒出兵就只是出張嘴，可以不負任何責任 ("Will the US send troops? If not, it's just talk without accountability")
Sonnet: CT | Opus: BNE
**Your call:** Sonnet — direct skepticism of troop commitment; Opus's BNE unsupported.

### 11015
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...@中天新聞CtiNews
**Thread:** 俄罗斯放话给中印面子，提前放出停战的意思，先要站在道德制高点上，如果欧盟再支持乌克兰，那冬天制裁欧洲就不愿俄罗其斯了。(analytical description of Russia's diplomatic/gas-leverage strategy)
Sonnet: (all false) | Opus: SU
**Your call:** Sonnet — purely descriptive/analytical about Russian strategy, no clear pro-Ukraine solidarity or anti-Russia condemnation; Opus's SU is a stretch.

---

## Summary of calls

- Sonnet (full row): 76 ids
- Opus (full row): 10 ids
- Explicit override (hybrid or all-false): 30 ids
- UNSURE: 1 id (10941)

## Notable patterns this batch

- **Recurring "skepticism of empty US promises" cluster**: a large share of overrides pair critical_taiwan with disappointment_with_us on comments that dismiss "rock solid"/"co-defense" rhetoric as hollow talk without real troop commitment (ids 10692, 10694, 10698, 10765, 10768, 10775, 10804, 10829, 10832, 10847, 10905, 10915, 10927, 10939, 10979). Sonnet consistently caught the CT half; Opus consistently caught DUS but frequently mislabeled the second half as `blame_nato_expansion` instead — worth a possible calibration note: **Opus this batch had a strong tendency to over-apply `blame_nato_expansion` to Taiwan-only skepticism-of-US-commitment comments that have zero NATO/Russia content.** This happened at least 20+ times (e.g. 10453, 10490 wait not applicable, 10514... — see the many "Opus's BNE unsupported" notes above). If this recurs in future Opus runs, worth flagging explicitly in the Opus labeling prompt to double-check BNE actually requires a NATO-expansion-as-cause argument, not just general skepticism/distrust content.
- **One exclusivity-rule violation found in Opus's raw run:** id 10810 has Opus's row with both `critical_taiwan=1` AND `supportive_taiwan=1` simultaneously, violating the stated mutual-exclusivity rule. Worth a quick DB-wide check for other such violations in this run before finalizing.
- **New calibration-note candidate:** mocking/attacking Taiwanese green media (三立/民視/自由) for bias by *implication* (e.g. "green media excessively fawns," or "wish green media had the conscience to invite [a fair pundit]") should extend the existing "mocking green media as biased/fake news" critical_taiwan note even when the comment doesn't explicitly call them "fake news" (ids 10453, 10677, 10785, 10923).
- **Ukraine-as-sacrificed-proxy pattern recurs**: several ids frame Ukraine as having been "used"/"harmed"/"told to die alone" by the US, extending the existing critical_ukraine proxy-war framing (ids 10655, 10666, 10673, 10730, 10902, 10934).
