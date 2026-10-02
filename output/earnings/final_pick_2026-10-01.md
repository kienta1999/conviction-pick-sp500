# THE PICK — earnings mode — 2026-10-01 (RERUN under the updated protocol)

**Plan B — wait for the number.** No position before the print. Enter the post-earnings drift on
Fri 2026-10-09 only if all three trigger legs confirm (see the event plan).

> **NO SAFE FALLBACK.** The 12–18 month EV on this name is +13.9%, below the +15% guardrail. If
> the print goes wrong and the exit is ugly, there is no acceptable long-term landing spot at
> these scenario weights — this is a trade with no safe place to land, and the exit rule below
> is the entire risk control. Do not convert it into a hold.

> **RERUN NOTE (2026-10-01, evening):** this writeup supersedes this morning's 2026-10-01
> earnings outcome (a legitimate PASS). The rerun was ordered after the protocol update
> (commit f98f9e4 — screen now logs drops: `drops_2026-10-01.csv`, `scripts/why.py`). On a full
> fresh fetch (503/503) + screen, PEP — absent this morning after ranking 75th of 98 by
> composite on a stale cache and being trimmed at the final stage — survives the funnel
> (rank 47/50) and is the only name inside the ~10-day actionable window. The evaluation below
> is fresh as of the 2026-10-01 close.

## THE PICK

**PEP — PepsiCo, Inc.** Consumer Staples / Soft Drinks & Non-alcoholic Beverages. Market cap
~$175.5B. Price at pick **$125.60** (2026-10-01 close; new 52-week intraday low $125.53 set the
same session).

## One-paragraph thesis

PepsiCo reports Q3 2026 on Thu Oct 8 (BMO) into the most hated setup in its recent history:
three downgrades in two days (Deutsche Bank, JPMorgan, TD Cowen) plus at least four more target
cuts in the same week, a fresh 52-week low, a forward multiple near a decade low (~14× vs a
~25× 3–5y average), and estimate revisions running 7-down / 0-up on FY26. The quarter itself is
beatable — a flat $2.30 bar vs $2.29 a year ago, four straight beats on a FactSet basis, an easy
+1.3% organic comp — but the full-year guide is back-half loaded (H1 core cc EPS +3% vs a
+4–6% guide), ~1pt of it is tariff-refund claims, and the CFO already attached "low end" to it
at Q2, the print the stock fell −3.3% on. So the trade is not the print — it is the drift
*after* a confirmed beat with the guide reaffirmed clean, entered 10/09, held 20–40 sessions.
If the guide disappoints again, there is no trade, and that is the design working.

## The print

- **Date:** Thursday, October 8, 2026, **before market open**. Company press release
  (pepsico.com, 2026-08-25): materials ~6:00 a.m. EDT, analyst Q&A (Laguarta + Schmitt)
  8:15 a.m. EDT. **Verification status: CONFIRMED** (independent verifier, 2026-10-01,
  against the PR via PR Newswire and the Zacks calendar).
- **Quarter:** Q3 2026 (quarter ended Sep 5, 2026).
- **Consensus:** EPS **$2.30**, revenue **$24.97B** (FactSet/MarketBeat, Oct 1 — verified).
  FY2026: $8.57 / ~$99B. JPMorgan's own Q3 model sits at $2.29, below consensus;
  revisions are one-way down into the print.

## The record

Last four quarters (reported vs consensus EPS, surprise %, revenue growth, print-session
reaction — PEP reports BMO, so the reaction lands on the print day itself; verifier
correction applied):

| Quarter | Cons. EPS | Reported EPS | Surprise | Rev. growth (reported / organic) | Reaction (print day) |
|---------|-----------|--------------|----------|----------------------------------|----------------------|
| Q3 2025 | $2.26 | $2.29 | +1.3% | +2.7% / +1.3% | +4.2% (guide raised) |
| Q4 2025 | $2.24 | $2.26 | +1.0% | +5.6% / +2.1% | ~+5% (FY26 guide set) |
| Q1 2026 | $1.54–1.55 | $1.61 | +4.3% | +8.5% / +2.6% | +2.3% (guide affirmed) |
| Q2 2026 | $2.19 | $2.20 | +0.5% | +6.4% / +2.4% | **−3.3%** (guide qualified "low end") |

Screen record: 3-of-4 EPS beats on the screen's vendor basis (the "miss" is Q2 2026, $2.20 vs
a $2.21–$2.23 vendor series — on FactSet all four are beats; research reconciles both, see
dossier §3); beat→up rate 83.3% (5 of 6 measured); avg reaction +1.02%; avg absolute 4.18%;
worst −4.9%; last four: −3%, +2%, +5%, +4%.

## Why the beats are real

Revenue is growing underneath the EPS line: reported revenue +2.7% → +5.6% → +8.5% → +6.4%
over the last four quarters, CFO/NI 1.29 (cash-backed), no earnings-quality flags on the
screen. The honest qualification is organic growth: +1.3% → +2.1% → +2.6% → +2.4% — flat at
the bottom half of the +2–4% guide, not accelerating. The beats are earned, but they are thin
(+1.43% average surprise) and the Q3 bar ($2.30 vs $2.29 a year ago) is a bar set to be
cleared. This is a beatable quarter attached to an unproven year — which is why the guide,
not the EPS line, carries the trade.

## What's priced in (THE TRAP)

- **Run into the print:** −9.2% over 21 sessions, −10.5% over one month, −19.1% over six
  months; −26.8% below the $171.48 52-week high on the $125.60 close (−24.1% on the screen's
  cached-high basis); −13.2% vs the 200-day. `run_into_print_flag`: **false** — this is a
  selloff, not a run-up. **Priced-in score 3/10** (high = bad).
- **Options-implied move:** a clean earnings-expiry figure **could not be sourced tonight**
  (nearest data points — a 1.3% weekly-chain expected move and a ±2.9% model swing — are not
  the earnings straddle and are not used). The screen's realised proxy stands: **4.18%**
  average absolute reaction, worst −4.9%. Note this differs from the ~1.8% options figure
  recorded on 9/28–9/30, which tonight's research could not re-source; the ledger therefore
  records the realised proxy per the addendum's fallback rule.
- **Valuation:** forward P/E 14.1× vs its own 3–5y trailing average ~24.7–24.8× — roughly
  40% below its decade norm; dividend yield ~4.7%. Analyst mean target $151.70–$153.86 implies
  +21–23% upside, but the target trajectory is falling fast — targets have not caught up with
  the downgrades in either direction.
- **Positioning:** Hold consensus (5 Buy / 14 Hold / 1 Sell), short interest rising (+20.8%
  d/d late Sep), put/call elevated — hedging demand, not euphoria.
- **Verdict:** the good news is not in the price — the *bad* news is. The trap here is not a
  priced-in beat; it is that the market has already convicted the guide, and a mere
  "low end" reaffirm confirms the conviction. A beat alone does not spring this trap; only a
  clean guide does.

## The reaction record

83.3% of measured beats were rewarded (5/6), avg +1.02%, avg absolute 4.18%, worst −4.9%.
The pattern across the last four prints is unusually legible: the market **buys raises**
(+4.2% after the Q3 2025 raise, ~+5% after the FY26 guide was set), **rewards clean
reaffirms** (+2.3% on Q1), and **sells reaffirms-with-caveats** (−3.3% print day on Q2's
"low end" framing — verified −3.26%, $142.51 → $137.86). The reaction is judgeable and
tradeable precisely because it keys off the guide language — which is why the Plan B trigger
requires the guide, not just the beat.

## The guide

- **The bar:** FY2026 guide (unchanged since Dec 8, 2025): organic revenue +2–4%, core
  constant-currency EPS +4–6% (translated $8.55–$8.71). Street FY26 **$8.57** — already the
  low end. Q4 2026 consensus **$2.43–$2.44** (+7.5–8% YoY), FY2027 $8.96–$9.01 (verified).
- **Run-rate support:** H1 core cc EPS +3% (Q1 +5%, Q2 +1%) vs the +4–6% guide — landing
  even the floor needs H2 at ~+5%, the midpoint ~+7%. Q4 consensus embeds exactly that
  acceleration, and **no 2026 quarter has shown it**. Supports: ~1pt of FY growth is
  tariff-refund claims (one-off, timing-dependent), record productivity savings, easier
  comps, international strength. Organic revenue (+2.4–2.6% H1) sits inside the guide with
  no cushion.
- **8-quarter history:** FY25 guide cut in Q1 2025, reaffirmed, partially un-cut in Q3 2025;
  FY26 guide affirmed Dec 2025, Feb, Apr 2026; Jul 9, 2026 reaffirmed in words but qualified
  to "toward the low end" by the CFO. One cut, one partial un-cut, no clean raise in eight
  quarters — a serial reaffirmer drifting to "low end" is a de facto cut in progress.
- **Pulled forward?** No pre-announcement, no raise between quarters. The trim already
  happened *in language* at Q2. A Q3 reaffirm that repeats "low end" is already in the $8.57
  consensus; the Plan B trigger therefore requires the qualifier to be **dropped** (or the
  range narrowed up), not merely repeated.
- **Guide-risk score: 8/10** (high = bad).

## The fallback

If the exit is ugly, what you hold: the world's largest convenient-foods and beverage
distribution system — direct-store-delivery for Frito-Lay plus a bottling/fountain network
across >200 countries, ~$94B of 2025 net revenue ($93,925M per the 10-K — verified), a
portfolio of billion-dollar brands, irreplaceability **8.5/10** (research score; no customer
in-sources this and no AI-native substitute routes around physical distribution; deducted
for absent switching-cost lock-in, NA share losses to Coca-Cola and private label, and
GLP-1/health category exposure — the company's historical "22 billion-dollar brands"
boilerplate count could not be verified for 2026 and is not relied on). Balance sheet:
net debt/EBITDA 2.25×, CFO/NI 1.29, a dividend raised 54 consecutive years yielding ~4.7%.
A −15% gap to ~$107 (~12.5× the $8.57 consensus, ~5.5% yield) held 18 months reads as
opportunity, not disaster — the disaster case requires the moat itself to fail. It is a
business worth owning; it is simply not priced to compensate the *event* risk, which is why
NO SAFE FALLBACK stands on the Gate B numbers, not the quality.

## The event plan

**THE DISQUALIFIER CHECKLIST** (any ticked box = no Plan A; the name drops to Plan B or the
run passes):

- [ ] Stock up more than 15% over the 21 sessions into the print — **CLEAR** (−9.2%).
- [x] Either of the last two prints was a beat that the stock fell on — **TICKED** (Q2 2026:
  beat +$0.01 vs FactSet, fell −3.26% on the print day on the guide qualification).
- [ ] Guidance was raised between quarters — **CLEAR** (none; the only intra-quarter signal
  ran the other way — "low end" language at Q2).
- [ ] Report date not confirmed on the company's own IR page — **CLEAR** (confirmed
  10/08 BMO, company PR Aug 25, verified).
- [x] Expected move inside the name's own `reaction_avg_abs_move` — **TICKED** (Plan A
  scenario EV ≈ +0.3% vs a 4.18% average absolute move — the thesis would be the market's
  base case, not an edge).
- [x] Next-quarter consensus implies an acceleration the last 2–3 quarters have not shown —
  **TICKED** (Q4 +7.5–8% YoY vs H1 core cc +3%, Q2 +1%).

Three boxes ticked. **No Plan A trade.** The name proceeds on Plan B only.

**Which plan, and why:** Plan B — enter after the number. The reaction record says the
market sells reaffirms-with-caveats and buys clean guides; the guide is where this trade
lives or dies, and Plan B's entry costs little on a name whose realised up-moves run +2 to
+5%. Holding through would be paying for the quarter while the call decides the year.
**Gate A2, computed on the drift** (conditional on the trigger firing): +7% (p 0.55) /
+2% (p 0.30) / −4% (p 0.15) → expected drift **+3.85%** over 20–40 sessions — positive and
materially better than a coin flip. Gate A2 passes for Plan B.

**The pre-registered prediction:** **down / −3.0% / implied 4.2%.** Direction down,
expected move −3.0% on the print session (the Q2 pattern: a beat sold on guide fear — the
guide bar is the year's highest and the CFO pre-telegraphed "low end"). The implied column
records the name's realised average absolute move (4.18%, rounded 4.2) because no clean
options-implied figure could be sourced tonight — the addendum's fallback; it replaces the
1.8 recorded on 9/28–9/30, which is noted here so the change is auditable. Recorded in the
ledger at pick time; falsifiable at the close.

**Entry (Plan B):** on **Fri 2026-10-09**, and only if all three confirm: (a) beat on
**both** EPS and revenue vs $2.30 / $24.97B; (b) the FY guide **raised**, or reaffirmed
across the full +4–6% core cc EPS range with the **"low end" qualifier dropped** (a low-end
reaffirm is already the $8.57 consensus and does not count); (c) the first session (10/08)
**closes up**. If any leg fails — miss, soft guide, or a down first session — **no trade**;
the close row records `event_exit` at the pick price with "trigger never fired."

**Event scenarios (single-session sketches, anchored to the name's own reaction history):**

| Scenario | Sketch | Prob |
|----------|--------|------|
| Beat-and-clean-guide | +4% to +6% (the raise pattern: +4.2%, +5%) | 0.25 |
| Beat, guide qualified / in-line | −2% to −4% (the Q2 pattern: −3.3%) | 0.50 |
| Miss or guide cut | −5% to −9% (worst measured −4.9%; gap risk wider) | 0.25 |

Probability reasoning: the guide bar is the year's highest, H1 ran at +3% against a +4–6%
guide, ~1pt of the year is tariff refunds, and the CFO pre-telegraphed "low end" — the base
case is a beat sold on the guide, not a clean reaffirm. The clean-guide case needs the FY
range reaffirmed without the qualifier *and* Q4 endorsed; possible, not likely.

**Exit rule (written before the event):** Plan B — hold the drift **20–40 sessions**; exit
the full position the moment the stock **closes back below its reaction-day (10/08)
close** — the drift thesis is dead at that level, and that is an exit, not a dip to add to.
On a gap *down* at the open with no trigger: no position exists, nothing to exit. The event
exit rule, **not** the ledger bear target, governs this position (addendum §2). A
`kind=close` ledger row with `exit_reason=event_exit` is written at the end of the drift
horizon — or at the pick price with "trigger never fired" if the trigger fails. **Come back
by 2026-10-09/10-14 for the trigger check and by 2026-12-04 (40 sessions) for the drift
close.**

**What converts the trade into a hold:** nothing pre-stated. If the print is a genuine
beat-and-clean-guide that re-rates the FY27 $8.96–9.01 case, that decision is made fresh,
in daylight, as a new thesis — never in the moment as an excuse not to exit.

## Scenarios & expected value (the fallback, 12–18 months)

Bottoms-up on the business's drivers, anchored to the trailing-four-quarter baseline.
**Gate B: EV computed exactly as the other modes — it does not clear +15%, so this pick
publishes with the NO SAFE FALLBACK warning above.**

- **Bear ($112, −10.8%, by 2027-Q4):** the print misses AND the miss is structural — the
  affordability reset fails, Frito-Lay volumes keep eroding to GLP-1/private-label pressure,
  FY27 consensus collapses from $8.96–9.01 toward the low-$8s, tariff refunds slip. Multiple
  compresses to ~13×. *This is the case where you are genuinely stuck with it — and the bear
  target is the fallback case, not the trade's stop (the event exit rule governs).*
- **Base ($150, +19.4%, by 2027-Q4):** the business compounds roughly as the last four
  quarters did — low-single-digit organic revenue growth, core EPS growing into the $9 area
  by FY27, productivity offsets commodity pressure, multiple steady at ~16–17× as the guide
  drama passes.
- **Bull ($172, +36.9%, by 2027-Q4):** the beat-and-clean-guide cadence resumes, the Sep
  price hikes stick without volume loss, NA volumes inflect, and the multiple re-rates
  toward 19–20×. Needs the guide *and* the volume story to turn together — two things going
  right simultaneously, and the writeup says so.

**Probabilities:** bear 0.30 / base 0.50 / bull 0.20. Reasoning: the bear case is nearly as
probable as the base — three downgrades in two days, a "low end" guide already telegraphed,
a Q4 bar demanding unshown acceleration, ~1pt of the year riding on tariff refunds. The
bull needs two independent turns (guide + volume); weight it accordingly. Not a default
25/50/25.

**Expected value:** EV = 0.30×112 + 0.50×150 + 0.20×172 = **$143.00** vs $125.60 →
**+13.9%**. Below the +15% guardrail — hence NO SAFE FALLBACK (Gate B is a warning, not a
block, in this mode).

**Market-implied scenario:** the current price sits closest to **bear** — the stock is
priced as if the guide disappointment is already decided. A price at the bear case is
normally a green flag; here it is the market telling you the call must *disprove* the
"low end," not merely meet it. The stock trades well **below** the $151.70–$153.86 analyst
mean target — no above-target red flag; the flag is that the targets are falling toward the
price, not the reverse.

## Key swing factors

1. The FY guide language on Oct 8 — "low end" dropped, repeated, or cut.
2. Frito-Lay (PFNA) volume after the Feb price cuts and the Sep price hikes — recovery or
   structural share loss (JPMorgan channel data says still soft).
3. Whether Q4's +7.5–8% consensus growth is endorsed or dodged on the call.
4. PBNA beverage volumes (Q2 unit volume −4%, margin −90bp) and NA margin trajectory.
5. Tariff-refund timing — ~1pt of FY EPS growth is a one-off claim, not operations.

## EPIC driver table

| Driver | E | P | I | C-gap |
|--------|---|---|---|-------|
| The guide reset: market expects "low end"; a clean reaffirm re-rates FY27 | ✓ | — | ✓ | Our view: the call is about the guide, not the quarter; consensus prices a qualification that a clean reaffirm would disprove |
| Priced-for-failure setup: −26.8% off the high, ~14× forward vs ~25× history, 7 target cuts/downgrades in a week | ✓ | ✓ | — | Falsifiable: an up first session on a beat + clean guide confirms the washout was overdone, in public |
| Snack-volume durability under GLP-1 / affordability pressure | ✓ | — | ✓ | Deprioritized drivers (dividend, buyback pace) don't decide the next 40 sessions; volume does |

Why these three: the trade's P&L is decided by the guide language and the first session's
verdict; everything else is commentary. A thesis with no consensus gap would be buying
beta — here the gap is explicit: the market has convicted the guide before it is printed.

## Sizing note (from POLICY.md)

The owner's pre-committed policy, applied to this pick's numbers — not personalized advice.
raw = (143.00/125.60 − 1) / (1 − 112/125.60) = 0.1385/0.1083 = 1.28;
size = min(2% [earnings cap, POLICY.md §1.5], 2.5 × 1.28) = 2% → earnings halving → **1%** →
pilot-regime halving → **0.5%** of investable capital. The halving is not a penalty for this
doctrine but the reason it is survivable (addendum §6). One earnings position at a time;
15% system cap; cash-only. `size_pct` is left empty in the ledger for the owner to record
the deployed %.

## Holding period & exit plan

Expected hold: **days to weeks** — enter 10/09 on trigger, exit the drift in 20–40
sessions (~mid-November to early December) or on a close below the 10/08 reaction-day
close, whichever comes first: base target $150 by ~2027-Q4 and bull $172 by ~2027-Q4 are
the *fallback* landmarks, not the trade's targets; the trade's clock is the drift window.
The thesis-break triggers that **cancel** the trade before entry: a delayed filing or moved
report date, a negative pre-announcement, a peer print revealing sector-wide pressure, a
downward estimate-revision wave in the final week (already running — one more leg down in
FY27 estimates on the pricing story is a cancel, not a size-down), a CFO departure.
**Leverage-safety note:** a single-session gap of 10–20% is a normal outcome in this mode,
not a tail — this is the mode where leverage is most obviously destructive. Risk education,
not a recommendation.

## Key risks / what invalidates the thesis

- The guide is cut (not merely "low end") — the priced-for-failure setup becomes
  priced-correctly, and the fallback bear case becomes the base case.
- The price hikes accelerate volume loss — the affordability strategy's failure becomes
  structural, and PFNA's Q1 recovery is confirmed as a head-fake.
- Tariff refunds slip or shrink — the low end of the FY guide is missed on a one-off.
- A market-wide selloff swamps the idiosyncratic setup (the trigger's "up first session"
  leg exists for exactly this).
- The trap case: beat, clean guide, and *still fall* — because the whisper number was
  higher, or the Q4 bar the call endorses is one the business cannot clear.

## What was verified

Independent verifier subagent, 2026-10-01 (`parts/2026-10-01/verification.md`), from its own
searches against primary sources: (1) report date Thu 2026-10-08 BMO, company PR Aug 25 —
**CONFIRMED** in full; (2) Q3 consensus $2.30 / $24.97B — **CONFIRMED**; (3) reaction
spot-checks — magnitudes and the Q2 "low end" language **CONFIRMED** (Q2 −3.26%, Q1 +2.28%),
with one wording **CORRECTION applied**: PEP reports BMO, so both reactions landed on the
print session itself, not the next session — the record table above uses print-day
reactions; (4) the guide bar (FY26 guide, $8.57 Street, Q4 $2.43–44, H1 +3%, ~1pt tariff
refunds) — **CONFIRMED**; (5) all three downgrades (DB, TD Cowen Sep 28; JPMorgan Sep 29) —
**CONFIRMED**; (6) moat facts — >200 countries and ~$94B 2025 revenue **CONFIRMED**, the
"22 billion-dollar brands" count **UNVERIFIED** for 2026 (legacy boilerplate) and not relied
on; (7) price — $125.60 close and $171.48 high **CONFIRMED**, with the correction that the
final Oct 1 intraday low was **$125.53** (the $126.12 figure in early coverage was an
intraday snapshot) and the drawdown vs the high is **−26.8%**.

## The panel

No 4-lens panel: with one actionable name the screen, not a panel, made the decision
(skill's 1–3-name rule; a vote over one name is theater). One research subagent (fresh
full dossier as of the 2026-10-01 close) plus one independent verifier subagent (claims
above). No ballots exist and none were fabricated. Adjudication by the orchestrator on
Gate A/A2/B: three disqualifier boxes ticked → no Plan A; Gate A2 on the drift positive
(+3.85%) → Plan B queued; Gate B fails the +15% guardrail → NO SAFE FALLBACK.

## Screen metrics (from shortlist.json)

Price $125.60 (2026-10-01 close); market cap ~$175.5B; trailing P/E 16.9×; forward P/E
14.1×; −24.1% off 52-week high (screen basis; −26.8% vs the $171.48 nominal high);
−13.2% vs 200-day; analyst mean target $152.55 (screen) / $151.70–$153.86 (press), ~+21%
upside; composite 0.381 (rank 47/50); beat_up 83.3%; reaction avg +1.02% / abs 4.18% /
worst −4.9%; last four −3%, +2%, +5%, +4%; ret_21d −9.2%; run-into-print flag false;
earnings-quality flags none; net debt/EBITDA 2.25×; next earnings 2026-10-08 (dte 7).

---

*Research output, not financial advice. Dated 2026-10-01 (rerun). All scenario numbers are
research estimates, not guarantees.*
