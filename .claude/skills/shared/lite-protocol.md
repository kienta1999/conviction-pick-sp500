# Shared LITE protocol — one agent, one pass, one memo

The cheap counterpart to `pick-protocol.md`. Same screen, same doctrine, same
weights and the same trap — but **you do all of it yourself, in one context**:
no research subagents, no 4-lens panel, no verifier, no ballots, no dossier.
Read this once, then execute it with the invoking `-lite` skill's parameters.

**Budget: ≤14 `WebSearch` total, no `WebFetch`.** Search snippets only — no
filings, no PDFs, no transcripts. If you are reaching for a fetch, the answer
is "not found" and you write that instead.

**Do not read `pick-protocol.md`.** It is the expensive path and its phases do
not apply here. Read the `-lite` skill's parent SKILL.md only for the doctrine
(what the trap is, what a good name looks like) — the parent's phase machinery
(triage.md, research briefs, ballots, Phase 3.5, EV guardrail, ledger) is
exactly what lite skips.

---

## 1. Screen

Same Phase 0 cache rule as the full protocol: read `generated` in
`OUT/shortlist.json`; if it is <24h old and the user didn't ask to refresh,
reuse it. Otherwise:

```bash
uv run python scripts/fetch.py && uv run python scripts/screen.py --mode <MODE>
```

Tell the user the field size, the sector spread and the top few by composite.

## 2. Triage — in your head, not to disk

Cut to the **~12-15** strongest on the skill's doctrine, using the metrics
already in the file plus what you know. No `triage.md` — the memo's table shows
every name you scored and the drop list is one line at the bottom. Say honestly
if you dropped a high-composite name.

## 3. Research — one search per *cluster*, not per name

Group the kept names by shared driver — same GICS sub-industry, or the same
headline (the AI-power names, the GLP-1 names, the tariff-hit industrials).
One search per cluster:

> `"<driver>" <Month YYYY>` + the skill's doctrine keyword

Names in a cluster **share** the driver-level scores unless a snippet gives a
name-specific reason — then write that one sentence. Spend a name-specific
search only on the 2-3 names most likely to end up in the buy bucket. Add one
macro/regime search. The rest of the scoring comes from `shortlist.csv`, which
already carries growth, margins, leverage, drawdown, analyst upside, valuation,
the beat record and (earnings mode) the reaction record.

## 4. Score and consolidate — in python, not in your head

Score every kept name 1-10 on each of the skill's five lite lenses, then run
this in the scratchpad:

```python
import pandas as pd
S = {"TICK": (8,9,7,6,7), ...}          # scores, in the skill's lens order
W, LENS, VETO, KEY = ...                # all four given by the skill
scan = pd.read_csv("output/<MODE>/shortlist.csv", index_col="ticker")
df = pd.DataFrame(S, index=LENS).T
df["wtd"] = (df * W).sum(axis=1).round(2)
df["veto"] = df[VETO] <= 3
for c in ["gics_sub_industry", "dist_52w_high", "analyst_upside",
          "forwardPE", "composite_score"]:           # + the skill's extra cols
    df[c] = scan[c].reindex(df.index)
df = df.sort_values("wtd", ascending=False)
df["grp_rank"] = 0; ok = ~df.veto
df.loc[ok, "grp_rank"] = df[ok].groupby("gics_sub_industry").cumcount() + 1
qual = ok & (df[KEY] >= 7) & (df.analyst_upside >= 0.15)   # skill may add a term
df["bucket"] = "watch"; df.loc[qual, "bucket"] = "alt"
df.loc[qual & (df.grp_rank == 1), "bucket"] = "buy"
df.loc[df.veto, "bucket"] = "avoid"
print(df.to_string())
```

`analyst_upside` comes straight from the screen (the CSV has no price column —
read `currentPrice` from `shortlist.json` for the memo) — lite does **not** build
bear/base/bull scenarios and therefore cannot run the full protocol's +15% EV
guardrail. `analyst_upside` is the stand-in and it is a weaker one; say so.

One buy per sub-industry: the rule stops the memo recommending the same trade
three times in three wrappers.

Then set **my rank** — start from `wtd` and reorder only where a fact justifies
it, one sentence per deviation.

## 5. Write it — same file names as the full protocol, `_lite` suffixed

Lite scores the whole field in one pass, so the ranking is free every run and
the "one pick" is just its top `buy` row. Mirror the full protocol's mode split:

| file | when |
|---|---|
| `OUT/final_ranking_lite.md` | **every run** — the scored field, the memo proper |
| `OUT/final_pick_lite.md` | when the user wants one pick (the default mode) — short: the buy row's thesis, why the trap doesn't apply, the catalyst, the top risk, and a pointer to the ranking. Do not restate the table. |

**Archive before overwriting**, exactly as the full protocol does:

```
OUT/old/final_pick_lite_<RUNDATE>.md
OUT/old/final_ranking_lite_<RUNDATE>.md
```

`<RUNDATE>` is the **superseded** run's own date, read from its header — not
today's, not the mtime. A same-day rerun suffixes the earlier one
`_<TICKER>_superseded.md`. `OUT/old/` is committed; skipping the archive
destroys the only record of the previous call.

`final_ranking_lite.md`:

```markdown
# stock-pick-<MODE> <DATE> — lite (one agent, N searches, no panel, no verifier)

Regime: 2-3 lines.

| my # | ticker | company | sub-industry | <5 lens cols> | wtd | price | upside | fwd PE | bucket | why (1 line) |

Deviations from the weighted score: one sentence each (or "none").
Buy: ...   Alt: ...   Watch: ...   Avoid: ...
Dropped at triage: tickers + one line.

Caveat: the one thing that flips the whole list.

## Sources
Every search run, as `query — publisher, date`. Lite has no dossier and no
verifier, so this list *is* the audit trail: a claim in a `why` line that
isn't traceable to a row here is a claim you should not have made.

Not done in lite: independent per-lens scoring (one head scored all five —
contamination risk), deep per-name research, verification of load-bearing
facts, bear/base/bull scenarios, the +15% EV guardrail, and the ledger row.
Run the full /stock-pick-<MODE> before sizing real money if the buy survives.
```

Nothing else is written: **no** `research_dossier.md` (there are no subagent
dossiers to consolidate — the evidence is the `why` lines plus Sources), **no**
`parts/`, and **no row in `picks/ledger.csv`** — lite produces no scenario
targets, so a ledger row would be a pick the scorecard cannot score. Say that
in the first two lines of `final_pick_lite.md`, where the file name most
invites the opposite assumption. If the user wants the pick recorded, that is
the full skill's job.

## Guardrails (unchanged from the full protocol)

- Never fabricate figures, backlogs, drawdowns, multiples, consensus numbers or
  reactions. "Not found" is an answer.
- Don't override the screen — pick from the screened set.
- No specific leverage multiple or position size. Research, not advice; date
  the disclaimer.
- The trap still vetoes: a name whose trap score is ≤3 lands in `avoid` no
  matter how good the rest of the row looks.
