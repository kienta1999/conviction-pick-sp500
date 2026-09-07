---
name: stock-pick-earnings-lite
description: Cheap single-agent version of stock-pick-earnings — same EARNINGS screen, same doctrine (a beat streak that the stock actually gets paid for, going into a print that isn't already priced), same priced-in veto and the same six-box disqualifier checklist, but ONE agent does everything in one pass with ≤14 web searches total and writes only output/earnings/final_ranking_lite.md (+ final_pick_lite.md for a single pick), archiving the prior run to output/earnings/old/. Plan B only (enter after a confirmed beat-and-raise) — lite never recommends holding through a print, because it has no verifier to confirm the date. No research subagents, no panel, no dossier, no ledger row. Use when the user says "lite", "quick", "cheap", "one pass", "no subagents", "who reports soon", is near a usage limit, or wants a fast read on the reporting wave. For the full panel, a confirmed date, a pre-registered prediction and a recorded pick, use stock-pick-earnings.
---

# stock-pick-earnings-lite — one agent, one pass, one memo

Same question as `stock-pick-earnings` (does this name get *paid* for its beats,
and is the good news already in the price?), scored by you alone.

**Read `.claude/skills/shared/lite-protocol.md`** for the machinery, and
`.claude/skills/stock-pick-earnings/SKILL.md` **for the doctrine only** — the
priced-in trap, the two entries, the disqualifier checklist. Skip that file's
phase sections; lite replaces all of them. Do not read `pick-protocol.md` or its
earnings addendum.

- **MODE:** `earnings` → `OUT = output/earnings/` (45-day default window; pass
  `--earnings-within 10` if the user wants this week only)

## Plan B only — this is the load-bearing simplification

Lite **never recommends Plan A** (holding through the print). Plan A requires a
report date confirmed against the company's own IR page by an independent
verifier, and lite has no verifier — the cached Yahoo date is sometimes an
estimate, and a wrong date makes the trade meaningless. So every lite
recommendation is: *wait for the number; enter only on beat + raised-or-above
guide + a first session that closes up.* Say this in the memo's first two lines.
If the user explicitly wants Plan A argued, that is the full skill.

## Field size

The calendar bounds this mode. Split the wave on `days_to_earnings` into
**actionable now** (≤10 days) and a dated **watchlist**, and hand back both. If
the actionable set is 0, report the funnel and the next wave's dates and stop —
an empty mid-quarter week is the screen working. Don't widen a gate to
manufacture a field.

## The six-box disqualifier checklist — run it first, mechanically

Five of the six boxes are already in `shortlist.csv`; run them before any prose,
as a visible list with numbers:

1. `run_into_print_flag` true (up >15% over 21 sessions into the print)
2. either of the last two entries in `reaction_last4` is a beat the stock fell on
3. guidance raised between quarters — *the one search-only box*
4. date not confirmed on the IR page — **always ticked in lite** (no verifier)
5. the expected move sits inside `reaction_avg_abs_move`
6. next-quarter consensus implies an acceleration `rev_accel` / the last 2-3
   quarters haven't shown

Box 4 is ticked for every name by construction, which is exactly why lite is
Plan B only. The other five still decide whether a name is a *good* Plan B
candidate or drops to watch.

## The five lite lenses

One head scores all five, 1-10:

| key | lens | weight | source |
|---|---|---|---|
| `react` | **reaction record** — `beat_up_rate`, `reaction_avg_move`, `reaction_last4`; where `print_reaction.note` says not judgeable, score it low and say "unproven, not vindicated" | .30 | CSV |
| `beat` | beat quality — `eps_surprise_avg_4q` size, `eps_surprise_trend` direction, `rev_yoy_q` and `rev_accel` underneath | .20 | CSV |
| `guide` | guide safety (**inverted risk** — 10 = the forward number looks comfortably supported by the run-rate) | .20 | search |
| `priced` | not-priced-in (**inverted** — 10 = nothing in the price; low = the run-up, the multiple and the implied move say the good news is already there) | .20 | CSV + search |
| `fall` | fallback quality — would you be content owning it 18 months after a bad gap? moat, margins, balance sheet | .10 | knowledge |

```python
W, LENS = (.30,.20,.20,.20,.10), ["react","beat","guide","priced","fall"]
VETO, KEY = "priced", "react"     # priced <= 3 = the trap = avoid
```

Extra CSV columns for the memo table: `next_earnings`, `days_to_earnings`,
`beat_up_rate`, `reaction_avg_abs_move`, `ret_21d`, `run_into_print_flag`.

`qual` also requires `guide >= 6` and **zero ticked boxes among 1/2/3/5/6** —
a ticked box is not argued with.

## Searches

One per reporting cluster (same sector reporting the same week — their read is
shared: a peer's print is the best available signal). Then one name-specific
search per likely buy, asking the two questions the CSV can't answer:
*was the guide already raised between quarters?* and *what is next-quarter
consensus, and does the run-rate support it?* One macro/regime search.

## Memo

Per the lite protocol's template, plus:

- the checklist, as a visible ticked/clear list with numbers, **before** the
  table;
- the **watchlist** table (names beyond ~10 days) with dates, at the end;
- for each `buy`/`alt`: the Plan B trigger in one line (beat on EPS *and*
  revenue, guide raised or above consensus, first full session closes up) and
  the drift horizon (20-40 sessions) with the level that ends it early (a close
  back below the reaction-day close).

Lite writes no ledger row and therefore **no `event_pred_*` pre-registration** —
say so; that falsifiability is a reason to run the full skill on a name worth
real money. While you have the ledger open, name any prior earnings pick whose
print has already passed and which still has no `kind=close` row.
