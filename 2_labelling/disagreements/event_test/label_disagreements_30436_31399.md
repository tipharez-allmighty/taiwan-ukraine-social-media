# Disagreement Review: ids 30436–31399 (event test, batch 7)

500 rows labeled, 435 agreed (87.0%), 65 disagreements below. Run 1 = `claude-sonnet-5`, run 2 = `claude-opus-5`. Only non-Simplified event-test comments. Disagreement rows: 32 thread_only, 33 thread_with_comment.

| Video | Title | Rows | Disagreements |
|---|---|---|---|
| `3Rn2T10z0uQ` | 未來戰場新形態？機器狗大戰無人機#機器狗 #無人機 #煙花 #中國 | 17 | 2 |
| `3_70nSb3UFA` | 黎智英兒子赴美國國會作證 呼籲不要讓香港欺騙全世界/他不是作奸犯科入罪 是為普世價值的公理坐牢｜20230519｜ @taiwanplus0709 ​ | 117 | 7 |
| `3hjt3AAVyKo` | 美國不可能棄台軍備要什麼給什麼 SIA主席：拜登花兩年發現台灣無可取代！  【關鍵時刻】20230418-2 劉寶傑 黃世聰 吳子嘉 | 8 | 1 |
| `445U-unDGFo` | 俄方入侵烏克蘭14個月後 俄羅斯人生活有何變化？－ BBC News 中文 | 358 | 55 |

Legend: CU=critical_ukraine, SU=supportive_ukraine, CT=critical_taiwan, ST=supportive_taiwan, DUS=disappointment_with_us, BNE=blame_nato_expansion. Bold = the labels where the runs differ.

Precedent used for "Your call": your batch 1–6 decisions and `labeling_prompt.md`, plus your final labels in full_data.db: 小粉紅/五毛 named → ST; pure 黃俄/黃鵝 jabs → false; NATO-provocation comments → BNE, with CU only when Ukraine itself is blamed; mocking US arms promises on `3hjt3AAVyKo` → DUS.

My calls: 50 Opus, 12 Sonnet, 3 other. 49 marked **Borderline**.

**Main patterns.**
- **BBC video on Russian life 14 months into the war (`445U-unDGFo`, 46 of 65).** Sonnet marked mockery of Russia's *domestic* system (brainwashing, censorship, 極權, seized Western firms) as SU; Opus left it false. The SU definition is about the war (solidarity, condemning the invasion, Russia's decline), so I took Opus (false). I did take SU where the comment is about the war going badly for Russia or Russia's decline (30791, 30803, 30935).
- **NATO comments.** Opus adds CU to plain "NATO provoked Russia" comments; Sonnet gives BNE only. You set CU on about half of your BNE rows in full_data.db, mostly when Ukraine is blamed or called a proxy. I took BNE only unless Ukraine itself is blamed (31238 → CU). I also added DUS where the US is condemned (31119, 31121).
- **黎智英 / Hong Kong video (`3_70nSb3UFA`).** It's not about Ukraine, but it stays in the test, so I applied the Taiwan labels: "try that in Taiwan and see" jabs at Taiwan's democracy → CT, pro-CCP/Xi → CT.
- **Possible off-topic videos.** `3_70nSb3UFA` (黎智英's son testifies to Congress, 117 rows) and `3Rn2T10z0uQ` (robot dog vs drones, 17 rows) aren't about Ukraine or Taiwan's war risk. Neither is in the 15 deleted videos. The robot-dog video is in your full_data.db labels (85 rows). I haven't changed anything — your decision.


**Removed after this file was written:** the robot-dog video (`3Rn2T10z0uQ`) was deleted from the DB on 2026-10-07 (see article/EVENT_TEST_PLAN.md, Change 3), including 2 of the rows below (30436, 30455). Batch 7 is now 483 rows: 420 agreed + 63 calls (48 Opus, 12 Sonnet, 3 other). The 黎智英 video was kept.

---

### id 30436
**Video:** `3Rn2T10z0uQ`
**Thread (context):** 蟾蜍不敢看这种片，看完会难受一整天😅
**Comment:** @zhicai1165  好了啦，軍式研發團隊資金都拿去養小三了，還跟養雞養狗的^_^。
**Translation:** (reply to '蟾蜍 can't bear to watch this') Fine, the military R&D money all went to mistresses, and they raise chickens and dogs ^_^

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Retort mocking China's robot-dog / PRC side → ST, as in batch 4 retorts.

---

### id 30455
**Video:** `3Rn2T10z0uQ`
**Thread (context):** 戰爭最好是這樣，誰的機器人輸誰輸，但台灣的政客一定會讓老百姓出戰，然而自己卻跑到美國
**Comment:** 對丫 所以怕死就舔共
**Translation:** (thread: Taiwan's politicians will send ordinary people to fight and flee to the US) Right — so if you're scared of dying, just suck up to the CCP.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Sarcastic jab at the capitulation logic → ST. Could be read as agreement; weak.

---

### id 30495
**Video:** `3_70nSb3UFA`
**Thread:** 就係因為有法治先會拉你個撲街佬豆好嘛，到處去搵人搞亂香港，你試下係美國搞吖，當場打成蜂竇啊。
**Translation:** It's because of rule of law that you get arrested… try making trouble in the US, you'd be shot full of holes on the spot.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Anti-US whataboutism (US violence) as a counterpoint → DUS per prompt rule.

---

### id 30543
**Video:** `3_70nSb3UFA`
**Thread:** 偏偏還有許多滯台華人很嚮往這種生活
**Translation:** Yet many 'Chinese stranded in Taiwan' still long for this kind of life.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — Mocks pro-PRC people in Taiwan (collaborator-type target) → ST.

---

### id 30550
**Video:** `3_70nSb3UFA`
**Thread:** 台灣狗官更可惡，只要買玩具槍零件，就可以當改造槍械集團，申請搜索票，抓人收押，直接消滅台毒叛亂份子
**Translation:** Taiwan's dog officials are worse… they arrest people for buying toy-gun parts, wiping out 'Taiwan-poison rebels'.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Attacks Taiwan's government, 台毒 = PRC term → CT.

---

### id 30552
**Video:** `3_70nSb3UFA`
**Thread (context):** 沒有共產黨，就没有「新香港」…… 美麗新香港😢😢😢🤮🤮🤮
**Comment:** 沒有西方列強， 世界就會好！
**Translation:** (reply to 'no CCP, no new Hong Kong 🤮') Without the Western powers, the world would be fine!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Anti-'Western powers' (US implied, not named) → DUS. Opus flagged this pattern itself.

---

### id 30558
**Video:** `3_70nSb3UFA`
**Thread:** 是嗎？中共吃飽沒事做抓你？為何不抓我？中國共產黨不是以前的共產黨！我長越大我越支持共產黨。支持習近平
**Translation:** The older I get the more I support the Communist Party. Support Xi Jinping.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Open support for CCP/Xi → CT.

---

### id 30595
**Video:** `3_70nSb3UFA`
**Thread:** 犯了法，扮無辜就想不用負責，還好意思出來講話。試試在台灣造謠亂駡政府，看看會不會被查水錶😂😂😂
**Translation:** Breaks the law, plays innocent… Try spreading rumours and cursing the government in Taiwan and see if the police come 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Discredits Taiwan's democracy as no better than HK → CT.

---

### id 30609
**Video:** `3_70nSb3UFA`
**Thread:** 你現在在台灣搞推翻民進黨試試看吧！
**Translation:** Try overthrowing the DPP in Taiwan now!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — **Borderline** — Same pattern as 30595 → CT.

---

### id 30628
**Video:** `3hjt3AAVyKo`
**Thread (context):** 哈哈哈，可憐喔！萊豬吃多了,開始幻想了,要甚麼給甚麼,
**Comment:** ​@小豆-t2n有夢最美，萊豬少吃點吧！
**Translation:** (thread mocks 'US will give whatever we want') Dreams are the most beautiful — eat less ractopamine pork!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 1 | 0 | **0** | 0 |
| Opus | 0 | 0 | 1 | 0 | **1** | 0 |

**Your call:** Opus (CT + DUS) — Mocks the promise of US arms → CT + DUS. Matches your labels on this video in full_data.db (又要劃大餅 → DUS).

---

### id 30660
**Video:** `445U-unDGFo`
**Thread (context):** 相信正義的一方會贏！💪
**Comment:** 其實二戰德國士兵也認為自己是正義的  一個德國老兵在戰後40年接受訪問  它拿起槍作戰就是希望能建立新秩序  為正義真理而戰
**Translation:** (reply to 'justice will win 💪') WWII German soldiers also thought they were the just side…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Sarcasm direction unclear (Russians or Ukrainians?) → false.

---

### id 30667
**Video:** `445U-unDGFo`
**Thread (context):** 俄羅斯無論輸贏,這場戰爭將會成為他們的污點,在歷史上不會被人埋沒的記憶,願榮歸烏克蘭
**Comment:** ​@popo-hb3yq 你知道台灣不是中華人礦共和國的就好，人礦你們要多吃著，不然比俄爹更慘的😂🤣
**Translation:** You just need to know Taiwan is not the 'People's Mine Republic of China'; eat more, or you'll end up worse than your Russian daddy 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — Retort to PRC user + Taiwan not PRC → ST.

---

### id 30703
**Video:** `445U-unDGFo`
**Thread (context):** 俄羅斯無論輸贏,這場戰爭將會成為他們的污點,在歷史上不會被人埋沒的記憶,願榮歸烏克蘭
**Comment:** 來看笑話。看小粉紅向俄爹請安😂
**Translation:** Came to watch the joke — watching the little pinks pay respects to Russian daddy 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | **0** | 0 | 0 |
| Opus | 0 | **0** | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — 小粉紅 named → ST (your rule). Not about Ukraine itself → no SU.

---

### id 30749
**Video:** `445U-unDGFo`
**Thread (context):** 希望俄羅斯趕緊解體了，這種垃圾獨裁國家壓根就不應該存在...
**Comment:** @霖枪 其實在非洲就有一個很友臺（中華民國）的獨裁國家喔，叫史瓦帝尼
還有當年革命前親美的古巴巴蒂斯塔政權也是獨裁政權
**Translation:** (reply to 'Russia's dictatorship shouldn't exist') Actually Eswatini in Africa is a dictatorship friendly to the ROC; Batista's pro-US Cuba was one too.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Points out pro-US dictatorships without moral condemnation of the US → false.

---

### id 30787
**Video:** `445U-unDGFo`
**Thread (context):** 半场开香槟往往到最后输的最惨😂
**Comment:** @yang10095 不要緊的,反正主義永遠高於現實
出了獨裁者都叫偉大領袖,有什麼苦難不是活該的?
**Translation:** Ideology always beats reality; every dictator is a 'great leader', so any suffering is deserved?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Mocks dictatorship in general, not the invasion → false.

---

### id 30791
**Video:** `445U-unDGFo`
**Thread (context):** 如果最後俄羅斯戰敗，這些在博物館裡針對俄烏戰爭的一切事物都會是笑話
**Comment:** @keke-user2023 老毛真的用了 就不是戰敗撤軍可解決  曾經那個讓北約歐美連續45年24小時都派戰略轟炸機在天上與數艘戰略核潛艦在海裡的國家已經消失  我想北約美國不會再等到俄國發展成為舊蘇聯那個讓世界膽顫驚心的國家了  在見識俄國的導彈準度與武力  應該可能會選擇核滅俄國  就簡單的跟你講蘇美兩國冷戰時期掉到海底的核彈都超過百枚 未找到至少還有50枚  包括西太平洋 大西洋  地中海 日本海   5000枚核彈 真正能用有幾枚  有幾枚能射到美國本土  美國本土自己核試爆都炸超過50枚  他有在擔心核攻擊嗎?
**Translation:** (long) The country that scared NATO for 45 years is gone… having seen Russia's missile accuracy, NATO/US might choose to nuke Russia…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Says Russia is weak and declining → SU per rule on Russia's decline.

---

### id 30796
**Video:** `445U-unDGFo`
**Thread (context):** 我朋友现在正在莫斯科出差，已经待了3个月了，据他说，完全感觉不到莫斯科民众有什么不对劲的，尤其是超市物价竟然完全没变，和开战前一模一样。
**Comment:** @李嘉駿-d7c 俄羅斯能源國石油天然氣大量輸出歐盟，要經濟脫鉤付出的損失不是中國能比的。
中國損失頂多就是代工，俄羅斯事能源這種更攸關民生的資源，你看其他國家為制裁俄羅斯提出的價格上限就知道。他們不是直接禁止而是規定每桶60美元以上不買，這代表其他國家只能選擇性抵制無法完全脫鉤。歐元還在那時候探底，跟美元達到1比1
**Translation:** Russia is an energy exporter; the EU can't fully decouple… price cap shows countries can only boycott selectively.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 0 | 0 | 0 | 0 |
| Opus | **0** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Economic explanation, not clearly pro-Russia → false.

---

### id 30803
**Video:** `445U-unDGFo`
**Thread (context):** 事实上并没啥影响😅
**Comment:** @中華民國大總統袁-o5m 那是因為你不是俄羅斯籍，而且全俄羅斯，莫斯科是影響最小的地方。
**Translation:** (reply to 'no real effect 😅') That's because you're not Russian, and Moscow is the least affected place.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Says war/sanctions do hurt Russia → SU (weak).

---

### id 30845
**Video:** `445U-unDGFo`
**Thread (context):** 俄國對付納粹德國用的是美國的金錢與坦克等裝備, 結果反美, 這和中國同樣接受美國資助後反美是一個模樣, 原因是他們中俄也想當世界老大...
**Comment:** 呵呵，老美你也信😂你也不想想戰前德國背後的美國資本。至於所謂中國接受美國資助更是雙方利益交換，美國給錢給技術，中國做反對蘇聯的盟友，可不存在甚麼你欠我我欠你的
**Translation:** Heh, you believe the Americans 😂 Think of the US capital behind pre-war Germany…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — Distrust of the US → DUS.

---

### id 30846
**Video:** `445U-unDGFo`
**Thread (context):** 俄國對付納粹德國用的是美國的金錢與坦克等裝備, 結果反美, 這和中國同樣接受美國資助後反美是一個模樣, 原因是他們中俄也想當世界老大...
**Comment:** 奥班巴當年說如果中國居民也像澳大利亞人、美國人現在過著這樣的生活，那麼我們所有人都將陷入十分悲慘的境地。
呵呵，世界的資源是有限的，就好比一個原本已經瓜分好的蛋糕，美歐持有最大份，而中國的崛起，管你是共產中國還是自由中國也好，相當於搶了列強們的資源配額，對於其他國家和資本就是不死不休
**Translation:** The world's resources are a cake the US and Europe already split; China's rise steals their share, so it's a fight to the death.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | 0 | **0** | 0 |
| Opus | 0 | 0 | 0 | 0 | **1** | 0 |

**Your call:** Opus (DUS) — **Borderline** — Condemns US/West as hostile hegemon → DUS.

---

### id 30851
**Video:** `445U-unDGFo`
**Thread (context):** 澤連斯基加油，為西方和俄戰鬥剩最後一個烏克蘭人，千萬不要放棄！加入北約，為了美好生活！
**Comment:** 愚民
**Translation:** (reply to sarcastic 'Zelensky fight to the last Ukrainian') 'Fools.'

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 0 | 0 | 0 | 0 |
| Opus | **0** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — Target unclear → false.

---

### id 30861
**Video:** `445U-unDGFo`
**Thread (context):** bbc中文是个很好的频道，但我更希望在这个频道里大家无论归属哪个国家，说话的时候理智一点，你们讨厌小粉红五毛，因为他们说话不过脑子；但那些喊着解体俄罗斯，解体中国的人一样没过脑子，武统和解体都属于简单粗暴不考虑后果的解决方式。如果世界真像你们想的那么简单，那就不需要联合国这种组织的存在了
**Comment:** 基本上解體俄中，解除武裝是對附近國家最安全的方式，我認為聯合國可能短暫接管，之後還給中國自治權
**Translation:** Dismantling Russia and China and disarming them is the safest for neighbouring countries; UN could take over, then give China autonomy.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — China as a threat to neighbours → ST.

---

### id 30864
**Video:** `445U-unDGFo`
**Thread (context):** bbc中文是个很好的频道，但我更希望在这个频道里大家无论归属哪个国家，说话的时候理智一点，你们讨厌小粉红五毛，因为他们说话不过脑子；但那些喊着解体俄罗斯，解体中国的人一样没过脑子，武统和解体都属于简单粗暴不考虑后果的解决方式。如果世界真像你们想的那么简单，那就不需要联合国这种组织的存在了
**Comment:** @joe2841 一個獨裁恐怖政府擁有一堆核武器有比較好嗎 哪一個對世界和平威脅比較大 我還沒看到哪個小國威脅動用核武的
**Translation:** Is a terror dictatorship with lots of nukes better? Which threatens world peace more?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Backs dismantling Russia → SU.

---

### id 30885
**Video:** `445U-unDGFo`
**Thread (context):** 一個我很驚訝的事實是，歐美的媒體機構和記者仍然能夠在俄羅斯運營並製作報導，為什麼俄羅斯沒有完全禁止掉外國媒體的存在呢？同時我向在俄羅斯內報導的記者們致敬。
**Comment:** @runcelim 你去打聽打聽為啥韭菜粉紅都愛收看'新聞聯播'你就該知道了. 新聞聯播是打鷄血, 誰不愛?
**Translation:** Go find out why the leek-pinks love watching 新聞聯播…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — 粉紅 named → ST.

---

### id 30908
**Video:** `445U-unDGFo`
**Thread (context):** 一個我很驚訝的事實是，歐美的媒體機構和記者仍然能夠在俄羅斯運營並製作報導，為什麼俄羅斯沒有完全禁止掉外國媒體的存在呢？同時我向在俄羅斯內報導的記者們致敬。
**Comment:** @xiangli2958 這是真的,台灣整天報烏克蘭又贏了,俄又拿出70年前坦克來了, 講了一年多, 結果老俄還在烏的領土裡打? 哇靠,不是一年前就說老俄沒彈藥了嗎? 所以不管在共匪國還是民主國,看新聞還是要有自己的判斷力
**Translation:** True, Taiwan reports Ukraine winning all day, Russia using 70-year-old tanks… yet Russia is still in Ukraine.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **0** | 0 | 0 | 0 |
| Opus | 1 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CU + CT) — Undercuts Ukraine success → CU; attacks Taiwan media → CT (prompt rule).

---

### id 30913
**Video:** `445U-unDGFo`
**Thread (context):** 一個我很驚訝的事實是，歐美的媒體機構和記者仍然能夠在俄羅斯運營並製作報導，為什麼俄羅斯沒有完全禁止掉外國媒體的存在呢？同時我向在俄羅斯內報導的記者們致敬。
**Comment:** @w3495x 中華民主共和國共產黨匪佔領區，淪陷首都所在地。簡稱西台灣。
**Translation:** 'The CCP-bandit-occupied area of the ROC, where the fallen capital is. Called West Taiwan for short.'

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — ROC claim + mocks PRC → ST.

---

### id 30917
**Video:** `445U-unDGFo`
**Thread (context):** 一個我很驚訝的事實是，歐美的媒體機構和記者仍然能夠在俄羅斯運營並製作報導，為什麼俄羅斯沒有完全禁止掉外國媒體的存在呢？同時我向在俄羅斯內報導的記者們致敬。
**Comment:** @司法何時敢直播 雖然俄羅斯實質上是一個幾乎不容許反對聲音的國家，而且是前蘇聯最大的遺產，但不可否認他們現在是民主制度，而且台灣也沒資格講俄羅斯，我們除了親美以外，其他地方都跟半個獨裁沒兩樣甚至還有政府機關跟國會議員想推行數位中介法這種惡法，但你會說台灣是極權國家嗎？不會吧？台灣還是民主社會，反觀俄羅斯，即使你討厭他入侵烏克蘭，即使他們的政治跟獨裁沒兩樣，但系統還是算民主制度。
**Translation:** Taiwan has no right to criticise Russia; apart from being pro-US we're half a dictatorship… Russia's system is still democratic.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | **0** | 0 | 0 | 0 |
| Opus | 0 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CT) — Discredits Taiwan's democracy → CT.

---

### id 30927
**Video:** `445U-unDGFo`
**Thread (context):** 一個我很驚訝的事實是，歐美的媒體機構和記者仍然能夠在俄羅斯運營並製作報導，為什麼俄羅斯沒有完全禁止掉外國媒體的存在呢？同時我向在俄羅斯內報導的記者們致敬。
**Comment:** @w3495x 西台灣又可稱黃俄羅斯
**Translation:** 'West Taiwan' can also be called Yellow Russia.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **1** | 0 | 0 |
| Opus | 0 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Sonnet (ST) — **Borderline** — 西台灣 meme, mocks PRC → ST (same as 30913). Pure 黃俄 jabs you usually left false — weak.

---

### id 30933
**Video:** `445U-unDGFo`
**Thread (context):** 一個我很驚訝的事實是，歐美的媒體機構和記者仍然能夠在俄羅斯運營並製作報導，為什麼俄羅斯沒有完全禁止掉外國媒體的存在呢？同時我向在俄羅斯內報導的記者們致敬。
**Comment:** @xiangli2958因為戰果如何可以從戰場上實際情況來判斷，當某個國家聲稱的戰果跟事實有很大差距的時候，去參考它的說法就沒什麼意義了。
**Translation:** Battle results can be judged from the real battlefield; when a country's claims differ that much from facts, its version is meaningless.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Dismisses Russia's claims → SU (weak).

---

### id 30935
**Video:** `445U-unDGFo`
**Thread (context):** 之前西方產品退出俄羅斯並不代表完全消失
很多西方的產品會被二手甚至三手帶進去俄羅斯境內，畢竟你要一下子完全禁止不現實，而對於生產商而言，他有銷路就好，管他賣給俄羅斯還是吉爾吉斯坦

再來，近期很多“替代品”取代了原本有的麥當勞、漢堡王等西方速食，但部分改做“經過俄羅斯化後的改良產品”，符合當地人口味的漢堡、或是餐點

至少可以看出，俄羅斯這個能源國短期內不會過太差
但長期來看，這很明顯不是一個好的方法，俄羅斯除開能源以外，其科技產業與工業並沒有與其他國家有太多優勢，而於此同時不得不大量進口外國產品導致貿易順差。
客觀上，俄羅斯滿足內需絕對不會有問題，但問題是你能夠“閉關鎖國”到什麼時候
**Comment:** 蘇聯時期就跟我們詮釋閉關鎖國後的俄國
**Translation:** The Soviet era already showed us Russia after closing itself off.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | 0 | 0 |
| Opus | 0 | **1** | 0 | 0 | 0 | 0 |

**Your call:** Opus (SU) — **Borderline** — Predicts Russia's isolation/decline → SU per prompt rule.

---

### id 30938
**Video:** `445U-unDGFo`
**Thread (context):** 之前西方產品退出俄羅斯並不代表完全消失
很多西方的產品會被二手甚至三手帶進去俄羅斯境內，畢竟你要一下子完全禁止不現實，而對於生產商而言，他有銷路就好，管他賣給俄羅斯還是吉爾吉斯坦

再來，近期很多“替代品”取代了原本有的麥當勞、漢堡王等西方速食，但部分改做“經過俄羅斯化後的改良產品”，符合當地人口味的漢堡、或是餐點

至少可以看出，俄羅斯這個能源國短期內不會過太差
但長期來看，這很明顯不是一個好的方法，俄羅斯除開能源以外，其科技產業與工業並沒有與其他國家有太多優勢，而於此同時不得不大量進口外國產品導致貿易順差。
客觀上，俄羅斯滿足內需絕對不會有問題，但問題是你能夠“閉關鎖國”到什麼時候
**Comment:** "近期很多“替代品”取代了原本有的麥當勞、漢堡王等西方速食"
這是把外國公司直接強佔收收歸國有...
**Translation:** Those 'substitutes' were foreign companies seized and nationalised…

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Criticises Russia's domestic conduct, not the invasion → false.

---

### id 30952
**Video:** `445U-unDGFo`
**Thread (context):** 不破不立。衷心感謝俄羅斯以一己之力，給了烏克蘭，俄羅斯本國，中國，北朝鮮，歐洲，以及全世界信仰民主自由的人民一個更上一層樓的機會。
**Comment:** @白晨宇-y9l 那你看看中國韭菜吧！我在說什麼你在說什麼，你可真厲害這都能扯美國，不愧是小粉紅思維聊東扯西
**Translation:** Look at China's leeks! … typical little-pink thinking.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — 小粉紅 named → ST.

---

### id 30969
**Video:** `445U-unDGFo`
**Thread (context):** 不破不立。衷心感謝俄羅斯以一己之力，給了烏克蘭，俄羅斯本國，中國，北朝鮮，歐洲，以及全世界信仰民主自由的人民一個更上一層樓的機會。
**Comment:** 自由要代價換來
**Translation:** (reply to 'thanks Russia for giving everyone a chance…') Freedom has to be paid for.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Too vague → false.

---

### id 31015
**Video:** `445U-unDGFo`
**Thread:** 偏見 從俄羅斯的角度 你北約直接來烏克蘭 俄羅斯怎可能不打 北約直接侵門踏戶威脅你莫斯科 你們BBC 怎不去講為什麼你們要這樣做！
**Translation:** Biased. From Russia's view, NATO came straight into Ukraine… how could Russia not fight? Why doesn't BBC say why you did this!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Sonnet (BNE) — **Borderline** — NATO-provocation only, no blame on Ukraine → BNE only. (You set CU on ~half of BNE rows; here no Ukraine criticism.)

---

### id 31033
**Video:** `445U-unDGFo`
**Thread:** 是外國勢力迫俄羅斯去烏克蘭開火反抗的,一切都是反俄勢力在背後策劃的超級大陰謀！
**Translation:** Foreign forces forced Russia to open fire in Ukraine; it's all a super conspiracy by anti-Russia forces!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Sonnet (BNE) — **Borderline** — Both said BNE; could be sarcasm. Took BNE only.

---

### id 31057
**Video:** `445U-unDGFo`
**Thread:** 呃怎麼烏克蘭的影片下那麼多灣灣在批評所謂的獨裁政權。是哪條法律規定每個國家都要民主呀？你美國爸爸規定的嗎？又有誰說俄羅斯不可以侵犯別國😂再說了，烏克蘭是怎麼咎由自取的請自己去閱讀。不要什麼都不會來丟人現眼
**Translation:** Why so many 灣灣 criticising dictatorships under a Ukraine video? Did your US daddy rule every country must be democratic? Who says Russia can't invade? Ukraine brought it on itself.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | **0** | 0 | 0 | 0 |
| Opus | 1 | 0 | **1** | 0 | 0 | 0 |

**Your call:** Opus (CU + CT) — **Borderline** — Ukraine brought it on itself → CU; mocks Taiwanese/US-daddy → CT.

---

### id 31088
**Video:** `445U-unDGFo`
**Thread:** 消滅共匪,人人有責
**Translation:** Wiping out the communist bandits is everyone's duty.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — Anti-CCP resolve → ST.

---

### id 31095
**Video:** `445U-unDGFo`
**Thread:** 烏克蘭親西方的政策是極端錯誤的，地緣囯沒有互信開戰是必然。不過無法掩蓋俄羅斯是侵略戰爭的事實。
**Translation:** Ukraine's pro-Western policy was extremely wrong; war was inevitable. But that can't hide that Russia waged a war of aggression.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | **1** | 0 | 0 | 0 | **0** |
| Opus | **1** | **0** | 0 | 0 | 0 | **1** |
| My call | **1** | **0** | 0 | 0 | 0 | **0** |

**Your call:** Other (CU) — **Borderline** — Blames Ukraine's policy → CU; NATO not named and still calls it aggression → no BNE. Mixed; could be false.

---

### id 31102
**Video:** `445U-unDGFo`
**Thread:** Describing countries opposed by the West in a dark, melancholic and sarcastic tone is a common technique used by Western journalists
**Translation:** Describing countries the West opposes in a dark, sarcastic tone is a common Western-journalist technique.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 0 | 0 | 0 | 0 |
| Opus | **0** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Media-bias complaint, no stance on Ukraine → false.

---

### id 31119
**Video:** `445U-unDGFo`
**Thread:** 2:40 以美國為首的北約推動在鳥克蘭境內佈署愛國者飛彈和雷達系統, 俄羅斯希望建立一個緩衝區不讓對方掃瞄自家門口, 這不是捍衛國家是什麼? 再說鳥克蘭有石油嗎? 沒有啊, 這和美國入侵中東的原因是不同的. 還有啊, 當年古巴在國內佈署了飛彈系統美國一樣不讓人家這樣做啊
**Translation:** US-led NATO put Patriots and radars in Ukraine; Russia wants a buffer… US invaded the Middle East; US didn't allow missiles in Cuba either.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | **0** | 1 |
| Opus | **1** | 0 | 0 | 0 | **1** | 1 |
| My call | **0** | 0 | 0 | 0 | **1** | 1 |

**Your call:** Other (DUS + BNE) — NATO cause → BNE; US whataboutism → DUS. No blame on Ukraine → no CU.

---

### id 31121
**Video:** `445U-unDGFo`
**Thread (context):** 2:40 以美國為首的北約推動在鳥克蘭境內佈署愛國者飛彈和雷達系統, 俄羅斯希望建立一個緩衝區不讓對方掃瞄自家門口, 這不是捍衛國家是什麼? 再說鳥克蘭有石油嗎? 沒有啊, 這和美國入侵中東的原因是不同的. 還有啊, 當年古巴在國內佈署了飛彈系統美國一樣不讓人家這樣做啊
**Comment:** @dcar6530 與美國當年要入侵古巴一樣而已
**Translation:** Same as the US wanting to invade Cuba back then.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | **0** | 1 |
| Opus | **1** | 0 | 0 | 0 | **1** | 1 |
| My call | **0** | 0 | 0 | 0 | **1** | 1 |

**Your call:** Other (DUS + BNE) — **Borderline** — Inherits the NATO argument → BNE; US hypocrisy → DUS.

---

### id 31137
**Video:** `445U-unDGFo`
**Thread (context):** 可是我感觉乌东地区，包括克里米亚的民众都是比较亲俄的，按照西方国家的双标政策应该支持民主，不应该承认主权啊！比如台湾的主权归属问题，为什么美国要支持台湾独立呢？
**Comment:** ​@haishishenlou-2025 臺灣現在是中華民國政府遷過來的，就好比如北宋變南宋，這樣宋朝難道就滅了嗎？不要太過相信教科書，要保持疑問
**Translation:** Taiwan is the ROC government that moved here, like Northern Song becoming Southern Song — the Song didn't end.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Opus (ST) — **Borderline** — ROC continuity against PRC claim → ST.

---

### id 31176
**Video:** `445U-unDGFo`
**Thread:** 搞笑 , 俄羅斯不打， 五 年後就是北約打俄羅斯了 , 不信嗎
**Translation:** Ridiculous. If Russia didn't fight, NATO would fight Russia in five years.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Sonnet (BNE) — **Borderline** — Like your '俄罗斯不打乌克兰，北约就会干到莫斯科' (BNE, CU=0) → BNE only.

---

### id 31180
**Video:** `445U-unDGFo`
**Thread:** 關你ＢＢＣ屁事，從拿破倫、納粹到北約 。。。只見西方侵略俄國，沒看過俄國侵略西方。。。海盜國死性不改！！！
**Translation:** None of BBC's business. From Napoleon, the Nazis to NATO… only the West invades Russia. Pirate nations never change!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Sonnet (BNE) — **Borderline** — NATO/West as aggressor → BNE. No Ukraine content → no CU.

---

### id 31183
**Video:** `445U-unDGFo`
**Thread:** 今日惡國.明日終國
**Translation:** Today the evil country (俄), tomorrow the end country (中).

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Pun, terse, unclear → false.

---

### id 31206
**Video:** `445U-unDGFo`
**Thread (context):** When the people of Russia does not feel the pain, there is no reason for them to stop the aggression。 The same with Japan in WWII, it was only until the homeland was attacked and bombed, the gov't and people finally started to think otherwise.
**Comment:** LOL
"Think otherwise"?? But think what? Did the Japanese people, upon being bombed by Americans, really start to think that their vision of  Eastern Asian Coprosperity Circle was a lie and their war of Great Eastern Asian liberation was unjust? The consensus among historians is quite clear: although there was clearly war-wariness, even until the last days of WWII, the overwhelming majority of Japanese people, brought up through ultranationalistic education and inundated by the regime's propaganda, remained thoroughly convinced that they were the victims of the White Powers' (i.e. American and British) colonial aggression, and was fighting for the liberation of the Yellow Race. The fact the American bombs directly fell on their heads and killed their families only served to further convince the population of the government's narrative of the event, which was that Americans were the evil monster who gave Japan no choice but to fight for its survival. 
Japan surrendered not because of some "great awakening" among its people, but because of the great mushroom clouds of the nukes.
Japan was defeated by the sheer brute force of Hard Power through blood and fire and nukes. It didn't voluntarily give up the fighting because its "gov't and people finally started to think otherwise". "Thinking" played no part in it, only annihilating destruction, which left Japan with NO choice but to surrender in the end. 

In order to repeat Japan's defeat in Russia the US have to literally bomb Russia into oblivion as it did Japan. The only problem in this scenario is that unlike Japan, Russia today is literally the top nuclear power in the world in terms of nuclear warheads: 6000 versus the 5900+ warheads owned by the entire NATO. Russia has more nukes than any country in the world and has explicitly avowed to use them in the event its homeland is under attack. 
Attempts to repeat Japan's defeat in Russia guarantee a nuclear war between Russia and the US, which will usher  in a nuclear winter that dooms the Earth.
Based on your recommendation It's quite clear you are an alien from another planet who wishes to blow up our planet and end the entire human civilization. Sorry you just  got exposed Mr. Alien. Nice try at pretending to be humans.
**Translation:** (long English reply) Japan surrendered only to nukes; to repeat that, the US would have to nuke Russia, which has the most nukes — guaranteed nuclear war.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 0 |
| Opus | **1** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Argues defeating Russia is impossible → CU.

---

### id 31238
**Video:** `445U-unDGFo`
**Thread:** 西方在各種場合提起俄羅斯侵略自由民主的烏克蘭，但從不反思為什麽會有這場戰爭，俄羅斯人並不想發動戰爭，但北約的東擴以及對莫斯科生存空間持續擠壓的「深層因素」，再加上述那些元素作用才誘發衝突。也從不提及20世紀以來烏東的局勢演變，烏克蘭主義俄羅斯族人的分裂和克什米亞衝突以及烏東地區多次的公投
**Translation:** The West never asks why this war happened… NATO expansion squeezing Moscow… nor mentions East Ukraine's ethnic split and referendums.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **0** | 0 | 0 | 0 | 0 | 1 |
| Opus | **1** | 0 | 0 | 0 | 0 | 1 |

**Your call:** Opus (CU + BNE) — **Borderline** — NATO cause → BNE; questions Ukraine's claim to the east → CU.

---

### id 31252
**Video:** `445U-unDGFo`
**Thread:** 俄國不是好東西，但用這種陰間色調是？
**Translation:** Russia isn't a good thing, but why this underworld colour grading?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Complaint about the video → false.

---

### id 31261
**Video:** `445U-unDGFo`
**Thread:** 爛國還在yt做怪
**Translation:** The rotten country is still making trouble on YT.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Target unclear → false.

---

### id 31264
**Video:** `445U-unDGFo`
**Thread (context):** 在这里 我感谢俄罗斯政府以及牺牲的俄罗斯士兵已经牺牲的乌克兰士兵表示他们维护核平衡的敬意
**Comment:** 黃鵝感恩鵝爹還需要理由的嗎?
**Translation:** (reply) Does the yellow goose need a reason to thank goose daddy?

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — Pure 黃俄 jab → false (your precedent '黃俄孝子沒去教育營也很支持俄爹丫' = all false).

---

### id 31272
**Video:** `445U-unDGFo`
**Thread:** 同情烏東被烏克蘭納粹屠殺的人民，願台灣與烏東追求民主獨立的人民都能不受壓迫，早日解放
**Translation:** Sympathy for East Ukrainians slaughtered by Ukrainian Nazis; may the people of Taiwan and East Ukraine seeking democratic independence be liberated soon.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 1 | 0 | 0 | **1** | 0 | 0 |
| Opus | 1 | 0 | 0 | **0** | 0 | 0 |

**Your call:** Opus (CU) — **Borderline** — Both said CU. Taiwan part reads as sarcasm (解放 = PRC term), direction unclear → no ST. Keeps CU.

---

### id 31278
**Video:** `445U-unDGFo`
**Thread:** worrying about china are heading to the same condition.
**Translation:** Worrying about China heading to the same condition.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | 0 | 0 | **0** | 0 | 0 |
| Opus | 0 | 0 | 0 | **1** | 0 | 0 |

**Your call:** Sonnet (all false) — **Borderline** — Terse, unclear → false.

---

### id 31280
**Video:** `445U-unDGFo`
**Thread:** 德國入侵了蘇聯，但之前蘇聯已入侵了波蘭、波羅的海三國和芬蘭。不過英美為了打敗納粹都假裝看不到吧了。今天俄羅斯人可以接受入侵烏克蘭，因為從前蘇聯也入侵了波蘭，他們覺得一樣的。當正義按照利益來計價，所以2014年入侵克里米亞時歐美也可以看不到。
**Translation:** The USSR invaded Poland, the Baltics and Finland before; Britain and the US pretended not to see… in 2014 the West also didn't see Crimea.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **0** | 0 | 0 | **0** | 0 |
| Opus | 0 | **1** | 0 | 0 | **1** | 0 |

**Your call:** Opus (SU + DUS) — **Borderline** — Condemns Russian invasions → SU; Western/US looking away → DUS.

---

### id 31288
**Video:** `445U-unDGFo`
**Thread (context):** 「還沒勝利的戰爭，卻被放入了勝利博物館。」
發人深省的一句話
**Comment:** 因為主義永遠凌駕於現實
這就是紅色
**Translation:** Because ideology always beats reality. That's red.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Mocks communism → false.

---

### id 31295
**Video:** `445U-unDGFo`
**Thread:** 不要總站你們西方的視角看問題，再說西方視角也不一定就正確，西方一直歧視俄國，所以俄國在你們眼中做什麽都是錯的。
**Translation:** Don't always look from your Western view; the West always discriminates against Russia, so whatever Russia does is wrong to you.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 0 | 0 | 0 | 0 |
| Opus | **0** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (CU) — **Borderline** — Defends Russia's actions against criticism → CU.

---

### id 31310
**Video:** `445U-unDGFo`
**Thread:** 未戰爭封鎖消息再洗腦 不愧是共產國家 國民黨以前也玩這套 反攻大陸 都是屁
**Translation:** Block news and brainwash before war — truly communist. The KMT did that too.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Russian domestic propaganda → false.

---

### id 31321
**Video:** `445U-unDGFo`
**Thread:** 沒什麼男人了！女人要哈死啦！沒有人可以啪啪了😮😮😮😮😮
**Translation:** No men left! The women will be desperate 😮

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Crude joke, not a clear stance → false.

---

### id 31326
**Video:** `445U-unDGFo`
**Thread:** 學強國最叻嗰招～洗腦🫢
**Translation:** Learned China's best trick — brainwashing 🫢

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Domestic → false.

---

### id 31343
**Video:** `445U-unDGFo`
**Thread:** 😂全球人民更關注的是⋯報導一下烏克蘭人民生活有什麼變化吧！
**Translation:** The world cares more about… report on Ukrainian people's lives!

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — No clear stance → false.

---

### id 31351
**Video:** `445U-unDGFo`
**Thread:** 推特、臉書、LINE等等都被禁用，然後說很自由整天洗腦，反戰言論就會被抓
跟中共87%像，不愧是父子
**Translation:** Twitter, Facebook, LINE all banned, then say it's free while brainwashing… 87% like the CCP, father and son.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Domestic → false.

---

### id 31352
**Video:** `445U-unDGFo`
**Thread:** 這個記者很勇敢，敢在俄國境內批評俄國😂
**Translation:** This reporter is brave, criticising Russia inside Russia 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — False.

---

### id 31362
**Video:** `445U-unDGFo`
**Thread:** 極權政府從來都不缺笑話😂
**Translation:** Totalitarian governments never lack jokes 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — False.

---

### id 31374
**Video:** `445U-unDGFo`
**Thread:** 而對黃俄孝子，連這些都不用就無條件支持俄軍了。
**Translation:** And the yellow-Russia filial sons support the Russian army unconditionally without any of this.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — Pure 黃俄 jab → false (your precedent).

---

### id 31387
**Video:** `445U-unDGFo`
**Thread (context):** 北约如果不东扩，俄罗斯会入侵乌克兰？其实道理大家都明白，只不过立场不同罢了
**Comment:** 怪北約呢 結果俄羅斯開戰 反而北約東擴 本末倒置？
**Translation:** Blame NATO? Russia started the war and NATO expanded instead — that's backwards.

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | 0 | **1** | 0 | 0 | 0 | 0 |
| Opus | 0 | **0** | 0 | 0 | 0 | 0 |

**Your call:** Sonnet (SU) — **Borderline** — Rejects the NATO argument and says the war backfired on Russia → SU.

---

### id 31394
**Video:** `445U-unDGFo`
**Thread:** 跟黑中國一樣！ bbc? My ass!!😂😂😂😂😂
**Translation:** Just like smearing China! BBC? My ass!! 😂

| | CU | SU | CT | ST | DUS | BNE |
|---|---|---|---|---|---|---|
| Sonnet | **1** | 0 | 0 | 0 | 0 | 0 |
| Opus | **0** | 0 | 0 | 0 | 0 | 0 |

**Your call:** Opus (all false) — **Borderline** — Media-bias complaint → false.

---
