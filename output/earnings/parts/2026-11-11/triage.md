> Run by: Muse Spark (muse-spark-1.3) — full panel

# Triage — earnings mode, 2026-11-11

Screen rebuilt today (`uv run python scripts/fetch.py && uv run python scripts/screen.py --mode earnings`):
8 candidates, byte-identical set to 2026-11-10 (same 8 tickers, same dates). Generated 2026-11-11 09:25:14.
Note: `ret_21d` is null for all 8 in today's screen output, so `run_into_print_flag` is
uncomputed — research must establish each name's run into the print from price history instead.

## Actionable vs watchlist split (days_to_earnings)

**Actionable now (reporting within ~10 days): 1 name — VYLR only (prints TODAY, 2026-11-11 AMC).**
The screen, not the panel, made this decision: a 4-lens vote over a 1-name actionable set is
theater, stated plainly per the earnings skill. Following the daily run's established practice
(and the skill's "rank the wave once, then split"), the panel researches and ranks the whole
8-name wave, with VYLR the only name a trade can be entered on this week; the other 7 are a
pre-vetted watchlist queue.

**Watchlist (further out):** A (Nov 23, 12d), ADSK (Nov 24, 13d), VEEV (Nov 25, 14d),
NTAP (Dec 1, 20d), AZO (Dec 8, 27d), CTAS (Dec 17, 36d), PAYX (Dec 18, 37d).

## Triage table (ordered by composite)

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|--------|-----------|-----------|----------------|-----------------|
| 1 | VEEV | 0.743 | KEEP | 7 | 4/4 beats +5.4% avg, rev +17.6% accelerating, beat_up 0.625 but last4 mixed (+15/−2/+4/−10), 9.1% avg abs move — the wave's best record, watchlist Nov 25 |
| 2 | NTAP | 0.690 | KEEP | 7 | Biggest surprises (+10.1% avg, trend +8.6), rev +29.9% accelerating, washed-out setup (−26.9% off high); INVENTORY_BUILD flag needs the narrative check; Dec 1 |
| 3 | VYLR | 0.656 | KEEP | 4 | ONLY actionable name (prints today AMC) but unproven: screen beat record is Corteva's, no Vylor reaction history, seasonal-loss quarter, no consensus found yesterday — kept because the calendar forces it, not because the doctrine loves it |
| 4 | ADSK | 0.627 | KEEP | 7 | 4/4 beats, 8/8 incl. guide raises, moat 8/10, beat_up 0.625, cheapest setup in wave (18.4x fwd); RECEIVABLES_OUTRUN flag to explain; Nov 24 |
| 5 | A | 0.523 | KEEP | 6 | Best reaction record in field (beat_up 0.857, +2.5% avg) but only 3/4 beats, first FY27 guide Nov 23 is the unknowable; RECEIVABLES_OUTRUN flag to explain |
| 6 | CTAS | 0.465 | KEEP | 5 | 4/4 beats but thinnest surprises (+0.99% avg), 36.1x fwd at fresh highs, UniFirst FTC binary Dec 11–17; Dec 17 |
| 7 | PAYX | 0.454 | KEEP | 4 | 4/4 beats but shrinking surprises, rev decelerating, last beat fell −9%, guide thin; Dec 18 |
| 8 | AZO | 0.222 | KEEP | 3 | Weakest composite by far; beat_up 0.333 on only 3 measured beats (not judgeable), revenue missed 4/4 prints, FY27 consensus not supported by run-rate; kept only because the field is 8 and the floor is the whole field |

No names dropped: the field is 8, below the ~12–15 triage target, so all 8 are researched.
Borderline flag: AZO is the weakest name in the wave on every doctrine axis (reaction record,
revenue record, surprise size) — its low composite (0.222 vs 0.454 for #7) is the screen
agreeing; it stays in only because there is nothing to triage away.

## Research batches (Phase 2)

- Batch 1: VEEV, NTAP
- Batch 2: VYLR, ADSK
- Batch 3: A, CTAS
- Batch 4: PAYX, AZO
