> Run by: Muse Spark (Muse Spark) — full panel

# FINAL PICK — EARNINGS mode — 2026-10-06

> **⚠ NO SAFE FALLBACK (Gate B).** The 12–18 month fallback EV on this name is
> +6.9% (EV \$153.75 vs \$143.75), below the +15% bar. This publishes because the
> event trade clears Gate A, but be explicit with yourself: **this is a trade with
> no acceptable place to land if the print goes badly.** If the event exit rule
> below is not followed mechanically, a bad gap becomes a permanent loss, not an
> inconvenience. Do not let the fallback quietly become the plan.

**Plan B — wait for the number.** Do NOT hold through the print. Enter only AFTER
the number, on a confirmed beat-and-raise, then ride the ~20–40-session drift.

---

## THE PICK

**BNY — BNY Mellon Corporation.** Sector: Financial Services (custody bank / asset
servicing). Market cap ~\$98.7B. Price at pick: **\$143.75** (shortlist screen,
2026-10-06).

**Thesis.** BNY has beaten consensus for eight-plus straight quarters while the street
has repeatedly reset the bar lower — the number keeps moving away from consensus, not
toward it — and the forward number the stock actually trades on, the twice-raised FY26
revenue-growth guide of 10–11%, is arithmetic, not hope: H1 delivered \$11.11B, so H2
needs only ~\$5.5B per quarter, exactly the Q3 consensus of \$5.53B. The stock sold off
12.8% in a month on nothing company-specific, and the options market prices a fear
premium (~5.2% implied vs a ~3.0% historical average move) — the market treats this print
as a coin flip, but an 8-quarter streak on a \$62.6T custody base makes a genuine miss the
tail, not the base case. The trade is the guide, not the quarter: confirm the beat with
the guide reaffirmed-or-raised and a positive first session, then own the drift of the
world's largest custodian at a derated multiple.

---

## THE EVENT PLAN

### THE DISQUALIFIER CHECKLIST — run first, before any prose

| # | Condition | BNY |
|---|---|---|
| 1 | Stock up >15% over the 21 sessions into the print | CLEAR — 1-month -12.8% |
| 2 | Either of the last two prints was a beat the stock fell on | CLEAR — last two: +2.2% (Q1), +6.6% premarket (Q2) |
| 3 | Guidance raised between quarters (pre-announcement, analyst day, conference remark) | CLEAR — raised AT the Q1 and Q2 prints, not between quarters |
| 4 | Report date not confirmed on the company's own IR page | CLEAR — company PR confirms Thu 2026-10-15, BMO (verified Phase 3.5) |
| 5 | Expected move inside the name's own `reaction_avg_abs_move` (3.01%) | CLEAR — options-implied ~5.2% is OUTSIDE it (a fear premium, i.e. mispricing in the trade's favor) |
| 6 | Next-quarter consensus implies an acceleration the last 2–3 quarters have not shown | CLEAR — implied Q4 EPS ~\$2.30 and H2 ~\$5.5B/qtr fall out of the run-rate |

No box ticked → the Plan A case is not disqualified by the checklist. Plan B is chosen
anyway (see below), because the options market already prices the reaffirm pop at ~5% —
there is no mispricing edge in holding through the print, and the trade is management's
tone on the guide, which is only knowable after the call.

### Which plan, and why

**Plan B.** All four panelists independently landed on Plan B for their top picks; for BNY
specifically: the beat is the consensus expectation (8+ quarter streak), the priced move
(~5.2%) already covers the pop the thesis needs, and the swing factor is qualitative
(management's tone on the twice-raised guide) — none of which pays for gap risk. The
edge is post-print selection: only enter when the number, the guide, and the tape all
confirm.

### The pre-registered prediction (written before the event, recorded in the ledger)

- **Direction:** up
- **Expected move:** **+2.4%** — probability-weighted across the panel's print
  scenarios: beat-and-reaffirm/raise +5.5% (p≈0.55) / in-line +2% (p≈0.25) /
  miss-or-guide-trim −5.5% (p≈0.20) → 0.55×5.5 + 0.25×2 − 0.20×5.5 = +2.4%
- **Move already in the price:** ~5.2% (options-implied; the name's own
  `reaction_avg_abs_move` is 3.01%)

### Gate A2 (the expected move must beat a coin flip)

The print EV of **+2.4%** is positive and better than a coin flip (~0). For the Plan B
trade itself — conditional on the trigger — the drift EV is roughly
P(trigger ≈ 0.45–0.50) × E[drift | trigger ≈ +4%] ≈ **+1.8–2.0%**, positive and
conditional by design: the trigger does the selection work that holding through cannot.

### Entry

**Plan B trigger (all three required):** (a) BNY beats on EPS **and** revenue
(\$2.25 / ~\$5.53B consensus); (b) the FY26 10–11% revenue-growth guide is
**reaffirmed or raised** — a trim fails the trigger even on an EPS beat;
(c) the first full session after the print (Thu 2026-10-15) **closes up**.
**Enter on the session after the reaction session** (Fri 2026-10-16), at the open.
If any leg fails — including a beat with a trimmed guide — **no trade**; the close row
records `event_exit` with `exit_price` = `price_at_pick` and a thesis line saying the
trigger never fired.

### Event scenarios (single-session sketches, from the panel's ranges)

| Scenario | Probability | Expected move |
|---|---|---|
| Beat-and-reaffirm/raise | 0.55 | +4% to +7% |
| In-line, guide held (relief) | 0.25 | +1% to +3% |
| Miss or guide trim | 0.20 | −4% to −7% |

### Exit rule, written before the event

- **Take the trade off 20–40 sessions after entry** (drift horizon), or earlier if the
  stock **closes back below its reaction-day (10/15) close** — the drift thesis is dead
  the moment that happens; that is an exit, not a dip to add to.
- **Gap down on the print:** no entry is taken (trigger fails) — the down case is where
  plans get abandoned, and this one says: do nothing.
- **Do not hold past the drift horizon regardless of direction.** A `kind=close` row
  with `exit_reason=event_exit` is written at exit (or, if the trigger never fired, with
  exit_price = price_at_pick and the thesis line above). Come back and record it by
  ~2026-12-11 (40 sessions after entry) at the latest.

### What converts the trade into a hold

Only this, decided now: if the drift completes its 20–40-session course, no thesis-break
trigger has fired, and the Q3 print started a third consecutive guide-raise cadence with
fee growth still accelerating — then the fallback thesis (below) may take over instead of
exiting. Anything less, and the exit rule governs. This is decided **now**, not in the
moment.

---

## The print

**Thursday, October 15, 2026 — before market open. VERIFIED** (Phase 3.5, against the
company's own 2026 earnings-calendar PR: results ~6:30 AM ET, call 11:00 AM ET; an
aggregator's Oct-14 listing was confirmed wrong). Q3 FY2026. Consensus: **EPS \$2.25**
vs \$1.91 a year ago (+17.8%); **revenue ~\$5.53B** (+9.0% y/y). Sources: skncbba.com
preview (~2026-09-29), ainvest.com earnings page (~2026-09-19); both verified 2026-10-06.

## The record

| Quarter (reported) | EPS rep / est | Surprise | Revenue rep / est | Next-session reaction |
|---|---|---|---|---|
| Q3'25 (2026-10-16) | \$1.91 / \$1.76 | +8.5% | \$5.07B / \$4.95B | not found |
| Q4'25 (2026-01-13) | \$2.08 / \$1.97 | +5.6% | \$5.18B / \$5.11B | +1.9% |
| Q1'26 (2026-04-16) | \$2.25 / \$1.94 | +16.0% | \$5.41B / ~\$5.14B | +2.2% |
| Q2'26 (2026-07-15) | \$2.46 / \$2.16 | +13.9% | \$5.70B / \$5.35B | +6.6% (premarket) |

Eight-plus straight beats; the last four surprises run 8.5% → 5.6% → 16.0% → 13.9% —
large, not penny-managed. The screen's `beat_up_rate` is 87.5%.

## Why the beats are real

Revenue is **accelerating underneath**: \$5.07B → \$5.18B → \$5.41B → \$5.70B, YoY growth
~7% → 13% → 13.3%. Pre-tax margin 37% in Q1 (+833 bps y/y); ROTCE ~26–29%; CET1 11.0%.
Fee revenue broad-based (Securities Services +17%, Markets & Wealth +11% in Q1); NII
supported by reinvestment of maturing securities at higher yields. The screen's
LOW_CASH_CONVERSION flag is a **benign custody-bank artifact** (verified in research):
operating cash flow swings with client settlement balances and deposits — judge BNY on
CET1, ROTCE, and fee growth, not cash conversion.

## What's priced in (THE TRAP)

1-month −12.8% on nothing company-specific; ~12% below the 52-week high of \$165.84;
forward P/E ~15.7x on FY26 \$9.26 — in line with its own recent range, **no premium** for
a record Q2 and a twice-raised guide. Options-implied move ~5.2% vs the name's own
3.01% average absolute move — the market prices **more** than history, a fear premium,
not complacency. Put/call volume 0.37 (bullish flow). Verdict: **not crowded**. The one
unpriced thing is a trim of the twice-raised guide — a reaffirm is a win, a trim is the
bear case.

## The reaction record

`beat_up_rate` 87.5% · `reaction_avg_move` +2.51% · `reaction_avg_abs_move` 3.01% ·
`reaction_worst` −2.03% · last four (screen, most-recent-first): +5%, +2%, +2%, −2% —
no material disagreement with the researched moves (Phase 3.5 spot-check). What this
stock has done with its own good news: **rewarded it, modestly and consistently** —
no priced-in shrug in the record (contrast MS's Q2 +0.38% on a record beat, or PEP's
−3.26% on a beat).

## The guide

BNY does not guide EPS; it guides FY revenue growth (now **10–11%**, raised at both the
Q1 and Q2 prints), NII growth (+~10%), and an expense range (3–4%). The market's forward
number is the 10–11% itself. **Run-rate check:** 10–11% on 2025's \$20.1B = ~\$22.1–22.3B;
H1 delivered \$11.11B → H2 needs ~\$5.5B/quarter; Q3 consensus \$5.53B lands cleanly
inside that math; implied Q4 EPS ≈ \$2.30 (FY \$9.26 − Q1–Q3) fits as well. **The
run-rate supports the forward number.** Guide history: medium-term targets raised (Jan,
+1.9%) → FY guide raised to ~6% (Apr, +2.2%) → FY guide raised to 10–11% + div +19%
(Jul, +6.6% premarket). Nothing raised between quarters. The "beat but guided soft"
loss case is explicit and live: an EPS beat with a trimmed 10–11% guide sinks the stock
regardless — management's tone on the call is the whole swing factor.

## The fallback

If the exit is ugly, what you hold: the world's largest custodian — **\$62.6T**
assets under custody/administration, \$2.2T AUM (verified 2026-10-06, company PR),
90%+ of the Fortune 100, settlement infrastructure with enormous switching costs no
client can in-source and no AI-native entrant can route around. **Irreplaceability
9/10.** ROTCE 26–29%, CET1 11.0%, dividend raised +19% at the Q2 print. A guide-trim
quarter without credit damage is a price opportunity, not a thesis break.

---

## Scenarios & expected value (12–18 month fallback)

Bottoms-up on the custody franchise's drivers (fee growth on AUC/A, NII on the
reinvestment tail, ROTCE), anchored to the trailing run-rate (FY25 \$20.1B revenue,
FY26E \$9.26 EPS) and recent multiples (12–18x):

- **Bear — \$114 (−21%), by ~2028-Q1 (p=0.25):** Q3 trims the twice-raised 10–11%
  guide; fee growth stalls on a market drawdown; expenses land at the top of the
  3–4% range. FY27 EPS ~\$9.5 × 12x. This is the case where you are genuinely stuck
  with it — and the reason for the NO SAFE FALLBACK warning.
- **Base — \$159 (+11%), by ~2028-Q1 (p=0.50):** guide held, FY27 EPS \$10.26 ×
  15.5x — the run-rate arithmetic continuing, multiple in line with its own range.
- **Bull — \$183 (+27%), by ~2028-Q1 (p=0.25):** a third consecutive guide raise,
  fee acceleration on market beta, FY27 EPS ~\$10.75 × 17x.

Probabilities: base gets 50% because the run-rate arithmetic supports the guide and
the franchise is structural; bear gets 25% because the twice-raised guide is the
known fragility (a trim is the live bear case) plus market-beta on fees; bull gets
25% because a third straight raise is plausible but not the base case.

**Expected value:** EV = 0.25×114 + 0.50×159 + 0.25×183 = **\$153.75**, i.e. **+6.9%**
over \$143.75 — below the +15% bar, hence the warning at the top. All numbers are
research scenarios, not guarantees.

**Market-implied scenario:** the price sits near **base** — ~15.5x FY26 \$9.26, and the
street's average target (~\$157) is essentially the base target. The edge is the event
(the fear premium vs the streak), not the level; the stock does not trade above the
analyst mean target.

## Key swing factors

1. Q3 revenue vs \$5.53B and management's tone on the 10–11% guide — the entire trade.
2. Expense/NII commentary: expenses at the top of 3–4%? Deposit-margin compression?
3. Fee-revenue market beta: did Q3 markets/inflows support base-fee growth?
4. The 10/13–10/14 bank tape (GS, MS, BLK, BAC report just before) setting sector mood.
5. Normalization of Q1's FX/investment-gain tailwinds against the record-Q2 comp.

## EPIC driver table

| Driver | E | P | I | Consensus gap (falsifiable) |
|---|---|---|---|---|
| Guide credibility: the twice-raised 10–11% survives Q3 | ✓ | ✓ | ✓ | Our view: the guide is arithmetic (H1 \$11.11B → H2 ~\$5.5B/qtr), not hope. Falsified if Q3 revenue prints below ~\$5.4B or the guide is trimmed. |
| Beat-streak persistence: 8+ quarters, bar reset lower sequentially (\$2.46 → \$2.25) | ✓ | ✓ | ✓ | Streaks persist, but the market prices this print as a coin flip (5.2% implied vs 3.01% history) — the fear premium is the mispricing. Falsified by a genuine EPS miss. |
| Post-print drift on rewarded beats (beat_up 87.5%) | ✓ | ✓ | ✓ | PEAD on a confirmed beat-and-reaffirm is the entry vehicle; the drift, not the gap, is the trade. Falsified if the reaction-day close is retaken to the downside within days. |

Deprioritized: the 9/10 moat (fallback insurance, not the event edge) and valuation
(15.7x is fair, not a driver). A thesis with no consensus gap is just buying beta —
here the gap is explicit: the market's fear premium vs the streak's base rate.

## Sizing note (POLICY.md, applied — not advice)

`raw = (EV/price − 1) / (1 − bear/price)` = (153.75/143.75 − 1) / (1 − 114/143.75) ≈
0.34 → 2.5 × raw is capped by the earnings-mode **2% per-pick cap** → **halved** by
the always-on earnings halving (next earnings 10/15 is within 10 days by construction)
→ **halved again** by the pilot regime → **0.5% of investable capital, maximum**. The
halving is not a penalty for this doctrine but the reason it is survivable: a single
session can take 10–20% off on a guide the market didn't like. One earnings position
at a time; counts against the 15% system cap while open.

## Holding period & exit plan

**Holding period:** days, not months — the drift horizon is 20–40 sessions after the
10/16 entry; the position is expected to be closed with a `kind=close` row by
~2026-12-11. **Exit triggers:** (1) drift horizon reached; (2) close back below the
10/15 reaction-day close — exit immediately; (3) any thesis-break trigger fires:
the report date moves (a delayed filing is a red flag in itself), a negative
pre-announcement, a peer print revealing a sector-wide credit problem, a downward
estimate-revision wave in the final two weeks, a CFO departure — any of these before
the event **cancels the trade**, not sizes it down. **Leverage-safety note:** a
single-session gap of 10–20% is a normal outcome in this mode, not a tail — this is
the mode where leverage is most obviously destructive (education, not a
recommendation; no leverage multiple or position size is suggested here).

## Key risks / what invalidates the thesis

The trap case: an EPS beat with a trimmed 10–11% guide — the stock re-rates lower on
the guide regardless of the beat (this is the owned, explicit loss case). Also: a
tough record-Q2 comp; fee revenue is market-value-linked; expenses at the top of the
range; five of the six screened names are financials reporting 10/13–10/15, so a macro
or credit headline hits the field together.

## What was verified (Phase 3.5, independent subagent, 2026-10-06)

All five load-bearing claims **CONFIRMED** against primary sources: (1) report date
Thu 2026-10-15 BMO — company PR (release ~6:30 AM ET, call 11:00 AM ET); the
aggregator's Oct-14 listing is wrong; (2) consensus \$2.25 EPS / ~\$5.53B revenue;
(3) Q2'26 print — \$2.46 vs \$2.16, \$5.70B revenue, guide raised to 10–11%, div +19%,
+6.6% premarket; screen reaction history shows no material disagreement; (4) FY26
\$9.26 consensus and the 10–11% guide; (5) moat — \$62.6T AUC/A, \$2.2T AUM at
6/30/2026, company PR. Full findings:
`output/earnings/parts/2026-10-06/verification.md`.

## The panel

Four independent lenses, one dossier, all Plan B:

| Lens | Top pick (conviction) | Runner-up |
|---|---|---|
| A — earnings momentum | BLK (8) | MS |
| B — setup / positioning skeptic | MS (7) | BNY |
| C — quality / moat & irreplaceability | BNY (8) | BLK |
| D — contrarian / risk skeptic | BNY (7) | BAC |

**Tally (top=2, runner-up=1):** BNY 5 · BLK 3 · MS 3 · BAC 1 · GS 0 · PEP 0.
**Adjudication:** BNY wins the vote with two #1s and the runner-up nod from the setup
skeptic. The trap filter is clean: B (the lens that exists to hunt the trap) ranked BNY
#2 and called the elevated implied move a fear premium — mispricing in the trade's
favor, not a trap. BLK lost the vote despite the best fundamentals precisely because B
and D named it the trap (most-expected beat, "beat and still flat" the modal outcome);
MS lost it on Q2's priced-in-shrug template. The strongest, freshest doctrine evidence —
the streak plus the run-rate-supported twice-raised guide plus the derated price — all
point the same way.

## Screen metrics (from `shortlist_2026-10-06.json`)

| Metric | Value |
|---|---|
| Price / market cap | \$143.75 / ~\$98.7B |
| Days to earnings / next earnings | 9 / 2026-10-15 |
| Composite score | 0.694 |
| beat_up_rate / reaction_avg_move / reaction_avg_abs_move / reaction_worst | 87.5% / +2.51% / 3.01% / −2.03% |
| Trailing / forward P/E | 16.8x / 14.0x |
| Dist. from 52w high / dist. from 200d SMA | −12.8% / +5.5% |
| Earnings-quality flags | LOW_CASH_CONVERSION (benign custody-bank artifact) |

---

*Research output, not financial advice. Prepared 2026-10-06 from that day's evidence;
all figures dated and sourced in the dossier. Panel model: default worker model (see
report) — panelists ran on Muse Spark, not the Opus policy model; ballots are
independent samples regardless.*
