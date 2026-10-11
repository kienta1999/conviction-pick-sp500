> Run by: Muse Spark (muse-spark) — full panel

# Triage — 2026-10-11 (earnings mode, full panel)

## Screen correction — 2026-10-11 08:41 UTC (orchestrator note)

The 2026-10-10 screen was initially reused per the 1-day cache rule, and this triage was written against it (8-name actionable field). During the run the coordinator rebuilt the screen so the run's dated inputs match RUN_DATE (per `scripts/check_run.py`, which fails when the newest shortlist/funnel is dated before the published run).

Two things changed on the rebuild:

1. **BNY was dropped at stage 1 ("profitable") with netIncomeToCommon=NaN / profitMargins=NaN — a DATA ERROR, not a doctrine cut.** The morning fetch had hit HTTP 401 (invalid crumb) errors that null-corrupted several cached info rows. A targeted `fetch.py --tickers BNY --refresh` restored the real values (net income $6.024B, profit margins 29.4%, price $142.71 — the Friday 10/09 close), and the screen re-run restored BNY to the actionable field. **Fix-the-run rule applied: the data was repaired, the screen was not overridden.**

2. **Five names rolled into the actionable window** as their reports crossed to dte=10: VRT, PM, CME, LVS, WAB (all 2026-10-21). This is the watchlist-queue design working: the screen promotes them, research and the panel now cover them.

**Corrected actionable field (13 names):** GS, MS, BLK, BNY, BAC, ISRG, JPM, FAST (researched in batches 1–3) + VRT, PM, CME, LVS, WAB (research batch 4). Skill rule for 10+ candidates: triage to ~12-15 — all 13 are kept; no cut.

New-name triage rows (doctrine score, one-line reason):

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|--------|-----------|-----------|---------------|-----------------|
| 9 | VRT | 0.537 | KEEP | 6 | 4/4 beats avg +13.0%, but beat_up only 62.5% and reaction worst −17.3% (last4 −17/+5/+24/+7) — gaps big both ways; INVENTORY_BUILD flag needs a narrative check; dist_52w −35.4% at 26.5× fwd |
| 10 | PM | 0.439 | KEEP | 5 | 3/4 beats avg +7.1%, beat_up 71.4%, last4 +3/+7/−1/−4; at the 52-week HIGH (dist 0.0%), ret_21d +6.9%, upside only +3.5% — the field's least-mispriced setup |
| 11 | CME | 0.429 | KEEP | 6 | beat_up 100.0% (the field's best reaction record) but surprises are tiny (+1.4% avg, 3/4 beats) — manages to the decimal; avg abs move only 1.6% (nothing to win); RECEIVABLES_OUTRUN flag |
| 12 | LVS | 0.360 | KEEP | 4 | 3/4 beats avg +8.5% but trend −18.9% (shrinking fast), beat_up 60.0%, last4 +2/−9/−14/+12, eps_yoy_q −25.3%, rev_yoy_q −0.7% — Macau hostage to policy; dist_52w −47.0%, +62.4% analyst upside (fallen angel) |
| 13 | WAB | 0.338 | KEEP | 5 | 4/4 beats avg +4.1% (widening +5.3), beat_up 57.1% (near coin flip), last4 +10/+3/+3/−2, rev accelerating (+17.5% yoy, accel +8.5%); freight/rail cyclicality is the print risk |

The panel ballots cast on the 8-name field are SUPERSEDED — all four lenses will be re-cast on the 13-name field off the same doctrine. Yesterday's (2026-10-10) run used the 8-name field; today's field is genuinely different (calendar rollover + data repair), so this run is not a duplicate-data consistency sample for the 8-name comparison.

Watchlist after promotion (still >10 days): CSX (2026-10-21, dte=11), CINF (2026-10-26), V/KO (2026-10-27), APH/GRMN/GOOGL/FTNT/GOOG/BIIB/ADP/META (2026-10-28), SNDK/INCY/LLY/CAT/HWM/MPWR/DXCM/AME/BMY/MA (2026-10-29), CBOE/REGN (2026-10-30), IDXX (2026-11-02), AMGN/PFE (2026-11-03), APP/CPAY/EW/EBAY (2026-11-04), MNST/PH/RL/COP (2026-11-05), OXY (2026-11-09), PTC (2026-11-11).

---

Shortlist source: `output/earnings/shortlist_2026-10-10.json` (generated 2026-10-10 08:31:37, <24h old — REUSED per the protocol's 1-day cache rule, not rebuilt). 50 candidates in the 45-day wave.

**Field split on days_to_earnings:** 8 names report within ~10 days (actionable now), 42 names further out (watchlist).

Skill rule for 4–9 actionable candidates: skip the cut, research ALL. Triage audited every name against the doctrine (below) but dropped none — "kept all 8, the field was the whole field."

Field composition vs 2026-10-10: IDENTICAL 8-name actionable set (GS, MS, BLK, BNY, BAC, ISRG, JPM, FAST), one day closer to their prints. Nothing rotated in or out; this is the duplicate-data consistency experiment working as designed.

Note on screen data quality: `ret_21d` / `run_into_print_flag` are stored inside each candidate's `print_reaction` block (top-level keys are null) — the values below are the real ones. `rev_yoy_q`/`rev_accel`/`eps_yoy_q` come from `earnings_trend`.

## Actionable now — research ALL (no triage cut)

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|--------|-----------|-----------|---------------|-----------------|
| 1 | GS | 0.781 | KEEP | 8 | 4/4 beats avg +20.5% (largest surprises, trend WIDENING +11.4), beat_up 87.5%, last4 +9/+2/+5/−2, ret_21d −12.2% (no run-up, 21.9% off high), fwd P/E 12.4; LOW_CASH_CONVERSION + RECEIVABLES_OUTRUN flags need a narrative check (bank accruals, likely benign) |
| 2 | MS | 0.718 | KEEP | 7 | 4/4 beats avg +18.4% but surprise trend SHRINKING (−5.2), beat_up 75%, last4 −4/+5/+6/+5 (most recent fell), rev +21.4% TTM and accelerating; eq flags need benign-model check |
| 3 | BLK | 0.696 | KEEP | 7 | 4/4 beats (small, +7.3% avg, trend widening), beat_up 87.5%, last4 all positive (+7/+3/+6/+3) — the field's cleanest reaction record; rev_yoy_q +30.6% with accel +13.8%; no quarterly EPS guide to beat-but-soft; picked 10/4, 10/5, 10/7, 10/8, 10/9 |
| 4 | BNY | 0.695 | KEEP | 7 | 4/4 beats avg +10.1% widening, beat_up 87.5%, last4 +5/+2/+2/−2, worst reaction only −2.0% (smallest gap risk), ret_21d −12.2% derisked; yesterday's pick |
| 5 | BAC | 0.537 | KEEP | 5 | 4/4 beats avg +7.7%, beat_up 75%, last4 +2/+2/−4/+4; weakest revenue engine (TTM +2.2%), avg abs move 2.5% — thin edge, honest low-conviction filler |
| 6 | ISRG | 0.499 | KEEP | 5 | 4/4 beats avg +15.7%, BUT beat_up only 62.5%, reaction worst −14.1% (avg abs 6.7%), last4 −14/+7/+0/+14 — gaps both ways; run_into_print_flag TRUE (+17.6%) at 35× fwd — the field's one priced-in-print suspect; trap case to resolve |
| 7 | JPM | 0.413 | KEEP | 4 | only 3/4 beats, beat_up 57.1% (barely above coin flip), last4 +2/−2/−4/−2 (fell on 3 of 4); rev accel +13.7% and 50.4% op margin are the only doctrine hooks; trap-fodder but researched honestly |
| 8 | FAST | 0.353 | KEEP | 4 | only 3/4 beats, surprise avg +0.07% (manages to the decimal), beat_up 66.7%, last4 −3/−7/+5/−8 (fell on 3 of 4); 36× fwd with −3.8% analyst downside — high valuation, weak record |

**Borderline note:** JPM and FAST have the thinnest doctrine cases (3/4 beats, sub-70% reaction records, tiny/absent surprises). They stay in the research set per the 4–9 rule, but the panel should treat them as the low-conviction tail unless research changes the picture. Sector concentration persists: 7 of 8 are financials (only ISRG, FAST outside).

**Field-level read for the panel:** with GS/JPM printing 10/13 BMO, MS/BLK/BAC/FAST printing 10/14, and BNY 10/15, the early prints are leading indicators for the later ones — the same-day-batch sequencing means a bad money-center morning should temper conviction in names that report after. Yesterday's run noted this too; the disqualifier checklist in the writeup must respect the sequencing.

## Watchlist — ranked, parked with dates (pre-vetted queue)

Reporting 2026-10-21 (d=11, just past the boundary — the 2026-10-12 screen may promote them): VRT (Vertiv), PM (Philip Morris), CME, CSX, LVS, WAB.

| date | ticker | company | composite |
|------|--------|---------|-----------|
| 2026-10-21 | VRT | Vertiv | 0.533 |
| 2026-10-21 | PM | Philip Morris International | 0.440 |
| 2026-10-21 | CME | CME Group | 0.432 |
| 2026-10-21 | CSX | CSX Corporation | 0.368 |
| 2026-10-21 | LVS | Las Vegas Sands | 0.364 |
| 2026-10-21 | WAB | Wabtec | 0.340 |
| 2026-10-26 | CINF | Cincinnati Financial | 0.488 |
| 2026-10-27 | V | Visa | 0.502 |
| 2026-10-27 | KO | Coca-Cola | 0.485 |
| 2026-10-28 | APH | Amphenol | 0.692 |
| 2026-10-28 | GRMN | Garmin | 0.593 |
| 2026-10-28 | GOOGL | Alphabet (A) | 0.569 |
| 2026-10-28 | FTNT | Fortinet | 0.559 |
| 2026-10-28 | GOOG | Alphabet (C) | 0.471 |
| 2026-10-28 | BIIB | Biogen | 0.429 |
| 2026-10-28 | ADP | ADP | 0.394 |
| 2026-10-28 | META | Meta | 0.359 |
| 2026-10-29 | SNDK | Sandisk | 0.805 |
| 2026-10-29 | INCY | Incyte | 0.771 |
| 2026-10-29 | LLY | Eli Lilly | 0.720 |
| 2026-10-29 | CAT | Caterpillar | 0.673 |
| 2026-10-29 | HWM | Howmet Aerospace | 0.635 |
| 2026-10-29 | MPWR | Monolithic Power Systems | 0.574 |
| 2026-10-29 | DXCM | Dexcom | 0.572 |
| 2026-10-29 | AME | Ametek | 0.520 |
| 2026-10-29 | BMY | Bristol Myers Squibb | 0.508 |
| 2026-10-29 | MA | Mastercard | 0.501 |
| 2026-10-30 | CBOE | Cboe Global Markets | 0.625 |
| 2026-10-30 | REGN | Regeneron | 0.572 |
| 2026-11-02 | IDXX | Idexx Laboratories | 0.557 |
| 2026-11-03 | AMGN | Amgen | 0.441 |
| 2026-11-03 | PFE | Pfizer | 0.401 |
| 2026-11-04 | APP | AppLovin | 0.763 |
| 2026-11-04 | CPAY | Corpay | 0.697 |
| 2026-11-04 | EW | Edwards Lifesciences | 0.442 |
| 2026-11-04 | EBAY | eBay | 0.379 |
| 2026-11-05 | MNST | Monster Beverage | 0.557 |
| 2026-11-05 | PH | Parker Hannifin | 0.534 |
| 2026-11-05 | RL | Ralph Lauren | 0.492 |
| 2026-11-05 | COP | ConocoPhillips | 0.468 |
| 2026-11-09 | OXY | Occidental Petroleum | 0.740 |
| 2026-11-11 | PTC | PTC | 0.397 |

Dates come from the cached screen (Yahoo-sourced) and are NOT yet confirmed against company IR pages — confirmation happens in Phase 2.
