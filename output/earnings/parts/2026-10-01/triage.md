> Run by: Muse AI (underlying model not recorded) — annotated 2026-10-06 from the owner's record, not by the run itself.

# Earnings triage — 2026-10-01 (RERUN under the updated protocol)

Rerun of the 2026-10-01 earnings screen/triage after the protocol update
(commit f98f9e4: screen now logs drops — `drops_2026-10-01.csv`, 453 dropped
names with stage + reason — and `scripts/why.py`). Full fresh fetch (503/503)
+ screen, generated 2026-10-01 22:13 PDT. This file overwrites the morning
run's triage in place.

**Change vs this morning:** the morning screen (stale/partial cache) had PEP
*absent* — it passed every gate but ranked 75th of 98 by composite and was
trimmed at the final stage, leaving 0 names inside the actionable window and
a legitimate PASS. After tonight's full data refresh PEP survives the funnel
(rank 47/50, composite 0.381) and is the **only name inside the ~10-day
actionable window** (reports Thu 2026-10-08, dte 7). The outcome therefore
changes from PASS to a single-name evaluation of PEP.

**Field:** 50 candidates (funnel: 503 → 419 profitable → 380 rev-growth →
274 leverage → 232 ≤45d → 192 ≥$20B → 175 misses<2 → 98 beat→up>50% → 65
margin → 63 EQ → 62 fwdPE → 50 final). **Actionable now (dte ≤ ~10): PEP
only.** Watchlist: the other 49, parked below in composite order with dates.

**Field-size rule (skill):** with 1 actionable name the screen, not a panel,
makes the decision — a 4-lens vote over one name is theater. Per the 9/28–9/30
precedent: research + independent verification on PEP only; no panel. The
watchlist order is the screen's composite, a pre-vetted queue, not a vote.

**Close-row check (addendum §3):** prior earnings singles — FSLR (10/29), GS
(10/13), PEP (10/08) prints all still future; PAYX already closed 2026-09-23.
No missing close rows.

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|--------|-----------|-----------|----------------|-----------------|
| 1 | GS | 0.838 | DROP (watchlist) | 8 | Best record in the field (4/4, +20.5% avg surprise, bu 88%) but dte 12 — first in the queue, reports 10/13 |
| 2 | APP | 0.758 | DROP (watchlist) | 6 | 4/4 and rev +53%, but 17.7% avg abs move is a lottery ticket, not an event edge; dte 34 |
| 3 | INCY | 0.732 | DROP (watchlist) | 7 | Huge avg surprise (+27.8%), bu 80%, rev accelerating; dte 26 |
| 4 | MS | 0.731 | DROP (watchlist) | 7 | 4/4, +18.4% surprises, sold off −11.8% into the print; dte 13 |
| 5 | LLY | 0.730 | DROP (watchlist) | 7 | 4/4, bu 83%, rev +48%; 8.0% abs move is the cost of being wrong; dte 28 |
| 6 | SNDK | 0.725 | DROP (watchlist) | 5 | Run-into-print flag TRUE (+16.3% in 21d) — the trap is live; dte 28 |
| 7 | BLK | 0.703 | DROP (watchlist) | 7 | 4/4, bu 88%, modest 4.5% abs move; dte 13 |
| 8 | CBOE | 0.695 | DROP (watchlist) | 7 | 4/4, bu 86%, smallest far-name abs move (3.6%); dte 29 |
| 9 | APH | 0.692 | DROP (watchlist) | 7 | 4/4, bu 88%, rev +58% accelerating; dte 27 |
| 10 | BNY | 0.690 | DROP (watchlist) | 7 | 4/4, bu 88%, quiet 3.0% abs move; dte 14 |
| 11 | CPAY | 0.670 | DROP (watchlist) | 6 | 4/4, bu 86%, small surprises (+3.8%); dte 34 |
| 12 | STX | 0.654 | DROP (watchlist) | 5 | Run-into-print flag TRUE (+15.9%), 11.0% abs move; dte 26 |
| 13 | CAT | 0.635 | DROP (watchlist) | 6 | 4/4, +17.5% surprises; 25.5× fwd P/E is rich for the record; dte 28 |
| 14 | REGN | 0.596 | DROP (watchlist) | 6 | 4/4, +18.9% surprises, cheap 12.1×; bu only 71%; dte 29 |
| 15 | MNST | 0.592 | DROP (watchlist) | 5 | 3/4 beats, thin +4.2% surprises, 31.8× fwd; dte 35 |
| 16 | MPWR | 0.591 | DROP (watchlist) | 5 | Rev +48% but 38.6× fwd and 8.9% abs move; dte 28 |
| 17 | IDXX | 0.581 | DROP (watchlist) | 5 | 10.4% abs move against +5.8% avg surprise — bad ratio; dte 32 |
| 18 | GOOGL | 0.573 | DROP (watchlist) | 6 | 4/4 with outsized surprises; bu only 62%; dte 27 |
| 19 | FTNT | 0.571 | DROP (watchlist) | 5 | 47.3× fwd, 9.6% abs move, bu 62%; dte 34 |
| 20 | DXCM | 0.569 | DROP (watchlist) | 5 | 9.0% abs move, rev growth fading (+13%, accel +2.8); dte 28 |
| 21 | GRMN | 0.565 | DROP (watchlist) | 5 | bu 83% but 11.4% abs move — the bet is bigger than the edge; dte 27 |
| 22 | FOXA | 0.552 | DROP (watchlist) | 6 | 4/4, +40% avg surprise (low-bar name), cheap 10.5×; dte 28 |
| 23 | FOX | 0.547 | DROP (watchlist) | 6 | Same story as FOXA, 9.6×; dte 28 |
| 24 | BAC | 0.546 | DROP (watchlist) | 6 | 4/4, bu 75%, tiny 2.5% abs move; dte 13 |
| 25 | PH | 0.534 | DROP (watchlist) | 6 | 4/4, bu 88%, steady; rev growth only +9.8%; dte 35 |
| 26 | MA | 0.534 | DROP (watchlist) | 5 | bu 62%, 2.6% abs move — priced for perfection at 24×; dte 28 |
| 27 | FFIV | 0.522 | DROP (watchlist) | 5 | +12.1% run into print (near flag), bu 75%; dte 25 |
| 28 | AME | 0.521 | DROP (watchlist) | 6 | 4/4, bu 88%, small clean record; dte 28 |
| 29 | V | 0.520 | DROP (watchlist) | 5 | Managed +2.7% surprises, bu 62%; dte 26 |
| 30 | ISRG | 0.514 | DROP (watchlist) | 5 | bu 62%, 33.6× fwd; dte 19 |
| 31 | AMGN | 0.513 | DROP (watchlist) | 5 | bu 62%, rev +9.5% only; dte 33 |
| 32 | BMY | 0.513 | DROP (watchlist) | 5 | Cheap 9.4× but rev +5.7%, bu 62%; dte 28 |
| 33 | VRT | 0.512 | DROP (watchlist) | 5 | 9.6% abs move, bu 62%; dte 20 |
| 34 | KO | 0.489 | DROP (watchlist) | 5 | 4/4 but +4.5% surprises at 24.4× — a hold, not an event; dte 26 |
| 35 | COP | 0.473 | DROP (watchlist) | 4 | bu 57% barely cleared the coin flip; 3/4 beats; dte 35 |
| 36 | CME | 0.473 | DROP (watchlist) | 4 | bu 100% but on +1.4% surprises and 1.6% moves — no event to trade; rev decelerating; dte 20 |
| 37 | GOOG | 0.473 | DROP (watchlist) | 5 | Duplicate class of GOOGL with a weaker record (3/4); dte 27 |
| 38 | WST | 0.471 | DROP (watchlist) | 4 | 14.3% abs move at 36.6× — variance, not edge; dte 21 |
| 39 | PM | 0.468 | DROP (watchlist) | 5 | 3/4, bu 71%, mid record; dte 20 |
| 40 | CINF | 0.468 | DROP (watchlist) | 4 | 3/4, rev decelerating (accel −1.8); dte 25 |
| 41 | BIIB | 0.429 | DROP (watchlist) | 4 | Big surprises off a low bar, rev +3.4% — beats manufactured by the bar; dte 27 |
| 42 | ADP | 0.425 | DROP (watchlist) | 4 | +1.9% avg surprise — manages the number to the decimal; dte 27 |
| 43 | EW | 0.420 | DROP (watchlist) | 4 | bu 57%, 3/4 — weakest reaction record in the field; dte 28 |
| 44 | PFE | 0.413 | DROP (watchlist) | 4 | Rev +2.6%, beats against a lowered bar; dte 33 |
| 45 | EBAY | 0.393 | DROP (watchlist) | 4 | bu 62%, 7.5% abs move; dte 34 |
| 46 | MLM | 0.392 | DROP (watchlist) | 4 | 3/4, +2.0% surprises; dte 33 |
| 47 | PEP | 0.381 | **KEEP** | 6 | **Only actionable name (10/08, dte 7).** bu 83% (5 of 6 measured beats rose), abs move 4.2%, down −9.2% into the print and −24% off the high — nothing priced in; but beats are thin (+1.4% avg) and the last-4 record is 3/4 with one miss, and the most recent print fell −3% on guide fear — the guide, not the beat, decides this one. Plan B by construction |
| 48 | UNP | 0.372 | DROP (watchlist) | 4 | bu 60%, +2.5% surprises; dte 21 |
| 49 | LVS | 0.367 | DROP (watchlist) | 3 | Revenue shrinking (revq −0.7%, accel −9.7) — a beat here would be manufactured; dte 20 |
| 50 | BSX | 0.362 | DROP (watchlist) | 4 | Rev accel negative (−1.6); dte 27 |

Borderline flag: **GS (dte 12)** misses the actionable window by two days and
has the field's best record — if the window were 12 days it would displace the
research budget. It stays watchlist per the ~10-day rule; its date enters the
window on the 2026-10-03 run.
