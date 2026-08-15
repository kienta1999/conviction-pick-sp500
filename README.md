# conviction-pick-sp500

Pick **one** S&P 500 stock with explosive-return potential (or a ranked top-N) —
by funneling all 503 members through a **deterministic quality screen** (Python),
then handing the survivors to a **multi-agent AI skill** that web-researches each
and forces a conviction pick. Three complementary strategies share the same funnel
and the same scripts, switched by `screen.py --mode`:

- **Momentum** (`--mode momentum`, skill `/stock-pick-momentum`) — buy
  **strength**. A profitable US company that is the biggest in its niche, **price
  above its 200-day SMA**, riding a **structural shortage** — demand the world
  can't supply fast enough, with a backlog that gives multi-year revenue
  visibility (MU's HBM booked out to 2026/2027 was the tell). Modeled on a
  friend's early Micron (MU) call.
- **Dip** (`--mode dip`, skill `/stock-pick-dip`) — buy **weakness**. The same
  quality, moaty, category-leading company, but **price below its 200-day SMA**
  and off its 52-week high (yet not wrecked), corrected on a **transitory** cause
  with an intact moat (especially **AI-irreplaceable**), a rebound catalyst, and
  a margin of safety. Buy the dislocation, not the decline.
- **Earnings** (`--mode earnings`, skill `/stock-pick-earnings`) — buy the
  **catalyst**. A ≥$20B company **reporting within the next 7 days** that has
  beaten consensus four quarters running with the revenue line still rising
  underneath the beats. **No SMA gate at all** — above or below the 200-day
  average is irrelevant when the thing expected to move the stock is the print.
  This is an **event trade**: entered before the report, exited into the
  reaction, closed in the ledger within days. Its trap is the *priced-in print* —
  the beat that was already in the price.

```
503 S&P 500 names ─[ deterministic funnel (--mode momentum|dip|earnings) ]─> quality candidates
                                                      │     (~30-50; earnings mode is
                                                      │      calendar-bound, often <10)
                                                      ▼
  /stock-pick-momentum | /stock-pick-dip | /stock-pick-earnings : research + Opus 4.8 panel
                                                      │        (+ claim verification pass)
                                                      ▼
                ONE conviction pick (or ranked top-N) + thesis → picks/ledger.csv
                                                      │
                                                      ▼
                scripts/scorecard.py : every past pick vs its target and vs SPY
```

## Pipeline

| Step | Script                                    | What it does                                                                                                                                                                                                                                                 |
| ---- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | `scripts/universe.py`                     | Current S&P 500 roster + GICS Sector / Sub-Industry (Wikipedia scrape, cached weekly).                                                                                                                                                                       |
| 2    | `scripts/fetch.py`                        | Per-ticker OHLCV (momentum + drawdown), yfinance fundamentals snapshot, annual revenue series (for TTM growth), quarterly statements (earnings-quality flags), and the earnings calendar + 12-quarter consensus-surprise history. Threaded, retrying, age-cached. |
| 3    | `scripts/screen.py --mode {momentum,dip,earnings}` | The deterministic funnel → `output/<mode>/shortlist.json`.                                                                                                                                                                                          |
| 4a   | `.claude/skills/stock-pick-momentum/`     | Momentum AI skill: web research → Opus 4.8 panel → verification → one pick (or top-N) → `output/momentum/final_pick.md` + ledger row(s).                                                                                                                     |
| 4b   | `.claude/skills/stock-pick-dip/`          | Dip AI skill: web research → Opus 4.8 panel → verification → one pick (or top-N) → `output/dip/final_pick.md` + ledger row(s).                                                                                                                               |
| 4c   | `.claude/skills/stock-pick-earnings/`     | Earnings AI skill: same machinery, event horizon → `output/earnings/final_pick.md` + ledger row(s) + a mandatory `kind=close` row within days of the print.                                                                                                  |
| 5    | `scripts/scorecard.py`                    | The feedback loop + **exit rules**: classifies every ledger row (AT_TARGET / STOPPED / EXPIRED / OPEN / CLOSED), benchmarks vs SPY, builds the realized track record from `kind=close` rows, and (`--check`) exits non-zero with an ALERTS section for cron. |

## The deterministic funnel (`screen.py`)

Each stage is a hard, repeatable gate. Between **momentum and dip**, only stage 5
(the price gate), the forward-PE default, and the composite score differ — every
quality gate is shared. **Earnings mode** differs more (no price gate, no stage
8; see its own section below). Real numbers from a 2026-07 run:

```
                       momentum   dip
0. Universe              503      503   all current S&P 500 members
1. Profitable            420      420   TTM net income > 0
2. US company            399      399   country == "United States"
3. Revenue growth        339      339   TTM YoY revenue growth > 0 (also anti-value-trap;
                                        smoothed from annual statements so one lumpy
                                        quarter doesn't eject a compounder — falls back
                                        to quarterly YoY if statements are missing)
4. Manageable debt       240      240   net-debt / EBITDA < 3.0  (net-cash passes)
5. Price gate            145       94   momentum: price ABOVE 200-day SMA
                                        dip:      price BELOW 200-day SMA …
5b. Drawdown floor        —        89   dip only: ≤55% below the 52-week high
                                        (drops falling knives; --dip-drawdown-floor)
6. Strong margins         69       42   operating margin > the GICS-sector median
6b. Earnings quality      —        42   dip + earnings, SOFT gate (--no-eq-gate off):
                                        drop names with 2+ red flags — Sloan accruals
                                        > +5%, CFO/NI < 0.6, receivables (or inventory)
                                        outrunning revenue — the quantifiable value-trap
                                        signature. One flag never gates; all flags ride
                                        into shortlist.json + penalize the composite.
                                        Financials are exempt from gate + penalty (their
                                        receivables are loans; CFO/NI isn't working-
                                        capital-driven) — metrics stay visible
7. Forward profit         69       41   0 < forward P/E < cap (60 momentum / 35 dip);
                                        tickers dropped for a MISSING estimate are printed
                                        ⚠️ forwardPE is Yahoo's, INDICATIVE ONLY — see below
8. Niche leaders          58       33   per GICS Sub-Industry: top-2 by market cap
                                        UNION co-leader ≥20% of the biggest UNION ≥50%
                                        of the SECOND-biggest (see below) —
                                        measured against the FULL universe, not the
                                        survivors (see below)
9. Trim to target         50       33   if >50 remain, keep top 50 by composite score
```

The **composite score** (used only to trim/rank, never to gate) blends
cross-sectional percentile ranks, and is mode-specific:

- **momentum:** TTM revenue growth (30%), 12-month momentum (20%), operating
  margin (15%), ROE (15%), analyst upside (10%), low leverage (10%) — growth +
  momentum first, then quality, then valuation headroom.
- **dip:** analyst upside / rebound headroom (25%), drawdown depth (20%, deeper =
  more room, the floor gate caps the wrecks), operating margin (15%), ROE (15%),
  TTM revenue growth (15%), low leverage / survival (10%) — rebound room +
  quality + balance-sheet durability, deliberately **not** momentum.
- **earnings:** average surprise size over the last 4 quarters (20%), beat count
  (15%), surprise trend — recent 2 vs prior 2 (5%), TTM revenue growth (20%),
  revenue acceleration (10%), operating margin (15%), ROE (10%), low leverage
  (5%) — the track record of clearing the bar first, then the top line that has
  to keep feeding it. Deliberately rewards **neither** momentum nor analyst
  upside: neither says anything about what a company does with next week's
  print, and rewarding either would smuggle the momentum doctrine into an event
  screen.

(Net-cash companies with no usable EBITDA rank as the _best_ balance sheets in
the leverage term, not neutral.)

Both composites then subtract a small **earnings-quality penalty**: −3
percentile points per red flag, capped at −6 (flags computed in `fetch.py`
from quarterly statements; a missing statement is an explicit `null` + note,
never a silent penalty). The weights are asserted to sum to 1.0 in code.

### A caveat on `forwardPE` (stage 7)

`forwardPE` is Yahoo's field, passed straight through — `screen.py` does no
valuation arithmetic of its own, and it is **not** in either composite, so nothing
is ever *ranked* on it. It gates at stage 7 and is otherwise for reading. Treat it
as indicative, and prefer a bottom-up multiple in any writeup. Two distortions live
in it:

1. **Stale price — fixed.** Yahoo computes it as `currentPrice / forwardEps`, and
   `currentPrice` comes from the info cache (~3-day TTL) while every price signal in
   the funnel uses `price` from the price cache (~1-day TTL). The gap reached 7.9%
   on LRCX. `_add_derived` now rescales onto `price`.
2. **Which fiscal year — not fixable here.** Whichever year Yahoo's `forwardEps`
   references varies by company: GE and HWM point a year out, while CF points
   *nearer* than the current year. Correcting this needs a forward figure derived
   from the quarterly statements `fetch.py` already pulls. **Open.**

### The "biggest in its niche" rule (stage 8)

"Biggest in what it's doing" is the heart of the doctrine, but GICS sub-industries
are coarse: there's no "memory / HBM" bucket, so **MU, NVDA, AVGO, AMD all sit in
the generic `Semiconductors` sub-industry**. A naive "keep only the #1 by market
cap" rule would throw away MU — even though it's a genuine memory franchise that
passes every quality gate — just because NVDA is bigger in the same bucket.

So stage 8 keeps the **union of three rules** per sub-industry:

1. **Top-N by market cap** (`--leaders-per-subindustry`, default **2**) — the
   clear leaders are always kept.
2. **Co-leader vs the leader** (`--coleader-ratio`, default **0.20**) — also
   keep any name whose market cap is ≥ 20% of the bucket's biggest name.
3. **Co-leader vs the runner-up** (`--coleader-2nd-ratio`, default **0.50**) —
   also keep any name ≥ 50% of the bucket's **second**-biggest name.

**Why rule 3 exists — rule 2 silently expires.** Rule 2 measures you against the
`#1`, so a runaway leader raises the bar for everyone else. On 2026-08-04 NVDA hit
$5T, which put the 20% bar at **$1.0T** and evicted **MU at $937B** — the #3
semiconductor, and the very name rule 2 was written to protect. It had passed the
same gate at 0.216 a month earlier. Meanwhile the same 20% bar in Insurance Brokers
is only **$18B**, so the rule was *hardest to pass exactly where leadership means
most*:

| bucket | leader | 20%-of-leader bar |
|---|---|---|
| Insurance Brokers | $92B | $18B — trivial |
| Semiconductors | $5,005B | $1,001B — brutal |

Rule 3 fixes the asymmetry because it is scale-free with respect to the leader: MU
is 0.50 of AVGO whether NVDA is worth $5T or $10T. The separation is clean rather
than marginal — MU scores 0.502 against the runner-up while the next-best rejected
semiconductor (TXN) scores 0.132, so nothing sits near the line. Today rules 1+2
keep 66 of 83 survivors; rule 3 adds exactly **MU** and **WAB** (0.559, a genuine
freight-rail leader buried in a coarse bucket).

An absolute floor (e.g. "auto-qualify above $100B") was considered and rejected: at
$100B it readmits TXN and ADI — the #6 and #7 semiconductors, at 4.9% and 3.5% of
the leader — which is the exact also-ran profile the gate exists to drop. Any dollar
threshold also drifts as the market grows, and $250B would have sat 1.6% above TXN's
$246B, flipping names in and out on noise.

Both measures are computed **against the full S&P 500 universe, not the funnel
survivors**. This matters most in dip mode: the true #1 of a niche is usually
_not_ in a dip, and a survivor-relative rule would crown the #4 name "leader"
just because its betters failed a gate. Measured against the universe, a dip
candidate must be a _genuine_ top-2/co-leader of its niche that happens to be
dipping (e.g. MSFT, WMT), not a pretender.

The ratio rules are _proportional_, so they adapt to every sector instead of
forcing an arbitrary count — "between MU and SNDK, pick MU." Tune all three knobs:

```bash
python scripts/screen.py --coleader-ratio 0.15         # wider co-leader net
python scripts/screen.py --coleader-2nd-ratio 0.35     # wider runner-up net
python scripts/screen.py --leaders-per-subindustry 1 \
                         --coleader-ratio 1.0 --coleader-2nd-ratio 1.0   # strict #1-only
```

### The earnings mode (stages 5/5b/5c, and the missing stage 8)

Earnings mode is the one place the funnel changes shape rather than just
thresholds. Four things are different:

**1. There is no price gate.** Momentum requires price above the 200-day SMA and
dip requires it below; earnings requires *nothing*. The catalyst is a scheduled
event, so trend direction is not evidence either way — a name qualifies from
above or below its average, and `dist_sma200` rides into the shortlist as
context for the "how much is priced in?" question instead of as a gate.

**2. The US-domicile gate is skipped.** Stage 2 comes from the founding
momentum doctrine ("a profitable US company biggest in its niche") and is about
who you want to *own for years*: domestic reporting standards, no FX translation
on a multi-year thesis, no foreign policy risk on the moat. None of it bears on
whether a company beats its number next Tuesday. Skipping it readmits the 23 S&P
members chartered in Ireland/UK/Switzerland/Singapore (LIN, STX, ETN, CB, MDT,
ACN, TT, NXPI, GRMN…) — American businesses by operation, foreign only by
domicile. They cluster in the late-October reporting wave, so the gate change is
usually worth 0 names and occasionally worth several.

**3. Stage 8 is skipped, replaced by a market-cap floor at 5b.** "Biggest in its
niche" answers *can this company hold its pricing for years* — the right question
for a multi-year shortage thesis, the wrong one for a print eight days out. A #3
name with four straight beats is a better earnings candidate than a #1 that keeps
missing. What the size rule was really doing for risk — keeping the system out of
small caps — is done directly by `--min-market-cap` (default **$20B**), because a
bad print takes 10-20% off in a single session and you want that to happen in a
name with the liquidity to exit into.

**4. Two gates are new** — the calendar and the track record:

```
                        earnings   (2026-08-15 run, --earnings-within 7)
1,3,4 shared gates          277    profitable + growing + leverage (no US gate)
5.  earnings window           9    next scheduled report within 7 days
                                   (--earnings-within; 250 dropped)
5b. market-cap floor          7    ≥ $20B (--min-market-cap)
5c. enough history            7    ≥4 reported quarters with surprise data;
                                   names dropped here are printed by ticker
5c. consensus record          6    <2 EPS misses in the last 4 quarters
                                   (--max-misses-4q; set to 1 to demand 4-for-4)
6.  strong margins            1    op margin > sector median — computed over the
                                   FULL universe here, not the survivors (see below)
6b. earnings quality          1    same soft gate dip mode uses: 2+ red flags drops
7.  forward profit            1    0 < forward P/E < 60
8.  niche leaders             1    SKIPPED — 5b does this job
```

**The sector median is computed differently here, deliberately.** In momentum and
dip, stage 6's median is taken over the survivors of stages 1-5 (a known leakage —
see the TODO). Earnings mode *cannot* do that: its stage-5 survivor pool is
"whoever happens to report this week", so a sector median over it would be built
from two or three arbitrary names, and a company would pass or fail on which peers
share its reporting week. Here the median comes from the full universe, the same
way stage 8 measures leadership.

**Expect a small field, and sometimes none.** The window is a hard calendar
constraint. Measured on 2026-08-15, a between-seasons Saturday:

| window | in-window | survivors | names |
|---|---|---|---|
| 7 days | 9 | **1** | ADI |
| 14 days | 22 | **6** | + INTU ADSK VEEV WSM ULTA |
| 30 days | 32 | **9** | + MDT ADBE NTAP |

A mid-quarter week can yield zero, and the screen exits cleanly with empty
outputs when it does. Peak season (late Jan/Apr/Jul/Oct) yields far more. The
skill is required to report the field size and *not* widen gates to manufacture
candidates — a 4-lens panel voting over 2 names is theater, and it says so.
Note the cost of widening: at 30 days you hold up to a month of unrelated market
risk before the catalyst you underwrote even arrives.

Two consequences worth knowing:

**Low-margin retail almost never qualifies**, in any mode, because of the shared
stage-6 margin gate. In the 7-day run WMT, TGT, TJX, ROST and HD all cleared the
calendar *and* the beat record, then died at the sector median — TJX and ROST by
2.2pp and 0.6pp with clean 4/4 streaks. That is the doctrine working as designed,
not an earnings-mode bug, but it means the off-price and big-box complex is
structurally invisible to this screen.

**The 6b earnings-quality gate keeps catching the AI-semi complex.** In the
30-day run it dropped **NVDA** (HIGH_ACCRUALS + INVENTORY_BUILD) and **AVGO**
(RECEIVABLES_OUTRUN + INVENTORY_BUILD) — two of the three largest prints in the
window, both on inventory growing faster than revenue. NVDA's numbers: TTM net
income $159.6B vs $125.6B operating cash flow, a $34.0B gap that is almost
exactly its working-capital build (receivables +$18.6B, inventory +$14.5B), with
inventory +128% against revenue +85%. Cash conversion (0.79) and receivables
(−1.3pp) both pass cleanly, so it is the *inventory* half doing the work.

That has a benign reading (stocking silicon ahead of a ramp) and a hostile one
(a writedown forming), and a screen cannot tell them apart. Worth checking
whether "hypergrowth mechanically trips accruals" — it does **not**: across
non-financials the flag rate runs 0.4% at 0-10% growth to 14% above 50%
(correlation 0.20), and the other hypergrowth names are clean — MU at +145%
revenue has an accrual ratio of −0.009 and CFO/NI of 1.02. Only SMCI scores
worse than NVDA. So the flag is picking up something specific, not a growth
artifact. Use `--no-eq-gate` to readmit these names with the flags still visible
and still penalizing the composite; the Phase 2 brief then forces a research
agent to give a benign-or-not verdict on each flag before the panel votes.

The beat record itself comes from Yahoo's earnings calendar (~24 quarters
available, 12 cached per ticker) and lands in `shortlist.json` as an
`earnings_trend` block: `eps_beats_4q`, `eps_misses_4q`, `eps_surprise_avg_4q`
(the *size* of the beats), `eps_surprise_trend` (recent 2 vs prior 2 — a
shrinking beat is the classic fade tell), `eps_beats_8q`, `eps_yoy_q` and
`eps_yoy_up_4q` from the *reported* EPS line (is it earning more, or just
beating a lowered bar?), plus `rev_yoy_q`, `rev_accel` and `rev_up_years`.

#### Should the earnings mode look outside the S&P 500?

Tempting, and it is the *right* lever for a calendar-bound screen — more names
in the same window, rather than a longer window with more pre-event risk.
Measured on 2026-08-15 against the Nasdaq screener (7,138 US-listed stocks):

```
  491  >= $20B and US-domiciled
   74  ...not already in the S&P 500  (after stripping preferreds, notes, dual classes)
   73  had usable data -> ran through the funnel:
   48  profitable        <- 25 die here
   42  growing
   27  sane debt         <- the pool the calendar draws from
    1  reporting within  7 days   ->  UI
    4  reporting within 14 days   ->  HEI, OKTA, UI, ZM
```

So roughly **+1 name at 7 days, +4 at 14** — meaningful against a field of 1,
but smaller than it looks, and for a structural reason: **S&P 500 inclusion
already requires profitability**, so the index committee applies gate 1 for us.
What sits outside is mostly unprofitable growth (CRWV, CBRS, RKLB, RVMD, ASTS) —
exactly what the gates exclude anyway.

**Not implemented, and the blocker is specific:** stage 6 compares operating
margin to the **GICS sector median**, and the Nasdaq screener returns its own
taxonomy (`Technology`, `Finance`, `Health Care`), not GICS. Mixing them would
corrupt the gate that already does the most cutting in this mode. A real GICS
source for non-index names is a prerequisite. Secondary costs: fetch grows to
~1,000 tickers (Yahoo already rate-limited us three times at 503 in one day),
and the scorecard's per-mode comparison is confounded if earnings runs on a
different universe than momentum/dip. If it is ever built, the clean shape is a
*supplementary* roster with proper GICS tags applied to **all three** modes.

⚠️ **The cached report date is Yahoo's and is sometimes an estimate.** It has a
1-day cache TTL — tighter than anything else here, because a stale date doesn't
degrade a score, it puts the wrong company in the funnel. The skill still
verifies the winner's date and BMO/AMC against the company's IR page before
publishing; that check is the first item in its verification phase.

## Quick start

```bash
uv sync                                   # install deps into .venv

uv run python scripts/universe.py         # build the S&P 500 roster
uv run python scripts/fetch.py            # fetch prices + fundamentals (~2 min, cached after)
uv run python scripts/screen.py --mode momentum   # → output/momentum/shortlist.{json,csv}
uv run python scripts/screen.py --mode dip        # → output/dip/shortlist.{json,csv}
uv run python scripts/screen.py --mode earnings   # → output/earnings/shortlist.{json,csv}

uv run python scripts/scorecard.py        # score all past picks vs targets and SPY
uv run python scripts/scorecard.py --check  # exit-rules alert mode (non-zero exit
                                            # when a target/stop/expiry fires — cron it)
```

(`--mode momentum` is the default, so bare `screen.py` is the momentum screen.)

Then run the AI picker from Claude Code — one skill per strategy:

```
/stock-pick-momentum          # buy strength: shortage + above-200d-SMA
/stock-pick-dip               # buy weakness: reboundable quality dip
/stock-pick-dip rank 10       # ranked top-10 instead of a single pick
/stock-pick-earnings          # buy the catalyst: reports within 7 days, 4/4 beats
/stock-pick-earnings 14 days  # widen the window when the week is empty
```

Each will (re)build its shortlist if needed, triage to the ~12-15 strongest
names, fan deep web research out to parallel research subagents, convene a
4-member Opus 4.8 voting panel, **verify the winner's load-bearing claims with
an independent web-search pass**, write the final conviction pick (or ranked
top-N) — with **bear/base/bull scenario builds, justified probabilities, an
expected-value-vs-price check (EV upside < +15% → the run publishes as a
"pass" and recommends buying nothing), key swing factors, and an EPIC driver
table** — to `output/<mode>/final_pick.md` (or `final_ranking.md`), and
**append the pick(s) to `picks/ledger.csv`** so `scorecard.py` can hold the
doctrine accountable.
The momentum panel runs supply-chain / growth / quality / contrarian lenses;
the dip panel runs catalyst / compounder / moat-&-AI-irreplaceability /
falling-knife-skeptic lenses; the earnings panel runs earnings-momentum /
setup-&-positioning-skeptic / moat-&-irreplaceability / contrarian lenses.

**Earnings mode diverges after the panel**, because it is an event trade rather
than a 12-18 month thesis (see the addendum at the foot of the protocol). Its
writeup leads with an **event plan** — entry timing, beat/in-line/miss scenarios,
and an exit rule written *before* the print — and the usual 12-18 month scenarios
demote to the **fallback**: what you are left holding if the gap is too ugly to
exit cleanly. The `+15% EV` guardrail splits in two: an *event* gate that must
beat what is already priced in (fail → `kind=pass`, no edge), and a *fallback*
gate that only warns (fail → the writeup carries a "NO SAFE FALLBACK" banner).
Closing is mandatory within days of the print, as a `kind=close` row with
`exit_reason=event_exit` — this is the only mode that produces realized outcomes
fast enough to teach the system anything.

### How the three skills share one protocol

All the machinery both skills have in common — mode parsing (single vs ranked
top-N vs multi-round), the Phase 0 shortlist build, research fan-out, panel
mechanics, the verification pass, Borda aggregation, the writeup template, the
ledger append, and the guardrails — lives once in
`.claude/skills/shared/pick-protocol.md`. Each SKILL.md contains only its
doctrine: the philosophy, its trap (momentum: disintermediation/in-sourcing;
dip: value-trap/permanent-impairment; earnings: the priced-in print), triage
criteria, research brief, the four panel lenses, and its writeup sections.
Change the machinery in one place; it applies to all three.

Subagents deliberately run on **Opus 4.8** (`model: "opus"`), not a
Mythos-class model — the panel fans out to 4×R agents and research batches, so
model cost multiplies. This is stated in the protocol so it doesn't silently
drift.

Dispatch is **sequential**, one agent at a time, each writing its output to a
designated file before returning — a parallel fan-out that trips the monthly
spend limit loses every in-flight agent at once, which has cost whole runs. If an
agent does die, the protocol requires the orchestrator to **halt the phase and
hand back**, never to write the missing ballot, dossier section or verification
itself. Those artifacts are independent samples by construction; an
orchestrator-authored substitute shares the orchestrator's priors, cannot disagree
with it, and turns a four-lens panel into one opinion wearing four hats — a short
panel you can no longer detect. An incomplete run publishes nothing: no writeup,
no ledger row. Resuming reuses every completed file and re-dispatches only what's
missing.

### Useful flags

```bash
python scripts/screen.py --mode dip                   # the buy-the-dip screen
python scripts/screen.py --mode dip --dip-drawdown-floor 0.40  # stricter falling-knife cut
python scripts/screen.py --target 30                  # tighter shortlist
python scripts/screen.py --max-net-debt-ebitda 2.0    # stricter leverage
python scripts/screen.py --max-forward-pe 30          # override the forward-valuation cap
python scripts/screen.py --leaders-per-subindustry 3  # keep top-3 per niche
python scripts/screen.py --coleader-ratio 0.15        # wider co-leader net
python scripts/screen.py --mode dip --no-eq-gate      # disable the stage-6b earnings-quality gate
python scripts/screen.py --mode earnings                       # reports within 7 days
python scripts/screen.py --mode earnings --earnings-within 14  # widen an empty week
python scripts/screen.py --mode earnings --min-market-cap 50e9 # bigger names only
python scripts/screen.py --mode earnings --max-misses-4q 1     # demand a clean 4-for-4 streak
python scripts/screen.py --no-trim                    # skip the trim-to-target step
python scripts/fetch.py --refresh                     # ignore caches, re-fetch
python scripts/fetch.py --tickers MU,NVDA,META        # debug a subset
python scripts/scorecard.py --mode dip                # score one strategy only
python scripts/scorecard.py --check                   # alert mode: non-zero exit when a rule fires
python scripts/scorecard.py --stop-pct 0.2 --grace-days 60  # tighter exit rules
```

## Outputs

Each mode writes to its own folder — `output/momentum/`, `output/dip/` or
`output/earnings/`:

- `output/<mode>/shortlist.json` — full records (~47 fields/candidate) for the skill.
- `output/<mode>/shortlist.csv` — human-readable, ranked (dip CSV surfaces `dist_52w_high`;
  every CSV now carries the earnings-calendar and beat-record columns).
- `output/<mode>/funnel.json` — stage-by-stage in/out/dropped counts (audit trail).
- `output/<mode>/research_dossier.md` — written by the skill (web research).
- `output/<mode>/final_pick.md` / `final_ranking.md` — written by the skill (the pick(s) + thesis).
  These always hold the **current** run.
- `output/<mode>/old/` — every **superseded** run, dated by its own run date
  (`final_pick_2026-07-12.md`), so the writeup behind a recorded ledger row is never
  destroyed by the next run. Same-day supersessions keep both, the earlier suffixed
  `_<TICKER>_superseded.md`. Committed — this is audit trail, and `ledger.csv`'s
  `source` column points here for past picks.
- `output/<mode>/parts/<run-date>/` — per-run working files: `triage.md` (the
  50 → ~14 cut, every name scored with a keep/drop reason), the raw research
  batches, each panel ballot, and the verification scorecard. **Gitignored**:
  scratch, consolidated into `research_dossier.md` and the final writeups.
  `triage.md` exists because that cut discards ~70% of the field, is made by a
  single agent, and is the one step nothing downstream can catch — the panel can
  only vote on what triage hands it.

Plus the cross-mode scorecard:

- `picks/ledger.csv` — append-only record of every pick: date, mode, entry
  price, **bear/base/bull targets with timing and probabilities, the EV price**
  (the WS-3 scenario discipline), one-line thesis, source. Exits are appended
  as `kind=close` rows (realized fill + reason) referencing the original pick
  by date+mode+ticker — rows are never mutated. Runs where the EV guardrail
  blocked the pick append a `kind=pass` row.
- `scripts/scorecard.py` — reads the ledger, fetches current prices, runs the
  **exit rules** (the recorded bear target is the stop; base target hit →
  reassess; past `base_by` + 90d grace → expired), prints each pick's return
  vs target and vs SPY, and aggregates closed picks into the **realized track
  record** (hit rate, avg win/loss, alpha per mode) — the only way to know
  whether any of this beats buying the index.
- `POLICY.md` — the human layer: position sizing (fractional-Kelly-lite with
  5%-per-pick / 15%-system caps), the no-leverage rule, the manual deployment
  checklist (the picker itself stays portfolio-blind by design), and the pilot
  protocol that gates scaling.

## Data sources

- **Roster + GICS:** Wikipedia "List of S&P 500 companies".
- **Prices + fundamentals:** Yahoo Finance via `yfinance` (prices cached ~1 day,
  info ~3 days, annual + quarterly statements ~7 days under `data/`, all
  git-ignored).
- **Earnings calendar + consensus-surprise history:** Yahoo Finance via
  `yfinance` `get_earnings_dates()` — the next scheduled report date plus 12
  quarters of estimate/reported/surprise, cached **~1 day** under
  `data/earnings/`. The dates are Yahoo's and are sometimes estimates, which is
  why the earnings skill verifies the winner's against the company's IR page
  before publishing.

This is a _current-snapshot_ screen, so unlike the sibling
`ranker-21d-sp500` project it needs no point-in-time membership history
or SEC XBRL pipeline.

## Roadmap / TODO

- [ ] **Backtest the deterministic funnel point-in-time** (the big one). The
      ledger only starts 2026-06-21, so `scorecard.py` needs years to judge the
      doctrine. But the sibling `ranker-21d-sp500` repo already has
      everything needed to backtest the _deterministic half_ historically:
      point-in-time S&P 500 membership (1996+), per-ticker OHLCV back to 2005,
      XBRL fundamentals (TTM income, D/E, revenue growth), and sectors.
      Re-implement `screen.py`'s gates as point-in-time functions over that
      panel, run the funnel monthly from ~2012 (post-XBRL coverage), hold each
      shortlist 6–12 months, measure vs SPY. Answers whether
      "profitable + growing + low debt + price gate + niche leader" has alpha
      _before_ the AI layer touches it — if the shortlist alone beats SPY, the
      panel only needs to not subtract value; if it doesn't, that's even more
      important to know. (~2–3 days, mirrored as a cross-project TODO in that
      repo's README.)
- [ ] **Third strategy: `--mode insider`.** Screen for cluster insider buying
      (multiple officers, direct open-market P transactions, meaningful net
      dollars — the Form 4 bulk pipeline in `ranker-21d-sp500/scripts/insider.py`
      already downloads this) + the shared quality gates, then a
      `/stock-pick-insider` skill researches _why_ insiders are buying. Panel
      lenses: conviction-buyer / opportunist-vs-routine / bagholder-skeptic /
      moat. A genuinely different signal source than momentum or dip.
- [ ] **Hybrid mode: AI panel on the ML model's picks.** Run the sibling repo's
      `today.py`, take the top ~15 by predicted return, and hand them to the
      shared research + panel protocol. The ML model finds statistical
      anomalies; the AI explains and vetoes them. Disagreements between the two
      projects are the most interesting output.
- [x] **Exit discipline for the ledger** (shipped 2026-07-12). `scorecard.py`
      now classifies every pick (AT_TARGET / STOPPED / EXPIRED / OPEN /
      CLOSED / TRACKED / PASS), uses the recorded `bear_target` as the stop
      (fallback −25%), builds the realized track record from append-only
      `kind=close` rows, and `--check` exits non-zero for cron alerting.
      Remaining: actually put it on a cron (the GitHub Actions pattern from
      `ai-stock-investment`).
- [ ] **Validate the earnings-quality gate historically.** Stage 6b (dip) and
      the composite EQ penalty shipped 2026-07-12 as a _soft_ gate on the
      working-capital methodology's thresholds — but they are untested
      factors. The point-in-time backtest above must run the dip funnel with
      and without them; if the gate doesn't improve forward returns, demote
      it to flag-only permanently.

## Disclaimer

Research / educational tooling. Not financial advice. Data from third-party
sources may be stale or wrong — verify before acting.

(Session breadcrumbs for past runs live in `NOTES.md`.)
