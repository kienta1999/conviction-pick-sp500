---
name: stock-pick-dip-lite
description: Cheap single-agent version of stock-pick-dip — same DIP screen, same doctrine (is the drop temporary or a permanent impairment?), same value-trap veto, but ONE agent does everything in one pass with ≤14 web searches total (one per driver cluster, not per name or per lens) and writes only output/dip/final_ranking_lite.md (+ final_pick_lite.md for a single pick), archiving the prior run to output/dip/old/. No research subagents, no 4-lens panel, no verifier, no dossier, no scenarios, no ledger row. Use when the user says "lite", "quick", "cheap", "one pass", "no subagents", is near a usage limit, or wants a fast read on which beaten-down S&P 500 quality names are worth a look. For the full panel with an audit trail and a recorded pick, use stock-pick-dip.
---

# stock-pick-dip-lite — one agent, one pass, one memo

Same question as `stock-pick-dip` (is this dip *temporary* or a broken
business?), scored by you alone.

**Read `.claude/skills/shared/lite-protocol.md`** for the machinery, and
`.claude/skills/stock-pick-dip/SKILL.md` **for the doctrine only** — the
value-trap trap, what a reboundable dip looks like. Skip that file's phase
sections (triage.md, research brief, the four lenses, the writeup template);
lite replaces all of them. Do not read `pick-protocol.md`.

- **MODE:** `dip` → `OUT = output/dip/`

## The five lite lenses

One head scores all five, 1-10:

| key | lens | weight | source |
|---|---|---|---|
| `cause` | **is the drop transitory?** macro/rates, sentiment, rotation, a one-off miss, a cyclical trough — *not* a lost moat or secular decline | .30 | search |
| `moat` | moat / AI-irreplaceability — switching costs, network effects, process-tech, certification lock-in, brand, capital intensity | .25 | knowledge + search |
| `trig` | rebound trigger (catalyst) — a concrete, dated path back up | .20 | search |
| `surv` | balance-sheet survival — `net_debt_ebitda`, FCF, cash | .10 | CSV |
| `mos` | margin of safety — `forwardPE` vs its own history, `analyst_upside`, `dist_52w_high` | .15 | CSV + knowledge |

```python
W, LENS = (.30,.25,.20,.10,.15), ["cause","moat","trig","surv","mos"]
VETO, KEY = "cause", "cause"      # cause <= 3 = permanent impairment = avoid
```

Extra CSV columns for the memo table: `dist_sma200`, `dist_52w_high`,
`net_debt_ebitda`, `ret_12m`.

`qual` also requires `moat >= 6` — a cheap dip in a dying franchise is the
value trap this doctrine exists to refuse.

## Searches

One per driver cluster: `"<sub-industry or headline>" selloff <Month YYYY>
outlook`. Plus one regime search (rates / the tape). Name-specific searches only
for the 2-3 likely buys, asking the one question that decides them: *is this
drop about the price or the business?*

Cluster siblings share `cause` and `cat` unless a snippet gives a name-specific
reason.

## Memo

Per the lite protocol's template, with the lens columns
`cause | moat | trig | surv | mos` and the CSV columns above. The `why` line must
say, in the same breath, why the drop is temporary and what re-rates it.
