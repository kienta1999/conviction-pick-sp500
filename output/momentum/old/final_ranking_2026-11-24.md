> Run by: Muse Spark 1.3 — full panel

# Final ranking — stock-pick-momentum, run 2026-11-24

## OFFICIAL PICK — consensus top 3

Consensus top 3 (5 runs, 2026-11-20 → 2026-11-24, `output/momentum/consensus_2026-11-24.md`): **MSFT (43 pts), WST (38), EW (22)**. The consensus only moves when several panels agree — MSFT has been top 10 in 5/5 runs and top 3 in 4/5. Today's Borda #1 is APH (consensus #6, 20 pts, top 10 in only 2/5 runs) and today's single pick is also APH — today's view and the consensus differ: the panel moved to APH on the new screen (ANET is the new composite #1, MSI fell out of the screen entirely at stage 6 on operating margin), while the consensus still anchors on MSFT/WST/EW. The screen-only top 3 (composite rank, no AI) is ANET, LLY, EOG.

Note on prices: the screen's `currentPrice` is the Fri Nov 20 close; its `targetMeanPrice` / `analyst_upside` are Nov 23-based. Prices in this writeup are the **verified Mon Nov 23 closes** — APH \$77.41, WST \$399.30, LLY \$1,364.60 (verified by Phase 3.5 / Finnhub) and, for the rest, implied from the screen's own target/upside (target / (1 + upside)), which reproduces the verified closes exactly. The screen's Nov 20 prices would overstate upside by up to ~11 points and are not used.

## The ranking (today's Borda)

Four lenses, one round (R = 1). Borda: rank 1 = 10 pts … rank 10 = 1, unranked = 0.

| Rank | Ticker | Company | Sector | Price | Analyst mean target | Fwd PE | Shortage | Irreplace. | Borda | Appear. | #1 | Avg place | One-line case |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | APH | Amphenol | Information Technology | \$77.41 | \$106.97 (+38.2%) | 21.4 | 9/10 | 8/10 | 40 | 4/4 | 4 | 1.00 | Orders > shipments 4 quarters; only a handful can build qualified 224G interconnect |
| 2 | WST | West Pharmaceutical Services | Health Care | \$399.30 | \$471.00 (+18.0%) | 38.4 | 7/10 | 8/10 | 36 | 4/4 | 0 | 2.00 | GLP-1 elastomer bottleneck, pricing power, 18–24 month capacity wall |
| 3 | LLY | Eli Lilly | Health Care | \$1,364.60 | \$1,470.06 (+7.7%) | 26.8 | 5/10 | 7/10 | 24 | 4/4 | 0 | 4.00 | Shortage over; #1 GLP-1, retatrutide filing Q1 2027 |
| 4 | MSFT | Microsoft | Information Technology | \$492.35 | \$636.12 (+29.2%) | 20.4 | 7/10 | 6/10 | 20 | 4/4 | 0 | 6.00 | \$677bn RPO, Azure demand exceeds supply; RPO flat, capex ~\$170bn |
| 5 | VEEV | Veeva Systems | Health Care | \$268.65 | \$325.87 (+21.3%) | 26.2 | 4/10 | 8/10 | 20 | 4/4 | 0 | 6.00 | Forced Vault CRM migration; -17.6% off high, Dec 3 earnings |
| 6 | UNP | Union Pacific | Industrials | \$288.94 | \$329.96 (+14.2%) | 20.1 | 5/10 | 7/10 | 18 | 4/4 | 0 | 6.50 | Intermodal capacity crunch; NS merger, STB ~Aug 2027 |
| 7 | ANET | Arista Networks | Information Technology | \$178.32 | \$249.65 (+40.0%) | 29.5 | 7/10 | 5/10 | 16 | 2/4 | 0 | 3.00 | AI networking +58.5% Q3; NVIDIA now leads, rents Broadcom silicon |
| 8 | VRTX | Vertex Pharmaceuticals | Health Care | \$538.26 | \$595.36 (+10.6%) | 27.0 | 3/10 | 9/10 | 14 | 4/4 | 0 | 7.50 | CF monopoly; povetacicept PDUFA 30 Nov 2026 |
| 9 | CBOE | Cboe Global Markets | Financials | \$354.60 | \$360.27 (+1.6%) | 22.8 | 3/10 | 10/10 | 14 | 3/4 | 0 | 6.33 | 25-year SPX monopoly to 2051; no shortage |
| 10 | VRSN | Verisign | Information Technology | \$313.86 | \$339.60 (+8.2%) | 28.6 | 2/10 | 10/10 | 9 | 3/4 | 0 | 6.67 | Sole .com registry; ~6% growth at 28.6x |

Tie-breaks: MSFT vs VEEV at 20 Borda — MSFT 4th on the doctrine (shortage 7/10 vs 4/10; both avg place 6.00, no #1 votes). VRTX vs CBOE at 14 — VRTX 8th (4/4 appearances vs 3/4, and the fresher catalyst: PDUFA in 6 days). EW scored 8 Borda (3/4 appearances) and is the just-missed name.

## Per-name thesis

**1. APH —** The only name satisfying all three doctrine legs: #1 interconnect globally, a genuine physical bottleneck at 224G (record Q3 orders \$12.17B, +99% YoY; book-to-bill 1.19:1, fourth straight quarter above 1.0; backlog +\$1.94B in the quarter; lead times >12 weeks), and a moat of signal-integrity process knowledge plus rack-level qualification that hyperscalers cannot in-source (irreplaceability 8/10). Verification softened one claim: four firms, not three, were in the first 224G certification batch (Amphenol, Molex, TE, Samtec) plus Chinese vendors in volume supply — a handful, not a trio. At 21.4x forward with +38.2% analyst upside, it is the cheapest of the AI shortage names. Unanimous single pick, 8/10 conviction on all four ballots.

**2. WST —** The only other genuine shortage in the set: HVP Components \$466.7m, +20.3% organically in Q3, GLP-1-linked HVP growing "well into the 30s%", pricing contributing just over 4 points of growth (above the 2–3% planning assumption), and new finishing capacity taking 18–24 months to come online. The moat is FDA/EMA qualification lock-in — a stopper is specified into the drug's approved filing. The discount: +55.4% in 12 months at 38.4x forward, and the RECEIVABLES_OUTRUN flag (receivables +30.3% vs 9M sales +14.2%) is mostly benign timing but unresolved until the Feb 2027 Q4 print.

**3. LLY —** The purest shortage story has become a market-share story: the FDA declared the tirzepatide shortage ended Dec 19, 2024 (semaglutide followed Feb 21, 2025 — corrected from the dossier's Dec 2024), and there is currently no Zepbound shortage. What remains is dominance: ~6 in 10 US obesity incretin prescriptions, Q3 revenue \$24.4B (+39%), Mounjaro \$10.7B (+65%), Zepbound \$5.35B (+49%), guidance raised three times to \$91–92B, and retatrutide beating semaglutide head-to-head (TRANSCEND-T2D-2: 20.9% vs 9.4% weight loss) with filing planned Q1 2027. The honest caveat: US realised price already −10% in Q3, and two drugs are ~66% of revenue.

**4. MSFT —** The largest backlog in the set by an order of magnitude: commercial RPO \$677bn (+73% YoY), with CFO Hood stating "customer demand continues to exceed our available supply" for Azure AI capacity, Azure +48% to \$33.2B. The bearish nuance the panel weighed: RPO is flat sequentially (\$678bn in Jun 2026), bookings fell 12% YoY, and capex runs ~\$170B for calendar 2026 while FCF fell 27%. The trap is the doctrine's own: OpenAI is ~45% of the Dec 2025 RPO and is diversifying compute to AWS.

**5. VEEV —** No physical shortage, but a forced, dated migration wave: support for the Salesforce-based CRM ends Dec 2029, 14 of the top 20 biopharma have committed to Vault CRM, >200 customers live, and the TAM was raised to \$30bn at the Nov 5 Investor Day (largely on industry-specific AI). The stock is −17.6% off its Oct 22 high despite the Investor Day — the market is discounting the story, not chasing it. Next earnings Dec 3 is the nearest catalyst in the set. The moat is GxP-validated workflow lock-in (8/10), but Salesforce+IQVIA is a credible, well-funded #2 already winning some of the largest accounts.

**6. UNP —** A real, quotable capacity crunch: intermodal volumes +11% to 956,000 carloads in Q3, domestic intermodal a fifth straight record quarter, UP rationing container reservations in CA/TX/Chicago/SLC with priority to contract customers, driven by diesel +70% YoY and a re-emerged truck-driver shortage. But it is a fuel/trucking cycle, not a structural shortage, and the upside is hostage to the \$85bn Norfolk Southern merger — STB final decision expected late Aug 2027.

**7. ANET —** The fastest revenue acceleration on paper (Q3 \$3.66B, +58.5% YoY; 2027 outlook ~\$18.5B, +38–40%; purchase commitments \$11.4B) — but the panel split on it: ranked 3rd by the supply-chain and growth lenses, left out entirely by the moat and skeptic lenses. The disintermediation trap is live: NVIDIA now leads datacenter Ethernet (21.5% vs Arista 20.7% in 1Q26 per IDC), Spectrum-X bundles networking into the GPU sale, and Arista rents its silicon from Broadcom (gross margin 65.6% → 63.4% YoY). Irreplaceability 5/10 — the lowest of the top 7.

**8. VRTX —** A CF monopoly on a fixed patient pool (irreplaceability 9/10), but no demand surge: the near-term leg is the povetacicept PDUFA on 30 Nov 2026, a binary event, not a shortage. Alyftrek \$706m (+186% YoY) is converting Trikafta patients onto a once-daily successor. The INVENTORY_BUILD flag is benign: 83% of the build is Crinetics purchase accounting, and 9M operating cash flow (\$3.20bn) exceeds net income (\$2.78bn).

**9. CBOE —** A superb, now-25-year monopoly franchise (exclusive SPX licence through 2051, signed Sep 29, 2026) with surging 0DTE volumes (65% of SPX volume) — but there is no supply shortage to explode on; it is a high-teens compounder miscast as a shortage bet, with only +1.6% analyst upside after a +39.9% 12-month run.

**10. VRSN —** The best moat in the batch and the worst explosive-return setup: sole .com registry (contract to Nov 2030), record 13.1m new registrations, guidance raised a third straight time, .com price \$10.26 → \$10.97 (Nov 1) — but only ~6% growth at 28.6x forward PE. Renewal rate slipped to 74.3% vs 75.4%, and a Sep 2026 antitrust suit alleges monopoly pricing.

## Just-missed names

- **EW (8 Borda, 3/4 appearances)** — #1 TAVR (65.7% US share) with a new-indication runway (asymptomatic + CMS NCD Sep 11, 2026; TMTT +45.6% to \$207m); a 10–12% compounder whose next test is the Dec 4 investor conference, not a shortage bet.
- **MA (1 Borda)** — the better of the two networks on momentum (EPS +21%, share gains ex-US, bigger services mix), but still a low-teens compounder with the same stablecoin/A2A bypass threat as Visa.
- **V (0 Borda)** — #1 network, VAS +31%, but no shortage, FY27 guide decelerates, and the bypass threat is the first credible one to the core toll in decades.

## What the panel revealed

- **Agreement:** all four lenses picked the same single pick (APH) and the same runner-up (WST) — the first unanimous momentum pick in the recent window. All four ranked APH #1, WST #2, and LLY, MSFT, VEEV, UNP, VRTX in their top 10.
- **Disagreement:** ANET is the whole story — ranked 3rd by the supply-chain and growth lenses, left out entirely by the moat lens (veto: rents Broadcom silicon, NVIDIA now leads) and the skeptic lens. That 16-point swing is the difference between ANET at #7 and a top-3 finish. The moat lens also ranked CBOE and VRSN 4th/5th (moat-first), while the growth lens left both out entirely.
- **Conviction vs consensus:** APH is both conviction (four #1 votes) and consensus (never below 1st). WST is pure consensus (#2 on every ballot, never #1). ANET is the contested name: high ceiling, live trap.
- **Strict-doctrine order vs Borda order:** the strict order (trap applied as a veto) would drop ANET out of the top 10 entirely and put VEEV/UNP higher; the Borda order keeps ANET at #7 because the trap is a flag in ranked mode, not a veto.

## If forced to ONE

The single pick the strict trap-veto would land on is **APH** — the same as the Borda #1. ANET is vetoed (Broadcom silicon dependence, NVIDIA leading its core segment), MSFT is flagged (OpenAI concentration, flat RPO), and WST survives the trap but is docked on valuation (+55.4% in 12 months at 38.4x) and the unresolved receivables flag. Today's single pick (APH) and the strict-doctrine view agree; there is no Borda-vs-doctrine split this run.

## Return scenarios — top 3

All numbers are research scenarios, not guarantees. Prices are the Mon Nov 23, 2026 close.

| Ticker | Bear | Base | Bull | Probabilities (bear/base/bull) | EV | EV upside |
|---|---|---|---|---|---|---|
| APH (\$77.41) | \$62 (-19.9%) by 2027-Q2 | \$107 (+38.2%) by 2027-Q3 | \$125 (+61.5%) by 2027-Q4 | 20% / 55% / 25% | \$102.50 | +32.4% |
| WST (\$399.30) | \$320 (-19.9%) by 2027-Q2 | \$471 (+18.0%) by 2027-Q3 | \$540 (+35.2%) by 2027-Q4 | 25% / 50% / 25% | \$450.50 | +12.8% |
| LLY (\$1,364.60) | \$1,080 (-20.9%) by 2027-Q2 | \$1,620 (+18.7%) by 2027-Q3 | \$1,950 (+42.9%) by 2027-Q4 | 20% / 50% / 30% | \$1,611.00 | +18.0% |

- **APH:** probabilities as in the final pick (20/55/25). Market price sits closest to base — below the \$106.97 mean target, with the market pricing capex doubt rather than the order book.
- **WST:** ⚠️ EV upside +12.8% is BELOW the +15% guardrail — it stays in the ranking (the guardrail only blocks actionable single picks), but the reader should see it: the shortage is real and the moat is the deepest in the batch after the monopolies, yet +55.4% in 12 months at 38.4x forward has already paid for most of it. Probabilities weighted to base (50%) with a fatter bear (25%) for the receivables flag and oral-GLP-1 bypass risk.
- **LLY:** probabilities 20/50/30 — the base is volume growth offsetting price erosion; the bull needs retatrutide to file in Q1 2027 as planned and the oral pill to open the injection-reluctant market. Market price sits closest to base — \$1,364.60 is below the \$1,470.06 mean target, and the +7.7% analyst upside is the smallest in the top 3.

## What was verified

Phase 3.5 verification (`parts/2026-11-24/verification.md`): 7 of 9 claims CONFIRMED — APH's \$12.17B orders, 1.19:1 book-to-bill and Q3 sales/guide; WST's HVP figures, 18–24-month capacity wall and Q3 beat/raise; LLY's Q3 revenue and drug sales. Two CONTRADICTED in part and corrected in the writeups: the 224G supplier set is four firms in the first certification batch (Amphenol, Molex, TE, Samtec) plus Chinese vendors in volume supply, not "only ~3 firms"; semaglutide's shortage was resolved Feb 21, 2025, not Dec 2024; and the dossier's "22.6% in TRIUMPH-1" retatrutide figure matches no published number and is dropped (actual: TRANSCEND-T2D-2, 20.9% vs 9.4% at 80 weeks). The verifier also found the screen's prices are the Fri Nov 20 close — APH closed \$77.41 on Nov 23, WST \$399.30, LLY \$1,364.60 — and all scenario math here uses the Nov 23 closes. No thesis-bearing claim failed.

## Risk lens & leverage-safety note

Sector concentration: the top 3 are all exposed to the same AI-infrastructure / GLP-1 demand cycle from different angles (APH and MSFT are AI-capex-linked; LLY and WST are the GLP-1 pair, WST literally selling into LLY's pens). The three oil names scored zero between them again — the panel refused to treat a fading war premium as a shortage. Highest-risk names: ANET (live disintermediation trap), MSFT (OpenAI concentration, ~\$170bn capex), VRTX (binary PDUFA 30 Nov), WST (38.4x forward, unresolved receivables flag). Steadiest compounders: CBOE and VRSN (monopolies, no shortage), V and MA (network tolls). Drawdown reality: the momentum names are cyclicals at high multiples — a high-beta name can draw down 50%+ fast, which is brutal with margin. This system is cash-only per POLICY.md §2; the leverage discussion here is risk education, not a recommendation, and no specific leverage multiple or position size is suggested.

## Thesis-break / trap triggers to watch

- APH: book-to-bill below 1.0 for a quarter; backlog shrinking; IT Datacom sequential growth turning negative; a top hyperscaler materially dual-sourcing away.
- WST: Q4 DSO not normalising (receivables flag becomes real); oral GLP-1s cutting pen volumes; HVP growth falling below ~15%.
- LLY: realised prices falling a second straight quarter by double digits; retatrutide filing slipping past Q1 2027.
- MSFT: OpenAI shifting material compute to AWS; Azure growth decelerating below ~40%; RPO shrinking sequentially.
- ANET: NVIDIA share gains widening in datacenter Ethernet; Broadcom raising silicon prices further.
- VRTX: povetacicept CRL on Nov 30.
- UNP: STB rejecting or heavily conditioning the NS merger.

*This is research output, not financial advice. All prices are the Mon Nov 23, 2026 close; all scenario numbers are research estimates, not guarantees. Run date 2026-11-24.*
