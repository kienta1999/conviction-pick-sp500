# Phase 1 triage — earnings mode — 2026-09-25

Fresh screen per the check's dated-input rule: `shortlist_2026-09-25.json` built 2026-09-25
08:36:17 UTC (~01:36 PDT, before the US open; last completed market session Thursday 9/24).
50 candidates in the 45-day window.

## Funnel (from screen output)

| stage | in | out | dropped |
|---|---|---|---|
| 6b earnings quality | 61 | 58 | 3 (LRCX: HIGH_ACCRUALS+RECEIVABLES_OUTRUN; WDC: HIGH_ACCRUALS+LOW_CASH_CONVERSION; CDNS: RECEIVABLES_OUTRUN+INVENTORY_BUILD) |
| 7 0<fwdPE<60 | 58 | 58 | 0 |
| 8 niche leaders | 58 | 58 | 0 (skipped — size floor replaces leadership rule) |
| 9 trim to target | 58 | 50 | 8 (top 50 by composite) |

New top-composite entrant vs 9/24 screen: LLY (#1, 0.759; 4/4 beats, +20.4% avg surprise,
beat_up_rate 0.833, dte 34). SNDK #2 (0.730) carries a `run_into_print_flag` (+18.4% over
21d). APP/CBOE/CPAY remain in the composite top 10 from yesterday.

## Actionable now (reporting within ~10 days): NONE

No candidate reports within the ~10-day window. Nearest to it:

| ticker | date | dte |
|---|---|---|
| PEP | 2026-10-08 | 13 |
| JPM | 2026-10-13 | 18 |
| MS / BLK / BAC / FAST | 2026-10-14 | 19 |
| BNY | 2026-10-15 | 20 |

Per the skill's 0-candidate rule: report the funnel, show the next wave, and stop. No pick.
No panel vote — a 4-lens vote over names 13+ days out with no actionable entry would be
theater, and the calendar, not the doctrine, made the decision. This matches the 9/23 and
9/24 runs (kind=pass both days).

## Watchlist — next reporting wave

Next actionable wave starts 2026-10-08 (PEP, dte 13). The wave queue in order:

| # | ticker | composite | date | dte | beat_up | note |
|---|---|---|---|---|---|---|
| 1 | PEP | 0.393 | 2026-10-08 | 13 | 0.833 | Next actionable wave; best clean reaction record in the field |
| 2 | JPM | 0.408 | 2026-10-13 | 18 | 0.571 | LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags per 9/24 |
| 3 | MS | 0.722 | 2026-10-14 | 19 | 0.750 | 4/4 beats; LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags |
| 4 | BLK | 0.721 | 2026-10-14 | 19 | 0.875 | 4/4 beats all paid; LOW_CASH_CONVERSION flag; date needs IR confirmation (10/13 vs 10/14) |
| 5 | BAC | 0.539 | 2026-10-14 | 19 | 0.750 | NII guide raised twice; RECEIVABLES_OUTRUN flag |
| 6 | FAST | 0.362 | 2026-10-14 | 19 | 0.667 | Thin surprises (mechanical beats) |
| 7 | BNY | 0.682 | 2026-10-15 | 20 | 0.875 | Best fallback moat (custody oligopoly); LOW_CASH_CONVERSION flag |
| 8 | GS | n/a (not in field) | 2026-10-13 per earnings-calendar feed | 18 | 0.875 (9/24) | 9/21 single-pick Plan B still queued (ledger row, IR-confirmed 10/13 BMO — no close owed yet). NOTE: GS was composite #1 on the 9/24 screen but is absent from the 9/25 field — the screen used the Yahoo info feed's `nextEarningsDate` (null as of the 9/25 fetch) rather than the earnings-calendar feed, which still shows `upcoming: ["2026-10-13"]` (fetched 2026-09-25 08:28). Feed quirk, not a moved date; flagged for the screen, does not affect the pass outcome (GS is not actionable at dte 18) or the open 9/21 pick.

All composites, dates and beat_up rates are from the 9/25 screen. All watchlist names are
parked, not researched — they enter the queue when their dates come within ~10 days. PEP
becomes actionable on the ~2026-09-28/29 screen (dte ~10).

## Close-row discipline (addendum §3)

Checked picks/ledger.csv before publishing: the 2026-09-22 PAYX single pick has its
kind=close row (recorded 2026-09-24, exit_reason=event_exit, trigger never fired). The
9/23 and 9/24 earnings rows were kind=pass (no close owed). The open single-pick rows are
9/21 GS (Plan B queued, print 2026-10-13) and 9/17 FSLR (Plan B queued, print 2026-10-29) —
both prints are in the future; no close rows owed. **No missing close rows.**
