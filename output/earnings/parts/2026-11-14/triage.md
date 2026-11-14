> Run by: Muse Spark (unknown) — full panel

# TRIAGE — earnings 2026-11-14 (full panel)

Screen: `output/earnings/shortlist_2026-11-14.json` (generated 2026-11-14 09:27:55, fresh rebuild — fetch + screen run this morning). Field: **6 names**. Funnel: 503 → 414 profitable → 374 rev growth → 277 leverage → 43 report ≤45d → 37 mktcap ≥\$20B → 36 misses<2 → **15 reaction gate** (21 dropped, incl. AVGO, WMT, PANW, CRWD, DIS, ADI, CRM, ACN, MRVL, MDT, ADBE, INTU, TGT, KEYS, WDAY, CIEN, P, WSM, HPQ, BBY) → **6 op margin > sector median** (9 dropped).

## Split: actionable now vs watchlist

**Actionable now (reporting within ~10 days): exactly ONE name — A (Nov 23, 9 days).** The screen, not the panel, made this decision: the calendar plus the gates left a single near-term print. A 4-lens vote over one actionable name is theater on the entry question, so this is stated plainly. Per the daily-run convention (same as 2026-11-06, when OXY was the only actionable name, and 2026-11-13, when A and ADSK were actionable), the panel still researches and ranks the **whole 6-name field** — the 45-day screen exists to build the queue, and the pick is the best event trade among the screened six, Plan B by default. The pick is NOT forced to be the actionable name; if the panel's Borda #1 is a watchlist name, that is the panel's call and the writeup will say so.

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | MU | 0.748 | KEEP (watchlist) | 3/10 | Highest composite but reaction record UNJUDGEABLE — price cache corrupt, no price, no reaction history; Dec 23 is 39 days out; cannot score the doctrine's central question |
| 2 | NTAP | 0.740 | KEEP (watchlist) | 7/10 | 4/4 beats avg +10.1%, surprise trend +8.6, beat-up 0.571, last four +3/+22/−3/+2%; Dec 1 (17d) is the nearest watchlist date; INVENTORY_BUILD flag to explain |
| 3 | A | 0.602 | KEEP (actionable) | 8/10 | THE actionable name — Nov 23 AMC, 9 days; best reaction record in the field (beat-up 0.857, avg +2.5%, worst −5.5%); beats small (+3.6% avg) and FY27 guide is the event; RECEIVABLES_OUTRUN flag |
| 4 | PAYX | 0.542 | KEEP (watchlist) | 4/10 | 4/4 beats but thin (+1.8% avg), avg reaction NEGATIVE (−1.4%), last print −9% on beat-plus-reaffirm; Dec 18 (34d); RECEIVABLES_OUTRUN flag |
| 5 | CTAS | 0.520 | KEEP (watchlist) | 6/10 | Best business in the field (4/4 raises, revenue +10.9% accelerating) at the worst price (36.7x fwd, target below price, FTC/UniFirst binary Dec 11–17); Dec 17 (33d) |
| 6 | AZO | 0.258 | KEEP (watchlist) | 3/10 | Cheapest (17.0x fwd) but beat-up 0.333 on only 3 measured beats — NOT judgeable; four straight revenue misses, last four reactions +3/−9/−6/−7%; Dec 8 (24d) |

No triage cut: 6 names, research all. No high-composite name dropped — the field IS the shortlist.

## Data-integrity flags (NOT re-added — the panel ranks only the screened set)

- **ADSK and VEEV dropped at stage 1 "profitable" on a Yahoo data failure, not a thesis change.** `uv run python scripts/why.py ADSK --mode earnings` → "dropped at 1 profitable: netIncomeToCommon=NaN; profitMargins=NaN"; same for VEEV. Their info caches written this morning carry marketCap but profitMargins=None / netIncomeToCommon=None. Yesterday's pick (ADSK @ \$260.01, Plan B, print Nov 24) and yesterday's #2 (VEEV) are therefore ABSENT from today's field. Do not override the screen — but this is a data artifact the owner should know about, and a re-fetch that returns the fields would re-admit both.
- **MU's price cache is corrupt.** `data/prices/MU.parquet` (written 09:24, 41,321 bytes) fails to deserialize ("Couldn't deserialize thrift: TProtocolException"). Hence MU has price=None, no dist_sma200/dist_52w_high/ret_12m/ret_21d, and print_reaction note "no price history cached". Its 3.49x forward P/E and 133% TTM revenue growth are also cache-derived and should be treated with suspicion until the price file is repaired. Three fetch.py processes (dip/momentum/earnings coordinators) wrote the same cache files concurrently this morning — a likely race. MU's reaction record is unjudgeable; the panel must say so, not quote a rate.
- **ret_21d is None at the top level for A, PAYX, CTAS, AZO, NTAP** in shortlist.json; use each name's `print_reaction.ret_21d` instead (NTAP −15.5%, A −0.9%, PAYX +5.5%, CTAS +6.4%, AZO +6.5%). No run_into_print_flag is set anywhere in the field.

## Watchlist (reporting beyond the actionable window)

| Ticker | Report date | Days | One line |
|---|---|---|---|
| NTAP | Dec 1, 2026 | 17 | Nearest watchlist date; strongest beat record after A |
| AZO | Dec 8, 2026 | 24 | Cheap, washed-out, revenue misses every print |
| CTAS | Dec 17, 2026 | 33 | Best business, worst price; FTC binary lands Dec 11–17 |
| PAYX | Dec 18, 2026 | 34 | Lowest bar; only acceleration or a raise moves it |
| MU | Dec 23, 2026 | 39 | Unjudgeable on reactions until the price cache is repaired |

## Yesterday (2026-11-13) for comparison

Pick ADSK @ \$260.01, Plan B, print Nov 24 AMC; Borda #1 ADSK 40 unanimous; top-6 overlap 6/6 vs 11-12. Today ADSK and VEEV are out of the field on the stage-1 data failure above, so overlap vs yesterday will be at most 4/6 (A, PAYX, CTAS, AZO survive; NTAP and MU are new to the field vs yesterday's six).
