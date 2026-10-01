# Phase 1 triage — earnings mode — 2026-10-01

Screen built FRESH for this run: `shortlist_2026-10-01.json`
(generated 2026-10-01 08:22:43 UTC; `fetch.py` + `screen.py --mode earnings`
both ran this morning). 50 candidates in the 45-day window. No prior-day
screen reused.

## Funnel (from `funnel_2026-10-01.json`)

| stage | in | out | dropped |
|---|---|---|---|
| 1 profitable | 503 | 419 | 84 |
| 2 US company | 419 | 419 | 0 (n/a in earnings mode) |
| 3 TTM rev growth>0 | 419 | 380 | 39 |
| 4 leverage ok | 380 | 274 | 106 |
| 5 reports <=45d | 274 | 233 | 41 |
| 5b mktcap>=$20B | 233 | 193 | 40 |
| 5c has >=4q history | 193 | 193 | 0 |
| 5c misses<2 of 4q | 193 | 176 | 17 |
| 5d beat->up rate>50% | 176 | 98 | 78 |
| 6 op margin>sector med | 98 | 66 | 32 |
| 6b earnings quality | 66 | 64 | 2 |
| 7 0<fwdPE<60 | 64 | 63 | 1 |
| 8 niche leaders | 63 | 63 | 0 (n/a in earnings mode) |
| 9 trim to target | 63 | 50 | 13 (top 50 by composite) |

Top of field by composite: GS (0.840), MS (0.733), SNDK (0.730), INCY (0.729),
APP (0.728). No name carries the `run_into_print_flag` this run.

Note on PEP (the 9/28, 9/29 and 9/30 single pick, reporting 2026-10-08): it is
NOT in today's 50. Traced through the stage masks — PEP passes every gate
(profitable, rev growth +3.7% TTM, leverage 2.25x, dte 7, mktcap $175B,
3/4 beats, beat_up 0.875, op margin above sector median, 0 quality flags,
fwdPE 14.4) but ranks 75th of 98 by composite (0.394 — thin mechanical
surprises) and was cut at stage 9's trim to 50. The screen is working as
designed; no gate was widened or narrowed to include or exclude it.

## Actionable now (reporting within ~10 days): NONE

No candidate reports within the ~10-day window. Nearest to it:

| ticker | date | dte |
|---|---|---|
| GS | 2026-10-13 | 12 |
| MS / BLK / BAC / STT | 2026-10-14 | 13 |
| BNY | 2026-10-15 | 14 |
| ISRG | 2026-10-20 | 19 |

Per the skill's 0-candidate rule: report the funnel, show the next wave, and
stop. No pick. No panel vote — a 4-lens vote over names 12+ days out with no
actionable entry would be theater, and widening the ~10-day window to catch GS
at dte 12 would be widening a gate to manufacture a field, which the skill
forbids. This matches the 9/23, 9/24, 9/25 and 9/26 runs (kind=pass all four).

## Watchlist — next reporting wave

Next actionable wave starts 2026-10-13 (GS, dte 12 — becomes actionable on the
~2026-10-03 screen). The wave queue in date order (top 14):

| # | ticker | composite | date | dte | beat_up | note |
|---|---|---|---|---|---|---|
| 1 | GS | 0.840 | 2026-10-13 | 12 | 0.875 | Top composite in field; 9/21 Plan B queue stands; LOW_CASH_CONVERSION flag |
| 2 | MS | 0.733 | 2026-10-14 | 13 | 0.750 | LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags |
| 3 | BLK | 0.721 | 2026-10-14 | 13 | 0.875 | 4/4 beats all paid; LOW_CASH_CONVERSION flag |
| 4 | BAC | 0.544 | 2026-10-14 | 13 | 0.750 | RECEIVABLES_OUTRUN flag |
| 5 | STT | 0.410 | 2026-10-14 | 13 | 0.571 | Weakest reaction record of the bank cluster |
| 6 | BNY | 0.690 | 2026-10-15 | 14 | 0.875 | Best fallback moat (custody oligopoly); LOW_CASH_CONVERSION flag |
| 7 | ISRG | 0.517 | 2026-10-20 | 19 | 0.625 | Beat_up barely above the gate |
| 8 | VRT | 0.514 | 2026-10-21 | 20 | 0.625 | INVENTORY_BUILD flag; 9.6% avg abs move — wide instrument |
| 9 | CME | 0.471 | 2026-10-21 | 20 | 1.000 | Perfect reaction record but only 1.6% avg abs move — tiny edge to harvest |
| 10 | PM | 0.463 | 2026-10-21 | 20 | 0.714 | — |
| 11 | CSX | 0.378 | 2026-10-21 | 20 | 0.600 | — |
| 12 | WST | 0.465 | 2026-10-22 | 21 | 0.625 | 14.3% avg abs move — the gap underwritten is large |
| 13 | UNP | 0.398 | 2026-10-22 | 21 | 0.600 | — |
| 14 | FFIV | 0.520 | 2026-10-26 | 25 | 0.750 | — |

All composites, dates and beat_up rates are from the fresh 10/01 screen. All
watchlist names are parked, not researched — they enter the queue when their
dates come within ~10 days. The remaining 36 names (dte 25–35, reporting
2026-10-26 through 2026-11-05) are in `shortlist_2026-10-01.json`.

## Close-row discipline (addendum §3)

Checked picks/ledger.csv before publishing. Open earnings rows:
- 2026-09-17 FSLR single pick (Plan B queued; print 2026-10-29 — future, no close owed).
- 2026-09-21 GS single pick (Plan B queued; print 2026-10-13 — future, no close owed).
- 2026-09-22 PAYX single pick — kind=close row already recorded 2026-09-24 (event_exit, trigger never fired).
- 2026-09-28 / 09-29 / 09-30 PEP single picks (Plan B; print 2026-10-08 — future, no close owed).
- 2026-09-23 / 09-24 / 09-25 / 09-26 were kind=pass rows (no close owed).

**No missing close rows.** (The 9/17 CTAS/PAYX rank10 rows noted on 9/30 are
ranked-mode rows, not single picks; the addendum's mandatory close discipline
covers single picks.)
