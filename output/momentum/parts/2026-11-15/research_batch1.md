> Run by: Muse Spark 1.3 (session 5e50828d-4e50-4174-ae80-7c86f93bc8d8) — full panel

# Research Batch 1 — Stock-Pick-Momentum Panel, RUN_DATE 2026-11-15

Candidates: ANET, APH, MSFT, META. Research date: 2026-11-15 (all figures as reported in sources cited; "not found" where a figure could not be verified in web search on this date). Prices/context from the brief: ANET Q3 2026 revenue $3.66bn +58.5% y/y; APH price $78.23 at Nov 13 close; MSFT Q1 FY27 reported Oct 28, 2026; META Q3 2026 reported Oct 21, 2026.

---

## ANET — Arista Networks

### 1. Shortage thesis
Yes — demand is outrunning supply, and the constraint is on Arista's *inputs*, not just end demand. CEO Jayshree Ullal on the Q1 FY2026 call (May 2026, reported by SDxCentral Nov 2026): "Our demand is actually the best I've ever seen in my Arista tenure. The supply, however, is a slightly different and opposite tale. We are experiencing industry wide shortages across the board, be it wafers, silicon chips, CPUs, optics, and, of course, memory… Clearly, our demand is outstripping our supply this year." In Q2 she added Arista was having to "smile and take it just about at any price we can get, and the prices are horrendous" for memory chips. The driver is the AI datacenter buildout: AI fabrics are the growth engine (see §5), Etherlink customers >100 in 2026 vs 4–5 at the start of the cycle, and management forecasts AI deployments exceeding 10 GW of capacity across 10+ accelerator types by end-2027. The shortage is therefore a *supply-side* shortage (wafers/silicon/memory/optics) throttling a demand surge — Arista cannot ship fast enough, which is why inventory rose to $3.2bn (from $2.5bn in Q2) as an intentional build and purchase commitments rose to $11.4bn.

### 2. Backlog / order book
- Remaining performance obligations (RPO): **$8.6bn at Sep 30, 2026**, vs $6.1bn at Dec 31, 2025 (+41% in nine months); ~91% expected within two years (Form 10-Q filed Nov 4, 2026, via Quantisnow / The Traders Spread). Caveat: this is deferred revenue ($6,839.5m) + other performance obligations ($1.4bn, of which only $943.5m is binding product agreements and $497.1m unbilled multi-year support) — it is NOT a pure unfilled-orders book. Deferred revenue actually fell $26.4m sequentially in Q3 (first sequential decline in Aardvark Labs' coverage), with $1,715.0m of Q3 revenue recognised from the opening deferred balance.
- Purchase commitments (supply side): **$11.4bn**, up from $9.7bn in Q2 and $6.8bn at end-FY2025; $2.1bn due beyond 12 months vs $0.3bn in June — multi-year silicon/memory commitments.
- How far out booked: not found as a customer-order horizon; RPO is ~91% inside two years.

### 3. Category position
**No longer #1 in datacenter Ethernet by revenue.** IDC Quarterly Ethernet Switch Tracker, calendar Q1 2026 (SDxCentral, Nov 2026): Nvidia #1 with $2.1bn, **21.5%** share (+192.7% y/y), Arista #2 with **20.7%** (revenue $2.2bn, +37.3% y/y, 92% of it datacenter). Q2 2026 (IDC via NewMarketPitch, Oct 2026): Nvidia still #1 at ~20.4% (~$2.5bn, +181% y/y), Arista ~18.7%, Cisco ~18.2%; datacenter Ethernet segment $12.3bn, +64.5% y/y. Overall Ethernet (all segments) Cisco still leads (~29.3%). Arista remains the leading *independent/open-Ethernet* vendor and co-founded the Ultra Ethernet Consortium; Nvidia's lead is bundled with its GPU/AI-factory sales (Spectrum-X), not a like-for-like switch displacement — Arista's switch revenue still grew ~37%.

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 6/10.**
- Moat: EOS software + CloudVision, qualification at hyperscale (multi-year testing/acceptance — product deferrals in Q2 were explicitly due to customer-specific acceptance requirements), open-Ethernet standards leadership (UEC co-founder), and scale (100+ Etherlink customers). Switching a live AI fabric is operationally risky and slow.
- Threats (concrete, not hypothetical): (a) Arista is "primarily reliant" on **Broadcom** for switching silicon (Jericho/Tomahawk), with no written supply guarantee (10-K FY2025) — its core chip is someone else's; (b) its two largest customers are Microsoft (~26%) and Meta (~16%) of 2025 revenue, and both run white-box SONiC/FBOSS stacks and are actively pushing open/disaggregated networking — they can and do second-source; (c) Nvidia bundles Spectrum-X with GPUs (90% networking attach rate claimed at CES 2026; Nvidia networking revenue $14.8bn in FY26 Q1, +199% — though that line includes InfiniBand) and is now the #1 datacenter Ethernet vendor; (d) scale-up (NVLink-class intra-rack) has **zero** Arista revenue in 2026 and only trials in 2027 — the highest-value segment is Nvidia-proprietary for now, and Arista's ESUN/Etherlink SU-144 answer is not yet commercial at scale. Only a handful of firms can make merchant switch silicon at this level (Broadcom, Marvell, Nvidia), but Arista itself does not make it.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, Nov 3, 2026:** revenue $3.66bn, +58.5% y/y — highest growth since IPO; beat $3.3bn guide by ~10.8% and ~$3.33bn consensus by ~9.8%; non-GAAP EPS $1.20 vs $1.08 expected; non-GAAP operating margin 49.1%. Q4 guide $3.9–4.0bn.
- **2027 outlook (first look, Nov 3):** total revenue ~$18.5bn (+38–40% vs ~$13.3bn FY2026, itself raised for the 4th time this year), ~10–13% above Street ($16.4–16.75bn). AI fabrics to **double to ~$7.0bn** (from $3.5bn 2026 target); Cognitive Campus ~$2.0bn (+60% vs $1.25bn).
- **Product:** at OCP (Oct 2026) launched open Ethernet rack-scale architectures — liquid-cooled Etherlink SU-144 (144 accelerators/rack, one hop; up to 1,024 XPUs cross-rack), 7800 AI Spine, SRv6 multiplane "scale-across" for distributed fabrics up to 1M XPUs, with AMD, Arm, Broadcom, d-Matrix, Meta, Microsoft, Qualcomm as partners.
- Analyst reaction: Aardvark Labs downgraded to Hold from Outperform on the Q3 print (deferred-revenue sequential decline trigger), citing ~41x FY2026 / ~30x 2027 earnings at the guide — valuation, not fundamentals.

### 6. Risks
Customer concentration (top-2 = 42% of revenue; management expects 3–4 customers ≥10% by year-end); Broadcom silicon dependence + memory/silicon cost inflation compressing gross margin (non-GAAP gross margin already 1.2pp below last year); Nvidia Spectrum-X bundling and share loss in datacenter Ethernet; scale-up revenue absent until 2028+ (CPO after 2028); $11.4bn purchase commitments = inventory/obsolescence risk if hyperscaler deployment schedules slip; deferred-revenue sequential decline in Q3; valuation (~30x 2027 guide) prices in the doubling AI story.

### 7. Shortage score & verdict
**Shortage score: 7/10. Verdict:** Real demand surge with a genuine supply choke (memory/silicon) and a doubling AI-fabric guide — but Arista is the *constrained middleman*, not the scarce asset itself: it buys its silicon from Broadcom, its biggest customers run white-box stacks, and Nvidia now leads its category.

---

## APH — Amphenol

### 1. Shortage thesis
Yes — the strongest order-book evidence of the four. The driver is AI datacenter buildout: high-speed copper, fibre-optic and power interconnects inside AI racks. CEO Adam Norwitt, Q3 2026 call (Oct 28, 2026): "the vast majority of our sequential growth was related to AI," with AI at ~three-quarters of IT datacom sales; IT datacom was 48% of Q3 sales (up from 41% Q1, 43% Q2) and supplied ~three-quarters of the sequential sales increase. Orders ran ahead of shipments (book-to-bill 1.19), i.e. customers are ordering faster than Amphenol can deliver — the classic shortage signature. Power interconnect is called out as a meaningful high-growth leg as chip power rises and 800V+ formats spread. **Lead times: not found** — the "40+ week high-speed interconnect lead times" figure in the brief could not be verified in web search on this date; Semibuffer (Nov 2, 2026) explicitly states it has "no lead-time figure for these families this week." Do not cite 40+ weeks without a source. No verified price-increase quote found either; margin expansion (adjusted operating margin 29.7%) is attributed to volume/operating leverage.

### 2. Backlog / order book
- **Orders Q3 2026: $12.17bn, +99% y/y, +13% sequentially** — a record (company release, Oct 28, 2026). **Book-to-bill 1.19:1**, positive in all but one end market.
- Sales Q3 2026: **$10.23bn, +65% y/y (+37% organic)**; Communications Solutions $6.58bn (+99% y/y, +51% organic); IT datacom +100% y/y in USD, +77% organic, +30% sequentially.
- Backlog horizon: Amphenol does not disclose a total backlog $ figure or a booked-out horizon in the release — **not found**. The 1.19 book-to-bill implies the order book grew by ~$1.94bn in the quarter, but no duration is stated.
- Guidance: Q4 2026 sales $10.3–10.5bn (+~60% y/y), adj. EPS $0.81–0.83; FY2026 sales $36.9–37.1bn (~+60%), adj. EPS $2.82–2.84 (~+70%). IT datacom expected ~half of full-year sales (vs ~a third last year); full-year 2026 AI-related sales expected to more than double (per TipRanks summary of the call — "about three-quarters of IT Datacom revenue now ties to AI, with full-year 2026 sales expected to more than double").

### 3. Category position
**#1 in interconnect/connectors by scale, but the market is fragmented.** Amphenol is the world's largest connector maker by revenue; in AI datacom its named rivals are TE Connectivity (Digital Data Networks only $813m in its FQ3 2026, +34% y/y; total orders $6.1bn in FQ4 vs Amphenol's $12.17bn in a quarter) and Bel Fuse. No single published "AI interconnect market share %" was found — **not found**. Communications Solutions at $6.6bn/quarter dwarfs TE's datacom-adjacent lines. CommScope CCS acquisition (closed Q1 2026) added fibre/connectivity breadth; 2026 CommScope sales guidance raised to $5.1bn (from $4.6bn, then $4.1bn).

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 5/10.**
- Moat: breadth (high-speed copper + fibre + power in one supplier), qualification/design-in across hyperscaler rack architectures, manufacturing scale and the CommScope fibre portfolio; interconnect is mission-critical — a cluster cannot function without the links — and Amphenol is designed into the reference architectures. Customer switching costs are real at the platform level (re-qualification, signal-integrity validation).
- Threats: interconnect is fundamentally a *standards-based, multi-source* business — TE Connectivity, Molex/Koch, Foxconn, Luxshare and others make equivalent connectors; hyperscalers dual-source deliberately and set the specs (e.g. OCP / UEC standards), so Amphenol is a price-taker on standard parts and wins on execution/scale, not proprietary technology. No single process-tech lead, patent wall or certification lock-in comparable to a chipmaker. The main defence is breadth + scale + being qualified everywhere, which is strong but replicable by TE at smaller scale. Optical/co-packaged optics over time could shift value from copper connectors toward silicon photonics players.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, Oct 28, 2026:** record sales $10.23bn (+65%), record orders $12.17bn (+99%), record adj. EPS $0.80 (+74% y/y, beat $0.73 estimate by ~9.7%), revenue beat ~$9.49bn estimate by ~7.8%; stock +4.9% on the print. 8th consecutive EPS beat.
- **Capital returns:** dividend raised 20% to $0.15/share (payable Jan 13, 2027); new 3-year **$4bn buyback** effective Jan 1, 2027.
- **M&A:** CommScope CCS performing above plan (2026 sales $5.1bn expected, $0.18 adj. EPS accretion); Trexon (~$1bn, defence interconnect) and Rochester Sensors closed/closing; further small 2026 acquisitions guided (~$320m Empire, $270m AdvancedPCB, $90m Dexgreen, $70m Humanetics Sensors).
- **Guidance raised:** FY2026 sales $36.9–37.1bn and adj. EPS $2.82–2.84.
- Analyst: Zacks (Aug 26, 2026) flagged Communications growth and CommScope/Wilder as strengthening the AI position; no major upgrade/downgrade in the last ~3 months found in search.

### 6. Risks
Concentration is rising, not falling: IT datacom ~48% of sales and ~¾ of growth — a hyperscaler capex pause hits Amphenol harder than its diversified history suggests; non-datacom markets are soft (communications networks organic −28% y/y in Q3; industrial/automotive expected to moderate in Q4); ~28pp of the 65% sales growth is acquisitions (CommScope), so organic AI growth (+37%) is the cleaner read and the acquisition contribution fades; multi-sourcing caps pricing power; free-cash-flow margin fell to 15.8% from 19.6% as working capital/capacity absorbed cash; valuation at ~$78 (Nov 13 close) after a ~58% surge — the beat-and-raise cadence (25 straight quarters beating the top of guide, per Inve) is now the expectation.

### 7. Shortage score & verdict
**Shortage score: 8/10. Verdict:** The cleanest shortage print in the batch — record $12.17bn orders, 1.19 book-to-bill, AI ~¾ of a datacom business that is now half the company — but the moat is scale and qualification, not scarcity of the technology itself, so the explosive upside depends on the AI capex cycle lasting, not on an un-replicable asset.

---

## MSFT — Microsoft

### 1. Shortage thesis
Yes — for Azure compute specifically, and management says so directly. CFO Amy Hood, Q1 FY27 call (Oct 28, 2026): "Customer demand continues to exceed available supply" / "demand still exceeds supply." Azure revenue $33.165bn, +48% y/y — the first time Microsoft printed Azure in dollars — and still beat expectations *despite* "some third-party capacity deliveries we expected in Q1 were delayed," with some third-party GPU-as-a-service contracts slipping to Jan–Jun 2027 (H2 FY27). The constraint is physical: data-center capacity, power/grid connection delays (flagged in the 10-Q), and third-party GPU supply. Foundry revenue more than tripled and CPU efficiency gains were used to free capacity for Foundry — i.e. Microsoft is rationing scarce capacity toward its highest-value AI workload. This is a genuine structural shortage: demand for AI compute exceeds the world's ability to build powered datacenters and supply GPUs.

### 2. Backlog / order book
- **Commercial RPO: $677bn, +73% y/y** (Q1 FY27, quarter ended Sep 30, 2026; reported Oct 28, 2026). Flat vs Q4 FY26 ($678bn) — the sequential story is lumpy (commercial bookings −12% y/y, lapping a large Azure commitment last year; Q1 included one large Azure commitment).
- Horizon: ~30% (~$203bn) recognised in the next 12 months (+29% y/y); the portion beyond 12 months +98% y/y; weighted-average duration **2.3 years**.
- Caveat: Microsoft does not split RPO by customer — **no ex-OpenAI split was given** — so how much of the $677bn is OpenAI vs diversified enterprise is not disclosed. The backlog is contracted revenue, but delivery depends on Microsoft building the capacity (see §1).

### 3. Category position
**#2 in cloud infrastructure, #1 in enterprise software.** Synergy Research Group, Q3 2026 (CRN/ChannelWeb): AWS 26%, **Azure 19%**, Google Cloud 16% (Q2 2026: AWS 28%, Azure 20%, Google 15%). Azure's share slipped 1pp y/y while growing revenue +48% — Google gained 3pp. In the broader Microsoft 365 / productivity market Microsoft is dominant (>430m Microsoft 365 users, per BBC Nov 2026). Azure is the fastest-growing of the big three in absolute dollars (+$10.8bn y/y in Q1 FY27) and the enterprise default via M365/Entra/Windows integration.

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 8/10.**
- Moat: the enterprise stack is the lock-in — M365/Office, Entra ID, Windows Server, Teams, plus Azure's 200+ services, compliance certifications (most of any cloud, per trade coverage), and the OpenAI partnership (Foundry revenue more than tripled). Migrating a large enterprise off Azure+M365 is a multi-year re-platforming, not a purchasing decision. Capital intensity is extreme: capex $45.2bn in Q1 FY27 alone (vs ~$50bn guide; Q2 capex expected above $50bn) — only three firms on earth build at this scale.
- Threats: customers *can* multi-cloud and increasingly do (89% of enterprises use 2+ clouds); Google Cloud is gaining share fastest (16% in Q3 2026, +3pp y/y) on AI/TPU strength; OpenAI itself is diversifying compute (TPU/AMD deals) and is both Microsoft's largest customer and a concentration risk inside the undisclosed RPO split; hyperscaler customers do not "in-source" Azure — the risk is share loss to AWS/GCP and price pressure on AI inference, not disintermediation. The Nov 12–13 M365 outage (see §5) is a reminder that centralisation is itself a risk customers weigh.

### 5. Recent catalysts (last ~3 months)
- **Q1 FY27 earnings, Oct 28, 2026:** revenue $92.279bn (+19%), operating income $45.9bn (+21%, 50% margin), Microsoft Cloud $63.9bn (+30%), Azure $33.165bn (+48%, first dollar print), RPO $677bn (+73%). Beat own guidance on revenue, operating income and EPS. Q2 guide: revenue $96.0–97.1bn; Azure +49–50% constant currency.
- **Negative catalyst — global M365 outage, Nov 12–13, 2026:** Exchange Online / Outlook / Teams / Copilot degraded worldwide for 20–25+ hours (incidents EX1550543 / MO1550821), Downdetector Outlook reports peaking at ~130,000, 70+ countries; Microsoft attributed it to a fault introduced during an earlier network capacity upgrade that surfaced after a network change (not cyber, not AI); fixes initially "not taking as expected"; full post-incident report pending as of Nov 13. Azure customer workloads were **not** confirmed affected (Azure status page showed no events).
- **Other:** ~60,000 employees (~a quarter of the workforce, VP-level and below) offered voluntary buyouts Oct 26, 2026, decisions due early December, departures Dec 31; $10.2bn returned via dividends/buybacks in Q1.

### 6. Risks
The $677bn RPO is only as good as capacity delivery — power, grid connections and third-party GPU delays already slipped contracts into H2 FY27; capex is running >$45bn/quarter with cloud gross margin falling to 66% on Azure mix shift; OpenAI concentration inside RPO is undisclosed; Google Cloud is taking share (Q3: GCP +3pp, Azure −1pp); the M365 outage damaged the reliability narrative for the exact enterprise customers Azure needs; valuation prices in sustained ~48–50% Azure growth that depends on capacity Microsoft does not yet have.

### 7. Shortage score & verdict
**Shortage score: 8/10. Verdict:** The shortage is real and management-admitted — Azure demand exceeds supply with a $677bn contracted backlog — but Microsoft is the *buyer* of the scarce GPUs/power as much as the seller of scarce compute, and the explosive-return case is capped by its size: +48% on $33bn is extraordinary, yet it is still the #2 cloud growing into a capacity wall it must spend >$50bn a quarter to climb.

---

## META — Meta Platforms

### 1. Shortage thesis
**Inverted: Meta is on the buying side of the shortage, not the selling side.** Meta's core product (advertising) is not in structural shortage — ad supply is effectively infinite and auction-priced. What is scarce is *AI compute for Meta itself*: on the Q3 2025 call management said compute needs "continued to expand meaningfully," and by Q3 2026 the constraint is explicit — Zuckerberg said the biggest constraint on Muse's rollout so far is **compute intensity**, and Muse is not yet global for that reason. Meta is therefore a *victim* of the AI-capacity shortage: it must spend $135–145bn of capex in 2026 (see §2) and rent/buy chips from everyone (Nvidia, AMD, and reportedly Google TPUs) to secure supply. There is no product Meta sells that customers cannot get enough of; the shortage thesis for META as a *beneficiary* does not hold — the bull case is instead that AI improves ad targeting/engagement enough to pay for the compute.

### 2. Backlog / order book
- **Not applicable / not found.** Meta is an advertising business, not an order-book business: it reports no backlog, RPO, bookings or book-to-bill. Revenue is recognised as ads are delivered.
- Closest analogues: Q3 2026 revenue **$64.601bn, +26% y/y** (ads $63.061bn, +26%); Q4 2026 revenue guide **$73–76bn**; Family daily active people 3.64bn. Capex (the demand-side figure): **$34.91bn in Q3 2026** alone (incl. finance-lease principal), **FY2026 guide $135–145bn** (floor raised from $130bn); no 2027 capex guide given — CFO Susan Li said the company is "still developing our budget and capacity plans" but will "continue investing aggressively"; Street estimates put 2027 capex near $200bn (per CompoundingCap / Substack summary of the call — treat as analyst estimate, not guidance). Free cash flow was **−$2.12bn** in Q3 (operating cash flow $32.79bn), the first negative FCF quarter in years; 9M FCF $11.0bn, down 63% y/y.

### 3. Category position
**#1 in social advertising by a wide margin, #2 in digital advertising overall behind Google.** Family of Apps ad revenue $63.1bn in a single quarter (~98% of total revenue); 3.64bn daily active people across Facebook, Instagram, WhatsApp, Threads. No verified current market-share % found in search — **not found** (commonly cited ~20%+ of global digital ad spend ex-China, but no citable 2026 figure was retrieved; do not use). In AI glasses Meta "continue[s] to lead the industry" (Q3 2025 release); Reality Labs revenue $443m in Q3 2026 (−6% y/y). In frontier AI models Meta is a challenger, not #1 (Muse Wonder is its first frontier model, shipped Q3 2026).

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 7/10 (for the ads business); 3/10 for the AI bet.**
- Moat (ads): network effects at 3.64bn daily users, the deepest consumer-behaviour dataset for ad targeting, and AI-driven ranking that is measurably lifting outcomes (Instagram time spent +4% from Reels relevance; advertisers using the Meta AI business assistant saw ~5% more conversions at the same cost and raised spend 9%; Muse-family models cut content-understanding cost >80%). Advertisers cannot replicate that audience or targeting elsewhere at scale — Google is the only comparable alternative, and the two are complements, not substitutes, for most budgets.
- Threats: the AI layer is *not* moated — Meta buys its accelerators from Nvidia/AMD and is reportedly negotiating to rent/buy **Google TPUs** (The Information, Nov 24, 2025; reported as talks, not a signed deal — Reuters could not verify; later reports describe a multi-year, multi-billion-dollar TPU *lease* as signed, but the sourcing is inconsistent and no contract value/chip count was disclosed, so treat as **unconfirmed**). Meta's own MTIA chips are not the story. Muse's unit economics are unproven: 10m+ sign-ups in ~6 weeks (25% daily use) but **zero disclosed Muse revenue**, retention ~73% day-1 / 30% day-7 / 23% day-14 (Sensor Tower via Cardano Capital), and management says it must cut Muse costs >10x in a year to reach profitability at scale. If AI inference commoditises, Meta's $135bn+ capex buys no durable edge.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, Oct 21, 2026:** revenue $64.6bn (+26%, beat ~$63.3bn expected); GAAP EPS $3.83 including a **$9.89bn charge** for the 52-state attorneys-general agreement (payments up to ~$18.59bn); ex-charge operating income $22.88bn, EPS ~$7.40, margin 35% (vs 20% GAAP). Q4 revenue guide $73–76bn. Stock fell ~20–25% from October highs after the print on capex fears.
- **Muse launch:** Meta's personal AI agent + Muse Wonder frontier model shipped; >10m people in the US/Canada set up Muse in ~6 weeks, #1 in the App Store almost daily; engagement per person in Meta AI more than doubled since April; management expects new AI businesses to begin contributing incremental revenue in 2027.
- **Capital structure:** new non-voting Class C stock approved (effective Jan 19, 2027; one Class C share as a one-time dividend per Class A/B share) — framed as a capital-raising tool for the buildout, with no specific financing plan attached. Long-term debt rose to $80.9bn (from $58.7bn at year-end) after $24.9bn of new debt in 2026.
- **Reality Labs:** 2026 losses guided $18–19bn, narrowing to ~$15bn in 2027.
- **Google TPU talks** (above) — unconfirmed, but a live November story; also a reported ~$60bn AMD chip deal days earlier (per AInvest summary — not independently verified here).

### 6. Risks
Capex is the risk: $135–145bn in 2026, possibly ~$200bn in 2027, with FCF already negative and cash ($82.45bn) now below debt ($83.7bn); the return on that spend is unproven (Muse: no revenue, weak retention, needs a >10x cost cut); ads are ~98% of revenue, so any ad slowdown meets a fixed-cost wall (total 2026 expenses guided $175–179bn, incl. the legal charge); $18.6bn legal overhang not fully booked; Reality Labs still burns $15–19bn/year; and Meta is structurally *dependent* on Nvidia/Google/AMD for the accelerators its strategy requires — it is paying the shortage's price, not collecting it.

### 7. Shortage score & verdict
**Shortage score: 3/10. Verdict:** Meta faces the AI shortage as a buyer, not a seller — its ads engine is firing (+26%) but the $135bn+ capex buildout to secure scarce compute has already flipped FCF negative, and the payoff (Muse monetisation) is unproven with zero revenue disclosed; this is a capex-cycle bet, not a shortage beneficiary.

---

## Cross-ticker summary

| Ticker | Shortage score | Irreplaceability | Backlog / orders | One-line verdict |
|---|---|---|---|---|
| ANET | 7/10 | 6/10 | RPO $8.6bn (+41% in 9M); purchase commitments $11.4bn | Doubling AI-fabric guide into a real supply choke — but it buys its silicon and its top customers run white-box. |
| APH | 8/10 | 5/10 | Orders $12.17bn (+99%), book-to-bill 1.19 | Cleanest shortage print in the batch; moat is scale/qualification, not un-replicable tech. |
| MSFT | 8/10 | 8/10 | Commercial RPO $677bn (+73%), 2.3-yr duration | Demand exceeds supply by management's own words, with the biggest backlog — but it must spend >$50bn/qtr to deliver it. |
| META | 3/10 | 7/10 ads / 3/10 AI | n/a (ads business; capex $135–145bn FY26) | Pays the shortage's price rather than collecting it; FCF already negative on the compute buildout. |

**Figures not found (do not use without a source):** APH "40+ week" high-speed interconnect lead times and any APH price-increase quote; a total $ backlog figure or booked-out horizon for APH; a current % market share for APH in AI interconnect; Meta's current % share of digital advertising; any signed/confirmed Meta–Google TPU contract value or chip count (talks reported Nov 24, 2025; later "signed lease" reports are inconsistently sourced); ANET customer-order horizon beyond the ~91%-in-two-years RPO split; an MSFT ex-OpenAI RPO split.

**Sources (all accessed 2026-11-15):** Arista Q3 2026 press release Nov 3, 2026 (investors.arista.com); Arista Form 10-Q filed Nov 4, 2026 (via Quantisnow, The Traders Spread); Nasdaq/ Motley Fool ANET Q3 call transcript Nov 3, 2026; SDxCentral IDC datacenter Ethernet Q1 2026 + Nvidia/Gartner; SDxCentral Arista chip-shortage warning (Q1 FY2026 call); Amphenol Q3 2026 release/call Oct 28, 2026 (Fool transcript, FourWeekMBA, TickerRoast, Quartr); Semibuffer Nov 2, 2026 (lead-time caveat); Microsoft Q1 FY27 release/call Oct 28, 2026 (Sotkn, Valuaize, TradingKey/Dolphin Research); Synergy Research Q2/Q3 2026 cloud share (CRN/ChannelWeb, Dipsonar); Microsoft M365 outage Nov 12–13, 2026 (BBC via BharatBeat, Medium/Control Plane, Microsoft 365 Status); Meta Q3 2026 release/call Oct 21, 2026 (Fool transcript, TradingView, Cardano Capital, HelioQuant); The Information via Reuters/Edge Nov 24–25, 2025 on Meta–Google TPU talks.
