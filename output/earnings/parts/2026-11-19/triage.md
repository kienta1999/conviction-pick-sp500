> Run by: Muse Spark (muse-spark) — full panel

# Triage — earnings mode, run 2026-11-19

Screen: `output/earnings/shortlist_2026-11-19.json` (generated 2026-11-19 09:17:40), 45-day window.
Field size **6** → per the earnings skill (4–9 candidates) **skip the cut and research all 6**.
Kept all 6; the field was the whole field. Nothing was dropped.

**Split — actionable now vs watchlist:**

- **Actionable now (reporting within ~10 days):** A (2026-11-23, 4d), ADSK (2026-11-24, 5d).
- **Watchlist:** VEEV (2026-12-03, 14d), AZO (2026-12-08, 19d), CTAS (2026-12-17, 28d), PAYX (2026-12-18, 29d).

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|--------|-----------|-----------|----------------|-----------------|
| 1 | VEEV | 0.803 | KEEP (watchlist) | 7/10 | Best composite: 4/4 beats, rev accel +6.2pp, ret_21d −9.0% (not run up), but reaction record is volatile (last4 +15, −2, +4, −10; avg abs 9.1%) — the biggest gap risk in the field |
| 2 | ADSK | 0.692 | KEEP (actionable) | 7/10 | 4/4 beats, surprise avg 6.4%, rev accel +4.6pp, fwd PE 18.0 vs 21% analyst upside; beat size shrinking (trend −1.96) and a RECEIVABLES_OUTRUN flag to explain |
| 3 | A | 0.607 | KEEP (actionable) | 8/10 | Best reaction record in the field: beat_up_rate 0.857, avg move +2.5%, last4 +2, +17, −3, +2; surprise trend +7.52 (accelerating); only 3/4 beats and a RECEIVABLES_OUTRUN flag |
| 4 | CTAS | 0.518 | KEEP (watchlist) | 5/10 | 4/4 beats but surprise avg only 0.99% — beats managed to the decimal; price 222.20 sits ABOVE the analyst mean target 218.44 at 36.1x fwd PE; reaction avg move +0.1% is a coin flip |
| 5 | PAYX | 0.518 | KEEP (watchlist) | 4/10 | Weakest reaction record that cleared the gate: beat_up_rate 0.571 with avg move −1.4% (beats fall on average), revenue decelerating (accel −3.9pp), RECEIVABLES_OUTRUN flag |
| 6 | AZO | 0.272 | KEEP (watchlist) | 3/10 | Lowest composite by far; beat_up_rate 0.333 on only 3 measured beats — the screen's own note says the rate is NOT judgeable; last4 reactions +3, −9, −6, −7 (three of four down). Kept, not vindicated |

**Triage scoring notes (per the skill's criteria, reaction record first):**

- **Reaction record:** A (0.857) > VEEV = ADSK = CTAS (0.625) > PAYX (0.571) > AZO (0.333, not judgeable — only 3 measured beats). PAYX and AZO have negative average reactions (−1.4%, −2.3%): their own beats have historically been sold.
- **Cost of being wrong (reaction_avg_abs_move / worst):** VEEV 9.1% / −9.8% — the largest single-session bet; A 4.7% / −5.5% — the cheapest gap; ADSK 4.9% / −8.6%; CTAS 4.7% / −10.6% (worst tail in the field); PAYX 4.1% / −9.4%; AZO 4.2% / −9.0%.
- **Beat record quality:** ADSK surprise avg 6.4% but shrinking (−1.96 trend); VEEV 5.4% flat (−0.16); A 3.6% but accelerating (+7.52); CTAS 0.99% (managed); PAYX 1.8% shrinking (−1.12); AZO 1.6% accelerating (+6.04) but from a low base with 3/4 beats and eps_yoy_up_4q only 2/4.
- **Revenue underneath:** VEEV rev_yoy 17.6%, accel +6.2pp (best); ADSK 16.1%, +4.6pp; CTAS 10.9%, +3.6pp; A 8.1%, +2.0pp; PAYX 5.9%, −3.9pp (decelerating); AZO 5.6%, ~0pp.
- **Earnings-line direction:** all 4/4 eps_yoy_up except AZO (2/4); eps_yoy_q: ADSK +26.0%, A +18.2%, VEEV +18.1%, AZO +15.1%, CTAS +13.3%, PAYX +9.8%.
- **Priced-in risk:** no run_into_print_flag anywhere (all ret_21d ≤ +6.0%). VEEV ret_21d −9.0% is the only name down into its print. CTAS is the valuation flag: 36.1x fwd PE, price above mean target. ADSK cheapest on fwd PE (18.0x) with 21.3% analyst upside.
- **Fallback quality:** VEEV net cash (−6.6x net debt/EBITDA), 29.9% operating margin, 17.6% rev growth — the strongest fallback. A: 24.5% operating margin, net debt/EBITDA 1.15x. ADSK: 28.1% operating margin, net cash, but receivables flag. CTAS: 23.6% operating margin, ROE 41.4%. PAYX: 39.9% operating margin, ROE 47.1% — quality business, weak reaction record. AZO: 17.7% operating margin, net debt/EBITDA 3.0x (most levered), negative book equity — weakest fallback.

**Borderline flags:** AZO's beat_up_rate is explicitly not judgeable yet it sits in the field — the panel must treat its reaction record as unproven, not as 0.333. CTAS's 0.99% average surprise is a managed-number signature, not a beat streak. PAYX's negative average reaction means the doctrine's central question (does the stock rise on its beats?) is answered "no" on the measured record.
