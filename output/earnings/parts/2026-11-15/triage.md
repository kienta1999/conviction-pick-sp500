> Run by: Muse Spark (unknown) — full panel

# TRIAGE — earnings 2026-11-15 (full panel)

Screen: `output/earnings/shortlist_2026-11-14.json` (generated 2026-11-14 09:27:55, <24h old — fresh per protocol Phase 0, reused; no market session since, Nov 14–15 is a weekend). Field: **6 names**. Funnel (from 2026-11-14 triage, same screen): 503 → 414 profitable → 374 rev growth → 277 leverage → 43 report ≤45d → 37 mktcap ≥$20B → 36 misses<2 → **15 reaction gate** (21 dropped, incl. AVGO, WMT, PANW, CRWD, DIS, ADI, CRM, ACN, MRVL, MDT, ADBE, INTU, TGT, KEYS, WDAY, CIEN, P, WSM, HPQ, BBY) → **6 op margin > sector median** (9 dropped).

## Split: actionable now vs watchlist

**Actionable now (reporting within ~10 days): exactly ONE name — A (Nov 23, 8 days from today).** The screen, not the panel, made this decision: the calendar plus the gates left a single near-term print. A 4-lens vote over one actionable name is theater on the entry question, so this is stated plainly. Per the daily-run convention (same as 2026-11-06, when OXY was the only actionable name, and 2026-11-13/11-14, when A was the only actionable name), the panel still researches and ranks the **whole 6-name field** — the 45-day screen exists to build the queue, and the pick is the best event trade among the screened six, Plan B by default. The pick is NOT forced to be the actionable name; if the panel's Borda #1 is a watchlist name, that is the panel's call and the writeup will say so.

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | MU | 0.748 | KEEP (watchlist) | 3/10 | Highest composite but reaction record UNJUDGEABLE — price cache corrupt, no price, no reaction history; Dec 23 is 38 days out; cannot score the doctrine's central question |
| 2 | NTAP | 0.740 | KEEP (watchlist) | 7/10 | 4/4 beats avg +10.1%, surprise trend +8.6, beat-up 0.571, last four +3/+22/−3/+2%; Dec 1 (16d) is the nearest watchlist date; INVENTORY_BUILD flag to explain |
| 3 | A | 0.602 | KEEP (actionable) | 8/10 | THE actionable name — Nov 23 AMC, 8 days; best reaction record in the field (beat-up 0.857, avg +2.5%, worst −5.5%); beats small (+3.6% avg) and FY27 guide is the event; RECEIVABLES_OUTRUN flag |
| 4 | PAYX | 0.542 | KEEP (watchlist) | 4/10 | 4/4 beats but thin (+1.8% avg), avg reaction NEGATIVE (−1.4%), last print −9% on beat-plus-reaffirm; Dec 18 (33d); RECEIVABLES_OUTRUN flag |
| 5 | CTAS | 0.520 | KEEP (watchlist) | 6/10 | Best business in the field (4/4 raises, revenue +10.9% accelerating) at the worst price (36.7x fwd, target below price, FTC/UniFirst binary Dec 11–17); Dec 17 (32d) |
| 6 | AZO | 0.258 | KEEP (watchlist) | 3/10 | Cheapest (17.0x fwd) but beat-up 0.333 on only 3 measured beats — NOT judgeable; four straight revenue misses, last four reactions +3/−9/−6/−7%; Dec 8 (23d) |

No triage cut: 6 names, research all. No high-composite name dropped — the field IS the shortlist.

## Data-integrity flags (carried from 2026-11-14 — same screen, same flags)

- **ADSK and VEEV dropped at stage 1 "profitable" on a Yahoo data failure, not a thesis change.** `uv run python scripts/why.py ADSK --mode earnings` → "dropped at 1 profitable: netIncomeToCommon=NaN; profitMargins=NaN"; same for VEEV. Yesterday's pick (VEEV @ $304.77, Plan B, print Nov 25) and the 11-13 pick (ADSK @ $260.01, Plan B, print Nov 24) are therefore ABSENT from today's field. Do not override the screen — but this is a data artifact the owner should know about, and a re-fetch that returns the fields would re-admit both.
- **MU's price cache is corrupt.** `data/prices/MU.parquet` fails to deserialize. Hence MU has price=None, no dist_sma200/dist_52w_high/ret_12m/ret_21d, and print_reaction note "no price history cached". Its 3.49x forward P/E and 133% TTM revenue growth are also cache-derived and should be treated with suspicion until the price file is repaired. MU's reaction record is unjudgeable; the panel must say so, not quote a rate.
- **ret_21d is None at the top level for A, PAYX, CTAS, AZO, NTAP** in shortlist.json; use each name's `print_reaction.ret_21d` instead (NTAP −15.5%, A −0.9%, PAYX +5.5%, CTAS +6.4%, AZO +6.5%). No run_into_print_flag is set anywhere in the field.

## Watchlist (reporting beyond the actionable window)

| Ticker | Report date | Days | One line |
|---|---|---|---|
| NTAP | Dec 1, 2026 | 16 | Nearest watchlist date; strongest beat record after A |
| AZO | Dec 8, 2026 | 23 | Cheap, washed-out, revenue misses every print |
| CTAS | Dec 17, 2026 | 32 | Best business, worst price; FTC binary lands Dec 11–17 |
| PAYX | Dec 18, 2026 | 33 | Lowest bar; only acceleration or a raise moves it |
| MU | Dec 23, 2026 | 38 | Unjudgeable on reactions until the price cache is repaired |

## Yesterday (2026-11-14) for comparison

Pick A @ $173.96, Plan B, print Nov 23 AMC; Borda #1 A 40 (unanimous). Top-6 overlap 6/6 vs yesterday — identical field, same screen (no new market session). Consistency check: expect near-identical ranking unless a lens re-rolls.

## ADDENDUM — screen rebuilt 2026-11-15 09:44 (after triage/research/panel)

`scripts/screen.py --mode earnings` was re-run to produce a dated 2026-11-15 screen (check_run.py requires the newest shortlist/funnel to be dated no earlier than the published run). The rebuild used the existing cache (no fetch — avoids the concurrent-fetch race that corrupted MU's price cache yesterday). Result: **the field changed from 6 names to 5 — MU dropped out.**

- **MU dropped at stage 5d (reaction gate):** `beat_up_rate=0.375; n_beats_measured=8; reaction_last4=+3%, +16%, -4%, +10%`. The MU price cache was repaired (presumably by a concurrent fetch from another mode's coordinator this morning), so the screen could finally measure MU's reaction record — and it fails the doctrine's own >50% beat→up gate. The `reaction_last4` matches the research reconstruction exactly. The screen working correctly, not a bug: MU beats and falls more often than not (3 of 8 beats rewarded), which is precisely the priced-in-print signature stage 5d exists to catch.
- **The other five names are unchanged** (same prices, same metrics; composites rose ~0.06–0.07 on the one-day-shorter days-to-earnings). ADSK/VEEV still dropped at stage 1 on the Yahoo NaN data failure.
- **Consequence for the panel:** the four ballots were cast on the 6-name field. MU received ZERO top-pick votes and ZERO runner-up votes, so the single pick (A) is unaffected. The ranking is re-tallied over the 5 screened names from the existing ballot files, preserving each ballot's relative order among the survivors (the skill forbids running a panel twice, and every ranking must come from a ballot file on disk). MU's research stands in the dossier as record but MU is NOT ranked — the screen, not the panel, removed it. AZO enters the top 3 and gets its own Phase 3.5 verification (verification_azo.md).
