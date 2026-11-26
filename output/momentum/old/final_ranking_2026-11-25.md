> Run by: Muse Spark 1.3 (muse-spark-1.3) — full panel

# Final ranking — stock-pick-momentum, run 2026-11-25

## OFFICIAL PICK — consensus top 3

Consensus top 3 (5 runs, 2026-11-21 → 2026-11-25, `output/momentum/consensus_2026-11-25.md`): **MSFT (43 pts), WST (37), LLY (30)**. The consensus only moves when several panels agree — MSFT has been top 10 in 5/5 runs and top 3 in 4/5. Today's Borda #1 is APH (consensus #5, 20 pts, top 10 in only 2/5 runs) and today's single pick is also APH — today's view and the consensus differ: the panel moved to APH on the confirmed \$12.17B order book (and APH has now been daily #1 two runs running), while the consensus still anchors on MSFT/WST/LLY. The screen-only top 3 (composite rank, no AI) is ANET, LLY, EOG.

Note on prices: the screen's `currentPrice` is the Fri Nov 20 close; its `targetMeanPrice` / `analyst_upside` are Nov 23-based. Prices in this writeup are the **verified Tue Nov 24 closes** for ranks 1–4 — APH \$73.47, ANET \$168.56, MSFT \$496.13, CBOE \$362.52 (verified by Phase 3.5 / Finnhub) — and, for the rest, implied from the screen's own target/upside (target / (1 + upside)), which reproduces the verified Nov 23 closes exactly for LLY (\$1,364.60) and WST (\$399.30). The screen's Nov 20 prices would overstate upside and are not used.

## The ranking (today's Borda)

Four lenses, one round (R = 1). Borda: rank 1 = 10 pts … rank 10 = 1, unranked = 0.

Prices: ranks 1–4 are verified Tue Nov 24, 2026 closes (Finnhub — APH \$73.47, ANET \$168.56, MSFT \$496.13, CBOE \$362.52). Ranks 5–10 are screen-implied Mon Nov 23 closes (target / (1 + upside) from `shortlist_2026-11-25.json` — this reproduces the verified Nov 23 closes exactly for LLY and WST). The screen's own `currentPrice` is the Fri Nov 20 close and is not used.

| Rank | Ticker | Company | Sector | Price | Analyst mean target | Fwd PE | Shortage | Irreplace. | Borda | Appear. | #1 | Avg place | One-line case |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | APH | Amphenol | Information Technology | \$73.47 | \$106.97 (+45.6%) | 21.4 | 8/10 | 6/10 | 33 | 4/4 | 3 | 2.75 | Record \$12.17B orders at 1.2x sales; cheapest AI shortage at 21.4x |
| 2 | ANET | Arista Networks | Information Technology | \$168.56 | \$249.65 (+48.1%) | 29.5 | 9/10 | 7/10 | 33 | 4/4 | 0 | 2.75 | AI-fabric shortage, FY27 pre-guided +38–40%; Nvidia now leads Ethernet |
| 3 | MSFT | Microsoft | Information Technology | \$496.13 | \$636.12 (+28.2%) | 20.4 | 8/10 | 8/10 | 33 | 4/4 | 0 | 2.75 | \$677bn RPO, Azure demand exceeds supply; too big for explosive upside |
| 4 | CBOE | Cboe Global Markets | Financials | \$362.52 | \$360.27 (-0.6%) | 22.8 | 8/10 | 9/10 | 32 | 4/4 | 1 | 3.00 | SPX monopoly locked to 2051, record 0DTE; already above mean target |
| 5 | LLY | Eli Lilly | Health Care | \$1,364.60 | \$1,470.06 (+7.7%) | 26.8 | 4/10 | 9/10 | 21 | 4/4 | 0 | 5.75 | Shortage over; #1 GLP-1, retatrutide BLA Q1 2027 |
| 6 | WST | West Pharmaceutical Services | Health Care | \$399.30 | \$471.00 (+18.0%) | 38.4 | 6/10 | 8/10 | 20 | 4/4 | 0 | 6.00 | GLP-1 elastomer bottleneck, Annex 1 wave, margin expansion |
| 7 | VRSN | VeriSign | Information Technology | \$313.95 | \$339.60 (+8.2%) | 28.6 | 7/10 | 10/10 | 18 | 3/4 | 0 | 5.00 | Sole .com registry; four years of +7% price hikes, ~6% growth |
| 8 | MA | Mastercard | Financials | \$635.48 | \$720.69 (+13.4%) | 27.4 | 3/10 | 9/10 | 10 | 3/4 | 0 | 7.67 | Duopoly toll road, services +19%; stablecoin answer via BVNK |
| 9 | UNP | Union Pacific | Industrials | \$288.89 | \$329.96 (+14.2%) | 20.1 | 4/10 | 8/10 | 8 | 3/4 | 0 | 8.33 | Record intermodal volumes; NS merger is a regulatory coin flip |
| 10 | VRTX | Vertex Pharmaceuticals | Health Care | \$538.54 | \$595.36 (+10.6%) | 27.0 | 2/10 | 10/10 | 5 | 2/4 | 0 | 8.50 | CF monopoly; Nov 30 PDUFA binary, not a shortage bet |

Tie-breaks: APH, ANET and MSFT tie at 33 Borda with identical appearances (4/4) and identical average placement (2.75). APH takes #1 on the doctrine — it holds 3 of the 4 single-pick votes and the hardest backlog evidence in the dossier (confirmed \$12.17B orders at 1.19x sales). ANET takes #2 over MSFT on the doctrine: shortage 9/10 vs 8/10 and a higher base-case upside (+33.5% vs +20.9%). CBOE at 32 is one point behind the tie — the closest near-miss at the top in this run series. VRTX takes #10 over IDXX and VEEV (both 3 Borda) on points alone.

## Per-name thesis

**1. APH —** The only name with a confirmed, quantified order book running ahead of shipments: record Q3 orders \$12.17B, +99% YoY, book-to-bill 1.19, with IT Datacom +117% (+77% organic) and AI ~3/4 of the segment. The moat is qualification lock-in and breadth across every accelerator vendor; the discount is multi-sourcing (irreplaceability 6/10, #2 behind TE) and the optical-substitution horizon (2029+). At 21.4x forward it is the cheapest AI-shortage name, and the Nov 24 selloff widened the gap to the \$106.97 target. See `final_pick_2026-11-25.md` for the full writeup.

**2. ANET —** The deepest shortage in the batch (9/10): component lead times 38–52 weeks, purchase commitments \$11.4B (from \$9.7B in Q2), Q3 revenue \$3.66B (+58.5% YoY, fastest since IPO), and an initial FY2027 guide of ~\$18.5B (+38–40%) with AI fabrics ~\$7B — all confirmed by verification. The reason it is #2, not #1: the disintermediation trap is live and present-tense. IDC Q1 2026 has Nvidia leading datacenter Ethernet (21.5% vs Arista 20.7%), Spectrum-X bundles networking into the GPU sale, and Arista has no scale-up answer until trials in 2027/production 2028. Microsoft and Meta each exceed 10% of revenue.

**3. MSFT —** The largest backlog in the set by an order of magnitude: commercial RPO \$677B (+73% YoY), ~2.3-year duration, plus an incremental \$250B OpenAI Azure commitment and up to \$49B from Anthropic after the quarter — while CFO Hood stated demand "continues to exceed our available supply" for Azure (+48%). The bearish nuance the panel weighed: RPO is flat sequentially, capex runs ~\$170B for calendar 2026, and OpenAI is ~11% of total revenue while multi-sourcing to five clouds. At ~\$3.6T, explosive upside is structurally capped — a compounder with a shortage kicker.

**4. CBOE —** The strongest shortage-framework fit outside AI hardware: a contractual monopoly on the benchmark equity derivative (SPX options), with record Q3 volumes — index options ADV +24% to 6.1M contracts, SPX 0DTE ADV a record 3.2M (+34%), 65% of all SPX activity — and the moat just re-locked for a generation (25-year S&P DJI exclusive license through 2051, signed Sep 29, 2026). It rose +2.21% on Nov 24 while the AI names fell ~5%. The flag: it already trades **above** its \$360.27 analyst mean target (−0.6% upside), and the 0DTE boom is both the driver and the regulatory risk.

**5. LLY —** The purest shortage story has become a market-share story: the FDA declared the tirzepatide shortage resolved Dec 19, 2024, and Q3 2026 was volume +53% / price −15%. What remains is dominance: ~6 in 10 US branded GLP-1 prescriptions, Q3 revenue \$24.4B (+39%), Mounjaro \$10.7B (+65%), Zepbound \$5.35B (+49%), guidance raised three times to \$91–92B, and retatrutide (up to 22.6% weight loss, beat Ozempic head-to-head) with a BLA planned Q1 2027. The honest caveat: incretins are ~66% of revenue and the oral (Foundayo) trails Novo's Wegovy pill.

**6. WST —** The closest thing to a real shortage outside AI: GLP-1 elastomers now 12% of sales, HVP Components \$466.7M (+19.7% YoY, 53% of sales), 375+ Annex 1 upgrade projects, and HVP capacity tight in Germany with new finishing capacity taking 18–24 months. Q3 adj. EPS +35.7% with guidance raised. The discount: no disclosed backlog, the RECEIVABLES_OUTRUN flag (AR +30.3% vs 9M sales +14.2%; mostly timing/mix per the dossier, but OCF trails net income), and 38.4x forward after +55.4% in 12 months.

**7. VRSN —** The best moat in the batch and the weakest explosive-return setup: sole .com registry (contract to Nov 2030), record 13.1M new registrations in Q3, domain base +6.1%, and the first of four contractual +7% annual price hikes took effect Nov 1. But revenue is only +5.7% and net income flat YoY; EPS missed (\$2.35 vs \$2.46); renewal rate slipped to 74.3% vs 75.4%. The RECEIVABLES_OUTRUN flag is benign (AR \$9.6M is 0.7% of revenue in a prepaid model with \$1.46B deferred revenue).

**8. MA —** A superb duopoly toll road (37.7% of combined Visa/Mastercard purchase volume, but earns 37.75 bp per dollar vs Visa's 29.01 bp) with the fastest-growing services engine (+19% YoY, ~41% of revenue) and a credible answer to the stablecoin threat (BVNK acquisition closed Aug 3, 2026). Q3 net revenue +14%, adj. EPS +21%. No shortage, and after a +47% swing off the June low the explosive move may already have happened.

**9. UNP —** The best-run railroad in North America (lowest operating ratio 59.8%) with record Q3 volumes — domestic intermodal a fifth straight record quarter — and a potential transformational merger. But the explosive case is the \$85bn Norfolk Southern deal, an STB coin flip with a decision deadline of Aug 28, 2027, and intermodal is low revenue per unit (\$1,586 vs \$4,136 industrial).

**10. VRTX —** A CF monopoly on a fixed patient pool (irreplaceability 10/10), but no demand surge: the near-term leg is the povetacicept PDUFA on Nov 30, 2026 — five days after this run — a binary event, not a shortage. Alyftrek \$706M (+186% YoY) is converting Trikafta patients onto a once-daily successor. The INVENTORY_BUILD flag is benign: 83% of the build is Crinetics purchase accounting. Earnings are flat while spending explodes (non-GAAP R&D/SG&A \$1.53B vs \$1.28B a year earlier).

## Just-missed names

- **IDXX (3 Borda, 2/4 appearances)** — #1 vet diagnostics (~59–70% share), Q3 +10% organic with guidance raised, InVue Dx installed base nearly 11,000; kept out by 40.7x forward PE for ~10% growth, the worst growth-per-multiple in the batch.
- **VEEV (3 Borda, 2/4 appearances)** — #1 life-sciences CRM (~80% share), forced Vault CRM migration wave, TAM raised to \$30B; kept out by zero shortage and ~15% growth, with Q3 FY2027 due Dec 3.
- **EW (1 Borda, 1/4 appearances)** — #1 TAVR (~66% global share), TMTT +45.6%, moderate-AS label + CMS NCD; kept out because the benefit is "gradual" by management's own words and TAVR share gains are moderating.
- **EOG (0 Borda, 0/4 appearances)** — best-in-class low-cost shale operator with a great Q3 (EPS \$4.87 beat, record production); unanimously left out because the IEA just flipped Q4 2026 to a ~1.7 mb/d surplus and EOG is a price-taker with irreplaceability 3/10.

## What the panel revealed

- **Agreement:** three of four lenses picked the same single pick (APH) and the same runner-up (ANET); all four ranked APH, ANET, MSFT and CBOE in their top 5, and LLY and WST in every top 10. The top 4 are separated by a single Borda point (33/33/33/32) — the tightest top of the recent window.
- **Disagreement:** the moat lens (C) dissented on the pick — CBOE over APH — because it ranks moat durability ahead of raw growth and rates APH a multi-sourced component (irreplaceability 6/10, #8 on its ballot) while CBOE is a legal monopoly to 2051. C also demoted ANET to #3 for the live Nvidia threat. The skeptic (D) demoted ANET to #4 for the same reason plus consensus pricing.
- **Conviction vs consensus:** APH is both conviction (three #1 votes) and consensus (never below #8, ranked #1 by three lenses). ANET and MSFT are pure consensus (never #1, never below #3). CBOE is the contested name: #1 on the moat ballot, #4–#5 on the others.
- **The Nov 23–24 AI selloff is the entry, not the thesis:** ANET −11.6% on Nov 20 and −5.47% on Nov 24; APH −5.09% on Nov 24 — while MSFT (+0.74%) and CBOE (+2.21%) rose. The panel bought the dislocation on APH/ANET, not the selloff itself.

## If forced to ONE

**APH.** The strict trap-veto lands on the same name as the Borda #1 after the tie-break: APH's disintermediation risk is low-to-medium (hyperscalers cannot in-source precision connectors; optical substitution is a 2029+ problem), while ANET — the only name with a deeper shortage score — fails the strict veto test on the live Nvidia lead in datacenter Ethernet. The Borda #1 and the forced single pick agree this run.

## Return scenarios — top 3

All numbers are research scenarios, not guarantees. Prices are the verified Tue Nov 24, 2026 closes. Anchor: analyst mean targets in `shortlist_2026-11-25.json`.

| Ticker | Price | Bear / by | Base / by | Bull / by | Probabilities | EV | EV upside |
|---|---|---|---|---|---|---|---|
| APH | \$73.47 | \$52 (-29.2%) / 2027-Q2 | \$100 (+36.1%) / 2027-Q2 | \$125 (+70.1%) / 2027-Q2 | 25 / 50 / 25 — base-weighted: the order book converts on contract; bear raised to 25% on the guided Q4 moderation | \$94.25 | +28.3% |
| ANET | \$168.56 | \$115 (-31.8%) / 2027-Q2 | \$225 (+33.5%) / 2027-Q2 | \$270 (+60.2%) / 2027-Q2 | 25 / 50 / 25 — base-weighted: FY27 guide is pre-committed; bear is the Nvidia share-loss case | \$208.75 | +23.9% |
| MSFT | \$496.13 | \$400 (-19.4%) / 2027-Q2 | \$600 (+20.9%) / 2027-Q2 | \$680 (+37.1%) / 2027-Q2 | 20 / 55 / 25 — base-weighted: RPO converts over 2.3 years; bear is the capex-returns disappointment | \$580.00 | +16.9% |

**Market-implied scenario:** all three prices sit below their base cases — APH closest to bear, ANET and MSFT between bear and base. None trades at its bull case. **Flag:** CBOE (#4) trades **above** its analyst mean target (\$362.52 vs \$360.27, −0.6% upside) — the only top-10 name above target. All three top-3 names clear the +15% EV guardrail (MSFT narrowly, at +16.9%).

## What was verified

Phase 3.5 verification (`parts/2026-11-25/verification.md`): **10 of 12 claims CONFIRMED; 1 contradicted, 1 unverified — both corrected before this writeup.**

- APH orders \$12.17B (+99% YoY), book-to-bill 1.19 — CONFIRMED (Q3 2026 call, Oct 28, 2026).
- APH IT Datacom growth rates — CONTRADICTED as stated: total IT Datacom grew **+117% YoY (+77% organic)**, not +100%; the +117% belongs to the whole segment, not AI-only. Corrected in the dossier and in both final files.
- APH "cable lead times toward a year / manufacturer sold out through 2026" — UNVERIFIED: connector lead times found are 8–12 weeks; the sold-out quotes belong to hard drives and HBM. Dropped from the thesis.
- APH mean target \$106.97, forward PE 21.4 — CONFIRMED (oppstock, Nov 24, 2026; other aggregators \$106.21–\$107.61 / 20.2–20.4x).
- ANET Q3 revenue \$3.66B (+58.5%), EPS \$1.20 vs \$1.08; purchase commitments \$11.4B; FY2027 guide ~\$18.5B (+38–40%), AI fabrics ~\$7B; IDC Q1 2026 Nvidia 21.5% vs Arista 20.7% — all CONFIRMED.
- MSFT RPO \$677B (+73% YoY); Hood demand-exceeds-supply + Azure +48%; OpenAI incremental \$250B Azure commitment — all CONFIRMED.
- Nov 24 closes APH \$73.47, ANET \$168.56, MSFT \$496.13, CBOE \$362.52 — CONFIRMED (Finnhub).

## Risk lens & leverage-safety note

Sector concentration: the top 3 are all Information Technology and all three are AI-capex-linked — a single hyperscaler spending pause hits the whole top of the list at once. The highest-risk names are ANET (single-architecture bet, Nvidia threat, customer concentration) and APH (cyclical connector order book, net debt \$12.6B); the steadiest are CBOE (monopoly volumes, net cash) and VRSN (contractual price hikes, prepaid model). Drawdown reality: high-beta cyclicals like memory/interconnect can fall 50%+ fast in a capex pause — the Nov 23–24 selloff took ~5% a day off ANET/APH. This is risk education, not advice: no specific leverage multiple or position size is suggested, and the system is cash-only.

## Thesis-break / trap triggers to watch across the ranked names

- APH: book-to-bill below 1.0 for a quarter; IT Datacom sequential growth negative for two quarters; a top hyperscaler dual-sourcing away.
- ANET: Nvidia datacenter Ethernet share widening past ~25%; a scale-up trial slip past 2027; Microsoft/Meta capex pause.
- MSFT: RPO declining sequentially for two quarters; OpenAI funding stress; Azure growth below 40%.
- CBOE: regulatory curb on 0DTE; SPX volumes falling with a volatility collapse.
- LLY: retatrutide BLA delay past Q1 2027; realized price falling faster than volume grows.
- WST: DSO still rising at the Q4 print; a top-10 customer loss.
- VRTX: Nov 30 PDUFA rejection or delay.
- UNP: STB rejecting the NS merger or imposing gutting concessions.
- EOG (not ranked): WTI below \$60 — the surplus thesis confirmed.

*This is research output, not financial advice. All scenario numbers are research estimates, not guarantees. Run date 2026-11-25.*
