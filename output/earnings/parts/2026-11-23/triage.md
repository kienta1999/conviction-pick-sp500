> Run by: Muse Spark 1.3 — full panel

# EARNINGS triage — 2026-11-23

Screen: output/earnings/shortlist_2026-11-22.json, generated 2026-11-22 09:56:41 (fresh, <24h, reused per protocol Phase 0). 45-day window. Field of 7 — per the earnings skill, 4–9 candidates means skip the cut and research all of them; there is nothing to triage away. Prices are Friday 2026-11-20 close.

Split on days_to_earnings: actionable now (≤ ~10 days) vs watchlist.

## Actionable now

| # | ticker | composite | next earnings | dte | beat_up_rate | reaction_avg_abs_move | reaction last4 | one-line reason |
|---|--------|-----------|---------------|-----|--------------|----------------------|----------------|-----------------|
| 1 | A | 0.522 | 2026-11-23 | 1 | 0.857 | 4.67% | +2%, +17%, -3%, +2% | Best reaction record in the field (beat→up 6/7); reports TODAY — research must confirm BMO/AMC and whether the print has already happened |
| 2 | ADSK | 0.693 | 2026-11-24 | 2 | 0.625 | 4.89% | +6%, -4%, +5%, +2% | Reports tomorrow; 4/4 beats, surprise trend shrinking (-1.96); RECEIVABLES_OUTRUN flag |
| 3 | NTAP | 0.711 | 2026-12-01 | 9 | 0.571 | 6.74% | +3%, +22%, -3%, +2% | Biggest surprises in the field (+10.08% avg, trend +8.61) and accelerating revenue (+29.9% YoY, accel +20.7%); INVENTORY_BUILD flag; worst reaction -15.6% |

## Watchlist (reporting beyond the actionable window)

| # | ticker | composite | next earnings | dte | beat_up_rate | reaction_avg_abs_move | reaction last4 | one-line reason |
|---|--------|-----------|---------------|-----|--------------|----------------------|----------------|-----------------|
| 4 | VEEV | 0.770 | 2026-12-03 | 11 | 0.625 | 9.13% | +15%, -2%, +4%, -10% | Just outside the window (11 days); biggest absolute moves in the field (9.13%) and the largest last-4 swing (+15% to -10%); yesterday's pick |
| 5 | AZO | 0.222 | 2026-12-08 | 16 | 0.333 | 4.20% | +3%, -9%, -6%, -7% | Weakest in the field: revenue missed 4/4, beat_up rate NOT JUDGEABLE (only 3 measured beats), last three reactions all negative |
| 6 | CTAS | 0.456 | 2026-12-17 | 25 | 0.625 | 4.70% | -3%, +7%, -5%, +1% | Best operator in the batch with the worst price: 35.7x forward P/E, top-of-guide consensus |
| 7 | PAYX | 0.505 | 2026-12-18 | 26 | 0.571 | 4.13% | -9%, -2%, +3%, +2% | Beats get sold (reaction avg -1.4%), guide never raised; RECEIVABLES_OUTRUN flag |

## Notes

- The screen did not compute `ret_21d` / `run_into_print_flag` for any name (both None) — the run-into-print check must come from research, not the screen.
- A reports today (2026-11-23): if it reports BMO, the print may already be out before this run publishes; if AMC, Plan A entry must be by today's close. The research batch must state BMO/AMC and the print status explicitly.
- ADSK's screen reaction sign was corrected on 2026-11-20 (reaction -3.67% flip); the research must re-verify the last four reactions from primary sources.
- Close-row backlog (protocol addendum item 3): 57 earnings singles in the ledger have prints already passed and no `kind=close` row (only 1 close row exists in ledger history). The most recent open ones: 2026-11-22 VEEV (Dec 3), 2026-11-21 ADSK (Nov 24), 2026-11-20 VEEV (Dec 3), 2026-11-19 VEEV (Dec 3), 2026-11-18 ADSK (Nov 24), 2026-11-17/16/15/14 A (Nov 23 — today), 2026-11-13 ADSK (Nov 24), 2026-11-12 VEEV (ledger next_earnings 2026-11-25 — that date has passed; whether the print occurred then or the date moved to Dec 3 is unverified, do not assert either), 2026-11-11/10/07 NTAP (Dec 1). Close rows need realised exit prices and are the owner's to record; this run names the backlog rather than inventing closes.
