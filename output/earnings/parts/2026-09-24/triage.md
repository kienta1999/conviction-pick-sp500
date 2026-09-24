# Phase 1 triage — earnings mode — 2026-09-24

Fresh screen per the check's dated-input rule: `shortlist_2026-09-24.json` built 2026-09-24
08:26:19 UTC (~04:26 ET, before the US open; last completed market session Tuesday 9/23,
so price inputs are the same 9/23 closes). 50 candidates in the 45-day window.

## Funnel

| stage | in | out | dropped |
|---|---|---|---|
| 1 profitable | 503 | 399 | 104 |
| 2 US company | 399 | 399 | 0 (skipped in earnings mode — domicile does not affect a print) |
| 3 TTM rev growth > 0 | 399 | 364 | 35 |
| 4 leverage ok | 364 | 260 | 104 |
| 5 reports <= 45d | 260 | 221 | 39 |
| 5b mktcap >= $20B | 221 | 186 | 35 |
| 5c has >= 4q history | 186 | 186 | 0 |
| 5c misses < 2 of 4q | 186 | 165 | 21 |
| 5d beat->up rate > 50% | 165 | 89 | 76 |
| 6 op margin > sector med | 89 | 57 | 32 |
| 6b earnings quality | 57 | 55 | 2 |
| 7 0 < fwdPE < 60 | 55 | 54 | 1 |
| 8 niche leaders | 54 | 54 | 0 (skipped — size floor replaces leadership rule) |
| 9 trim to target | 54 | 50 | 4 (target 50) |

The reaction gate (5d) did the heaviest doctrinal work: 76 names whose own beats have not
historically been rewarded were removed — the priced-in print, measured rather than argued.
Stage 9 trimmed the field to 50; new entrants vs yesterday's screen include KO, CSX, ADP,
AMGN, EBAY, CAT, CBOE, CPAY and APP. PAYX and CTAS fell out (both printed 2026-09-23 —
they are last quarter's history, not next quarter's setup).

## Actionable now (reporting within ~10 days): NONE

No candidate reports within the ~10-day window. The two names nearest it reported
YESTERDAY, 2026-09-23, and are no longer in the field:

| ticker | note |
|---|---|
| PAYX | Reported 2026-09-23 BMO — print already happened. FQ1 FY27: EPS $1.34 vs $1.32–1.33 consensus (beat), revenue $1.63B in-line (not a beat), FY27 guide merely reaffirmed at midpoint (not raised/above consensus), first session closed −8.77% at $104.49. The 9/22-queued Plan B trigger required all three (EPS+revenue beat, raised/above-consensus guide, up first session) — it did NOT fire. Close row recorded today per the addendum: trigger never fired, exit_price = price_at_pick. No new tradeable window. |
| CTAS | Reported 2026-09-23 — print already happened. Runner-up on 9/22 with a backup Plan B trigger; it never became a pick, so no close row is owed. No tradeable window today. |

Per the skill's 0-candidate rule: report the funnel, show the next wave, and stop. No pick.
No panel vote — a 4-lens vote over already-printed names would be theater.

## Watchlist — next reporting wave

Next actionable wave starts 2026-10-08 (PEP, dte 14). The rest of the wave:

| # | ticker | composite | date | dte | beat_up | note |
|---|---|---|---|---|---|---|
| 1 | PEP | 0.373 | 2026-10-08 | 14 | 0.833 | Next actionable wave; best clean reaction record in the field |
| 2 | JPM | 0.407 | 2026-10-13 | 19 | 0.571 | LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags |
| 3 | GS | 0.769 | 2026-10-13 | 19 | 0.875 | Screen #1, IR-confirmed 10/13 BMO (9/21 verifier); Plan B queue material |
| 4 | FAST | 0.340 | 2026-10-14 | 20 | 0.667 | Thin surprises (mechanical beats) |
| 5 | BAC | 0.525 | 2026-10-14 | 20 | 0.750 | NII guide raised twice; RECEIVABLES_OUTRUN flag |
| 6 | MS | 0.710 | 2026-10-14 | 20 | 0.750 | 4/4 beats; LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags |
| 7 | BLK | 0.718 | 2026-10-14 | 20 | 0.875 | 4/4 beats all paid; LOW_CASH_CONVERSION flag; date needs IR confirmation (10/13 vs 10/14) |
| 8 | BNY | 0.666 | 2026-10-15 | 21 | 0.875 | Best fallback moat (custody oligopoly); LOW_CASH_CONVERSION flag |
| 9 | KO | 0.489 | 2026-10-20 | 26 | 0.750 | New entrant this screen |
| 10 | ISRG | 0.497 | 2026-10-20 | 26 | 0.625 | Nearest after the bank cluster |
| 11 | WAB | 0.319 | 2026-10-21 | 27 | 0.571 | Just above gate |
| 12 | CSX | 0.361 | 2026-10-21 | 27 | 0.600 | New entrant this screen |
| 13 | LVS | 0.366 | 2026-10-21 | 27 | 0.600 | RECEIVABLES_OUTRUN flag |
| 14 | CME | 0.424 | 2026-10-21 | 27 | 1.000 | Perfect beat_up on small sample; RECEIVABLES_OUTRUN flag |
| 15 | PM | 0.453 | 2026-10-21 | 27 | 0.714 | — |
| 16 | VRT | 0.512 | 2026-10-21 | 27 | 0.625 | INVENTORY_BUILD flag |
| 17 | UNP | 0.378 | 2026-10-22 | 28 | 0.600 | — |
| 18 | WST | 0.458 | 2026-10-22 | 28 | 0.625 | Largest gap risk in field (14.3% avg_abs per 9/22) |
| 19 | NSC | 0.491 | 2026-10-22 | 28 | 0.714 | — |
| 20 | CINF | 0.465 | 2026-10-26 | 32 | 0.714 | — |
| 21 | V | 0.502 | 2026-10-27 | 33 | 0.625 | Thin surprises (2.68%) |
| 22 | STX | 0.647 | 2026-10-27 | 33 | 0.625 | 10.98% avg_abs; RECEIVABLES_OUTRUN flag |
| 23 | INCY | 0.725 | 2026-10-27 | 33 | 0.800 | Largest accelerating surprises (+27.8%) |
| 24 | BSX | 0.363 | 2026-10-28 | 34 | 0.625 | Thin surprises |
| 25 | BIIB | 0.409 | 2026-10-28 | 34 | 0.750 | 36.3% surprises, RECEIVABLES_OUTRUN flag |
| 26 | ADP | 0.419 | 2026-10-28 | 34 | 0.750 | New entrant this screen |
| 27 | REGN | 0.546 | 2026-10-28 | 34 | 0.714 | No guide to miss; date 10/27 vs 10/28 conflict unresolved |
| 28 | GOOG | 0.572 | 2026-10-28 | 34 | 0.625 | HIGH_ACCRUALS flag |
| 29 | GOOGL | 0.577 | 2026-10-28 | 34 | 0.625 | Same print as GOOG, HIGH_ACCRUALS flag |
| 30 | APH | 0.680 | 2026-10-28 | 34 | 0.875 | 0.875 beat_up, clean compounder |
| 31 | TT | 0.371 | 2026-10-29 | 35 | 0.625 | — |
| 32 | EW | 0.401 | 2026-10-29 | 35 | 0.571 | Just above gate |
| 33 | BMY | 0.501 | 2026-10-29 | 35 | 0.625 | — |
| 34 | AME | 0.524 | 2026-10-29 | 35 | 0.875 | — |
| 35 | FOX | 0.541 | 2026-10-29 | 35 | 0.750 | RECEIVABLES_OUTRUN flag |
| 36 | FOXA | 0.548 | 2026-10-29 | 35 | 0.750 | RECEIVABLES_OUTRUN flag |
| 37 | DXCM | 0.568 | 2026-10-29 | 35 | 0.667 | — |
| 38 | MPWR | 0.590 | 2026-10-29 | 35 | 0.750 | Big avg_abs move (8.9%); RECEIVABLES_OUTRUN flag |
| 39 | CAT | 0.650 | 2026-10-29 | 35 | 0.800 | New entrant this screen |
| 40 | CBOE | 0.694 | 2026-10-30 | 36 | 0.857 | New entrant this screen |
| 41 | IDXX | 0.587 | 2026-11-02 | 39 | 0.750 | — |
| 42 | PFE | 0.386 | 2026-11-03 | 40 | 0.750 | — |
| 43 | AMGN | 0.510 | 2026-11-03 | 40 | 0.625 | New entrant this screen |
| 44 | EBAY | 0.359 | 2026-11-04 | 41 | 0.625 | New entrant this screen |
| 45 | FTNT | 0.547 | 2026-11-04 | 41 | 0.625 | 45x fwd, 9.6% avg_abs |
| 46 | CPAY | 0.681 | 2026-11-04 | 41 | 0.857 | New entrant this screen |
| 47 | APP | 0.689 | 2026-11-04 | 41 | 0.750 | New entrant this screen |
| 48 | COP | 0.441 | 2026-11-05 | 42 | 0.571 | 45-day edge of window |
| 49 | HWM | 0.671 | 2026-11-05 | 42 | 0.750 | Most derisked into print per 9/21 run |
| 50 | SNDK | 0.722 | 2026-11-06 | 43 | 0.667 | — |

All watchlist names are parked, not researched — they enter the queue when their dates
come within ~10 days. Next check: 2026-10-06 gives PEP (dte 2) a fresh research window.
