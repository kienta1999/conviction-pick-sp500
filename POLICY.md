# POLICY.md — position sizing & deployment policy (the human layer)

This file is the **only** place portfolio- and money-management context lives.
The picker itself stays portfolio-blind by design (see README): no script,
dossier, or panel ever reads holdings. Every number here is a default — edit it
here, once, and the skills/scorecard echo it.

The stock-pick skills must read this file and include a **sizing note** in
every writeup that echoes the formula below with the pick's own EV and bear
numbers — as the owner's pre-committed policy, not personalized advice.

---

## 1. Per-pick sizing (fractional-Kelly-lite)

Size is proportional to modeled edge per unit of modeled downside, from the
writeup's scenario table (WS-3 discipline):

```
raw      = (ev_price / price − 1) / (1 − bear_target / price)
size_pct = min(5.0, 2.5 × raw)          # % of investable capital
```

Worked example: price $231, EV $283 (+22.5%), bear $190 (−17.7%) →
raw = 0.225 / 0.177 = 1.27 → size = min(5, 3.2) = **3.2%**.

Adjustments, in order:

1. **Earnings halving** — if `next_earnings` is within **10 days** of entry,
   halve the size (event risk; the writeup must flag the date).
2. **Per-pick cap: 5%** of investable capital, always.
3. **System cap: 15%** across all open picks from this system combined
   (`scorecard.py` prints current recorded exposure vs this cap and alerts
   over it).
4. **Pilot regime (until §5 is satisfied): halve the computed size again.**

The scenario numbers feeding `raw` are AI-panel research estimates, not
measurements — treat the formula as a *discipline* that forces downside math
before money moves, and the caps as the real risk control. Never size up
because the formula "says so"; only ever size down from it.

### 1.5 Earnings mode — a tighter regime

`mode=earnings` picks are event trades held into a scheduled print. Rule 1.1's
earnings halving applies to **every** pick in this mode by construction — that
is the point, not an edge case — and on top of it:

- **Per-pick cap: 2%** of investable capital (not 5%), before the halving and
  before the pilot halving of rule 1.4. A single session can take 10-20% off a
  large, healthy company on a guide the market didn't like; the position has to
  be small enough that the gap is an annoyance rather than an event.
- **One earnings position at a time.** Two open prints in the same week is a
  bet on earnings season, not on a company.
- **The exit is part of the entry.** Do not open the position without the
  writeup's exit rule in front of you. An event trade held past its rule
  because "the thesis is still intact" has become an unplanned long position,
  sized for an event that already passed.
- **Plan B is the default entry.** The skill's default is to enter *after* the
  print on a confirmed beat-and-raise with a positive first session, not to
  hold through it. Holding through (Plan A) requires the writeup to have run
  the disqualifier checklist clean and argued the case explicitly. Measured on
  this repo's own shortlist, beats produced an up move only ~54% of the time
  with a 5.9% average absolute move — the gap is a coin flip, and the 2% cap
  below is what makes taking it survivable, not a reason to take it.
- Earnings positions count against the 15% system cap like any other while
  they are open — which, per the protocol, should be days.

## 2. No leverage — hard rule

Picks from this system are **cash-only**. No margin, no options as leverage
substitutes, no borrowing against the position. The dip doctrine's own warning
("catching a knife with margin is brutal") is policy here, not advice. Leverage
decisions belong to the owner's separate personal framework and never to this
repo's picks.

## 3. Deployment checklist (manual, before any order)

The system is portfolio-blind, so the overlap check is a **human step**:

- [ ] Does this pick overlap a position I already hold in size (same name,
      same niche, or tightly correlated — e.g. another AI-capex proxy)? If
      yes, reduce or skip; the ledger still records the pick either way.
- [ ] Is total open exposure from this system after this entry ≤ 15%? (Run
      `uv run python scripts/scorecard.py` — it prints the recorded total.)
- [ ] Earnings within 10 days? Halve (writeup should already flag it).
- [ ] `mode=earnings`? Apply §1.5 (2% cap, then halve), confirm no other
      earnings position is open, and have the exit rule written down before
      the order goes in.
- [ ] Record the actual deployed size in the pick's ledger row (`size_pct`)
      so the scorecard can police the cap. Unfunded picks leave it empty.
- [ ] `mode=earnings`? The pick row must carry the pre-registered call
      (`event_pred_dir`, `event_pred_move`, `event_implied_move`) before the
      order goes in — that is what makes the close row informative.
- [ ] After an earnings print: append the `kind=close` row
      (`exit_reason=event_exit`) the same week (Plan A), or at the end of the
      stated drift horizon (Plan B). A Plan B trigger that never fired still
      gets a close row. This is not optional
      bookkeeping — it is the only realized-outcome data this system gets
      quickly.

## 4. The "pass" outcome is a first-class result

If the writeup's probability-weighted expected value is less than **+15%**
above the current price over 12–18 months, the run publishes as **"pass —
best of a weak field"** and appends a `kind=pass` row to the ledger instead of
an actionable pick. Deploy nothing. Passes are tracked so the scorecard can
eventually show whether they were right. The system must stay comfortable
recommending nothing.

## 5. Pilot protocol (gates scaling, not entry)

Until **both** are true, all sizes run at half (rule 1.4):

- `scorecard.py --check` has run on a schedule (cron) for a **full quarter**
  with the exit rules live, and
- the point-in-time backtest (README roadmap / WS-8) has reported whether the
  deterministic funnel alone beats SPY.

The ledger only started 2026-06-21 — the system has no realized track record
yet. Position sizes scale with evidence, not conviction.

## 6. Dip basket — the executed portfolio (`/stock-pick-dip-execute`)

The one thing this repo trades mechanically. Account **U27177562** (IBKR, the
dip-basket account — never `U26645119`, that is `ranker-21d-sp500`'s). Rules
are pre-registered here so a rebalance never re-argues them:

- **Names: the top 3 of the latest dip `rank10` run**, equal weight. Ranks 1–3
  are the only rows the panel underwrites with scenario targets and a bear
  stop (`scorecard.py` shows them OPEN; 4–10 are TRACKED only). Sweep on
  2026-09-17 (`scripts/basket_backtest.py`, 5 runs / 80 days, META out):
  equal3 +22.5% / maxDD −3.7% vs equal10 +11.3% / −5.0%, equal5 +9.3% / −9.2%,
  SPY +2.9%. equal5 < equal10 < equal3 is not a monotone edge — it is five
  samples. The top-3 rule stands on the underwriting argument, not the sweep.
- **Exclusion list: META** (owner's employer compliance). Dropped before
  weighting; `scripts/basket_backtest.EXCLUDE` is the single source.
- **Leverage 1.0, vol-target 0.20** — §2 (cash-only) still applies. The
  overlay `min(1.0, 0.20 / spy_vol_20d)` can only *de-risk* in a stressed
  tape; it never borrows. The sweep shows leverage merely scaling return and
  drawdown together (Sharpe flat to lower) with nothing clever to buy.
- **Three slots, rebalanced monthly.** Run the full `/stock-pick-dip` panel
  once a month (it only writes the ledger; nothing trades until
  `/stock-pick-dip-execute`). A slot frees only when its name:
  (a) hits its bear stop, (b) reaches its base target, (c) expires past
  `base_by`, or (d) is **outranked while still in the screen** — still a dip,
  the panel just prefers others. A held name that left the screen by
  *recovering above its 200d SMA* keeps its slot until (a)–(c): it is doing
  what it was bought for, and the screen's own gate would otherwise sell a
  −35% dip on a +3% bounce (ISRG sits 2.7% under its 200d on 2026-09-17).
  Free slots fill from the new run's ranking, top down. Slots are equal
  weight; re-weight survivors only past the `--min-order` threshold. A stop
  between runs is a manual sell + `kind=close` row; the slot stays cash until
  the next run.
- **Sizing is the account, not §1.** The basket account is funded at the
  ALLOCATION.md conviction-pick sleeve; §1's per-pick formula is for
  discretionary single picks and does not apply inside the basket.

---

*Research/educational tooling. Not financial advice.*
