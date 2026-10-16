> Run by: Muse Wonder (muse-wonder) — full panel

# Earnings triage — 2026-10-16

Screen: shortlist_2026-10-15.json, 50 candidates, 45-day window, generated 2026-10-15 08:17:40 — reused, <24h old at run start (2026-10-16 04:16 EDT), per protocol Phase 0. Split per earnings SKILL.md Phase 1: actionable = days_to_earnings <= ~10 from 2026-10-16 (screen dte minus 1 day).

**Actionable (5): ISRG (4d, 2026-10-20), PM (5d, 2026-10-21), CME (5d, 2026-10-21), NSC (6d, 2026-10-22), CINF (10d, 2026-10-26).** Field size 5 is in the 4-9 band: research ALL actionable names, no cut. The screen, not a triage cut, made this field.

**Changes vs 2026-10-15:** BNY printed 2026-10-15 and leaves the field (past). VRT stays watchlist — its date was corrected in 2026-10-15 research/verification to 2026-10-28 BMO (screen 2026-10-21 unsupported), 12d out. CINF enters actionable at exactly 10d. Watchlist (44) plus BNY past = 45 non-actionable rows below.

Doctrine scoring (0-10, orchestrator): reaction record first (beat_up_rate, 40%), beat quality (beats/4 + surprise size, 25%), revenue underneath (TTM growth, 20%), priced-in inverse (ret_21d / run flag, 15%). Scores are triage heuristics, not panel scores.

## Unclosed prior earnings picks whose print already happened (no kind=close row)

Single picks with next_earnings before 2026-10-16 and no matching kind=close row in picks/ledger.csv: GS (picks 2026-09-21 and 2026-10-03, print 2026-10-13), PEP (picks 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-02, print 2026-10-08), BLK (picks 2026-10-04, 2026-10-05, 2026-10-07, 2026-10-08, 2026-10-09, 2026-10-11, print 2026-10-14), BAC (pick 2026-10-12, print 2026-10-14), BNY (picks 2026-10-06 and 2026-10-10, print 2026-10-15). FSLR (2026-09-17, print 2026-10-29) and CME (2026-10-13/14/15, print 2026-10-21) are not yet past. No close prices are fabricated here; these need owner close rows.

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | SNDK | 0.805 | DROP | 8.6 | WATCHLIST 13d to 2026-10-29; beat_up 0.67, avg_abs 7.8%, beats 4/4 avg +46.3%, rev TTM 81.9%, ret21 -8.3% |
| 2 | INCY | 0.782 | DROP | 7.5 | WATCHLIST 13d to 2026-10-29; beat_up 0.80, avg_abs 6.9%, beats 3/4 avg +27.8%, rev TTM 17.5%, ret21 -11.1% |
| 3 | APP | 0.766 | DROP | 8.2 | WATCHLIST 19d to 2026-11-04; beat_up 0.75, avg_abs 17.7%, beats 4/4 avg +4.1%, rev TTM 36.5%, ret21 -18.5% |
| 4 | OXY | 0.740 | DROP | 7.8 | WATCHLIST 24d to 2026-11-09; beat_up 0.88, avg_abs 4.6%, beats 4/4 avg +54.2%, rev TTM 10.3%, ret21 -0.2% |
| 5 | LLY | 0.734 | DROP | 8.8 | WATCHLIST 13d to 2026-10-29; beat_up 0.83, avg_abs 8.0%, beats 4/4 avg +20.4%, rev TTM 30.8%, ret21 +2.5% |
| 6 | STX | 0.733 | DROP | 7.2 | WATCHLIST 11d to 2026-10-27; beat_up 0.62, avg_abs 11.0%, beats 4/4 avg +11.8%, rev TTM 21.9%, ret21 -7.2% |
| 7 | CPAY | 0.704 | DROP | 7.2 | WATCHLIST 19d to 2026-11-04; beat_up 0.86, avg_abs 5.4%, beats 4/4 avg +3.8%, rev TTM 13.8%, ret21 -3.3% |
| 8 | APH | 0.694 | DROP | 8.7 | WATCHLIST 12d to 2026-10-28; beat_up 0.88, avg_abs 6.0%, beats 4/4 avg +11.2%, rev TTM 35.4%, ret21 +9.5% |
| 9 | BNY | 0.689 | DROP | 7.5 | DROP — PRINTED 2026-10-15, past; beat_up 0.88, avg_abs 3.0%, beats 4/4 avg +10.1%, rev TTM 10.2%, ret21 -10.5% |
| 10 | CAT | 0.687 | DROP | 7.5 | WATCHLIST 13d to 2026-10-29; beat_up 0.80, avg_abs 5.0%, beats 4/4 avg +17.5%, rev TTM 11.5%, ret21 -1.4% |
| 11 | HWM | 0.652 | DROP | 6.9 | WATCHLIST 13d to 2026-10-29; beat_up 0.75, avg_abs 5.9%, beats 4/4 avg +7.5%, rev TTM 12.9%, ret21 -4.5% |
| 12 | CBOE | 0.638 | DROP | 7.0 | WATCHLIST 14d to 2026-10-30; beat_up 0.86, avg_abs 3.6%, beats 4/4 avg +5.3%, rev TTM 10.4%, ret21 +2.7% |
| 13 | GRMN | 0.610 | DROP | 6.9 | WATCHLIST 12d to 2026-10-28; beat_up 0.83, avg_abs 11.4%, beats 3/4 avg +17.4%, rev TTM 8.9%, ret21 -1.4% |
| 14 | GOOGL | 0.604 | DROP | 7.0 | WATCHLIST 12d to 2026-10-28; beat_up 0.62, avg_abs 4.4%, beats 4/4 avg +84.9%, rev TTM 13.8%, ret21 +1.3% |
| 15 | REGN | 0.587 | DROP | 7.1 | WATCHLIST 14d to 2026-10-30; beat_up 0.71, avg_abs 6.1%, beats 4/4 avg +18.9%, rev TTM 8.5%, ret21 -5.1% |
| 16 | FTNT | 0.586 | DROP | 6.8 | WATCHLIST 12d to 2026-10-28; beat_up 0.62, avg_abs 9.6%, beats 4/4 avg +19.8%, rev TTM 13.7%, ret21 +12.1% |
| 17 | MNST | 0.580 | DROP | 6.1 | WATCHLIST 20d to 2026-11-05; beat_up 0.75, avg_abs 4.8%, beats 3/4 avg +4.2%, rev TTM 13.5%, ret21 -2.0% |
| 18 | MPWR | 0.578 | DROP | 7.0 | WATCHLIST 13d to 2026-10-29; beat_up 0.75, avg_abs 8.9%, beats 4/4 avg +4.4%, rev TTM 22.7%, ret21 +15.6% |
| 19 | IDXX | 0.566 | DROP | 6.5 | WATCHLIST 17d to 2026-11-02; beat_up 0.75, avg_abs 10.4%, beats 4/4 avg +5.8%, rev TTM 8.0%, ret21 +2.1% |
| 20 | DXCM | 0.558 | DROP | 6.5 | WATCHLIST 13d to 2026-10-29; beat_up 0.67, avg_abs 9.0%, beats 4/4 avg +11.5%, rev TTM 9.7%, ret21 +0.4% |
| 21 | FOXA | 0.557 | DROP | 7.1 | WATCHLIST 17d to 2026-11-02; beat_up 0.75, avg_abs 5.1%, beats 4/4 avg +40.4%, rev TTM 3.5%, ret21 -8.8% |
| 22 | FOX | 0.551 | DROP | 7.1 | WATCHLIST 17d to 2026-11-02; beat_up 0.75, avg_abs 5.3%, beats 4/4 avg +36.1%, rev TTM 3.5%, ret21 -8.5% |
| 23 | PH | 0.531 | DROP | 6.9 | WATCHLIST 20d to 2026-11-05; beat_up 0.88, avg_abs 4.4%, beats 4/4 avg +8.1%, rev TTM 5.7%, ret21 +2.6% |
| 24 | ISRG | 0.522 | KEEP | 6.6 | ACTIONABLE 4d to 2026-10-20; beat_up 0.62, avg_abs 6.7%, beats 4/4 avg +15.7%, rev TTM 13.7%, ret21 +11.7% |
| 25 | AME | 0.521 | DROP | 6.8 | WATCHLIST 13d to 2026-10-29; beat_up 0.88, avg_abs 4.1%, beats 4/4 avg +4.8%, rev TTM 7.7%, ret21 +7.4% |
| 26 | BMY | 0.520 | DROP | 6.2 | WATCHLIST 13d to 2026-10-29; beat_up 0.62, avg_abs 4.6%, beats 4/4 avg +12.8%, rev TTM 2.0%, ret21 -10.7% |
| 27 | VRT | 0.517 | DROP | 6.9 | WATCHLIST 12d to 2026-10-28 (corrected 2026-10-15); beat_up 0.62, avg_abs 9.6%, beats 4/4 avg +13.0%, rev TTM 17.6%, ret21 -0.0% |
| 28 | FFIV | 0.517 | DROP | 6.7 | WATCHLIST 11d to 2026-10-27; beat_up 0.75, avg_abs 7.0%, beats 4/4 avg +15.9%, rev TTM 7.2%, ret21 +15.7% |
| 29 | GOOG | 0.504 | DROP | 6.2 | WATCHLIST 12d to 2026-10-28; beat_up 0.71, avg_abs 4.3%, beats 3/4 avg +9.1%, rev TTM 13.8%, ret21 +1.1% |
| 30 | RL | 0.497 | DROP | 6.5 | WATCHLIST 20d to 2026-11-05; beat_up 0.75, avg_abs 6.2%, beats 4/4 avg +8.2%, rev TTM 9.4%, ret21 +9.8% |
| 31 | VEEV | 0.497 | DROP | 6.0 | WATCHLIST 40d to 2026-11-25; beat_up 0.62, avg_abs 9.1%, beats 4/4 avg +5.4%, rev TTM 12.9%, ret21 +13.5% |
| 32 | CINF | 0.493 | KEEP | 6.3 | ACTIONABLE 10d to 2026-10-26; beat_up 0.71, avg_abs 2.5%, beats 3/4 avg +10.5%, rev TTM 12.9%, ret21 -3.2% |
| 33 | V | 0.492 | DROP | 5.9 | WATCHLIST 11d to 2026-10-27; beat_up 0.62, avg_abs 2.7%, beats 4/4 avg +2.7%, rev TTM 11.2%, ret21 +5.5% |
| 34 | MA | 0.488 | DROP | 6.0 | WATCHLIST 13d to 2026-10-29; beat_up 0.62, avg_abs 2.6%, beats 4/4 avg +5.9%, rev TTM 10.3%, ret21 +5.4% |
| 35 | KO | 0.482 | DROP | 6.2 | WATCHLIST 11d to 2026-10-27; beat_up 0.75, avg_abs 2.9%, beats 4/4 avg +4.5%, rev TTM 5.0%, ret21 +1.5% |
| 36 | WST | 0.478 | DROP | 6.6 | WATCHLIST 13d to 2026-10-29; beat_up 0.62, avg_abs 14.3%, beats 4/4 avg +16.8%, rev TTM 9.6%, ret21 +4.7% |
| 37 | PM | 0.460 | KEEP | 5.6 | ACTIONABLE 5d to 2026-10-21; beat_up 0.71, avg_abs 5.9%, beats 3/4 avg +7.1%, rev TTM 6.2%, ret21 +3.2% |
| 38 | ADSK | 0.458 | DROP | 6.3 | WATCHLIST 42d to 2026-11-27; beat_up 0.62, avg_abs 4.9%, beats 4/4 avg +6.4%, rev TTM 13.1%, ret21 +0.7% |
| 39 | NSC | 0.453 | KEEP | 6.2 | ACTIONABLE 6d to 2026-10-22; beat_up 0.71, avg_abs 2.7%, beats 4/4 avg +7.9%, rev TTM 3.1%, ret21 +0.3% |
| 40 | CME | 0.453 | KEEP | 6.5 | ACTIONABLE 5d to 2026-10-21; beat_up 1.00, avg_abs 1.6%, beats 3/4 avg +1.4%, rev TTM 5.0%, ret21 -0.9% |
| 41 | AMGN | 0.448 | DROP | 6.0 | WATCHLIST 18d to 2026-11-03; beat_up 0.62, avg_abs 5.1%, beats 4/4 avg +11.1%, rev TTM 5.7%, ret21 +8.2% |
| 42 | EW | 0.435 | DROP | 5.2 | WATCHLIST 19d to 2026-11-04; beat_up 0.57, avg_abs 4.0%, beats 3/4 avg +4.7%, rev TTM 9.7%, ret21 -0.3% |
| 43 | COP | 0.430 | DROP | 5.3 | WATCHLIST 20d to 2026-11-05; beat_up 0.57, avg_abs 2.4%, beats 3/4 avg +6.8%, rev TTM 11.0%, ret21 +3.1% |
| 44 | BIIB | 0.427 | DROP | 6.8 | WATCHLIST 12d to 2026-10-28; beat_up 0.75, avg_abs 4.1%, beats 4/4 avg +36.3%, rev TTM 1.9%, ret21 +5.3% |
| 45 | ADP | 0.411 | DROP | 6.1 | WATCHLIST 12d to 2026-10-28; beat_up 0.75, avg_abs 3.1%, beats 4/4 avg +1.9%, rev TTM 4.7%, ret21 -0.3% |
| 46 | PFE | 0.408 | DROP | 6.7 | WATCHLIST 18d to 2026-11-03; beat_up 0.75, avg_abs 2.4%, beats 4/4 avg +17.6%, rev TTM 1.4%, ret21 +2.3% |
| 47 | PTC | 0.405 | DROP | 6.9 | WATCHLIST 26d to 2026-11-11; beat_up 0.75, avg_abs 5.3%, beats 4/4 avg +26.1%, rev TTM 7.8%, ret21 +41.9% |
| 48 | MLM | 0.394 | DROP | 5.6 | WATCHLIST 18d to 2026-11-03; beat_up 0.67, avg_abs 3.4%, beats 3/4 avg +2.0%, rev TTM 10.6%, ret21 -5.7% |
| 49 | EBAY | 0.376 | DROP | 5.9 | WATCHLIST 12d to 2026-10-28; beat_up 0.62, avg_abs 7.5%, beats 4/4 avg +4.4%, rev TTM 9.9%, ret21 +6.8% |
| 50 | A | 0.373 | DROP | 5.9 | WATCHLIST 40d to 2026-11-25; beat_up 0.86, avg_abs 4.7%, beats 3/4 avg +3.6%, rev TTM 6.4%, ret21 +17.1% |

Borderline flag: CINF at exactly 10d is the borderline actionable inclusion; VRT is borderline watchlist only because its verified date moved — if verification re-confirms 2026-10-21 it would re-enter, but the 2026-10-15 company-PR evidence says 2026-10-28.
