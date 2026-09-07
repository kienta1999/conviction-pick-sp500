---
name: stock-pick-momentum-lite
description: Cheap single-agent version of stock-pick-momentum — same MOMENTUM screen, same doctrine (a structural shortage plus a product customers cannot in-source), same disintermediation veto, but ONE agent does everything in one pass with ≤14 web searches total (one per shortage cluster, not per name or per lens) and writes only output/momentum/lite/<DATE>-lite.md. No research subagents, no 4-lens panel, no verifier, no dossier, no scenarios, no ledger row. Use when the user says "lite", "quick", "cheap", "one pass", "no subagents", is near a usage limit, or wants a fast read on which S&P 500 names are riding a shortage. For the full panel with an audit trail and a recorded pick, use stock-pick-momentum.
---

# stock-pick-momentum-lite — one agent, one pass, one memo

Same question as `stock-pick-momentum` (a real shortage, sold by someone the
customer *can't* become?), scored by you alone.

**Read `.claude/skills/shared/lite-protocol.md`** for the machinery, and
`.claude/skills/stock-pick-momentum/SKILL.md` **for the doctrine only** — the
disintermediation trap, what the MU-shaped bet looks like. Skip that file's
phase sections; lite replaces all of them. Do not read `pick-protocol.md`.

- **MODE:** `momentum` → `OUT = output/momentum/`

## The five lite lenses

One head scores all five, 1-10:

| key | lens | weight | source |
|---|---|---|---|
| `short` | **shortage** — is the product supply-constrained or in a demand surge supply can't meet? | .30 | search |
| `irrep` | irreplaceability — can a hyperscaler/large customer in-source it, or a substitute route around it? (10 = nobody can) | .25 | knowledge + search |
| `book` | backlog / order-book visibility — a quoted backlog, bookings, "sold out", take-or-pay | .20 | search |
| `cat` | category dominance — clear #1 with pricing power (`subind_rank`, `mc_vs_2nd`) | .10 | JSON |
| `room` | headroom — how much is already priced (`ret_12m`, `forwardPE`, `analyst_upside`, `dist_52w_high`). High score = room left | .15 | CSV |

```python
W, LENS = (.30,.25,.20,.10,.15), ["short","irrep","book","cat","room"]
VETO, KEY = "irrep", "short"      # irrep <= 3 = the customer builds it = avoid
```

Extra CSV columns for the memo table: `ret_12m`, `dist_sma200`,
`operatingMargins`, `rev_growth_ttm`.

`qual` also requires `irrep >= 7` — this doctrine's whole edge is the moat, and
a shortage without one is a bet the trap eventually collects on.

## Searches

One per shortage cluster (AI compute/HBM, power & grid, cooling, nuclear,
defense, GLP-1, niche semis…): `"<shortage driver>" backlog sold out
<Month YYYY>`. Plus one regime search (the AI-capex tape / rates). Name-specific
searches only for the 2-3 likely buys, asking the one question that decides
them: *has a top customer announced its own version?*

Cluster siblings share `short` unless a snippet gives a name-specific reason.
`book` is per name — a backlog number is not shared; if none is quotable, score
it low and say "not found" rather than inferring one.

## Memo

Per the lite protocol's template, with the lens columns
`short | irrep | book | cat | room` and the CSV columns above. The `why` line
must name the shortage *and* the thing that stops the customer building it.
