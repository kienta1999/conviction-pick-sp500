> Run by: Muse Wonder (unknown) — full panel

# Momentum Research Batch 2 — 2026-10-13
Screen context: ANET $210.88 / fwd PE 40.4 / target $242.55 / earnings 2026-11-03; AMAT $497.53 / 26.9 / $638.94 / 2026-11-12; KLAC $190.12 / 28.2 / $232.77 / 2026-10-28; APH $86.19 / 25.9 / $101.29 / 2026-10-28. All four are AI-infrastructure picks-and-shovels, but shortage quality differs sharply: KLAC/AMAT sell into a wafer-fab-equipment (WFE) market raised to ~$150B, ANET is supply-constrained on switch silicon, APH is order-constrained on interconnect — not a hard capacity shortage.

---

## ANET — Arista Networks

**1. Shortage thesis — YES, for high-speed AI Ethernet, driver: AI datacenter buildout.**
Ethernet has taken >65% of new AI back-end deployments (Tamar, early 2026) as it catches InfiniBand on latency. Arista itself is the constrained party: CEO Jayshree Ullal on Q1 2026 call — "the real hole is lead times" from "significant wafer fab shortages"; COO Todd Nightingale: "52-week lead times pretty reliably with reservation needs beyond that" (MarketBeat transcript, 2026-05-05). Q2 call added PCB/capacitor tightness. Inventory ~$2.5B and multi-year purchase commitments are defensive buying, not slack.

**2. Backlog / order book**
No formal backlog disclosed. Best proxies at Q2 2026 (ended 2026-06-30, reported 2026-08-04): deferred revenue **$6.9B**, up from $6.2B in Q1, incl. +$600M sequential product deferred revenue from customer-specific acceptance clauses; shipped AI gear can take 18–24 months to be accepted/recognised (Citi conf., 2026-09-10). Purchase commitments (Arista's own, to suppliers) **$9.7B**, ~3x the $3.6B a year earlier — management locking silicon years out. Deferred revenue ≈ >2 quarters of revenue.

**3. Category position — co-#1, now contested**
IDC Q1 2026 cited in press: Nvidia data-center Ethernet switch revenue $2.1B, **21.5% share**, edging Arista **20.7%**, Cisco 17.8%. Arista had been #1 in data-center switching in early 2025 (~21.5%) and holds >40% in 400G/800G cloud-titan segments per industry summaries — but it is no longer unambiguously #1.

**4. Irreplaceability / disintermediation — 5/10**
Moat: EOS software, operational track record at Microsoft/Meta scale, open/multi-vendor Ethernet (Ultra Ethernet Consortium co-founder, ESUN) vs Nvidia lock-in — hyperscalers actively want a second source. Threat is concrete and already happening, on two fronts: (a) **Nvidia Spectrum-X** bundling switch+DPU+cable+CUDA with the GPU cluster — share <4% → 21.5% in ~2 years; (b) hyperscaler white-box / own designs and Broadcom merchant silicon commoditising the box — Arista does not make its own switch ASICs (Tomahawk 6 from Broadcom), so its value-add is software/systems, replicable in principle. Customers cannot trivially in-source EOS-grade reliability, but they do not need to: Nvidia routes around it.

**5. Recent catalysts (last ~3 months)**
- Q2 2026 (2026-08-04): revenue **$3.04B, +37.7% YoY**, non-GAAP EPS $1.02 vs $0.89 cons.; FY26 guidance **raised to $12.6B (+40%)** from $11.5B, AI revenue ≥$3.5B, campus ≥$1.25B; Q3 guide $3.3B.
- 2026-10-07: **ESUN rack-scale launch** — Etherlink SU-144 scale-up (144 accelerators/rack, to 1,024 cross-rack) engineered with AMD, Arm, Broadcom, d-Matrix, Meta, Microsoft, Qualcomm; demo at OCP Summit Oct 12–15. June: 1.6T 7060XE7 on Tomahawk 6.
- 2026-09-30: Bernstein initiates Outperform, $250 target. Cash $13.3B, no debt.

**6. Risks**
Customer concentration — top-2 hyperscalers ~40–42% of revenue (Microsoft/Meta cited); Nvidia bundling; 40.4x fwd PE prices in flawless AI capex; gross margin already slipping (63.4% Q2 vs 65.6% YoY) on component premiums/tariffs; sole/limited-source components; a hyperscaler capex pause hits networking early.

**7. Shortage score: 7/10 — Verdict:** Real 52-week supply constraint and a raised $12.6B guide, but the shortage benefits the category, not uniquely Arista — Nvidia is now taking the incremental share.

---

## AMAT — Applied Materials

**1. Shortage thesis — YES, for leading-edge WFE, driver: AI chip capacity (logic + HBM/DRAM + advanced packaging).**
SEMI: WFE $143.9B in 2026 → $200B by 2028. Management (Q3 FY26, 2026-08-13): Semiconductor Systems growth in calendar 2026 **>30%** (raised from >20%); leading-edge foundry/logic, DRAM and advanced packaging ≈ **80% of WFE growth in 2026–27**; advanced packaging **>70% growth in 2026**, DRAM revenue +52% YoY to a record. The binding constraint management named is now customer **clean-room space**, not tool demand — customers pulled deliveries forward in 2026 and clean-room availability "will determine what the industry can ship in 2027" (Q3 call summary). AMAT is doubling manufacturing space and targets ability to **double quarterly system output by 2028**.

**2. Backlog / order book**
AMAT does **not disclose a formal backlog**. Proxy: contract liabilities / deferred revenue **$3.27B at 2026-07-26, up from $2.57B at FY-end** (+27% in 9 months, AInvest balance-sheet read). Visibility instead: customers giving **rolling eight-quarter forecasts, some discussions to 2030**, >10 new fab projects announced in Q3 alone; roadmap talks extending ~10 years per call commentary. Booked-out horizon: ~2 years firm-ish, decade-long roadmap alignment — softer than KLAC's hard backlog.

**3. Category position — #1 by breadth/revenue among diversified WFE, #2 overall**
Largest semiconductor-equipment maker by revenue ex-lithography; ~17.9–20% total equipment share (down from 20.0% in 2024, per Pluang/Gartner-style tallies) behind ASML (which monopolises EUV). Category leads: deposition ~35%, CMP >60% at leading nodes, ion implant ~50%. Losing some share in 2025–H1 2026 to Lam, KLA, ASML and Chinese suppliers — #1 position is real but eroding, not expanding.

**4. Irreplaceability / disintermediation — 7/10**
Moat: broadest portfolio in WFE (deposition, etch, CMP, implant, thermal, e-beam metrology — everything except litho/track), integrated materials solutions co-optimising sequences under one vacuum, qualification lock-in per process step, and a huge installed base — >37,000 chambers connected to AIx, AGS services $1.78B in Q3 (+22%). Customers (TSMC/Samsung/Intel) cannot in-source this breadth; attempts at in-house equipment are a noted long-term TAM risk but not a live substitute at leading edge. Weakness vs ASML/KLAC: **every AMAT category has a credible rival** (Lam in etch/deposition, TEL, KLA in inspection) — it wins share step-by-step, it is not a sole gate. EPIC co-development network (11 partners, Broadcom added Q3) deepens lock-in.

**5. Recent catalysts (last ~3 months)**
- Q3 FY26 (2026-08-13): **record revenue $9.12B, +25% YoY / +15% QoQ** (largest QoQ jump in company history), non-GAAP EPS record $3.50 (+41%), gross margin 50.4% (13th straight YoY expansion), operating cash flow record $3.04B; **Q4 guide $10.25B ±$0.5B (+51% YoY at midpoint), EPS $4.02**.
- Process diagnostics & control tracking **>50% growth in 2026**; AGS guide raised to >20% growth in 2026.
- Singapore manufacturing centre opened; +1,500 manufacturing/AGS staff in Q3; agreement to acquire ASMPT's NEXX panel-level packaging business; $5B India investment plan over a decade (reported Sept).

**6. Risks**
Classic WFE cyclicality — stock already ~28% below its $739.67 June high despite records, i.e. market is pricing cycle peak; China was **28% of Q3 revenue** and export controls previously guided to a ~$600M FY26 hit; share loss to Lam/KLAC/ASML/China domestic; clean-room bottleneck caps 2027 shipments regardless of demand; capex intensity jumped to ~9% of revenue (vs 2.8% 14-yr average) locking in fixed costs if cycle bends; pull-forward demand may not repeat.

**7. Shortage score: 8/10 — Verdict:** Broadest beneficiary of a genuine, SEMI-confirmed equipment shortage with accelerating (+51% guided) revenue — explosive torque, but breadth dilutes bottleneck pricing power and cyclicality/China cap the score.

---

## KLAC — KLA Corporation

**1. Shortage thesis — YES, strongest of the batch, driver: process-control intensity rising with AI complexity (2nm/GAA, HBM, EUV-in-DRAM, advanced packaging/hybrid bonding).**
Every added layer/node needs more inspection/metrology per wafer — demand grows faster than WFE itself. Management raised calendar-2026 WFE outlook to **low-$150B** (from ~$140B, and ~$120B in 2025). Evidence of shortage at KLA itself: CFO Bren Higgins (Goldman conf., Sept 2026) — H1 was "somewhat supply constrained… I could ship more if I had more parts even today"; average lead times **~12 months, some products 18–24 months**; earlier in 2026 described as "virtually sold out across most products in H1." H2 2026 revenue guided **~+20% vs H1** purely as long-lead supply comes online.

**2. Backlog / order book**
Hard backlog, from FY2026 10-K (year ended 2026-06-30): **$12.57B, up from $7.86B a year earlier (+60%)**, increase explicitly "due to strong demand driven by the AI infrastructure buildout." That is ~0.93x FY26 revenue of $13.58B — roughly 3–4 quarters of systems revenue, with 12–24-month lead times implying booking well into 2027. Caveat in the 10-K itself: backlog timing is not a reliable guide to revenue recognition; pushout/cancellation risk rises as customers balance project timing. Contract liabilities $1.78B at 2026-06-30.

**3. Category position — clear #1**
Dominant in process control: **~52–62% global share** (Gartner-cited ~62% in leading-edge process control; ~52% inspection, ~85% reticle inspection in industry primers) vs #2 Applied Materials' diagnostics unit and Onto Innovation — no rival close to parity. Process-control share of WFE keeps rising with node complexity.

**4. Irreplaceability / disintermediation — 9/10**
Moat: physics-plus-algorithms — broadband plasma optical inspection, e-beam, and yield data accumulated over decades; ~1,600–1,700 applications engineers embedded in customer fabs; qualification lock-in (a yield tool is qualified into a process flow and almost never ripped out mid-node). Hyperscalers are irrelevant as in-sourcers here — customers are TSMC/Samsung/SK hynix, and **no fab can in-source inspection**: you cannot yield-manage a 2nm line without KLA-class tools, and only a handful of firms on earth (KLA, AMAT, Hitachi High-Tech, Lasertec in niches) make any of it. Concrete threat is only at the edges: AMAT growing diagnostics >50% in 2026 and ASML bundling metrology/inspection with EUV — share nibbling, not bypass. No substitute technology routes around defect inspection at smaller geometries; intensity per wafer rises.

**5. Recent catalysts (last ~3 months)**
- Q4 FY26 (2026-07-28): revenue **$3.66B, +15% YoY**, non-GAAP EPS $1.05 vs $1.00 cons., gross margin 62.4%; **Q1 FY27 guide ~$4.0B ±$0.2B**, GM 62.5% ±1pt.
- Advanced-packaging process-control revenue to reach **~$1.1B in 2026, +>70% YoY** (almost 2x market growth); WFE outlook raised to low-$150B; Sept-quarter mix guide: foundry/logic 73% / memory 27% (DRAM ~90% of memory).
- Sept investor conferences: management reiterated 2027 growth at least as strong as 2026, several new greenfield fabs in 2027; Investor-Day frame of 17% revenue CAGR to 2030 cited at Goldman conf. Negative: Morgan Stanley cut target to $227 from $253 (2026-10-05) on margin caution; CEO Wallace sold 72,019 shares 2026-09-15 under disclosed filing.

**6. Risks**
China ~28% of 2025 revenue, mid-to-high-20s% expected 2026 — export-control escalation is the biggest single hit; memory mix rising (27% → more in Dec quarter) adds DRAM cyclicality; tariffs ~100bp gross-margin drag guided, rising memory-component costs pressure GM through 2027; WFE cyclicality at a low-$150B peak-ish print; valuation (stock had traded to $307 high, since split-adjusted volatile) and insider selling; backlog pushouts explicitly flagged in 10-K.

**7. Shortage score: 9/10 — Verdict:** The purest shortage in the batch — sold out, 12–24-month lead times, backlog +60% to $12.57B, and a ~60% share of a category whose intensity structurally outgrows WFE.

### Earnings-quality addendum — KLAC RECEIVABLES_OUTRUN (recv_rev_divergence +0.12)
Evidence: Q4 FY26 cash-flow statement shows accounts receivable consumed **$586M of cash in the June quarter alone (vs $68M a year earlier)**, with operating cash flow $906M vs net income $1,363M — cash conversion trailed earnings in the quarter (also flagged in press, e.g. TS2, Sept 2026). But the 10-K business model explains the mechanics: terms are **70–90% payable within 30–60 days of shipment, remainder within 30 days of acceptance**, and revenue is recognised on shipment/transfer of control while fab readiness and acceptance stretch out — exactly what happens when shipments surge +15–20% into capacity-constrained customer fabs late in a quarter. Contract assets also rose ($124.1M of revenue recognised subject to non-time conditions). Backlog +60% and deferred system revenue +$312M in the quarter corroborate real, ordered demand rather than stuffed channels; no disclosure of loosened terms, extended DSO policy, or aged-receivable deterioration was found.
**Verdict: Mostly benign business-model timing — acceptance-based billing on a shipment surge — not earnings running ahead of cash, but monitor: if receivables keep outrunning revenue for 2+ more quarters while backlog flattens, it flips to a warning.**

---

## APH — Amphenol

**1. Shortage thesis — PARTIAL, driver: AI datacenter interconnect (high-speed copper + fiber + power).**
Not a structural shortage of connectors globally — APH can and does add capacity — but AI racks are interconnect-bound: every GPU rack needs orders of magnitude more high-speed copper, fiber and power interconnect, and qualified supply lags. CEO framing: interconnect as the "central nervous system" of AI; a ~$3M rack is worthless if connectors do not arrive (Fool, 2026-10-01). IT datacom organic growth **+63% YoY in Q2** (reported +89% incl. acquisitions), now **43% of sales**, ~4x its size two years ago. Customers place long-term non-cancelable orders (management cited at Citi conf. — company does not announce them). No lead-time/sold-out disclosures comparable to ANET/KLAC found — "not found" for explicit lead-time extension.

**2. Backlog / order book**
APH does not report a dollar backlog. Best evidence: **Q2 2026 orders a record $10.7B, book-to-bill 1.23:1** — orders 23% above shipments, the clearest forward indicator in the print. Plus undisclosed long-term non-cancelable customer commitments per management conference remarks. Horizon: not quantified — "not found."

**3. Category position — #1 / #2, effectively co-leader and now largest by momentum**
Historically #2 in global connectors behind TE Connectivity (TE ~16.7% share in older Bishop data vs APH ~9% then); APH has since outgrown the field for a decade (fastest-growing major, ~14.8% 10-yr CAGR) and with Q2 revenue annualising well above TE's connector revenue and a market cap ~3x TE's, it is now described as the leading high-performance interconnect supplier, dominant in AI datacom specifically. Precise current global share vs TE: "not found" from a primary source — treat as co-#1 overall, clear #1 in AI-server interconnect.

**4. Irreplaceability / disintermediation — 6/10**
Moat: qualification/design-in lock-in (a connector qualified into a server/rack design, or mil-spec in defense/aerospace, stays for the platform life), signal-integrity know-how at 224G+ speeds, breadth across **copper + fiber + power** (now architecture-neutral after CommScope CCS), decentralised entrepreneurial model with deep co-location at customers, and scale manufacturing. In-sourcing threat is low — hyperscalers do not make connectors — but **substitution/bypass is real**: Nvidia integrated rack systems can specify rival interconnect (TE, Molex, Samtec, Luxshare), optical-vs-copper architecture shifts can strand a product line (Baron noted market "copper displacement fears" in 2026), and connectors are ultimately precision manufacturing that Asian rivals (Luxshare, JONHON) can replicate at the lower end. Nobody bypasses interconnect itself — every architecture needs it — but they can bypass Amphenol for a given socket.

**5. Recent catalysts (last ~3 months)**
- Q2 2026 (2026-07-30): **record sales $8.76B, +55% YoY (organic +30%)**, adj. EPS $1.35 (+67%) vs $1.19 cons., adj. operating margin record **29.8%** (Communications Solutions 33.6%); **Q3 guide $9.3–9.4B (+50–52% YoY), EPS $1.40–1.42**.
- CommScope CCS (closed Jan 2026, $10.5B): Q2 sales >$1.2B, IT datacom nearly doubled YoY; **2026 CCS expectation raised to $4.6B from $4.1B**, EPS accretion raised to $0.30.
- Continued M&A: EI.com (Italy, defense/industrial interconnect) closed in Q2 period; hedge-fund letters Q3 2026 cite APH as a top AI-infrastructure add, estimates +60% EPS growth expected in 2026.

**6. Risks**
Mix concentration flipped: **43% of sales now IT datacom** — a hyperscaler capex pause hits APH first and hardest among its end markets; leverage from the $10.5B CommScope deal (debt-to-equity cited ~133% in mid-2026 commentary) plus integration risk; valuation — traded at up to ~55x forward earlier in 2026 per press (screen now 25.9x fwd on post-split/updated estimates, target $101.29); copper-displacement/optical transition risk; higher tax rate guided; customer bargaining power at hyperscale volumes pressures the record 29.8% margin.

**7. Shortage score: 6/10 — Verdict:** Record 1.23 book-to-bill and +63% organic AI datacom growth prove demand outruns shipments, but interconnect is expandable capacity, not a physics bottleneck — a demand surge APH can meet, not a shortage only APH can fill.

---

## Batch ranking (shortage quality)
1. **KLAC 9/10** — sold out, $12.57B backlog, ~60% share, irreplaceability 9/10
2. **AMAT 8/10** — broadest WFE torque, accelerating to +51% guided growth, irreplaceability 7/10
3. **ANET 7/10** — 52-week lead times but Nvidia now #1 in its category, irreplaceability 5/10
4. **APH 6/10** — 1.23 book-to-bill demand surge, replicable supply, irreplaceability 6/10

Sources: company earnings releases/calls and 10-K via PR Newswire, MarketBeat, Motley Fool, GuruFocus transcripts (ANET Q1/Q2 2026, KLAC Q4 FY26, APH Q2 2026, AMAT Q3 FY26, all Jul–Aug 2026); KLAC FY2026 10-K backlog and payment-terms disclosures via StockTitan; Arista press release 2026-10-07 (ESUN); IDC Q1 2026 switch share via AInvest; SEMI WFE forecast via AInvest; Zacks (KLAC/AMAT/APH, Sept–Oct 2026); Insider Monkey (AMAT Q3, APH letters). Where a figure could not be sourced it is marked "not found" rather than estimated.
