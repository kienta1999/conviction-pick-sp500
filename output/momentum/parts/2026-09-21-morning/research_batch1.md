# Momentum Research Dossier — Batch 1 (SNDK / MU / NVDA / KLAC)
RUN_DATE: 2026-09-21. Research subagent. All figures sourced from web search; "not found" where unavailable. Prices: Finnhub/Celsius data as of 2026-09-18 unless noted.

---

## 1. SNDK — Sandisk Corp (pure-play NAND flash)

### Shortage thesis
Structural NAND shortage driven by the AI datacenter buildout: enterprise SSD demand (KV-cache offloading, inference storage) absorbed virtually all production. Concrete evidence: fabs "operate at full capacity" with hyperscalers "paying premium prices to secure additional storage"; company "will reportedly double prices for enterprise 3D NAND SSDs" (blockonomi, ~Feb 2026); 2026 NAND manufacturing capacity "sold out" (blockonomi). TrendForce: NAND contract prices +70–75% QoQ in spring 2026, ~+10–15% in the current quarter; shortage projected through 2027 (biggo, 2026-08-29; options.cafe analysis Mar 2026). Gartner cited estimating NAND flash prices could rise "as much as 234 percent in 2026"; Morningstar's William Kerwin forecast a further ~100% price increase into fiscal 2027 (business-news-today, Jul 2026). Jensen Huang at CES 2026 called storage the "largest unserved market" in AI (options.cafe). Counterpoint Q2 2026: eSSDs jumped to 48% of total NAND shipments vs 26% a year earlier (sammobile, Aug 2026).

### Backlog / order book
No conventional dollar backlog disclosed, but closest proxy: 8 multiyear New Business Model (NBM) agreements with Datacenter/Edge customers, weighted-average duration >4 years, expected to cover **>50% of fiscal 2027 bits and ~two-thirds of fiscal 2028 bits**, with "minimum expected revenues at floor pricing totaling **$93.9 billion**" (Zacks summary of Q4 FY2026 earnings call, Aug 11, 2026; sandisk.com PR, Aug 5, 2026). $16.5B in financial guarantees secured (tradingtips, Aug 2026). Effectively booked years out at price floors.

### Category position
#4–#5 in NAND by revenue share, NOT #1. TrendForce Q2 2026: Samsung 29.3%, SK Hynix+Solidigm 18.2%, Micron 15.1%, Kioxia 13.6%, **Sandisk ~11%** (TrendForce via trendforce.com, Sep 18, 2026; Counterpoint via club386: Samsung 25%, SK Hynix 22%, YMTC/Kioxia 14%, Micron 13%, **Sandisk 11%**). Edge: only pure-play NAND company — Samsung/SK Hynix cannibalize their own NAND capacity for DRAM/HBM while Sandisk grows flash output undivided; spun off with lean $179M TTM capex and $3.7B cash, no net debt (ainvest, Jun 2026).

### Irreplaceability / disintermediation risk — score 6/10
NAND is a commodity; hyperscalers can buy Samsung, SK Hynix, Micron, Kioxia, or YMTC instead. No customer can "in-source" a NAND fab cheaply (multi-billion fab capex + process know-how), but substitution between the five players is real. Moat: BiCS technology leadership — BiCS10 (332-layer, 1Tb, 29Gb/mm², sampling since Jul 3, 2026 with Kioxia, mass production targeted 2027, ~59% denser than BiCS8 at ~10% lower cost/GB), and High Bandwidth Flash (HBF) — a NAND+HBM hybrid architecture with an MoU signed with SK hynix to standardize under OCP (aistockwire; options.cafe). Qualification lock-in on enterprise SSD controllers is meaningful but weaker than HBM qualification.

### Recent catalysts (last ~3 months)
- Q4 FY2026 reported Aug 5, 2026: revenue $8.97B (+51% seq, +372% YoY), beat consensus ~$8.4–8.5B; non-GAAP EPS $39.25 vs ~$34.4–35 expected; non-GAAP gross margin 84.6%; datacenter revenue +103% seq (+437% YoY for the year); guided Q1 FY27 $10.3–10.8B / EPS $44–46 (sandisk.com PR; marketbeat). Stock fell ~13% anyway — guidance midpoint ($10.55B) missed FactSet's $10.8B consensus (tradingtips).
- Signed 5 more NBM agreements since April; revenue shipments of QLC Stargate platform began (Zacks, Aug 11, 2026).
- Board added $14B buyback ($15.5B total remaining authorization) on Aug 5.
- FY2026: revenue $20.25B (+175% YoY), GAAP EPS $73.76 (sandisk.com).

### Risks
- NAND is inherently cyclical: margins went 7% → 51% (options.cafe) and can revert; TrendForce price increases are already decelerating (70–75% → 10–15% QoQ).
- Peak-on-peak valuation: ~$262B market cap (Finnhub, Sep 18, 2026), beta ~3.8–5.2; -35% from the June 2026 all-time high $2,354.39.
- Guidance already punishing: -13% on a mere $250M top-line guidance miss.
- China: YMTC at 14% share, CXMT planning NAND R&D line (Reuters via TrendForce, Sep 18, 2026); consumer NAND pricing softening.
- One class-action alleges coordinated production shift to HBM starving conventional DRAM (targeting Samsung/SK Hynix/Micron; sector headline risk).

### SNDK price-history verification (DATA WARNING confirmed)
The screen's ret_12m of 18.07 is bogus. Sandisk spun off Feb 21, 2025, began trading Feb 24, 2025 (opened ~$40, record low $27.89 in Apr 2025). Finnhub (as of 2026-09-18): current price **$1,791.82**, 52-wk high $2,354.39 (June 2026), 52-wk low $93.54, **1-year return +1,653%**, YTD +655%. MarketBeat: +1,518% over last 12 months from ~$94. It is the #1 S&P 500 performer of 2026 (+600% YTD per biggo, Aug 2026) — the 18.07 figure appears to be a spin-off history artifact and must NOT be used.

### Shortage score: 9/10 — "Explosive fundamental setup at an explosive price: genuine sold-out NAND supercycle with multi-year contracted demand, but the stock has already repriced for perfection and punishes any guidance stumble."

---

## 2. MU — Micron Technology (DRAM + HBM + NAND)

### Shortage thesis
Structural AI-memory shortage: HBM requires ~3x the wafer area of standard DRAM (physical capacity constraint), and Micron can meet only **50–66% of customer bit demand** — "sold out through 2026" with the entire 2026 HBM supply contracted, HBM4 already allocated (CEO Sanjay Mehrotra; aiweekly, Aug 2026; cryptobriefing, Jun 2026). Management expects supply constraints to "persist beyond calendar 2026" and is working on multi-year supply commitments (Tom's Hardware, Dec 2025 earnings call). HBM4 revenue already >$1B, ramping 2x faster than HBM3E (aiweekly). Micron projects the HBM TAM grows from ~$35B (2025) to ~$100B by 2028, outpacing the entire 2024 DRAM market. Q4 FY26 guidance: ~$50B revenue vs ~$11B a year ago, 86% non-GAAP gross margin, EPS ~$31 (insiderfinance, Sep 2026). Crossed $1T market cap in May 2026.

### Backlog / order book
Not a formal backlog, but: **$22B in customer prepayments** collected, and reported **multiyear customer agreements covering ~$22B in memory supply through 2030 with guaranteed floor prices** — a contracted, price-floored order book that de-commoditizes the business (insiderfinance, Sep 2026; aiweekly, Aug 2026). FY2026 capex raised to ~$27B (from $20B) to serve it.

### Category position
#3 in DRAM, closing on #2: TrendForce Q2 2026 — Samsung 39.4%, SK Hynix 24.9%, **Micron 23.3%** (just 1.6pp behind SK Hynix, up from a 6.4pp gap last quarter; fool.com, Sep 10, 2026). HBM: SK Hynix ~58%, Samsung ~21%, **Micron ~23%** — #2 ahead of Samsung but reportedly the thinnest share of Nvidia's HBM4 allocation (cryptobriefing; aiweekly). NAND: #3–4 at ~13–15% (TrendForce Q2 2026: 15.1%). One of only 3 firms on earth making HBM at scale.

### Irreplaceability / disintermediation risk — score 8/10
Customers cannot build HBM/DRAM themselves: only Samsung, SK Hynix, and Micron manufacture HBM commercially (tradingkey, Mar 2026). Moats: extreme capital intensity (>$25B/yr capex), EUV process-tech lead, and Nvidia qualification lock-in (HBM3E sits on Nvidia's H100/H200/Blackwell interposer). No credible in-sourcing threat from hyperscalers; the substitute threat is technology-mix (more inference on ASICs with different memory), not DIY DRAM. Docked 2 points for being the #3 HBM supplier with the thinnest Nvidia allocation — share could be squeezed between SK Hynix and Samsung.

### Recent catalysts (last ~3 months)
- Q3 FY2026 (~Jun 24, 2026): revenue nearly **$42B, quadrupled from ~$9B** a year earlier (beat ~$36B consensus); gross margin >81%; adj. EPS >$25 vs ~$21 expected; guided Q4 ~$50B vs ~$44B consensus (aiweekly, Aug 2026). Q4 earnings due Sep 30, 2026 after close (insiderfinance).
- Raised FY2026 capex to ~$27B; credit rating upgraded to BBB+ (Sep 2026).
- Killed the Crucial consumer brand (Dec 2025) to redirect supply to datacenter — "disappointed" it can't meet demand in all segments (Tom's Hardware).
- Analyst buy reiterated with $1,600 target (Sep 2026).

### Risks
- Deep cyclicality — memory's history is boom/bust; today's 81–86% gross margins are the peak of the cycle by construction.
- HBM #3: thinnest Nvidia HBM4 allocation; SK Hynix leads HBM at ~58%.
- China: CXMT now 7–9.5% of DRAM, entering NAND (Reuters via TrendForce, Sep 18, 2026); price-based share pressure.
- Litigation: June 2026 California class action alleging Samsung/SK Hynix/Micron coordinated a shift from conventional DRAM to HBM, with conventional DRAM prices up ~700% over 4 years (cryptobriefing).
- Stock already volatile: −5–7% around Sep 14 on AI-spending moderation fears; forward P/E 6–12x suggests market still prices cyclicality, which caps rerating until the contracted model is proven.

### Shortage score: 9/10 — "The purest sold-out AI-memory trade: 2026 supply fully contracted at floor prices with prepayments, meeting only half of demand — priced far more sanely than SNDK but still hostage to the memory cycle."

---

## 3. NVDA — Nvidia (AI accelerators + networking)

### Shortage thesis
Compute demand compounding faster than supply can be built. Q2 FY2027 (reported Aug 26, 2026): revenue **$96.2B (+106% YoY)**, datacenter **$89.0B (+117% YoY, +18% QoQ)**; guided Q3 FY2027 to **$108B ±2%** — first $100B+ quarter; guided **~70% FY2028 revenue growth explicitly "supply-constrained"** with "demand materially higher" (stocktitan; bobeskillz; Zacks). Blackwell Ultra the majority of revenue; cloud GPUs "sold out" — "Blackwell sales are off the charts, and cloud GPUs are sold out" (Huang, Nov 2025 Q3 FY26 call, repeated since). $279B in future supply-chain commitments; Vera Rubin (~20% of Q3 datacenter revenue guided) carries 288GB HBM4 per package; $40B/GW revenue per Vera Rubin compute vs $25B/GW Blackwell vs $18B/GW Hopper (bullxbear, Aug 2026). "Supply remains the bottleneck through the end of fiscal 2028."

### Backlog / order book
Nvidia doesn't publish backlog, but committed demand: **$279B in future supply-chain commitments**; OpenAI ~12GW commitment through 2030 (4.25GW initial, via SoftBank); AWS partnership deploying 2M+ GPUs Q2 FY2027–Q2 FY2029; neocloud partners exiting 2026 with 8GW installed (vs 3GW end-2025); sovereign AI tripled YoY (bullxbear, Aug 2026). Earlier: "visibility to $500B of Blackwell+Rubin revenue through end of 2026" (Nov 2025 call).

### Category position
#1 by a wide margin: ~75–81% of AI accelerator revenue in H1 2026 (cryptobriefing, Jul 2026), ~70–80% estimated for 2026 (techtimes, May 2026). #2 AMD at ~5–7%; Intel ~1%. Demand broadened: hyperscale only ~half the business now ("about half of our business… growing 100% a year" — sovereign, neoclouds, AI startups, enterprise) (I/O Fund via Medium, Sep 2, 2026).

### Irreplaceability / disintermediation risk — score 8/10
Moat: CUDA — a decade-plus software ecosystem, NVLink/Spectrum-X networking, full-stack rack systems; training workloads effectively locked in. The REAL threat is its own biggest customers in-sourcing inference: Google TPU v6 Trillium at scale, AWS Trainium2, Microsoft's "Braga" (delayed to 2026), Meta MTIA, OpenAI's first custom chip with Broadcom/TSMC for 2026 production. Custom ASIC shipments growing 44.6% vs 16.1% for GPUs (TrendForce); ASIC-based AI servers 27.8% of AI server shipments in 2026; Nvidia's share expected to slide ~90% → 75–80% by end-2026, with inference share possibly falling toward 20–30% by 2028 (kapualabs; techtimes; druce.ai). Hyperscaler teams openly refer to the "Nvidia tax." Score 8, not 10, because the disintermediation is concrete and already in progress — though Nvidia offsets it with customer diversification and rising $/GW per architecture.

### Recent catalysts (last ~3 months)
- Q2 FY2027 beat Aug 26–27, 2026: EPS $2.22 vs $2.09; revenue $96.2B vs $92.2B expected; stock +8.7% next session, $5.58T market cap (stocktitan). First-ever FY2028 growth guide (~70%).
- Rubin shipping; Vera Rubin at ~20% of Q3 datacenter revenue guided.
- Gross margin flag: Q3 guided to 74.0% from 75.0% as HBM4 costs rise — "AI server prices would rise over 15% for early-2027 shipments because of the memory spike" (temperature2, Aug 2026).
- Jetson Orin Nano 2 announcement (Aug 25) as edge/robotics catalyst.

### Risks
- The central bear case: hyperscaler custom silicon eroding share and pricing, compounding over generations; share already sliding from >95% toward ~75%.
- China: Q3 FY27 guidance assumes **zero** datacenter compute revenue from China — a large addressable market foregone to export controls.
- Valuation: ~$5.6T market cap requires compounding to continue; 70% FY28 growth is explicitly supply-capped, not demand-driven, so any supply hiccup hits the number.
- Margin trajectory: HBM4 content (288GB/GPU) squeezing gross margin from 75% toward a projected 71–72% trough in Q4 FY27 (bullxbear).
- The whole AI-capex durability debate — Nvidia's quarter is now the referendum; a miss reprices the entire chain.

### Shortage score: 9/10 — "Demand 'materially higher' than even a 70%-growth supply-constrained plan can serve; the shortage is real and multi-year, but the disintermediation risk from its own largest customers is the one genuine crack in the thesis."

---

## 4. KLAC — KLA Corporation (process control / inspection & metrology)

### Shortage thesis
Indirect but real: wafer-fab equipment demand outstripping what the industry can deliver. Management: WFE is "literally just as fast as we can go as an industry" — industry capacity, not customer capex, is the binding constraint (Motley Fool Q3 FY26 transcript, Apr 2026). AI raises process-control intensity every node (smaller killer defects, EUV multi-patterning, larger AI die, HBM stacks, hybrid bonding). KLA raised CY2026 WFE outlook to the **low-$150B range** (from >$140B), expects ~20% H2-over-H1 growth and "continued sequential growth into calendar 2027" (Zacks, Jul 29, 2026). Advanced packaging process-control revenue raised to ~$1.1B in CY2026 (+70% YoY); specialty process/PCB/component inspection >+25%.

### Backlog / order book
**$12.57B as of June 30, 2026**, up from $7.86B a year earlier (**+60% YoY**), "due to strong demand driven by the AI infrastructure buildout" (FY2026 10-K, stocktitan, ~Aug 2026). Management expects backlog ~$12.5B giving visibility into late 2026 and 2027 (Zacks). Company itself cautions backlog timing is uncertain (pushouts/cancellations possible).

### Category position
Undisputed #1 in process control: **~56–58% share** (KLA investor day claims ~58%; industry research ~56%), **~7x the nearest competitor** (Applied Materials at ~10% of metrology/inspection), +360bps share gain since 2021 (github.com/kiankyars/chips research). Near-monopolies: reticle/photomask inspection 80%+, patterned wafer inspection 75–80%, optical inspection ~90% per some analyses (ainvest; tradingview). Also took #1 in advanced wafer-level packaging process control in CY2025 (+14pp share, +~70% revenue). Finnhub: price ~$177 (Sep 18, 2026), market cap ~$231B, P/E ~48x; 1-year return ~+69–95%.

### Irreplaceability / disintermediation risk — score 9/10
The highest moat in the batch: fabs cannot in-source inspection — it requires decades of defect-classification data ("algorithmic moat"), optical/e-beam physics, and fab-wide integration where KLA tools are the default reference platform ("choosing whether to maintain compatibility with the process control infrastructure they have already deployed," ainvest). Switching costs are extreme; qualification is at the process level. No customer DIY threat exists; competitors (Onto, Nova, Hitachi High-Tech, ASML/HMI, Lasertec) nibble at niches. Services (~24% of revenue, 13–15% CAGR target) add a recurring floor. Docked 1 point only for cyclicality — in a WFE downturn, orders pause even if the installed base persists.

### Recent catalysts (last ~3 months)
- Q4 FY2026 (Jul 29, 2026): raised WFE outlook; backlog visibility to ~$12.5B; advanced packaging raised to $1.1B (+70% YoY); incremental $7B buyback authorization + 17th consecutive dividend increase; 2030 model: 13–17% revenue CAGR, >90% of FCF returned (zacks; tradingview).
- CEO Wallace Q1 FY26 call: "not enough wafers will be available" to meet AI capex announcements — gating factors prevent overheating (Fool transcript, Oct 2025).
- Simply Wall St (Sep 19, 2026): framed ~27% undervalued on fair value; earnings growth ~19%/yr.

### Risks
- China exposure + tariffs: explicitly flagged as the key margin/demand risk (simplywall.st, Sep 2026).
- Semi-cap cyclicality: WFE is cyclical; backlog admits pushouts; Intel/Samsung fab delays already noted.
- Valuation: ~48x P/E is a premium multiple for an equipment vendor — priced for the 2027 ramp executing.
- Revenue concentration in leading-edge logic/foundry capex decisions by a handful of customers (TSMC, Samsung, Intel, Micron/SK Hynix).

### Shortage score: 7/10 — "Not a scarce consumable, but a sold-out-ish equipment ramp with record backlog (+60% YoY) and WFE growth gated by industry capacity, not demand — the least cyclical-looking equipment cycle in years, priced accordingly at ~48x."

---

## Earnings-quality flags (deterministic screen) — verdicts

- **MU: RECEIVABLES_OUTRUN** — Benign / business-model mechanical. Receivables growing with revenue that went from $9B to $42B YoY (+367%); HBM sold-out on multiyear contracts with **$22B customer prepayments** collected — cash is coming in ahead, not behind. Verdict: growth artifact, not channel-stuffing.
- **NVDA: HIGH_ACCRUALS** — Benign at this growth rate. Revenue +106% YoY with $279B in supply-chain commitments; large accruals (stock comp, inventory commitments for the Rubin ramp, deferred revenue) are the normal accounting footprint of tripling production for supply-constrained demand. Verdict: scale-and-growth artifact; watch it if revenue decelerates while accruals don't.
- **NVDA: RECEIVABLES_OUTRUN** — Benign. 106% YoY revenue growth to creditworthy hyperscalers/sovereigns mechanically inflates receivables; collection risk near zero with this customer base. Verdict: growth artifact.
- **KLAC: RECEIVABLES_OUTRUN** — Benign. Tool shipments bill on milestones/acceptance against a record $12.57B backlog (+60% YoY); receivables naturally lead in a backlog-conversion ramp, and FCF was strong ($622M in FQ3). Verdict: backlog-conversion timing, not credit deterioration.

## Scorecard

| Ticker | Shortage (0–10) | Irreplaceability (0–10) | #1 in category? | 12-mo return (verified) |
|---|---|---|---|---|
| SNDK | 9 | 6 | No (#4–5 NAND, ~11%) | ~+1,650% (NOT 18.07) |
| MU | 9 | 8 | No (#3 DRAM 23.3%, #2–3 HBM ~23%) | ~+250% YTD (screen: verify) |
| NVDA | 9 | 8 | Yes (~75–80% AI accelerators) | large; screen: verify |
| KLAC | 7 | 9 | Yes (~56–58% process control, ~7x #2) | ~+69–95% |

Sources: sandisk.com PR Aug 5 2026; zacks.com Aug 11 2026; tradingtips.com Aug 2026; marketbeat.com; finnhub.io (SNDK price, Sep 18 2026); trefis.com Sep 15 2026; thestreet.com; aiweekly.co Aug 2026; insiderfinance.io Sep 2026; tomshardware.com Dec 2025; tradingkey.com; cryptobriefing.com Jul 2026; fool.com Sep 10 2026; koreajoongangdaily.com; trendforce.com Sep 18 2026; stocktitan.net (NVDA Q2 FY27); zacks.com Aug 27 2026; temperature2.com Aug 26 2026; bullxbear.com Aug 2026; beth-kindig.medium.com Sep 2 2026; techtimes.com May 2026; nova.kapualabs.com; zacks.com Jul 29 2026 (KLAC); fool.com transcripts Apr 2026 / Oct 2025; simplywall.st Sep 19 2026; ainvest.com; github.com/kiankyars/chips.
