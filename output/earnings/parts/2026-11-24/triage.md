> Run by: Muse Spark 1.3 — full panel

# Triage — EARNINGS — 2026-11-24

Screen: output/earnings/shortlist_2026-11-24.json, generated 2026-11-24 09:35:28 (fresh, rebuilt per protocol Phase 0 — fetch.py + screen.py run today). 45-day window, field of **5** — researched all, no triage cut (skill: 4–9 candidates → skip the cut).

Prices are Monday 2026-11-23 close. Yesterday's field was 7; two names left the field on the refreshed screen — see "Dropped vs yesterday" below. Those are screen decisions, not thesis changes.

## Split: actionable vs watchlist

**Actionable now (reporting within ~10 days):** VEEV (9d), ADSK (0d — reports TODAY, Tue 2026-11-24 AMC).
**Watchlist (further out, ranked and parked):** AZO (14d), CTAS (23d), PAYX (24d).

## Triage table (ordered by composite)

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | VEEV | 0.815 | KEEP | 8 | Cleanest setup: 4/4 beats (+5.4% avg), revenue accelerating (+17.6% YoY, rev_accel +6.5pp), beat-up 0.625, sold off −16.8% in 21 sessions into the print |
| 2 | ADSK | 0.736 | KEEP | 7 | Longest beat streak (12/12 EPS) and de-rated to 18.0x forward, but reports TODAY — the panel ranks it, Plan B entry would be Nov 26; surprise trend −1.96 (shrinking beats) is the watch item |
| 3 | PAYX | 0.552 | KEEP | 6 | Beatable bar (management's own soft ~4% guide) and cheapest implied move, but beats get sold (reaction avg −1.4%, beat-up 0.571) — the worst reaction record in the field |
| 4 | CTAS | 0.545 | KEEP | 6 | Best business (5 straight guide raises, record margins, rev +10.9%) but worst setup: FY27 consensus EPS $5.54 at the very top of the raised guide, 36.3x forward, FTC/UniFirst binary before the print |
| 5 | AZO | 0.293 | KEEP | 4 | Weakest in the field: revenue missed 4/4, comps fading, beat-up rate not judgeable (3 measured beats), CFO departs Nov 25 — kept because the field is only 5 and the skill says research all of them |

## Dropped vs yesterday (screen decisions, verified)

- **A (Agilent)** — dropped at stage 5 (reports ≤45d): next_earnings is now NaN. It reported Mon 2026-11-23 AMC, so its next print falls outside the 45-day window. Yesterday it ranked #4. This is the calendar, not a thesis change. Its Nov 23 print result is a research input for the ledger close-row backlog, not for today's ranking.
- **NTAP (NetApp)** — dropped at stage 5d (beat→up rate >50%): beat_up_rate = 0.4286 on 7 measured beats, reaction_last4 +22%, −3%, +2%, +5% (confirmed by `scripts/why.py NTAP --mode earnings`). Yesterday it ranked #6 with a screen beat_up of 0.571. The refreshed price/earnings caches re-measured its reaction history and it now fails the screen's own reaction gate. That is the screen working as designed — a name whose beats are not rewarded does not get research budget — but note the gate's measurement is BMO/AMC-ambiguous (see the skill's Phase 3.5 note on `_reaction_at`), so yesterday's researched first-session reactions (+2.6/+22.4/−0.1/−2.0) told a less bad story than today's screen gate. Flagged here so the panel and the reader see the discrepancy; NTAP is NOT ranked today because the screen dropped it, and the panel must not re-add it.

## Borderline notes

- **ADSK at 0 days:** it reports after the close today. The research and panel must treat it as a live Plan B candidate only — a Plan A entry would have had to be by today's close, and the writeup must not pretend otherwise. Its price is up +4.4% since yesterday ($244.48 → $255.33) into the print, ret_21d now +1.2% (was −4.1%).
- **AZO's beat-up rate (0.333) is not judgeable** on 3 measured beats (screen's own note) — it was kept, not vindicated, on the doctrine's central question.
- **No name carries run_into_print_flag** today (all False). VEEV is still −16.8% over 21 sessions; ADSK has rallied into the print.
- **Earnings-quality flags:** ADSK and PAYX both carry RECEIVABLES_OUTRUN (see research briefs — the research agents must explain each flag per the protocol).
