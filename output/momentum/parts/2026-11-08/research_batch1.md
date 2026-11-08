> Run by: Muse Spark (muse-spark-1.3) — full panel

# Momentum Research Dossier — Batch 1 (RUN_DATE 2026-11-08)

**Tickers:** ANET (Arista Networks), VLO (Valero Energy), CF (CF Industries), V (Visa Inc.)
**Screen prices (2026-11-08 screen):** ANET $170.80 | VLO $346.45 | CF $119.39 | V $422.65
**Research date:** 2026-11-08. Sources are primary (company releases, earnings calls/transcripts) and reputable press; dates given. Figures not found are marked "not found" — nothing fabricated.

---

## 1. ANET — Arista Networks, Inc.

### 1. Shortage thesis
Yes — a genuine demand-surge shortage, but the shortage is in the *inputs* (switch silicon, wafers, memory, optics) as much as in Arista's own product, and demand is outrunning supply. Driver: AI datacenter buildout — hyperscalers wiring ever-larger GPU clusters with high-speed Ethernet. On the Q1 2026 call (5 May 2026) management said industry-wide shortages across "wafers, silicon chips, CPUs, optics, and memory" were constraining supply, that "demand is outstripping supply in 2026" and shortages were expected to persist "for one to two years." Dell'Oro expects AI back-end switch sales to exceed $100bn by 2030, ~$80bn of it in the next five years. Ethernet has displaced InfiniBand: InfiniBand fell from ~80% share in late 2023 to under one-third by 2025; Ethernet is now over two-thirds of AI back-end switching. Arista's Etherlink AI fabric went from 4–5 cumulative customers in 2024 to 100+ by mid-2026. Concrete evidence of demand exceeding supply: purchase commitments (see §2) nearly tripled YoY; management said on the Q1 call that lead times exceeded 52 weeks for some components ("wafer shortages, supply de-commits and lead times beyond 52 weeks are limiting its ability to fill AI demand" — Fierce Network, 22 Jul 2026). Note the nuance: by Q3 the supply-constraint bear case was easing — management pointed to tangible supply-chain progress — so the shortage is now more a demand signal than a hard production ceiling.

### 2. Backlog / order book
Arista does not use the word "backlog" in filings and does not disclose a customer order book. The closest filed figures (Q3 2026 10-Q, reported 3–4 Nov 2026):
- **Non-cancellable supplier purchase commitments: $11.4bn** (up from $9.7bn at 30 Jun 2026 and $3.6bn a year earlier), of which $2.1bn is due beyond 12 months (vs $0.3bn in June). This is Arista's obligation *to* its suppliers — a supply-side number, not customer orders; quoting it as backlog would invert its meaning.
- **Deferred revenue: $6,839.5m** at 30 Sep 2026, down $26.4m sequentially — the first sequential decline in coverage; $1,715.0m of Q3 revenue (46.9%) came from the opening deferred balance. Only **$943.5m** is binding remaining performance obligations for future product shipments; the rest is multi-year support/service and product held for acceptance clauses.
- Visibility: management still cites ~two quarters of visibility, but has now guided five quarters out (FY2027 outlook issued with Q3).
- AI-fabrics target: at least $3.5bn in 2026, guided to double to ~$7bn in 2027 (per Q3 recap).

### 3. Category position
Historically #1 in data-center Ethernet switching — Arista overtook Cisco as the largest data-center Ethernet switch vendor in 2024 and claimed #1 share in high-speed switching (>10GbE) in Q1 2026. **But it has just lost the narrow DC-Ethernet revenue lead:** Nvidia booked $2.1bn of data-center Ethernet switch revenue in the March 2026 quarter, 21.5% of the market vs Arista's 20.7% (Dell'Oro via DK Street Journal, Aug 2026). So: #1 in high-speed switching overall, #2 (narrowly) in DC Ethernet revenue to Nvidia as of Q1 2026. Cisco is #3 in this segment (its FY2026 hyperscaler AI-infrastructure orders were $9.3bn, but ~40% was optics, putting switching content nearer $5.6bn).

### 4. Irreplaceability / disintermediation risk
**Score: 6/10.** The moat is real but partial and under active attack from both sides.
- Moat: EOS — a single operating system and management stack spanning every box from 1-gig campus to 1.6T AI spines — plus 15+ years of hyperscaler qualification, and co-founding of the Ultra Ethernet Consortium / ESUN open-Ethernet standards. Management/analysts argue hyperscalers cannot easily replicate EOS functionality in-house.
- The hole in the moat: Arista makes **no switch silicon of its own — 100% Broadcom** (Tomahawk front-end + Jericho routing). Broadcom collects whether a hyperscaler buys an Arista box or builds white-box. White-box (Microsoft SONiC, Meta FBOSS on Broadcom-based ODM hardware) is already ~20–25% of DC Ethernet revenue.
- Concrete in-sourcing threat: Nvidia Spectrum-X — Meta adopted Spectrum-X in Oct 2025 and Arista shares lost ~10% in two days; Nvidia's networking revenue topped $31bn in FY ended Jan 2026 and its DC Ethernet share now exceeds Arista's. Cisco named Microsoft and Alibaba as production customers for its Silicon One P200 routing chip (OCP, 12 Oct 2026), with Alibaba running its own Quantum Cat routers on it via open-source SONiC — a live example of hyperscalers routing around branded vendors. Scale-up networking (inside-rack GPU-to-GPU) is Nvidia NVLink's bastion; Arista has no offering until 2027 at the earliest.
- Customer concentration compounds it: Microsoft 26% + Meta 16% = 42% of 2025 revenue (21%+18% in 2023, 15%+20% in 2024).

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, 3 Nov 2026 — a blowout:** revenue $3.66bn, +58.5% YoY, the highest growth since IPO; beat own $3.3bn guidance by +10.8% and consensus ~$3.33bn by +9.8%. Non-GAAP EPS $1.20 vs $1.06–1.08 guided (+11.1%); non-GAAP operating margin 49.1%.
- **Guidance raised for the 4th time in 2026:** FY2026 revenue to ~$13.3bn (+48%, from ~$12.6bn); Q4 2026 guided $3.9–4.0bn. First FY2027 outlook: ~$18.5bn (+38–40%), ~10–13% above the Street's ~$16.4–16.75bn; AI fabrics to double to ~$7bn, campus ~$2bn.
- 1.6-terabit Etherlink platforms in production; 7060X-E7 100-terabit switch named. Shares rose on the print (Finnhub: $159.16 pre-print → $170.80 at 6 Nov close, +7.3% on 6 Nov alone; 1-month return −19.0% before that, so the print was a sharp reversal off a selloff).
- Watch item: one recap downgraded to Hold on the first sequential deferred-revenue decline (Aardvark Labs, Nov 2026).

### 6. Risks
Customer concentration (42% from two customers); Nvidia Spectrum-X share gains and vertical integration (GPU+switch+optics bundle); 100% dependence on Broadcom silicon; white-box/SONiC in-sourcing by Microsoft/Meta; deferred revenue's first sequential decline as a possible demand-cooling signal; valuation — ~41x FY2026 estimates, ~30x 2027 guide even after the selloff; AI-capex cyclicality if hyperscaler spending pauses; scale-up networking gap until 2027.

### 7. Shortage score & verdict
**Shortage score: 8/10. Verdict:** The strongest genuine AI-infrastructure shortage story in this batch — demand is demonstrably outrunning supply and growth just printed +58.5% — but it is a systems integrator's shortage, not a silicon owner's: Nvidia has already taken the DC-Ethernet revenue lead and the two biggest customers could white-box around it.

---

## 2. VLO — Valero Energy Corp.

### 1. Shortage thesis
Yes — a structural refined-products shortage, concentrated in diesel/distillate, driven by capacity destruction rather than a demand boom. Drivers: (a) refinery closures/conversions — ~1.235m b/d of U.S. crude processing capacity removed (~6.5% of operable capacity, 18.4m b/d in Jan 2025), including LyondellBasell Houston 263,776 b/d (closed early 2025), Phillips 66 Los Angeles 138,700 b/d (by end-2026), and Valero's own Benicia 145,000 b/d (idled Apr 2026); California alone lost ~17–18% of capacity (Benicia + Rodeo/Martinez conversions). (b) Geopolitics: the Iran war / Strait of Hormuz disruption and Ukraine conflict lifted freight and crude differentials — VLCC Gulf Coast→Asia freight ~$30–35/bbl vs ~$5/bbl 2025 average. (c) No new capacity: U.S. plants run 95–100% of capacity (API CEO, Oct 2026; EIA utilization 93.4% w/e 16 Oct, 2026 high 98.0% in late Aug) and new builds take years. EIA forecasts distillate inventories at their lowest since 2000 in 2026. Concrete price evidence: Valero's refining margin hit $39.24/bbl in Q3 2026 — a 20-year high and ~3x the $13.14 of Q3 2025; the 3-2-1 crack spread averaged >150% higher YoY in Jul–Sep; California wholesale gasoline trades ~$26/bbl (~63¢/gal) over the Gulf Coast. COO Gary Simmons (Q3 call): simpler Asian refiners make only ~$2–3/bbl after freight — "high confidence that this current crack spread environment is very sustainable."

### 2. Backlog / order book
**Not applicable / not found.** Refiners do not carry an order book — product is sold into spot/contract wholesale markets as it is produced. The analogue is utilization + inventories: throughput ~2.97m b/d in Q3 2026 at near-record utilization; Q4 throughput guided 2.875–2.975m b/d (Gulf Coast 1.855–1.905m b/d). No backlog figure exists to quote.

### 3. Category position
**#1 global independent refiner** (company statement; 14 refineries, ~3.0m b/d throughput capacity across U.S., Canada, UK). In the U.S. specifically it is **#2 by capacity** behind Marathon: EIA (Jan 2025 data) — Marathon 2.96m b/d (16% of U.S. total, 13 refineries) vs Valero 2.2m b/d (12%, 13 refineries at that count); ExxonMobil #3 at 1.96m b/d (10.6%). Valero's edge vs Marathon is complexity and Gulf Coast concentration (~55% of capacity), giving feedstock flexibility into discounted heavy/sour crude, plus the largest renewable-diesel (Diamond Green Diesel JV) and ethanol (12 plants, 1.7bn gal/yr) footprint among independents.

### 4. Irreplaceability / disintermediation risk
**Score: 5/10.** The moat is capital intensity and permitting — nobody builds a new U.S. refinery (no greenfield refinery in decades; restarts of idled plants are "a tough challenge" per Energy Secretary Wright, Oct 2026) — and Valero's complex Gulf Coast plants can process crude grades simple refiners cannot. But the product is a fungible commodity: gasoline/diesel molecules are identical whoever refines them, customers are price-takers, and there is no technology lock-in, patent moat, or qualification barrier. The "shortage" protects margins only while capacity stays shut; any restart (Benicia permits are being kept; St. Croix has a public restart target), new international capacity, or demand destruction (EV adoption, recession) unwinds it. The U.S. government is actively pushing restarts and cheaper diesel — political risk cuts both ways.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, 22 Oct 2026 — record quarter:** net income $6.8bn / $23.89 per diluted share vs $1.1bn / $3.53 a year earlier; adjusted EPS $23.90 beat consensus $21.28 (+~13%). Revenue $46.1bn, +43.3% YoY. Refining operating income $8.8bn vs $1.6bn. Operating cash flow ~$6.9bn. Second straight record quarter.
- Renewable Diesel swung to +$353m operating income (from −$28m); Ethanol record production 4.8m gal/day, +$272m (from $183m).
- St. Charles FCC optimization completed on schedule/within budget; Port Arthur diesel hydrotreater (damaged Mar 2026) expected back by year-end, largely insurance-covered. 2026 capex guidance held ~$2.0bn; Q4 a light-maintenance quarter supporting high utilization.
- Market reaction is the tell: despite the record print, VLO fell 2.4% on the day and another 1.6% the next, with MPC/PSX down too — investors trading a margin peak, not the quarter. Diesel crack has already dipped below $100 after a record near $112.
- Washington pressure: Energy Secretary Chris Wright publicly pushing refinery restarts and more diesel (Oct 2026) — headline risk to the margin story.

### 6. Risks
Extreme cyclicality — the entire thesis is a crack spread, and spreads are mean-reverting; Q3's $39.24/bbl is ~3x the year-ago level and already off its peak. Political intervention (SPR releases, restart pressure, California margin caps under SB X1-2/ABX2-1). Demand destruction: U.S. wholesale gasoline +4% / distillate +2% YoY in Q3 shows none yet, but a recession or faster EV adoption hits volumes. War-premium reversal: if the Iran conflict de-escalates, freight normalizes ($30–35 → $5/bbl) and Gulf crude discounts narrow. RFS compliance costs: market RVO cost topped $14/bbl in Q3 (vs $3.39 in Q2 2024) — Valero's net cost is only $2.61/bbl thanks to in-house RINs, but policy change is a swing factor. Valuation: +107.9% over 12 months and fwd PE 6.5x on peak earnings — cheap on today's earnings, expensive if earnings normalize. Own capacity decisions cut both ways: Benicia's closure cost an estimated $1.6–2.2bn of forgone margin since shutdown (UC Berkeley Energy Institute, 26 Oct 2026) — Valero idled a plant into the best margin environment in 20 years.

### 7. Shortage score & verdict
**Shortage score: 7/10. Verdict:** A real, documented distillate shortage with record margins and 95–100% utilization — but it is a cyclical commodity spike priced off a war premium, and the market is already fading it: record earnings, falling stock. Explosive upside requires the shortage to persist, not just exist.

---

## 3. CF — CF Industries Holdings, Inc.

### 1. Shortage thesis
Yes — a genuine, war-driven nitrogen shortage layered on structural tightness. Drivers: (a) Middle East war: since hostilities began late Feb 2026, ~9m metric tons of urea supply lost; Middle East urea exports cut roughly in half (normal 1.5–1.7m t/month → ~800k t/month incl. Oman); QAFCO (world's largest single-site urea producer, ~5.6–5.8m t/yr, ~14% of globally traded urea) shut by strikes on Qatar's Mesaieed/Ras Laffan complexes in Mar 2026; Strait of Hormuz complications persist. (b) Europe: >35% (37% in Oct) of ammonia capacity curtailed/offline on high natural-gas costs; Trinidad permanently shutting 35% of its ammonia capacity; European shutdowns may come 12–18 months earlier than expected. (c) Demand resilient: nitrogen purchases rebounded in Q3 across Americas, Europe, India on higher corn/wheat prices despite low channel inventories; India to import >10m t of urea in 2026; global inventories low across North America, South America, Europe, SE Asia. Concrete price evidence: Middle East granular urea $436–494/t (late Feb) → $604–710/t by 19 Mar 2026 (+40–74%); urea futures peaked $684/t, highest since Oct 2022; CF's own ammonia averaged $677/t in Q2 (+50% YoY), granular urea +29%, UAN +37%; Q3 ammonia price $532/t, +27% YoY. New plants take 3–4 years to build — no rapid supply response; CF expects the balance "to tighten long term" and pricing "positive through at least H1 2027." CF's structural edge: U.S. Henry Hub gas (~$3.37/MMBtu realized) vs European gas at €81.69/MWh — the global price is set by the high-cost producer, CF banks the spread.

### 2. Backlog / order book
CF does not disclose a dollar backlog. The closest order-book evidence (Q3 2026 call, 5 Nov 2026): **"its order book extended into the first quarter of 2027"** (UAN fill program), and participation in the fall ammonia program was "very strong" with volumes potentially among the highest of the past 10 years (weather permitting). Shipped nearly 2m tons of UAN in Q3 — highest quarterly UAN volume of the decade. Sales volume +7% YoY to 4.799m product tons (would have been ~+13% ex-Yazoo City outage). No quantified backlog figure — **not found** as a dollar number.

### 3. Category position
**#1 in North American nitrogen, world's largest ammonia producer.** CF controls ~35–40% of U.S. nitrogen market share by one estimate (~35% nitrogen share; Farm Doc Daily via RRFN, May 2026: CF ~40% of U.S. ammonia production capacity vs Nutrien #2 at 16%). By broader U.S. agricultural macronutrients share, CF leads at 16–19% vs Nutrien 14–17% (BIS Research, 2025). Donaldsonville, Louisiana is the world's largest nitrogen/ammonia complex; CF operates 17 ammonia plants across 9 complexes globally. Next-largest North American rival is Nutrien; Koch Fertilizer is also a major producer.

### 4. Irreplaceability / disintermediation risk
**Score: 7/10.** The moat is scale + cost-curve position + logistics, not technology: nitrogen fertilizer is a commodity molecule (no patent/qualification lock-in — any ammonia is fungible), but (a) CF sits at the bottom of the global cost curve on cheap Henry Hub gas while the marginal price-setter pays European/Asian LNG or coal prices; (b) Donaldsonville is the world's largest complex with a pipeline/barge/terminal distribution network no rival can replicate quickly; (c) new capacity takes 3–4 years and ~$3.7bn per world-scale plant (cf. Blue Point One, 1.5m t nitrogen-equivalent, production from 2029, $3.7bn); (d) low-carbon premium: ~10% of H1 volumes sold as low-carbon ammonia at >$20/t premium, ~1m tons contracted to JERA/Mitsui, Donaldsonville CCS sequestering 2m t CO2/yr with 45Q credits. Customers (farmers/distributors) cannot in-source — they cannot build ammonia plants. The real "substitute" is demand destruction: high nitrogen prices vs corn prices (nitrogen-to-corn ratio hit a six-year high of 0.20 in Mar 2026) can cut application rates, and precision-ag / biologicals nibble at the margin — but there is no substitute for nitrogen in high-yield corn/wheat at scale.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, 4–5 Nov 2026:** net sales $1.86bn (+12% YoY); net earnings $436m, EPS $2.87 (vs $2.19, +24% net); adjusted EBITDA $833m (+25%); gross margin $720m. 9M 2026 adjusted EBITDA ~$3.0bn; TTM operating cash flow $3.08bn, FCF $2.03bn.
- Ammonia capacity ran at **97% utilization** YTD (98% in H1); ~9.5m t ammonia production expected for 2026.
- Blue Point One low-carbon ammonia JV (with JERA/Mitsui) on track: $3.7bn total cost unchanged, production from 2029; nitrogen-per-share growth projected +15% by 2030 via growth projects + buybacks.
- Capital return: 3.0m shares repurchased for $367m in Q3.
- War-duration signal: President Trump's late-Oct address signalled the war/Hormuz disruption runs "another two to three weeks at minimum" — CF surged ~5% premarket 2 Apr 2026 on similar news and is +67% YTD (per 21 Oct 2026 report); note urea has since fallen to $443/t from April's $935 emergency print as China's export quota expanded — the spot price has already corrected sharply from the panic peak even as CF's realized prices held up.
- Corn acreage forecast 95–96m acres for 2027 supports demand.

### 6. Risks
Pure commodity cyclicality: urea already fell from $935/t (Apr) to $443/t — the panic premium is mostly gone; CF's Q3 strength is ammonia/UAN mix, not urea. Ceasefire/peace would restore ~9m t of supply and collapse the premium. Chinese urea export policy is the swing factor (authorizations ~9m t vs <5m t last year; China expects +2–4m t more exports). Natural-gas price risk at home (Q1 gas cost jumped 24% to $4.57/MMBtu and compressed margins despite +19.4% revenue). Weather-dependent demand (wet/ warm Corn Belt delayed fall ammonia application). Yazoo City outage cost ~6pts of volume growth. Valuation: shares ~20% above Apr 2022 close on 2026 consensus earnings 8.5% *below* 2022 actual earnings — peak-earnings multiple widened 6.7x → 8.8x (DK Street Journal, Sep 2026). Long-dated capex: $3.7bn Blue Point One not producing until 2029.

### 7. Shortage score & verdict
**Shortage score: 7/10. Verdict:** The most structurally advantaged commodity shortage here — CF is the low-cost #1 producer while war and European gas costs remove rival supply — but the urea panic price has already halved from its April peak, so the explosive move may be partly behind it; the remaining edge is duration of the disruption, not its existence.

---

## 4. V — Visa Inc.

### 1. Shortage thesis
**No — there is no shortage.** Visa sells network access and transaction processing, a service with effectively infinite capacity; nothing is sold out, back-ordered, or lead-time constrained. The bull case is the opposite of shortage: secular volume growth (digital payments displacing cash) plus pricing power on a two-sided network. What *is* surging: cross-border volume (+14% YoY ex-intra-Europe in Q4 FY26; travel +13%, cross-border e-commerce +17%), value-added services (+31% in constant dollars to $4.0bn in Q4; $14bn for FY26, +30%), and data-processing revenue (+16% in Q4 vs +10% processed-transaction growth — a 6-pt spread; +17% vs +9% for the full year). There is no capacity constraint to quote — processed transactions were 74.2bn in the quarter (+10%) with no mention of limits. Score this section honestly: the "shortage" lens does not apply.

### 2. Backlog / order book
**Not applicable / not found.** Visa does not carry a backlog; revenue is a take-rate on flows. The closest forward indicator: ~25% of payments volume renews in FY27 (vs ~20% in FY26) — i.e., a large slug of client contracts is up for renegotiation, which is a risk (incentives) as much as an opportunity. No backlog figure exists.

### 3. Category position
**Yes — clear #1.** Visa processed 62.27% of combined Visa+Mastercard purchase volume in the 12 months to 30 Jun 2026 ($15.34tn vs Mastercard's $9.29tn; Axis Intelligence, Oct 2026). In the U.S., Visa's share of combined volume was 70.96% in the Apr–Jun 2026 quarter (70.28% a year earlier); U.S. debit 73.59%, U.S. credit 67.92%. Nilson Report (May 2026): Visa handled 31% of U.S. debit transactions and 30% of credit transactions vs Mastercard 12% debit / 14% credit — roughly a 2x lead on each. 4.7bn+ cards in circulation, 175m+ merchant locations, 200+ countries. Amex/Discover are distant. Globally by purchase transactions Visa ~38.7% vs UnionPay ~33.2% (Nilson H1 2024) — UnionPay is the only near-rival and is China-concentrated.

### 4. Irreplaceability / disintermediation risk
**Score: 8/10 — but the threat is the most discussed in markets, so score it with eyes open.** Moat: 175m+ merchant acceptance, issuer relationships, fraud/risk tooling, chargeback infrastructure, regulatory licences, and decades of consumer habit; digital wallets still run primarily on Visa/Mastercard rails. The concrete disintermediation threats, all live in 2026:
- **Stablecoins:** pitched as a way to bypass card rails entirely. Reality check so far favours Visa: stablecoin-card spending reached $3.9bn through Sep 2026 (10x YoY) but is **0.03% of Visa's quarterly volume** (Allium, Oct 2026); ~90% of crypto-card transactions already run *through Visa*; Visa's own stablecoin settlement passed a $25bn annualized run rate (up 10x in a year; ~$20bn per Sep 2026 reporting) and its Oct 2026 Mesh partnership makes crypto/stablecoin balances spendable at 175m+ merchants with the merchant receiving fiat. Visa is absorbing the threat into its own rails.
- **Agentic commerce / AI agents:** Citrini Research (Feb 2026) warned AI agents optimised for cost could route around 2–3% interchange to near-zero-cost stablecoin rails; Morgan Stanley estimates agentic buying could be $385bn of U.S. e-commerce by 2030. Visa's answer: AI-agent payment infrastructure and charging for trust (data processing +16% vs transactions +10%).
- **Regulation / politics:** Trump's proposed 10% cap on credit-card interest rates; interchange scrutiny. Visa/Mastercard/Amex fell 18–23% from peaks in early 2026 on these fears.
- Net: no customer can realistically "build Visa" — the acceptance network is the product — but merchants and agents can route *around* it at the margin, which is why the multiple has de-rated (24–27x forward vs higher historical averages).

### 5. Recent catalysts (last ~3 months)
- **Q4 FY2026 earnings, 27 Oct 2026:** net revenue $12.14bn (+13% YoY, +13% constant dollar), effectively in line with $12.09bn consensus (+0.4%); non-GAAP EPS $3.48 (+17%) vs $3.44 consensus — beat came from the tax line, operations landed on consensus. FY26: revenue $45.9bn (+15%, strongest ex-pandemic/acquisitions in 15+ years), non-GAAP EPS $13.27 (+16%). Payments volume +9% (U.S. +10%); processed transactions 74.2bn (+10%). Dividend raised 16% to $0.78/quarter (record date 10 Nov, payable 1 Dec).
- FY27 guide: low-double-digit revenue and opex growth (non-GAAP constant dollar, ex-acquisitions); GAAP EPS growth low-20s%. One recap downgraded to Hold (target $405 unchanged) on the guide step-down and incentive pressure.
- Stablecoin settlement ~$25bn annualised run rate (10x YoY); Mesh partnership (19 Oct 2026). Buybacks: $4.0bn in Q4 at avg $369.12 (vs $7.9bn at $320.66 in Q2) — the buyback itself is buying higher.
- Mastercard reported 29 Oct 2026 (event risk passed).

### 6. Risks
Client incentives are the key margin leak: +21% YoY to $5.1bn in Q4 (29.7% of gross revenue), growing faster than revenue, with ~25% of volume renewing in FY27 and management guiding incentive growth to step up from FY26's 16%. International transaction revenue grew only +8% vs +14% cross-border volume (currency-volatility drag) for a second straight quarter. Stablecoin/agentic disintermediation is a slow-burn structural risk, not a 2026 event — but it is exactly the kind of risk that caps the multiple. Regulatory overhang (rate-cap proposal, interchange). No shortage dynamic means no explosive re-rating catalyst — this is a compounder, not a squeeze. Consumer-spending slowdown would hit volumes directly.

### 7. Shortage score & verdict
**Shortage score: 2/10. Verdict:** A dominant, high-quality network compounder with zero shortage characteristics — the wrong lens for an explosive-return bet; the only "explosion" here would be a multiple re-rating if stablecoin fears prove overblown, and the Q4 print gave no reason to expect it imminently.

---

## Summary table

| Ticker | Shortage score | Irreplaceability | One-line verdict |
|---|---|---|---|
| ANET | 8/10 | 6/10 | Strongest AI shortage story in the batch, but Nvidia has taken the DC-Ethernet lead and the moat is software, not silicon. |
| VLO | 7/10 | 5/10 | Real distillate shortage, record margins — but the market is already fading a war-premium peak. |
| CF | 7/10 | 7/10 | Best cost-curve position in a war-driven nitrogen shortage; the urea panic price has already halved. |
| V | 2/10 | 8/10 | Dominant network, no shortage — a compounder, not an explosive bet. |

**Strongest shortage thesis overall: ANET** (demand demonstrably outrunning supply, +58.5% growth, guidance raised 4x), with CF the best risk-adjusted commodity version of the same idea. VLO's shortage is real but most clearly past its peak; V does not fit the lens.

**Caveats / not found:** No company in this batch discloses a dollar customer backlog — ANET's $11.4bn is supplier purchase commitments (not orders); CF's order book is described only qualitatively ("into Q1 2027"); VLO and V have no backlog concept. ANET's deferred-revenue sequential decline (first in coverage) and VLO's post-earnings selloff are the two freshest caution flags, both dated within the last week.
