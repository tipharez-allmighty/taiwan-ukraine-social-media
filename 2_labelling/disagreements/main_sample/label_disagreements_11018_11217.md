# Label disagreements: ids 11018-11217

55 disagreements out of 200 labeled rows (Sonnet run_number=1 vs Opus run_number=2). All 55 rows in this range are `row_type='thread_only'` (standalone top-level comments, no reply chain) — the labeled text is `thread_text_original` itself, shown below as **Comment**.

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion. Only labels set to true are listed per model; anything not listed is false for that model.

---

### 11018
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Comment:** 会不会派兵来台保护，只有开战才知道 ("Whether they'll send troops to protect Taiwan — we'll only know once war breaks out")
Sonnet: (all false) | Opus: CT, DUS
**Your call:** Opus — near-verbatim match to the critical_taiwan definition's "skepticism the US would actually intervene," plus distrust.

### 11019
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Comment:** 歡迎美國團來台拿苦苦回去 ("Welcome the US delegation to Taiwan, [may they] take the bitterness back")
Sonnet: (all false) | Opus: DUS
**Your call:** Sonnet — genuinely ambiguous phrasing, no clear distrust/betrayal statement articulated; default false per the sarcasm-ambiguity calibration note.

### 11020
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Comment:** 🇺🇸❤️🇹🇼 👍👍👍
Sonnet: (all false) | Opus: ST
**Your call:** Sonnet — bare flag-heart emoji doesn't assert defense/resolve content or a named target; too thin per the supportive_taiwan substantive-content bar.

### 11023
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Comment:** 老共给了你们14亿的贸易顺差 你们给他钱💰他们公关团队来台照顾你们下次生意 生意场这很正常嘛 你们不要矮化台湾 台湾才是美国的爸爸 ("China gave you a $1.4B trade surplus... don't demean Taiwan, Taiwan is actually America's daddy")
Sonnet: CT | Opus: CT, DUS
**Your call:** Sonnet — mocks the "Taiwan needs US protection" framing as self-demeaning (critical_taiwan), but doesn't articulate actual distrust/betrayal of the US; Opus's DUS is a stretch.

### 11025
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Comment:** 美國要選舉了，聽聽就好 ("The US has elections coming, just take it with a grain of salt")
Sonnet: DUS | Opus: CT, DUS
**Your call:** Opus — dismissing US promises as election-year rhetoric is skepticism-of-commitment (critical_taiwan) on top of the distrust; Sonnet's DUS-only misses the CT angle.

### 11027
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Comment:** 還邀另一個國家來壯膽，他們的艦故障嗎？ ("Also invited another country along for courage — are their ships broken?") [re: US+Canada joint patrol]
Sonnet: CT | Opus: DUS
**Your call:** Sonnet — mocks the patrol's credibility as toothless symbolism, fitting the "skepticism of actual commitment" reading; no explicit distrust/betrayal language for DUS.

### 11030
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Comment:** 台灣民眾真的很無知 美軍 沒有利益 的事情他們不會做的 有種美軍 駐防在台灣 這樣才可以相信美軍真的做得到 ("Taiwanese are ignorant — US military won't act without benefit; if US troops actually station in Taiwan, then I'd believe it")
Sonnet: DUS | Opus: CT, DUS
**Your call:** Opus — matches the established "demand proof via troop stationing" pattern (see id 10494 precedent) = critical_taiwan + disappointment_with_us.

### 11031
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Comment:** 你們感謝美國什麼 美國只會放屁 美國有種著軍在台灣 不要 一直在那邊放屁 ("What are you thanking the US for, US only talks BS — if they have guts, station troops in Taiwan")
Sonnet: DUS | Opus: CT, DUS
**Your call:** Opus — same demand-proof pattern as 11030, plus explicit dismissal of gratitude toward the US.

### 11039
**Video:** 今日烏克蘭明日台灣？中外交部:「台人蹭熱度碰瓷」
**Comment:** 這就是去武求和的下塲 ("This is the result of disarming and seeking peace")
Sonnet: (all false) | Opus: ST
**Your call:** Opus — reads as a motivating warning against disarmament (implicitly citing Ukraine's fate), applicable as a lesson for Taiwan's own defense posture.

### 11041
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 說得很好！加油！！！ ("Well said! Keep it up!!!")
Sonnet: (all false) | Opus: ST
**Your call:** Sonnet — bare cheering without restating any substantive content, too thin per the terse-reply-carries-no-independent-stance pattern.

### 11042
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 愛台論，台灣可能輸在賄美 ("Pro-Taiwan-ism — Taiwan might lose because of bribing the US")
Sonnet: DUS | Opus: CT, DUS
**Your call:** Opus — critiques Taiwan's reliance-on-purchased-support strategy as a losing approach (critical_taiwan) and implies the relationship is transactional/corrupt (DUS).

### 11043
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 台湾人垃圾论！ ("Taiwanese-people-garbage theory!")
Sonnet: (all false) | Opus: CT
**Your call:** Sonnet — too vague/terse a fragment to connect to any specific frame; Opus's CT unsupported.

### 11044
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 美国佬会来为你台湾而战，醒醒吧。 ("Americans will fight for you Taiwan? Wake up.")
Sonnet: CT | Opus: CT, DUS
**Your call:** Opus — explicit "wake up" carries both skepticism of US commitment (CT) and distrust/betrayal framing (DUS).

### 11047
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 最近多了，有美女牌，菜市場牌，夜市牌，再玩下去，福建省會先要求民主，反正以其人之道反制其人，她請我們去，我們請她來 (satirical riff on election-candidate nicknames, joking about promoting democracy in Fujian tit-for-tat)
Sonnet: (all false) | Opus: ST
**Your call:** Sonnet — satirical domestic-politics wordplay without substantive defense content or a named target; Opus's ST unsupported.

### 11056
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看
**Comment:** 祖國不用怕，有國民黨內奸在團結亂台灣，武統還是有希望的 ("Motherland needn't fear — KMT traitors within are sowing discord in Taiwan, forced unification still has hope")
Sonnet: CT | Opus: ST
**Your call:** Sonnet — a pro-unification voice ("祖國") cheering 武統 and *praising* KMT as useful collaborators is squarely critical_taiwan; Opus's ST is backwards — the KMT is being praised here, not criticized, and by a pro-China voice.

### 11058
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看
**Comment:** 關台灣屁事，聯合國有給台灣荒唐偉遊說費嗎莫名其妙？ ("None of Taiwan's business, did the UN give Taiwan some absurd lobbying fee? Bizarre")
Sonnet: (all false) | Opus: CT
**Your call:** Sonnet — garbled/unclear reference, not clearly connected to any of critical_taiwan's specific criteria.

### 11060
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看
**Comment:** 两天，哈哈😄，西方新闻真搞笑，不会说一天 ("Two days, haha, Western news is so funny, why not just say one day")
Sonnet: (all false) | Opus: CU
**Your call:** Opus — mocks Western media's (wrong) predictions of a quick Russian collapse as a joke, undercutting the Ukraine/West-favorable narrative = critical_ukraine per the "sarcastically undercuts the winning narrative" pattern.

### 11061
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Comment:** 中国对这群无耻的东西没必要客气，中国维护藏南主权，不见他们影子；中国在钓鱼岛维权，看不到他们的影子；中国在南海维权看不到他们的影子；抓大陆渔民积极的很，比日本人都积极 (pro-China rant that Taiwan is selectively active — cracking down on mainland fishermen but absent on Tibet/Diaoyu/South China Sea sovereignty issues)
Sonnet: (all false) | Opus: CT
**Your call:** OVERRIDE — all false. Tangential pro-China grievance about fishermen/sovereignty disputes; doesn't argue capitulation, mock defense preparedness, or touch US reliability — doesn't substantively engage any of the 6 frames.

### 11065
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Comment:** 我服役的時候，要碰到機槍是在士官訓時後 ("When I served, the only time I got to touch a machine gun was during NCO training")
Sonnet: (all false) | Opus: CT
**Your call:** Opus — anecdote illustrating inadequate/limited weapons training implicitly mocks Taiwan's defense preparedness.

### 11069
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習
**Comment:** 阿共快來啊!!台灣東岸聯合軍演如果不小心沉了飛機掉了，可能連人在哪都找不到喔..如果到時候又不敢飛越台灣救人!! 那就真的好笑了!! ("Come on CCP!! ...if they don't even dare fly over Taiwan to rescue people, that'd be hilarious!!")
Sonnet: (all false) | Opus: ST
**Your call:** Opus — "阿共快來啊" defiant taunt plus mocking PLA's presumed cowardice fits the defiant-dare resolve pattern = supportive_taiwan.

### 11071
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習
**Comment:** 中共：汪汪汪 ("CCP: woof woof woof")
Sonnet: ST | Opus: (all false)
**Your call:** Opus — generic "all bark" mockery of the CCP without a named target (五毛/小粉紅/馬英九/鄭麗文) or substantive defense content, too thin per the calibration bar; Sonnet's ST doesn't meet it.

### 11075
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習
**Comment:** 連塔利班多打不贏的貨色天天自hi ("Can't even beat the Taliban, this pathetic bunch hypes itself up daily")
Sonnet: DUS | Opus: CT, DUS
**Your call:** Opus — mocking the US's Afghanistan failure as proof of unreliability ties to both skepticism of US capability to actually help Taiwan (CT) and the Afghanistan-whataboutism pattern (DUS).

### 11079
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...
**Comment:** 话说回来，美国的国内法律对海外的台湾有啥用呢？想多了想多了，喝酒喝酒 ("What use is US domestic law for overseas Taiwan? Overthinking it, let's just drink")
Sonnet: DUS | Opus: CT, DUS
**Your call:** Opus — questioning whether US legal commitments (e.g. the Taiwan Relations Act) have real teeth is skepticism of actual US intervention (CT), plus the dismissive distrust (DUS).

### 11081
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...
**Comment:** 牠媽媽的，還是只考慮選舉，都不去慰問災民 ("Damn it, still only thinking about elections, not even visiting disaster victims") [re: Tsai visiting Tzu Chi instead]
Sonnet: (all false) | Opus: CT
**Your call:** Opus — criticizes Tsai/DPP for prioritizing political optics over disaster relief, fits "mocks the DPP" criterion.

### 11083
**Video:** 【#綠也掀桌 互動LIVE】拜登4度承諾美軍協防台灣...
**Comment:** 鯊入亮點 為你解析點評...感謝 亮哥 精闢的解析 希望台灣人能夠醒醒 真正的來面對問題... (fan praise for a 中天 talk-show host, hoping "Taiwanese people wake up and truly face the problem")
Sonnet: (all false) | Opus: CT
**Your call:** Opus — praising a 中天 pundit's "wake up and face the problem" message echoes the capitulation-adjacent fatalism associated with that channel per prior calibration.

### 11089
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Comment:** 一打仗就跑了 ("As soon as war breaks out, they'll [the US] run")
Sonnet: CT | Opus: CT, DUS
**Your call:** Opus — direct claim the US will flee once war starts is both classic skepticism-of-commitment (CT) and distrust (DUS).

### 11091
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Comment:** 看起來是很有一回事，但是基本上我不認為匪國敢在這個時間點攻擊...而美國這時候要大選正是打台灣牌的時候，反正美國發戰爭財也不是一兩天了...有了俄羅斯的例子，我看席皇帝應該是不會硬來啦 (long geopolitical analysis; includes "美國發戰爭財" — the US profits from war)
Sonnet: ST | Opus: DUS
**Your call:** Opus — "美國發戰爭財" (US profits from war) is a direct match to the "US profits from war" → disappointment_with_us pattern; no clear supportive_taiwan content (no defense-buildup, resolve, or named-target).

### 11092
**Video:** 美軍協防台灣立即有動作!...三立新聞台
**Comment:** 這種才是非盟友勝似盟友，台美友誼無上限 台灣不用像日韓一樣，每年要繳百億的保護費就能得到相同的待遇 另外那個被吞了海參崴的非盟友勝似盟友，中俄友誼無上限然後布丁打仗維尼瑟瑟發抖 (praises US-Taiwan alliance value; separately mocks Russia having lost Vladivostok to China, and Putin fighting while Xi "trembles")
Sonnet: SU, ST | Opus: ST
**Your call:** Opus — clear ST (praising the US-Taiwan alliance's value). The Vladivostok/Putin-Xi riff mocks Sino-Russian territorial history and Xi's fear, not Ukraine's war specifically — Sonnet's SU is unsupported.

### 11093
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 台灣內賊太多 ("Too many internal traitors in Taiwan")
Sonnet: CT | Opus: ST
**Your call:** Opus — "內賊" is the standard term for domestic pro-China collaborators (a common trope), matching the "criticizes collaborators" pattern even without naming KMT specifically.

### 11094
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 烏克蘭只有一個字形容就是慘，選有智慧和前瞻的領導人，才是最重要的！！ ("Ukraine in one word: tragic. Choosing a wise, forward-looking leader is what matters most!!")
Sonnet: CU | Opus: CU, CT
**Your call:** Opus — clearly critical_ukraine (frames Ukraine's outcome as tragic, implicitly blaming leadership); the "choose wise leaders" framing also functions as a fatalistic "next Ukraine" warning extended to Taiwan, fitting CT too.

### 11096
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 國內有人想消滅中華民國～這個就是在打擊國家認同感～ ("There are people at home who want to destroy the ROC — this undermines national identity")
Sonnet: (all false) | Opus: CT
**Your call:** Sonnet — ambiguous domestic identity-politics complaint (unclear who "wants to destroy the ROC"), doesn't clearly engage capitulation/DPP-mockery/US-skepticism criteria; Opus's CT is a stretch.

### 11103
**Video:** 今日烏克蘭明日台灣？中外交部:「台人蹭熱度碰瓷」
**Comment:** "今日烏克蘭，明日台灣"，可是川普先說的喔，龐培歐訪台時，可以問問他怎麼詮譯他前老板的這句話嗎？😂😂😂 (needling that Trump said this phrase first, ask Pompeo to explain his ex-boss's words)
Sonnet: (all false) | Opus: DUS
**Your call:** Opus — the Trump/Pompeo-inconsistency "gotcha" implies distrust of the sincerity/reliability of US political commitment.

### 11108
**Video:** 今日烏克蘭明日台灣？中外交部:「台人蹭熱度碰瓷」
**Comment:** 把817赶下海！ ("Drive the 817 into the sea!") [817 = derogatory slang for DPP supporters]
Sonnet: (all false) | Opus: CT
**Your call:** Opus — "817" is established derogatory slang for DPP/green-camp supporters; hostile jab fits "mocks the DPP" criterion.

### 11117
**Video:** 美要台灣自我防衛 學者籲修法:戰時高官不得落跑
**Comment:** 这个支持。。。。 ("I support this....")
Sonnet: ST | Opus: (all false)
**Your call:** Sonnet — unlike a neutral terse fact-confirmation, this explicitly endorses the video's specific self-defense/wartime-accountability policy, which is substantive ST content even though terse.

### 11118
**Video:** 美要台灣自我防衛 學者籲修法:戰時高官不得落跑
**Comment:** 自我防衛就是再花大錢買武器 ("Self-defense just means spending more big money buying weapons")
Sonnet: CT | Opus: DUS
**Your call:** Opus — frames "self-defense" cynically as just US arms purchases, matching the "profits from arms sales" pattern → disappointment_with_us; doesn't clearly argue defense is hopeless (which would be CT).

### 11124
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Comment:** 这5⃣️个人这次出场费台湾付出5⃣️亿美金，超值？ ("These 5 people, this appearance fee — Taiwan paid $500M USD, worth it?")
Sonnet: DUS | Opus: CT, DUS
**Your call:** Opus — sarcastic "worth it?" casts doubt on whether the payment yields real security benefit (CT) while also framing the visit as transactional/for-profit (DUS).

### 11132
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Comment:** 你看的比國軍那批將領透徹 ("You see things more clearly than that bunch of ROC generals")
Sonnet: (all false) | Opus: CT
**Your call:** Opus — implicitly mocks ROC military leadership as less capable/insightful than a random commentator, fits mocking Taiwan's defense preparedness.

### 11147
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看
**Comment:** 今日狗頭普丁明日的小熊維尼習近平 ("Today's dog-head Putin, tomorrow's Winnie-the-Pooh Xi Jinping")
Sonnet: SU, ST | Opus: ST
**Your call:** Sonnet — derogatory mockery of Putin ("dog-head") is anti-Russia sentiment (SU), and predicting Xi will follow Putin's failed path is anti-China sentiment (ST); Opus's ST-only misses the clear Putin-mockery component.

### 11151
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習
**Comment:** 中共緊張甚麼? 人家來收保護費而已 ("What's the CCP so nervous about? They're just here to collect protection money")
Sonnet: CT, DUS | Opus: DUS
**Your call:** Sonnet — the "protection racket" framing both casts doubt on whether the visit represents genuine commitment (CT) and frames it as transactional (DUS); Opus's DUS-only misses the CT skepticism component.

### 11154
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習
**Comment:** 解放軍怎麼還不把沉玉針收回去呢？ 真是令倫耽心啊！ (garbled/unclear reference)
Sonnet: ST | Opus: (all false)
**Your call:** Opus — text is too garbled/unclear ("沉玉針"/"令倫" don't resolve to a clear referent) to confidently support any label.

### 11155
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習
**Comment:** 對啦, 最會是演習, 永遠不敢真打. 俄羅斯最起碼會真打不會嘴炮 ("Yeah right, always just drills, never dares to actually fight. Russia at least would actually fight, not just talk")
Sonnet: ST | Opus: CT
**Your call:** OVERRIDE — all false. Compares China's threat credibility (dismissed as bluster) against Russia's, without substantively arguing Taiwan's own defense posture (ST) or framing Taiwan's situation as hopeless (CT) — neither definition cleanly fits a comment about relative adversary resolve.

### 11161
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 有你們真好加油 ("It's great having you all, keep going")
Sonnet: (all false) | Opus: ST
**Your call:** Sonnet — bare generic encouragement without restating substantive content, too thin per the terse-cheering pattern.

### 11163
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 打起来你先上呃 ("If it comes to fighting, you go first")
Sonnet: (all false) | Opus: CT
**Your call:** Opus — mocks the sincerity of resistance talk (implying the speaker/addressee wouldn't actually fight), undermining the resolve narrative = mocks Taiwan's defense preparedness.

### 11166
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 台灣會輸的最大一個點就是認知～ ("The biggest reason Taiwan will lose is 'cognition' [cognitive warfare/mindset]")
Sonnet: CT | Opus: ST
**Your call:** Sonnet — explicitly predicts Taiwan *will lose*, textbook fatalistic framing = critical_taiwan; Opus's ST misreads this as resolve when it's actually predicting defeat.

### 11174
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Comment:** 先赢过宇宙神国印度再说吧。 ("Beat the 'cosmic god-nation' India first before you talk") [internet meme mocking Indian nationalist hype]
Sonnet: (all false) | Opus: CT
**Your call:** Sonnet — off-topic meme-mockery of India, not substantively about Taiwan's defense preparedness; Opus's CT is a stretch.

### 11177
**Video:** 國軍的不對稱作戰計畫 傳統軍力被輾壓怎麼辦?
**Comment:** 台湾第一啦😂！第一不好吗？干嘛你要说自己成第二😂😂😂，说成第一不是更好吗😂😂 ("Taiwan is #1 lol! What's wrong with #1? Why say you're #2, isn't #1 better?")
Sonnet: (all false) | Opus: CT
**Your call:** Opus — sarcastic "why settle for #2" mocks a military-weakness ranking joke, fitting mockery of Taiwan's defense preparedness.

### 11189
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Comment:** 0 利益關係 ("0 conflict of interest")
Sonnet: DUS | Opus: (all false)
**Your call:** Sonnet — sarcastic "0 conflict of interest" implies distrust that the US visit is genuinely disinterested, matching the same cynical-transactional-motives pattern as neighboring comments in this thread (11124, 11151).

### 11191
**Video:** #iNEWS最新 抵台了！美國特使團閃電訪台30小時...三立iNEWS
**Comment:** 乌克兰没利用价值了，在再来忽悠一下台湾，派了一帮卖军火的过来，美国掺合过的地方哪个和平了 ("Ukraine has no more use value, now come deceive Taiwan too — sent a bunch of arms dealers, wherever the US gets involved, is anywhere ever peaceful?")
Sonnet: CT, DUS | Opus: CU, CT, DUS
**Your call:** Opus — explicitly frames Ukraine as a discarded US proxy (CU), Taiwan as the next target of deception (CT), and general anti-US whataboutism (DUS) — all three cleanly match.

### 11201
**Video:** 今日烏克蘭.明日臺灣? 美CIA局長:制裁俄國給大陸看
**Comment:** 反制裁三步走...三十五年，楚伐随。随曰：我无罪。楚曰：我蛮夷也。 (details Russia's counter-sanctions, closes with a classical allusion where "Chu" tells "Sui" that as a "barbarian" it isn't bound by convention — a might-makes-right justification)
Sonnet: (all false) | Opus: CU
**Your call:** Opus — approvingly details Russia's retaliatory measures and closes with a classical allusion normalizing might-makes-right aggression, favoring/justifying Russia's posture.

### 11204
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 台灣為誰而戰？民進黨嗎？美國嗎？超限戰爭來臨時台灣還有剩下多少人？ ("Who does Taiwan fight for? The DPP? The US? When unrestricted warfare comes, how many Taiwanese will be left?")
Sonnet: CT | Opus: CT, DUS
**Your call:** Opus — questioning whether Taiwan fights "for the US" implies the resistance serves US interests rather than Taiwan's own (proxy-war distrust) = DUS, in addition to the clear fatalism (CT).

### 11206
**Video:** 🔥提防中共對台心理戰：美國棄台論 台軍無能論！
**Comment:** 以前我也相信民主制度是普世價值...美國英國陸續走上民粹政治...但民主集中制的中國與新加坡卻是一個成效良好的實驗...我寧願不要 (long argument: disillusioned with Western democracy's inequality/populism, praises China/Singapore's "democratic centralism" as better)
Sonnet: CT | Opus: DUS
**Your call:** OVERRIDE — CT and DUS both true. Praising China/Singapore's authoritarian governance as superior to Western democracy is a capitulation-adjacent ideological argument for the CCP system's legitimacy (CT), while the extended critique of US political dysfunction (inequality, populism, unfit leaders) is general moral condemnation of the US as an actor, per the anti-US-whataboutism principle (DUS) — both models caught one half each.

### 11212
**Video:** 徐巧芯要台灣借鏡烏克蘭 王定宇批：無視侵略者霸凌
**Comment:** 徐巧芯若是妳已離婚要改嫁...惹怒前夫不爽要殺妳.徐巧芯妳覺得可以這樣? (divorce/ex-husband analogy defending "aggression isn't justified by provocation," aimed at KMT legislator 徐巧芯)
Sonnet: SU | Opus: SU, ST
**Your call:** Opus — the analogy squarely defends the anti-aggression framing (SU); it's also a direct, pointed rebuttal aimed at a named KMT legislator, fitting the "criticizes KMT" component of ST.

### 11214
**Video:** 徐巧芯要台灣借鏡烏克蘭 王定宇批：無視侵略者霸凌
**Comment:** 肖查某 (crude Hokkien insult, ~"crazy woman")
Sonnet: (all false) | Opus: ST
**Your call:** Sonnet — bare crude insult toward a KMT figure not in the specific named-target list (五毛/小粉紅/馬英九/鄭麗文), with no collaboration-content substance; too thin per the generic-mockery bar.

### 11216
**Video:** 徐巧芯要台灣借鏡烏克蘭 王定宇批：無視侵略者霸凌
**Comment:** 烏克蘭人為啥會要抗俄保烏??...美國和英國，卻對此袖手旁觀...會怕的都是那些專制的獨裁政權! (defends Ukraine's alliance-seeking as justified given US/UK stood by during Crimea 2014, violating the Budapest Memorandum)
Sonnet: SU | Opus: SU, DUS
**Your call:** Opus — explicitly criticizes the US (Budapest Memorandum signatory) for standing by and doing nothing during Crimea 2014, textbook distrust of US commitment reliability, on top of the clear SU content.

### 11217
**Video:** 美議員來訪:棄台是放縱槍桿子統治 共軍嗆:將在台周邊海空演習
**Comment:** 玩了烏克蘭還要玩台灣....哼 ㄎㄨㄣˇ ("Played/used Ukraine, now want to play/use Taiwan too... hmph")
Sonnet: CT, DUS | Opus: CU, CT, DUS
**Your call:** Opus — "玩了烏克蘭還要玩台灣" frames Ukraine as a used-up US pawn (CU) and Taiwan as the next target (CT), plus general distrust of US manipulation (DUS) — same three-label pattern as the near-identical id 11191.
