# TODO — findings from the 2026-08-05 four-lens review

Four reviewers (PM/allocator, risk manager, quant research, operational DD) reviewed
the system independently on 2026-08-05. Full write-ups are session scratch; the
findings that survived verification are below, ordered by leverage.

**Headline: three of the four reviewers independently traced their worst finding to
the same root cause — nothing in this system ever closes a position.** The ledger holds
87 rows and **zero** `kind=close` rows. Every alpha number the scorecard prints is an
unrealized mark, not a return. Fix that first; several items below dissolve when it lands.

---

## P0 — the system cannot currently tell whether it works

### 1. Zero realized outcomes. Ever. `picks/ledger.csv`
- **Verified:** 87 rows, `kind` is only ever `rank10` (80) or `single` (7). No `close` rows.
- `scripts/scorecard.py` already implements exit rules and close-row logic — it fires
  ALERTS correctly — but nothing ever acts on them. The alert just reprints forever.
- MU's stop objectively fired (close $739 vs $775 bear_target, 2026-07-29). It was
  never closed. A second overlapping MU lot (bear $550) is also still dangling.
- MSFT has been sitting at AT_TARGET across three rows since 2026-08-03. Never taken.
- **Consequence:** the realized track record is not "thin", it is **empty**. There is no
  evidence this system makes money, in either direction. Six weeks of "alpha" numbers
  are open opinions marked to market.
- **Action:** append `kind=close` rows for MU (stopped) and MSFT (at target) now. Then
  make closing mandatory: the scorecard's `--check` mode should be a blocking step
  before any new run publishes.

### 2. Same names re-picked without ever resolving the prior thesis
- AVGO ×5, MSFT ×5, HWM/MU/GE/NVDA ×4 — each a fresh row, none closing the last.
- The system cannot distinguish "the 2027 thesis is playing out" from "the stock
  wiggled this fortnight," because it re-picks on a 2-week cadence against targets
  dated 2027-09 / 2027-11.
- **Action:** decide the unit of account. Either a name is one open thesis that gets
  closed before re-entry, or re-picks are explicitly marked as adds to an existing lot.
  Pick one and encode it in `pick-protocol.md`.

### 3. Horizon mismatch: graded weekly, underwritten for 18 months
- Theses are written for 12–18 months; performance is judged every run.
- At n=4 overlapping, non-independent runs per mode, **neither** momentum's negative
  alpha **nor** the dip-single's +24.6% is statistically distinguishable from noise.
- **Action:** do not kill momentum on this sample, and do not credit single-pick mode
  for the MSFT print. Define the evaluation horizon up front and stop reading the
  fortnightly alpha column as if it means something.

---

## P1 — risk controls that are nominally present but not actually operating

### 4. The 15% exposure cap is unenforceable
- `size_pct` is populated in **1 of 87 rows** (BR, 0.83% — and that edit is still
  uncommitted). AVGO's real $5,000 position is invisible to the scorecard.
- Investable capital is recorded **nowhere**, so `size_pct` has no denominator and
  the cap cannot be evaluated even in principle.
- **Action:** record investable capital in `POLICY.md`. Backfill `size_pct` for funded
  positions. Have the scorecard refuse to report exposure when funded rows lack sizing
  rather than silently reporting 0.8%.

### 5. No correlation or theme cap — the book is one trade
- 8 of the latest 10 momentum picks (AVGO, LRCX, MSFT, APH, GOOGL, NVDA, KLAC, VRT)
  are the same AI-capex/semis factor.
- The 15% cap is dollar-notional only. Ten names at policy size is not a diversified
  book, it is one levered bet on AI capex wearing ten tickers.
- **Action:** add a theme/factor sub-cap to `POLICY.md`. The deployment checklist
  already asks the human to eyeball overlap — that is not a control.

### 6. The sizing formula amplifies model error into position size
- `size_pct = min(5.0, 2.5 × raw)` runs directly on `ev_price` and `bear_target`, which
  are **LLM panel estimates, not measurements**. The 2.5× multiplier scales confidence,
  not evidence.
- MU's actual 27-day drawdown (−28.4%) blew straight through its recorded bear case —
  while that writeup itself cited a 50–53% peak-to-trough base rate for prior cycles.
  The panel had the disconfirming number and sized against it anyway.
- **Action:** floor `bear_target` at the name's own historical drawdown base rate when
  the dossier cites one. Consider cutting the multiplier until realized outcomes exist.

---

## P2 — methodology

### 7. Stage 8 is overfit to MU — name it honestly
- `scripts/screen.py:130-132`: the 0.50 co-leader-vs-runner-up threshold was adopted
  because it readmits MU at 0.502. The rule's own justification cites the ticker it was
  built to readmit. That is textbook specification search.
- Three tuned knobs (`N`, `R`, `R2`) against ~4 known reference names, no holdout.
- The fix may well be *correct* — the runaway-#1 bug is real — but "it lets MU back in"
  is not evidence that it generalizes.
- **Action:** state the bias in the README section rather than the current framing.
  The honest test is whether the rule helps on names nobody was thinking about.

### 8. No backtest exists, and the data can't support one as-is
- `universe.py`/`fetch.py` are current-snapshot only and self-admittedly not
  point-in-time. Current S&P roster + current fundamentals = survivorship and
  restatement bias. Any naive backtest on this data would be invalid and flattering.
- **Action:** this is already on the README TODO. Promote it. **Stop tuning gates until
  it exists** — until then every threshold change is unfalsifiable.

### 9. Sector-median leakage at the op-margin gate
- `screen.py:351-355` computes the sector median over **post-gate survivors**, not the
  full sector — so the gate's stringency varies by sector and by what happened upstream.
- Inconsistent with the care taken at stage 8, which deliberately measures against the
  full universe for exactly this reason.
- **Action:** compute the median on the full universe, same as `subind_rank`.

### 10. Composite score: fewer factors than it looks
- Rank-based blend is mechanically fine, but weights are hand-picked and growth (30%)
  and 12m momentum (20%) are collinear. A nominal 6-factor score is probably 2–3.
- **Action:** print a correlation matrix of the components once. Cheap, one-off.

---

## P3 — process integrity

### 11. The panel's audit trail is gitignored
- `.gitignore` excludes `output/*/parts/` — the individual ballots and
  `verification.md`. The only committed record of "4 independent votes" is the
  orchestrator's own summary of them.
- The protocol was *just* hardened (2026-08-04) to require agents write ballots to
  disk — and those files are then excluded from the repo.
- **Action:** commit `output/*/parts/`. Trivial cost, closes the largest audit gap.
  This is the single cheapest fix on this list.

### 12. "Independent panel" overstates what four prompts of one model produce
- Four agents, one base model, one shared dossier, differentiated by prompt. Real
  disagreement does occur, but it is correlated-sample dispersion, not independent
  evidence. Borda counts and "unanimous 4/4" language imply more than exists.
- **Action:** keep the panel, downgrade the language. "4/4 lenses agreed" should not
  read like four analysts agreed.

### 13. ~79% of the dossier is never verified
- Phase 3.5 checks only the winner's highlighted claims — roughly 3 of 14 names.
  **Negative** claims used to exclude rivals are never fact-checked at all, and those
  are exactly the claims that decide the outcome silently.
- **Action:** extend verification to the claims that eliminated the runner-up.

### 14. False precision feeding real money
- `base_target 205 by 2027-09`, `p_base 0.50` — 2–3 significant figures of implied
  precision on narrative confidence. These feed the sizing formula **directly**, and
  BR is already funded off them.
- **Action:** round targets to the nearest 5, probabilities to 0.05, and state in the
  writeup template that these are scenario sketches, not estimates.

---

## Open question blocking item 4

Investable capital is still undisclosed. Without it, `size_pct` is uninterpretable
and the 15% cap cannot be checked. Everything in P1 stays theoretical until this
number is written into `POLICY.md`.

---

## DONE 2026-09-06 — `-lite` versions of the three skills

Pattern proven in `etf-dipfinder/.claude/skills/etf-dip-pick-lite/SKILL.md` (same date): same scan, same
lenses/weights/veto, but ONE agent, one search per theme (~10 total, snippets only, no fetches), scores
consolidated with an inline pandas snippet, memo only to `log/<DATE>-lite.md`, nothing to `output/`, no verifier.
~1/6 the tokens of the panel and it reached the same buy list. Do the same for:
- `stock-pick-dip` → `stock-pick-dip-lite` ✅
- `stock-pick-momentum` → `stock-pick-momentum-lite` ✅
- `stock-pick-earnings` → `stock-pick-earnings-lite` ✅ (Plan B only — no verifier, so the
  IR-confirmed date box is ticked by construction)

Built as `.claude/skills/shared/lite-protocol.md` (the machinery: screen → in-head triage →
one search per driver cluster → inline-pandas scoring with a sub-industry one-buy rule →
memo) plus three thin doctrine files that supply lenses/weights/veto. Output mirrors the full skill:
`output/<mode>/final_ranking_lite.md` every run plus `final_pick_lite.md` in single-pick mode,
prior runs archived to `output/<mode>/old/final_*_lite_<RUNDATE>.md`; lite writes no ledger row (no scenarios = nothing the
scorecard can score) and no `parts/`. Not yet run end-to-end — first run will show whether
the ≤14-search budget holds for ~15 single names as well as it did for 15 ETFs.
Cadence: lite first; run the full panel only if the lite buy list changes vs the last full run.
