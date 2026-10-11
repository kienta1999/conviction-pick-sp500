> Run by: Muse Spark (muse-spark) — full panel

# Final pick — earnings mode — 2026-10-11

> **NO SAFE FALLBACK.** The 12–18 month fallback EV is +10.6%, below the +15% guardrail — if this print gaps down and the exit is ugly, there is no acceptable place to land; the position has no sound long-term home. This is a pure event trade on a days-long horizon. The event exit rule, not the bear target, governs this position.

## THE PICK

**BLK — BlackRock, Inc.**, Financials / Asset Management & Custody Banks. Market cap ~$173.1B (screen, 2026-10-11). Price at pick: $1,082.39 (Friday 2026-10-09 close; market closed this weekend). **Plan B** — enter only after a confirmed beat-and-raise with a positive first session; do NOT hold through the print.

## One-paragraph thesis

BLK is the cleanest event setup in a 13-name field: four straight beats with widening surprises (+7.3% average, trend +4.4), the field's only all-positive reaction streak (+7/+3/+6/+3, 87.5% beat-to-up rate), revenue accelerating into the print (+25.2% → +30.6% yoy) with the adjusted operating margin at a ~5-year high (45.9%), and no quarterly EPS guide to cut — the "beat but guided soft" loss case structurally cannot fire. The named mis-modelling is market-observable: options imply ~2.7% while the stock's own history averages 4.5% absolute — the event is under-priced relative to the record. But the disqualifier checklist ticks box 5 (probability-weighted expected print move +3.0% sits inside the 4.5% average absolute move), so holding through is not an edge: this is a Plan B drift trade — let the number prove itself, then ride the post-earnings drift that BLK's reaction record says follows a beat-and-raise.

## THE EVENT PLAN

### The disqualifier checklist (Gate A1) — run first, before any prose

- [ ] **Box 1 — Stock up more than 15% over the 21 sessions into the print.** CLEAR. ret_21d +1.9%; screen run_into_print_flag FALSE; 8–11% below the 52-week high.
- [ ] **Box 2 — Either of the last two prints was a beat that the stock fell on.** CLEAR. Last two beats printed +7% and +3% on the report-day sessions (BMO).
- [ ] **Box 3 — Guidance was raised between quarters.** CLEAR. BLK does not guide EPS/revenue; the last capital-return raise (buybacks $1.8B → $2B) was at the Q2 print (2026-07-15), not between quarters.
- [ ] **Box 4 — The report date is not confirmed on the company's own IR page.** CLEAR. Confirmed: Wednesday 2026-10-14, results before the NYSE open, call 7:30 AM ET, per BlackRock's own press release (2026-09-30). Phase 3.5 verifier re-confirmed today.
- [x] **Box 5 — The expected move is inside the name's own reaction_avg_abs_move (or inside the options-implied move where found).** TICKED. The probability-weighted expected print move is +3.0% (0.65 x +5% beat-and-raise, 0.25 x +1% in-line, 0.10 x −5% miss) — inside the 4.5% average absolute move. The market's base case already contains a move this size; holding through is not an edge.
- [ ] **Box 6 — Next-quarter consensus implies an acceleration the last 2–3 quarters have not shown.** CLEAR. Q4'26 consensus ~$15 (verified; the dossier's $16 was corrected) against a 9M run-rate of ~$13.2/quarter and revenue growing +25–31% yoy — a seasonal step-up Q4'25 also showed ($13.16), not an acceleration the business has not shown.

**One box ticked → no Plan A trade.** BLK drops to Plan B. (Three of four lenses voted Plan A on the beat record; the checklist overrules them — that is what the checklist is for.)

### Which plan, and why

**Plan B (enter after the number).** The default. Box 5 says the print itself is fairly priced — but the reaction record (4/4 beats, 4 of 4 rewarded, average +4.75%) says that WHEN BLK beats, the market pays and the drift continues. Plan B harvests the drift without paying for the fairly-priced event. No "why not just wait" paragraph is needed — we ARE waiting. Note the sequencing: GS and JPM report Tuesday 10/13 BMO and MS/BLK/BAC report Wednesday 10/14 BMO — if Tuesday's tape shows a September markets-activity collapse, stand down even if BLK's own bar looks winnable; the leading read is evidence, not background.

### The pre-registered prediction

- **Direction:** up. **Expected move:** +4.0% (drift after entry, conservative vs the +4.75% average of the last four reactions). **Implied move for comparison:** 4.5% (the screen's reaction_avg_abs_move; the live options-implied reference is ~2.7% — cheaper than history, which is the mis-modelling).
- Ledger: event_pred_dir=up, event_pred_move=4.0, event_implied_move=0.045.

### Entry

**Enter on Thursday 2026-10-15 (the session after the print) IF all three trigger conditions hold:** (1) BLK beat consensus on BOTH adjusted EPS ($14.29–14.36) and revenue ($7.45–7.52B); (2) net inflows were intact (the swing factor — Q1 missed the ~$150B Visible Alpha whisper with $130–136B; a repeat is the loss case) AND the capital-return posture was not cut (buyback/dividend); (3) the Wednesday 10/14 session closed POSITIVE. **If any condition fails, NO TRADE** — record the close row with exit_price=1082.39, exit_reason=event_exit, thesis "trigger never fired."

### Event scenarios with rough probabilities (single-session sketches for the print; the trade is the drift after)

- **Beat-and-raise (p=0.65):** +5% (the Q2'26 template: +9.6% EPS beat, 45.9% margin, record AUM $15.34T printed +7%; Q4'25: +6.2% beat printed +5.9%).
- **In-line / reaffirm (p=0.25):** +1%. Small beat, inflows merely in line — a quarter the market shrugs at.
- **Miss or weak inflows (p=0.10):** −5%. The loss case is an inflows miss, not an EPS miss — Q1'26's Visible Alpha shortfall is the template.
- **Gate A2 (on the drift):** probability-weighted expected drift +2.73% (0.65 x +4% drift, 0.25 x +0.5%, 0.10 x no trade = 0) — positive and materially better than a coin flip, so the drift trade clears A2. These are scenario sketches over single sessions, not guarantees.

### Exit rule, written before the event

**Plan B:** enter 10/15 on confirmed triggers; hold the drift for a stated horizon of **20–40 sessions**. End it early the moment the stock **closes back below its 10/14 reaction-day close** — the drift thesis is dead then, and that is an exit, not a dip to add to. On a gap DOWN at the open on 10/15 (trigger condition 3 fails): no trade was taken — there is nothing to exit. **Do not hold past the drift horizon regardless of direction.** Then write the kind=close ledger row with exit_reason=event_exit. The record must come back on or before **2026-11-06** to record the exit (print 10/14 + ~15 sessions, the earliest end of the drift window).

### What converts the trade into a hold

Nothing pre-stated. The fallback scenarios below are insurance, not the plan — and Gate B fails, so there is no sound hold to convert into. "It gapped down but the long-term thesis is intact" is not available here: this trade exits on its rule or it never should have been taken.

## The print

- **Date:** Wednesday 2026-10-14, before the NYSE open; call 7:30 AM ET. **VERIFIED** against BlackRock's own press release (2026-09-30) by the Phase 3.5 verifier — CONFIRMED, not an estimate, no move.
- **Quarter:** Q3 2026. **Consensus:** adjusted EPS ~$14.29–14.36 (AlphaStreet 15 analysts / MarketBeat, early Oct 2026; range $13.59–16.78), revenue ~$7.45–7.52B. Revisions −0.1% in 30 days (flat), +2.6% over 90 days. Implied +23.7% EPS / +15.5% revenue yoy.

## The record

| Quarter (reported) | Consensus EPS | Reported EPS | Surprise % | Revenue growth yoy | Next-session reaction |
|---|---|---|---|---|---|
| Q2'26 (2026-07-15) | $12.69 | $13.91 | +9.6% | +30.6% | +7% |
| Q1'26 (2026-04-14) | $11.48 | $12.53 | +9.2% | +27.0% | +5.3% |
| Q4'25 (2026-01-15) | $12.39 | $13.16 | +6.2% | +23.4% | +5.9% |
| Q3'25 (2025-10-14) | $11.19 | $11.55 | +3.2% | +25.2% | +3–4% |

The surprise is WIDENING (+3.2% → +9.6%) and every print was rewarded. Phase 3.5 spot-checked the two most recent reactions against reported moves: CONFIRMED (+6.6% and +5% figures reconcile with the table above within sourcing noise).

## Why the beats are real

Revenue growth is ACCELERATING into the print (+25.2% → +23.4% → +27.0% → +30.6% yoy), not decelerating; the adjusted operating margin expanded from ~30% to 45.9% (~5-year high) on operating leverage and mix shift (private markets via GIP/HPS, tech services +24% yoy in Q4'25). The deterministic screen raised one earnings-quality flag (LOW_CASH_CONVERSION); the research narrative check found it benign — asset managers collect fees in cash monthly/quarterly while GAAP operating cash flow trails on bonus/tax/seed-capital timing. The cash is real: $1.6B of buybacks in 2025, dividend raised 10%, buyback authorization raised to $2B. These are cash-backed beats, not accrual-financed ones.

## What's priced in (THE TRAP)

ret_21d +1.9% (steady, not extended); 8–11% below the 52-week high $1,219.94; below the 50-day SMA $1,110.93, above the 200-day $1,056.68. Forward P/E 16.9 vs trailing ~25.8 — compressed for a 20%+ EPS grower. **Options-implied move ~2.7%** (Oct 9) vs the screen's realized average absolute reaction **4.5%** — options are pricing LESS than the stock's own history. Verdict: the good news is NOT already in the stock. The one crowding signal is this panel itself — BLK was the pick on 10/4, 10/5, 10/7, 10/8 and 10/9 — but the market's own pricing shows no crowding; panel positioning is not market positioning.

## The reaction record

beat_up_rate 87.5% (of 8 measured beats, 7 were rewarded with an up move); reaction_avg_move +3.0%; reaction_avg_abs_move 4.5%; reaction_worst −5.9%; last four +7/+3/+6/+3. This is what the stock has historically done with its own good news: it pays. The rate is judgeable (8 measured beats, note=null) — kept and vindicated, not merely kept.

## The guide

BLK does not guide EPS or revenue. Its "guide" channels are organic base-fee growth color, expense cadence, and capital-return plans. The forward number the market carries: FY2026 consensus ~$55.7, FY2027 ~$65. Run-rate check: H1'26 adjusted EPS $26.44; H2 needs ~$14.6/quarter — credible against the Q3 bar given the margin trajectory and buybacks. Q4'26 ~$15 (verified; the dossier's $16 was corrected by the verifier) is the seasonally biggest quarter (Q4'25 carried $754M of performance fees) — demanding but consistent with the seasonal pattern. Capital-return "raise" history: Q4'25 dividend +10% and $1.8B buyback authorization (stock +5.9%); Q2'26 buybacks raised to $2B (stock +5–7%). A third capital-return step-up would read as a raise. The loss case is an inflows miss — Q1 missed the ~$150B Visible Alpha whisper with $130–136B — named explicitly because it is the one thing that turns a beat into a sell.

## The fallback

Why this is a business worth owning for 18 months if the exit is ugly — **with the Gate B warning above firmly attached**: $15.34T AUM scale; iShares liquidity network effects; Aladdin embedded in clients' risk infrastructure (multi-year switching); GIP/HPS private-markets moat; IBIT $54B AUM plus tokenization as offense. Moat score 9/10, the field's highest alongside PM. AI is a tailwind (Preqin data, Aladdin AI), not a threat. But the fallback EV is +10.6%, below the +15% guardrail — this is insurance with a known shortfall, not a second thesis.

## Scenarios & expected value (12–18 month fallback, not the trade)

Bottoms-up builds on the business's drivers, anchored to the trailing-four-quarter baseline:

- **Bear — $900 by 2027-Q2 (−16.9%):** what breaks: a market-beta drawdown compresses AUM, net inflows stall or reverse, the 45.9% margin mean-reverts on comp inflation. Quantified: AUM back toward $13T, base fees down mid-single digits. The bear target is recorded for the scorecard, but **the event exit rule, not the bear target, governs this position.**
- **Base — $1,240 by 2027-Q2 (+14.6%):** the most likely path: inflows continue at the H1 pace, margin holds 44–46%, AUM compounds with markets; the multiple stays compressed (16–18x forward).
- **Bull — $1,450 by 2027-Q4 (+34.0%):** what has to go right: AUM past $17T on sustained record inflows, private-markets mix lift, multiple re-rates toward 20x on durable 20%+ EPS growth. Multiple things must go right simultaneously — that compounds the risk.
- **Probabilities — 0.25 / 0.55 / 0.20, with reasoning:** bear at 0.25 because the margin is at a 5-year high and the print record, while clean, sits inside a bank-heavy earnings tape that could sour on macro; base at 0.55 because the revenue acceleration and margin expansion are broad-based and the moat is intact; bull at 0.20 because the multiple re-rating requires sustained perfection. Never a default 25/50/25. Honesty clause: the bear case is not the most probable scenario here, but it is a full quarter of the probability mass — respect it.
- **Expected value:** EV = 0.25 x 900 + 0.55 x 1240 + 0.20 x 1450 = **1197**, vs the current price $1,082.39 → **+10.6% upside, below the +15% guardrail.** This is exactly the NO SAFE FALLBACK case.
- **Market-implied scenario:** the current price sits between bear and base, closer to the middle of the range — not priced for perfection (the analyst mean target ~$1,316 sits above the base case; the stock trades below it). All numbers are research scenarios, not guarantees.

## Key swing factors

1. **Net inflows** — the quarter's trigger metric; a Q1-style Visible Alpha miss is the loss case.
2. **Tuesday's money-center tape (GS/JPM 10/13)** — markets-activity tone sets the read for BLK's markets-beta revenue.
3. **Adjusted operating margin** — 45.9% is a 5-year high; comp inflation is the threat.
4. **Performance fees in Q4** — the seasonal kicker that makes or breaks the FY $55.7 math.
5. **Fixed-income ETF flows** — $2.4B of MBS ETF redemptions in September, the largest since March 2020; a trend would bite.

## EPIC driver table

| Driver | E (moves value materially) | P (evidence-based view formable) | I (market systematically mis-weights it) | C (consensus gap, falsifiable) |
|---|---|---|---|---|
| Net inflows re-acceleration | ✓ | ✓ | ✓ | Our view: Q3 inflows beat the Visible Alpha whisper on AI-adjacent fixed-income demand; the market models a repeat of Q1's miss. Falsifiable: the reported long-term net inflows number. |
| Margin durability at ~46% | ✓ | ✓ | — | Our view: the mix shift (GIP/HPS, tech services) makes the margin structural, not cyclical; consensus treats it as peak. Falsifiable: the adjusted operating margin print. |
| Event mispricing (implied 2.7% vs 4.5% history) | ✓ | ✓ | ✓ | Our view: the options market underprices this print's historical variance. Falsifiable: the 10/14 session move. |

Why these beat the deprioritized ones: AUM level and dividend yield are the consensus story already in every note; the three above are where the quarter is actually decided and where the market's pricing is observably wrong (the implied-vs-realized gap). A thesis with no consensus gap is just buying beta — the third driver is the gap here.

## Sizing note (from POLICY.md)

The owner's written policy, applied to this pick: per-pick cap 2% of investable capital → earnings halving (this mode halves by construction) → halved again = **maximum 0.5% of investable capital**. One earnings position at a time — no second print position may be opened while this one is live. Counts against the 15% system cap while open. Cash-only: no margin, no leverage substitutes. This is the owner's policy being applied, not personalized advice — and the thin edge at this hit rate is exactly why the cap is the risk control.

## Holding period & exit plan

**The trade horizon is the drift: 20–40 sessions from the 10/15 entry.** Base target is not a price target for the trade — the trade exits on the drift rule: out at the end of the 20–40 session window, or early the moment the stock closes back below its 10/14 reaction-day close. Thesis-break exit triggers: the report date moving (a delayed filing is a red flag in itself), a negative pre-announcement, a peer's print revealing a sector-wide markets-activity problem, an estimate-revision wave downward in the final two weeks, a CFO departure before the print — any of these before the event is a reason to **cancel the trade**, not to size down. The 12–18 month fallback targets ($900 / $1,240 / $1,450) are insurance math for the ledger, not a hold plan. **Leverage-safety note:** a single-session gap of 10–20% is a normal outcome in this mode, not a tail — this is the mode where leverage is most obviously destructive; the position is cash-only by policy.

## Key risks and what would invalidate the thesis

- An inflows miss (the Q1 template) — the single most likely invalidation.
- A weak Tuesday tape (GS/JPM 10/13) showing September markets-activity collapse — stand down even with a clean BLK bar.
- Margin compression from comp inflation against the 45.9% high.
- Fixed-income ETF outflows accelerating.
- The panel's own book: this is the sixth straight panel to pick BLK — if the reasoning ever becomes "BLK because BLK," the process has failed; today's pick rests on the dossier and the checklist, not the streak.

## What was verified

Phase 3.5 (independent verifier subagent, findings in `output/earnings/parts/2026-10-11/verification.md` and `verification_13.md`): the 10/14 BMO date CONFIRMED against BlackRock's own press release (2026-09-30); consensus EPS/revenue figures CONFIRMED; the two most recent reactions spot-checked and reconciled (+6.6%, +5%); the FY2026 figure confirmed with a correction (Q4 consensus ~$15, not $16 — folded into the writeup); the moat's central factual claims ($15.34T AUM, 45.9% margin, Aladdin) CONFIRMED. The verifier also corrected the screen's stale Q4 math for BNY ($2.30–2.33, not $2.47–2.49) and GS's M&A share (~38% LSEG H1'26, not ~32%) — neither affects this pick. The earlier verifier pass's headline: CORRECT (minor, non-blocking).

## The panel

- **A — earnings-momentum (conviction 8):** BLK / BNY. "Cleanest beat-and-raise record." Plan A, conditional on Tuesday's tape.
- **B — setup/positioning skeptic (conviction 7):** CME / BLK. Picked CME on the cleanest setup (100% beat-up, 1.6% avg move, no crowding); BLK runner-up on cheap vol and clean reactions. Argued VRT last (unconfirmed date), ISRG 12th (run-up flag).
- **C — quality/moat (conviction 8):** CME / BLK. Deepest moat, non-event print; BLK runner-up (9/10 moat, cleanest reactions; Plan B, closest to A).
- **D — contrarian/risk skeptic (conviction 7):** BLK / WAB. Named the mis-modelling (implied 2.7% vs 4.5% history); Plan B, citing Tuesday's tape as the live leading indicator.

**Adjudication:** top-pick votes tied 2–2 (BLK: A, D; CME: B, C). The strongest, freshest doctrine evidence wins ties. CME's case is a high-probability non-event — its own record (1.6% average absolute move) says the print doesn't move the stock, which leaves no drift to harvest and no edge to price. BLK's case is a named, market-observable mispricing (the implied-vs-realized gap) plus the field's cleanest reaction record and a real drift payoff. The trap filter vetoes neither. BLK is the pick. WAB was the Borda #2 (45 pts, best average placement 2.75) but drew zero #1 votes — consensus, not conviction; it stays in the ranking. Gate A1's box 5 then moves the pick from the lenses' Plan A to Plan B — the checklist overrules the vote, as designed.

## Screen metrics (from `output/earnings/shortlist_2026-10-11.json`)

Price $1,082.39; market cap $173.1B; forward P/E 16.9; trailing P/E 25.6; analyst upside +21.6%; operating margin 35.1%; ROE 12.3%; revenue growth TTM +16.9%; dist_52w_high −8.1%; ret_12m −5.1%; ret_21d +1.9%; beat_up_rate 87.5%; reaction_avg_move +3.0%; reaction_avg_abs_move 4.5%; reaction_worst −5.9%; EPS beats 4/4, avg surprise +7.3% (trend +4.4); composite 0.707.

## Watchlist (reporting beyond the actionable window)

CSX (2026-10-21, d=11 — the 2026-10-12 screen may promote it), CINF (2026-10-26), V/KO (2026-10-27), APH/GRMN/GOOGL/FTNT/GOOG/BIIB/ADP/META (2026-10-28), SNDK/INCY/LLY/CAT/HWM/MPWR/DXCM/AME/BMY/MA (2026-10-29), CBOE/REGN (2026-10-30), IDXX (2026-11-02), AMGN/PFE (2026-11-03), APP/CPAY/EW/EBAY (2026-11-04), MNST/PH/RL/COP (2026-11-05), OXY (2026-11-09), PTC (2026-11-11). Dates are Yahoo-sourced screen estimates, not yet confirmed against company IR pages.

---

*Research output, not financial advice. Prices as of the Friday 2026-10-09 close. Model: Muse Spark (muse-spark), full panel, 13-name field, 4 research batches + 4 lens panelists + 2 verification passes, run 2026-10-11.*
