# Momentum Research — Batch 2 of 3 (RUN_DATE 2026-10-01)

Dossiers: LRCX, APH, AMAT, CAT. Prepared for the 2026-10-01 momentum stock-pick run.
Sources: earnings calls/press releases, 10-Ks, and financial press; figures quoted with date.

---

## 1. LRCX — Lam Research (wafer fab equipment: etch + deposition)

### Shortage thesis
Etch is the physical bottleneck step in AI memory. A 3D NAND etch is "drilling a perfectly straight hole 1000× thinner than a hair, 50× deeper than it is wide — several billion times per wafer" (equipment research via kiankyars/chips notes, crawled Sep 2026). Lam reported on its fiscal Q4 2026 call (July 29, 2026): NAND revenue more than doubled sequentially, memory rose to 46% of systems revenue on AI-driven storage demand; CFO said gross margin expanded on "pricing actions" — i.e., Lam is extracting price, not discounting, in a shortage. Lam raised its calendar-2026 WFE outlook to the low-$150B range, and Berenberg (Sep 9, 2026) models WFE at $164B in 2026 and $205B in 2027. Deferred revenue rose $213M in the quarter to $2.43B, "primarily due to customer down payments" — customers paying up-front to secure tools.

### Backlog / order book
Lam does not disclose a formal backlog number — **not found**. Proxies: deferred revenue $2.43B (June 2026 quarter, +$213M seq, customer down payments); FQ1 FY27 revenue guide of ~$8.10B ±$400M (reported July 29, 2026), implying year-over-year EPS growth of 71% — booked visibility at least one quarter out.

### Category position
#1 in etch: ~45% etch market share (industry analyses, 2025–2026), #2 overall WFE supplier behind Applied Materials. IndexBox (Sep 2026) lists Lam as the etch market leader ("dominant share in dielectric etch"); Tokyo Electron is #2 in etch (~25%); AMAT is #3 (~30% deposition). Kiyo/Flex conductor-etch lines and SABRE electrochemical deposition are the standard products.

### Irreplaceability / disintermediation
The moat is process-of-record status: each Lam tool is qualified into a fab's recipes over 12–18+ months, and ripping it out means re-qualifying the entire flow — switching costs are near-prohibitive once in production. Hyperscalers cannot in-source: they don't buy fabs, let alone build etch chambers, and there is no substitute physics for plasma etch/deposition in 3D NAND and GAA logic. The structural threat is Chinese domestic substitution (AMEC, NAURA) — but those are 5+ years behind at the leading edge; Lam's share "where it can compete" is stable. **Irreplaceability score: 8.**

### Recent catalysts (last ~3 months)
- Record FQ4 FY26 (July 29): revenue $6.72B (+30% YoY), adj EPS $1.82 (+37%), record op margin 38.4%.
- Raised quarterly dividend ~27% to $0.33/share (Sep 2026).
- Broke ground on new Oregon R&D lab; plans $3B+ global lab-network investment over 5 years (Sep 2026).
- Raised calendar-2026 WFE outlook to low-$150B; Berenberg raised target to $420 (Sep 9, Buy), BofA to $480, Susquehanna $475, Citi $450 (Jun–Jul 2026). Morgan Stanley cut to $367 and UBS to $425 (still Buy) in late Jul/Sep — expect a caution flag at consensus target $361.81.
- Stock +92% YTD, +131% 1yr (Finnhub, Sep 30, 2026); price ~$328.51.

### Risks
China is the largest exposure (~35%+ of revenue; Taiwan/Korea add more) — export-control tightening could strand leading-edge sales. WFE is deeply cyclical; record margins at peak orders can invert fast. P/E ~56 (Finnhub) is demanding; insiders (incl. CEO) have sold only, no buys, in the last six months. Director Bethany Mayer sold ~31% of her stake (Sep 11, 2026).

### Earnings-quality flags
- **HIGH_ACCRUALS** — LRCX FY26 10-K (filed Aug 2026): net income $7.27B vs net cash from operations $5.86B; OCF *fell* YoY ($6.17B → $5.86B) while net income rose $5.36B → $7.27B. The gap is dominated by a $1.96B build in accounts receivable plus a $286M reversal of deferred profit — classic accruals. Verdict: partially benign — customers are blue-chip fabs (TSMC, Samsung, Micron), deferred revenue rose on customer *down payments* (cash collected before revenue), and inventory was held flat ($4.3B) with improving turns (3.0 vs 2.9) — but cash conversion trailing reported earnings two years running is the value-trap warning light; watch it in Q1 FY27.
- **RECEIVABLES_OUTRUN** — Accounts receivable $5.34B vs $3.38B a year earlier (+58%) while FY revenue grew 30%; DSO stretched to ~68.5 days vs 58.4 the prior year. Verdict: mostly benign quarter-end timing — record June-quarter systems shipments plus down-payment-heavy order mix; inventory discipline (flat YoY) argues against channel-stuffing. But the pattern is now two years of receivables growth far outpacing revenue growth, so this is the metric that would confirm the value-trap read if it keeps deteriorating.

### Shortage score: 7/10 — Verdict
Etch is the true AI-memory chokepoint and Lam owns it with pricing power, but the WFE cycle is late-stage and the price (+131% in a year, 56× P/E) leaves no room for a memory capex wobble; the receivables trend needs watching.

---

## 2. APH — Amphenol (interconnect: connectors, cables, fiber, power)

### Shortage thesis
Orders are running 23% faster than Amphenol can ship: record Q2 2026 orders of $10.7B with a book-to-bill of 1.23 (July 29/30, 2026, company press release + CEO R. Adam Norwitt: "we also booked record orders"). Lead times are the hard evidence — CCS/Amphenol fiber lead times have stretched to ~50 weeks, and hyperscalers are now securing capacity years ahead through long-term agreements and purchase orders (Edgewater Research channel check, Sep 2026). Connector supply is "tightening incrementally, with lead times extending and pockets of constraints emerging" (same Sep 2026 survey); Edgewater's B2B is 1.2–1.3×. Per-TPU connector content is exploding: TPU9i's cabled backplane takes connector TAM to >$750/TPU vs $300–350 in TPU7/8, with Amphenol as lead designer.

### Backlog / order book
Amphenol does not disclose a formal backlog figure — **not found** — but reports record quarterly orders ($10.7B, Q2 2026) and a 1.23 book-to-bill; CEO commentary and 50-week lead times imply backlog measured in multiple quarters of shipments. Hyperscalers securing capacity "years ahead" via LTAs gives CY27 visibility already firming ("early planning pointing to sustained double-digit growth," Sep 2026 channel).

### Category position
#2 global connector maker behind TE Connectivity (Amphenol is "the second-largest connector market share globally," Nasdaq industry comparison). But in the segment that matters — AI high-speed interconnect — Amphenol is the #1/lead designer: NVIDIA's VR Ultra backplane IP is licensed *by Amphenol to* Foxconn/TE at NVIDIA's request (Sep 2026), and OverPass cables (12.8 Tbps) replace PCB traces in the largest AI racks. Post–CommScope-CCS acquisition ($10.5B, closed Jan 2026, raised to ~$4.6B of 2026 sales), Amphenol is credible in fiber as well as copper — the "architecture-neutral" position.

### Irreplaceability / disintermediation
The moat is qualification: interconnect is designed into rack/shelf architectures and qualified at the system level — when a failed link can kill an entire training run, hyperscalers don't shop on spec, and Amphenol/TE/Molex are the only shortlist. BUT: hyperscalers multi-source *by design*, and NVIDIA making Amphenol license VR Ultra IP to TE/FIT directly proves customers keep second sources alive — credible competitors exist and are deliberate. Co-packaged optics is the bypass threat: a fast shift to CPO would move content from high-speed copper (Amphenol's highest-share, highest-margin ground) toward optics where Amphenol is the newer entrant. Hyperscalers can't build their own precision interconnect at scale, but they can and do dual-source everything. **Irreplaceability score: 6.**

### Recent catalysts (last ~3 months)
- Record Q2 2026 (July 29): sales $8.76B (+55% YoY, 5.6% above consensus), adj EPS $1.35 (+67%, beat by 13%), adj op margin record 29.8%; IT datacom now 43% of sales, +63% organic.
- Q3 2026 guide of $9.3–9.4B (+50–52% YoY), 7.1% above consensus.
- CommScope CCS 2026 guidance raised to $4.6B sales / $0.30 EPS accretion.
- 2-for-1 stock split completed (shares distributed Sep 2, 2026; trading began Sep 3).
- Stock ~$77 mid-Sep 2026, consolidated ~1% over the prior month after the run-up.

### Risks
Valuation is the big one: ~55× forward earnings, ~7.8× trailing sales, EV/EBITDA ~27.5×; a DCF flagged the stock as overvalued even with rising analyst targets. 43% of sales is now a direct derivative of hyperscaler capex (~$725B combined 2026 guidance, increasingly debt-funded, ~94% of operating cash flow committed per one analysis) — any capex pause hits APH hardest in the portfolio. Debt-to-equity ~133% post-CommScope limits error tolerance. Integration strain at 2× size; raw-fiber input risk. CPO/architecture shift could move margin mix against them.

### Shortage score: 9/10 — Verdict
The purest shortage signal in this batch — 50-week lead times, 1.23 book-to-bill, customers locking capacity years out — but the price (55× forward) already assumes the shortage lasts through 2027, and it's the weakest moat of the four: hyperscalers keep TE/Molex alive on purpose.

---

## 3. AMAT — Applied Materials (WFE: deposition, etch, advanced packaging)

### Shortage thesis
Management's own words on the FQ3 FY26 call (mid-Aug 2026): "most leading edge logic and DRAM fabs are running at full capacity." DRAM-tool revenue grew 52% YoY; advanced-packaging equipment revenue is expected to jump 70% in 2026. Customers have announced plans for 10+ new fabs, and Applied has started negotiating customer contracts *for 2030*. Applied is doubling its manufacturing space and plans to double quarterly system output by 2028 (a "capacity plan, not a revenue forecast," per mgmt) — customers are pushing deliveries against clean-room limits; CFO Brice Hill said customers "found ways around limited clean room space" and then "sharply raised their demand for tool deliveries." The KIOXIA partnership at the $5B EPIC Center (announced late Sep 2026) targets next-gen memory for AI workloads. Applied holds an eight-quarter visibility backlog — customers forecast demand two years out.

### Backlog / order book
No formal backlog dollar figure disclosed — **not found** — but the eight-quarter customer-forecast backlog (CFO, Aug 2026 call) is the visibility proxy, plus tool-delivery contracts being negotiated for 2030 (Motley Fool, Sep 29, 2026) and record Q3/Q4 tool volumes ($7B of tools sold in FQ3, ~77% of $9.12B revenue).

### Category position
The #1 WFE supplier globally with the broadest process portfolio (deposition, etch, inspection/metrology, packaging). In a representative 50k-wpm 7nm DUV fab, Applied holds ~40% of etchers and ~35% of CVD systems (industry estimates cited by thewaytohappinessindia, Aug 2026). Uncontested at the leading edge (sub-3nm logic, HBM production).

### Irreplaceability / disintermediation
Same fab-qualification moat as Lam, wider: single-vendor process integration across deposition–etch–inspection plus the installed-base services annuity (AGS $1.78B/qtr, +22%). No customer can build these tools; there is no substitute physics. The disintermediation threat is not customers but the *state*: Chinese domestic vendors (Naura, AMEC, Piotech) are growing 3× faster than Western incumbents, Beijing pushes 30% local procurement, and Chinese vendors could take 40% of the domestic WFE market by 2030 — cutting ~$3.5B/yr from Applied's addressable China revenue (crackthemarket/Ozeco analysis, Sep 2026). Plus export controls: the affiliates-rule suspension expires November 10, 2026 and reinstates automatically — a dated binary event. **Irreplaceability score: 7** (8–9 on technology, docked for the China structural risk).

### Recent catalysts (last ~3 months)
- Record FQ3 FY26 (mid-Aug): revenue $9.12B (+25% YoY), non-GAAP GM 50.4%, record op margin 34%, record EPS $3.50 (+41%), record $3.04B operating cash flow — 13th straight quarter of YoY GM expansion.
- Raised FQ4 guide to ~$10.25B revenue (+51% YoY) and $4.02 non-GAAP EPS (+85%).
- New DRAM/advanced-packaging systems launched (June 2026); NEXX (ASMPT) acquisition closed (May 2026); Nvidia/Synopsys AI + quantum-chemistry collaboration; KIOXIA next-gen-memory partnership (late Sep 2026); $5B India investment over a decade.
- Morgan Stanley cut target to $563 (from $642, equal weight, Sep 29, 2026) but *raised* 2027 revenue/earnings forecasts — target cut was multiple compression (26×→22×), not a fundamentals call.

### Risks
China is the largest market (28% of FQ3 revenue, $2.506B; Taiwan 22%, Korea 17%, US 15%) — export controls already cost $600M of FY26 revenue, and the Nov 10, 2026 affiliates-rule expiry is a binary re-tightening risk. Domestic substitution is structural, not cyclical. DRAM WFE is heading for a 4th straight growth year — historically unusual, overbuild risk when the cycle turns. Valuation: P/E ~43.6, stock +135% in a year (Finnhub, Sep 30, 2026). Applied is expanding capacity at peak orders, which amplifies the next downturn.

### Shortage score: 8/10 — Verdict
Leading-edge fabs at full capacity, eight quarters of customer visibility, 10+ new fabs coming — the broadest shortage exposure in WFE — but China is both the largest customer and the largest structural threat, and the price (+135% 1yr) is already pricing the boom through 2027.

---

## 4. CAT — Caterpillar (power generation + construction/mining machinery)

### Shortage thesis
CEO Joe Creed on the Q2 2026 call (Aug 4, 2026): "If we can get more units out, they're asking us to give them more units" — data-center customers want more large generators than CAT can build. Power generation sales to users soared 72% in Q2, driven by data-center operators ordering large reciprocating engines and gas turbines; some Power & Energy customers are placing orders as far out as 2030. Capital actions prove the shortage is physical: $725M expansion of an Indiana generator plant, a Kansas plant converted to turbine engines, resumption of 10MW generators last made in 2022; CAT is targeting ~3× 2024 large-engine output by 2030. CAT is one of fewer than five qualified hyperscale-grade backup-power vendors in North America (edgen.tech, Jul 2026).

### Backlog / order book
Record $72B backlog at end of Q2 2026, +92% YoY (+$9B sequentially) — the largest order book in company history; 59% expected to be delivered within 12 months, with power-generation orders booked into 2028–2030 (Aug 4, 2026 earnings release/call).

### Category position
#1 global maker of construction, mining, and power-generation equipment. In data-center power: CAT's edge is large-scale natural-gas turbines for primary on-site power ("data centers as their own utilities"); Cummins dominates high-reliability backup. Generac (GNRC) and Kohler compete at lower MW; Mitsubishi Heavy is the non-US player.

### Irreplaceability / disintermediation
This is the weakest moat of the four. The moat is distribution and scale — the Cat dealer network, the Major Projects rental JV, installed-base service — not physics. Hyperscalers routinely multi-source across CAT, Cummins, Generac, Kohler, and Mitsubishi; a failed engine doesn't take down a training run the way a failed interconnect does, so price competition works. No credible hyperscaler in-sourcing of gensets, but also no lock-in: the switching costs are procurement contracts, not recipes. Large-scale gas-turbine share is CAT's closest thing to a choke point. **Irreplaceability score: 5.**

### Recent catalysts (last ~3 months)
- Record Q2 2026 (Aug 4): first-ever $20B quarter ($20.5B, +24%), adj EPS $8.17 (+73% vs $6.20 est.), adj op margin 21.9% (+430bps), record MP&E free cash flow $5.1B.
- Raised full-year 2026 sales guidance to mid-to-high-teens growth.
- Strategic agreement to deploy 1.25 GW of integrated power infrastructure for hyperscaler AI data centers (Aug 2026); Vertiv turnkey liquid-cooling + power integration targeting Microsoft/Meta.
- WSJ reported (Aug 15, 2026) US manufacturing at its highest level since 2022, driven by AI data centers, naming CAT among the key pivots.

### Risks
CAT is a cyclical at a peak multiple: ~34.5× trailing earnings, ~6× sales, >20× EV/EBITDA vs 22.4× for the S&P 500 (Trefis, Sep 2026); stock is down ~8% in the past month. Power generation is only ~15% of consolidated sales — construction and resources (~50%) can swamp the AI story on a macro turn. Policy risk is live: New York imposed a one-year moratorium on new hyperscale data centers (July 2026); if other states follow, 2027–28 orders get impaired, and long-dated backlog can be rescheduled or canceled. Tariffs are a ~$2.2B full-year drag. Capacity execution is the swing factor — a six-month delay lets Cummins/Mitsubishi close the gap.

### Shortage score: 7/10 — Verdict
The power-gen shortage is real (customers literally begging for units, orders booked to 2030), but it's 15% of a cyclical machinery giant trading at a software multiple with state-level regulatory risk building — the shortage thesis is strong, the vehicle is diluted.

---

## Summary table

| Ticker | Shortage score (0–10) | Irreplaceability (0–10) | Verdict |
|---|---|---|---|
| LRCX | 7 | 8 | Etch is the true AI-memory chokepoint and Lam owns it with pricing power, but the WFE cycle is late-stage and the price (+131% 1yr, 56× P/E) leaves no room for a memory capex wobble; the receivables trend needs watching. |
| APH | 9 | 6 | The purest shortage signal in this batch — 50-week lead times, 1.23 book-to-bill, customers locking capacity years out — but the price (55× forward) already assumes the shortage lasts through 2027, and it's the weakest moat of the four: hyperscalers keep TE/Molex alive on purpose. |
| AMAT | 8 | 7 | Leading-edge fabs at full capacity, eight quarters of customer visibility, 10+ new fabs coming — the broadest shortage exposure in WFE — but China is both the largest customer and the largest structural threat, and the price (+135% 1yr) is already pricing the boom through 2027. |
| CAT | 7 | 5 | The power-gen shortage is real (customers literally begging for units, orders booked to 2030), but it's 15% of a cyclical machinery giant trading at a software multiple with state-level regulatory risk building — the shortage thesis is strong, the vehicle is diluted. |

*Dossier written 2026-10-01 for momentum run batch 2 of 3. No figures fabricated; gaps marked "not found."*
