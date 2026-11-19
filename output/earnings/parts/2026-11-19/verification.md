> Run by: Muse Spark (muse-spark) — full panel

# Phase 3.5 verification — stock-pick-earnings, run 2026-11-19

Tentative winner: **VEEV (Veeva Systems)** — top pick of 3 of 4 lenses (A, B, C), runner-up of the fourth (D, which picked NONE). Ranked top 3: VEEV, A (Agilent), ADSK (Autodesk).

Scope: independent re-check of the five priority claims in the task brief, plus the load-bearing ballot claims named in the brief (Investor Day "meet or exceed", four straight guide raises, ret_21d sell-off). Sources are primary where possible (company releases, SEC 8-K, Zacks detailed estimates) and otherwise reputable press/aggregators. Verification date: 2026-11-19. Prices/closes below are from Finnhub daily candles as surfaced in search results, cross-checked against press reports.

## 1. Report dates and BMO/AMC — all three top-3 names

| Ticker | Dossier claim | Verification | Source |
|---|---|---|---|
| VEEV | Wed 2026-12-03, AMC | CONFIRMED | PR Newswire, 2026-11-12: "will announce financial results for its third quarter ending October 31, 2026 after market close on December 3, 2026", call 2:00 p.m. PT. Re-fetched from the PR Newswire Veeva news page on 2026-11-19 — headline listed first. |
| A | Mon 2026-11-23, AMC | CONFIRMED | Business Wire, 2026-10-29: "will release financial results for the fourth quarter of fiscal year 2026 after the stock market closes on Monday, Nov. 23", call 1:30 p.m. PST. Agilent's own press-release index also lists "Agilent to Announce Fourth-Quarter Fiscal Year 2026 Financial Results on Nov. 23". |
| ADSK | Tue 2026-11-24, AMC | CONFIRMED | Autodesk News / PR Newswire, 2026-11-02: "Third quarter fiscal 2027 financial results conference call to be held Tuesday, November 24, 2026, 2 p.m. PT" via autodesk.com/investors. A 2 p.m. PT call implies release just after the close, Autodesk's usual pattern; no separate release time is stated, so AMC is inferred from the call time, as the dossier does. |

No date moves. The non-negotiable item — VEEV on Wed 2026-12-03 AMC — is confirmed against the company's own release.

## 2. VEEV Q3 FY2027 consensus EPS and revenue

| Metric | Dossier claim | Verification | Source / as-of |
|---|---|---|---|
| Q3 FY2027 non-GAAP EPS | \$2.33–2.34 | CONFIRMED | Zacks detailed estimates, updated 2026-11-17: current-quarter consensus \$2.33; MarketBeat and TipRanks show \$2.34. The one-cent spread is a vendor difference, not a disagreement. |
| Q3 FY2027 revenue | ~\$934m (Zacks \$933.79m) | CONFIRMED | Zacks detailed estimates, updated 2026-11-17: \$933.79m. MarketBeat shows \$935.22m — same range, within \$1.5m. |
| Management Q3 guide | \$932–935m revenue; \$2.33–2.34 EPS | CONFIRMED | Company Q2 FY2027 release, 2026-08-26, restated in the 8-K of 2026-11-06 and in CMC Markets, 2026-11-18: total revenue \$932–935m, subscription ~\$782m, services \$150–153m, non-GAAP operating income \$417–420m, non-GAAP EPS \$2.33–2.34. Consensus sits exactly on the guide, as the dossier says. |
| Year-ago Q3 FY2026 | EPS \$2.04, revenue \$811.24m | CONFIRMED | Zacks detailed estimates (year-ago sales \$811.24m; year-ago EPS \$2.04 per TipRanks/Zacks); company Q3 FY2026 release. |

Cross-check flag (not a contradiction): Finnhub's estimate table shows a higher Q3 bar — EPS \$2.39 and revenue \$953.68m. That is inconsistent with Zacks, MarketBeat and TipRanks, all of which cluster at \$2.33–2.34 / ~\$934–935m, and with management's own guide ceiling (\$935m revenue). Treat the Finnhub figure as an outlier; do not use it. The dossier's figures stand.

## 3. Last-quarter surprise, stock reaction, and the screen `reaction_last4`

Most recent print: Q2 FY2027, reported Wed 2026-08-26 AMC.

| Claim | Dossier | Verification |
|---|---|---|
| Reported EPS / revenue | Non-GAAP EPS \$2.35, revenue \$928.0m | CONFIRMED — Zacks, 2026-08-27: EPS \$2.35 beat the Zacks consensus of \$2.22; revenue \$928m vs \$904.07m consensus. MarketBeat: \$2.35 vs \$2.23 consensus, revenue \$927.96m vs \$905.38m. |
| Surprise | EPS beat +5.4%, revenue beat +2.5% | CONFIRMED — \$2.35 vs \$2.22–2.23 is +5.4–5.9%; \$928.0m vs \$905.4m is +2.5%. |
| Guide | Raised FY27 to \$3.682–3.687B / ~\$9.21 | CONFIRMED — company release, 2026-08-26; Trefis, 2026-10-23. |
| Next-session reaction | +15% | CONFIRMED — Finnhub candles: close \$244.91 on 2026-08-26 → \$282.13 on 2026-08-27 = +15.20%. TipRanks: "following the earnings report the stock price went up 15.197%". Motley Fool, 2026-08-28: up 13.8% into Friday's open vs the prior week's close. |

Spot-check of the two most recent entries in the screen's `reaction_last4` ("+15%, -2%, +4%, -10%", most recent first), computed close-to-close from Finnhub daily candles:

| Screen entry | Print | Next-session close-to-close (Finnhub candles) | Verdict |
|---|---|---|---|
| +15% | Q2 FY2027, 2026-08-26 | \$244.91 → \$282.13 = +15.20% | CONFIRMED |
| -2% | Q1 FY2027, 2026-06-03 | \$178.72 (2026-06-03) → \$178.60 (2026-06-04) = -0.07% | CONTRADICTED as a next-session figure |
| +4% (checked as third entry) | Q4 FY2026, 2026-03-04 | \$188.48 → \$196.06 = +4.02% | CONFIRMED |
| -10% (checked as fourth entry) | Q3 FY2026, 2025-11-20 | \$270.50 → \$244.06 = -9.77% | CONFIRMED (rounded to -10%) |

The -2% discrepancy matters and is explained by the screen's BMO/AMC-ambiguous heuristic, exactly as the task brief warned. For Q1 FY2027 (reported AMC on 2026-06-03), the -2.31% move happened on the report day itself (\$182.94 on 2026-06-02 → \$178.72 on 2026-06-03, before the release), while the first full session after the print was essentially flat (-0.07%). Barchart's earnings-reaction table agrees: Day 0 -2.31%, Day +1 -0.07%. The screen's -2% therefore captures pre-release drift on the report day, not the market's reaction to the print. The dossier itself flags this entry honestly ("next-session close not found precisely" for Q1 FY2027) and the ballots repeat the screen figure without that caveat.

**Which figure to prefer:** the researched next-session figure, -0.07% (effectively flat), not the screen's -2%. Consequences: VEEV's last-four reactions on a consistent next-session basis are +15.2%, ~0%, +4.0%, -9.8% — still the widest distribution in the field, but the second print was a non-reaction rather than a down day. The screen's `reaction_avg_move` (+4.3%) and `reaction_avg_abs_move` (9.1%) are slightly overstated by the -2% entry; recomputed on next-session closes the average absolute move is about 7.3% ((15.2 + 0.1 + 4.0 + 9.8) / 4). That narrows, but does not erase, the gap the ballots lean on between the options-implied move (±6.9%) and the name's own history — the implied move is now roughly in line with, rather than below, recent realised moves. The "implied move below history" point should be softened, not deleted.

The Q3 FY2026 -10% also deserves its full context, which the dossier gives correctly: the stock fell a further ~3.4% the following session (\$244.06 → \$235.74 on 2025-11-24), so the two-session damage was about -13%. AInvest (Nov 2025) and IndexBox both record the -9.9%/-10.6% first-session fall on a clean beat-and-raise, attributed to decelerating growth expectations.

## 4. Next-quarter consensus — the number the Q4 guide will be judged against

| Metric | Dossier claim (implied from FY27 guide) | Verification | Source / as-of |
|---|---|---|---|
| Q4 FY2027 revenue | ~\$940m | CONFIRMED as a published consensus, not just an arithmetic implication | Zacks detailed estimates, updated 2026-11-17: next-quarter (Q4 FY2027, period ending 01/2027) consensus revenue \$940.75m (high \$944.40m). |
| Q4 FY2027 non-GAAP EPS | ~\$2.29 | CONFIRMED as a published consensus | Zacks detailed estimates, updated 2026-11-17: next-quarter consensus EPS \$2.29. Current-year consensus \$9.22 / \$3.69B, matching the dossier. |

This is a genuine strengthening of the dossier: the dossier said a published Q4 consensus was "not found" and derived ~\$940m / ~\$2.29 only by subtracting Q1–Q3 from the FY27 guide. The Zacks detailed-estimates page now shows the same numbers as published consensus, so the implied bar and the Street bar coincide. The arithmetic also checks: FY27 revenue midpoint \$3,684.5m less Q1 \$883.0m, Q2 \$928.0m and Q3 guide \$933.5m = \$940.0m; FY27 EPS \$9.21 less \$2.24 + \$2.35 + \$2.335 = \$2.285. **Correction to the dossier: Q4 FY2027 consensus is published (Zacks, 2026-11-17) at \$940.75m revenue / \$2.29 EPS — the "not found" should be updated, but the number itself is unchanged.** The ballots' Plan A condition (Q4 guide above ~\$940m / ~\$2.29) therefore stands exactly as written.

## 5. The moat's central factual claim

Claim as made in the ballots: Veeva is the system of record for regulated life-sciences commercial workflows, with the Vault CRM migration locked in through 2029 (top-20 customers committed), and no credible substitute routes around it.

| Sub-claim | Verdict | Evidence |
|---|---|---|
| Vault CRM: 200+ customers live, 5 of top 20 live, 14 of top 20 committed | CONFIRMED | Investor Day transcript, 2026-11-05 (CEO Peter Gassner): "over 200 customers live on Vault CRM, including five out of the top 20 biopharmas. 14 out of the top 20 have selected us." Finnhub/MarketBeat report of the same day, 2026-11-06, confirms verbatim. UCB selected Vault CRM on 2026-11-04 (company PR); Regeneron selected it in Aug 2026. |
| Migration completes end of 2029; ~halfway through | CONFIRMED | Investor Day transcript: "We're halfway through that adventure… We won't finish all the migrations until the end of 2029." |
| Veeva is the system of record for regulated life-sciences R&D, quality and commercial workflows | CONFIRMED in substance, with a scope note | Vault is embedded in clinical, regulatory, safety and quality workflows; the Q2 FY2027 10-Q and Investor Day materials describe the industry-specific data model. No source found contradicts the "system of record" characterisation for R&D/quality. |
| "Locked in through 2029" | OVERSTATED wording — soften | "Committed/selected" is what the company says; a selection is not an irrevocable lock-in, and 6 of the top 20 have *not* committed. The migration *runs* to end-2029; revenue is not contractually "locked in" through 2029 on the evidence shown. |
| "No credible substitute routes around it" | CONTRADICTED for the commercial/CRM slice; UNVERIFIED as a blanket claim | Salesforce Life Sciences Cloud went generally available in October 2025 (now branded Agentforce Life Sciences), with announced customers including AstraZeneca, Novartis, Takeda and Pfizer (TikaMobile guide, updated July 2026; Revosuite guide). IQVIA OCE is supported through 2029 while IQVIA partners with Salesforce. A 2026-11-19 check of Veeva's Q2 FY2027 10-Q coverage notes certain customers chose competitors and some expressed intent to move to Salesforce. The ballots themselves name Salesforce as "the credible alternative for the uncommitted 6 of the top 20" — so the "no credible substitute" phrasing in the moat summary contradicts the ballots' own caveat. For the regulated R&D/quality Vault applications (clinical, regulatory, safety), no equally credible drop-in substitute was found in this pass — that narrower claim survives. |

**Moat verdict:** the facts underneath the moat score (14 of 20 committed, migration to end-2029, industry-specific regulated workflows) are confirmed, but the summary sentence overclaims in two places: "locked in" should become "committed, with migration running to end-2029", and "no credible substitute" should become "no credible substitute for the regulated R&D/quality core; Salesforce Life Sciences Cloud is a credible substitute for the commercial CRM slice and is the destination for the 6 uncommitted top-20 accounts". The 8/10 moat score is not overturned by this — the evidence supports a strong moat with a live competitor — but the wording must change, because as written it asserts something the sources contradict.

## Other load-bearing ballot claims

| Claim | Verdict | Evidence |
|---|---|---|
| Investor Day 2026-11-05: CFO said Q3 will "meet or exceed" guidance on all metrics | CONFIRMED | 8-K filed 2026-11-06 (Exhibit 99.1); InvestorDataDigest: "said during its 2026 Investor Day on Nov. 5, 2026 that it expects third-quarter fiscal 2027 results to meet or exceed the preliminary guidance it gave on Aug. 26, 2026"; CMC Markets, 2026-11-18, same. Note the 8-K restates the August guidance and does *not* raise it — the remark pulls the beat forward without lifting the bar, exactly as the ballots describe it. |
| Four straight guide raises | PARTLY CONFIRMED — imprecise as stated | Confirmed: Q1 FY2027 (2026-06-03) raised FY27 to \$3.635–3.645B / ~\$9.05 from \$3.585–3.600B / ~\$8.85; Q2 FY2027 (2026-08-26) raised FY27 again to \$3.682–3.687B / ~\$9.21 (Trefis, 2026-10-23; company release). Q3 FY2026 (Nov 2025) raised FY26 to \$3.166–3.169B / \$7.93 (Zacks, 2025-11-21). Q4 FY2026 (Mar 2026) *set the initial* FY27 guide (\$3.585–3.600B / ~\$8.85) — that is not a raise of an existing guide. So the accurate statement is: the FY27 guide was raised twice (Q1, Q2), the FY26 guide was raised in Q3 FY2026, and Q4 FY2026 set the initial FY27 guide. "Raised every quarter in the last four" is true only if setting an initial guide counts as a raise; "four straight raises" should be corrected to "raised in three of the last four prints, and set-then-raised-twice for FY27". The underlying point — a serial-raiser record — survives. |
| ret_21d sell-off (-9.0%) | CONFIRMED | Finnhub candles: close \$316.80 on 2026-10-19 (21 trading days before 2026-11-17) → \$288.41 on 2026-11-17 = -8.96%. Finnhub also shows 5-session -9.28% and 1-month -12.5%, matching the dossier. The 52-week high \$325.99 (2026-10-22) and low \$148.05 (2026-04-10) are confirmed by the same source. |
| Q1/Q2 beat guide by \$25m-plus | CONFIRMED | Q1 FY2027: revenue \$882.9m vs guide \$855–858m = +\$24.9–27.9m (Tapebrief, from the 2026-06-03 release). Q2 FY2027: revenue \$928.0m vs guide \$902–905m = +\$23–26m. The "\$25m-plus" phrasing is at the top of the Q2 range and just below it at the low end; "\~\$25m" would be more precise. |
| Cash ~\$7.1–7.3B | CONFIRMED | Zacks, 2026-07-03: cash and short-term investments \$7.31B at 2026-04-30 (Q1 FY2027). Ballot B says ~\$7.3B (correct); ballot A says ~\$7.1B (slightly stale/low, immaterial). Net cash, no earnings-quality flags: not re-verified in this pass beyond the dossier's accrual/CFO figures — no contradicting source found. |
| \$6B 2030 run-rate target; TAM raised to \$30B from \$20B; Vault AI priced at 10% of Vault subscription | CONFIRMED | Investor Day, 2026-11-05: Finnhub/MarketBeat report 2026-11-06 (TAM \$30B, up from \$20B, "largely because of opportunities in industry-specific AI"; Vault AI "priced at 10% of the applicable Vault subscription fee"). The 2030 goal is reaffirmed in the same report and in The Inference, 2026-11-10. The Inference also notes the 2030 plan explicitly excludes AI products — confirming the dossier's point that the print cannot disappoint on AI revenue that was never guided. |
| Options-implied move ±6.9% | UNVERIFIED in this pass | No independent source for the ApexVol ±6.9% figure was retrieved in this verification; the dossier cites it without a retrievable quote. Do not treat it as confirmed. Its comparison against the realised average absolute move also weakens (see §3): on corrected next-session figures the realised average is ~7.3%, not 9.1%, so ±6.9% is roughly in line with history rather than below it. |

## What must change before the panel result is used

1. **Screen reaction series, VEEV second entry:** replace -2% with ~0% (-0.07% next-session, 2026-06-03 → 2026-06-04) and note the screen's -2% is the pre-release report-day move. Recompute the realised average absolute move as ~7.3% (not 9.1%) and soften every ballot sentence that leans on "implied move below history" — the gap is now ~0.4pp, not ~2.2pp.
2. **Moat wording:** change "locked in through 2029" to "committed, migration running to end-2029" and "no credible substitute" to "no credible substitute for the regulated R&D/quality core; Salesforce Life Sciences Cloud is a credible substitute for the commercial CRM slice (GA Oct 2025; AstraZeneca, Novartis, Takeda, Pfizer announced)".
3. **Guide-raise count:** change "four straight guide raises" to "FY27 guide raised twice (Q1, Q2 FY2027); FY26 guide raised in Q3 FY2026; Q4 FY2026 set the initial FY27 guide".
4. **Q4 consensus status:** update the dossier's "Q4 FY2027 published consensus — not found" to "published: Zacks, 2026-11-17, \$940.75m revenue / \$2.29 EPS", which coincides with the dossier's implied ~\$940m / ~\$2.29. No number changes.
5. **Minor:** Q1/Q2 guide beat is ~\$25m (Q2 range \$23–26m), not " \$25m-plus" in every case; ballot A's cash figure ~\$7.1B should read ~\$7.3B.

None of these changes alters the ranking: the date, the consensus bar, the Q2 beat-and-raise (+15.2%), the Q4 bar, the sell-off into the print, the Investor Day remark and the Vault CRM commitments all check out.

## Verdict

The winner survives verification. VEEV's report date (Wed 2026-12-03, AMC) is confirmed against the company's own 2026-11-12 release; the Q3 consensus (\$2.33–2.34 EPS, ~\$934m revenue) sits exactly on management's guide, confirmed by Zacks as of 2026-11-17; the most recent print was a genuine beat-and-raise that rose 15.2% the next session; the Q4 bar the guide will be judged against is now confirmed as a published consensus (\$940.75m / \$2.29, Zacks 2026-11-17), identical to the dossier's implied figure; the Vault CRM facts (200+ live, 5 of top 20 live, 14 of top 20 committed, migration to end-2029) are confirmed from the Investor Day transcript; and the sell-off into the print (-9.0% over 21 trading days) is confirmed from price candles. Two claims failed in their stated form and must be corrected before use: the screen's second reaction entry (-2% for Q1 FY2027 is the pre-release report-day move; the next-session reaction was flat, -0.07%), which also pulls the realised average absolute move from 9.1% to ~7.3% and largely closes the "implied move below history" gap; and the moat's "no credible substitute / locked in through 2029" wording, which overstates the position against a real Salesforce Life Sciences Cloud alternative for the commercial slice. The guide-raise count needs the same softening (two FY27 raises, not four straight). With those four corrections applied, the panel's conclusion — VEEV top, A second, ADSK third, with VEEV the only conditional Plan A — stands, and the dissenting lens D's caution (the beat is already half-announced by the Investor Day remark, and the guide is the trade) is, if anything, strengthened by the flat Q1 reaction: this name's prints are judged on the guide and the Vault CRM narrative, not on the beat.
