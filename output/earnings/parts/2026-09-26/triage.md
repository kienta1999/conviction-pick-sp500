# Phase 1 triage — earnings mode — 2026-09-26

Screen reused per the protocol's 1-day cache check: `shortlist_2026-09-25.json`
(generated 2026-09-25 08:36:17 UTC; ~23.8h old, inside the 24h freshness window).
50 candidates in the 45-day window. Dates below are computed off today's run
date (2026-09-26); the screen's `days_to_earnings` was built 9/25, so each is
one day lower.

## Funnel (from `funnel_2026-09-25.json`, same screen as yesterday)

| stage | in | out | dropped |
|---|---|---|---|
| 1 profitable | 503 | 428 | 75 |
| 2 US company | 428 | 428 | 0 (n/a in earnings mode) |
| 3 TTM rev growth>0 | 428 | 388 | 40 |
| 4 leverage ok | 388 | 276 | 112 |
| 5 reports <=45d | 276 | 235 | 41 |
| 5b mktcap>=$20B | 235 | 197 | 38 |
| 5c misses<2 of 4q | 197 | 175 | 22 |
| 5d beat->up rate>50% | 175 | 94 | 81 |
| 6 op margin>sector med | 94 | 61 | 33 |
| 6b earnings quality | 61 | 58 | 3 (LRCX, WDC, CDNS — accrual/receivable flags) |
| 7 0<fwdPE<60 | 58 | 58 | 0 |
| 9 trim to target | 58 | 50 | 8 (top 50 by composite) |

Top of field by composite: LLY (0.759), SNDK (0.730), INCY (0.729), MS (0.722),
BLK (0.721). SNDK still carries the `run_into_print_flag` (+18.4% over 21d).

## Actionable now (reporting within ~10 days): NONE

No candidate reports within the ~10-day window. Nearest to it:

| ticker | date | dte (from 9/26) |
|---|---|---|
| PEP | 2026-10-08 | 12 |
| JPM | 2026-10-13 | 17 |
| MS / BLK / BAC / FAST | 2026-10-14 | 18 |
| BNY | 2026-10-15 | 19 |

Per the skill's 0-candidate rule: report the funnel, show the next wave, and
stop. No pick. No panel vote — a 4-lens vote over names 12+ days out with no
actionable entry would be theater, and the calendar, not the doctrine, made
the decision. This matches the 9/23, 9/24 and 9/25 runs (kind=pass all three).

## Watchlist — next reporting wave

Next actionable wave starts 2026-10-08 (PEP, dte 12). The wave queue in order:

| # | ticker | composite | date | dte | beat_up | note |
|---|---|---|---|---|---|---|
| 1 | PEP | 0.393 | 2026-10-08 | 12 | 0.833 | Next actionable wave; best clean reaction record in the field |
| 2 | JPM | 0.408 | 2026-10-13 | 17 | 0.571 | LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags per 9/24 |
| 3 | MS | 0.722 | 2026-10-14 | 18 | 0.750 | 4/4 beats; LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags |
| 4 | BLK | 0.721 | 2026-10-14 | 18 | 0.875 | 4/4 beats all paid; LOW_CASH_CONVERSION flag; date needs IR confirmation (10/13 vs 10/14) |
| 5 | BAC | 0.539 | 2026-10-14 | 18 | 0.750 | NII guide raised twice; RECEIVABLES_OUTRUN flag |
| 6 | FAST | 0.362 | 2026-10-14 | 18 | 0.667 | Thin surprises (mechanical beats) |
| 7 | BNY | 0.682 | 2026-10-15 | 19 | 0.875 | Best fallback moat (custody oligopoly); LOW_CASH_CONVERSION flag |

All composites, dates and beat_up rates are from the reused 9/25 screen. All
watchlist names are parked, not researched — they enter the queue when their
dates come within ~10 days. PEP becomes actionable on the ~2026-09-28/29 screen
(dte ~10).

## Close-row discipline (addendum §3)

Checked picks/ledger.csv before publishing. Open earnings rows:
- 2026-09-17 FSLR single pick (Plan B queued; print 2026-10-29 — future, no close owed).
- 2026-09-21 GS single pick (Plan B queued; print 2026-10-13 — future, no close owed).
- 2026-09-22 PAYX single pick — kind=close row already recorded 2026-09-24 (event_exit, trigger never fired).
- 2026-09-23 / 09-24 / 09-25 were kind=pass rows (no close owed).

**No missing close rows.**
