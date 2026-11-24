> Run by: Muse Spark 1.3 — full panel

# Final pick — stock-pick-momentum, run 2026-11-24

## THE PICK

**APH — Amphenol Corporation** (Electronic Components), price **\$77.41** (Mon Nov 23, 2026 close, verified — see price note below), market cap ~\$172bn (screen), analyst mean target \$106.97 (+38.2%).

**Panel vote: unanimous 4/4.** Every lens — supply-chain, growth/momentum, quality/moat, contrarian — picked APH as its single pick, conviction 8/10 each, runner-up WST in all four ballots. This is the first unanimous momentum pick in this run series' recent window.

## Price note — the screen's prices are one session stale

The deterministic screen's `currentPrice` field is the **Fri Nov 20 close** (\$69.72 for APH), while its `targetMeanPrice` and `analyst_upside` are Nov 23-based: \$106.97 / \$77.41 = +38.2%, exactly the screen's upside figure. Phase 3.5 verification confirmed APH closed **\$77.41 on Nov 23**; Finnhub confirms WST \$399.30 and LLY \$1,364.60 on Nov 23 (vs screen \$390.30 / \$1,347.11). All prices and scenario math in this writeup use the **verified Mon Nov 23 closes**; where a Nov 23 close is not independently verified it is implied from the screen's own target/upside (target / (1 + upside)), which reproduces the verified closes exactly for APH, WST, LLY and VEEV (\$268.65, matching the dossier's stated Nov 23 close). The screen's Nov 20 prices would have overstated APH's upside by ~11 points — the writeup does not use them.

## One-paragraph thesis

Amphenol is the only name in the 13-name dossier that satisfies all three legs of the momentum doctrine at once: the #1 interconnect manufacturer globally, sitting on a genuine physical bottleneck — at 224 Gb/s per lane, signals degrade on PCB traces and only a handful of certified suppliers can build the cable assemblies AI training runs depend on — with orders exceeding shipments for four straight quarters while the order book keeps growing. Q3 2026 was the first-ever \$10B quarter (sales \$10.23B, +65%, +37% organic; adj. EPS \$0.80, +74%), FY2026 guidance implies +60% sales and +70% EPS, and at 21.4x forward earnings it is the cheapest of the AI shortage names — the market is doubting "what's next for 2027 profit" (shares off their Oct 6 high) while the backlog compounds.

## The shortage + backlog evidence

- **Record orders \$12.17B in Q3 2026 (+99% YoY, +13% QoQ)**, book-to-bill **1.19:1** — the fourth consecutive quarter above 1.0 (1.31 / 1.24 / 1.23 / 1.19). Orders were 17% above the midpoint of Q4 sales guidance (\$10.3–10.5B): more than a full quarter of shipments already booked.
- **Backlog grew \$1.94B in the quarter.** The dossier's "\$5.7B year-to-date" backlog growth is a secondary-source derivation, not a company-stated total — treat it as indicative, not verified.
- **High-speed assembly lead times exceed 12 weeks**; procurement is advised to lock multi-year volume agreements for 2027 delivery. IT Datacom (48% of sales) grew 100% in dollars / 77% organically in Q3; AI is ~3/4 of IT Datacom (~36% of the whole company).
- Q4 guide: \$10.3–10.5B sales, \$0.81–0.83 EPS; FY2026 guide \$36.9–37.1B sales, \$2.82–2.84 EPS. CommScope outlook raised again to \$5.1B sales. 2-for-1 split effective Sep 3, 2026; ~\$1.6B committed to four acquisitions, 20% dividend increase, new \$4B buyback.

## Why it's the category leader

#1 interconnect manufacturer globally: >15% share of industrial connectors (TE 13%, Molex 7.5%); >12.5% of fiber optic connectors; 36.2% of military connectors (TE 14.4%); 31.2% of North America circular connectors; 13.0% of cable assemblies (TE 12.5%) — Global Market Insights 2025 data. In the AI-relevant high-speed datacom niche it is the widest lane, though TE and Molex are credible #2/#3.

## Why it's irreplaceable

The moat is signal-integrity process knowledge at 224G/448G, rack-level qualification lock-in (a failed link can kill an entire training run — "nobody chases the cheapest cable"), vertically integrated global manufacturing, and breadth across copper + fiber + power (CommScope acquisition, \$10.5B, closed 2025, adds fiber/structured cabling, \$3.6B sales). Hyperscalers cannot realistically in-source this: it is precision manufacturing + qualification, not software. **Correction from verification:** the dossier's "only ~3 firms" is overstated — PNA Fiber (July 2026) lists **four** firms in the first 224G certification batch (Amphenol, Molex, TE, **Samtec**), plus Chinese vendors now in volume supply. The node is narrow (a handful of certified suppliers), not a three-firm oligopoly. Disintermediation risk: **low**. The live risks are dual-sourcing (share loss, not disintermediation) and copper-to-fiber/CPO migration at 1.6T, hedged via CommScope and Amphenol's own optical portfolio (XPO OverPass, 448G co-packaged copper demos). Irreplaceability 8/10 — the highest of any name in the set that also has a real shortage.

## Scenarios & expected value

All numbers are research scenarios, not guarantees. Prices are the Mon Nov 23, 2026 close (\$77.41). Built on the shortage math: backlog-to-revenue conversion at today's pricing, not bare multiples.

| Scenario | Price | % vs \$77.41 | By when | What drives it |
|---|---|---|---|---|
| Bear | \$62 | -19.9% | 2027-Q2 | Datacenter capex pauses; IT Datacom rolls over (Q4 already guided to mid-single-digit sequential growth); book-to-bill drops below 1.0; copper-to-fiber migration strands copper share |
| Base | \$107 | +38.2% | 2027-Q3 | Order book converts at today's pricing; FY2026 guide (\$36.9–37.1B sales, \$2.82–2.84 EPS) delivered; multiple holds near ~21x forward — the base is the analyst mean target |
| Bull | \$125 | +61.5% | 2027-Q4 | Shortage extends through 2027, book-to-bill stays above 1.15, and the market re-rates Amphenol from components supplier to the narrow node of the AI buildout |

**Probabilities: bear 20% / base 55% / bull 25%.** Weighted to base because the backlog converts on contract, not on forecast — \$12.17B of Q3 orders is already booked, and most demand comes from highly capitalised customers, not neoclouds. Bear is 20%, not higher, because the order book is a full quarter ahead of shipments and lead times are still >12 weeks; bull is 25% because the re-rating requires the shortage to persist a full year and the Q4 moderation is already visible.

**Expected value: EV = 0.20 × \$62 + 0.55 × \$107 + 0.25 × \$125 = \$102.50, +32.4% over the \$77.41 close.** That clears the +15% EV guardrail comfortably — this run publishes as an actionable pick, not a pass.

**Market-implied scenario:** the current price sits closest to base but below it — \$77.41 is well under the \$106.97 mean target, and the market is pricing the ~\$170B of AI capex doubt (shares off the Oct 6 high) rather than the order book. The price is NOT at the bull case: there is room to surprise.

## Key swing factors

1. **Book-to-bill through 2027** — stays above 1.15 (bull) or slips below 1.0 (bear). The single most load-bearing number.
2. **IT Datacom sequential growth** — Q4 guided to mid-single-digit after +30% in Q3; a second deceleration quarter is the early warning.
3. **Copper vs fiber/CPO migration** — whether Amphenol's optical portfolio and CommScope fiber keep share as 1.6T links move off copper.
4. **Hyperscaler capex** — the \$170B calendar-2026 AI buildout continuing into 2027, and Amphenol's share of it vs dual-sourced TE/Molex/Samtec.
5. **CommScope integration** — the \$5.1B sales outlook holding, and whether fiber offsets the 28% organic decline in Communications networks.

## EPIC driver table

| Driver | Effect | Predictability | Independence | Consensus gap |
|---|---|---|---|---|
| 224G backlog conversion (orders > shipments, >12-week lead times) | ✓ moves value materially — a full quarter of shipments pre-booked | ✓ evidence-based: four straight quarters of book-to-bill >1.0 | ✓ market mis-weights it: shares off highs on "what's next for 2027 profit" while the book grows | ✓ falsifiable: book-to-bill <1.0 for a quarter kills the thesis |
| AI capex durability (hyperscaler spend into 2027) | ✓ ~36% of revenue is AI-linked | — partially: capex is announced but can pause | — the market prices this correctly as the main risk | — no gap: everyone watches the same capex numbers |
| Pricing/mix via CommScope fiber + optical | ✓ fiber/structured cabling is the hedge against copper migration | — early: CommScope outlook raised twice, but integration is young | ✓ the market treats Amphenol as a copper story; the fiber leg is underappreciated | ✓ falsifiable: CommScope sales vs the \$5.1B outlook |

These drivers beat the deprioritised ones (buyback/dividend, the 2-for-1 split, the four small acquisitions) because they are the ones that decide whether the backlog is a multi-year annuity or a one-quarter spike.

## Sizing note (from POLICY.md)

The owner's pre-committed policy, applied with this pick's numbers — not personalised advice. `raw = (EV/price − 1) / (1 − bear/price) = (102.50/77.41 − 1) / (1 − 62/77.41) = 0.324 / 0.199 = 1.63`. `size = min(5%, 2.5 × 1.63) = 4.1%` of investable capital. **Pilot regime (POLICY §5) halves it again: ~2.0%.** Next earnings Jan 27, 2027 — 64 days out, so no earnings halving. 15% system cap across all open picks applies; run `scorecard.py` before deploying. Cash-only per POLICY §2 — no margin, no options as leverage substitutes.

## Holding period & exit plan

**Hold horizon: 12–18 months**, tied to the backlog conversion timeline — the thesis is the order book turning into shipments through 2027, not a single print. Base target \$107 by ~2027-Q3; bull target \$125 by ~2027-Q4 if book-to-bill stays above 1.15. **Exit if it hits the downside trigger price \$62 or any thesis-break trigger fires:**

- Book-to-bill below 1.0 for a quarter, or backlog shrinking quarter-over-quarter.
- IT Datacom sequential growth turning negative for two straight quarters.
- A top hyperscaler materially dual-sourcing interconnect away from Amphenol (share loss, not just price pressure).
- Copper-to-fiber/CPO migration accelerating with Amphenol losing optical share.
- CommScope sales missing its raised \$5.1B outlook materially.

**Leverage-safety note:** Amphenol is a cyclical at the heart of the AI capex cycle — ~36% of revenue is AI-linked, and a datacenter capex pause can take a high-beta name down 50%+ fast, which is brutal with margin. This system is cash-only; the leverage discussion here is risk education, not a recommendation, and no specific leverage multiple or position size is suggested.

## Key risks

- **AI concentration (~36% of revenue):** a datacenter capex pause hits hard and fast; Q4 IT Datacom moderation is already guided.
- **Dual-sourcing:** TE, Molex and now Samtec are certified at 224G — share loss is the realistic downside, not disintermediation.
- **Technology migration:** copper → fiber/CPO at 1.6T could strand copper expertise; the CommScope/optical hedge is unproven at scale.
- **Communications networks fell 28% organically** (broadband softness) — the non-AI half is not all growing.
- **Neocloud funding risk** if AI buildout financing tightens (management downplays it; most demand is from highly capitalised customers).

## What was verified

Phase 3.5 verification (`parts/2026-11-24/verification.md`): **7 of 9 claims CONFIRMED; 2 contradicted in part and corrected in this writeup.**

- APH orders \$12.17B (+99% YoY), book-to-bill 1.19:1, backlog +\$1.94B in the quarter — CONFIRMED (Oct 28, 2026 call transcript, SEC 8-K). The \$5.7B YTD backlog figure is a secondary-source derivation, not company-stated.
- APH "only ~3 firms can supply qualified 224G interconnect" — CONTRADICTED in part: four firms in the first 224G certification batch (Amphenol, Molex, TE, Samtec) plus Chinese vendors in volume supply. Softened to "a handful of certified suppliers" above. Lead times >12 weeks CONFIRMED verbatim.
- APH Q3 sales \$10.23B, adj EPS \$0.80, FY26 guide \$36.9–37.1B / \$2.82–2.84 — CONFIRMED.
- WST HVP \$466.7m (+20.3% organic), GLP-1 HVP "well into the 30s", pricing +4pts, 18–24-month capacity, Q3 sales \$874.5m / adj EPS \$2.66, FY26 guide — all CONFIRMED.
- LLY tirzepatide shortage resolved Dec 19, 2024 — CONFIRMED, but **semaglutide was resolved Feb 21, 2025, not Dec 2024**; corrected. "No Zepbound shortage currently" CONFIRMED in substance.
- LLY Q3 revenue \$24.397B (+39%), Mounjaro \$10.723B (+65%), Zepbound \$5.352B (+49%) — CONFIRMED (SEC 8-K, Oct 29, 2026).
- LLY retatrutide head-to-head win — CONFIRMED with correction: trial is **TRANSCEND-T2D-2** (Oct 28, 2026), retatrutide 12 mg 20.9% vs semaglutide 9.4% at 80 weeks, Q1 2027 filing planned. The dossier's "22.6% in TRIUMPH-1" matches no published figure (actual: 28.3% efficacy / 25.0% treatment-regimen) and is dropped from this writeup.
- **Price staleness found by the verifier:** the screen's `currentPrice` is the Fri Nov 20 close; APH closed \$77.41 on Nov 23 (not \$69.72). Scenario math here uses the verified Nov 23 closes.

## The panel

- **A — Supply-chain analyst:** APH (runner-up WST), conviction 8/10. "The only name satisfying all three doctrine legs."
- **B — Growth/momentum investor:** APH (runner-up WST), conviction 8/10. "Fastest compounder that also passes the doctrine."
- **C — Quality/moat & irreplaceability:** APH (runner-up WST), conviction 8/10. Vetoed ANET (rents Broadcom silicon; NVIDIA now leads datacenter Ethernet).
- **D — Contrarian/risk skeptic:** APH (runner-up WST), conviction 8/10. Cheapest of the growth peers at 21.4x forward while the market doubts 2027 profit.

Adjudication: no adjudication was needed — the panel was unanimous on both the pick and the runner-up. The trap filter (disintermediation veto) does not touch APH: all four lenses rate its disintermediation risk low, and the verifier's correction (four certified suppliers, not three) narrows the moat slightly without breaking it. WST is the unanimous runner-up on the GLP-1 elastomer bottleneck, docked for +55.4% in 12 months at 38.4x forward and the unresolved receivables flag.

## Screen metrics for the pick (from shortlist_2026-11-24.json)

APH: rev growth TTM +48.2%, operating margin 28.7%, ret 12m +19.6%, analyst upside +38.2% (Nov 23-based), forward PE 21.4, market cap ~\$172.2bn, next earnings 2027-01-27 (64 days). No earnings-quality flags. Sub-industry: Electronic Components. Composite score 0.711 (rank 8 of 50) — the composite is not the doctrine; the panel ranked it #1 on the shortage evidence.

*This is research output, not financial advice. All prices are the Mon Nov 23, 2026 close; all scenario numbers are research estimates, not guarantees. Run date 2026-11-24.*
