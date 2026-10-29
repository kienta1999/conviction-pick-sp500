> Run by: Muse Spark (muse-spark) — full panel

# Momentum triage — 2026-10-29

Screen: shortlist_2026-10-29.json, 50 candidates, generated 2026-10-29 08:30:12 (coordinator ran fetch + screen --mode momentum; fetch took ~12 min under Yahoo throttling but finished 503/503 on all five data types). Kept 13 of 50 for deep research.

Screen-data caveats (do not hide them): many prices in today's shortlist are identical to the 2026-10-28 shortlist to the cent (ANET $187.00, APH $78.21, CSCO $111.38, ABNB $168.82, AMP $492.85, CME $293.48, AMGN $447.95, AME $246.22, CSX $52.27, CTAS $214.80, ABBV $286.39, CL $92.17, BRO $67.55) — the ~1-day price cache had not expired for those names at fetch time, so those prices are still the 2026-10-27 close, while SNDK/MU/NVDA/NEM refreshed to the 2026-10-28 close. The panel ranks from this screen as generated; the staleness is a fetch-cache artifact, not a panel judgment.

Yesterday's top-10 names missing today (why.py, not guesses): LLY dropped at stage 1 (profitable) on NaN netIncomeToCommon/profitMargins — a data artifact on its earnings day, not a thesis change; VRTX dropped at the same stage on the same NaN artifact; META dropped at stage 5 (above 200d SMA) with dist_sma200 = -0.02979, i.e. it fell below its 200-day SMA — real price action. All three are outside the screened set and cannot be ranked today; the screen is not overridden.

SNDK reports today (2026-10-29); WST reports today (2026-10-29); APH already reported (next_earnings now None).

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | SNDK | 0.956 | KEEP | 10 | Purest NAND shortage play; AI SSD demand vs no new industry capacity; reports today 2026-10-29 |
| 2 | MU | 0.953 | KEEP | 10 | HBM shortage archetype; take-or-pay visibility, only ~3 HBM makers on earth |
| 3 | NEM | 0.804 | KEEP | 7 | World's largest gold miner; gold structural supply deficit + central-bank demand, miner margin leverage; borderline — commodity, not backlog |
| 4 | ANET | 0.767 | KEEP | 7 | AI datacenter networking leader, switching demand surge; reports 2026-11-03 |
| 5 | NVDA | 0.751 | KEEP | 9 | AI compute shortage, order visibility; HIGH_ACCRUALS/RECEIVABLES_OUTRUN flags to explain in research |
| 6 | CF | 0.709 | KEEP | 8 | Nitrogen shortage (Hormuz / gas), low-cost producer, tight global supply |
| 7 | EOG | 0.707 | DROP | 4 | Quality E&P but commodity-price beta, no distinct shortage/backlog mechanism — high composite, no doctrine |
| 8 | HAS | 0.696 | DROP | 2 | Leisure/toys momentum, no shortage or backlog thesis — high composite, no doctrine |
| 9 | BNY | 0.690 | DROP | 3 | Custody bank scale, no shortage; LOW_CASH_CONVERSION flag |
| 10 | STT | 0.683 | DROP | 3 | Custody bank like BNY, no shortage mechanism — high composite, no doctrine |
| 11 | FANG | 0.674 | KEEP | 6 | Permian E&P with strong margins; weakest kept name — energy supply discipline, borderline |
| 12 | V | 0.671 | DROP | 5 | Irreplaceable payments network but no shortage/surge; borderline — dropped for supplier-shortage names |
| 13 | APH | 0.664 | KEEP | 8 | AI interconnect shortage; +33.5% rev growth, datacenter demand; reported 2026-10-28 |
| 14 | AAPL | 0.663 | DROP | 4 | Mega-cap hardware at -5.1% analyst upside, no shortage thesis |
| 15 | MA | 0.646 | DROP | 5 | Same as V — durable network, no surge/backlog; reports today |
| 16 | DVN | 0.642 | DROP | 4 | E&P duplicate of FANG/EOG, commodity beta |
| 17 | OXY | 0.636 | DROP | 4 | E&P commodity beta, no distinct doctrine edge over FANG |
| 18 | CBOE | 0.600 | DROP | 4 | Exchange moat, ~zero analyst upside, no shortage |
| 19 | COP | 0.593 | DROP | 4 | E&P commodity beta |
| 20 | CSCO | 0.592 | KEEP | 6 | AI networking orders / infrastructure refresh; second networking name behind ANET; INVENTORY_BUILD flag to explain |
| 21 | EXPE | 0.582 | DROP | 3 | Travel platform, no shortage/backlog |
| 22 | UNP | 0.575 | DROP | 3 | Rail duopoly, no surge |
| 23 | ABNB | 0.557 | DROP | 3 | Travel platform, no shortage |
| 24 | AMP | 0.551 | DROP | 3 | Wealth manager, no doctrine fit |
| 25 | FAST | 0.549 | DROP | 4 | Industrial distributor, no structural shortage/backlog angle |
| 26 | ISRG | 0.546 | KEEP | 8 | Surgical robotics installed-base lock-in, razor/blade, certification moat |
| 27 | WST | 0.536 | KEEP | 6 | Pharma packaging / GLP-1 fill-finish capacity, qualified-supplier lock-in; reports today 2026-10-29 |
| 28 | VRSN | 0.504 | DROP | 4 | .com registry monopoly but low growth, no surge; RECEIVABLES_OUTRUN flag |
| 29 | CME | 0.499 | DROP | 4 | Exchange moat, no shortage; RECEIVABLES_OUTRUN flag |
| 30 | AMGN | 0.496 | DROP | 3 | Below analyst mean target (-11.3% upside), pipeline binary, no shortage |
| 31 | JPM | 0.496 | DROP | 3 | Bank scale, no shortage; LOW_CASH_CONVERSION/RECEIVABLES_OUTRUN flags |
| 32 | PM | 0.496 | DROP | 3 | Nicotine-pouch growth but no explosive shortage |
| 33 | RL | 0.487 | DROP | 2 | Apparel brand momentum, no doctrine fit |
| 34 | VEEV | 0.485 | DROP | 4 | SaaS moat, above analyst target, no shortage |
| 35 | PAYX | 0.482 | DROP | 2 | Payroll compounder, no shortage; RECEIVABLES_OUTRUN flag |
| 36 | EBAY | 0.476 | DROP | 2 | Marketplace, negative upside, no surge |
| 37 | AME | 0.470 | KEEP | 6 | Niche #1 test/process instruments, record backlog in prior runs, pricing power |
| 38 | EW | 0.470 | DROP | 5 | Structural-heart leader but slower, borderline — dropped for ISRG/WST medtech overlap |
| 39 | BRO | 0.465 | DROP | 2 | Insurance brokerage roll-up, no shortage; RECEIVABLES_OUTRUN flag |
| 40 | CSX | 0.457 | DROP | 3 | Rail, no surge |
| 41 | JNJ | 0.452 | DROP | 3 | Diversified pharma, no single shortage driver |
| 42 | SPGI | 0.447 | DROP | 4 | Ratings oligopoly, no shortage surge |
| 43 | CTAS | 0.444 | DROP | 3 | Route moat, above target, no surge |
| 44 | ABBV | 0.443 | DROP | 4 | Immunology leader but at target, no shortage |
| 45 | FCX | 0.442 | KEEP | 9 | Copper structural deficit, Grasberg scale — lowest kept composite because screen rev growth reflects Grasberg disruption, which is itself the supply shortage; INVENTORY_BUILD flag to explain |
| 46 | ROK | 0.418 | DROP | 5 | Automation leader, reshoring tailwind, but no shortage/backlog thesis as strong as AME; borderline |
| 47 | ITW | 0.390 | DROP | 3 | Diversified industrial, no shortage driver |
| 48 | NSC | 0.390 | DROP | 3 | Rail, no surge |
| 49 | CL | 0.385 | DROP | 3 | Staples compounder, no shortage/surge |
| 50 | BR | 0.359 | DROP | 4 | Fintech infrastructure compounder, no shortage/surge |

Kept (13): SNDK, MU, NEM, ANET, NVDA, CF, FANG, APH, CSCO, ISRG, WST, AME, FCX.
Borderline flagged: NEM (commodity, not backlog), FANG (weakest keep, energy beta), ROK/EW/V (dropped but genuine moats without a surge).
High-composite drops explained: EOG, HAS, BNY, STT all rank top-10 on composite but lack any shortage/backlog/disintermediation-resistance mechanism.
Earnings-quality flags in kept set: NVDA (HIGH_ACCRUALS, RECEIVABLES_OUTRUN), CSCO (INVENTORY_BUILD), FCX (INVENTORY_BUILD) — research briefs must explain each.
