> Run by: Muse Spark 1.3 (muse-spark-1.3) — full panel

# Final pick — stock-pick-momentum, run 2026-11-25

## THE PICK

**APH — Amphenol Corporation** (Electronic Components), price **\$73.47** (Tue Nov 24, 2026 close, verified — see price note below), market cap ~\$172bn (screen), analyst mean target \$106.97 (+45.6% vs the Nov 24 close).

**Panel vote: 3 of 4 lenses picked APH** (A — supply-chain, B — growth/momentum, D — contrarian, conviction 8/10, 8/10, 7/10); C — quality/moat picked CBOE (8/10) with MSFT runner-up. Runner-up across the panel: ANET (A, B) and CBOE (D). APH also won the Borda ranking (33 points, tied with ANET and MSFT — see final_ranking for the tie-break).

## Price note — the screen's prices are one session stale, and two dossier claims were corrected

The deterministic screen's `currentPrice` field is the **Fri Nov 20 close** (\$69.72 for APH), while its `targetMeanPrice` and `analyst_upside` are Nov 23-based: \$106.97 / \$73.47 ≈ +45.6% from the verified Nov 24 close. Phase 3.5 verification confirmed APH closed **\$73.47 on Nov 24** (Finnhub; MarketBeat \$73.60), ANET **\$168.56**, MSFT **\$496.13**, CBOE **\$362.52**. All scenario math in this writeup uses the **verified Tue Nov 24 closes** for APH; where a Nov 24 close is not independently verified it is implied from the screen's own target/upside (target / (1 + upside)), which reproduces the verified Nov 23 closes exactly for LLY (\$1,364.60) and WST (\$399.30). The screen's Nov 20 prices are not used for the pick.

**Two dossier claims were corrected by verification before this writeup was built** (see "What was verified"): the IT Datacom growth rates were swapped (total IT Datacom grew +117% YoY, +77% organic — there is no separate +117% AI-only rate), and the "cable lead times stretching toward a year / a manufacturer sold out through 2026" claim is unverified (connector lead times found are 8–12 weeks; the sold-out quotes belong to hard drives and HBM). Neither claim is relied on below; the dossier file was corrected in place.

## One-paragraph thesis

Amphenol is the broadest play on the one shortage in this batch documented in hard order-book terms rather than guidance: AI data-center interconnect is capacity-constrained, and in Q3 2026 customers ordered \$12.17B of Amphenol product — 99% more than a year earlier and 1.19x what the company shipped — with the IT Datacom backlog stretching further out than usual. It sells into every accelerator vendor and every hyperscaler, so no single customer can starve it, and its IT Datacom business — 48% of sales, ~3/4 AI, +117% in Q3 — is growing faster than the AI build-out itself. At 21.4x forward earnings it is the cheapest of the AI shortage names, and the Nov 23–24 selloff (APH −5.1% on Nov 24 alone) widened the gap between the order book and the price rather than narrowing it.

## The shortage + backlog evidence

- **Record orders \$12.17B in Q3 2026 (+99% YoY, +13% QoQ)**, book-to-bill **1.19:1** — customers ordered 19% more than Amphenol shipped. Orders exceeded the midpoint of Q4 sales guidance (\$10.3–10.5B) by 17%: more than a full quarter of shipments already booked. (Q3 2026 call, Oct 28, 2026 — CONFIRMED by verification.)
- **IT Datacom +117% YoY (+77% organic) in Q3**, with AI ~3/4 of the segment (~36% of the whole company). Q3 sales \$10.23B (+65% YoY, +37% organic) — the first-ever \$10B quarter; adj. EPS \$0.80 (+74%), beating \$0.73 consensus.
- **Backlog is stretching further out than usual** (BofA question on the Q3 call); management said longer-dated orders are normal and most demand comes from highly capitalised customers, not neoclouds.
- Q4 guide: \$10.3–10.5B sales, \$0.81–0.83 EPS; FY2026 guide \$36.9–37.1B sales (~+60%), adj. EPS \$2.82–2.84 (~+70%).
- Dropped from the thesis: the dossier's "cable lead times toward a year" line — verification could not support it for connectors (8–12 weeks found). The shortage case here rests on the order book, not on lead-time anecdotes.

## Why it's the category leader

#2 in connectors globally (TE #1 at ~15.8–18.2% share, Amphenol ~10.1–12.4%, Molex ~8.0–8.7% per 2026 industry surveys), top-10 in 10 of 11 connector sectors, and #1 where it matters for this thesis: military connectors (36.19% share in 2025 vs TE 14.42%) and the dominant AI-datacom interconnect supplier by growth. The Jan 2026 \$10.5B acquisition of CommScope's connectivity/cable business (ANDREW brand) materially widened its fibre/cable portfolio. In the AI-relevant high-speed datacom niche it is the widest lane, though TE and Molex are credible #2/#3.

## Why it's irreplaceable

The moat is breadth plus qualification lock-in: precision manufacturing across copper, fibre, power and sensors, co-design with every accelerator vendor, and validation cycles in harsh-environment and mil-spec products that take years to repeat. Hyperscalers cannot realistically in-source connectors — it is a fragmented, standards-driven, precision-manufacturing business with low unit economics per part but extreme qualification barriers. The risk is substitution at the architecture level (optics replacing copper inside the rack, co-packaged optics) rather than in-sourcing, and the dossier puts full optical scale-up no earlier than 2029 — beyond this pick's 12–18 month horizon. Disintermediation risk: **low to medium** (A: medium, B: low, D: low; the offsetting weakness is multi-sourcing — Amphenol shares the shortage with TE/Molex/Samtec rather than owning it outright, which caps pricing power versus a true monopoly). Irreplaceability 6/10 — the lowest of the top names, and the honest discount on this pick.

## Scenarios & expected value

All numbers are research scenarios, not guarantees. Prices are the Tue Nov 24, 2026 close (\$73.47). Built on the shortage math: backlog-to-revenue conversion at today's pricing, not bare multiples.

| Scenario | Price | % vs \$73.47 | By when | What drives it |
|---|---|---|---|---|
| Bear | \$52 | -29.2% | 2027-Q2 | Datacenter capex pauses; IT Datacom rolls over (Q4 already guided to mid-single-digit sequential growth); book-to-bill drops below 1.0; orders de-book faster than shipments |
| Base | \$100 | +36.1% | 2027-Q2 | Order book converts at today's pricing; FY2026 guide (\$36.9–37.1B sales, \$2.82–2.84 EPS) delivered; multiple holds near ~21x forward — the base is near the analyst mean target |
| Bull | \$125 | +70.1% | 2027-Q2 | Shortage extends through 2027, book-to-bill stays above 1.15, AI datacom stays triple-digit, and the market re-rates Amphenol from components supplier to the narrow node of the AI buildout |

**Probabilities: bear 25% / base 50% / bull 25%.** Weighted to base because the backlog converts on contract, not on forecast — \$12.17B of Q3 orders is already booked, and most demand comes from highly capitalised customers. Bear is 25%, higher than yesterday's 20%, because the Q4 moderation is already guided and the Nov 23–24 selloff shows the tape punishing AI hardware fast; bull is 25% because the re-rating requires the shortage to persist a full year and the corrected lead-time evidence is weaker than the dossier first claimed.

**Expected value: EV = 0.25 × \$52 + 0.50 × \$100 + 0.25 × \$125 = \$94.25, +28.3% over the \$73.47 close.** That clears the +15% EV guardrail comfortably — this run publishes as an actionable pick, not a pass.

**Market-implied scenario:** the current price sits closest to bear but below base — \$73.47 is well under the \$106.97 mean target, and the market is pricing AI-capex doubt (shares fell ~5% on Nov 24 in a broad AI selloff) rather than the order book. The price is NOT at the bull case: there is room to surprise.

## Key swing factors

1. **Book-to-bill through 2027** — stays above 1.15 (bull) or slips below 1.0 (bear). The single most load-bearing number.
2. **IT Datacom sequential growth** — Q4 guided to mid-single-digit after +30% QoQ in Q3; a second deceleration quarter is the early warning.
3. **Copper vs fiber/CPO migration** — whether Amphenol's optical portfolio and CommScope fiber keep share as 1.6T links move off copper.
4. **Hyperscaler capex** — the ~\$170B calendar-2026 AI buildout continuing into 2027, and Amphenol's share of it vs dual-sourced TE/Molex/Samtec.
5. **CommScope integration** — the raised outlook holding, and whether fiber offsets softness in Communications networks.

## EPIC driver table

| Driver | Effect | Predictability | Independence | Consensus gap |
|---|---|---|---|---|
| Record order book conversion (orders 1.19x sales, backlog stretching out) | ✓ moves value materially — more than a full quarter of shipments pre-booked | ✓ evidence-based: signed orders, not guidance | ✓ market mis-weights it: shares fell ~5% on Nov 24 while the book grows | ✓ falsifiable: book-to-bill <1.0 for a quarter kills the thesis |
| AI capex durability (hyperscaler spend into 2027) | ✓ ~36% of revenue is AI-linked | — partially: capex is announced but can pause | — the market prices this correctly as the main risk | — no gap: everyone watches the same capex numbers |
| Pricing/mix via CommScope fiber + optical | ✓ fiber/structured cabling is the hedge against copper migration | — early: CommScope deal closed Jan 2026, integration is young | ✓ the market treats Amphenol as a copper story; the fiber leg is underappreciated | ✓ falsifiable: CommScope sales vs its raised outlook |

These drivers beat the deprioritised ones (buyback/dividend, small tuck-in acquisitions) because they are the ones that decide whether the backlog is a multi-year annuity or a one-quarter spike.

## Sizing note (from POLICY.md)

The owner's pre-committed policy, applied with this pick's numbers — not personalised advice. `raw = (EV/price − 1) / (1 − bear/price) = (94.25/73.47 − 1) / (1 − 52/73.47) = 0.283 / 0.292 = 0.97`. `size = min(5%, 2.5 × 0.97) = 2.4%` of investable capital. **Pilot regime (POLICY §5) halves it again: ~1.2%.** Next earnings Jan 27, 2027 — 64 days out, so no earnings halving. 15% system cap across all open picks applies; run `scorecard.py` before deploying. Cash-only per POLICY §2 — no margin, no options as leverage substitutes.

## Holding period & exit plan

**Hold horizon: 12–18 months**, tied to the backlog conversion timeline — the thesis is the order book turning into shipments through 2027, not a single print. Base target \$100 by ~2027-Q2; bull target \$125 by ~2027-Q2 if book-to-bill stays above 1.15. **Exit if it hits the downside trigger price \$52 or any thesis-break trigger fires:**

- Book-to-bill below 1.0 for a quarter, or backlog shrinking quarter-over-quarter.
- IT Datacom sequential growth turning negative for two straight quarters.
- A top hyperscaler materially dual-sourcing interconnect away from Amphenol (share loss, not just price pressure).
- Copper-to-fiber/CPO migration accelerating with Amphenol losing optical share.
- CommScope sales missing its raised outlook materially.

**Leverage-safety note:** Amphenol is a cyclical at the heart of the AI capex cycle — ~36% of revenue is AI-linked, and a datacenter capex pause can take a high-beta name down 50%+ fast, which is brutal with margin. This system is cash-only; the leverage discussion here is risk education, not a recommendation, and no specific leverage multiple or position size is suggested.

## Key risks

- **AI concentration (~36% of revenue):** a datacenter capex pause hits hard and fast; Q4 IT Datacom moderation is already guided.
- **Dual-sourcing:** TE, Molex and Samtec are certified at 224G — share loss is the realistic downside, not disintermediation.
- **Technology migration:** copper → fiber/CPO at 1.6T could strand copper expertise; the CommScope/optical hedge is unproven at scale.
- **Leverage:** net debt \$12.6B after the \$10.5B CommScope deal leaves less cushion than debt-free peers (ANET).
- **Input costs:** copper/gold/silver at multi-year highs squeeze margins or force price increases.
- **Neocloud funding risk** if AI buildout financing tightens (management downplays it; most demand is from highly capitalised customers).

## What was verified

Phase 3.5 verification (`parts/2026-11-25/verification.md`): **10 of 12 claims CONFIRMED; 1 contradicted and 1 unverified, both corrected in this writeup.**

- APH orders \$12.17B (+99% YoY), book-to-bill 1.19:1, sales \$10.23B — CONFIRMED (Q3 2026 call transcript, Oct 28, 2026).
- APH IT Datacom growth rates — CONTRADICTED as stated: total IT Datacom grew **+117% YoY (+77% organic)**, not +100%; the +117% belongs to the whole segment, not to AI-only. AI ~3/4 of the segment CONFIRMED. Corrected above and in the dossier.
- APH "cable lead times toward a year / a manufacturer sold out through 2026" — UNVERIFIED: connector lead times found are 8–12 weeks; the sold-out quotes belong to hard drives (Seagate/WD) and HBM. Dropped from the thesis.
- APH analyst mean target \$106.97 and forward PE 21.4 — CONFIRMED (oppstock, Nov 24, 2026; other aggregators \$106.21–\$107.61 / 20.2–20.4x).
- ANET Q3 revenue \$3.66B (+58.5%), EPS \$1.20 vs \$1.08 — CONFIRMED; purchase commitments \$11.4B (from \$9.7B) — CONFIRMED; FY2027 guide ~\$18.5B (+38–40%), AI fabrics ~\$7B — CONFIRMED; IDC Q1 2026 Nvidia 21.5% vs Arista 20.7% datacenter Ethernet — CONFIRMED.
- MSFT commercial RPO \$677B (+73% YoY) — CONFIRMED; Hood's demand-exceeds-supply remark + Azure +48% — CONFIRMED; OpenAI incremental \$250B Azure commitment — CONFIRMED (Q1 FY2027 10-Q, Oct 2026).
- Nov 24 closes: APH \$73.47 (Finnhub; MarketBeat \$73.60), ANET \$168.56, MSFT \$496.13, CBOE \$362.52 — CONFIRMED.

## The panel

- **A — Supply-chain analyst:** APH (runner-up ANET), conviction 8/10. "The hardest backlog evidence in the dossier — record orders at 1.2x sales."
- **B — Growth/momentum investor:** APH (runner-up ANET), conviction 8/10. "Fastest revenue acceleration in the dossier at the cheapest AI-shortage multiple."
- **C — Quality/moat & irreplaceability:** CBOE (runner-up MSFT), conviction 8/10. Ranked APH #8 — "record orders, but a multi-sourced component" (irreplaceability 6/10); penalised ANET to #3 for the live Nvidia Spectrum-X threat.
- **D — Contrarian/risk skeptic:** APH (runner-up CBOE), conviction 7/10. "The AI-shortage name the market still prices as a cyclical connector stock."

Adjudication: APH wins on the vote (3 of 4 single picks) and on the doctrine — it is the only name with a confirmed, quantified order book running ahead of shipments, and its disintermediation risk is low-to-medium with the substitution threat dated 2029+, beyond the pick's horizon. C's dissent is honest and recorded: APH is a multi-sourced component, not a monopoly, which is why its irreplaceability is 6/10 and why the bull case requires a re-rating, not just conversion. The trap filter (disintermediation veto) does not touch APH. ANET is the runner-up on the fastest shortage in the batch, docked for the live Nvidia lead in datacenter Ethernet and Microsoft/Meta concentration.

## Screen metrics for the pick (from shortlist_2026-11-25.json)

APH: rev growth TTM +48.1%, operating margin 28.7%, return on equity 40.1%, net debt/EBITDA 1.15x, ret 12m +19.6%, analyst upside +38.2% (Nov 23-based), forward PE 21.4, market cap ~\$172.2bn, next earnings 2027-01-27 (64 days). No earnings-quality flags. Sub-industry: Electronic Components. Composite score 0.714 (rank 8 of 50) — the composite is not the doctrine; the panel ranked it #1 on the shortage evidence.

*This is research output, not financial advice. All prices are the Tue Nov 24, 2026 close unless noted; all scenario numbers are research estimates, not guarantees. Run date 2026-11-25.*
