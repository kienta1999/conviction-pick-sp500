---
name: stock-pick-earnings
description: Pick ONE S&P 500 stock to hold through its upcoming earnings print — or a ranked top-N — from the deterministic EARNINGS screen (reports within the next N days, market cap above $20B, four straight quarters of clearing consensus, revenue still rising). Runs the Python funnel in --mode earnings, web-researches each survivor for the beat/raise track record, what consensus expects this quarter, the moat and AI-irreplaceability behind the numbers, and the setup risk, fans the dossier out to multiple Opus 4.8 subagents that independently nominate (or rank), then aggregates into one conviction pick or a ranked top-N with an explicit pre-print entry and post-print exit plan. Use when the user asks to "pick an earnings play", "who reports next week", "find a beat-and-raise", "rank earnings candidates", or invokes /stock-pick-earnings. For trend-following names use /stock-pick-momentum; for beaten-down quality use /stock-pick-dip.
---

# Stock Pick (Earnings) — from S&P 500 to one earnings play (one pick, or a ranked top-N)

> Buys the **catalyst**: this skill positions into a scheduled earnings report
> from a company with a proven record of clearing the bar. Unlike its two
> siblings there is **no SMA/trend gate at all** — a name qualifies whether it
> is above or below its 200-day average, because the thing expected to move the
> stock is the print, not the trend. Same quality funnel, different trigger.

**First, read `.claude/skills/shared/pick-protocol.md`** — it defines the whole
machinery (mode selection, Phase 0 shortlist build, triage, research fan-out,
the voting panel, Phase 3.5 verification, Phase 4A/4B aggregation, the picks
ledger, and the guardrails), including an **earnings-mode addendum** that
changes the horizon, the EV guardrail and the closing rule. Execute that
protocol with these parameters and the doctrine below:

- **MODE:** `earnings` → `OUT = output/earnings/`, screen command
  `uv run python scripts/fetch.py && uv run python scripts/screen.py --mode earnings`
  (add `--earnings-within N` when the user gives a window other than 7 days).
- **THE TRAP (the protocol's veto/flag):** the priced-in print — defined below.
- **HORIZON:** an **event trade**. Enter before the print, exit into the
  reaction. The 12–18 month scenarios still get written, as the *fallback* — see
  "The two horizons" below. This is the one mode where the position is expected
  to be closed, and a `kind=close` ledger row written, within days.

Everything below is the earnings doctrine — the content the protocol's phases
consume.

---

## The doctrine

A great earnings play is **a large, high-quality company that has beaten
consensus four quarters running, with the revenue line still rising underneath
the beats, going into a print the market has not already fully priced.**

Three ideas, in order of weight:

1. **The record is the edge.** Beat streaks persist more than random — post-
   earnings-announcement drift and the tendency of managements to guide
   conservatively are among the most durable effects in the literature. A
   company that has cleared its own bar four times running usually set the fifth
   bar the same way. The deterministic screen has already enforced this: fewer
   than 2 consensus misses in the last four quarters, plus the size, direction
   and trend of the surprises feeding the composite.

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
  bar is no longer the published EPS estimate, it is the buy-side whisper.
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
"beat streak continues" are meaningfully better than a coin flip; historical hit
rates on "stock rises after a beat" are much closer to one. The panel is
selecting for the first and can only partly reason about the second.

---

## Phase 1 triage criteria (keep the ~12-15 strongest, or the whole field if smaller)

**Field size first.** The earnings window is a hard calendar constraint, so
unlike the sibling skills the shortlist is often small. Before triaging, tell the
user how many candidates the screen produced, and:

- **~10+ candidates** → triage normally to ~12-15.
- **4-9 candidates** → skip the cut, research all of them, and say so. There is
  nothing to triage away.
- **1-3 candidates** → say plainly that the *screen*, not the panel, has made
  this decision, and that a 4-lens vote over 2 names is theater. Offer to widen
  the window (`--earnings-within 14` / `21`) and rerun, and let the user choose
  before spending the research budget.
- **0 candidates** → report the funnel, show which names fell out where and when
  the next reporting wave starts, and stop. No pick. Mid-quarter weeks are
  routinely empty and that is not a failure of the run.

Still write `triage.md` in every case (the protocol's Phase 1 rule), even when
nothing was dropped — "kept all 6, field was the whole field" is itself the
audit record.

Score each candidate on:

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
- **Priced-in risk** — how far the stock has run recently (`ret_12m`,
  `dist_52w_high`, `dist_sma200`) and what it costs (`forwardPE`,
  `analyst_upside`). This is the trap; weight it here, not just at Phase 4.
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
> 5. **Guidance and what's changed this quarter** — the company's own outlook
>    for the quarter being reported, plus anything since the last print that
>    moves the number: pre-announcements, analyst day, segment data, channel
>    checks, peer results already reported (a peer's print is often the best
>    available read), FX, pricing actions, a big contract.
> 6. **How much is priced in** — the stock's move over the last 1 and 3 months,
>    where it sits vs its 52-week high, its forward P/E vs its own 3-5 year
>    range, and, if findable, the **options-implied move** for this print and
>    the average absolute move over the last 4 prints. Say explicitly whether
>    the setup looks crowded.
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
> 9. **Beat-likelihood score 0-10**, **priced-in score 0-10** (10 = the good news
>    is entirely in the price already — HIGH IS BAD), and a one-sentence verdict.
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
  the run into the print, the implied move, the valuation vs the name's own
  history, the reaction history of past beats. This lens exists to hunt THE
  TRAP; it should be willing to reject the best fundamental candidate on setup
  alone and say so.
- **Agent C — Quality/moat & irreplaceability investor:** weight the fallback.
  Margins, returns on capital, balance sheet, and above all
  **irreplaceability** — reject any name whose customers could realistically
  in-source it or that a substitute (including AI-native competition) could
  route around. Answer the question: which of these would I be *happy* to be
  stuck holding after a bad print?
- **Agent D — Contrarian/risk skeptic:** hunt for the print the market is
  mis-modelling in either direction, and explicitly weigh downside: the tough
  comp, the guide nobody is discussing, the segment that has been soft for two
  quarters. Also allowed — and expected — to nominate **no trade** if the whole
  field is a coin flip.

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
> - **Fallback if the print disappoints:** would you hold it 12-18 months? Why?
> - **Event scenario:** rough % move on a beat-and-raise / in-line / miss
> - **Top risk:**
> - **Conviction (1-10):**

**Ranked ballot** — per the protocol's ranked variant:
> A numbered list, best first: `RANK. TICKER — <=6-word reason (this lens)`.
> Then, for its **top 3 only**, 2–3 sentences on the most compelling record or
> setup data point, the priced-in risk, and a rough beat / in-line / miss move.
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
- **What's priced in (THE TRAP)** — the run into the print, options-implied move
  if found, forward P/E vs the name's own range, and an honest verdict on
  whether the good news is already in the stock. If it is, say so even when the
  fundamentals are excellent.
- **The fallback** — why this is a business worth owning for 18 months if the
  exit is ugly: the moat, the irreplaceability score, the balance sheet.

**The event plan (this mode's headline section — put it directly after the
thesis, before the scenarios):**

- **Entry:** when to be in by (state it relative to the print — e.g. "by the
  close on the session before"), and the current price.
- **Event scenarios with rough probabilities:** beat-and-raise / in-line /
  miss-or-weak-guide, each with an expected % move anchored to the name's own
  recent reaction history and the implied move where known. Say explicitly that
  these are scenario sketches over a single session.
- **Exit rule, written before the event:** the specific rule for taking the
  trade off — e.g. "exit at the open of the session after the print, or on a
  defined intraday level; do not hold past T+2 regardless of direction." Include
  what to do on a gap *down* as well as a gap up: the down case is where a plan
  gets abandoned.
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
**beat-likelihood score** and the **priced-in score** (flag high priced-in
rather than vetoing it), plus each name's **report date** and **days to print** —
the reader needs the calendar to act on the list at all. Sort ties toward the
name reporting sooner only when the doctrine evidence is genuinely level. Each
top-3-5 thesis paragraph must cover the record, the revenue direction, the
priced-in verdict, and the fallback.

Phase 3.5 verification targets for this doctrine, in priority order:
1. **The report date and BMO/AMC**, against the company's IR page — this is
   non-negotiable and comes first. A wrong date invalidates everything.
2. The consensus EPS and revenue figures for the quarter.
3. The last-quarter surprise and the stock's reaction to it.
4. The moat's central factual claim.
