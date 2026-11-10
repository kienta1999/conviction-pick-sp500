> Run by: Muse Spark (muse-spark) — full panel

# Final pick — earnings — 2026-11-09 — ADSK (Plan B)

**NO SAFE FALLBACK — Gate B warning.** The 12–18 month fallback EV is +11.9%, below the +15% guardrail. This is a trade with no acceptable place to land if the print goes wrong: a bad gap becomes a permanent loss, not an inconvenience, unless the fallback conditions in "What converts the trade into a hold" are met. Size accordingly (see the sizing note) and do not let the fallback quietly become the plan.

**Plan B — enter AFTER the number.** No position before the print. Entry only on a confirmed beat-and-raise with a positive first session (see the event plan). The writeup states the plan in its first two lines, as the doctrine requires.

## THE PICK

**ADSK — Autodesk, Inc.** — Information Technology / Application Software. Market cap ~\$54.7bn. Price at pick: \$261.72 (screen price, 2026-11-06 close). Next earnings: **Tue 2026-11-24 AMC** (verified against the company's Nov 2 press release; call 5:00 PM ET).

## Thesis

Autodesk is the highest-probability beat in this field — eight consecutive non-GAAP EPS beats, a full-year guide raised at each of the last four prints, mid-teens revenue growth — attached to the most defensible moat in it: AutoCAD and Revit are the file-format standards of architecture, engineering, construction and manufacturing, with switching costs no large customer can dodge cheaply. The stock is −18% below its 52-week high and −12% year-to-date despite three consecutive guide raises, which is multiple compression, not euphoria. But the Q3 number itself is nearly pre-ordained — consensus sits at the midpoint of management's own guide — so the trade is not the quarter, it is the Q4 guide, which cannot be known in advance. That is why this is Plan B: own the business after the number confirms the guide, don't pay to hold through the print.

## THE EVENT PLAN

### THE DISQUALIFIER CHECKLIST — run first, before any prose

Gate A1. Any single box ticked means **no Plan A trade**. Two boxes are ticked, so there is no Plan A case; the pick is Plan B.

- [ ] 1. Stock up **more than 15%** over the 21 sessions into the print — **CLEAR.** `ret_21d` is +12.0%, below the 15% line.
- [x] 2. **Either of the last two prints** was a beat that the stock fell on — **TICKED.** Q2 FY27 (2026-08-27): beat +5.8% on EPS and raised the full-year guide, and the stock fell −3.7% the next session on a soft Q3 EPS guide. The Q1 FY27 reaction was not independently verified, but Q2 alone ticks the box.
- [x] 3. Guidance was **raised between quarters** — **TICKED.** The FY27 guide was raised twice since February: revenue midpoint \$8,135M (Feb) → \$8,185M (May) → \$8,320M (Aug), +\$185M cumulative; non-GAAP EPS midpoint \$12.43 → \$12.53 → \$12.56. Part of the August raise is MaintainX (~\$60M H2 revenue), part underlying. Some of the good news is already out.
- [ ] 4. The report **date is not confirmed** on the company's own IR page — **CLEAR.** Confirmed Tue 2026-11-24 AMC by Autodesk's own press release, 2026-11-02 (verified Phase 3.5).
- [ ] 5. The expected move is **inside the name's own `reaction_avg_abs_move`** — **CLEAR (marginal).** The expected beat-and-raise move is +5% to +7%, just outside the 4.9% realised average absolute move. No options-implied move was found, so there is no second measure to check against — treat this as a weak clear, not a strong one.
- [ ] 6. Next-quarter consensus implies an **acceleration the last 2-3 quarters have not shown** — **CLEAR.** Q4 FY27 consensus (Finviz, verified Phase 3.5) is EPS \$3.20 / revenue \$2.21B — +12% EPS and +13% revenue YoY vs Q4 FY26 (\$2.85 / \$1,957M), in line with the trailing growth rate. The guide is a continuation, not an acceleration.

**Boxes 2 and 3 are ticked. A ticked box is not a debate; it is the answer. No Plan A.**

### Which plan, and why

**Plan B — buy the drift.** Enter only after the number, and only if all three confirm: (a) the company beat on EPS **and** revenue (vs \$3.07 / \$2.13B), (b) the guide for the next quarter was **raised or reaffirmed above consensus** — Q4 FY27 guide at or above \$3.20 EPS / \$2.21B revenue, or the FY27 guide raised — not merely "in line", (c) the market rewarded it, i.e. the first full session after the print (Wed Nov 25) closed **up**. Entry on the session after the reaction session.

#### why not just wait for the number

That is exactly what this pick does. Holding through the print would mean paying for a Q3 beat that is nearly pre-ordained (consensus sits inside the company's own guide) while the payoff is decided by a Q4 guide that is unknowable in advance — and the freshest precedent is a beat-and-raise that fell −3.7% on a soft next-quarter guide. The reaction record says the market grades the guide, not the quarter: +2.4% on the Q3 FY26 raise, −3.7% on the Q2 FY27 beat-and-raise. The probability-weighted reaction across the three event scenarios is ~0% (see below) — a coin flip with 5% of variance. There is no edge in holding through; the edge is in entering only after the guide is confirmed good, when the −3.7% loss case is already excluded by construction.

### The pre-registered prediction

- Direction: **up**
- Expected move: **+5%** (the beat-and-raise scenario: a clean Q4 guide on top of the Q3 beat)
- Name's own `reaction_avg_abs_move`: **4.9%** (no options-implied move found)

These go in the ledger's `event_pred_dir`, `event_pred_move` and `event_implied_move` columns at pick time. Note the honest caveat: the probability-weighted reaction across all three scenarios is ~0% — the +5% is the beat-and-raise scenario the trade is conditioned on, not an unconditional forecast. The close row will judge whether the print moved as predicted.

### Entry

**Plan B:** enter Fri Nov 27, 2026 — the first trading session after the reaction session (Wed Nov 25) — only if the three trigger conditions above all confirm. Thu Nov 26 is Thanksgiving Day (market closed), so the entry session is the Fri Nov 27 short session; do not enter on Wed Nov 25 itself, whatever the reaction. If any trigger fails (EPS or revenue miss, Q4 guide at or below \$3.20 / \$2.21B, or the Nov 25 session closes down), **no position is opened** — a trade not taken is an outcome, and it still gets a close row with `exit_reason=event_exit` and `exit_price` equal to `price_at_pick`.

### Event scenarios with rough probabilities

Scenario sketches over a single session, anchored to the name's own recent reaction history (realised average absolute move 4.9%, worst −8.6%):

| Scenario | Probability | Expected move | What it looks like |
|----------|-------------|---------------|-------------------|
| Beat-and-raise (clean Q4 guide) | 45% | +5% to +7% | Q3 beats \$3.07 / \$2.13B and Q4 guide comes in at or above \$3.20 / \$2.21B with billings holding |
| In-line (beat Q3, soft Q4 guide) | 35% | −2% to −4% | Q3 beats but Q4 EPS guide lands below ~\$3.19, or FCF guidance narrows — the Q2 FY27 template (−3.7%) |
| Miss or guide cut | 20% | −8% to −10% | Q3 misses, or billings/RPO deterioration turns the revenue-quality question into the story |

Probability-weighted expected reaction: 0.45 × +6% + 0.35 × −3% + 0.20 × −9% = +2.7% − 1.05% − 1.8% = **−0.15%** — effectively zero. That is the honest number, and it is why this is Plan B: the print itself is a coin flip on the guide, and the trade only exists after the guide is known.

### Exit rule, written before the event

**Plan B:** hold for the drift, typically **20–40 sessions** from entry (Fri Nov 27, 2026 → ~late Jan 2027). Exit early — the drift thesis is dead — the moment the stock **closes back below its reaction-day (Wed Nov 25) close**; that is an exit, not a dip to add to. Exit at the end of the drift horizon regardless of direction. On a gap *down* after entry (a post-entry guide downgrade, a MaintainX writedown, a sales-reorg disruption surfacing), exit on the same rule — do not average down into a guide problem. The event exit rule, not the bear target, is what governs this position.

### What converts the trade into a hold

Narrow, pre-stated, decided now: the position converts to a hold only if the Nov 24 print delivers **all three** — (i) a Q4 guide clearly above \$3.20 / \$2.21B, (ii) Q3 billings growth re-accelerating to at or above revenue growth (reversing the +10% billings vs +16% revenue gap), and (iii) MaintainX shown accretive or at least not dilutive to margin — **and** the reaction is +7% or more. Then the 12–18 month base target (\$308) becomes the frame. Anything less, and the drift rule above applies. This must be decided now, not in the moment.

## THE PRINT

- **Date:** Tue 2026-11-24, after market close (AMC); conference call 5:00 PM ET the same day. **Verification status: CONFIRMED** — Autodesk press release, 2026-11-02 (Phase 3.5 verified against the company's own announcement; MarketBeat still labels the date "estimated" — aggregator lag).
- **Quarter being reported:** Q3 FY2027 (quarter ending 2026-10-31).
- **Consensus:** non-GAAP EPS **\$3.07**, revenue **\$2.13B** (MarketBeat; Finviz: EPS \$3.07, GAAP EPS est. \$1.85, revenue \$2.13B). Prior-year Q3 FY26: non-GAAP EPS \$2.67, revenue \$1.853B — the bar implies +15.0% EPS, +15.2% revenue YoY.
- **The bar is the company's own guide:** on Aug 27 Autodesk guided Q3 FY27 revenue \$2,125–2,140M and non-GAAP EPS \$3.04–3.09. Consensus sits at the guide midpoint. There is almost no daylight between Street and management for this quarter.

## THE RECORD

| Print | Consensus EPS | Reported EPS | Surprise % | Revenue growth | Next-session reaction |
|-------|---------------|--------------|------------|----------------|----------------------|
| Q2 FY27, 2026-08-27 AMC | \$3.12 | \$3.30 | +5.8% | +16% (\$2,046M) | −3.7% (verified: \$270.58 → \$260.66) |
| Q1 FY27, 2026-05-28 | ~\$2.84 | \$2.99 | +5.2% | +18% (\$1,934M) | not independently verified (screen +5%) |
| Q4 FY26, 2026-02-26 | \$2.63 | \$2.85 | +8.4% | +19% (\$1,957M) | not independently verified |
| Q3 FY26, 2025-11-25 AMC | \$2.50 | \$2.67 | +6.8% | +18% (\$1,853M) | +2.4% (verified: \$294.43 → \$301.38) |

Eight consecutive non-GAAP beats (Finviz table). The record is the doctrine's core evidence, and it makes both the beat streak and the priced-in problem visible in one place: ADSK beats the quarter, and the stock moves on the guide.

## Why the beats are real

Revenue direction: +18%, +19%, +18%, +16% YoY over the last four quarters — mid-teens growth, gently decelerating, still double-digit; underlying growth ex-new-transaction-model ~12%. Margin trend: Q2 FY27 GAAP operating margin 29% (+4ppt), non-GAAP 41% (+2ppt); FY27 non-GAAP margin guided ~39%. Earnings quality: the RECEIVABLES_OUTRUN flag is **benign** — accounts receivable fell from \$1,439M (Jan 31, 2026) to \$684M (Jul 31, 2026), the H1 cash-flow statement shows a \$753M decrease in receivables (collections exceeding new billings), deferred revenue is \$4,258M (+11% YoY), current RPO \$5,245M (+12%), Q2 free cash flow \$561M (+24% YoY), H1 operating cash flow \$1.47B. The flag is a seasonal billings-pattern artefact (Q4 is the big billings quarter), not earnings running ahead of cash. One watch item: billings (+10%) and RPO (+2%) lag revenue (+16%) — the revenue beat is partly recognition timing, and the backlog is growing much more slowly than recognised revenue.

## What's priced in (THE TRAP)

- `ret_21d` **+12.0%** (1 month +11.2%, 5 days +4.85%) — the worst run into the print in the field, but the stock sits **−18.2% below its 52-week high** (\$320.00) and **−11.6% YTD** despite three consecutive guide raises: multiple compression, not euphoria. No `run_into_print_flag` (below the 15% line).
- Options-implied move: **not found** — no implied-move figure for the Nov 24 print was retrieved. The screen's realised proxy is 4.9% average absolute move (worst −8.6%). Do not use a placeholder.
- Forward P/E: screen 18.4 (forward year unclear); MarketBeat 23.95; on FY27 non-GAAP EPS guidance \$12.52–12.60, \$261.72 is ~20.8x. No verified 3–5 year forward-P/E range was found — do not anchor on any single multiple as "cheap".
- **Verdict:** priced-in risk is **medium (5/10)**. A third consecutive raise is now the base case, and the Q2 lesson is that a soft next-quarter EPS guide gets punished even alongside a beat-and-raise. But expectations are elevated, not euphoric — the stock is a bounce off the lows, not a crowded long.

## The reaction record

`beat_up_rate` 0.625 (5 of 8 measured beats rewarded), `reaction_avg_move` +1.0%, `reaction_avg_abs_move` 4.9%, `reaction_worst` −8.6%. Last four (verified where noted): +2.4% (Q3 FY26 raise rewarded), −3.7% (Q2 FY27 beat-and-raise punished on a soft Q3 guide), Q1 FY27 and Q4 FY26 not independently verified. What this stock has historically done with its own good news: **it grades the guide, not the quarter.** A beat is not what you are paid on here — the Q4 guide is.

## THE GUIDE

- **Next-quarter consensus (Q4 FY27):** EPS **\$3.20**, revenue **\$2.21B** (Finviz, verified Phase 3.5, 2026-11-09). The FY27 company guide (Aug 27) implies Q4 of ~\$2,195M revenue and ~\$3.19 non-GAAP EPS — consistent with the Finviz consensus within 1%. Anchor the Q4 bar at \$3.20.
- **Full-year guide (Aug 27):** billings \$8,575–8,650M; revenue \$8,295–8,345M; non-GAAP margin ~39%; non-GAAP EPS \$12.52–12.60; GAAP EPS \$7.89–8.72; FCF \$2,725–2,750M. At the Aug 27 guide, FY consensus revenue (~\$8.21B) sat below the new guide midpoint — the guide was a raise above Street.
- **Does the run-rate support it?** Yes. H1 FY27 revenue \$3,980M implies H2 \$4,315–4,365M (Q3 ~\$2,133M midpoint + Q4 ~\$2,195M, +12% YoY vs Q4 FY26's \$1,957M). Non-GAAP EPS: H1 \$6.29 implies H2 \$6.23–6.31 (Q3 ~\$3.07 + Q4 ~\$3.19, +12% vs Q4 FY26's \$2.85). Both halves are internally consistent — no heroic Q4 required.
- **Guide history, last 4 prints — all raises:** Q3 FY26 raised FY26 (stock +2.4%); Q4 FY26 set FY27 with a "prudence" caveat for sales-reorg disruption; Q1 FY27 raised (rev \$8,155–8,215M, EPS \$12.40–12.65); Q2 FY27 raised again (rev \$8,295–8,345M, EPS \$12.52–12.60) but narrowed FCF down at the top end and issued a Q3 EPS guide below Street (stock −3.7%). A raise is necessary but not sufficient.
- **Already raised between quarters?** Yes — twice since February (FY27 revenue midpoint +\$185M cumulative). Part of the August raise is MaintainX (~\$60M H2 revenue), part underlying.
- **What changed this quarter:** MaintainX acquired 2026-08-03 (~\$3.53B net consideration): ~\$60M H2 FY27 revenue, margin-dilutive, ~\$45M transaction costs inside the FCF guide — Q3 is the first print showing its contribution and dilution. Sales reorganisation "proceeding as expected" — Nov 24 shows whether it is disrupting billings. New-transaction-model tailwind fading (was +\$137M revenue in Q4 FY26, ~2ppt in Q2 FY27) and multi-year-contracts annualisation — flagged by management as a FY27 headwind. Same-day peer print: Workday also reports Nov 24 — a same-day SaaS read-through.

## The fallback

If the print gaps down and the exit is ugly, this is what you are left holding: AutoCAD and Revit are the file-format standards of AEC and manufacturing; switching costs are enormous (retraining, libraries, workflows, client deliverables in DWG/RVT). **Correction (Phase 3.5): the "duopoly with Dassault" claim is contradicted — Morningstar names four wide-moat peers (Autodesk, Bentley, PTC, Dassault) and Siemens is at similar scale; it is an oligopoly of 4–5, not a duopoly. Wide moat and switching costs confirmed (Morningstar wide moat, "global industry standard").** Irreplaceability 8/10. Subscription revenue is recurring, FCF runs ~\$2.7B/yr, the balance sheet is net cash. Large AEC customers cannot in-source a CAD platform. AI cuts both ways: Autodesk embedding AI (generative design, Forma, automation) strengthens the moat if it works — AI-native text-to-CAD startups are the credible long-tail threat. A guide-driven dip is a buying opportunity in a business whose moat does not depend on one quarter's guide — **unless** billings/RPO softness accelerates into a genuine demand problem, which is the one thing that would break the fallback.

## Scenarios & expected value (the 12–18 month fallback)

Bottoms-up on the business's drivers, anchored to the trailing-four-quarter baseline (FY27 guide: revenue \$8,295–8,345M, non-GAAP EPS \$12.52–12.60, FCF \$2,725–2,750M). Label every number a research scenario, not a guarantee.

| Scenario | Price | % vs \$261.72 | By when | What has to happen |
|----------|-------|--------------|---------|-------------------|
| Bear | \$215 | −17.8% | 2027-Q2 | The print misses AND the miss reveals something structural: billings/RPO deterioration becomes a demand problem, MaintainX dilution worse than guided, transaction-model recognition unwinds. Multiple compresses to ~17x on FY27 EPS \$12.56. |
| Base | \$308 | +17.7% | 2027-Q2 | The business compounds roughly as the last four quarters did: FY27 guide met, Q4 guide firm, multiple ~20.8x on FY27 EPS holds. The analyst mean target (\$308.28) is the anchor. |
| Bull | \$340 | +29.9% | 2027-Q4 | The beat-and-raise cadence continues, Q4 guide comes in above \$3.20 with billings re-accelerating, and the multiple re-rates toward ~27x on FY27 EPS as the market pays for the moat again. |

Probabilities — never a default 25/50/25: **bear 25%** (billings softness is a real leading indicator and the Q2 precedent shows the market punishes guide weakness fast), **base 50%** (the most likely path — the guide is supportable on run-rate and the moat is intact), **bull 25%** (requires both a clean Q4 guide and a multiple re-rate; two things going right at once). **EV = 0.25 × \$215 + 0.50 × \$308 + 0.25 × \$340 = \$292.75**, vs the current price \$261.72 → **+11.9%**.

**Gate B: EV upside +11.9% is below the +15% guardrail — NO SAFE FALLBACK (see the warning at the top).** The pick still publishes (Plan B, conditional entry), but the fallback does not clear the bar. The market-implied scenario: the current price sits closest to **base** — at ~20.8x FY27 guide EPS, the market is paying for the guide being met, not for a re-rate. The stock trades **below** the analyst mean target (\$308.28, +17.8% upside).

## Key swing factors

1. **The Q4 FY27 EPS guide** (bar \$3.20) — the single variable that decides beat-and-raise vs beat-and-fall.
2. **Billings and RPO vs revenue** — billings +10% and RPO +2% vs revenue +16% is the leading indicator; a further deceleration turns the revenue-quality question into the story.
3. **MaintainX contribution and dilution** — first full quarter in this print; ~\$60M H2 revenue against margin dilution and ~\$45M transaction costs.
4. **Sales-reorg disruption** — management built "prudence" into FY27 for this; any sign it is biting shows up in billings linearity first.
5. **AEC/construction macro** — management has repeatedly cited "elevated macro uncertainty"; a cyclical turn hits the guide, not the quarter.

## EPIC driver table

| Driver | Effect | Predictability | Independence | Consensus-gap |
|--------|--------|----------------|--------------|---------------|
| Q4 guide quality (the print's real event) | ✓ moves value materially | ✓ a view is formable from the run-rate and the \$3.20 bar | ✓ the market systematically over-weights the headline beat and under-weights the next-quarter guide | The guide, not the quarter, is the trade — the market prices the beat, we price the guide |
| Subscription moat / switching costs (the fallback) | ✓ moves value materially over 18 months | ✓ formable from the installed base, RPO and FCF | — the market knows the moat; it is priced in the multiple | Our view differs only in that the moat makes a guide-driven dip a buying price, not a thesis break |
| Billings/RPO vs revenue (revenue quality) | ✓ moves value materially if it breaks | ✓ formable — the gap is already visible (+10%/+2% vs +16%) | ✓ the market is not yet pricing it (the Q2 reaction was about the EPS guide, not billings) | If billings re-accelerate, the quality question dissolves; if they decelerate, the bear case is the market's next narrative |

These three beat the deprioritised drivers (the Q3 beat itself — pre-ordained by the company's own guide; the MaintainX revenue contribution — small and dilutive; the Workday same-day read-through — a peer, not a driver).

## Sizing note (from POLICY.md §1.5)

Per the repo's pre-committed policy, applied with this pick's numbers: the earnings-mode per-pick cap is **2%** of investable capital, **halved** by the earnings rule to 1%, **halved again** by the pilot rule to **0.5%** of investable capital — that is the maximum size for this trade. One earnings position at a time: note that the 2026-11-08 OXY Plan B pick (entry Nov 11 on its trigger) is still pending — if that trigger fires and the position is still open, do not open ADSK on top of it. This is the owner's written policy being applied, never personalised advice. The halving is not a penalty for this doctrine but the reason it is survivable: at a ~54% historical beat→up rate and a ~5% average absolute move, the edge is thin and a single-session gap of 10–20% is a normal outcome here, not a tail.

## Holding period & exit plan

**Holding period:** the drift, 20–40 sessions from entry (Fri Nov 27, 2026 → ~late Jan 2027). **Base target \$308 by ~2027-Q2; bull target \$340 by ~2027-Q4 if the Q4 guide is clean and billings re-accelerate; exit if the stock closes back below its Nov 25 reaction-day close, or if any thesis-break trigger fires.** Thesis-break exit triggers: the report date moving (a delayed filing is a red flag in itself), a negative pre-announcement, a peer's print revealing a sector-wide problem (Workday Nov 24 is the same-day read), an estimate revision wave downward in the final two weeks, a CFO departure before the print. Any of these before the event is a reason to **cancel the trade**, not to size down. **Leverage-safety note:** a single-session gap of 10–20% is a normal outcome in this mode — this is where leverage is most obviously destructive. This is risk education, not a personalised leverage recommendation.

## Key risks

- **The Q4 guide is the event, not Q3** — a soft Q4 EPS guide (as in Q2) or cautious FY28 language repeats the −3.7% (or worse) reaction.
- **Billings/RPO softness** — if Q3 billings decelerate further, the revenue-quality question gets louder.
- **MaintainX dilution** — first full quarter of contribution and dilution; integration costs or a lower-than-\$60M H2 contribution hits margin and FCF guidance.
- **The trap (priced-in print):** +12% in 21 days into the print, a third consecutive raise now the base case — a mere reaffirm reads as a disappointment.
- **Valuation vs the record:** a 4/4 beat streak at ~20.8x FY27 guide EPS is a different bet than the same streak at 18x — and the multiple is on a guide that has already been raised twice.

## What was verified (Phase 3.5)

- **Report date + BMO/AMC — CONFIRMED:** Tue 2026-11-24 AMC, call 5:00 PM ET, per Autodesk's own press release, 2026-11-02.
- **Consensus EPS/revenue — CONFIRMED:** \$3.07 / \$2.13B across MarketBeat, Finviz, TipRanks; guide \$2,125–2,140M / \$3.04–3.09 from the Aug 27 company PR; consensus at the guide midpoint.
- **Last-quarter surprise + reaction — CONFIRMED:** Q2 FY27 EPS \$3.30 vs \$3.12 (+5.8%), reaction −3.7% verified from Finnhub closes (\$270.58 → \$260.66); Q3 FY26 EPS \$2.67 vs \$2.50 (+6.8%), reaction +2.4% verified (\$294.43 → \$301.38). The screen's +6% reaction entry matches neither recent print — the dossier's flag was correct.
- **Next-quarter consensus — CORRECTED:** the dossier's "not found" was wrong in the narrow sense — Finviz publishes Q4 FY27 EPS \$3.20 / revenue \$2.21B, which matches the FY-consensus arithmetic. Phase 4 anchors the Q4 bar at \$3.20, not "not found". The dossier was corrected before publishing.
- **Moat's central factual claim — MIXED:** standard status and switching costs confirmed (Morningstar wide moat, "global industry standard", 3–6 months to learn basics); "Dassault the only peer / duopoly" **contradicted** — Morningstar names four wide-moat peers (Autodesk, Bentley, PTC, Dassault) and Siemens is at similar scale. It is an oligopoly of 4–5, not a duopoly. The dossier was corrected before publishing.
- **Spot-checks:** OXY Mon 2026-11-09 AMC **CONFIRMED** (oxy.com PR Oct 1; call Tue Nov 10, 1 PM ET). NTAP Tue 2026-12-01 AMC **CONFIRMED** as a company target date (NetApp May 6 PR; AMC by pattern; no standalone Dec-1 webcast PR yet).

## The panel

- **Agent A (earnings-momentum):** ADSK, runner-up OXY, conviction 7/10. Highest-probability beat-and-raise; Plan B.
- **Agent B (setup/positioning skeptic):** OXY, runner-up NTAP, conviction 6/10. ADSK ranked 3rd — the +12% run into the print and the pre-ordained Q3 beat kept it from #1 on this lens; Plan B for ADSK.
- **Agent C (quality/moat):** ADSK, runner-up CTAS, conviction 7/10. CAD moat, net cash, ~\$2.7B/yr FCF; Plan B.
- **Agent D (contrarian/risk skeptic):** **NO TRADE**, runner-up OXY, conviction 6/10 in the no-trade call. Every print's payoff is decided by the guide, not the quarter; the field is a coin flip on guide. ADSK ranked 4th on this lens.

**Adjudication:** single-pick tally is ADSK 2 (A, C), OXY 1 (B), NO TRADE 1 (D — a field-level call, not a vote for OXY). ADSK also leads the Borda order 35 to OXY's 29, and has the best average placement (2.25 vs 3.75); ranked-ballot #1 votes are tied 2–2 (ADSK on A and C, OXY on B and D). The strict-doctrine order at the top would also put ADSK first — highest beat-likelihood (8), best moat (8/10), cleanest fallback. D's objection is honoured in the form of the pick, not by discarding it: the pick is **Plan B**, which is exactly the risk-managed form D's objection points toward — no position before the print, enter only after the guide is confirmed good, when the beat-and-fall loss case is already excluded by construction. A Plan A case would have failed D's objection and Gate A1 (boxes 2 and 3 ticked).

## Screen metrics (from shortlist_2026-11-09.json)

Price \$261.72; composite 0.592; market cap ~\$54.7bn; forward PE 18.4 (screen) / ~20.8x on FY27 guide EPS; analyst mean target \$308.28 (+17.8%); 4/4 beats (8/8), surprise avg +6.4%, surprise trend −1.96; beat_up_rate 0.625; reaction_avg_move +1.0%; reaction_avg_abs_move 4.9%; reaction_worst −8.6%; reaction_last4 "+6%, −4%, +5%, +2%" (ordering ambiguous — see the verification note); ret_21d +12.0%; run_into_print_flag false; dist_52w_high −15.6%; dist_sma200 +11.9%; rev_growth_ttm +11.9%; rev_yoy_q +16.1%; rev_accel +4.1%; net cash (net_debt/EBITDA −0.20). Earnings-quality flags: RECEIVABLES_OUTRUN — **benign** (see "Why the beats are real").

---

*This is research output, not financial advice. Dated 2026-11-09. Holding through a print is a bet on a reaction, not just on a business — even a perfect read of the fundamentals loses when the move was already priced. Historical hit rates on "beat streak continues" are meaningfully better than a coin flip; the measured hit rate on "stock rises after a beat" in this repo's own shortlist was 54%, with a mean absolute move of 5.9%.*
