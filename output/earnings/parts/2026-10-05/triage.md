# Phase 1 triage — earnings mode, run 2026-10-05

Screen: `shortlist_2026-10-05.json` (generated 2026-10-05 08:22:01 local), 50 candidates
after the 45-day window funnel (503 -> 50). No gate widening; no names dropped on
transient cache issues — the refetch completed 503/503 on all five data types, so
the NaN-drop quirk did not trigger.

## Field split: actionable vs watchlist

Per the skill, the 45-day window is split on `days_to_earnings`:

- **Actionable now (<=10 days): 7 names.** The skill's field-size rule says
  4-9 candidates -> skip the cut, research ALL of them, and say so.
  The screen, not the panel, made this decision; a 4-lens vote over 7 names is
  the whole field, not theater. No watchlist names pulled forward.
- **Watchlist (reporting >10 days out): 43 names**, ranked and parked below
  with dates.

| # | ticker | composite | KEEP/DROP | days to print | doctrine score | one-line reason |
|---|--------|-----------|-----------|---------------|----------------|-----------------|
| 1 | GS | 0.840 | KEEP | 8 | 9 | 4/4 beats, +20.5% avg surprise, 88% beat->up (last4 +9,+2,+5,-2); cheap 12.4x fwd; reaction gate cleared. |
| 2 | MS | 0.732 | KEEP | 9 | 7 | 4/4 beats (+19%), 75% beat->up; BUT two eq flags (LOW_CASH_CONVERSION, RECEIVABLES_OUTRUN) need the benign-or-trap verdict in research. |
| 3 | BLK | 0.708 | KEEP | 9 | 9 | 4/4 beats, 88% beat->up, avg abs move 4.5%; quality compounder, rev accelerating (rev_q +30.6%). |
| 4 | BNY | 0.703 | KEEP | 10 | 8 | 4/4 beats, 88% beat->up, tiny 3.0% avg abs move = cheap setup; ret_21d -10.3% (no crowding). |
| 5 | BAC | 0.537 | KEEP | 9 | 7 | 4/4 beats, 75% beat->up, 10.2x fwd; banks cluster with GS/MS/BLK/BNY - sector read from bank prints matters (JPM not in field). |
| 6 | PEP | 0.386 | KEEP | 3 | 7 | Reports 2026-10-08 BMO - imminent; 3/4 beats, 83% beat->up, pred registered down -3% vs 4.2% avg abs (contrarian setup); also queued Plan B from prior runs. |
| 7 | FAST | 0.347 | KEEP | 9 | 6 | 3/4 beats (thin 0.07% avg surprise - managing the number), 67% beat->up, 36x fwd; weakest composite of the field but calendar-eligible. |

Watchlist (reporting beyond the actionable window), ordered by composite:

| ticker | days to print | date (screen) | one-line |
|--------|---------------|---------------|----------|
| INCY | 22 | 2026-10-27 | 3/4 beats but +27.8% avg surprise, 80% beat->up; biotech event vol (6.9% avg abs). |
| OXY | 35 | 2026-11-09 | 4/4 beats +54% avg surprise, 88% beat->up; commodity-exposed fallback. |
| SNDK | 24 | 2026-10-29 | 4/4 beats +46% surprise, rev +371% yoy (NAND cycle); 67% beat->up. |
| CPAY | 30 | 2026-11-04 | 4/4 beats, 86% beat->up; small-surprise (+3.8%) pattern. |
| APH | 23 | 2026-10-28 | 4/4 beats, 88% beat->up, rev +58% q; 26.5x fwd rich. |
| HWM | 24 | 2026-10-29 | 4/4 beats, 75% beat->up; aerospace cycle, 35.8x fwd. |
| CAT | 24 | 2026-10-29 | 4/4 beats +17.5%, 80% beat->up; industrial bellwether. |
| REGN | 25 | 2026-10-30 | 4/4 beats, 71% beat->up; rev_q +16.7%. |
| GOOGL | 23 | 2026-10-28 | 4/4 beats (+84.9% surprise), 62% beat->up; HIGH_ACCRUALS flag; megacap event. |
| FTNT | 23 | 2026-10-28 | 4/4 beats, 62% beat->up; run_into_print_flag TRUE (+17.1% ret_21d) - trap suspect. |
| GRMN | 23 | 2026-10-28 | 3/4 beats, 83% beat->up, 11.4% avg abs move - big vol name. |
| IDXX | 28 | 2026-11-02 | 4/4 beats, 75% beat->up, 10.4% avg abs. |
| MNST | 31 | 2026-11-05 | 3/4 beats, 75% beat->up; consumer staple-ish fallback. |
| FOXA | 24 | 2026-10-29 | 4/4 beats +40% surprise, 75% beat->up. |
| FOX | 24 | 2026-10-29 | dual-class twin of FOXA, same record. |
| V | 22 | 2026-10-27 | 4/4 beats, 62% beat->up; tiny 2.7% avg abs move. |
| MA | 24 | 2026-10-29 | 4/4 beats, 62% beat->up; tiny 2.6% avg abs move. |
| PH | 31 | 2026-11-05 | 4/4 beats, 88% beat->up; industrial compounder. |
| ISRG | 15 | 2026-10-20 | 4/4 beats +15.7%, 62% beat->up; moat name. |
| AME | 24 | 2026-10-29 | 4/4 beats, 88% beat->up; small moves (4.1% avg abs). |
| FFIV | 21 | 2026-10-26 | 4/4 beats, 75% beat->up; run_into_print_flag TRUE (+16.1%) - trap suspect. |
| RL | 31 | 2026-11-05 | 4/4 beats, 75% beat->up; consumer discretionary. |
| BMY | 24 | 2026-10-29 | 4/4 beats, 62% beat->up; pharma, 9.3x fwd. |
| VRT | 16 | 2026-10-21 | 4/4 beats, 62% beat->up; INVENTORY_BUILD flag; AI-datacenter levered. |
| KO | 22 | 2026-10-27 | 4/4 beats, 75% beat->up; 2.9% avg abs move. |
| GOOG | 23 | 2026-10-28 | GOOGL twin (class C), same profile. |
| WST | 17 | 2026-10-22 | 4/4 beats, 62% beat->up; 14.3% avg abs - huge vol. |
| COP | 31 | 2026-11-05 | 3/4 beats, 57% beat->up - near the reaction gate floor. |
| CME | 16 | 2026-10-21 | 3/4 beats, 100% beat->up but only 1.6% avg abs - micro moves. |
| NSC | 17 | 2026-10-22 | 4/4 beats, 71% beat->up; railroad. |
| PM | 16 | 2026-10-21 | 3/4 beats, 71% beat->up. |
| ADP | 23 | 2026-10-28 | 4/4 beats, 75% beat->up; tiny surprise (+1.95%). |
| EW | 24 | 2026-10-29 | 3/4 beats, 57% beat->up - near floor. |
| BIIB | 23 | 2026-10-28 | 4/4 beats, 75% beat->up; RECEIVABLES_OUTRUN flag. |
| PFE | 29 | 2026-11-03 | 4/4 beats, 75% beat->up, 9.6x fwd. |
| EBAY | 30 | 2026-11-04 | 4/4 beats, 62% beat->up; 7.5% avg abs. |
| LVS | 16 | 2026-10-21 | 3/4 beats, 60% beat->up; rev_q -0.7% decelerating. |
| UNP | 17 | 2026-10-22 | 3/4 beats, 60% beat->up. |
| BSX | 23 | 2026-10-28 | 4/4 beats, 62% beat->up; -59% off 52w high. |
| META | 23 | 2026-10-28 | 3/4 beats, 57% beat->up; run_into_print_flag TRUE (+22.9%) - trap suspect. |
| ODFL | 23 | 2026-10-28 | 4/4 beats, 57% beat->up - near floor. |
| TT | 24 | 2026-10-29 | 4/4 beats, 62% beat->up. |
| CSX | 16 | 2026-10-21 | 3/4 beats, 60% beat->up. |

Borderline notes: FAST is the weakest actionable name (0.347 composite, 3/4 beats,
0.07% avg surprise, 36x fwd) but the skill's 4-9 rule keeps it in the research
set; the panel may rank it last. MS kept despite two eq flags - screen passed it;
research must render the benign-vs-trap verdict per the protocol's flag rule.
GS/MS/BLK/BNY/BAC form a bank cluster reporting 10/13-10/15 - peer prints (esp.
bank peers already out) are the best guide read; research should use that.
