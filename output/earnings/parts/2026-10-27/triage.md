> Run by: Muse Wonder (Muse Wonder) — full panel

# Phase 1 triage — earnings, 2026-10-27

Screen rebuilt today for the dated-file requirement (fetch + screen --mode earnings; shortlist_2026-10-27.json generated 2026-10-27, 49 candidates, 45-day window) — note the 2026-10-26 shortlist was <24h old, but check_run.py requires dated shortlist/funnel/dossier matching the published run date, so a fresh dated screen was built; prices are the 2026-10-26 close. Funnel: 503 → profitable → rev growth → leverage → within 45d → ≥$20B → 4q history → misses <2 of 4q → beat-to-up >50% → margin → earnings quality → forward PE → 49. Split per the earnings skill: **actionable now** = reports within ~10 days (44 names); **watchlist** = further out (5 names: OXY 13d, VEEV 29d, A 29d, NTAP 35d, AZO 42d). Actionable set triaged to 15 for the full research fan-out. Reaction record scored first, then beat quality, revenue acceleration, priced-in risk (ret_21d / run flag), and fallback quality. No 2026-10-27 parts existed before this run; nothing reused.

**Prior open earnings picks (addendum §3 check):** named for the owner — no kind=close row exists in picks/ledger.csv for the following single picks whose prints have already happened: GS (picked 2026-09-21 and 2026-10-03, print 2026-10-13), PEP (picked 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-02, print 2026-10-08), BLK (picked 2026-10-04, 2026-10-05, 2026-10-07, 2026-10-08, 2026-10-09, 2026-10-11, print 2026-10-14), BNY (picked 2026-10-06, 2026-10-10, print 2026-10-15), BAC (picked 2026-10-12, print 2026-10-14), CME (picked 2026-10-13 to 2026-10-17, print 2026-10-21). Also CINF was rank10 #10 on 2026-10-26 with a 2026-10-26 print and no close row yet. PAYX (2026-09-22) is the only earnings single with a close row. This run writes no close rows (owner's action per protocol).

Reporting calendar (screen dates): Tue 2026-10-27 STX, FFIV, V, ECL; Wed 2026-10-28 APH, GOOGL, FTNT, GRMN, VRT, GOOG, EBAY, ADP, ODFL, BSX, ORLY; Thu 2026-10-29 SNDK, INCY, LLY, HWM, MPWR, DXCM, MA, WST, TT, ILMN; Fri 2026-10-30 CBOE, REGN, ABBV, KVUE; Mon 2026-11-02 IDXX, FOX, FOXA; Tue 2026-11-03 AME, AMGN, PFE; Wed 2026-11-04 APP, CPAY, PTC, EW, MLM; Thu 2026-11-05 PH, MNST, RL, COP; watchlist Mon 2026-11-09 OXY, Tue 2026-11-25 VEEV/A, Tue 2026-12-01 NTAP, Tue 2026-12-08 AZO.

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | SNDK | 0.811 | KEEP | 9 | Rev accelerating hard, ret_21d -29.4%, -46% off high — de-rated not crowded; beat_up 0.667, avg surprise +46.3% but trend shrinking -19.2, short post-spin history |
| 2 | INCY | 0.759 | KEEP | 8 | beat_up 0.80, surprise trend +23.6 (beats growing), rev accelerating; two of last4 reactions negative |
| 3 | APH | 0.756 | KEEP | 9 | Best beat-to-up actionable (0.875), rev +58% YoY accelerating, ret_21d -9.6%; prints Wed 2026-10-28 |
| 4 | APP | 0.750 | KEEP | 7 | Promoted from yesterday's edge alternate — now 8d out; field's biggest bet (avg abs 17.7%, two -20% reactions), worst -19.7%; panel must weigh variance |
| 5 | STX | 0.737 | KEEP | 8 | Rev accelerating, ret_21d -28.6% — optimism wrung out; beat_up 0.625, avg abs 11.0%; RECEIVABLES_OUTRUN flag for Phase 2; prints TODAY Tue 2026-10-27 |
| 6 | LLY | 0.715 | KEEP | 7 | Elite record (4/4 at +20.4%, last4 all positive), ret_21d +7.8% near highs — priced-in is the whole case |
| 7 | CPAY | 0.693 | KEEP | 8 | beat_up 0.857, last4 all positive, worst only -3.4%, reports Wed 2026-11-04 |
| 8 | OXY | 0.686 | DROP (watchlist) | 7 | Reports 2026-11-09 (13d) — watchlist; strong record (beat_up 0.875, avg surprise +54.0%) parked |
| 9 | HWM | 0.663 | KEEP | 7 | ret_21d -16.9%, clean record beat_up 0.75, rev accelerating; prints Thu 2026-10-29 |
| 10 | MPWR | 0.660 | KEEP | 6 | Rev accelerating, surprise trend positive, ret_21d -14.5%; avg abs 8.9%, worst -17.5%, RECEIVABLES_OUTRUN flag, 33.1x forward. Borderline |
| 11 | GOOGL | 0.636 | KEEP | 6 | Elite fallback; print is the capex event of the week; GAAP surprises distorted, HIGH_ACCRUALS flag — research must normalise |
| 12 | FTNT | 0.621 | KEEP | 6 | Surprise trend strong, rev accelerating, but 48.4x forward — kept so the setup lens can prosecute the trap |
| 13 | GRMN | 0.606 | KEEP | 7 | beat_up 0.833, avg move positive; avg abs 11.4% is a large bet, worst -11.5% |
| 14 | CBOE | 0.597 | KEEP | 8 | Best risk shape: beat_up 0.857, last4 all positive, worst -1.7%, avg abs 3.6%; flaw: run_into_print_flag TRUE (ret_21d +31.3%) — the trap case in pure form |
| 15 | DXCM | 0.584 | DROP (alternate) | 5 | Surprise trend attractive but last reaction -15%, avg abs 9.0%, worst -14.6% — first alternate |
| 16 | REGN | 0.571 | DROP | 5 | Solid but unremarkable; no doctrine axis beats the keeps |
| 17 | AME | 0.569 | KEEP | 7 | Yesterday's pick, re-screened: metronome record beat_up 0.875, last4 all positive, worst -2.0%, avg abs 4.1% — low-variance candidate; reports Tue 2026-11-03 (7d) |
| 18 | PH | 0.552 | DROP (edge alternate) | 7 | Reports 2026-11-05 (9d, edge); beat_up 0.875 parked as edge alternate |
| 19 | VRT | 0.549 | DROP | 5 | Reactions violent (-17%/+24% in last4), INVENTORY_BUILD flag — coin flip |
| 20 | FFIV | 0.546 | KEEP | 7 | beat_up 0.75, prints TODAY Tue 2026-10-27; print IS the initial FY guide event — guide-risk is the question |
| 21 | IDXX | 0.540 | DROP | 5 | Actionable (6d) but rev growth thin, avg surprise +5.8%, 34.0x forward. Borderline |
| 22 | MNST | 0.535 | DROP (edge) | 6 | Reports 2026-11-05 (9d); 35.4x for a beverage name, avg surprise only +4.2% |
| 23 | GOOG | 0.535 | DROP | 5 | Same company as GOOGL (kept); duplicate class adds nothing; HIGH_ACCRUALS flag |
| 24 | FOX | 0.506 | DROP | 5 | Surprise trend negative and RECEIVABLES_OUTRUN flag; duplicate economics with FOXA |
| 25 | VEEV | 0.500 | DROP (watchlist) | 5 | Reports 2026-11-25 (29d) — watchlist |
| 26 | FOXA | 0.500 | DROP | 5 | Same as FOX |
| 27 | RL | 0.496 | DROP (edge) | 6 | Reports 2026-11-05 (9d); no axis beats the keeps |
| 28 | MA | 0.495 | DROP | 4 | Beats barely pay (avg abs 2.6%) — no event edge |
| 29 | V | 0.485 | DROP | 4 | Same shape as MA (avg abs 2.7%); prints Tue 2026-10-27 |
| 30 | WST | 0.483 | DROP | 4 | At highs, 39.4x, reaction_worst -38.2% — gap risk uncompensated |
| 31 | NTAP | 0.458 | DROP (watchlist) | 5 | Reports 2026-12-01 (35d) — watchlist; INVENTORY_BUILD flag |
| 32 | AMGN | 0.449 | DROP | 5 | Actionable (7d) but no axis beats keeps. Borderline |
| 33 | PFE | 0.422 | DROP | 5 | Surprise trend negative (beats shrinking) |
| 34 | COP | 0.419 | DROP (edge) | 5 | Reports 2026-11-05 (9d); beat_up 0.571, avg abs 2.4%, run flag TRUE |
| 35 | A | 0.418 | DROP (watchlist) | 6 | Reports 2026-11-25 (29d) — watchlist; beat_up 0.857 parked |
| 36 | PTC | 0.411 | DROP (edge) | 4 | Reports 2026-11-04 (8d); run flag TRUE (+40.5%) — trap shape |
| 37 | EW | 0.409 | DROP (edge) | 5 | Reports 2026-11-04 (8d); beat_up only 0.571 |
| 38 | EBAY | 0.372 | DROP | 4 | Last print -16%, worst -15.9% — reaction record fails the doctrine |
| 39 | TT | 0.368 | DROP | 4 | Avg surprise only +2.4% — beats too small to pay |
| 40 | MLM | 0.358 | DROP (edge) | 4 | Reports 2026-11-04 (8d); avg reaction negative |
| 41 | ADP | 0.351 | DROP | 4 | Avg surprise +1.9% (managed to the decimal) — priced-in shape |
| 42 | ODFL | 0.344 | DROP | 4 | beat_up 0.571 lowest tier, avg reaction negative |
| 43 | ILMN | 0.319 | DROP | 3 | beat_up 0.571, rev growth low, 44.5x forward |
| 44 | BSX | 0.315 | DROP | 3 | Guide referendum after repeated cuts/withdrawal in prior research — guide-risk maximal |
| 45 | ABBV | 0.292 | DROP | 4 | beat_up 0.571, avg surprise only +1.7% |
| 46 | ECL | 0.272 | DROP | 4 | Prints Tue 2026-10-27 but avg surprise +0.3% — no beat edge |
| 47 | KVUE | 0.228 | DROP | 3 | beat_up 0.571, rev growth low — weakest record tier |
| 48 | ORLY | 0.193 | DROP | 3 | beat_up 0.333 on few measured beats — not judgeable, unproven |
| 49 | AZO | 0.138 | DROP (watchlist) | 3 | Reports 2026-12-08 (42d) — watchlist; beat_up 0.333, not judgeable; RECEIVABLES_OUTRUN flag |

## Kept for research (15)

SNDK, INCY, APH, APP, STX, LLY, CPAY, HWM, MPWR, GOOGL, FTNT, GRMN, CBOE, AME, FFIV — batches: (1) SNDK, STX, MPWR, GOOGL, FTNT (tech/storage/semis); (2) APH, HWM, GRMN, CBOE, AME (industrials/exchange/instruments); (3) INCY, LLY, CPAY, APP, FFIV (pharma/fintech/software/networking).

## Watchlist (reports >10 days out — parked, pre-vetted)

| ticker | next print | days | note |
|---|---|---|---|
| OXY | 2026-11-09 | 13 | beat_up 0.875, avg surprise +54.0% — strongest watchlist name |
| VEEV | 2026-11-25 | 29 | 4/4 beats, avg abs 9.1% |
| A | 2026-11-25 | 29 | beat_up 0.857 |
| NTAP | 2026-12-01 | 35 | INVENTORY_BUILD flag to resolve |
| AZO | 2026-12-08 | 42 | beat record not judgeable (few measured) |
