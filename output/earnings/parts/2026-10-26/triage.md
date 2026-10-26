> Run by: Muse Wonder (Muse Wonder) — full panel

# Phase 1 triage — earnings, 2026-10-26

Screen rebuilt today (fetch + screen --mode earnings; shortlist_2026-10-26.json generated 2026-10-26 16:40 UTC, Monday intraday prices): 50 candidates, 45-day window. Funnel: 503 → profitable → rev growth → leverage → within 45d → ≥$20B → 4q history → misses <2 of 4q → beat-to-up >50% (165→83, 82 dropped) → margin (83→52) → earnings quality (52→51, CDNS dropped) → forward PE (51→50). Split per the earnings skill: **actionable now** = reports within ~10 days (45 names); **watchlist** = further out (5 names: OXY 14d, VEEV 30d, NTAP 36d, A 30d, AZO 43d). Actionable set triaged to 15 for the full research fan-out. Reaction record scored first, then beat quality, revenue acceleration, priced-in risk (ret_21d / run flag), and fallback quality. No 2026-10-26 parts existed before this run; nothing reused.

**Screen-data note (gate artifact, not a thesis change):** BMY, CAT and KO — yesterday's Borda top-3 / single pick (BMY) — are ABSENT today, dropped at stage 1 "profitable" with netIncomeToCommon=NaN / profitMargins=NaN in drops_2026-10-26.csv (confirmed via scripts/why.py). Fetch reported 503/503 ok, so this reads as a cached-fundamentals NaN artifact, not deteriorated profitability. Per protocol the screen is not overridden: the panel judges only today's screened set, and the BMY print (Thu 2026-10-29) pick history stands in the ledger untouched. CME also absent (next print 2027-02-03, outside the window).

**Prior open earnings picks (addendum §3 check):** named for the owner — CME (picked 2026-10-17, rank10 #1 row, print 2026-10-21) has already printed and still has NO kind=close row in picks/ledger.csv; all other open earnings #1 rows (APH 2026-10-28, CAT 2026-10-29, BMY 2026-10-29) print later this week and are not yet due. This run writes no close rows (owner's action).

Reporting calendar (screen dates): Mon 2026-10-26 CINF (today, 0d); Tue 2026-10-27 STX, FFIV, V, ECL; Wed 2026-10-28 APH, GOOGL, GOOG, FTNT, GRMN, VRT, EBAY, ADP, ODFL, BSX, ORLY; Thu 2026-10-29 SNDK, INCY, LLY, HWM, MPWR, DXCM, MA, WST, TT, ILMN; Fri 2026-10-30 CBOE, REGN, ABBV, KVUE; Mon 2026-11-02 IDXX, FOX, FOXA; Tue 2026-11-03 AME, AMGN, PFE; Wed 2026-11-04 APP, CPAY, PTC, EW, MLM; Thu 2026-11-05 PH, MNST, RL, COP.

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | SNDK | 0.812 | KEEP | 9 | Rev YoY +372% accelerating hard, ret_21d -29.2%, -46% off high — de-rated not crowded; beat_up 0.667, avg surprise +46.3% but trend shrinking (-19.2), short post-spin history |
| 2 | INCY | 0.763 | KEEP | 8 | beat_up 0.80, surprise trend +23.6 (beats growing), rev +37.7% accelerating; two of last4 reactions negative (-8%, -2%) |
| 3 | APH | 0.758 | KEEP | 9 | Best beat-to-up conversion actionable (0.875), rev +58.4% accelerating, ret_21d -9.6%; prints Wed 2026-10-28 |
| 4 | APP | 0.750 | DROP (edge alternate) | 7 | Reports 2026-11-04 (9d, edge); field's biggest bet (avg abs 17.7%, two -20% reactions in last4), worst -19.7% |
| 5 | STX | 0.739 | KEEP | 8 | Rev +48.5% accelerating, ret_21d -28.6% — optimism wrung out; beat_up 0.625, avg abs 11.0% is a big bet; RECEIVABLES_OUTRUN flag for Phase 2; prints Tue 2026-10-27 |
| 6 | LLY | 0.720 | KEEP | 7 | Elite record (4/4 at +20.4%, trend +12.4, last4 all positive), ret_21d +7.8% but price 1275.80 near highs — priced-in is the whole case |
| 7 | CPAY | 0.696 | KEEP | 8 | Promoted from yesterday's first-off-the-bench: beat_up 0.857, last4 all positive (+1/+13/+12/+6), worst only -3.4%, surprise trend +4.8; reports Wed 2026-11-04 (9d, edge) |
| 8 | OXY | 0.686 | DROP (watchlist) | 7 | Reports 2026-11-09 (14d) — watchlist; strong record (beat_up 0.875, avg surprise +54.0%) parked |
| 9 | HWM | 0.662 | KEEP | 7 | Screen price 193.10 (recovered from yesterday's 185.91 low print), ret_21d -16.9%, clean record beat_up 0.75, rev +24.1%; prints Thu 2026-10-29 |
| 10 | MPWR | 0.662 | KEEP | 6 | Promoted: rev +47.6% accelerating, surprise trend +5.7, ret_21d -14.5%; against it avg abs 8.9%, worst -17.5%, RECEIVABLES_OUTRUN flag, 33.1x forward — kept so the panel can weigh it with the flag explained. Borderline |
| 11 | GOOGL | 0.635 | KEEP | 6 | Elite fallback; print is the capex event of the week; GAAP surprises distorted (avg +84.9% not clean), HIGH_ACCRUALS flag — research must normalise |
| 12 | FTNT | 0.622 | KEEP | 6 | Surprise trend +13.7, rev accelerating, but price 183.55 at 48.4x forward — kept so the setup lens can prosecute the trap |
| 13 | GRMN | 0.608 | KEEP | 7 | beat_up 0.833, avg move +4.5%; avg abs 11.4% is a large bet, worst -11.5% |
| 14 | CBOE | 0.596 | KEEP | 8 | Best risk shape: beat_up 0.857, last4 all positive, worst only -1.7%, avg abs 3.6% smallest bet; flaw: run_into_print_flag TRUE (ret_21d +31.3%) — the trap case in pure form |
| 15 | DXCM | 0.584 | DROP (alternate) | 5 | Surprise trend +11.0 attractive but last reaction -15%, avg abs 9.0%, worst -14.6% — first alternate |
| 16 | REGN | 0.572 | DROP | 5 | Solid but unremarkable; no doctrine axis beats the keeps |
| 17 | AME | 0.568 | KEEP | 7 | Promoted from yesterday's alternate: metronome record beat_up 0.875, last4 all positive, worst -2.0%, avg abs 4.1% — the low-variance candidate; reports Tue 2026-11-03 (8d) |
| 18 | PH | 0.554 | DROP (edge alternate) | 7 | Reports 2026-11-05 (10d, edge); beat_up 0.875 parked as edge alternate |
| 19 | VRT | 0.551 | DROP | 5 | Reactions violent (last4 -17%/+24%), INVENTORY_BUILD flag — coin flip with leverage-like variance |
| 20 | FFIV | 0.549 | KEEP | 7 | beat_up 0.75, prints Tue 2026-10-27; print IS the initial FY guide event — guide-risk is the question |
| 21 | MNST | 0.539 | DROP (edge) | 6 | Reports 2026-11-05 (10d, edge); 35.4x for a beverage name, avg surprise only +4.2% |
| 22 | IDXX | 0.539 | DROP | 5 | Actionable (7d) but rev only +9.7%, avg surprise +5.8% thin, 34.0x forward — weakest doctrine case among near names. Borderline |
| 23 | GOOG | 0.535 | DROP | 5 | Same company as GOOGL (kept); duplicate class adds nothing; HIGH_ACCRUALS flag |
| 24 | FOX | 0.508 | DROP | 5 | Actionable (7d) but surprise trend -18.3 and RECEIVABLES_OUTRUN flag; duplicate economics with FOXA |
| 25 | FOXA | 0.503 | DROP | 5 | Same as FOX; surprise trend -15.2 |
| 26 | RL | 0.498 | DROP (edge) | 6 | Reports 2026-11-05 (10d, edge); no axis beats the keeps |
| 27 | VEEV | 0.497 | DROP (watchlist) | 5 | Reports 2026-11-25 (30d) — watchlist |
| 28 | MA | 0.494 | DROP | 4 | Beats barely pay (avg abs 2.6%) — no event edge |
| 29 | V | 0.485 | DROP | 4 | Same shape as MA (avg abs 2.7%); print is initial FY outlook; prints Tue 2026-10-27 |
| 30 | WST | 0.484 | DROP | 4 | At highs, 39.4x, reaction_worst -38.2% is the field's left tail — gap risk uncompensated |
| 31 | NTAP | 0.456 | DROP (watchlist) | 5 | Reports 2026-12-01 (36d) — watchlist; INVENTORY_BUILD flag |
| 32 | AMGN | 0.452 | DROP | 5 | Actionable (8d) but no axis beats keeps. Borderline |
| 33 | CINF | 0.446 | KEEP | 5 | Prints TODAY (Mon 2026-10-26, 0d) and the contrarian case (bar cut hard); honestly weak — surprise trend -34.0, last4 reactions all negative; kept so the panel, not triage, decides. Borderline |
| 34 | PFE | 0.427 | DROP | 5 | Actionable (8d) but surprise trend -18.4 (beats shrinking fast) |
| 35 | A | 0.419 | DROP (watchlist) | 6 | Reports 2026-11-25 (30d) — watchlist; beat_up 0.857 parked |
| 36 | COP | 0.416 | DROP (edge) | 5 | Reports 2026-11-05 (10d, edge); beat_up 0.571, avg abs 2.4%, run flag TRUE (+18.6%) |
| 37 | PTC | 0.413 | DROP (edge alternate) | 4 | Reports 2026-11-04 (9d, edge); revenue shrinking YoY, surprise trend -23.3, run flag +40.5% — trap shape |
| 38 | EW | 0.409 | DROP (edge) | 5 | Reports 2026-11-04 (9d, edge); beat_up only 0.571 |
| 39 | TT | 0.370 | DROP | 4 | Avg surprise only +2.4% — beats too small to pay |
| 40 | EBAY | 0.370 | DROP | 4 | Last print -16%, worst -15.9% — reaction record fails the doctrine |
| 41 | MLM | 0.344 | DROP (edge) | 4 | Reports 2026-11-04 (9d, edge); avg reaction negative |
| 42 | ADP | 0.354 | DROP | 4 | Avg surprise +1.9% (managed to the decimal), ret_21d +14.5% near the run flag — priced-in shape |
| 43 | ODFL | 0.344 | DROP | 4 | beat_up 0.571 lowest tier, avg reaction negative |
| 44 | ILMN | 0.321 | DROP | 3 | beat_up 0.571, rev +4.8%, 44.5x forward — no doctrine axis beats the keeps |
| 45 | BSX | 0.315 | DROP | 3 | Print is a guide referendum after repeated cuts/withdrawal in prior research — guide-risk maximal |
| 46 | ABBV | 0.296 | DROP | 4 | Actionable (4d) but beat_up 0.571, surprise trend -3.0, avg surprise only +1.7% |
| 47 | ECL | 0.275 | DROP | 4 | Prints Tue 2026-10-27 but avg surprise +0.3% — no beat edge at all |
| 48 | KVUE | 0.231 | DROP | 3 | beat_up 0.571, rev +3.1% — weakest record in the field |
| 49 | ORLY | 0.195 | DROP | 3 | beat_up 0.333 on only 3 measured beats — rate not judgeable per screen note; unproven on the doctrine's central question |
| 50 | AZO | 0.139 | DROP (watchlist) | 3 | Reports 2026-12-08 (43d) — watchlist; beat_up 0.333 on 3 measured beats, not judgeable; RECEIVABLES_OUTRUN flag |

## Kept for research (15)

SNDK, INCY, APH, STX, LLY, CPAY, HWM, MPWR, GOOGL, FTNT, GRMN, CBOE, AME, FFIV, CINF — batches: (1) SNDK, STX, MPWR, GOOGL, FTNT (tech/storage/semis); (2) APH, HWM, GRMN, CBOE, AME (industrials/exchange/instruments); (3) INCY, LLY, CPAY, FFIV, CINF (pharma/fintech/networking/insurance).

## Watchlist (reports >10 days out — parked, pre-vetted)

| ticker | next print | days | note |
|---|---|---|---|
| OXY | 2026-11-09 | 14 | beat_up 0.875, avg surprise +54.0% — strongest watchlist name |
| VEEV | 2026-11-25 | 30 | 4/4 beats, avg abs 9.1% |
| A | 2026-11-25 | 30 | beat_up 0.857 |
| NTAP | 2026-12-01 | 36 | INVENTORY_BUILD flag to resolve |
| AZO | 2026-12-08 | 43 | beat record not judgeable (3 measured) |
