> Run by: Muse Wonder (unknown) — full panel

# Triage — earnings — 2026-10-21

Screen: `scripts/screen.py --mode earnings` run 2026-10-21 16:36 UTC on prices as of the 2026-10-20 close (parent ran `fetch.py`: 503 tickers, 0 errors). Funnel: 503 → 382 profitable → 342 rev growth >0 → 244 leverage ok → 197 reports ≤45d → 161 mktcap ≥$20B → 141 misses <2 of 4q → 71 beat→up rate >50% (stage 5d dropped 70) → 49 op margin > sector median → 47 earnings quality → **46 final**.

Field split (skill Phase 1): **actionable now = days_to_earnings ≤10 → 30 names**; **watchlist = 11–45 days → 16 names**. Actionable set is 10+, so triage normally to 15 for the research fan-out. Watchlist names are scored and parked below the table — they are DROP for this run's research budget only, not doctrine rejects.

Calendar of the actionable wave: today 2026-10-21 — META, MCO, LVS, CSX; 2026-10-22 — UNP; 2026-10-26 — NUE; 2026-10-27 — STX, KO, V, ECL; 2026-10-28 — APH, FTNT, GRMN, GOOG, BIIB, EBAY, ADP, BSX, ODFL, ORLY; 2026-10-29 — LLY, MPWR, HWM, DXCM, WST, MA, TT, ILMN; 2026-10-30 — REGN, ABBV.

Doctrine score = reaction record first (beat_up_rate, reaction_avg_abs_move, reaction_last4), then beat size/trend, revenue acceleration, priced-in risk (ret_21d / run flag / forward PE), fallback quality. Screen data quoted from `shortlist_2026-10-21.json`.

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | APP | 0.793 | DROP — watchlist | 5 | Reports 2026-11-04 (14d); reaction record violent (avg abs 17.7%, last4 −20/+6/−20/+1) and surprise trend shrinking (−4.3) despite high composite — parked, not researched |
| 2 | APH | 0.785 | KEEP | 9 | Best actionable reaction record: beat-up 0.875, avg surprise +11.2% rising, rev +58.4% YoY accelerating, no run into print (−3.8%), no EQ flags; prints 2026-10-28 |
| 3 | STX | 0.776 | KEEP | 8 | Surprise +11.8% rising, rev accel +27.2%, price washed out into print (ret_21d −24.1%) so little priced in; beat-up only 0.625 and RECEIVABLES_OUTRUN flag to explain; prints 2026-10-27 |
| 4 | LLY | 0.740 | KEEP | 9 | Largest surprises on sheet (+20.4%, trend +12.4), last4 reactions all positive (+5/+10/+10/+4), rev +47.7%; priced-in watch: near 52w high, analyst upside only +5.1%; prints 2026-10-29 |
| 5 | OXY | 0.712 | DROP — watchlist | 6 | Reports 2026-11-09 (19d); strong record (beat-up 0.875) but commodity-driven EPS surprises (+54.2% avg) are oil beta, not guide craft — parked |
| 6 | MPWR | 0.703 | KEEP | 8 | Beat-up 0.75, surprise trend +5.7, rev accel +25.3%, ret_21d −7.6% (not priced); RECEIVABLES_OUTRUN flag to explain; 36× fwd PE is the trap question; prints 2026-10-29 |
| 7 | HWM | 0.700 | KEEP | 8 | Steady payer: beat-up 0.75, last4 −3/+6/+6/+2, avg abs only 5.9%, surprise +7.5%, quality fallback; prints 2026-10-29 |
| 8 | CPAY | 0.699 | DROP — watchlist | 7 | Reports 2026-11-04 (14d); excellent reaction record (beat-up 0.857, worst −3.4%) — first name off the watchlist if a slot opens; parked by calendar |
| 9 | FTNT | 0.689 | KEEP | 7 | Surprise +19.8% with trend +13.7 and rev accel; against it: worst reaction −22.0%, trades above analyst mean target (upside −2.6%), 45.6× fwd PE — priced-in lens decides; prints 2026-10-28 |
| 10 | DXCM | 0.639 | KEEP | 7 | Surprise trend +11.0 (accelerating beats), beat-up 0.667, ret_21d −8.5%; revenue growth modest (+13.1%) is the doubt; prints 2026-10-29 |
| 11 | GRMN | 0.629 | KEEP | 7 | Beat-up 0.833, surprise +17.4%, big typical move (avg abs 11.4%) cuts both ways; revenue only +11.4% YoY; prints 2026-10-28 |
| 12 | REGN | 0.615 | KEEP | 7 | Surprise +18.9% trend +8.7 at only 13.0× fwd PE — cheapest big-beat record in the actionable set; beat-up 0.714; prints 2026-10-30 (9d, inside window) |
| 13 | IDXX | 0.591 | DROP — watchlist | 6 | Reports 2026-11-02 (12d); reaction avg +6.8% attractive but surprise trend negative and revenue +9.7% — parked |
| 14 | MNST | 0.588 | DROP — watchlist | 6 | Reports 2026-11-05 (15d); fine record, low variance (avg abs 4.8%) — parked by calendar |
| 15 | AME | 0.585 | DROP — watchlist | 7 | Reports 2026-11-03 (13d); beat-up 0.875, worst only −2.0%, last4 all positive — strongest watchlist fallback name; parked by calendar |
| 16 | GOOG | 0.579 | KEEP | 6 | Fallback is the best balance sheet in the field and rev accel +10.6%, but surprise trend −15.4 (shrinking beats) and HIGH_ACCRUALS flag (accrual ratio 0.082, CFO/NI 0.76) must be explained; prints 2026-10-28. Borderline keep |
| 17 | FOX | 0.547 | DROP — watchlist | 5 | Reports 2026-11-02 (12d); surprise trend −18.3 collapsing, RECEIVABLES_OUTRUN — parked |
| 18 | WST | 0.527 | DROP | 4 | Actionable (2026-10-29) but worst reaction −38.2% and avg abs 14.3% — the gap being underwritten is the largest on the sheet; beat-up only 0.625 |
| 19 | KO | 0.522 | KEEP | 7 | Low-variance payer: beat-up 0.75, last4 +5/+4/+2/+4, avg abs only 2.9% (cheapest cost of being wrong), surprise trend stable; prints 2026-10-27 |
| 20 | VEEV | 0.520 | DROP — watchlist | 4 | Reports 2026-11-25 (35d) and carries the run-into-print flag (+22.6% in 21d) — parked and flagged |
| 21 | MA | 0.514 | KEEP | 6 | Tiny typical move (avg abs 2.6%), beat-up 0.625, quality fallback; ret_21d +12.3% approaches the run flag — priced-in check; prints 2026-10-29. Borderline keep |
| 22 | V | 0.513 | KEEP | 6 | Same low-variance payments profile as MA (avg abs 2.7%), surprise trend +4.2 improving; ret_21d +12.9% is the priced-in question; prints 2026-10-27 |
| 23 | AMGN | 0.495 | DROP — watchlist | 5 | Reports 2026-11-03 (13d); trades above analyst mean (upside −9.6%) — parked |
| 24 | NUE | 0.493 | KEEP | 7 | Soonest non-today print (2026-10-26, 5d), beat-up 0.714, surprise +9.6%, only 12.5× fwd PE; cyclical steel guide is the risk |
| 25 | EW | 0.472 | DROP — watchlist | 5 | Reports 2026-11-04 (14d); beat-up 0.571 thinnest in field — parked |
| 26 | ADSK | 0.469 | DROP — watchlist | 5 | Reports 2026-11-27 (37d) — parked |
| 27 | BIIB | 0.461 | DROP | 4 | Actionable (2026-10-28) but revenue +3.4% YoY barely clears the growth gate — beats on a flat top line are the manufactured kind; RECEIVABLES_OUTRUN flag |
| 28 | META | 0.450 | DROP | 3 | Prints TODAY (2026-10-21) with the record deteriorating: avg reaction −0.6%, last4 −8/−9/+10/−11, surprise trend −11.9 — high composite nowhere; the screen's date, not a thesis |
| 29 | COP | 0.443 | DROP — watchlist | 4 | Reports 2026-11-05 (15d) with run-into-print flag (+16.6%) — parked and flagged |
| 30 | MCO | 0.434 | DROP | 4 | Prints TODAY (2026-10-21); beat-up 0.571, surprise trend negative — no edge to research on print day |
| 31 | PTC | 0.433 | DROP — watchlist | 3 | Reports 2026-11-04 (14d) with run flag (+38.5%), revenue shrinking YoY (−6.8%), surprise trend −23.3 — parked and flagged |
| 32 | MLM | 0.410 | DROP — watchlist | 5 | Reports 2026-11-03 (13d); avg reaction slightly negative (−0.1%) despite beats — parked |
| 33 | EBAY | 0.401 | DROP | 4 | Actionable (2026-10-28) but avg reaction −0.6% — its beats do not pay; trades above analyst mean (upside −5.2%) |
| 34 | ADP | 0.396 | DROP | 4 | Actionable (2026-10-28); avg surprise only +1.9% — managed-to-the-decimal beats, no event edge at 22× |
| 35 | TT | 0.383 | DROP | 4 | Actionable (2026-10-29); avg surprise +2.4% too thin to underwrite an 8.4% worst reaction |
| 36 | LVS | 0.382 | DROP | 3 | Prints TODAY (2026-10-21) on shrinking revenue (−0.7% YoY, decelerating) and surprise trend −18.9 — manufactured-beat profile |
| 37 | BSX | 0.370 | DROP | 4 | Actionable (2026-10-28); worst reaction −17.6%, revenue decelerating (accel −0.6%) — tail too big for a 0.625 beat-up rate |
| 38 | CSX | 0.368 | DROP | 5 | Prints TODAY (2026-10-21); beat-up 0.60, small surprises (+3.3%) — kept only as the peer read for UNP in research, not a candidate. Borderline drop |
| 39 | UNP | 0.362 | KEEP | 6 | Prints 2026-10-22 (1d) — the most imminent actionable name; beat-up 0.60 and small surprises (+2.5%) are weak, but CSX prints the evening before as a live read and the fallback is a wide-moat railroad. Borderline keep — the panel may reject it on the record |
| 40 | ODFL | 0.358 | DROP | 3 | Actionable (2026-10-28); avg reaction −0.7% — beats do not pay |
| 41 | EMR | 0.334 | DROP — watchlist | 5 | Reports 2026-11-04 (14d); avg surprise only +1.5% — parked |
| 42 | ABBV | 0.310 | DROP | 4 | Actionable (2026-10-30, 9d); beat-up 0.571, surprise +1.7% shrinking — thinnest record in the actionable set |
| 43 | ECL | 0.305 | DROP | 3 | Actionable (2026-10-27, 6d) but avg surprise +0.3% is near-zero — beats managed to the decimal with no event edge; low variance (avg abs 3.8%) does not create an edge where none exists |
| 44 | ILMN | 0.286 | DROP | 3 | Actionable (2026-10-29); trades above analyst mean (upside −12.4%) at 45.8× fwd PE with last4 including +25%/−10% — priced-in and erratic |
| 45 | KVUE | 0.261 | DROP — watchlist | 5 | Reports 2026-11-05 (15d) — parked by calendar |
| 46 | ORLY | 0.220 | DROP | 2 | Actionable (2026-10-28) but beat-up 0.333 on only 3 measured beats — screen note says the rate is not judgeable; the doctrine's central question is unproven here |

**Research set (15):** APH, LLY, STX, HWM, MPWR, GRMN, FTNT, DXCM, REGN, GOOG, KO, V, NUE, UNP, MA.
Batches: B1 = APH, LLY, STX, HWM · B2 = MPWR, GRMN, FTNT, DXCM · B3 = REGN, GOOG, KO, V · B4 = NUE, UNP, MA.

**Watchlist (parked, with dates):** CPAY 2026-11-04 · AME 2026-11-03 · IDXX 2026-11-02 · APP 2026-11-04 · MNST 2026-11-05 · OXY 2026-11-09 · FOX 2026-11-02 · AMGN 2026-11-03 · EW 2026-11-04 · MLM 2026-11-03 · EMR 2026-11-04 · KVUE 2026-11-05 · COP 2026-11-05 (run flag) · PTC 2026-11-04 (run flag) · VEEV 2026-11-25 (run flag) · ADSK 2026-11-27.

**Prior-pick close check (addendum §3):** ledger scan before this run found these earnings `single` picks whose `next_earnings` has passed or is today with NO `kind=close` row — GS 2026-09-21 (print 2026-10-13); PEP 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-02 (print 2026-10-08); GS 2026-10-03 (print 2026-10-13); BLK 2026-10-04, 2026-10-05, 2026-10-07, 2026-10-08, 2026-10-09, 2026-10-11 (print 2026-10-14); BNY 2026-10-06, 2026-10-10 (print 2026-10-15); BAC 2026-10-12 (print 2026-10-14); CME 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17 (print 2026-10-21 — TODAY). No close prices are invented in this run; they are named as outstanding in the final writeup and the report to the parent. (FSLR 2026-09-17 prints 2026-10-29, APH 2026-10-18 prints 2026-10-28 and CAT 2026-10-19 prints 2026-10-29 — prints still ahead, not outstanding.)
