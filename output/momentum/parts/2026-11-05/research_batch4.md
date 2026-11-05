> Run by: Muse Spark 1.3 (unknown) — full panel

# Momentum research — Batch 4: CSCO, ROK, AME
Run date: 2026-11-05. Prices (screen, per brief — see verification note below): CSCO $102.97, ROK $443.88, AME $248.58.
Price verification (Finnhub snippets via search, and MarketBeat): CSCO's Nov 4 close was $103.61 (previous close $102.97 — so the $102.97 screen price is the Nov 3 close, stale by one session). ROK's Nov 4 close was $443.88, matching the screen price. AME is the stale one that matters: it closed Nov 4 at $237.30 (MarketBeat), −4.54% from the $248.58 Nov 3 close — i.e. the screen price is already ~4.5% above where the stock actually traded after its Nov 3 earnings. Finnhub pre-market Nov 5 showed $237.09. Do not use $248.58 as a live price.

Timing note: AME reported Q3 2026 on Nov 3, 2026 (covered below). ROK reports Q4 FY2026 before the open on Thu Nov 5, 2026 — i.e. TODAY, after this dossier was written; its latest reported quarter is Q3 FY2026 (Aug 4, 2026). CSCO's latest reported quarter is Q4 FY2026 (Aug 12, 2026); Q1 FY2027 is due mid-November (Nov 12 per the Bank of America note cited below; one data provider lists Nov 11 — treat the exact day as unconfirmed).

---

## CSCO — Cisco Systems (screen $102.97; Nov 4 close $103.61)

### 1. Shortage thesis
Real demand surge, not a physical shortage of Cisco's own product. The driver is the AI datacenter buildout: hyperscalers need far more switching/routing/optics to connect GPU clusters, and Cisco's AI infrastructure orders from webscale customers exploded. "We took $4B in orders in Q4, bringing the total for FY26 to $9.3B, approximately 4.5 times our FY25 total" (Cisco Q4 FY26 prepared remarks, Aug 12, 2026). FY25 total was just over $2B (Q4 FY25 call, Aug 13, 2025). The constraint sits upstream, on Cisco's side: memory (HBM), custom ASICs and optical components are allocation-constrained, which is why Cisco pre-bought aggressively (see appendix). Cisco itself calls this a "networking supercycle" and says it is "only at the beginning of this super cycle" (Q4 FY26 call coverage, Aug 2026). IDC: the worldwide Ethernet switch market grew 31.5% in 2025 to $55.1B, with the datacenter portion up 63% YoY in Q4 2025, "driven by the build-out of datacenter network infrastructure to support AI workloads" (IDC, Mar 18, 2026). No quote found of Cisco lead times extending or Cisco raising prices on AI gear — the evidence is order-volume, not price rationing.

### 2. Backlog / order book
No clean disclosed AI-only backlog figure — be careful here. Cisco disclosed: FY26 hyperscaler AI orders $9.3B vs ~$4B recognised as AI revenue in FY26, with $7.5B expected in FY27 (Q4 FY26 release, Aug 12, 2026). Bank of America (Nov 3, 2026 note, via The Inference) puts booked-but-unshipped AI orders at ~$6B, covering most of the $7.5B FY27 target. But an independent check (btw.media) warns $9.3B − $4B = $5.3B is *not* a disclosed backlog: "the order and revenue flows lack a common opening balance, cohort-conversion schedule and AI-only RPO reconciliation" and "Cisco has not published that table." Company-wide remaining performance obligations (RPO) were $46.73B at Jul 25, 2026, product RPO $23.44B (+9% YoY), 49% due within 12 months (SEC-API analysis of FY26 10-K). Total product orders +35% YoY in Q4 FY26 (+25% ex-hyperscalers, double-digit in every geography and customer market); networking product orders +40% YoY, an eighth straight quarter of double-digit growth. Book-to-bill in AI networking is well above 1 (orders $9.3B vs revenue ~$4B for the year), but how far out the book extends is not disclosed.

### 3. Category position
Yes — #1 overall in Ethernet switching, but *not* #1 in the datacenter segment that matters for AI. IDC Q4 2025: Cisco 27.6% of the total Ethernet switch market vs Arista #2 at 12.6% and Huawei 10.6%; Cisco router share 30.6%. In the datacenter segment, Arista leads (~19–21% share) and Nvidia has overtaken Cisco too — Nvidia booked $2.1B of datacenter Ethernet revenue in the Mar 2026 quarter (21.5% share) vs Arista 20.7%, per Dell'Oro-cited coverage; Fierce Network notes Arista "took over from Cisco a number of quarters ago" as the largest datacenter switch vendor. Cisco is #3 in datacenter Ethernet. Its strength is breadth: campus/enterprise (63.9% of its switch revenue is non-datacenter) plus routing, security, optics (Acacia) and software.

### 4. Irreplaceability / disintermediation risk
Moderate — the moat is real but the in-sourcing threat is concrete and already happening. Moat: Silicon One custom silicon (P200 51.2T systems now in production at Microsoft and Alibaba Cloud, per Cisco OCP release Oct 12, 2026), Acacia coherent optics, full-stack (switching + routing + security + observability + Splunk), and qualification at hyperscale. Threats: (a) hyperscalers design their own gear — Alibaba deployed its *in-house* Quantum Cat router built on Cisco's P200 silicon, running open-source SONiC; Microsoft likewise runs P200 systems, i.e. they buy Cisco's chip, not necessarily Cisco's box; (b) Nvidia bundles networking with GPUs (Spectrum-X / InfiniBand; Nvidia datacenter networking revenue was a record $14.8B in the quarter ended Apr 26, 2026, +199% YoY) and prefers to sell the full stack; (c) Broadcom's merchant Tomahawk 6 (102.4T) lets hyperscalers/white-box builders assemble open fabrics without Cisco or Arista, and Celestica builds much of what hyperscalers design themselves; (d) white-box/SONiC disaggregation caps pricing power — Arista's CEO dismissed white box as "a tactical solution" for simple use cases, but the structural direction is toward open, merchant-silicon fabrics. One analysis estimates only ~60% of Cisco's $9.3B AI orders is Silicon One systems, ~40% Acacia optics, putting switching content nearer $5.6B. **Irreplaceability: 5/10.**

### 5. Recent catalysts (last ~3 months)
- **Aug 12, 2026 — Q4 FY26 beat:** revenue $17.3B (+18% YoY, vs ~$16.8B consensus), non-GAAP EPS $1.22 (+23%, vs $1.17 est.), FY26 revenue $63.3B (+12%). Stock fell ~9–10% post-print to ~$112 on margin compression (see Risks).
- **FY27 guidance raise:** revenue $72.2–73.4B (+14–16%), non-GAAP EPS $5.05–5.11, $7.5B hyperscaler AI revenue; Q1 FY27 revenue guided $18.0–18.2B.
- **Oct 12, 2026 — OCP Global Summit:** 51.2T Silicon One P200 systems in production at hyperscalers (Microsoft, Alibaba Cloud named); G300 102.4T systems shipping; new G302 51.2T top-of-rack chip shipping before end-2026; joint Cisco–NVIDIA USFP open optics standard (400G-per-lane, up to 12.8T per module) with TE Connectivity and Amphenol.
- **Nov 3, 2026 — Bank of America** maintained Buy, $150 target (Tal Liani), citing the ~$6B unshipped AI backlog; Evercore ISI also $150. Morgan Stanley Overweight $135; JPMorgan Overweight $150 (Aug 2026). Consensus target ~$138–141 (TipRanks, Aug 2026).
- Dividend $0.42/share quarterly (raised 2% in Feb 2026; paid Oct 21, 2026).

### 6. Risks
- **Margin compression is the market's verdict:** non-GAAP gross margin fell 68.4% → 66.3% in Q4 FY26; product gross margin −270 bps to 64.8% on hardware mix and rising memory costs; Q1 FY27 gross margin guided 65–66%, and BofA expects ~64.5% for FY27. AI hardware is lower-margin than Cisco's software-rich mix; services revenue was flat in FY26.
- **Valuation no longer cheap after the run:** +~61% in 2026 before the Aug print (52-week range $70.54–$130.37 per Finnhub); at the $102.97 screen price vs FY27 non-GAAP EPS guidance midpoint $5.08, ~20x forward earnings — reasonable, but the stock already fell ~21% from its $130 high by Nov 4, and the Aug earnings beat still sold off 9–10%. The explosive-return case needs order conversion, not just orders.
- **Hyperscaler concentration and capex cyclicality:** AI orders come from a handful of webscalers; if hyperscaler capex slows, order flow flattens before earnings do. Two webscale customers each placed >$1B of total orders in FY25 — concentration is high.
- **Disintermediation (see §4):** Nvidia Spectrum-X/InfiniBand, Broadcom merchant silicon, white-box/SONiC, and customers buying chips (P200) instead of systems.
- **Inventory / working-capital overhang:** see appendix — $17.17B of purchase commitments (+126% YoY) is a bet that the $7.5B FY27 AI revenue materialises.

### 7. Shortage score and verdict
**Shortage score: 7/10. Verdict: The AI networking order surge is genuine and the largest in Cisco's history ($9.3B vs $2B), but it is a demand surge Cisco must convert at deteriorating margins against Nvidia/Arista/white-box competition — a strong momentum name, not a structural-shortage monopoly.**

---

## ROK — Rockwell Automation (screen $443.88; Nov 4 close $443.88)

### 1. Shortage thesis
Weak — there is no structural shortage of Rockwell's products. The driver is a *cyclical recovery* in factory automation plus a secular overlay (reshoring, labour shortages, AI on the factory floor), not supply that can't meet demand. Q4 FY25 call (Nov 6, 2025): "CapEx activity in longer cycle businesses remained muted, with customers holding off on larger investments" and "project delays… as customers wait for more clarity and stability around the impact of trade and policy." By Q3 FY26 (Aug 4, 2026) demand had broadened — "led by semiconductor, data center, e-commerce and warehouse automation," with "early renewed project activity in automotive and life sciences" — but management still said customers "continued to delay some large projects amid tariff and geopolitical uncertainty." No evidence found of sold-out capacity, extending lead times, or price increases driven by scarcity; FY25 growth was +3% pricing offsetting −2% volume, i.e. pricing power, not shortage pricing. The genuine demand pocket is narrow: e-commerce/warehouse automation sales +30% YoY in Q3 FY26 and +70%+ in Q4 FY25; discrete +20% in Q4 FY25; Software & Control organic sales +30% in Q4 FY25 and +18% in Q3 FY26 (Logix strength).

### 2. Backlog / order book
Contracting, not growing. Total order backlog $2.878B at Sep 30, 2025, down from $3.091B a year earlier (−7% YoY), "primarily in the core Intelligent Devices and Lifecycle Services segments" (FY25 10-K; Lifecycle Services $1.520B of it, −11%; Intelligent Devices −4%). At ~$8.3B annual sales, that backlog is only ~4 months of revenue. Q3 FY26 backlog figure: **not found** — the Aug 4, 2026 press release and prepared remarks do not disclose a total backlog number; Lifecycle Services book-to-bill was 0.97 in Q3 FY26 and ~0.9 in Q4 FY25, with overall book-to-bill "around one." No backlog growth to cite; the forward book is shrinking while sales recover, i.e. the recovery is being shipped from orders, not booked ahead.

### 3. Category position
#1 in its *defined* niche, not #1 in industrial automation overall. Rockwell calls itself "the world's largest company dedicated to industrial automation and digital transformation" (company releases) — the qualifier matters. Globally, Siemens is the world's largest industrial automation company (IoT Analytics, 2025; Siemens ~14.2% share per Verified Market Research vs Rockwell ~5.65% of the broader automation-components market per GlobeNewswire, May 2025, where Rockwell was the largest competitor in that particular components cut, ahead of Siemens 5.31%). In PLCs, ABI Research ranks Siemens #1 and Rockwell #2 (market leaders, ahead of Bosch Rexroth and ABB). Rockwell is dominant in North America and in discrete automation / Logix PLCs; Siemens leads in Europe and process. Addressed market ~$120B (FY25 10-K) vs Rockwell FY25 sales $8.34B — a small share of a fragmented market.

### 4. Irreplaceability / disintermediation risk
Moderate-high at the plant level, low at the technology level. Moat: the Logix / FactoryTalk installed base — ripping out a plant's control system is expensive, risky and re-qualification-heavy; Rockwell claims to be "the only automation provider capable of supporting discrete, process, batch, safety, security, motion, robotics, and power control within a single hardware and software environment"; ~65% of sales go through independent distributors, embedding it in machine-builder designs. Customers cannot realistically in-source a PLC/DCS stack themselves — no manufacturer builds its own controllers. But substitutes are plentiful: Siemens, ABB, Schneider Electric, Emerson, Mitsubishi, Honeywell and Dassault all compete (10-K named competitors), and software is the contested layer — Rockwell's answer is FactoryTalk Conductor (AI orchestration, launched Oct 21, 2026) plus NVIDIA Nemotron support (Oct 22, 2026), which is an *adoption* of Nvidia's models, not a proprietary moat. No single customer concentration was disclosed as a risk in the material reviewed. **Irreplaceability: 6/10** (sticky installed base, but a crowded, interoperable market with a larger #1).

### 5. Recent catalysts (last ~3 months)
- **Aug 4, 2026 — Q3 FY26 beat:** sales $2.313B (+8% reported, +10% organic; vs $2.24B consensus), adjusted EPS $3.49 (+22%, vs $3.38–3.39 consensus), GAAP EPS $3.65 (+40%). Free cash flow $654M vs $489M a year earlier. FY26 guidance raised: sales growth 7.5–9.5% (reported and organic), adjusted EPS $13.00–13.30 (midpoint +$0.35), GAAP EPS $12.72–13.02.
- **Oct 21–22, 2026 — FactoryTalk Conductor launch + NVIDIA Nemotron support:** AI-native orchestration platform for industrial automation; open-model, on-premises deployment pitch. Product news, no orders figure attached.
- **Jun 9, 2026 — $1.0B share repurchase authorisation** (up to ~2% of shares).
- **Oct 1, 2026:** company report that 90% of life sciences manufacturers view digital transformation as business-critical (marketing, not orders).
- **TODAY, Nov 5, 2026 (before open) — Q4 FY26 results + first FY27 guidance:** Zacks consensus EPS $3.55 (+6.3% YoY) on revenue $2.39B (+3.1%); MarketBeat consensus $3.69 on $2.41B (note: MarketBeat's "prior-year revenue $4.63B" is erroneous — actual Q4 FY25 revenue was $2.035B — ignore it). Zacks Earnings ESP +6.59%, Rank #3 (Hold); Deutsche Bank raised its target $469 → $500 on Sep 30, 2026 (Hold). Average analyst target ~$468 (MarketBeat). This dossier is written pre-print; the print is the immediate catalyst/risk.
- Sensia JV dissolution completed Apr 1, 2026 (−$250M annualised revenue, +~50 bps margin).

### 6. Risks
- **No shortage, no backlog growth:** the momentum case rests on a cyclical turn that the backlog does not yet confirm (−7% YoY, book-to-bill ~1). FY25 organic sales grew just 1% (volume −2%).
- **Cyclicality and capex delays:** demand follows industrial production and customer capex; tariffs/policy uncertainty are still delaying large projects (Q3 FY26 call). Food & beverage and parts of process had not yet seen a capex pickup as of Aug 2026.
- **Valuation:** at $443.88 vs FY26 adjusted EPS guidance midpoint $13.15, ~34x earnings (Finnhub trailing P/E 41.1x) for a business that grew 1% organically in FY25 and is guided to 7.5–9.5% in FY26 — the multiple already prices a strong recovery. 52-week range $347.53–$497.36.
- **Memory/input-cost pressure:** management flagged memory-related electronic-component inflation hitting Software & Control hardest in Q4 FY26; pricing actions are the offset.
- **Legacy drags:** $224M pre-tax Sensia impairment in FY25; asbestos/environmental charges spiked to $154M in FY25 (from $21M in FY24); BEPS Pillar Two adds ~3pp to the effective tax rate from FY26.

### 7. Shortage score and verdict
**Shortage score: 3/10. Verdict: A cyclical automation recovery with genuinely strong software/Logix momentum and a fresh AI product story, but no shortage and a shrinking backlog — the explosive-return case needs the Nov 5 print and FY27 guide to confirm the turn, at a ~34x multiple that already assumes it.**

---

## AME — AMETEK (screen $248.58; Nov 4 close $237.30 — see price note at top)

### 1. Shortage thesis
Broad-based demand surge across many niches rather than a single-product structural shortage. The drivers named by management on the Q3 2026 call (Nov 3, 2026): aerospace & defence, semiconductor, automation, power and process instrumentation — plus data-center power (AMETEK's UPS systems adapted for data centers; a Q3 2025 call cited a >$25M backlog and ~$30M pipeline for those, a small absolute number). Evidence is order *volume*, not scarcity: "September was a record month for orders" (Q3 2026 call); orders +35% YoY. No quote found of capacity sold out, lead times extending, or shortage-driven price increases. The "shortage" here is really synchronised strength across AMETEK's ~40 autonomous niche businesses (precision instruments, sensors, power systems, aerospace components, medical, specialty metals) — diversified, not concentrated in one bottleneck product.

### 2. Backlog / order book
The strongest backlog in this batch, and reported *two days ago*. Q3 2026 (quarter ended Sep 30, 2026; reported Nov 3, 2026): orders $2.65B, +35% YoY (organic orders +17%); backlog a record **$4.54B, +27% from the beginning of 2026**. Management's rule of thumb: "~80% of our backlog is shippable in the next 12 months… pretty ratable going into next year" (CEO Dave Zapico, Q3 2026 call) — so ~$3.6B of the backlog converts within a year, against quarterly sales of $2.22B (~6 months of sales in backlog). Prior context: Q2 2026 orders $2.3B (+28% YoY), backlog $4.11B; Q3 2025 backlog was $3.54B. The trajectory is accelerating, not just elevated.

### 3. Category position
Not a single #1 — a portfolio of #1s in niches. AMETEK describes itself (and is described by PitchBook/company materials) as a leader in differentiated technology with "leading positions in niche markets" across two groups: Electronic Instruments (EIG, ~66.5% of FY25 revenue, 29.4% segment margin) and Electromechanical (EMG). FY25: EIG $4.92B sales, EMG $2.48B. No single market-share figure vs a #2 was found — the company competes niche-by-niche (process/analytical instrumentation $3.46B; aerospace & power $2.19B in FY25) against different rivals in each; its claim is breadth + mission-critical specification, not a category crown. Treat any "#1 player" framing for AME as not established.

### 4. Irreplaceability / disintermediation risk
Moderate — the moat is qualification and mission-criticality spread across dozens of niches, not one un-replicable technology. Customers (aerospace, defence, semiconductor fabs, power, medical) buy instruments/sensors/power systems that are specified into long-cycle programs, qualified and hard to swap; aftermarket/consumables/service revenue recurs after the initial sale (notably for the acquired Indicor businesses). No hyperscaler-style customer can in-source precision measurement instrumentation — there is no credible "build it yourself" threat from AMETEK's customers, and no substitute technology routes around a sensor or a power system. The offset: none of the niches is individually a monopoly, the portfolio is acquisitive (integration risk), and demand is tied to its customers' capex cycles. **Irreplaceability: 6/10** (high switching costs niche-by-niche, diluted by diversification; no single 10/10 moat).

### 5. Recent catalysts (last ~3 months)
- **Nov 3, 2026 — Q3 2026 record quarter, guidance raised:** sales a record $2.22B (+17% YoY; organic +10%, acquisitions +7pts), adjusted EPS a record $2.21 (+17%, vs $2.11 consensus and $2.08–2.10 guidance), operating income a record $595M (+20%), margin 26.8% (+60 bps), EBITDA $704M (31.7% margin), free cash flow a record $527M (+26%). FY26 adjusted EPS guidance raised to **$8.53–8.57** (from $8.20–8.30), ~+15% YoY; Q4 guided sales +low-20s%, adjusted EPS $2.26–2.30 (+12–14%). Zacks Rank #1 (Strong Buy) after the print; consensus target ~$278 (MarketBeat).
- **Aug 26, 2026 — Indicor Instrumentation closed:** $5.0B all-cash, AMETEK's largest deal; mission-critical instrumentation, ~$1.1B annual sales; contributed >$100M of Q3 revenue and ~$0.08 of expected 2026 EPS accretion; management targets 10–12% synergies over three years and says there will be "no pause in M&A" with $2.7B of cash + available credit.
- **$29.8M U.S. Air Force contract** for VDATS kits (AMETEK Programmable Power) — cited in Q3 coverage.
- **Paradox — the stock fell on the beat:** AME closed Nov 4 at $237.30, −4.54% on the day (MarketBeat), after closing Nov 3 at $248.58. No single explanation was found in the coverage reviewed; candidates in the print itself are the leverage jump (see Risks) and profit-taking after a run to the $261.16 all-time high (Aug 13, 2026). Do not assert a cause.
- Earlier in the window: First Aviation Services acquired May 21, 2026; FARO Technologies acquisition closed earlier (debt-funded; see Q3 2025 call).

### 6. Risks
- **Leverage jumped with Indicor:** total debt $6.67B at Sep 30, 2026 vs $2.28B at end-2025; net debt/EBITDA 2.1x (Zacks) / 2.3x (CMC); interest expense ~$40M in Q3 vs $23M a year earlier (+$17M YoY). The deal must earn its keep; integration is the execution risk.
- **Valuation and the post-earnings sell-off:** at the Nov 4 close of $237.30 vs FY26 EPS guidance midpoint $8.55, ~27.8x (vs ~29x at the stale $248.58 screen price); Finnhub trailing P/E 35.4x; PEG ~2.3. The market sold a record beat by 4.5% — either leverage/valuation indigestion or a signal the guide was not enough.
- **Acquisition-dependent growth:** 7pts of Q3's 17% sales growth was acquisitions; organic growth (+10%) is strong but the model leans on M&A, and GAAP EPS ($1.77 in Q2) runs well below adjusted EPS due to acquisition amortisation/charges.
- **Cyclical end markets:** aerospace/defence/semiconductor/power are all capex- and program-cycle sensitive; a semiconductor or aerospace down-cycle would hit several niches at once despite diversification.
- **No single explosive driver:** unlike CSCO's AI orders, there is no one product with a 4.5x order ramp — the story is steady compounding + M&A, which fits a momentum panel less cleanly.

### 7. Shortage score and verdict
**Shortage score: 6/10. Verdict: The best backlog momentum in this batch (record $4.54B, orders +35%, September a record month) with a fresh $5B acquisition already contributing — but it is broad niche demand, not a structural shortage, and the stock just sold off 4.5% on a record beat while leverage tripled.**

---

## Batch ranking (shortage score)
1. **CSCO — 7/10** — only name with a genuine demand explosion (AI orders 4.5x), tempered by margin compression and disintermediation.
2. **AME — 6/10** — best backlog/orders momentum, broadest demand, but no single shortage and fresh leverage.
3. **ROK — 3/10** — cyclical recovery story only; backlog still shrinking, book-to-bill ~1, and its Q4 print lands today (Nov 5).

## Appendix — CSCO earnings-quality flag: INVENTORY_BUILD

**What the flag is:** Cisco's inventory rose ~80% in FY26 — to **$5.694B at Jul 25, 2026 from ~$3.16B a year earlier (+$2.53B)** — and inventory purchase commitments rose 125.9% to **$17.17B from $7.60B** (FY26 10-K via SEC-API analysis; btw.media). Raw materials rose to $2.796B and work-in-process surged to $1.140B (from $83M in 2024), while finished goods recovered to $1.525B. The cash-flow statement records a $2.541B inventory use in FY26. Meanwhile FY26 operating cash flow was **$14.177B, essentially flat** despite net income rising to $13.267B (from $10.180B), and free cash flow fell 3.9% to $12.77B.

**Benign or value trap?** Mostly benign, deliberately disclosed, and tied to a named demand signal — not the classic earnings-ahead-of-cash pattern. Cisco's Q3 FY26 commentary (via HyperFRAME summary of the call) says it deployed cash into long-term inventory and component commitments "to shield itself from shortages of critical high-bandwidth memory (HBM), custom ASICs, and optical components," locking in "multi-billion dollar, multi-year supply tranches directly with tier-one semiconductor and memory foundries," with silicon fabrication "locked down… through the end of calendar year 2026." The April-quarter commitments (+111% to $16.03B) were "primarily related to manufacturing Silicon One and other products for hyperscalers" (btw.media). In other words: the build is pre-positioning for the $9.3B of AI orders and the $7.5B FY27 AI revenue target — raw materials and WIP, not unsold finished goods piling up (finished goods $1.525B is only modestly above the 2023 peak of $1.493B).

**The caveat that keeps the flag live:** the build only pays if the orders convert. Operating cash flow flat while revenue grew 12% and commitments more than doubled means Cisco has pre-funded a bet; if hyperscaler AI revenue falls short of $7.5B in FY27, or memory/optics prices fall, the $17.17B commitment book becomes the overhang. Also note the mix effect is already visible in margins (product gross margin −270 bps in Q4 FY26).

**One-line verdict per flag:**
- **INVENTORY_BUILD — Benign-to-watch: a deliberate, disclosed pre-buy of HBM/Silicon One/optics against $9.3B of hyperscaler AI orders, not channel-stuffing — but it converts the thesis into a delivery test, and flat operating cash flow despite higher earnings is the number to re-check at Q1 FY27 (Nov 12).**

## Sources and dates
- Cisco Q4 FY25 call/prepared remarks, Aug 13, 2025 (investor.cisco.com); Cisco Q4 FY26 release + prepared remarks, Aug 12, 2026 (SEC 8-K; s21.q4cdn.com); Cisco Q2 FY26 release, Feb 2026 (newsroom.cisco.com).
- Cisco OCP 2026 release, Oct 12, 2026 (newsroom.cisco.com); Unite.ai / The Inference / EBC / TradingView (Zacks) coverage of Q4 FY26, Aug 2026; BofA Nov 3, 2026 note via The Inference and stockanalysis.com ratings.
- SEC-API Cisco FY26 analysis (10-K FY26, filed 2026; prices as of Oct 9, 2026); btw.media on Cisco AI backlog/inventory; stock-analysis-on.net Cisco inventory history.
- IDC Ethernet switch tracker: Q2 2025 (Sep 11, 2025) and Q4/full-year 2025 (Mar 18, 2026); Next Platform, Jun 23, 2025; Fierce Network on Arista/Nvidia; DK Street Journal on Arista/Nvidia/Broadcom; sotkn.com AI cluster networking explainer, Nov 2, 2026.
- Rockwell Automation Q4 FY25 release + call, Nov 6, 2025 (rockwellautomation.com; Motley Fool transcript); FY25 10-K (filed Nov 12, 2025) via tickerscout.ai; Q3 FY26 release + prepared remarks, Aug 4, 2026; Zacks Q4 FY26 preview, Nov 3, 2026; MarketBeat/Finviz Q4 FY26 estimates; Rockwell FactoryTalk Conductor / NVIDIA Nemotron release, Oct 22, 2026; ABI Research PLC ranking; IoT Analytics industrial automation projects, 2025; GlobeNewswire automation components, May 7, 2025.
- AMETEK Q3 2025 release, Oct 30, 2025 (PRNewswire via CentralCharts); AMETEK Q3 2026 call transcript, Nov 3, 2026 (AlphaStreet/MarketBeat); Zacks Q3 2026 coverage, Nov 4, 2026; Tickeron/TradingKey/Watchlist News Q3 2026 recaps, Nov 3–4, 2026; Insider Monkey on Indicor close, Sep 19, 2026; AMETEK Q3 preview, Zacks; MarketBeat AME quote page (Nov 4, 2026 close $237.30).
- Prices: Finnhub snippets via search (CSCO Nov 4 close $103.61, prev. close $102.97; ROK Nov 4 close $443.88; AME Nov 4 close $237.09 pre-market / $237.30 MarketBeat close).

## Not found / not established
- Cisco: total AI-only backlog (only analyst ~$6B estimate; company has not published an AI-only RPO reconciliation); Cisco AI-gear lead times / price increases; Cisco's exact Q1 FY27 earnings date (Nov 11 vs Nov 12 in different sources).
- Rockwell: Q3 FY26 total backlog figure (not disclosed in the Aug 4, 2026 release/remarks); a precise Rockwell market-share % vs Siemens in its core discrete/PLC market.
- AMETEK: a single-product market-share figure vs a #2 competitor; a specific cause for the Nov 4 −4.5% post-earnings sell-off.
