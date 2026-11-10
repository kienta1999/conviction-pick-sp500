> Run by: Muse Spark (muse-spark) — full panel

# Triage — momentum 2026-11-10

Shortlist: `output/momentum/shortlist_2026-11-10.json`, generated 2026-11-10 16:41:03 UTC, 50 candidates, fresh (fetch took ~20 min on Yahoo throttling; prices ok=503/503). Triage criteria per stock-pick-momentum SKILL.md: shortage potential, backlog/order-book visibility, category dominance, irreplaceability / disintermediation risk. Kept 15 of 50.

**PRICE FIELD WARNING — read before using this screen:** the JSON carries two price fields and they diverge today. `price` is the fresh 2026-11-09 close from the refreshed price cache; `currentPrice` is a STALE info-cache value (2026-11-06 close). Yesterday both fields were identical; today they are not. All prices in this file, the dossier, ballots and ledger use the `price` field. The gaps are large where the market moved on 2026-11-09: ANET $188.26 vs stale $170.80 (+10.2% on 11-09, post-Q3-print bounce), NUE $257.49 vs $244.97 (+5.1%), MSI $525.11 vs $514.51 (+2.1%), EOG $151.15 vs $147.13 (+2.7%), CF $121.14 vs $119.39 (+1.5%), CBOE $357.22 vs $353.27 (+1.1%), V $421.95 vs $422.65 (−0.2%), ISRG $445.04 vs $452.80 (−1.7%). `analyst_upside` in the JSON is computed off the fresh `price` field (verified: ANET 249.07/188.26 − 1 = +32.3%). The panel must judge "already priced" off the fresh price, not the stale one.

**Note vs yesterday (2026-11-09 run):** the screen turned over on data, not thesis. OXY (#9 yesterday) dropped at stage 5 — its 11-09 close slipped just below the 200d SMA (dist_sma200 = −0.0059) — a real price move, not a glitch; it cannot be ranked today (its Q3 printed after the close 11-09; the earnings-mode panel covers it). WST, EMR, MU, MSFT, LLY, WAB all dropped at stage 1 with `netIncomeToCommon=NaN` — the SAME Yahoo fundamentals-cache glitch as yesterday (WST/EMR/MU dropped the same way 11-09), still unrepaired; none can be ranked today. VLO dropped at stage 6 on operating margin exactly at the sector median (0.2047 = 0.2047) — a gate artifact. Two new names entered the field: META (composite #7) and CDNS (#22). Yesterday's #1 CBOE, #2 ANET, #3 MSI, #4 CF, #5 EW, #6 EOG, #7 NUE, #8 VRSN, #10 ISRG all survive; #9 OXY is out (see above).

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
| --- | --- | --- | --- | --- | --- |
| 1 | ANET | 0.884 | KEEP | 9 | AI-datacenter Ethernet, rev +36.3% TTM, Q3 +58.5%, 44.9% op margin, $11.4bn purchase commitments; +10.2% on 11-09 already — panel must weigh priced-in vs guide |
| 2 | ABNB | 0.812 | DROP | 3 | High composite dropped — no shortage thesis, irreplaceability ~3/10, +55% in 12m; yesterday only one lens ranked it (#5) |
| 3 | EOG | 0.791 | KEEP | 7 | Lowest-cost shale E&P, record production, Dorado gas; RECEIVABLES_OUTRUN flag to explain (recv div +21.6pts, CFO/NI 1.95x) |
| 4 | V | 0.733 | KEEP | 6 | #1 payments network, 63.7% op margins, irreplaceable rails; no shortage, moat score high |
| 5 | COP | 0.731 | KEEP | 7 | Largest US E&P (2.1x #2), +60% in 12m; commodity cycle, no moat beyond scale |
| 6 | CF | 0.720 | KEEP | 8 | Ammonia/nitrogen shortage, 97% utilisation, ~9m tons urea supply lost — war premium |
| 7 | META | 0.687 | KEEP | 6 | New to the field: +23.4% rev, +32.0% analyst upside, 18.1x fwd — cheapest mega-cap grower; shortage angle weak (it IS the hyperscaler), borderline |
| 8 | MNST | 0.678 | DROP | 2 | Energy drinks — strong growth but no shortage, no backlog, no moat |
| 9 | CBOE | 0.676 | KEEP | 7 | Sole SPX/VIX venue, licence locked through 2051; irreplaceable exchange moat; analyst target at the price (−0.5%) |
| 10 | BNY | 0.673 | DROP | 2 | Custody bank — no shortage thesis |
| 11 | NUE | 0.672 | KEEP | 8 | #1 US steel, +80.5% in 12m, tariffs + grid/datacenter steel demand; cyclical |
| 12 | STT | 0.664 | DROP | 2 | Custody bank — no shortage thesis; LOW_CASH_CONVERSION flag |
| 13 | AAPL | 0.654 | DROP | 3 | No shortage thesis; iPhone supply ample, trading above analyst target, fully priced |
| 14 | BLK | 0.623 | DROP | 3 | Asset manager — scale moat but no shortage/backlog |
| 15 | AMP | 0.610 | DROP | 2 | Asset manager/wealth — no shortage thesis, modest growth |
| 16 | UNP | 0.607 | DROP | 3 | Rail duopoly moat but no shortage; rev growth only +7.7%, net debt/EBITDA 2.1x |
| 17 | VRTX | 0.570 | KEEP | 5 | CF franchise near-monopoly; Nov 30 PDUFA binary (povetacicept); INVENTORY_BUILD flag to explain (inv div +26.2pts); borderline, 1 of 4 EPS beats |
| 18 | ISRG | 0.559 | KEEP | 7 | da Vinci record placements, installed-base annuity; first real competition now — moat test; −20.5% in 12m |
| 19 | EBAY | 0.554 | DROP | 2 | Marketplace, no shortage; RECEIVABLES_OUTRUN flag, sub-scale vs Amazon |
| 20 | ABBV | 0.553 | DROP | 3 | Pharma scale, Skyrizi/Rinvoq growth, but no shortage/backlog; high debt 2.2x EBITDA |
| 21 | EW | 0.525 | KEEP | 5 | TAVR heart-valve leader, procedure-pool expansion; borderline, no backlog, 30.3x forward |
| 22 | CDNS | 0.519 | KEEP | 7 | New to the field: EDA duopoly (with SNPS) — AI chip-design bottleneck, near-impossible to in-source; +23.4% analyst upside; RECEIVABLES_OUTRUN + INVENTORY_BUILD flags to explain |
| 23 | MCO | 0.515 | DROP | 3 | Ratings duopoly moat, no shortage; rev growth only +7.2% |
| 24 | VRSN | 0.493 | KEEP | 6 | Legal .com monopoly, 7% annual price rises, record registrations; RECEIVABLES_OUTRUN flag (recv div +185pts — explain, likely price-rise receivables timing) |
| 25 | AME | 0.488 | DROP | 4 | Industrial instruments leader, +20.8% analyst upside, but no clear shortage/backlog; weaker than CDNS on the same AI-infra angle |
| 26 | PAYX | 0.484 | DROP | 2 | Payroll/HR services — no shortage; RECEIVABLES_OUTRUN flag; reports Dec 18 |
| 27 | JPM | 0.483 | DROP | 2 | Largest bank, no shortage thesis; LOW_CASH_CONVERSION flag |
| 28 | MSI | 0.482 | KEEP | 9 | Record $16.6bn backlog, orders +25%, defence/drone kicker; INVENTORY_BUILD flag to explain (inv div +48.0pts); 0.5% below 52w high |
| 29 | IDXX | 0.482 | KEEP | 6 | Vet-diagnostics leader, 80% recurring revenue; 41.0x forward, fully priced risk |
| 30 | CME | 0.469 | DROP | 3 | Exchange moat but no shortage; CBOE kept as the stronger exchange name |
| 31 | VEEV | 0.454 | DROP | 3 | Life-sciences software leader, no shortage/backlog; reports Nov 25 |
| 32 | JNJ | 0.453 | DROP | 2 | Pharma conglomerate, no shortage; +54% in 12m is a re-rate, not a shortage |
| 33 | SPGI | 0.446 | DROP | 3 | Ratings/index duopoly moat, no shortage; flat 12m return |
| 34 | PH | 0.436 | DROP | 2 | Industrial conglomerate, no shortage thesis |
| 35 | CTAS | 0.434 | DROP | 2 | Uniform rental compounder, no shortage/backlog; reports Dec 17 |
| 36 | PKG | 0.410 | DROP | 2 | Packaging, no shortage thesis |
| 37 | NSC | 0.403 | DROP | 2 | Rail, same as UNP but weaker; no shortage |
| 38 | MO | 0.402 | DROP | 2 | Tobacco — no shortage; RECEIVABLES_OUTRUN flag, rev growth +2.2% |
| 39 | ITW | 0.390 | DROP | 2 | Industrial conglomerate, rev growth +3.9% — no shortage thesis |
| 40 | BRO | 0.384 | DROP | 2 | Insurance broker, negative 12m return — no shortage thesis |
| 41 | VRSK | 0.376 | DROP | 2 | Data/analytics, negative 12m return — no shortage thesis |
| 42 | HIG | 0.374 | DROP | 2 | Insurer, no shortage thesis |
| 43 | DOV | 0.371 | DROP | 2 | Industrial conglomerate, no shortage thesis |
| 44 | MMM | 0.341 | DROP | 2 | Industrial conglomerate, rev growth +1.4% — no shortage thesis |
| 45 | WSM | 0.337 | DROP | 2 | Home furnishings, no shortage; reports Nov 18 |
| 46 | PG | 0.336 | DROP | 2 | Consumer staples — no shortage thesis |
| 47 | KMB | 0.304 | DROP | 2 | Household products — no shortage thesis |
| 48 | EFX | 0.300 | DROP | 2 | Credit bureau, negative 12m return — no shortage thesis |
| 49 | RSG | 0.292 | DROP | 2 | Waste services, no shortage thesis |
| 50 | ROP | 0.273 | DROP | 2 | Industrial software roll-up, no shortage thesis |

Borderline keeps: META (hyperscaler, not supplier — weak shortage angle, kept on +32% analyst upside and 18x fwd), VRTX (1 of 4 EPS beats, INVENTORY_BUILD flag, binary not shortage), EW (no backlog, valuation). Borderline drops: ABNB (high composite 0.812 dropped — no shortage thesis, the doctrine's core test), AME (real leader, no shortage; CDNS covers the AI-infra angle better).

Research batches: 1) ANET, EOG, COP, CF; 2) V, META, CBOE, VRSN; 3) NUE, CDNS, VRTX, MSI; 4) ISRG, EW, IDXX.
