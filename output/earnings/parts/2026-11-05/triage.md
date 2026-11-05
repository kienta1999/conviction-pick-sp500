> Run by: Muse Spark (unknown) — full panel

# Triage — earnings mode — 2026-11-05

Screen: `output/earnings/shortlist_2026-11-04.json`, generated 2026-11-04 09:21:41 (17 candidates).
Cache status: nominally <24h old, so reused per protocol — BUT the fetch rebuild
attempted this morning stalled on Yahoo 401 crumb errors (fetch.py stuck at
434/503 tickers, killed) and the screen's prices are stale: they are Oct 30 / Nov 2 /
Nov 3 closes, not Nov 4 closes. Verified Nov 4 closes via Yahoo chart API
(query1.finance.yahoo.com, 2026-11-05 ~01:30 PT) for the six actionable names and
recorded below; the panel must use the VERIFIED Nov 4 closes as current prices,
not the screen's stale `price` field. No price was invented — every verified close
below comes from that Yahoo chart pull.

Verified Nov 4 closes (Yahoo chart API, timestamps 2026-11-04 09:30 ET):
PH 910.19 (screen 899.82, Oct 30) | RL 412.06 (screen 392.87, Oct 30) |
MNST 48.75 (screen 47.18, Nov 3) | COP 136.94 (screen 144.40, Nov 3) |
OXY 57.33 (screen 64.00, Oct 30) | VYLR 71.25 (screen 73.63, Nov 2).

## Split first: actionable vs already-reported vs watchlist

- **Actionable now (reports within ~10 days, print not yet happened): 6 names** —
  MNST, RL, PH, COP (all 2026-11-05), OXY (2026-11-09), VYLR (2026-11-11).
  Field size 4–9 → per the skill, skip the cut and RESEARCH ALL SIX. No triage
  cut was applied to the actionable set.
- **Already reported 2026-11-04 (days_to_earnings = 0, print done): APP, CPAY, EW,
  PTC, EMR.** Dropped from this run's panel — the pre-print trade is gone, not
  because the doctrine failed. CPAY had the cleanest reaction record on the sheet
  (beat_up 0.857, last4 +1/+13/+12/+6) but it printed yesterday.
- **Watchlist (reports beyond ~10 days): 6 names** — A 2026-11-23, ADSK 2026-11-24,
  VEEV 2026-11-25, AZO 2026-12-08, CTAS 2026-12-17, PAYX 2026-12-18. Parked, not
  researched; listed with dates at the end of final_ranking.

## Triage table (ordered by composite)

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | APP | 0.796 | DROP — printed 2026-11-04 | 7 | Best composite but printed yesterday; last4 −20/+6/−20/+1, avg abs 17.7% — violent, untradeable now |
| 2 | CPAY | 0.774 | DROP — printed 2026-11-04 | 8 | Cleanest reaction record (0.857, last4 all up) but printed yesterday |
| 3 | OXY | 0.719 | KEEP — research | 6 | beat_up 0.875 but 54% avg surprise is oil-price noise, not execution; Nov 9 print |
| 4 | MNST | 0.628 | KEEP — research | 6 | 3/4 beats only, rev +20.2% YoY accelerating, but 36.1x forward and +12.3%/21d history of priced-in risk |
| 5 | VEEV | 0.609 | DROP — watchlist 2026-11-25 | 7 | 4/4 beats, rev +17.6% YoY, but avg abs 9.1% and last4 +15/−2/+4/−10 — too far out to research now |
| 6 | RL | 0.606 | KEEP — research | 8 | 4/4 beats, 8.19% avg surprise, rev +14% YoY accelerating, 18.8x forward; Nov 5 print |
| 7 | PH | 0.599 | KEEP — research | 8 | 4/4 beats, 8.07% avg surprise, beat_up 0.875, record backlog; third straight day as the panel's lead name — print today |
| 8 | COP | 0.520 | KEEP — research | 5 | 3/4 beats, weakest reaction record (beat_up 0.571, avg move +0.9%), oil deck; small 2.4% avg move caps both sides |
| 9 | ADSK | 0.515 | DROP — watchlist 2026-11-24 | 6 | 4/4 beats, 6.37% avg surprise, but RECEIVABLES_OUTRUN flag and Nov 24 date |
| 10 | VYLR | 0.483 | KEEP — research | 3 | 3/4 beats with NEGATIVE avg surprise (−12.11%, trend −37.69), no measurable reaction history — weakest field member, kept only because the 4–9 rule researches all |
| 11 | EW | 0.481 | DROP — printed 2026-11-04 | 6 | 3/4 beats, muted reactions (worst −1.4%), printed yesterday |
| 12 | A | 0.447 | DROP — watchlist 2026-11-23 | 7 | 3/4 beats, beat_up 0.857, last4 +2/+17/−3/+2, but RECEIVABLES_OUTRUN flag and Nov 23 date |
| 13 | PTC | 0.420 | DROP — printed 2026-11-04 | 5 | 4/4 beats but rev YoY −6.8% and surprise trend −23.3 collapsing; printed yesterday |
| 14 | PAYX | 0.384 | DROP — watchlist 2026-12-18 | 5 | 4/4 beats but 1.80% avg surprise, avg move −1.4%, RECEIVABLES_OUTRUN; Dec 18 |
| 15 | EMR | 0.370 | DROP — printed 2026-11-04 | 6 | 4/4 beats, thin 1.52% avg surprise; printed yesterday |
| 16 | CTAS | 0.337 | DROP — watchlist 2026-12-17 | 6 | 4/4 beats, 1.07% avg surprise — beats are rounding errors; Dec 17 |
| 17 | AZO | 0.194 | DROP — watchlist 2026-12-08 | 4 | 3/4 beats, beat_up 0.333 on only 3 measured beats — rate NOT judgeable, avg move −2.3% |

## Borderline flags

- VYLR is the honest borderline: negative surprise trend and no reaction history
  mean the screen kept it on revenue growth (+78% TTM) alone. The panel may rank
  it last; it must not win on revenue growth without a reaction record.
- COP vs OXY: both are oil-deck prints; COP's reaction record (0.571) is materially
  worse than OXY's (0.875) while OXY's surprise record is commodity noise. The
  panel should not treat either as an execution story.
- PH prints today (2026-11-05, BMO per prior runs — research must re-confirm);
  it has been the single pick on 2026-11-03 and 2026-11-04. A fourth straight
  PH pick on the same print would be the panel re-voting the same trade, not a
  new decision — the panel should say so if that is what happens.
- Screen `ret_21d` is null for every candidate (stale cache) — the run-into-print
  flag is uncomputed this run. Research must supply the 1-month move per name
  from the web; Gate A1 box 1 cannot be ticked from the screen alone.

## Watchlist (parked, with dates)

| ticker | report date | days out | note |
|---|---|---|---|
| A | 2026-11-23 | 19 | beat_up 0.857; RECEIVABLES_OUTRUN |
| ADSK | 2026-11-24 | 20 | 4/4 beats; RECEIVABLES_OUTRUN |
| VEEV | 2026-11-25 | 21 | 4/4 beats; avg abs 9.1% |
| AZO | 2026-12-08 | 34 | beat_up 0.333, not judgeable |
| CTAS | 2026-12-17 | 43 | 4/4 beats, 1.07% avg surprise |
| PAYX | 2026-12-18 | 44 | 4/4 beats, avg move −1.4%; RECEIVABLES_OUTRUN |
