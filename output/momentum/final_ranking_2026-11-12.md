> Run by: Muse Spark (muse-spark-1.3) — full panel

## Consensus top 3 (official pick — 5-run consensus, see consensus_2026-11-12.md)

**CF, ANET, CBOE** — the consensus top 3 (in the top 10 in ≥ 4 of 5 runs, by Borda points: CF 37, ANET 30, CBOE 27; window 2026-11-08 → 2026-11-12). Difference vs today's Borda: consensus puts CF first, but CF is only today's #3; ANET is consensus #2 but only today's #8, and CBOE is consensus #3 but only today's #10 — while today's Borda #1 and single pick, MU, is only consensus #9 (top 10 in just 1 of 5 runs — it only entered the screen today) and today's #2 CDNS does not qualify (top 10 in only 3 of 5 runs, despite 29 points). The consensus is the slow-moving pick; today's MU #1 and the actionable verdict are today's view, not the system's.

# Momentum ranked top-10 — 2026-11-12

Shortlist: `output/momentum/shortlist_2026-11-12.json` (50 candidates, generated 2026-11-12 09:23:27 UTC). Triage kept 15; research in four batches; four-lens panel (A supply-chain, B growth/momentum, C quality/moat, D contrarian) each returned a single-pick ballot and a ranked top-10. Borda: rank 1 = 10 pts … rank 10 = 1 pt, summed across 4 ballots. Dossier: `output/momentum/research_dossier_2026-11-12.md`. Ballots: `output/momentum/parts/2026-11-12/ballot_{A,B,C,D}1.md`.

Note vs yesterday: the screen turned over on data, not thesis — 5 names entered (MU, OXY, EXPE, FOX, FOXA) and 5 left (VLO, META, DOV, HIG, VRSK). **MU enters the screen for the first time at composite #1 (0.972)** and wins the single-pick tally 6–3 over CF; yesterday's pick CDNS falls to screen #28 but repeats as Borda #2. Top-10 overlap vs yesterday: 8 of 10 (out: VLO, VRTX; in: MU, PH). The panel's single-pick tally is MU 6, CF 3, CDNS 2, ANET 1, and the adjudicated winner MU clears the +15% EV guardrail (+33.5%).

**Price note:** the screen ran pre-open (09:23 UTC = 01:23 PST), so its `price` field is effectively the 2026-11-11 close. The ledger's `price_at_pick` uses the screen price per protocol.

## The ranking

| Rank | Ticker | Company | Sector / Sub-industry | Price | Analyst target | Fwd PE | Shortage | Irreplace. | Borda | Appear. | #1 votes | Avg place | One-line case |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MU | Micron Technology | Information Technology / Semiconductors | \$811.30 | \$1,561.91 (+92.5%) | 3.9x | 10 | 7 | 34 | 4/4 | 3 | 2.50 | HBM sold out, \$32bn prepayments, ~\$150bn RPO |
| 2 | CDNS | Cadence Design Systems | Information Technology / Application Software | \$329.26 | \$411.76 (+25.1%) | 33.4x | 6 | 9 | 28 | 4/4 | 1 | 4.00 | Flat year, record \$8.2bn backlog, EDA duopoly |
| 3 | CF | CF Industries | Materials / Fertilizers & Agricultural Chemicals | \$123.24 | \$128.79 (+4.5%) | 10.9x | 9 | 8 | 27 | 3/4 | 0 | 2.00 | 97% utilisation, ~9m tons urea lost; war-dependent |
| 4 | PH | Parker Hannifin | Industrials / Industrial Machinery & Supplies & Components | \$972.90 | \$1,138.29 (+17.0%) | 23.8x | 7 | 9 | 26 | 4/4 | 0 | 4.50 | Record \$13.7bn backlog, certification lock-in |
| 5 | MSFT | Microsoft | Information Technology / Systems Software | \$521.13 | \$636.12 (+22.1%) | 21.5x | 7 | 8 | 25 | 4/4 | 0 | 4.75 | Azure +48%, \$677bn RPO, demand exceeds supply |
| 6 | NUE | Nucor | Materials / Steel | \$261.39 | \$296.81 (+13.6%) | 11.9x | 7 | 7 | 17 | 4/4 | 0 | 6.75 | Record shipments, towers backlog into 2028; FLAG tariff wall is policy, reversible |
| 7 | LLY | Eli Lilly | Health Care / Pharmaceuticals | \$1,437.29 | \$1,453.40 (+1.1%) | 28.4x | 7 | 9 | 17 | 3/4 | 0 | 5.33 | GLP-1 #1 by 1.7x, guidance raised \$5.5bn; at 52w high |
| 8 | ANET | Arista Networks | Information Technology / Communications Equipment | \$196.68 | \$249.07 (+26.6%) | 32.9x | 8 | 6 | 16 | 3/4 | 0 | 5.67 | AI networking +58.5%, guide \$18.5bn; FLAG Nvidia now leads Ethernet |
| 9 | ISRG | Intuitive Surgical | Health Care / Health Care Equipment | \$449.53 | \$486.57 (+8.2%) | 36.1x | 5 | 8 | 15 | 4/4 | 0 | 7.25 | Record placements, sold-off moat, 84% recurring |
| 10 | CBOE | Cboe Global Markets | Financials / Financial Exchanges & Data | \$369.19 | \$355.60 (-3.7%) | 23.9x | 7 | 9 | 9 | 3/4 | 0 | 8.00 | Legal SPX monopoly to 2051, record 0DTE surge; FLAG target below price |

Tie-break: #6 vs #7 is a tie at 17 Borda points (NUE vs LLY). Decided on doctrine: NUE appears on all 4 ballots (LLY on 3) and carries the fresher backlog evidence (record Q3, towers backlog doubled since January with orders into early 2028, GM platform win) while LLY's FDA shortage is resolved, it sits at its 52-week high, and analyst upside is only +1.1%. Every other Borda total is distinct. Closest call at the top is #1 vs #2: MU 34 vs CDNS 28 — MU also wins the single-pick tally (6 vs 2) and has the better average placement (2.50 vs 4.00).

## Per-name thesis

**1. MU — Micron Technology.** The shortage is physical and contracted: HBM sold out through 2026 with most of 2027 committed, \$32bn of customer prepayments on ~\$150bn RPO (30 Sep 2026), DRAM prices +400% since 2024 while shipments grew only ~4–20%. Category leader in a ~90%-concentrated DRAM oligopoly (Samsung, SK Hynix, Micron) — verification corrected the dossier's literal "only three firms" wording: CXMT is a fourth producer at ~9.5% share, a long-run margin threat, not an in-sourcing threat. The moat is fab scale + Nvidia qualification lock-in; no hyperscaler builds its own DRAM fab.

**2. CDNS — Cadence Design Systems.** The contrarian's pick and the panel's #2: flat over 12 months (+0.1%), 20.9% below its high, while the business posted a third straight beat-and-raise, revenue +22% YoY, and a record \$8.2bn backlog (+17% YoY) with \$4.2bn RPO in the next 12 months. The moat is the Synopsys–Cadence duopoly (~74% combined share) with foundry-certified flows and near-100% retention — in-sourcing feeds it, since every custom hyperscaler ASIC is designed on Cadence tools. Shortage score is only 6/10 because there is no physical shortage; it is a compounding tollbooth, not a price spike.

**3. CF — CF Industries.** The only genuine physical shortage in the field: Middle East hostilities since Feb 2026 removed ~9M metric tons of urea, exports halved, >35% of European ammonia capacity curtailed, CF's own plants at 97% utilisation, Q3 UAN shipments the highest of the decade. Nitrogen is biologically irreplaceable (irreplaceability 8/10). The caveat is the driver: a war that could end, and the street is only a Hold at ~\$123 — the shortage is real but unawarded. **EV guardrail flag: CF's probability-weighted EV upside is +12.8%, below the +15% guardrail** (see scenarios below) — it stays in the ranking, but the guardrail would block it as an actionable single pick.

**4. PH — Parker Hannifin.** Record \$13.7bn backlog (+13% rolling orders), certification lock-in on flight-critical systems (irreplaceability 9/10), FY27 guidance raised after a record Q1 FY27. Re-admitted after yesterday's borderline cut. The flag is balance sheet: debt nearly doubled to \$14.64bn for the \$9.25bn Filtration Group deal, plus a \$2.55bn CIRCOR deal pending, at the batch's highest multiple (23.8x fwd PE).

**5. MSFT — Microsoft.** Azure \$33.2bn, +48% YoY (first-ever dollar disclosure, 28 Oct 2026); commercial RPO \$677bn, +73% YoY — but flat sequentially (−\$1bn QoQ) and ~45% OpenAI-concentrated; bookings fell 12%. Capex \$45.2bn/quarter is eating FCF (−27%). The stock is up only +3.8% in 12 months with +22.1% analyst upside: the market is openly sceptical of the biggest contracted AI backlog on earth.

**6. NUE — Nucor.** Record 7.2M-ton shipments (third straight record quarter), towers & structures backlog more than doubled since January with orders into early 2028, data centres ~15% of backlog, and a GM entire-platform win for exposed auto sheet. Q3 2026: \$5.80 EPS, \$2.28bn EBITDA, best quarter in 3+ years. FLAG: +85.4% in 12 months on a cyclical steel boom, and the tariff wall is policy, reversible.

**7. LLY — Eli Lilly.** GLP-1 demand surge intact (Q3 rev +39% to \$24.4bn; Mounjaro +65%, Zepbound +49%; guidance raised to \$91–92bn for the third time this year), clear #1 at ~1.7x Novo's GLP-1 revenue. But the FDA shortage is resolved — it is now a capacity/share race, not empty shelves — and the stock sits at its 52-week high with only +1.1% analyst upside.

**8. ANET — Arista Networks.** Q3 2026 revenue \$3.66bn, +58.5% YoY, fastest since IPO; FY27 guided ~\$18.5bn (+38–40%). FLAG (the trap, live): Nvidia Spectrum-X is now #1 in datacenter Ethernet (20.4% vs Arista's 18.7%, IDC 2Q26) and hyperscalers self-build with white-box/Celestica — Panelist C excluded ANET from its top 10 entirely on this ground.

**9. ISRG — Intuitive Surgical.** Placements +28% (546 systems, 315 da Vinci 5) and procedures +15%, but guidance narrowed to 14–15% and management flagged a 3–5% per-procedure instrument price cut from H1 2027; shares fell ~13% post-print despite a big beat. Hugo/Versius competition is now real.

**10. CBOE — Cboe Global Markets.** SPX 0DTE ADV record 3.2m (+34%), 65% of SPX volume; Q3 net revenue \$712.2m (+18%), adj. EPS \$3.63 (+36%); exclusive SPX licence extended through 2051 (irreplaceability 9/10). FLAG: at a 52-week high with analyst upside −3.7% — the surge looks already priced.

## Just-missed names

- **EOG (Borda 3, 2/4 ballots)** — record production (1.433 MMBoe/d), \$20bn buyback, but a war-premium oil price-taker; EIA sees a 4.91 mb/d surplus in 2027. RECEIVABLES_OUTRUN flag judged benign (timing swell, OCF > net income by >\$1bn).
- **VRTX (Borda 2, 1/4 ballots)** — a monopoly, not a shortage (shortage 3/10); growth rests on Casgevy/Journavx and the 30 Nov povetacicept PDUFA. INVENTORY_BUILD flag judged benign (launch stocking).
- **NEM (Borda 1, 1/4 ballots)** — record Q3 on a \$4,317/oz realised gold price, but production fell 8%: the "shortage" is price, not volume, and gold is perfectly substitutable.
- **PM and COP (Borda 0, unranked by all four lenses)** — PM's Zyn supply crunch is over and Velo is taking two-thirds of category growth; COP is the weaker E&P (80% reserve replacement, reserves shrank, production −2% YoY).

## What the panel revealed

- **Agreement:** A, B, and C all put MU #1 (conviction 8/10 each); CF is #2 on three ballots (A, C, D) but unranked by B, which treats it as a price story, not a compounder. CDNS is the only name ranked by all four lenses in the top 8 and the contrarian's top pick.
- **Disagreement:** the panel splits on whether MU is a durable contracted shortage or the most crowded trade in the market — D demotes MU to #7 (+220.7% in 12m, "already priced") while A/B/C rank it #1. The same split runs through ANET: B ranks it #2 on growth, C excludes it entirely on the live Nvidia/white-box in-sourcing threat.
- **Conviction vs consensus:** MU is both (3 #1 votes, 4/4 appearances); CF is pure consensus (ranked #2 by three lenses, zero #1 votes, best average placement in the field at 2.00); CDNS is the contrarian conviction name (D's #1, only 1 #1 vote overall, worst average placement of the top 3 at 4.00).

## If forced to ONE

**MU** — the strict trap-veto would land on the same name as Borda #1. The trap (disintermediation/in-sourcing) cannot touch MU: hyperscalers cannot build DRAM fabs, and the only live threat (CXMT, 9.5% share) is a margin competitor, not an in-sourcer. CDNS would be the forced pick only if the panel weighted "not yet priced" above "shortage contracted in cash" — that is D's case, and it lost 6–2 in the single-pick tally.

## Return scenarios — top 3

All numbers are research scenarios, not guarantees. Prices are the 2026-11-11 close from the screen.

| Name | Bear (price, by) | Base (price, by) | Bull (price, by) | Probabilities | EV | EV upside |
| --- | --- | --- | --- | --- | --- | --- |
| MU | \$580, 2027-Q2 | \$1,152, 2027-Q2 | \$1,562, 2027-Q4 | 30 / 45 / 25 | \$1,082.90 | +33.5% — clears +15% |
| CDNS | \$263, 2027-Q2 | \$428, 2027-Q2 | \$527, 2027-Q4 | 20 / 55 / 25 | \$419.75 | +27.5% — clears +15% |
| CF | \$92, 2027-Q2 | \$148, 2027-Q2 | \$179, 2027-Q4 | 30 / 45 / 25 | \$138.95 | +12.8% — BELOW +15% guardrail, flagged |

- **MU:** bear is a July-style 28% drawdown if HBM pricing rolls over (30% — weighted up for a price spike on ~4% shipment growth); base is the contracted backlog converting at today's pricing (45%); bull needs the shortage to extend into 2028 *and* a multiple re-rating (25%). Market price sits between bear and base, closer to bear — the market prices a short cycle.
- **CDNS:** bear is a continued expensive-multiple de-rating on China/export-control exposure (20%); base is ~21% growth compounding plus partial multiple repair toward the +25.1% analyst upside (55%); bull is a full re-rating to and beyond the 52-week high on continued beat-and-raise quarters (25%). Market price sits between bear and base.
- **CF:** bear is the war ending and urea normalising (30%); base is tight pricing persisting into H1 2027 (45%); bull is the disruption persisting through 2027 (25%). Market price sits closest to base (street Hold at ~\$123) — the shortage is real but the market has not awarded it a premium. **EV upside +12.8% is below the +15% guardrail: CF stays in the ranking, but it would not be an actionable single pick.**

## What was verified

Phase 3.5 (parts/2026-11-12/verification.md), 10 claims: 8 CONFIRMED, 1 CONTRADICTED, 1 UNVERIFIED. MU: HBM sold out through 2026 / most of 2027 committed — CONFIRMED; \$32bn prepayments — CONFIRMED (and RPO corrected up to ~\$150bn at 30 Sep 2026 from the dossier's stale ~\$100bn); Q4 FY26 revenue \$54.23bn / FY26 \$133.19bn — CONFIRMED (with the 14-week vs 13-week nuance); next earnings 2026-12-23 — UNVERIFIED, aggregator estimate only. MU moat wording — CONTRADICTED as literally worded ("only three firms make DRAM at scale"; CXMT is a fourth at ~9.5%) and corrected to a ~90%-concentrated oligopoly. CDNS \$8.2bn backlog +17% / \$4.2bn RPO +20% — CONFIRMED; EDA duopoly ~74% — CONFIRMED. CF ~9M tons urea removed, 97% utilisation, Q3 adj. EBITDA \$833M — CONFIRMED. Screen figures confirmed: MU \$811.30 / \$1,561.91; CDNS \$329.26; CF \$123.24.

## Risk lens & leverage-safety note

Sector concentration: the top 10 spans 5 sectors, but the top 3 are all single-theme AI/commodity-cycle names (memory, EDA, fertilizer) — the ranking is a bet on shortage duration, not diversification. Highest-risk: MU and CF are both hostage to a single variable (memory-cycle duration; a war). Steadiest compounders: CDNS, PH, MSFT — contracted backlogs with multi-year visibility. Drawdown reality: MU fell 28% in July 2026 on a margin-duration repricing alone and sits 33.1% off its high after +220.7% in 12 months; ISRG fell ~13% post-print despite a beat; a high-beta cyclical can draw down 50%+ fast, which is brutal with margin. POLICY.md §2 is cash-only. This is risk education, not advice: no specific leverage multiple or position size is recommended here.

## Thesis-break / trap triggers to watch

- MU: backlog/RPO shrinking; DRAM spot pricing rolling over two months running; CXMT share >15%; a top customer shrinking a prepayment contract.
- CDNS: backlog growth stalling; China export controls tightening (~15.6% of revenue); open-source EDA reaching advanced-node parity.
- CF: Middle East hostilities ending; urea exports normalising toward 1.5M+ t/month; new capacity announcements through 2030.
- ANET: Nvidia extending its Ethernet lead; a hyperscaler announcing a large white-box self-build.
- NUE: tariff wall weakening; South Korea import surge accelerating.
- CBOE: 0DTE volumes rolling over; SPX licence terms revisited before 2051.

*This is research output, not financial advice. All scenario numbers are research estimates, not guarantees.*
