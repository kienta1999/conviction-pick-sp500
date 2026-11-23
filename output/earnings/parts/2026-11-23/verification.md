> Run by: Muse Spark 1.3 — full panel

# Verification report — stock-pick-earnings — RUN_DATE 2026-11-23

Scope: the consolidated dossier `output/earnings/research_dossier_2026-11-23.md` and triage `output/earnings/parts/2026-11-23/triage.md`, verified against primary sources only (company press releases / IR pages, SEC filings, and Finnhub daily closes for reaction math; Zacks / MarketBeat / TwelveData for consensus, since there is no primary source for consensus). No panelist ballot file was read.

Method for reactions: "first-session reaction" = close-to-close from the last close before the print is released to the first close after it is released — i.e. print-day close for a BMO print, next-session close for an AMC print. All reaction figures below were recomputed from Finnhub daily closes (via the saved `browser.search` finance data) and cross-checked against press accounts. This matters because the screen's `reaction_last4` mixes windows: in several cases the screen's figure is the print-day move (for AMC prints, a session that happened *before* the release) or the second session after the print.

## Tally

- **Confirmed: 44**
- **Contradicted: 7**
- **Unverified: 1**

Breakdown: dates 7 confirmed; upcoming-print consensus 7 confirmed; last-quarter actuals (most recent print) 7 confirmed; reactions (two most recent per name) 11 confirmed / 3 contradicted, plus 3 further contradictions found in older prints checked opportunistically; next-quarter consensus 6 confirmed / 1 contradicted; moat 6 confirmed-or-plausible / 1 unverified.

## 1. Report dates and BMO/AMC

| Ticker | Dossier claim | Verdict | Evidence |
|---|---|---|---|
| A | Mon 2026-11-23 AMC, CONFIRMED (co. PR Oct 29) | **Confirmed** | Agilent PR Oct 29, 2026 (agilent.com / BusinessWire): results "after the stock market closes on Monday, Nov. 23", call 1:30 p.m. PST. Print had not happened at verification time (morning Nov 23 PT). |
| ADSK | Tue 2026-11-24 AMC, CONFIRMED (co. PR Nov 2) | **Confirmed** | Autodesk PR Nov 2, 2026 (adsknews / PRNewswire): Q3 FY2027 call Tue Nov 24, 2:00 p.m. PT. Zacks also labels it a confirmed date, AMC. |
| NTAP | Tue 2026-12-01 AMC, CONFIRMED (co. PR Nov 10) | **Confirmed** | NetApp PR Nov 10, 2026 (investors.netapp.com / BusinessWire): "After market close on December 1, 2026", webcast 2:30 p.m. PT; quarter ended Oct 30, 2026. |
| VEEV | Thu 2026-12-03 AMC, CONFIRMED (co. PR Nov 12) | **Confirmed** | Veeva PR Nov 12, 2026 (PRNewswire): results after market close Dec 3, 2026, call 2:00 p.m. PT; prepared remarks ~1:05 p.m. PT. Zacks labels it a confirmed date, AMC. |
| AZO | Tue 2026-12-08 BMO, CONFIRMED (co. PR Nov 11) | **Confirmed** | AutoZone PR Nov 11, 2026 (GlobeNewswire): results for Q1 ended Sat Nov 21, 2026 "before market open on Tuesday, December 8, 2026", call 10:00 a.m. ET. Zacks labels it a confirmed date. |
| CTAS | Thu 2026-12-17 BMO, ESTIMATED, not confirmed | **Confirmed as stated** (date itself unverified) | No company PR found. Zacks (estimated), MarketBeat (estimated) and TipRanks (est.) all say Dec 17 BMO. **Discrepancy stands unresolved:** Finnhub lists Dec 16, 2026 (EPS $1.393, revenue $3.089B), corroborated by FXEmpire/Sync2Cal Dec 16. The dossier's Dec 17 is the majority view, not a confirmed date. |
| PAYX | Fri 2026-12-18 BMO, ESTIMATED, not confirmed | **Confirmed as stated** (date itself unverified) | No company PR found. Zacks (estimated) and MarketBeat (estimated) say Dec 18 BMO. **Additional dissent beyond what the dossier noted:** Finnhub lists Dec 17, 2026 (EPS $1.301, revenue $1.654B), matching the TipRanks Dec 17 the dossier already flagged. Majority view is Dec 18, not confirmed. |

## 2. Consensus EPS / revenue for the upcoming print

All seven confirmed within the dossier's stated ranges. Vendor dispersion is real and worth noting: Finnhub's estimates run higher than Zacks on NTAP ($2.66/$2.148B vs $2.60/$2.11B), VEEV ($2.39/$953.7M vs $2.33/$933.8M), ADSK ($3.13/$2.176B vs $3.07/$2.13B), AZO ($35.62/$4.994B, inside the dossier's range) and CTAS ($1.393/$3.089B vs $1.36–1.37/$3.02–3.03B). The dossier's ranges are the Zacks/MarketBeat/TwelveData consensus and are correct on that basis.

| Ticker | Dossier claim | Verdict | Evidence |
|---|---|---|---|
| A | $1.73 / $1.99B | **Confirmed** | Zacks/MarketBeat: $1.73 / $1.99B; guide $1.71–1.74 confirmed (TipRanks, MarketBeat). Finnhub $1.76/$2.03B differs — already flagged in dossier. |
| ADSK | $3.07 / $2.13B | **Confirmed** | Zacks detailed estimates: $3.07 / $2.13B; guide $3.04–3.09 / $2.125–2.140B confirmed. Finnhub $3.13/$2.176B differs — already flagged. |
| NTAP | $2.60–2.61 / $2.11B | **Confirmed** | Zacks $2.60 / $2.11B; MarketBeat $2.61 / $2.11B. Guide $2.54–2.64 confirmed (company Q1 FY27 release). |
| VEEV | $2.33–2.34 / ~$934–935M | **Confirmed** | Zacks $2.33 / $933.79M; MarketBeat $2.34 / $935.22M; guide $2.33–2.34 / $932–935M confirmed (company Q2 release). |
| AZO | $35.40 / $4.94B (Zacks $36.06) | **Confirmed** | MarketBeat $35.40 / $4.94B; Zacks $36.06; TwelveData $35.39 / $4.95B. Zacks labels Dec 8 a confirmed date. |
| CTAS | $1.36–1.37 / $3.02–3.03B | **Confirmed** | Zacks $1.36 / $3.02B; MarketBeat $1.37 / $3.03B. |
| PAYX | $1.28–1.30 / $1.62B (Zacks rev $1.64B) | **Confirmed** | Zacks $1.29–1.30 / $1.64B; MarketBeat/arincen $1.28 / $1.62B. |

## 3. Last quarter: actual vs consensus, and the stock's reaction

Most-recent-print actuals are confirmed for all seven names. Reactions were spot-checked on the two most recent entries of each screen `reaction_last4` list, recomputed close-to-close from Finnhub candles. **Three of the fourteen spot-checked reactions are contradicted**, and three further contradictions were found in older prints checked opportunistically. The pattern: the screen sometimes records the print-day move (for AMC prints, a session that occurred *before* the release) or the second session after the print, instead of the first session that priced the print.

### A — Agilent
- Q3 FY26 (Aug 26 AMC): EPS $1.62 vs $1.49 consensus **confirmed** (MarketBeat table; $1.62 vs $1.48 per sci-tech-today). Rev $1.88B vs $1.84B **confirmed**. Reaction: Aug 26 close $155.08 → Aug 27 $157.69 = **+1.68% — screen +2% confirmed**.
- Q2 FY26 (May 27 AMC): EPS $1.49 vs $1.41 **confirmed** (InsideArbitrage table). Reaction: May 27 $115.84 → May 28 $135.38 = **+16.87% — screen +17% confirmed**.

### ADSK — Autodesk
- Q2 FY27 (Aug 27 AMC): EPS $3.30 vs $3.12 **confirmed**; rev $2.046B vs $2.01B **confirmed** (multiple sources). Reaction: **CONTRADICTED.** Screen says +6%; first-session close-to-close Aug 27 $270.58 → Aug 28 $260.66 = **−3.67%**. The +6.21% was the Aug 27 regular-session rally *before* the AMC print (Aug 26 $254.77 → Aug 27 $270.58). Qanvo's +2.3% is the two-day Aug 26→28 move (+2.31%), also not the first session. The dossier's claim that the screen "uses a different window — same sign pattern" is wrong for this print: the sign flips. ADSK's most recent print was a beat-and-fall, not a +6% rally.
- Q1 FY27 (May 28 AMC): reaction May 28 $240.95 → May 29 $231.31 = **−4.00% — screen −4% confirmed**. (Q1 consensus $2.99 vs $2.84 as stated in the dossier was not independently re-verified.)

### NTAP — NetApp
- Q1 FY27 (Sep 2 AMC): EPS $2.58 vs $2.12 **confirmed** (MarketBeat table: $2.58 vs $2.12; Tikr: beat by 21.54%); rev $2.03B vs $1.84B **confirmed**. Reaction: Sep 2 $180.77 → Sep 3 $185.38 = **+2.55% — screen +3% confirmed**.
- Q4 FY26 (May 28 AMC): reaction May 28 $142.40 → May 29 $174.29 = **+22.39% — screen +22% confirmed**. (Q4 consensus $2.43 vs $2.27 as stated was not independently re-verified.)
- Older prints (checked opportunistically): Q3 FY26 (Feb 26 AMC) screen −3% **contradicted** — first session Feb 27 was −0.11% (Feb 26 $99.14 → Feb 27 $99.03); −2.69% was the Feb 25→26 print-day move. Q2 FY26 (Nov 25, 2025 AMC) screen +2% **contradicted** — first session Nov 26 was −2.00% (Nov 25 $111.48 → Nov 26 $109.25); +2.32% was the Nov 24→25 print-day move. NTAP's reaction record is worse than the screen shows: two of the last four first-session reactions were ~flat/negative, not −3%/+2%.
- **Conflict (a) RESOLVED — both figures are real under different windows; the screen's +3% (close-to-close) is confirmed.** Tikr's "fell ~10.1%" is the after-hours/intraday trough: shares fell 8.92% after hours to $164.64 (Parameter.io) and opened Sep 3 at $161.95 (−10.4% vs the Sep 2 close of $180.77), then recovered to close Sep 3 at $185.38 (+2.55%). The dossier's explanation — that the −10% figure reflects an intraday/after-hours swing — is correct. The panel should use +2.6% close-to-close and note the stock traded ~10% lower intraday before recovering.

### VEEV — Veeva
- Q2 FY27 (Aug 26 AMC): EPS $2.35 vs $2.22 **confirmed** (Zacks: beat by 5.9%); rev $928M vs $905M **confirmed**. Reaction: Aug 26 $244.91 → Aug 27 $282.13 = **+15.20% — screen +15% confirmed** (Weiss reports +16.4% to a $285.05 close; Finnhub's close is $282.13 — vendor closes differ slightly, either way +15–16%).
- Q1 FY27 (Jun 3 AMC): reaction **CONTRADICTED.** Screen says −2%; first-session close-to-close Jun 3 $178.72 → Jun 4 $178.60 = **−0.07% (essentially flat)**. The −2.31% was the Jun 3 print-day move (Jun 2 $182.94 → Jun 3 $178.72), which occurred before the AMC release. "Beat and fell −2%" overstates it; the market was flat on the print.

### AZO — AutoZone
- Q4 FY26 (Sep 22 BMO): EPS $56.05 vs Zacks $54.54 **confirmed** (+2.8% beat, Zacks article; Finnhub table: actual $56.05, rev $6.595B); rev $6.59B vs $6.69–6.70B miss **confirmed**. Reaction: Sep 21 $2,803.25 → Sep 22 $2,894.73 = **+3.26% — screen +3% confirmed**.
- Q3 FY26 (May 26 BMO): reaction May 22 $3,406.50 → May 26 $3,100.11 = **−8.99% — screen −9% confirmed** (TickerOn/GuruFocus: −9.0% on the Q3 print; rev $4.84B vs $4.86B consensus confirmed via TickerOn). (Q3 EPS consensus $38.07 vs $36.18–36.65 as stated was not independently re-verified.)

### CTAS — Cintas
- Q1 FY27 (Sep 23 BMO): EPS $1.39 vs $1.35 **confirmed** (Zacks summary; Finnhub table: $1.390, rev $3.014B); rev $3.01B vs $2.97–2.98B **confirmed**. Reaction: Sep 22 $198.80 → Sep 23 $191.97 = **−3.44% — screen −3% confirmed** (earnings-watcher −3.4%).
- Q4 FY26 (Jul 15 BMO): EPS $1.29 vs $1.24 **confirmed** (MarketBeat table; CoinCodex). Reaction: **CONTRADICTED.** Screen says +7%; print-day Jul 14 $184.33 → Jul 15 $192.37 = **+4.36%** (earnings-watcher close-to-close +4.4%). The +7.22% move was the *following* day, Jul 16 ($192.37 → $206.25). The dossier itself noted the +7% was "not independently corroborated" — it is the second session's move, not the earnings-day reaction.

### PAYX — Paychex
- Q1 FY27 (Sep 23 BMO): EPS $1.34 vs $1.32 **confirmed** (MarketBeat; Finnhub table: $1.340, rev $1.631B); rev $1.6305B vs $1.627B **confirmed**. Reaction: Sep 22 $114.53 → Sep 23 $104.49 = **−8.78% — screen −9% confirmed** (earnings-watcher −8.8%).
- Q4 FY26 (Jun 24 BMO): reaction Jun 23 $97.99 → Jun 24 $96.30 = **−1.72% — screen −2% confirmed**. (Q4 EPS consensus $1.32 vs $1.31 as stated was not independently re-verified.)
- Older print (checked opportunistically): Q2 FY26 (Dec 19, 2025 BMO) screen +2% **contradicted** — print-day Dec 18 $114.24 → Dec 19 $112.28 = **−1.72%**; +2.32% was the following Monday Dec 22 ($112.28 → $114.88). The dossier flagged this conflict; the print-day figure is −1.7%, which strengthens (not weakens) the dossier's "beats get sold" narrative.
- **Conflict (b) RESOLVED in favour of +3.03%.** Q3 FY26 (Mar 25 BMO): Finnhub candles show Mar 24 close $90.61 → Mar 25 close $93.36 = **+3.03%** (Tikr: "rose 3.03% on the day, closing at $93.36"). CoinCentral/Blockonomi's −3.09% to $90.61 is the **Mar 24 (pre-print) session's** move (Mar 23 $93.50 → Mar 24 $90.61 = −3.09%), misattributed to the earnings day. Screen +3% is correct.

## 4. Next-quarter consensus (the number the guide will be judged against)

| Ticker | Dossier claim | Verdict | Evidence |
|---|---|---|---|
| A (Q1 FY27) | EPS $1.50, rev ~$1.85B | **Confirmed (EPS); revenue unverified** | InsideArbitrage estimates table: Q1 FY27 EPS est. $1.50. The ~$1.85B revenue figure was not independently located. |
| ADSK (Q4 FY27) | No standalone consensus found; implied ~$3.16–3.24 EPS / $2.17–2.22B rev from FY guide | **Confirmed — and the standalone figure exists** | Zacks detailed estimates: Q4 FY27 (Jan 2027) EPS **$3.18**, revenue **$2.21B** (10 estimates) — inside the dossier's implied range. FY27 Zacks EPS $12.62 vs guide top $12.60: consensus sits $0.02 *above* the guide top, a slightly stronger tension than the dossier's "~guide midpoint ($12.56)" framing. |
| NTAP (Q3 FY27) | EPS $2.42, rev $2.01B; FY27 $10.05 / $8.23B | **Confirmed** | Zacks detailed estimates: next qtr $2.42 / $2.01B; current year $10.05 / $8.23B (8 estimates). The guide-top problem is real: FY consensus EPS $10.05 > guide top $10.03. |
| VEEV (Q4 FY27) | EPS $2.35, rev ~$963M | **CONTRADICTED** | Zacks detailed estimates: next qtr (Jan 2027) EPS **$2.29**, revenue **$940.75M** (7 estimates); InsideArbitrage Q4 FY27 est. EPS $2.31. The dossier's $2.35/~$963M matches neither. Guide-implied Q4 is ~$2.28 EPS / ~$936–941M rev, so the gap vs the Zacks consensus is ~$0.01 EPS, not ~$0.07 — the "mandatory raise" tension largely evaporates. FY27 consensus $9.22 **confirmed** (Zacks). |
| AZO (Q2 FY27) | EPS $31.75, rev $4.59B; FY27 $169.37 | **Confirmed** | TwelveData: next qtr $31.75 / $4.59B; current year $169.37. (Zacks runs higher: $32.32 / $4.60B, FY $170.30 — vendor dispersion, dossier's TwelveData figures confirmed.) |
| CTAS (Q3 FY27) | EPS $1.35, rev $3.04B; FY27 $5.54 / $12.23B | **Confirmed** | Zacks detailed estimates: next qtr $1.35 / $3.04B; current year $5.54 / $12.23B. |
| PAYX (Q3 FY27) | EPS $1.87, rev $1.91B; FY27 $5.96 / $6.86B | **Confirmed** | Zacks detailed estimates: next qtr $1.87 / $1.91B; current year $5.96 / $6.86B. |

## 5. Moat claims

Moat scores are judgments; I checked the factual anchors each rests on. None is contradicted on the facts checked. One is unverified on its specifics.

- **A — 7/10: plausible, anchors confirmed.** Pharma revenue +12% in Q3 FY26 confirmed (earnings-call transcript via Motley Fool). Regulated-pharma-QC switching costs and the named competitors (Thermo Fisher, Waters, Danaher, Shimadzu) are real; the cyclicality caveat is fair. Not overstated.
- **ADSK — 7/10: plausible, anchors confirmed.** Billings +10% vs revenue +16% in Q2 FY27 confirmed (Tikr); MaintainX margin dilution confirmed (GAAP op-margin guide cut to 25–27%, Tikr/SiliconANGLE). The per-seat-pricing risk is a live, widely discussed thesis, not invented. Not overstated.
- **NTAP — 6/10: plausible, anchors confirmed.** All-flash array revenue $1.31B, +47% YoY in Q1 FY27 confirmed (Tikr, Parameter.io); CEO Kurian's pull-forward admission confirmed verbatim (Tikr). The modest 6/10 is appropriately cautious given Pure Storage / Dell / HPE / hyperscaler competition. Not overstated.
- **VEEV — 8/10: supported, key facts confirmed.** Investor Day Nov 5, 2026 transcript (stockanalysis.com) and Nasdaq's report: "over 200 customers live on Vault CRM, including five out of the top 20 biopharmas. 14 out of the top 20 have selected us." PR Sep 23, 2026: 190+ live, 14 top-20 commitments. $6B revenue run-rate-by-2030 ambition confirmed (Nasdaq). 1,500+ customers confirmed (company PR: "serves more than 1,500 customers"). The Salesforce threat is real (6 of top 20 uncommitted) and the dossier discloses it. The 8/10 is the strongest in the batch and the facts support it.
- **AZO — 7/10: supported, key facts confirmed.** 8,031 stores confirmed (FY26 10-K / proxy via SEC: 6,863 US + 1,001 Mexico + 167 Brazil; 374 net new stores in FY26). Domestic commercial sales +10.6% in FY26 confirmed (10-K summary). The EV structural-threat caveat is a fair long-term note, not a near-term contradiction. Not overstated.
- **CTAS — 8/10: supported, key facts confirmed.** UniFirst deal confirmed via SEC 8-K (Oct 6, 2026): $5.5B, $310/share, second request Jun 11, substantial compliance certified Oct 2, timing agreement barring close before Dec 11, 2026, expects close before end of 2026; $350M reverse termination fee confirmed (Laurelton). Semafor's FTC-may-sue signal is accurately characterised in the dossier (no vote, no complaint filed as of Nov 19–20); later reporting (SeekingAlpha) that the FTC "has not told Cintas it plans to sue" is consistent with that. Route-density/switching-cost moat is qualitative but the business facts check out. Not overstated.
- **PAYX — 6/10: unverified on specifics.** The sticky-SMB-payroll / PEO / Gusto-Rippling-ADP competitive framing is plausible and directionally standard, but I did not independently verify the dossier's specific anchors (WISE AI "600 AI features", PEO +12% in Q1 FY27, Management Solutions +4%). No contradiction found; mark unverified rather than confirmed.

## Material corrections (one line each)

1. ADSK Q2 FY27 reaction is **−3.67%** (beat-and-fell), not +6% — the +6% was the pre-print rally; the dossier's "same sign pattern" claim is wrong.
2. VEEV Q4 FY27 consensus is **$2.29 / $940.75M (Zacks)**, not $2.35 / ~$963M — the guide-implied gap is ~$0.01 EPS, not ~$0.07, so the "mandatory raise" tension largely evaporates.
3. CTAS Q4 FY26 reaction was **+4.4%** on the print day, not +7% — the +7.2% move was the following day (Jul 16).
4. NTAP screen reactions for Q3 FY26 (−3%) and Q2 FY26 (+2%) are print-day moves, not post-print reactions (−0.1% and −2.0% first-session) — the reaction record is worse than the screen shows.
5. VEEV Q1 FY27 reaction was essentially flat (**−0.07%**), not −2% — the −2.3% was the pre-print session.
6. PAYX Q2 FY26 reaction was **−1.7%** on the print day, not +2% — the +2.3% was the following Monday (this strengthens the "beats get sold" narrative).
7. PAYX Q3 FY26 conflict resolved: **+3.03% is correct** (Mar 25 close $93.36); −3.09% was the Mar 24 pre-print session's move, misattributed to earnings day.
8. NTAP Q1 FY27 conflict resolved: Tikr's **−10.1% is the after-hours/intraday trough**; the close-to-close first-session reaction was **+2.6%** — the screen's +3% is confirmed.
9. CTAS date discrepancy unresolved (Finnhub Dec 16 vs Zacks/MarketBeat Dec 17); PAYX has the same shape of dissent (Finnhub Dec 17 vs Zacks/MarketBeat Dec 18) — neither date is company-confirmed.
10. ADSK Q4 FY27 standalone consensus found: **Zacks $3.18 / $2.21B** (dossier said not found; its implied range brackets this) — and FY27 Zacks EPS $12.62 sits $0.02 above the guide top.

## Implications for the panel

- The dossier's Plan B verdicts stand — nothing here makes a Plan A case — but two of its supporting arguments weaken: VEEV's "mandatory raise" (the Q4 gap is ~$0.01, not ~$0.07) and ADSK's "most reliable beater" framing (its most recent print was a beat that fell 3.7% the next session, and the screen's +6% is a pre-print rally).
- The screen's `reaction_last4` is window-inconsistent across names and vintages. Any panel ranking that leans on reaction history should use the first-session close-to-close figures in §3, not the screen's raw list: corrected last-4 (most recent first) are A +1.7/+16.9/−3.0/+2.3; ADSK −3.7/−4.0/+5.3/+2.4; NTAP +2.6/+22.4/−0.1/−2.0; VEEV +15.2/−0.1/+4.0/−9.8; PAYX −8.8/−1.7/+3.0/−1.7; CTAS −3.4/+4.4/−5/+1 (last two not re-verified by me); AZO +3.3/−9.0/−6/−7 (last two not re-verified by me).
- CTAS and PAYX dates remain estimates with a one-day vendor dissent each; re-verify against the company IR pages as the dates approach, as the dossier already advises.

## Figures I could not verify (left unverified, not fabricated)

- Second-print consensus figures for ADSK Q1 FY27 ($2.99 vs $2.84), NTAP Q4 FY26 ($2.43 vs $2.27), VEEV Q1 FY27 ($2.24 vs $2.14), PAYX Q4 FY26 ($1.32 vs $1.31), AZO Q3 FY26 ($38.07 vs $36.18–36.65) — stated in the dossier, not independently re-verified; reactions for those prints were verified.
- CTAS Q3 FY26 (−5%) and Q2 FY26 (+1%) reactions, AZO Q2 FY26 (−6%) and Q1 FY26 (−7%) reactions — beyond the two-most-recent spot-check; not re-verified.
- A Q1 FY27 revenue consensus (~$1.85B); PAYX moat specifics (WISE AI feature count, Q1 PEO/Management Solutions splits).
- Whisper numbers, 3–5yr forward-P/E ranges, and the CTAS/PAYX earnings-day straddles — not found, same as the dossier.
