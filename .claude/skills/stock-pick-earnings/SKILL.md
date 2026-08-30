---
name: stock-pick-earnings
description: Pick ONE S&P 500 stock to trade around its upcoming earnings print — or a ranked top-N — from the deterministic EARNINGS screen (reports within the window, market cap above $20B, four straight quarters of clearing consensus, revenue still rising, AND a history of the stock actually rising on those beats). Runs the Python funnel in --mode earnings, web-researches each survivor for the beat/raise track record, what consensus expects this quarter and next, the guide risk, the moat and AI-irreplaceability behind the numbers, and the setup risk, fans the dossier out to multiple Opus 4.8 subagents that independently nominate (or rank), then aggregates into one conviction pick or a ranked top-N with an explicit entry plan — by default entering AFTER the print on a confirmed beat-and-raise rather than gambling on the reaction — and a written exit rule. Use when the user asks to "pick an earnings play", "who reports next week", "find a beat-and-raise", "rank earnings candidates", or invokes /stock-pick-earnings. For trend-following names use /stock-pick-momentum; for beaten-down quality use /stock-pick-dip.
---

# Stock Pick (Earnings) — from S&P 500 to one earnings play (one pick, or a ranked top-N)

> Buys the **catalyst**: this skill positions around a scheduled earnings report
> from a company with a proven record of clearing the bar *and* of being paid
> for it. Unlike its two siblings there is **no SMA/trend gate at all** — a name
> qualifies whether it is above or below its 200-day average, because the thing
> expected to move the stock is the print, not the trend. Same quality funnel,
> different trigger.
>
> **The default entry is AFTER the number, not before it** (Plan B — see "The
> two entries"). A beat is not the tradeable variable; the reaction is, and this
> repo's own measurement puts the beat→up-move rate at ~54% with a 5.9% average
> absolute move. Holding through the print is available as Plan A, but it must
> be argued for.

**First, read `.claude/skills/shared/pick-protocol.md`** — it defines the whole
machinery (mode selection, Phase 0 shortlist build, triage, research fan-out,
the voting panel, Phase 3.5 verification, Phase 4A/4B aggregation, the picks
ledger, and the guardrails), including an **earnings-mode addendum** that
changes the horizon, the EV guardrail and the closing rule. Execute that
protocol with these parameters and the doctrine below:

- **MODE:** `earnings` → `OUT = output/earnings/`, screen command
  `uv run python scripts/fetch.py && uv run python scripts/screen.py --mode earnings`
  (the default window is now **45 days** — a whole reporting wave, split into
  "actionable now" and a watchlist at Phase 1; pass `--earnings-within 10` for
  this week's field only). The screen also drops names whose own beats have not
  historically been rewarded (stage 5d) and flags those that ran >15% into the
  print (stage 5e) — `--no-reaction-gate` disables the former if the user wants
  the unfiltered field.
- **THE TRAP (the protocol's veto/flag):** the priced-in print — defined below.
- **HORIZON:** an **event trade**. Plan B (default): enter after the print on a
  confirmed beat-and-raise, hold the drift ~20–40 sessions. Plan A (exception):
  enter before the print, exit into the reaction within days. The 12–18 month
  scenarios still get written, as the *fallback* — see "The two horizons" below.
  Either way the position is expected to be closed and a `kind=close` ledger row
  written on a timescale of days-to-weeks, not quarters.

Everything below is the earnings doctrine — the content the protocol's phases
consume.

---

## The doctrine

A great earnings play is **a large, high-quality company that has beaten
consensus four quarters running, with the revenue line still rising underneath
the beats, going into a print the market has not already fully priced.**

Three ideas, in order of weight:

1. **The record is the edge — but only the reaction record is tradeable.**
   Beat streaks persist more than random: managements guide conservatively and
   a company that has cleared its own bar four times running usually set the
   fifth bar the same way. The screen enforces that (fewer than 2 misses in
   four quarters, plus the size, direction and trend of the surprises).

   **The beat is not what you are paid on, though.** Measured across the nine
   names in the 2026-08-15 shortlist, a perfect 4/4 beat record converted into
   an up move only **~54% of the time**, mean reaction **+0.1%**, mean absolute
   move **5.9%** — a coin flip with 6% of variance. ADBE and VEEV each beat 4
   of 4 and *fell* on three of those four prints, and the old screen ranked both
   as top-tier candidates because it could not see reactions at all.

   So the screen now measures the second record too (stage 5d, `print_reaction`
   in `shortlist.json`): of a name's own past beats, how many were rewarded with
   an up move (`beat_up_rate`), by how much on average (`reaction_avg_move`),
   and how big the typical move is in either direction
   (`reaction_avg_abs_move` — the poor man's implied move, and the denominator
   of any honest event EV). A name that beats and falls every quarter is not a
   thesis that needs more care; it is a name whose good news is in the price by
   revealed behaviour, and the screen drops it before research is spent.

2. **Beats must be earned, not manufactured.** A beat streak on a falling
   revenue line, or one financed by accruals running ahead of cash, is a
   countdown, not a track record. The screen gates on TTM revenue growth > 0 and
   drops names with 2+ earnings-quality red flags — your job is to check the
   *narrative*: is the top line accelerating into the print, or is management
   squeezing a shrinking business to make the EPS number?

3. **The business has to be worth owning if the trade goes wrong.** You cannot
   exit a −15% gap at the price you wanted. The only thing that makes the left
   tail survivable is that the name is one you'd hold anyway — so the moat,
   irreplaceability and AI-disruption questions from the sibling skills apply
   here in full, as **downside insurance** rather than as the thesis.

**THE TRAP: the priced-in print.** A company can beat, raise, and *still fall
8%* — because the beat was smaller than the whisper number, the guide was merely
in line, or the stock had already run 25% into the event. This is the earnings
doctrine's exact analogue of momentum's disintermediation risk, and it is what
kills otherwise-correct theses. Weight heavily:

- **How much has the stock already moved into the print?** A name up hard in the
  four weeks before reporting has consensus optimism embedded in the price; the
  bar is no longer the published EPS estimate, it is the buy-side whisper. The
  screen now measures this (`ret_21d`) and **flags** any name up more than 15%
  over the 21 sessions into its print (`run_into_print_flag`) — it is a flag,
  not a gate, because a run-up can be a re-rating the print confirms. That
  judgement is the panel's; making it *visible* is the machinery's.
- **What does the options market imply?** The implied move is roughly the price
  of admission. A thesis that says "they'll beat by 5%" is not actionable if the
  implied move is ±9% — that beat is already the base case.
- **Has the guide been raised recently?** A raise between quarters pulls the
  good news forward and leaves the print with nothing to deliver.
- **Valuation vs the record.** A 4/4 beat streak at 45× forward earnings is a
  different bet than the same streak at 18×.

A name where the trap is credible is a **poor** earnings play even with a
perfect record — that is the veto in single-pick mode, the flag in ranked mode.

---

## The two entries — Plan B is the default

The doctrine justifies itself with **post-earnings-announcement drift**, and
PEAD is a *post*-print effect: the drift runs for weeks **after** the number is
public. Holding *through* the print buys the drift and, bundled with it, a
single-session coin flip on a reaction nobody can forecast — the part of the
trade with no edge in it. Those can be separated, and this mode separates them.

- **Plan B — buy the drift (the DEFAULT).** No position before the print. Enter
  only *after* the number, and only if all three confirm: (a) the company beat
  on EPS **and** revenue, (b) the guide for the next quarter was **raised or
  reaffirmed above consensus** — not merely "in line", (c) the market rewarded
  it, i.e. the first full session after the print closed **up**. Entry on the
  session after the reaction session; hold for the drift, typically 20–40
  sessions, with the exit rule written in advance. The gap risk is gone because
  the gap has already happened, in public, and you declined to be in it.
- **Plan A — hold through the print (the EXCEPTION).** Reserved for a setup that
  is demonstrably *not* priced: no `run_into_print_flag`, a strong
  `beat_up_rate`, and an expected move that clears the name's own
  `reaction_avg_abs_move`. Plan A must be **argued for** in the writeup against
  Plan B, in a paragraph headed "why not just wait for the number" — the burden
  of proof is on taking the gap risk, never on avoiding it.

Both plans use the identical funnel, dossier and panel. They differ only in
*when the order goes in*, and the writeup must state which plan it is
recommending, in its first two lines.

## The two horizons — read this before writing anything

Every earnings pick has to answer two separate questions, and the writeup keeps
them visibly apart:

- **The trade (primary).** Enter before the print, exit into the reaction —
  typically the session after, or on a defined rule (see the event plan below).
  This is what gets executed and what the `kind=close` ledger row records.
- **The fallback (insurance).** If the print gaps down and the exit is ugly, the
  12–18 month bear/base/bull scenarios say what you are left holding. These fill
  the ledger's target columns exactly as in the other two modes, so the scorecard
  and the track record stay comparable across all three doctrines.

Never let the fallback quietly become the plan. "It gapped down 12% but the
long-term thesis is intact" is how an event trade turns into an accidental
position, and it is the single most common way this strategy loses money. The
writeup must state the exit rule in advance, in numbers.

**Honest framing, to state plainly in every writeup:** holding through a print
is a bet on a *reaction*, not just on a business. Even a perfect read of the
fundamentals loses when the move was already priced. Historical hit rates on
"beat streak continues" are meaningfully better than a coin flip; the measured
hit rate on "stock rises after a beat" in this repo's own shortlist was **54%**,
with a mean absolute move of **5.9%**. The panel can select hard for the first
and only partly reason about the second — which is precisely why Plan B (enter
after the number) is the default and Plan A must be argued for.

State the sizing consequence too: at that hit rate and that variance, the edge
is thin, and POLICY.md §1.5's 2% cap → halved → halved again **is** the risk
control. This mode's standing value is that it is the only one producing
realized outcomes fast enough to teach the system anything.

---

## Phase 1 triage criteria (keep the ~12-15 strongest, or the whole field if smaller)

**Split the field first: actionable vs watchlist.** The screen now defaults to a
**45-day** window — a whole reporting wave, not one week — because a 7-day
window meant picking the best of whatever ~6 names happened to report that week:
the calendar, not the doctrine, made the decision. Rank the wave once, then
split it on `days_to_earnings`:

- **Actionable now** — reporting within ~10 days. These get the full research
  fan-out and the panel.
- **The watchlist** — everything further out, ranked and parked. It is a
  pre-vetted queue: when one of those dates comes within ~10 days, it enters as
  an already-screened candidate rather than as whoever the calendar coughed up.
  List it in `triage.md` and in the final writeup, with dates.

Hand the user both lists. If the actionable set is thin but the wave is rich,
say so plainly — "nothing worth trading this week, four names queued for the
week of X" is a good outcome, not a failed run.

**Then field size.** If the *actionable* set is still small:

- **~10+ candidates** → triage normally to ~12-15.
  (Widen to the watchlist only if the user asks for a bigger research run.)
- **4-9 candidates** → skip the cut, research all of them, and say so. There is
  nothing to triage away.
- **1-3 candidates** → say plainly that the *screen*, not the panel, has made
  this decision, and that a 4-lens vote over 2 names is theater. Offer the
  watchlist names whose dates are nearest, and let the user choose before
  spending the research budget.
- **0 candidates** → report the funnel, show which names fell out where and when
  the next reporting wave starts, and stop. No pick. Mid-quarter weeks are
  routinely empty and that is not a failure of the run.

Still write `triage.md` in every case (the protocol's Phase 1 rule), even when
nothing was dropped — "kept all 6, field was the whole field" is itself the
audit record.

Score each candidate on:

- **Reaction record — score this FIRST.** `beat_up_rate` (of its own past beats,
  how many were rewarded), `reaction_avg_move`, `reaction_avg_abs_move` and
  `reaction_last4` from the `print_reaction` block. The screen has already
  dropped names at or below a 50% beat→up rate, so everything you see cleared
  the coin flip; rank on how far above it they cleared. Where
  `print_reaction.note` says the rate is **not judgeable** (too few measured
  beats), treat the name as unproven on the doctrine's central question and say
  so — it was kept, not vindicated.
- **What it costs to be wrong.** `reaction_avg_abs_move` is the size of the bet.
  A name that routinely moves 9% is a different instrument from one that moves
  3%, whatever the thesis says, and `reaction_worst` is the gap you are
  underwriting.
- **Beat record quality** — not just `eps_beats_4q`, but the *size* of the beats
  (`eps_surprise_avg_4q`) and their *direction* (`eps_surprise_trend`). Four 0.4%
  beats is a company managing the number to the decimal; four 7% beats is one
  outrunning it. A shrinking beat is a warning even at 4/4.
- **Revenue underneath** — `rev_growth` (TTM), `rev_yoy_q` (latest quarter) and
  `rev_accel` (is the latest quarter faster than the trailing year?). Accelerating
  revenue into a print is the single best setup on the sheet.
- **Earnings-line direction** — `eps_yoy_q` and `eps_yoy_up_4q` from the
  *reported* EPS, which say whether the company is earning more than a year ago
  or merely beating a lowered bar.
- **Priced-in risk** — `ret_21d` and the `run_into_print_flag` the screen
  computed (up >15% into the print), plus `dist_52w_high`, `dist_sma200`,
  `forwardPE`. This is the trap; weight it here, not just at Phase 4. A flagged
  name is not disqualified, but it must earn its place against an unflagged one.
- **Fallback quality** — would you be content owning this for 18 months if the
  print goes badly? Moat, margins, balance sheet.

---

## Phase 2 research brief (per batch of tickers)

> Research these S&P 500 companies as candidates to hold through an upcoming
> earnings report: [TICKERS + company names + each one's screen-recorded
> earnings date]. For EACH, use web search to gather and report:
> 1. **The date, confirmed.** Verify the scheduled report date against the
>    company's own investor-relations page or press release, and state whether
>    it reports **before the open (BMO) or after the close (AMC)**. Our cached
>    date comes from Yahoo and is sometimes an estimate — say CONFIRMED /
>    ESTIMATED / MOVED, with the source and date. This is the load-bearing fact
>    of the entire thesis: if the date is wrong, there is no trade.
> 2. **The bar.** Consensus EPS and consensus revenue for the quarter being
>    reported, with the source and as-of date. Note any "whisper number" or
>    recent estimate revisions (up or down) in the last 30 days — a rising
>    estimate raises the bar the company must clear.
> 3. **The last four prints, one line each:** reported vs consensus EPS, revenue
>    vs consensus, what management guided, and **how the stock reacted the next
>    session (%)**. The reaction history matters as much as the beat history —
>    a company that beats every quarter and falls every quarter is telling you
>    its prints are priced in.
> 4. **Revenue and margin trend** — the last 4-8 quarters of reported revenue
>    growth and operating margin. Is the top line accelerating or decelerating
>    into this print? Quote the figures with dates.
> 5. **THE GUIDE — treat this as the most important item after the date.** A
>    beat with a weak guide is the single most common way this trade loses, so
>    the guide gets its own five questions, each answered with figures + dates:
>    (a) **Does the company guide at all**, and at what granularity (next
>    quarter, full year, revenue only, EPS too, or a refusal to guide)? A
>    non-guider cannot disappoint on guidance — a different risk profile, not a
>    safer one. (b) **What is consensus for the NEXT quarter and the full year**
>    — not just the quarter being reported. That forward number is the bar the
>    guide will be judged against, and it is where the "beat and dump" happens.
>    (c) **Does the company's own run-rate support that forward number?** Take
>    the last 2-3 quarters of revenue and margin and say plainly whether the
>    implied next-quarter figure is a continuation or an acceleration the
>    business has not yet shown. (d) **Guide history over the last 8 quarters** —
>    raised / reaffirmed / trimmed / cut each time, and what the stock did on
>    each. A serial raiser that merely reaffirms is a de facto cut. (e) **Has
>    the guide already been raised between quarters** (pre-announcement,
>    conference remark, analyst day)? That pulls the good news forward and
>    leaves the print nothing to deliver.
>    Then the rest of what's changed this quarter: segment data, channel checks,
>    peer results already reported (a peer's print is often the best available
>    read), FX, pricing actions, a big contract.
> 6. **How much is priced in** — the stock's move over the last 1 and 3 months,
>    where it sits vs its 52-week high, its forward P/E vs its own 3-5 year
>    range, and, if findable, the **options-implied move** for this print. Our
>    screen already computes a realized proxy (`reaction_avg_abs_move`) from the
>    last ~8 prints — report the options-implied move *against* it and say which
>    is larger. Say explicitly whether the setup looks crowded.
> 7. **Moat / AI-irreplaceability** — the downside insurance. Can its biggest
>    customers in-source this, could a substitute technology (including AI-native
>    competitors) route around it, and what protects it — patents, switching
>    costs, certification lock-in, scale, network effects, capital intensity?
>    Give an **irreplaceability score 0-10** (10 = nobody can replicate or
>    bypass it). Frame it as: if this gaps down 15% and I am stuck holding it
>    for 18 months, is that a disaster or an opportunity?
> 8. **Risks specific to THIS print** — what could produce a miss or a weak
>    guide (a tough comp, a known one-off in the base, macro exposure, a
>    segment already flagged as soft, litigation/regulatory overhang, a CFO
>    transition).
> 9. **Beat-likelihood score 0-10**, **guide-risk score 0-10** (10 = the forward
>    number the market is carrying looks unsupportable by the run-rate — HIGH IS
>    BAD), **priced-in score 0-10** (10 = the good news is entirely in the price
>    already — HIGH IS BAD), and a one-sentence verdict.
> 10. **Plan A or Plan B?** One line: is there a case for holding *through* this
>    print (not priced in, reaction record strong, expected move clears the
>    name's own average absolute move), or is this a wait-for-the-number name?
>    Default to B and say what would have to be true for A.
> Return a compact dossier per ticker. Prefer primary sources (earnings calls,
> 10-Q/10-K, company IR pages and PRs) and reputable financial press; include
> dates. Do not fabricate numbers — especially not consensus estimates, implied
> moves, or past reactions. If you can't find a figure, say "not found".

---

## Phase 3 — the four lenses

- **Agent A — Earnings-momentum analyst:** weight the beat/raise record, the
  size and trend of the surprises, estimate revisions, and revenue acceleration
  into the print. Wants the highest probability of a beat-and-raise.
- **Agent B — Setup / positioning skeptic:** weight what is already priced —
  `ret_21d` and the run-into-print flag, the implied move against the name's own
  `reaction_avg_abs_move`, the valuation vs its own history, and above all the
  **reaction record** (`beat_up_rate`, `reaction_last4`): what this stock has
  actually done with its own good news. This lens exists to hunt THE TRAP; it
  should be willing to reject the best fundamental candidate on setup alone and
  say so. It is also the lens that argues Plan B against Plan A.
- **Agent C — Quality/moat & irreplaceability investor:** weight the fallback.
  Margins, returns on capital, balance sheet, and above all
  **irreplaceability** — reject any name whose customers could realistically
  in-source it or that a substitute (including AI-native competition) could
  route around. Answer the question: which of these would I be *happy* to be
  stuck holding after a bad print?
- **Agent D — Contrarian/risk skeptic:** hunt for the print the market is
  mis-modelling in either direction, and explicitly weigh downside: the tough
  comp, the guide nobody is discussing, the segment that has been soft for two
  quarters. **Own the guide-down case specifically** — for its top pick, state
  the forward number the market is carrying and whether the run-rate supports
  it. Also allowed — and expected — to nominate **no trade** if the whole field
  is a coin flip.

**Single-pick ballot** — each subagent must return, in this exact structure:
> - **Top pick:** TICKER
> - **Runner-up:** TICKER
> - **Thesis (3-5 sentences):** why this print goes well and why that isn't
>   already in the price
> - **Key evidence from the record:** the single most compelling data point
>   (beat streak + size, revenue acceleration, guide history)
> - **Priced-in risk (THE TRAP):** how much is already in the stock — low /
>   medium / high, and why (run into the print, implied move, valuation,
>   reaction history)
> - **The guide:** the next-quarter number the market is carrying, and whether
>   this company's run-rate supports it. "Beat but guided soft" is the loss case
>   — name it explicitly or the ballot is incomplete.
> - **Plan A or Plan B**, with one sentence of justification. Plan A (hold
>   through the print) carries the burden of proof.
> - **Fallback if the print disappoints:** would you hold it 12-18 months? Why?
> - **Event scenario:** rough % move on a beat-and-raise / in-line / miss
> - **Top risk:**
> - **Conviction (1-10):**

**Ranked ballot** — per the protocol's ranked variant:
> A numbered list, best first: `RANK. TICKER — <=6-word reason (this lens)`.
> Then, for its **top 3 only**, 2–3 sentences on the most compelling record or
> setup data point, the reaction record, the guide risk, the priced-in risk, and
> a rough beat / in-line / miss move, ending with Plan A or Plan B.
> Then one line: which names it deliberately left out of its top N and why.
> (Rank the whole field when the field is smaller than the protocol's floor of
> 10 — never pad a ranking with names the screen didn't produce.)

---

## Doctrine-specific sections of the final writeup

In `final_pick.md`, between the thesis and the return scenario (see the
protocol's common template), include:

- **The print** — the confirmed date, BMO/AMC, the quarter being reported, and
  consensus EPS + revenue with sources. State the verification status of the
  date explicitly.
- **The record** — a small table of the last 4-8 quarters: consensus EPS,
  reported EPS, surprise %, revenue growth, and **the next-session stock
  reaction**. This table is the doctrine's core evidence; it makes both the beat
  streak and the priced-in problem visible in one place.
- **Why the beats are real** — revenue direction and acceleration, margin trend,
  and the earnings-quality metrics (accruals, cash conversion) that say the EPS
  line is cash-backed rather than manufactured.
- **What's priced in (THE TRAP)** — `ret_21d` and the run-into-print flag, the
  options-implied move against the name's own `reaction_avg_abs_move`, forward
  P/E vs the name's own range, and an honest verdict on whether the good news is
  already in the stock. If it is, say so even when the fundamentals are
  excellent.
- **The reaction record** — `beat_up_rate`, `reaction_avg_move`,
  `reaction_avg_abs_move`, `reaction_worst` and the last four reactions, with
  one line on what this stock has historically done with its own good news. If
  `print_reaction.note` says the rate is not judgeable, say that plainly rather
  than quoting a rate computed on two observations.
- **The guide** — the next-quarter and full-year numbers the market is carrying,
  whether the run-rate supports them, the 8-quarter raise/reaffirm/cut history,
  and whether anything was already pulled forward between quarters.
- **The fallback** — why this is a business worth owning for 18 months if the
  exit is ugly: the moat, the irreplaceability score, the balance sheet.

**The event plan (this mode's headline section — put it directly after the
thesis, before the scenarios):**

- **THE DISQUALIFIER CHECKLIST — run it first, in the writeup, as a visible
  list.** Any single box ticked means **no Plan A trade**; the name either
  drops to Plan B (wait for the number) or the run publishes as a pass. This
  exists because "everything looked great and it dumped anyway" is not a
  surprise, it is an un-run checklist — a great story can always talk its way
  past a bad setup in prose, so the check happens before the prose.
  - [ ] Stock up **more than 15%** over the 21 sessions into the print
        (`run_into_print_flag` is true).
  - [ ] **Either of the last two prints** was a beat that the stock fell on.
  - [ ] Guidance was **raised between quarters** (pre-announcement, analyst day,
        conference remark) — the good news is already out.
  - [ ] The report **date is not confirmed** on the company's own IR page.
  - [ ] The expected move is **inside the name's own `reaction_avg_abs_move`**
        (or inside the options-implied move where found) — the thesis is the
        market's base case, not an edge.
  - [ ] Next-quarter consensus implies an **acceleration the last 2-3 quarters
        have not shown** — the guide-down setup.
  State each as ticked/clear with its number. A ticked box is not a debate;
  it is the answer.
- **Which plan, and why.** Plan B (enter after the number, on beat + raised
  guide + a positive first session) is the default. If recommending **Plan A**
  — holding through the print — the writeup needs a paragraph headed **"why not
  just wait for the number"** that answers it with the reaction record and the
  expected move, not with conviction about the business.
- **The pre-registered prediction — write it before the event, record it in the
  ledger.** One direction (up/down), one expected % move, and the name's own
  `reaction_avg_abs_move` for comparison. These go in the ledger's
  `event_pred_dir`, `event_pred_move` and `event_implied_move` columns at pick
  time. Without them the close row records only what happened and never whether
  the panel *called* it, and this mode's whole justification is that it can
  generate that evidence quickly.
- **Entry:** when to be in by. **Plan B:** the trigger conditions and the
  session to enter on. **Plan A:** relative to the print — e.g. "by the close
  on the session before" — plus the current price.
- **Event scenarios with rough probabilities:** beat-and-raise / in-line /
  miss-or-weak-guide, each with an expected % move anchored to the name's own
  recent reaction history and the implied move where known. Say explicitly that
  these are scenario sketches over a single session.
- **Exit rule, written before the event:** the specific rule for taking the
  trade off. **Plan A:** "exit at the open of the session after the print, or on
  a defined intraday level; do not hold past T+2 regardless of direction."
  **Plan B:** the drift horizon in sessions (typically 20–40) and the level that
  ends it early — the drift thesis is dead the moment the stock closes back
  below its reaction-day close, and that is an exit, not a dip to add to.
  Include what to do on a gap *down* as well as a gap up: the down case is where
  a plan gets abandoned.
- **What converts the trade into a hold:** the narrow, pre-stated conditions
  (if any) under which the fallback thesis takes over instead of exiting — and
  the honest note that this must be decided now, not in the moment.

**Scenario drivers (for the protocol's 12–18 month bear/base/bull builds):**
these are the *fallback*, and they get built the same way as in the other modes
— bottoms-up on the business's drivers, anchored to the trailing-four-quarter
baseline. Bear = the print misses AND the miss reveals something structural
(the beat streak was accrual-financed, the revenue deceleration continues, a
segment is permanently impaired) — that's the case where you are genuinely stuck
with it. Base = the business compounds roughly as the last four quarters did.
Bull = the beat-and-raise cadence continues and the multiple holds.

Thesis-break exit triggers here look like: the report date moving (a delayed
filing is a red flag in itself), a negative pre-announcement, a peer's print
revealing a sector-wide problem, an estimate revision wave downward in the final
two weeks, a CFO departure before the print. Any of these before the event is a
reason to **cancel the trade**, not to size down. The leverage-safety note
should reflect that a single-session gap of 10-20% is a normal outcome here, not
a tail — this is the mode where leverage is most obviously destructive.

In `final_ranking.md`, the ranking table's doctrine scores are the
**beat-likelihood score**, the **guide-risk score** and the **priced-in score**
(flag high priced-in rather than vetoing it), plus **`beat_up_rate`**,
**`reaction_avg_abs_move`**, the **run-into-print flag**, the recommended
**plan (A/B)**, and each name's **report date** and **days to print** —
the reader needs the calendar to act on the list at all. Sort ties toward the
name reporting sooner only when the doctrine evidence is genuinely level. Each
top-3-5 thesis paragraph must cover the record, the **reaction record**, the
revenue direction, the **guide risk**, the priced-in verdict, and the fallback.
Keep the **watchlist** (names reporting beyond the actionable window) as its own
short table at the end, with dates — that queue is the point of screening a
whole reporting wave rather than a single week.

Phase 3.5 verification targets for this doctrine, in priority order:
1. **The report date and BMO/AMC**, against the company's IR page — this is
   non-negotiable and comes first. A wrong date invalidates everything.
2. The consensus EPS and revenue figures for the quarter.
3. The last-quarter surprise and the stock's reaction to it — and, because the
   screen's reaction figures come from a BMO/AMC-ambiguous heuristic (see
   `_reaction_at` in `fetch.py`), spot-check the **two most recent** entries in
   `reaction_last4` against the reported move. If they disagree materially, say
   so and prefer the researched figure.
4. The next-quarter consensus figure the guide will be judged against — the
   number that decides a beat-and-dump.
5. The moat's central factual claim.
