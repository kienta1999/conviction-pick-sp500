# Momentum Research — Batch 4
**Date:** 2026-08-04 | **Tickers:** GOOGL, MSFT, FCX, CF
**Frame:** explosive-return momentum bet — structural shortage + order-book visibility + irreplaceability

---

## SUMMARY TABLE

| Ticker | Shortage | Irreplace. | Fwd PE | ret_12m | Verdict (1 line) |
|---|---|---|---|---|---|
| GOOGL | 9 | 9 | 25.3 | +100% | Real sold-out compute shortage + the only vertically-integrated silicon-to-model stack; $4.6T cap is the only real brake. |
| MSFT | 8 | 7 | 20.8 | -5% | Shortage is genuine ($678B RPO, +84%) but the market is repricing capex/depreciation, not demand — the de-rate is the opportunity. |
| FCX | 8 | 8 | 15.6 | +70% | Copper deficit is intact and Grasberg is recovering on schedule — 2027 is the volume-plus-price year, 2026 is the pothole. |
| CF | 6 | 6 | 10.5 | +32% | Cheapest name here on the strongest current cash flow, but nitrogen is a cyclical price-taker, not a structural shortage. |

---

# 1. GOOGL — Alphabet

**Latest reported quarter:** Q2 2026 (Jun-qtr), reported **2026-07-22**.

| Metric | Actual | Consensus | Note |
|---|---|---|---|
| Revenue | **$119.80B** (+24% YoY) | $116.84B | Beat |
| Diluted EPS (GAAP) | **$9.11** | ~$2.89 | Beat, but see below — **$6.26/sh of it is a non-cash mark** |
| Operating income | $40.77B (+30%) | — | Op margin 34%, +1.6pt |
| Google Cloud rev | **$24.77B (+82% YoY)** | $22.42B | Big beat |
| Cloud op income | $8.81B (vs $2.83B LY) | — | Op margin 35.6% vs 20.7% |
| Search & other | $63.3B (+17%) | — | AI Overviews **not** cannibalizing |
| YouTube ads | $11.1B (+13%) | — | |
| Capex (qtr) | **$44.9B** | — | Record |
| FCF (qtr) | **-$5.9B** | — | Negative |

> ⚠️ **EPS caveat — do not use $9.11 as run-rate.** Other income (expense), net was **$97,983M**, "primarily reflecting net unrealized gains on equity securities." The net equity-securities gain of ~$99.0B **increased net income by $77.1B ($6.26/sh)**. These are marks on stakes including Anthropic and SpaceX. Underlying operating EPS is roughly **$2.85** — still a beat vs ~$2.89 consensus on an operating basis given the 30% op-income growth. Sources: Alphabet Q2 2026 8-K/press release (2026-07-22), TradingView/StockTitan filing summaries.

**Forward guidance given:** 2026 capex **raised to $195–205B** from $180–190B (2026-07-22). Management said capex will "**increase significantly again in 2027.**" No formal revenue guidance (Alphabet does not guide).

### 1. Shortage thesis — score 9/10
- **CFO Anat Ashkenazi (Q2 2026 call): Alphabet remains "supply-constrained"**, and will use **third-party capacity as a "bridging strategy"** while building its own. That is a hyperscaler renting someone else's datacenters because it cannot build fast enough — the strongest possible tell of genuine shortage.
- **Sundar Pichai (Q2 2026 call):** "It feels like we are in very early innings of what feels like [a] secular shift"; more bullish than a year ago.
- Quantification of the shortage: **capex guide raised $15B mid-year** (to $195–205B) and **still guided up again for 2027**. Companies do not raise capex 8% mid-year into a demand-uncertain market.
- Cloud revenue **+82% YoY** while cloud **operating margin simultaneously expanded 15 points** (20.7% → 35.6%). Accelerating volume *and* expanding margin is the pricing signature of a sold-out market — capacity is being allocated, not discounted.

### 2. Backlog / order book — the key number
- **Google Cloud contracted backlog: $514.0B** as of Q2 2026, **up ~$50B sequentially** (Q2 2026 earnings call, 2026-07-22).
- **Over half expected to convert to revenue within 24 months** (management, same call).
- Context: $514B backlog vs ~$24.8B quarterly cloud revenue = **~5.2 years of current run-rate revenue already contracted.** This is the single most important visibility number in the GOOGL story.

### 3. Category position
- Cloud infrastructure share (Synergy Research, Q1 2026): **AWS ~28%, Azure ~21%, Google Cloud ~14%.** Google is a clear **#3 by share**.
- But **#1 by growth by a wide margin**: GCP +82% vs Azure +43% (MSFT Q4 FY26) vs AWS +28% (Q1 2026). Google is the only one of the three *gaining share at an accelerating rate*.
- **#1 in the one place that matters strategically: merchant AI silicon.** Google is the only hyperscaler whose custom accelerator has become an externally-demanded product (see below).

### 4. Irreplaceability / disintermediation — score 9/10
**Reverse-angle interrogation (are they price-takers burning capex, or owners of the value chain?): Alphabet is the clearest *owner* in the group.** Evidence:
- **Anthropic:** Oct 2025 — access to up to **1 million TPUs**, >1GW online by 2026. Apr 2026 — expanded via Broadcom to **3.5GW of next-gen TPU capacity, up to ~5GW overall**; Anthropic post-money marked at **$350B**. Google Cloud CEO **Thomas Kurian explicitly attributed the win to TPU price-performance, not strategic alignment** — i.e. TPUs win on unit economics against Nvidia in an open bake-off.
- **Meta:** signed a **multibillion-dollar TPU lease** (reported 2026-02-26 / confirmed early Mar 2026) to train and serve models via Google Cloud, and is in talks to **buy TPUs outright for its own datacenters from 2027**.
- Other external TPU users: Salesforce (Einstein on Ironwood), Midjourney, Replit.
- Historically TPUs were rentable only inside GCP. **Google is now moving to sell silicon into customers' own datacenters** — targeting ~10% of Nvidia's datacenter revenue. This converts Alphabet from a capex-consuming cloud into a **merchant silicon vendor with a captive foundry-scale demand base**, capturing margin at the chip layer *and* the cloud layer *and* the model layer (Gemini).
- **Verdict on the reverse angle:** Alphabet is not a price-taker. It is the only Western company that owns TPU (chip) + DeepMind/Gemini (model) + GCP (distribution) + Search/YouTube (demand sink) + its own network/DC fabric. Every dollar of capex buys an asset it controls end-to-end, and its two biggest AI-lab competitors (Anthropic, Meta) are now paying it rent. **Disintermediation risk is near-zero at the compute layer.**
- **Model competition (OpenAI/Anthropic):** real but *structurally hedged* — Alphabet monetizes Anthropic three ways (equity stake, TPU sales, GCP rent) regardless of whether Gemini or Claude wins.
- **Search disruption:** Search & other still grew **+17% YoY in Q2 2026** with AI Overviews fully deployed. The cannibalization thesis has now been empirically falsified for six-plus quarters. This is the biggest single de-risking event in the story.
- **Antitrust (the genuine residual risk, and it has gone Alphabet's way):** Judge Mehta (Sept 2025) **rejected Chrome divestiture and contingent Android divestiture**, imposing behavioral remedies only (no exclusive Search distribution contracts). Google filed a **111-page D.C. Circuit appeal on 2026-05-22** seeking to overturn both the monopoly finding and the remedies; DOJ + state AGs cross-appealed in Feb 2026 arguing remedies were too weak. **No oral-argument date set.** Ad-tech case: Judge Brinkema found illegal monopolization of publisher ad server + ad exchange (2025-04-17); **no divestiture order issued as of mid-2026.** Net: the structural-breakup tail risk has been substantially removed; residual is ad-tech remedy and appellate reversal risk, both slow-moving.
- **Score 9/10** (not 10 — antitrust appeal and the theoretical possibility a rival lab's model leapfrogs Gemini keep it off the top).

### 5. Recent catalysts (since ~2026-05)
- **2026-05-22:** Google files D.C. Circuit appeal brief challenging monopoly finding + remedies.
- **2026-07-22:** Q2 2026 — revenue beat, Cloud +82%, backlog $514B, **capex guide raised to $195–205B**. Stock **sold off ~5%** on the capex hike, not on results.
- **Apr 2026 (2026-04-06/07/24):** Anthropic TPU expansion to 3.5GW / up to 5GW; largest AI-startup compute commitment outside MSFT-OpenAI.
- **Feb–Mar 2026:** Meta multibillion-dollar TPU lease; TPU direct-sale strategy emerges.
- Cloud op margin expansion 20.7% → 35.6% YoY — the AI business is now demonstrably profitable at scale.

### 6. Risks
- **AI capex digestion.** Q2 FCF was **-$5.9B**. If cloud growth decelerates while $200B/yr of capex is committed, the FCF hole widens and the multiple compresses fast. This is the live bear case and it is why the stock fell on a beat.
- **Depreciation drag.** $200B of 2026 capex plus a bigger 2027 number means a multi-year rising depreciation wave hitting operating margin from ~2027–2029.
- **Law of large numbers (explicitly asked).** At **$4,568B market cap**, a double requires adding ~$4.6T — more than the entire market cap of any company that existed before 2024. Honest assessment: **GOOGL is very unlikely to be the highest-percentage-return name in a momentum screen.** ret_12m of +100% at this size was already a historical anomaly. Analyst mean target $427 implies only **+13.1%**. For an *explosive-return* mandate, size is a real, non-hand-wavable cap. The counter: the earnings base is compounding at 24% revenue / 30% op income with margin expansion, and at 25.3x forward it is not priced for that. But the realistic bull case is +30–50%/yr, not a 3x.
- **Antitrust:** ad-tech remedy still pending; appellate outcomes unknowable.
- **Equity-mark reversal:** the $99B gain on Anthropic/SpaceX marks cuts both ways — a private-AI-valuation reset would produce enormous GAAP losses.

### HIGH_ACCRUALS flag — explanation (accrual_ratio 0.082, cfo/ni 0.76)
**Verdict: benign accounting artifact, not deteriorating earnings quality — but it masks a separate real issue.**
- The flag is almost entirely mechanical. Q2 2026 net income was **$112.1B**, of which **$77.1B was a non-cash unrealized mark-to-market gain on equity securities** (Anthropic, SpaceX et al., ASU 2016-01 fair-value accounting). That gain inflates the NI denominator but by construction **never appears in cash flow from operations**. CFO/NI of 0.76 is exactly what you would expect: strip the $77.1B and CFO/NI goes back above 1.0.
- The accrual ratio of 0.082 is further inflated by the balance-sheet side of the same thing plus the enormous PP&E build (capex $44.9B/qtr) growing net operating assets.
- **This is not the classic bad-accruals signature** (receivables/inventory ballooning ahead of collections, or revenue recognized before cash). Alphabet's receivables and deferred revenue are not the driver.
- **However — the flag accidentally points at a real thing.** FCF was **-$5.9B** in Q2. Earnings are not running ahead of *operating* cash, but reported profit is running far ahead of *free* cash because of the capex cycle. That is the legitimate concern, and it is a capex-cycle concern, not an earnings-quality one.
- **One-line verdict:** *Benign — the accrual flag is the signature of a $77.1B non-cash equity-mark plus a record capex build, not of earnings running ahead of cash; the number to actually watch is the negative free cash flow, not the accrual ratio.*

### 7. Score & verdict
**Shortage 9/10 · Irreplaceability 9/10**
> Alphabet is the highest-quality expression of the compute shortage — supply-constrained by its own CFO's admission, $514B of contracted backlog (~5 years of run-rate), the only hyperscaler whose silicon competitors pay it rent — but at $4.6T the law of large numbers makes it a superb compounder rather than an explosive-return bet.

---

# 2. MSFT — Microsoft

**Latest reported quarter:** FQ4 FY2026 (Jun-qtr), reported **2026-07-29**.

| Metric | Actual | Consensus | Note |
|---|---|---|---|
| Revenue | **$90.0B** (+18% YoY) | $87.67B | Beat |
| Diluted EPS (GAAP) | **$4.81** (+32% YoY) | $4.24 | Big beat |
| EPS ex-OpenAI impact | $4.74 (+23%) | — | Clean number |
| Intelligent Cloud | $39.3B (+32%) | — | |
| Productivity & Business Processes | $37.8B (+14%) | — | |
| More Personal Computing | $12.9B (-4%) | — | |
| **Azure & cloud services** | **+43%** | guide was 39–40% | **Beat its own guide** |
| Microsoft Cloud | $59.3B (+27%) | — | |
| **Commercial RPO** | **$678B, +84% YoY** | — | The headline number |
| M365 Copilot seats | >30M paid | — | Net adds **more than doubled** QoQ |
| **FY26 full year** | Rev **$331.8B** (+18%), EPS **$17.95** (+32%) | — | |

Stock reaction: **+8.9% after hours** (2026-07-29).

**Forward guidance given:** Calendar-2026 capex expectation **revised to ~$175B** (down from ~$190B guided in April) — but note this is an **optical reduction from a lease reclassification**, not a spending cut: extending server useful lives shifts more future datacenter leases from finance leases (in capex) to operating leases (not in capex); **"the underlying investment plans remain unchanged."** FY27 **operating margins guided to decline slightly** on continued AI infra + R&D investment. FX to reduce Q1 FY27 revenue growth by <1pt.

> ⚠️ **Correction to a widely circulated figure:** the "$255–260B FY27 capex guidance" appearing in some coverage traces to a **pre-earnings analyst preview, not to anything CFO Amy Hood actually guided.** Do not treat it as company guidance. Capex is guided to grow; the specific number is not company-sourced.

### 1. Shortage thesis — score 8/10
- **CFO Amy Hood, FQ4 FY26 call (2026-07-29), verbatim: "Yes, demand continues to exceed available supply."** She attributed the Azure acceleration to "significant efficiency gains across our CPU and GPU fleet" — i.e. they beat the guide by squeezing more out of existing iron, *because they could not add iron fast enough.*
- Management has guided **capacity-constrained through 2026** (and constraints on AI infrastructure expected to persist at least that long). Broad and growing customer demand continues to exceed supply.
- Quantified: **Azure revenue passed $100B for the first time in FY26, +41% for the full year**, and Q4 came in at **+43% vs a 39–40% guide** — accelerating *while supply-constrained*. Five AI datacenters at ≥1GW scale set to come online in 2026; multiple **Fairwater** sites, each with hundreds of thousands of GB200/GB300s, >2GW total interconnected capacity.
- Slightly below GOOGL only because MSFT's constraint is partly self-imposed (lease/power timing) and its growth, while excellent, is half Google Cloud's rate.

### 2. Backlog / order book — the key number
- **Commercial remaining performance obligation: $678B, +84% YoY** (FQ4 FY26, 2026-07-29). This is the largest corporate backlog figure in the market.
- **Quality check — this is the crucial detail:** **RPO grew 25% excluding OpenAI**, and **all sequential RPO growth was driven by commitments from customers *outside* frontier model companies.** Commercial bookings **+18% ex-OpenAI**.
- **Longer-term contractual commitments rose ~138%** — customers are locking in multi-year AI capacity.
- **CFO Amy Hood: nearly 90% of Microsoft Cloud revenue now comes from customers outside the frontier AI labs.** This directly rebuts the "MSFT is just an OpenAI SPV" bear case.
- vs ~$59.3B quarterly Microsoft Cloud revenue, $678B RPO is **~2.9 years of contracted cloud revenue.**

### 3. Category position
- **#2 in cloud infrastructure** (Synergy Q1 2026: AWS ~28%, **Azure ~21%**, GCP ~14%) — but **#1 in enterprise cloud + productivity bundled**, which is the real competitive unit.
- Growth: Azure **+43%** vs AWS **+28%** — Azure is taking share from #1. GCP is growing faster but from a base ~40% of Azure's.
- **#1 outright in AI-assisted productivity**: >30M paid M365 Copilot seats with net adds doubling QoQ — no competitor is close.

### 4. Irreplaceability / disintermediation — score 7/10
**Reverse-angle: Microsoft is a *partial* owner of the value chain — stronger than a pure reseller, weaker than Alphabet.**
- **In-sourcing:** **Maia 200** launched 2026-01-26 — inference-optimized accelerator, >10 PFLOPS FP4 / >5 PFLOPS FP8 in a 750W SoC envelope; plus Cobalt CPUs and the Fairwater DC fabric. Genuine vertical integration.
- **But:** Maia is a **generation behind TPU in external validation** — nobody outside Microsoft buys or rents Maia the way Anthropic and Meta buy TPU capacity. Microsoft's silicon reduces its own Nvidia bill; it does not create a merchant revenue stream. That is the core structural difference vs GOOGL and the reason for the 7 vs 9.
- **OpenAI relationship (restructured):** Microsoft holds **~27% equity in OpenAI (~$135B carrying value)**, retains **royalty-free IP rights**, and the partnership is now **non-exclusive through 2032.** Non-exclusivity cuts both ways: OpenAI can (and does) buy compute elsewhere, but Microsoft can now serve every other lab and keeps the IP. **OpenAI equity-method losses are a real GAAP drag — $3.1B in Q1 FY26 vs $523M a year earlier.**
- **Can customers in-source?** No. The moat is not compute — it is **Entra ID / M365 / the enterprise contract + compliance perimeter**. An enterprise can move a GPU workload; it cannot move its identity graph and 400M seats of Office. That is why 90% of Microsoft Cloud revenue is non-frontier-lab and why RPO ex-OpenAI still grew 25%.
- **Model competition:** the sharpest risk. If OpenAI/Anthropic commoditize the model layer and enterprises buy models direct, Azure becomes rented real estate. Mitigated by MSFT's IP rights through 2032 and its in-house MAI models.
- **Score 7/10** — unassailable in enterprise distribution, only mid-tier in AI silicon.

### 5. Recent catalysts (since ~2026-05)
- **2026-07-29: FQ4 FY26** — revenue and EPS beat, Azure +43% vs 39–40% guide, RPO $678B (+84%), FY26 revenue $331.8B. **Stock +8.9% AH.**
- Calendar-2026 capex optically cut to ~$175B via useful-life/lease reclassification — investors read this as capital discipline (positive) even though underlying plans are unchanged.
- **2026-01-26:** Maia 200 launch.
- Copilot inflection: >30M paid seats, net adds more than doubling QoQ — the first hard evidence of AI *software* (not just infrastructure) monetization.
- Recovery off the **~$356 April 2026 52-week low** to $492.81.

### 6. Risks
- **Depreciation drag on cloud margins.** This is the #1 risk and the direct cause of the de-rate. Capex nearly doubled in two years (FQ3 FY26 capex $30.9B, +84% YoY). **FY27 operating margins are company-guided to decline.** The useful-life extension that flattered capex optics also *delays* — but does not avoid — the depreciation wave, and extending useful lives on AI servers is an aggressive assumption if hardware cycles compress.
- **OpenAI GAAP losses** scaling with OpenAI's burn ($3.1B in one quarter and rising).
- **Non-exclusivity through 2032** means OpenAI workloads can migrate.
- **AI capex digestion:** if enterprise AI adoption plateaus, $175B+/yr of committed spend becomes stranded.

### The flat 12-month return — explanation (explicitly asked)
**ret_12m of -5% despite +18% revenue and +32% EPS growth is entirely multiple compression, not a business problem.**
- Path: **~$555 all-time high (late Oct 2025) → ~$356 52-week low (early Apr 2026), a >35% drawdown → $492.81 now.** So the "flat" 12-month number conceals a violent de-rate-and-recover round trip; the stock is up ~38% off the April low.
- **Why the de-rate:** the market spent 2024–25 pricing MSFT as though AI revenue would arrive immediately and cleanly at software margins. 2026 forced the recognition that this is a **3–5 year infrastructure cycle with messy free cash flow in the middle** — capital-intensive, depreciation-heavy, and margin-dilutive before it is accretive. Investors re-rated MSFT from "asset-light software compounder" toward "capital-intensive infrastructure," and those carry different multiples. MSFT traded to **~21.8x earnings — its lowest valuation in three years.** Screen's fwd PE 20.8 corroborates.
- **Opportunity or warning? Opportunity, with a caveat.** The evidence says demand is not the problem: Azure accelerated to +43% *above its own guide*, RPO +84% (+25% ex-OpenAI), Copilot seats inflecting, 90% of cloud revenue non-frontier-lab. You are buying **18% revenue / 32% EPS growth at 20.8x forward** — cheaper than the S&P's large-cap growth cohort and cheaper than GOOGL at 25.3x. **The caveat is real:** the de-rate is not irrational, it is a legitimate repricing of capital intensity, and management has *guided FY27 margins down*. So the multiple may not re-expand until depreciation peaks. This is the **highest risk-adjusted quality** name in the batch and the **lowest explosive-return probability** in the near term — you get paid by earnings growth, not by re-rating, unless AI software margins (Copilot) surprise.
- Note the setup asymmetry: MSFT is **-9% from its 52w high with -5% 12m return** while GOOGL is -6% from high with +100%. MSFT is the un-crowded AI trade.

### 7. Score & verdict
**Shortage 8/10 · Irreplaceability 7/10**
> The shortage is real and management says so in plain words ("demand continues to exceed available supply") with $678B of backlog behind it — but the market has correctly re-rated Microsoft from software compounder to capital-intensive infrastructure, so the return comes from 30% earnings growth at 20.8x, not from a re-rating, making it the safest and least explosive name in the batch.

---

# 3. FCX — Freeport-McMoRan

**Latest reported quarter:** Q2 2026, reported **2026-07-23**.

| Metric | Actual | Consensus | Note |
|---|---|---|---|
| Revenue | **$7.029B** | $6.71B | Beat +4.8% |
| Adjusted EPS | **$0.74** | $0.59 | **Beat +25.4%** |
| GAAP net income | $984M ($0.68/sh) | — | Adj net income $1.1B |
| Copper production | 786 Mlb | — | |
| **Copper sales** | **710 Mlb @ $6.17/lb realized** | — | Realized price is the story |
| Gold production | 192 koz | — | |
| Moly production | 23 Mlb | — | |
| Unit net cash cost | **$1.97/lb** (vs $1.13 LY) | — | Elevated on low PTFI volumes |
| Operating cash flow | $2.048B | — | Net of $596M WC use |
| Capital returns | $0.15/sh dividend; 1.7M sh repurchased for $110M | — | |

Note: idle facility + restoration costs of **$284M** were excluded from the unit-cash-cost metric — a real cash drag that flatters the reported cost figure. Stock **fell** on the print despite the beat.

**Forward guidance given (2026):** ~**3.1 Blb copper sales**, **650 koz gold**, **93 Mlb moly**; copper unit net cash costs ~**$1.90/lb**; **operating cash flow ~$8.3B** at stated metal price assumptions.
**2027 guidance:** copper sales **+>20% vs 2026**; gold volumes **+>50%**; further gains in 2028. **2027 capex ~$4.8B** (~$300M above prior guidance).

### 1. Shortage thesis — score 8/10
- **Price is the evidence.** Copper **$6.63/lb on 2026-08-04, +51.6% YoY.** LME cash $13,408.50/t (2026-07-10); record highs of **$6.61/lb COMEX and $13,842.50/t LME set 2026-01-29.** LME stocks **306,500t and drawing down** (from 324,850t at the start of that month).
- **Demand drivers:** grid electrification, AI datacenter buildout (each GW of datacenter is copper-intensive in busbar, cabling, transformers), EVs. Structurally these are additive to, not substitutes for, traditional construction demand.
- **Supply disruption is the acute driver:** Grasberg — one of the two or three largest copper-gold orebodies on earth — is running at a fraction of capacity (see below), removing hundreds of millions of pounds from a market with no spare capacity.
- **Tariff distortion adds a US-specific premium:** 50% Section 232 tariff on **semi-finished** copper products and copper-intensive derivatives in effect since **2025-08-01**. Refined cathode/anode/ore/concentrate/scrap **currently exempt but under active review** — Commerce was to update the President on US copper markets by **2026-06-30**, with a proposed phased refined-copper tariff of **15% in 2027 / 30% in 2028**. This has produced a **record ~30% COMEX-LME premium** and pulled COMEX stocks from <100kt to **>461,000t** (some reports >650kt) as importers front-ran the duty.
- **Honest counter-evidence (do not ignore):** **Macquarie forecasts a 262kt *surplus* in 2026 and surpluses >700kt annually in 2027–28.** S&P Global analysts have called the elevated-price period "overextended." So the "structural deficit" is contested at the 1–3 year horizon; the deficit is more clearly a 2028+ story. Price forecasts: Macquarie raised 2026 average to **$13,165/t**; BofA **$11,313/t 2026 / $13,501/t 2027**; **Goldman expects prices to decline somewhat from record highs in 2026.**
- Score 8, not 9–10, precisely because the near-term balance may be in surplus and the current price embeds a tariff premium that could be arbitraged away.

### 2. Backlog / order book equivalent
Copper miners have no backlog; the analogues are contracted volumes, realized price and production guidance:
- **Realized copper price Q2 2026: $6.17/lb** (vs spot $6.63 on 2026-08-04 — realizations lag and include provisional pricing).
- **2026:** 3.1 Blb Cu / 650 koz Au / 93 Mlb Mo; **OCF ~$8.3B**.
- **2027:** copper **+>20%**, gold **+>50%** — this is the visibility number.
- **Leach initiative:** targeting a **300 Mlb/yr run rate** on a path toward **800 Mlb/yr** — low-capital incremental production from existing stockpiles. Modeled annual EBITDA **~$13–20B** depending on copper price.

### 3. Category position
- **Among the largest publicly traded copper producers globally**, and the **dominant US-domestic producer** — Morenci (AZ) is the largest US copper mine; Freeport also owns US smelting capacity, which is strategically scarce given the Section 232 regime. In a tariff world, **domestic mine-to-metal integration is a structural advantage no foreign competitor can replicate.**
- **Bagdad expansion (AZ):** studies being updated ahead of a **potential investment decision in H2 2026**; would add **200–250 Mlb/yr**, cost **~$3.5B**, take **3–4 years**, require an incentive price of **~$4.00/lb** (vs $6.63 spot — comfortably economic), and make Bagdad the **second-largest US copper mine** behind Morenci. **45% of 2026's $1.6B discretionary capex is going to Bagdad early works.**
- CEO is actively lobbying for **US incentives to expand domestic copper** — a policy tailwind unavailable to non-US peers.

### 4. Irreplaceability / disintermediation — score 8/10
**Quantified moat:**
- **Time:** average copper mine takes **~17 years from discovery to production** (S&P Global). Mines starting 2020–23 took **17.9 years** vs 12.7 years for those started 15 years earlier — the timeline is *lengthening*. **12 of ~16 years is discovery/exploration/studies**; permitting, environmental review and community consultation consume most of the rest.
- **Capital:** weighted-average capital intensity for 26 upcoming copper projects starting by 2030 is **$22,359 per tonne of annual paid copper.** Replacing Grasberg's ~1 Blb/yr (~450kt) would cost **~$10B and take ~17 years** — and there is no second Grasberg-grade orebody to build it on.
- **FCX's own expansion math confirms it:** Bagdad, a *brownfield* expansion on an existing operating mine with existing permits, still costs **$3.5B and takes 3–4 years** for only 200–250 Mlb/yr.
- **Substitution:** aluminum can substitute in some transmission applications at a conductivity penalty, but not in motors, windings, or high-density datacenter power distribution. Substitution is a slow, partial ceiling — not a bypass.
- **Disintermediation:** customers (utilities, automakers, datacenter builders) cannot in-source an orebody. The only "disintermediation" is recycling/scrap, which is already priced into the market and cannot scale to the deficit.
- **Score 8/10** — the orebody+permit moat is close to absolute, but FCX is a **price-taker on a fungible commodity**, which caps it below 9–10. It cannot set price; it can only own the lowest-cost tonnes.

### 5. Recent catalysts (since ~2026-05)
- **2026-07-23: Q2 2026** — EPS $0.74 vs $0.59 (beat 25%), revenue $7.03B vs $6.71B. **Stock fell anyway** — market focused on cost inflation ($1.97/lb) and the slow Grasberg ramp.
- **Grasberg ramp inflecting:** production rates **doubled during Q2, from ~34,000 t/day in April to 69,000 t/day in June.**
- **2027 guidance issued:** copper +>20%, gold +>50%.
- **2027 capex raised ~$300M to ~$4.8B** — advancing US projects.
- **Bagdad FID expected H2 2026** — near-term catalyst.
- **Copper +51.6% YoY as of 2026-08-04**; records set Jan 2026.
- **Section 232 refined-copper decision window opened 2026-06-30** — a binary US-price catalyst still pending.
- **Negative:** **Morgan Stanley downgraded FCX in April 2026** on Grasberg concerns.

### 6. Risks
- **Grasberg is the single most important variable and it is still unresolved.** The **2025-09-08 mud rush** put ~**800,000 tonnes of wet material** into the block cave and **killed seven workers.** Phased ramp-up recommenced **March 2026**. Recovery has been **repeatedly pushed out**: FCX now expects **~65% of nameplate in H2 2026 (cut from a prior ~85% estimate)**, **80% by mid-2027**, and **approaching full capacity only by year-end 2027.** Any further material-handling problem, seismic event or Indonesian regulatory action resets the whole thesis. Indonesian government/PTFI ownership and export-permit politics are a persistent overhang.
- **Copper price reversal:** Macquarie sees surpluses 2026–28; Goldman sees prices declining from records. A move back to $4.50/lb would halve FCX's earnings power.
- **Tariff reversal:** if the refined-copper exemption is made permanent, the ~30% COMEX premium and the record COMEX stockpile could unwind violently.
- **Cost inflation:** unit cash costs went $1.13 → $1.97/lb YoY. Even at guided $1.90/lb, margin compression is real, and $284M of excluded idle/restoration cost is still cash out the door.
- **Valuation:** analyst mean target $72 = **only +6.6%** upside. The sell side does not think copper upside is unrecognized.

### Reconciling ~1% TTM revenue growth with the copper bull case (explicitly asked)
**These are consistent, and the reconciliation is the actual investment case.**
- **Price up ~50%, volume down ~25% → revenue roughly flat.** Copper is +51.6% YoY, but Grasberg has been offline/ramping since Sept 2025, cutting 2026 copper sales guidance to **3.1 Blb (from ~3.4 Blb)** and gold to **650 koz (from ~0.8–0.9 Moz)**. Grasberg is FCX's highest-margin, lowest-cost, gold-credit-rich production — losing those tonnes hurts margin more than revenue. That is also why unit cash costs blew out to $1.97/lb: fixed costs spread over far fewer PTFI pounds.
- **So TTM revenue growth of 1% is not evidence the copper thesis is broken — it is evidence that FCX has been running the copper bull market with one engine out.**
- **The setup:** 2027 guidance is copper **+>20%** and gold **+>50%** on a volume base that is currently depressed, landing into a copper price that is +50% and a possible US refined-copper tariff. That is **operating leverage stacked on price leverage** — the classic explosive-return configuration. Modeled EBITDA of $13–20B against a **$91B market cap** frames the upside.
- **The risk symmetry:** it requires Grasberg to actually ramp on the stated schedule (65% H2'26 → 80% mid-'27 → ~100% YE'27) *and* copper to hold. Both have to go right. Q2's April→June doubling (34k → 69k t/day) is the first hard evidence the ramp is real.
- **Screen-metric check:** rev growth TTM 1% is corroborated and correctly explained. Fwd PE 15.6 vs consensus 2026 adj EPS of **$2.56** (+44.6% vs $1.77 in 2025) implies ~26x on 2026 — the 15.6x figure is presumably on 2027 normalized earnings. **Flagging this: the "15.6 fwd PE" is doing a lot of work and depends entirely on the 2027 Grasberg recovery being delivered.** Do not treat 15.6x as a current-earnings multiple.

### 7. Score & verdict
**Shortage 8/10 · Irreplaceability 8/10**
> The copper deficit thesis is intact and FCX owns irreplaceable orebodies behind a 17-year, $22k/tonne replacement barrier, but the entire explosive-return case rests on Grasberg ramping from 65% to full capacity by end-2027 — Q2's doubling of daily rates says it is working, and 2027 stacks +20% copper and +50% gold volume onto a +50% price.

---

# 4. CF — CF Industries

**Latest reported quarter:** **Q1 2026** (Mar-qtr), reported **2026-05-06**.
> ⚠️ **Q2 2026 has NOT yet been reported as of 2026-08-04.** CF reports **Q2/H1 2026 after the close on Wednesday 2026-08-05**, with the call at 11:00am ET **Thursday 2026-08-06**. **This is an imminent binary catalyst — within 24 hours of this dossier.** Consensus: **EPS $5.65, revenue $2.45B.**

**Q1 2026 (reported 2026-05-06):**

| Metric | Q1 2026 | Q1 2025 | Note |
|---|---|---|---|
| Net earnings to common | **$615M ($3.98/sh)** | $312M ($1.85/sh) | ~2x YoY |
| EBITDA | $1.01B | $617M | |
| Adjusted EBITDA | **$983M** | $644M | +53% |
| Special item | **+$170M litigation settlement gain** | — | ~$1.10/sh of the $3.98 — **not recurring** |
| Realized nat gas cost | **$4.57/MMBtu** | $3.68 | **-$76M earnings impact** |
| Buyback | 150,000 sh for **$15M** | — | **Very slow** |
| Authorization remaining | **$1.7B** (expires Dec 2029) | — | |
| TTM operating cash flow | ~$2.7B | — | TTM FCF ~$1.65B |

Beat consensus. Note the quality caveat: **~$170M of the quarter was a one-off litigation settlement.**

**Forward guidance given:** 2026 consolidated capex **~$1.3B** — ~$550M for existing operations + ~**$600M for Blue Point JV construction**. Management: geopolitical disruptions have left **global nitrogen markets tight, expected to persist through 2026 and into 2027.**

### 1. Shortage thesis — score 6/10
**This is the weakest shortage case in the batch — it is a tight cyclical market with a durable cost advantage, not a structural shortage.**
- **Tightness is real but cyclical:** CF states ammonia ASPs rose in 2026 vs 2025 on a **tight global nitrogen supply-demand balance, further tightened by conflict-related supply disruptions.** Israel-Iran tensions threaten a region critical to global gas and ammonia production and to Suez shipping routes linking North African/Gulf producers to European and American buyers.
- **Current pricing:** **Tampa ammonia settled ~$487/tonne in August 2026**, with indications of **higher September prices**. Urea rose sharply into summer 2026 then **eased modestly**; global urea markets have been **cooling on affordability pressure** (early Aug 2026).
- **The durable part — the gas-cost moat, which IS structural:**
  - **Henry Hub ~$3.25/MMBtu (2026-07-01)**, $2.97 in June 2026; EIA expects HH to fall ~2% to just under **$3.50/MMBtu average in 2026** before rising in 2027.
  - **European TTF ~€43.51/MWh (2026-07-01)**, down from €48.82 in June — roughly **$14–16/MMBtu equivalent**, a **4–5x** multiple of Henry Hub.
  - Global nitrogen pricing is **set by the marginal ton produced in Europe or Asia on LNG at $12–15/MMBtu**, while CF produces at **~$3.31/MMBtu realized (2025)** / $4.57 (Q1 2026).
  - **Natural gas is 70–90% of variable production cost** for nitrogen. Every dollar of HH-TTF spread flows to CF's gross margin. **This is the real, structural, durable edge — and it is a cost moat, not a shortage.**
- **Why only 6:** nitrogen has no order book, no lead times, no sold-out capacity, and prices are already **cooling on affordability**. Unlike compute or copper, nitrogen supply *can* be added — and is being added (see risks).

### 2. Backlog / order book
- **No meaningful backlog disclosure found** — CF sells into spot and short-dated forward markets. Forward order book: **not found** as a disclosed figure.
- **Contracted clean-ammonia offtake:** offtake is handled **independently by each JV partner pro rata to ownership** (CF 40% / JERA 35% / Mitsui 25%). JERA has **secured offtake from new low-carbon ammonia demand sources and received Contract-for-Difference (CfD) awards from the Japanese government** — real, government-underwritten demand, but it accrues largely to the partner's share. **A specific contracted volume/tonnage for CF's own 40% share: not found.**
- **This is the structural weakness vs the other three names: there is no visibility number.**

### 3. Category position — clear #1
- **Largest nitrogen fertilizer producer in North America.**
- **Six US complexes, two Canadian, one UK; ~10.5 Mt/yr gross ammonia capacity.**
- Share of North American capacity (per company filings): **~37% ammonia, ~34% granular urea, ~45% UAN, ~21% AN.** CF's strongest position is **UAN at ~44–45%** — near-half of the continent.
- **Donaldsonville, LA** is the **largest nitrogen complex in the US** (1,400 acres, ~5 Mt of nitrogen products, six ammonia plants) and the world's largest and most flexible ammonia complex.
- Unambiguously **#1, with no close #2** in North American nitrogen.

### 4. Irreplaceability / disintermediation — score 6/10
- **Capital/time barrier:** **Blue Point costs ~$4.0B and takes from 2026 construction start to 2029 production — 3–4 years** for **~1.4 Mt/yr nameplate (>1.5 Mt gross)**. So a world-scale ammonia plant is **~$2,700–2,900 per tonne of annual capacity and ~4 years.** Compare copper: ~$22,359/tonne and ~17 years. **Ammonia is roughly one-eighth the capital intensity and one-quarter the lead time of copper.** That is the quantified reason CF's moat is materially weaker than FCX's.
- **Permitting:** US Gulf Coast permitting for ammonia is far easier than for a mine — Blue Point was described as moving forward at "Trump speed."
- **Location moat is the real one:** Donaldsonville's scale, its integration into the US pipeline/barge/rail logistics network, and Henry Hub feedstock access cannot be replicated in Europe or Asia at any price — geography is the moat, not the plant.
- **Disintermediation:** farmers cannot in-source ammonia. But **customers can and do buy imported tons** — nitrogen is a globally traded, fully fungible commodity. Chinese urea export policy alone can reset North American pricing. This is genuine bypass risk that FCX does not face to the same degree (copper is also fungible, but nobody can quickly add copper supply).
- **Score 6/10** — #1 position and an unassailable *cost* position, but a replicable *asset* and a fungible product.

### 5. Recent catalysts (since ~2026-05)
- **2026-05-06: Q1 2026** — net earnings $615M / $3.98 EPS vs $312M / $1.85; adj EBITDA $983M (+53%). Beat.
- **Dividend raised 20% to $0.60/quarter.**
- **Blue Point construction commencing in 2026**; ~$600M of CF's 2026 capex.
- **Scotiabank raised PT to $115 from $85** (Sector Perform maintained) on nitrogen supply outlook.
- **Mizuho DOWNGRADED to Underperform from Neutral, PT $100 (from $95)** — argued gains driven by surging oil/fertilizer prices are overdone.
- **Zacks and others raised FY2026 EPS estimates (early July 2026).** Consensus FY2026 EPS **~$15.87**; Scotiabank $16.20.
- **Stock up ~55% in calendar 2026** per press coverage — though it is now **-14% from its 52-week high**, i.e. it has already given back a chunk.
- **IMMINENT: Q2 2026 earnings 2026-08-05 after close** (consensus EPS $5.65 / revenue $2.45B).

### 6. Risks
- **New supply is coming, and management's own project is part of it.** Analysts flag **new US Gulf Coast ammonia capacity additions** that may weaken pricing power — and CF is building 1.4 Mt of it. In a fungible commodity, being #1 does not protect you from the marginal ton.
- **Chinese urea exports.** H2 2026 is expected to bring **increased Chinese urea exports plus the normal seasonal slowdown** — the two most reliable historical triggers for nitrogen price breaks.
- **Affordability ceiling.** Global urea markets were already **cooling on affordability pressure** as of early Aug 2026. Farmer economics cap how long high nitrogen prices persist.
- **Nat-gas spike.** Realized gas went $3.68 → **$4.57/MMBtu** YoY, a **-$76M** hit in a single quarter. EIA sees HH **rising in 2027**. CF's entire edge is the HH-TTF spread; a US gas spike (LNG export growth, cold winter, datacenter power demand) compresses it directly. **This is the most under-appreciated risk** — AI datacenters bidding for US gas is a direct negative for CF and a direct positive for MSFT/GOOGL, an amusing internal hedge within this batch.
- **Peace/de-escalation risk.** A meaningful share of current tightness is conflict-driven. Resolution of Israel-Iran or Russian/Ukrainian ammonia flows would remove it quickly.
- **Buyback has effectively stopped.** Only **$15M / 150k shares in Q1 2026** with **$1.7B still authorized.** For a company generating **~$1.65B TTM FCF** and a **$18B** market cap, buying back $15M in a quarter is a near-zero pace. Management is redirecting cash to Blue Point capex. **This removes a major prior support for the stock** — CF's historical equity story was aggressive share-count reduction, and that engine is currently idling.

### Why only a "hold" with +6% to target — explanation (explicitly asked)
The sell-side view is coherent and worth taking seriously:
1. **Consensus rating is Hold** — of 11 analysts, **27% Buy / 55% Hold / 18% Sell.** Note there is an *active Sell contingent* (Mizuho at Underperform), which is unusual and meaningful.
2. **Peak-cycle earnings.** Analysts are marking CF at or near a cyclical peak: nitrogen prices are elevated on conflict-driven disruption, and the standard commodity-analyst discipline is to apply a *low* multiple to *peak* earnings. Hence a $125 target on ~$15.87 of 2026 EPS = **~7.9x peak earnings** — the multiple is doing the de-rating.
3. **The stock has already run.** Up ~55% in 2026, +32% over 12 months. Much of the tightness is in the price.
4. **H2 2026 has identifiable negative catalysts** (Chinese urea exports, seasonal slowdown, new Gulf Coast supply).
5. **Capital is going into the ground, not to shareholders** — Blue Point absorbs ~$600M of 2026 capex and the buyback has stalled, with no cash-return offset until 2029 production.

**Screen-metric discrepancy — flagging explicitly:**
- Screen says **fwd PE 10.5**. But **FY2026 consensus EPS is ~$15.87** (Scotiabank $16.20). At $118.11 that is **~7.4x**, not 10.5x. The 10.5x figure is only reachable on ~$11.25 of EPS — i.e. **the "forward" multiple is being computed on a 2027 estimate that assumes nitrogen prices normalize ~30% lower.** Two readings: (a) CF is genuinely cheaper than the screen shows on current earnings, or (b) the screen is already correctly telling you the market does not believe 2026 earnings are sustainable. **Both are the same fact viewed from opposite ends, and it is the crux of the CF debate. Do not treat 10.5x as a cheapness signal without resolving which year it is on.**
- Separately, one source cited a Simply Wall St 2026 EPS estimate of **$19.06** — inconsistent with both the $15.87 consensus and with CF's ~$2.5–3B EBITDA base against ~145M shares. **Treat $19.06 as unreliable; use ~$15.87.**
- Press reports "stock surged 55% in 2026" (YTD) vs screen ret_12m +32% — these are different windows and are reconcilable given the stock is now -14% off its 52-week high.

### 7. Score & verdict
**Shortage 6/10 · Irreplaceability 6/10**
> CF is the cheapest and highest-current-cash-flow name here with an unassailable #1 North American position and a structural 4-5x Henry Hub vs TTF feedstock advantage, but nitrogen is a fungible, replicable commodity with no backlog, new Gulf Coast supply coming, a stalled buyback and conflict-driven pricing — it is a well-run cyclical at a cycle high, not a structural shortage.

---

# CROSS-CUTTING NOTES

**Ranking for an explosive-return momentum mandate:**
1. **FCX** — highest asymmetry. Depressed volume base + 2027 guided +20% Cu / +50% Au + 50% higher price + a possible US refined-copper tariff, on a $91B cap. Requires Grasberg to deliver; Q2 evidence says it is.
2. **GOOGL** — highest quality shortage evidence and best backlog ($514B, ~5 yrs of run-rate) plus a genuinely unique silicon-to-model stack, but $4.6T caps the percentage return.
3. **MSFT** — best risk-adjusted, worst explosive-return odds. You are buying 32% EPS growth at 20.8x after a de-rate; the market has to stop worrying about depreciation for the multiple to help.
4. **CF** — cheapest optically, weakest thesis. Cyclical tightness, not shortage. Q2 print 2026-08-05 is a coin-flip catalyst.

**Internal hedge worth noting:** AI datacenter power demand bids up US natural gas, which is simultaneously the input cost that determines CF's entire margin. GOOGL/MSFT and CF are, at the margin, on opposite sides of the same Henry Hub trade.

**Metrics I could not verify / not found:**
- CF forward order book (no such disclosure exists for CF).
- CF's own contracted clean-ammonia offtake tonnage for its 40% Blue Point share.
- MSFT Q4 FY26 quarterly capex — sources conflict (one gave "$41M," an obvious typo; another reported AI capex "more than doubled to $35.8B"). **Exact Q4 FY26 total capex: not confirmed.**
- Any company-sourced FY27 MSFT capex dollar figure (the $255–260B number is an analyst preview, not guidance).

**Screen metrics I am flagging as questionable:**
- **CF fwd PE 10.5** — inconsistent with ~$15.87 FY26 consensus EPS (implies ~7.4x). Likely computed on a normalized 2027 number. Material to the thesis.
- **FCX fwd PE 15.6** — inconsistent with 2026 consensus adj EPS of $2.56 (implies ~26x). Likely a 2027 post-Grasberg-recovery number. Material to the thesis.
- **GOOGL HIGH_ACCRUALS** — flag is technically correct but economically misleading; driven by a $77.1B non-cash equity mark. See detailed verdict above.
- GOOGL fwd PE 25.3 and MSFT fwd PE 20.8 both look consistent with sources.

---

## SOURCES

**GOOGL**
- [Alphabet Announces Second Quarter 2026 Results (8-K/press release, 2026-07-22)](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf)
- [Alphabet Q2 2026 earnings call coverage — BigGo Finance](https://finance.biggo.com/news/US_GOOG_2026-07-22)
- [Alphabet posts $119.8B revenue in Q2 2026; EPS $9.11 as other income nets $98.0B — TradingView](https://www.tradingview.com/news/tradingview:2f065a78e4f80:0-alphabet-posts-119-8b-revenue-in-q2-2026-eps-9-11-as-other-income-nets-98-0b/)
- [Alphabet Q2 2026 profit surges on $99B equity gain — StockTitan 8-K](https://www.stocktitan.net/sec-filings/GOOG/8-k-alphabet-inc-reports-material-event-c600716f9a4d.html)
- [Alphabet earnings takeaways: Q2 revenue beats, GOOGL sinks on 2026 capex hike — CNBC (2026-07-22)](https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html)
- [Anthropic expands partnership with Google and Broadcom for multiple gigawatts of compute — Anthropic](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- [Anthropic Expands Use of Google Cloud and TPUs — Google Cloud Press Corner (2026-04-06)](https://www.googlecloudpresscorner.com/2026-04-06-Anthropic-Expands-Use-of-Google-Cloud-and-TPUs)
- [Google and Anthropic confirm 1GW+ cloud deal with up to 1 million TPUs — DataCenterDynamics](https://www.datacenterdynamics.com/en/news/google-and-anthropic-confirm-massive-1gw-cloud-deal-with-up-to-one-million-google-tpus/)
- [Google and Meta strike multibillion-dollar AI chip deal — SiliconANGLE (2026-02-26)](https://siliconangle.com/2026/02/26/google-meta-reportedly-strike-new-multibillion-dollar-ai-chip-deal/)
- [Meta signs multi-billion dollar deal to rent Google's TPUs — the-decoder](https://the-decoder.com/meta-signs-multi-billion-dollar-deal-to-rent-googles-tpus-in-a-direct-challenge-to-nvidias-ai-chip-dominance/)
- [Federal Court Endorses Behavioral Remedies, Rejects Structural Relief, in Google Search Antitrust Litigation — CRS/Congress.gov](https://www.congress.gov/crs-product/LSB11362)
- [Google appeals search monopoly decision — PYMNTS (2026)](https://www.pymnts.com/google/2026/google-appeals-court-decision-on-search-monopoly/)
- [Google Search Remedy to be Appealed by State Attorneys General — Bloomberg (2026-02-03)](https://www.bloomberg.com/news/articles/2026-02-03/google-search-remedy-to-be-appealed-by-state-attorneys-general)

**MSFT**
- [Microsoft FY26 Q4 Press Release — Microsoft Investor Relations (2026-07-29)](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast)
- [Microsoft Corp (MSFT) Q4 2026 Earnings Call Highlights — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/microsoft-corp-msft-q4-2026-050436699.html)
- [Microsoft Fiscal Year 2026 Fourth Quarter Earnings Conference Call — Microsoft IR](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- [Microsoft surges on strong revenue outlook, maintained capex guidance — Investing.com](https://www.investing.com/news/earnings/microsoft-beats-on-profit-and-revenue-shares-rise-after-hours-4821565)
- [Microsoft's AI Capex Cycle Is Repricing the Stock's Cash Flow Premium — Investing.com](https://www.investing.com/analysis/microsofts-ai-capex-cycle-is-repricing-the-stocks-cash-flow-premium-200682893)
- [Why Microsoft Stock Is Falling: AI Capex and OpenAI Risk — INDmoney](https://www.indmoney.com/blog/us-stocks/why-microsoft-stock-is-falling-ai-capex-openai-risk-analysis)
- [Microsoft Q3 FY2026: The $190B Capex Plan That Repriced AI — Global Data Center Hub](https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex)
- [Maia 200: The AI accelerator built for inference — Official Microsoft Blog (2026-01-26)](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)
- [Microsoft AI Self-Sufficiency: MAIA 200 and Fairwater — Windows Forum](https://windowsforum.com/threads/microsoft-ai-self-sufficiency-diversifying-with-mai-maia-200-and-fairwater.401112/)
- [Cloud infrastructure market share (Synergy Research) — CloudZero](https://www.cloudzero.com/blog/cloud-service-providers/)

**FCX**
- [Freeport-McMoRan Q2 2026 8-K / press release — StockTitan (2026-07-23)](https://www.stocktitan.net/sec-filings/FCX/8-k-freeport-mcmoran-inc-reports-material-event-4d50c58d801a.html)
- [FREEPORT-MCMORAN INC Form 8-K Q2 2026 Exhibit 99.1 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0000831259/000083125926000033/a2q2026exhibit991.htm)
- [FREEPORT-MCMORAN INC Form 8-K Q2 2026 conference call — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0000831259/000083125926000033/fcx2q26cc_final.htm)
- [FCX Q2 Earnings Call Highlights Grasberg Ramp and U.S. Growth — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/fcx-q2-earnings-call-highlights-140000464.html)
- [Freeport-McMoRan Earnings Call Highlights Copper Upside — TipRanks](https://www.tipranks.com/news/company-announcements/freeport-mcmoran-earnings-call-highlights-copper-upside)
- [Freeport Provides Update on Restart Plans for Grasberg Minerals District — FCX IR](https://investors.fcx.com/investors/news-releases/news-release-details/2025/Freeport-Provides-Update-on-Restart-Plans-for-Grasberg-Minerals-District/default.aspx)
- [Freeport says it's on track to restart Grasberg after deadly mudslide — MINING.COM](https://www.mining.com/web/freeport-says-its-on-track-to-restart-grasberg-copper-mine-after-deadly-mudslide/)
- [Morgan Stanley Downgrades Freeport-McMoRan (April 2026) — 24/7 Wall St](https://247wallst.com/investing/2026/04/24/morgan-stanley-downgrades-freeport-mcmoran-is-the-copper-story-breaking-down-at-grasberg/)
- [Bagdad Mining Complex Expansion — The Mining Record](https://miningrecord.com/bagdad-mining-complex-expansion-to-increase-production-to-250-million-pounds-per-year/)
- [Freeport CEO pushes for US incentives to expand copper — MINING.COM](https://www.mining.com/freeport-ceo-pushes-for-us-incentives-to-expand-copper/)
- [Copper price and 1-year change — Trading Economics (2026-08-04)](https://tradingeconomics.com/commodity/copper)
- [Discovery to production averages 15.7 years for 127 mines — S&P Global Market Intelligence](https://www.spglobal.com/market-intelligence/en/news-insights/research/discovery-to-production-averages-15-7-years-for-127-mines)
- [Capital demands soar for new copper supply — S&P Global Market Intelligence](https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/12/capital-demands-soar-for-new-copper-supply)
- [Copper Prices Forecast to Decline Somewhat from Record Highs in 2026 — Goldman Sachs](https://www.goldmansachs.com/insights/articles/copper-prices-forecast-to-decline-from-record-highs-in-2026)
- [Period of elevated copper prices overextended: analysts — S&P Global](https://www.spglobal.com/energy/en/news-research/latest-news/metals/010726-period-of-elevated-copper-prices-overextended-analysts)
- [President Trump orders 50 percent Section 232 tariff on copper imports — White & Case](https://www.whitecase.com/insight-alert/president-trump-orders-50-percent-section-232-tariff-copper-imports)
- [Section 232 National Security Tariffs on Copper Imports — CRS/Congress.gov](https://www.congress.gov/crs-product/IN12614)
- [Adjusting Imports of Copper Into the United States — Federal Register (2025-08-05)](https://www.federalregister.gov/documents/2025/08/05/2025-14893/adjusting-imports-of-copper-into-the-united-states)

**CF**
- [CF Industries Reports First Quarter 2026 Net Earnings of $615M, Adjusted EBITDA of $983M — Businesswire (2026-05-06)](https://www.businesswire.com/news/home/20260506162870/en/CF-Industries-Holdings-Inc.-Reports-First-Quarter-2026-Net-Earnings-of-$615-Million-Adjusted-EBITDA-of-$983-Million)
- [CF Industries Holdings Form 8-K Q1 2026 earnings exhibit — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001324404/000132440426000011/cf-05062026_ex991xearnings.htm)
- [CF Industries Holdings Form 10-Q FY2026 (period ended 2026-03-31) — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001324404/000132440426000013/cf-20260331.htm)
- [CF Industries (CF) Q1 2026 Earnings Transcript — The Motley Fool (2026-05-07)](https://www.fool.com/earnings/call-transcripts/2026/05/07/cf-industries-cf-q1-2026-earnings-transcript/)
- [CF Industries Q1 2026 slides: earnings beat amid tight nitrogen markets — Investing.com](https://www.investing.com/news/company-news/cf-industries-q1-2026-slides-earnings-beat-amid-tight-nitrogen-markets-93CH-4670512)
- [CF Industries Announces JV with JERA and Mitsui for Low-Carbon Ammonia — CF Industries](https://www.cfindustries.com/newsroom/2025/blue-point-joint-venture)
- [Blue Point Complex — CF Industries](https://www.cfindustries.com/bluepoint)
- [Project Blue Point: $3.7–4 Billion World's Largest Low-Carbon Ammonia Plant — Energy News Beat](https://energynewsbeat.co/agriculture/project-blue-point-3-7-4-billion-worlds-largest-low-carbon-ammonia-plant-moves-forward-in-louisiana-at-trump-speed/)
- [CF Industries Announces Planned Schedule for Quarterly Financial Results in 2026 — CF IR](https://ir.cfindustries.com/Investors/news/news-details/2026/CF-Industries-Holdings-Inc--Announces-Planned-Schedule-for-Quarterly-Financial-Results-to-be-Released-in-2026/default.aspx)
- [CF Industries raises quarterly dividend 20% to 60 cents — StockTitan](https://www.stocktitan.net/news/CF/cf-industries-holdings-inc-announces-20-increase-in-quarterly-7cdif8mjgy1r.html)
- [Scotiabank raises CF Industries price target on nitrogen supply outlook — Investing.com](https://www.investing.com/news/analyst-ratings/scotiabank-raises-cf-industries-stock-price-target-on-nitrogen-supply-outlook-93CH-4623952)
- [Does CF Industries' Cautious Upgrades Reveal a Deeper Shift? — Simply Wall St News (2026-06-02)](https://simplywall.st/stocks/us/materials/nyse-cf/cf-industries-holdings/news/does-cf-industries-cf-analysts-cautious-upgrades-reveal-a-de)
- [What to Expect From CF Industries' Q2 2026 Earnings Report — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/expect-cf-industries-q2-2026-132144055.html)
- [We expect Henry Hub natural gas spot prices to fall slightly in 2026 before rising in 2027 — U.S. EIA](https://www.eia.gov/todayinenergy/detail.php?id=67004)
- [Henry Hub vs TTF Natural Gas: A Trader's Guide to the Spread in 2026 — TradeEdge Pro](https://tradeedgepro.net/henry-hub-vs-ttf-2026/)
- [Fertilizer Outlook: Global Risks, Higher Costs, Tighter Margins — American Farm Bureau Federation](https://www.fb.org/market-intel/fertilizer-outlook-global-risks-higher-costs-tighter-margins)
- [Weekly Update – Global Fertiliser Markets w/e 08.05.2026 — EcoNews](https://econews.com.au/weekly-update-global-fertiliser-markets-w-e-08-05-2026-global-urea-markets-cool-as-affordability-pressure-builds-across/)
- [Key Questions About Fertilizer and Its Price Answered — CF Industries](https://www.cfindustries.com/newsroom/2026/2026-fertilizer-prices-faq)
