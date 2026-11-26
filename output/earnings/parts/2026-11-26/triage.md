> Run by: Muse Spark (unknown) — full panel

# Earnings triage — 2026-11-26

Screen: `output/earnings/shortlist_2026-11-26.json`, generated 2026-11-26 09:29:32. Field size **4** (45-day window). Per the earnings skill, a 4–9 candidate field **skips the triage cut** — research all of them; there is nothing to triage away. Kept all 4, field was the whole field.

## Split: actionable now vs watchlist

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | VEEV | 0.878 | KEEP — actionable | 9/10 | 8/8 beats, +5.42% avg surprise, revenue accelerating (+17.6% YoY, rev_accel +6.5%), beat_up_rate 0.625, stock −13.3% into the print (no run-up flag) — reports 2026-12-03 (7 days) |
| 2 | CTAS | 0.642 | KEEP — watchlist | 7/10 | 8/8 beats, record margins, 5 straight guide raises, but tiny +1.07% surprises and beat_up_rate 0.625 with flat avg reaction (+0.07%); trades above mean target — reports 2026-12-17 (21 days) |
| 3 | PAYX | 0.578 | KEEP — watchlist | 6/10 | 4/4 beats but shrinking surprises (trend −1.12), revenue decelerating (rev_accel −3.6%), worst reaction record (avg −1.38%, last print −9% on a beat), RECEIVABLES_OUTRUN flag — reports 2026-12-18 (22 days) |
| 4 | AZO | 0.373 | KEEP — actionable | 4/10 | Only 3/8 beats, beat_up_rate 0.333 on 3 measured beats (note: not judgeable), revenue missed 4/4, reaction_last4 all negative except +3% — the weakest record in the field, but still screened in — reports 2026-12-08 (12 days) |

**Actionable now** (reporting within ~10 days; the skill's ~10-day line is applied with the 12-day AZO included because it is the second-earliest date and the field is only 4): VEEV (Dec 3), AZO (Dec 8).

**Watchlist** (further out, ranked and parked): CTAS (Dec 17), PAYX (Dec 18).

Note on the split: AZO at 12 days is just outside the ~10-day line, but with a 4-name field the skill's 4–9 rule says research all of them anyway, so the split is a labeling decision, not a research cut. All four go to Phase 2.

## Reaction-record first (doctrine scoring)

- **VEEV** — beat_up_rate 0.625 (5/8), reaction_avg_move +4.30%, avg abs 9.13%, worst −9.77%, last4: +15%, −2%, +4%, −10%. Largest moves in the field in both directions; the +15% most recent print is the best single reaction on the sheet.
- **CTAS** — beat_up_rate 0.625 (5/8), reaction_avg_move +0.07%, avg abs 4.70%, worst −10.57%, last4: −3%, +7%, −5%, +1%. Coin-flip reactions on tiny beats (+1.07% avg surprise) — the record says the market yawns.
- **PAYX** — beat_up_rate 0.571 (4/7), reaction_avg_move −1.38%, avg abs 4.13%, worst −9.40%, last4: −9%, −2%, +3%, +2%. Negative average reaction on beats — the priced-in print, measured.
- **AZO** — beat_up_rate 0.333 (1/3, not judgeable per screen note), reaction_avg_move −2.27%, avg abs 4.20%, worst −8.99%, last4: +3%, −9%, −6%, −7%. Three of the last four prints fell; the screen kept it on the 3/4 beat count but the reaction record is the field's worst.

## Priced-in risk

No name carries `run_into_print_flag` (all ret_21d < 15%): VEEV −13.3% (sold off into the print), CTAS +6.2%, PAYX +8.4%, AZO +8.3%. VEEV's selloff is the only setup where the bar looks lowered rather than raised.

## Earnings-quality flags

- PAYX: `RECEIVABLES_OUTRUN` (recv_rev_divergence +0.130) — appended to its research brief per protocol.
- VEEV, CTAS, AZO: no flags.

## Borderline notes

- AZO is the genuine borderline: 3/8 beats over 8 quarters and a non-judgeable beat_up_rate, yet it passed the screen's gates. It stays because the field is 4 and the skill says research all — the panel, not triage, decides whether it belongs in the ranking.
- PAYX's RECEIVABLES_OUTRUN flag plus its negative reaction record make it the most likely bottom of the ranking, but it is the cheapest bar in the field (consensus ≈ management's soft ~4% guide per yesterday's run), so it is not a triage drop.
