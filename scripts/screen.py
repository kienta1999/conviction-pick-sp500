#!/usr/bin/env python3
"""Deterministic S&P 500 screen -> a shortlist of quality candidates.

Three modes share the same quality funnel but differ at the price/event gate
(stage 5), the leadership rule (stage 8) and the ranking score, so one script
feeds all three AI skills:

  --mode momentum (default) — the original doctrine (a friend's MU call:
      profitable, US, biggest in its niche, riding a structural shortage). Buys
      STRENGTH: price ABOVE its 200-day SMA; score rewards 12-month momentum.
      Consumed by the `stock-pick-momentum` skill. Writes to output/momentum/.

  --mode dip — buy a reboundable quality dip. Same quality gates, but buys
      WEAKNESS: price BELOW its 200-day SMA and off its 52-week high (but not
      wrecked — a value-trap floor drops names down more than the floor). Score
      rewards rebound headroom + quality + balance-sheet survival, not momentum.
      Consumed by the `stock-pick-dip` skill. Writes to output/dip/.

  --mode earnings — buy a quality compounder INTO its scheduled print. No SMA
      gate at all (the catalyst is the event, not the trend, so a name qualifies
      whether it is above or below its 200-day average). Two gates replace it:
      the company must report within EARNINGS_WITHIN_DAYS, and it must clear a
      MIN_MARKET_CAP floor — the stage-8 "biggest in its niche" rule does NOT
      apply here, because a scheduled print is not a niche-leadership question
      and the size floor is the thing that keeps the run off small caps, where
      an earnings gamble is worst. Adds an earnings-track-record gate (stage 5c)
      and scores on the beat streak. Consumed by the `stock-pick-earnings`
      skill. Writes to output/earnings/.

Funnel (each stage prints how many names it drops):

  0. Universe          all current S&P 500 members
  1. Profitable        TTM net income > 0
  2. US company        country == "United States". SKIPPED in earnings mode —
                       domicile shapes a multi-year hold, not a single print.
  3. Revenue growth    TTM YoY revenue growth > 0 (also the anti-value-trap
                       gate). Uses rev_growth_ttm (smoothed, from annual
                       statements — see fetch.py) so one lumpy quarter doesn't
                       eject a compounder; falls back to Yahoo's single-quarter
                       revenueGrowth when statements are unavailable.
  4. Manageable debt   net-debt / EBITDA < MAX_NET_DEBT_EBITDA (net-cash passes)
  5. Price/event gate  momentum: price ABOVE its 200-day SMA
                       dip:      price BELOW its 200-day SMA, AND drawdown from
                                 the 52-week high no worse than DIP_DRAWDOWN_FLOOR
                       earnings: NO price gate. Instead —
                         5  reports within EARNINGS_WITHIN_DAYS days
                         5b market cap >= MIN_MARKET_CAP
                         5c earnings track record: fewer than
                            MAX_MISSES_4Q consensus misses in the last 4
                            quarters, and enough history to judge
  6. Strong margins    operating margin above the company's GICS-sector median
  6b. Earnings quality dip + earnings modes, soft gate (--no-eq-gate disables):
                       drop names with 2+ earnings-quality red flags (Sloan
                       accruals, cash conversion, receivables/inventory vs
                       revenue — see fetch.py). One flag never gates; every flag
                       penalizes the composite score slightly in ALL modes and
                       rides into shortlist.json as an `earnings_quality` block.
  7. Forward profit    0 < forward P/E < MAX_FORWARD_PE — positive forward
                       earnings (makes money next year) and not an absurd
                       valuation; NaN forward P/E is dropped (conservative,
                       and the dropped tickers are printed so a missing Yahoo
                       estimate never costs a name invisibly).
                       Default ceiling tightens for dip (cheapness tilt).
  8. Niche leaders     momentum + dip ONLY. Per GICS Sub-Industry keep the top-N
                       by market cap UNION any co-leader ≥ R× the bucket's
                       biggest name (keeps MU alongside NVDA; drops small
                       also-rans like SNDK). Leadership is measured against the
                       FULL S&P 500 universe, not the gate survivors — so a #4
                       name can't become a "leader" just because the real
                       leaders failed a gate. SKIPPED in earnings mode (the
                       stage-5b size floor does that job instead).
  9. Trim to target    if >TARGET remain, rank by a mode-specific composite —
                       quality/explosive (momentum), rebound (dip), or
                       beat-streak quality (earnings) — and keep the top TARGET

Outputs (under output/<mode>/):
    shortlist.csv    human-readable, ranked
    shortlist.json   full records for the stock-pick skill to consume
    funnel.json      the stage-by-stage drop counts (audit trail)

Run scripts/fetch.py first (it populates the caches this reads).

CLI:
    python scripts/screen.py                       # momentum (default)
    python scripts/screen.py --mode dip            # buy-the-dip screen
    python scripts/screen.py --mode dip --dip-drawdown-floor 0.40
    python scripts/screen.py --mode earnings       # reporting within 7 days
    python scripts/screen.py --mode earnings --earnings-within 14
    python scripts/screen.py --mode earnings --min-market-cap 50e9
    python scripts/screen.py --target 50 --max-net-debt-ebitda 3.0
    python scripts/screen.py --no-trim             # keep all category leaders
"""

import argparse
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from fetch import load_metrics  # noqa: E402

_ROOT = os.path.dirname(_HERE)
# Per-mode output folder: output/momentum/, output/dip/ or output/earnings/.
# Resolved via _output_dir(mode); the three filenames inside are identical
# across modes.
OUTPUT_ROOT = os.path.join(_ROOT, "output")
MODES = ("momentum", "dip", "earnings")


def _output_dir(mode: str) -> str:
    return os.path.join(OUTPUT_ROOT, mode)


DEFAULT_TARGET = 50
DEFAULT_MAX_NET_DEBT_EBITDA = 3.0
# Forward-valuation gate (stage 7). A high cap, not a value screen: it's a
# sanity backstop. 0 < forwardPE enforces positive forward earnings ("makes
# money next year"); the < 60 ceiling sits well above the legitimate growth
# range (the universe tops out ~50) so it only ever catches absurd blow-off
# names, never a real franchise like HWM (~46) or the semi-equipment complex.
DEFAULT_MAX_FORWARD_PE = 60.0
# Dip mode tightens the ceiling — a reboundable quality dip should also be a
# margin-of-safety entry, not a still-expensive falling knife.
DEFAULT_MAX_FORWARD_PE_DIP = 35.0
# Dip price gate (stage 5). Keep names BELOW their 200-day SMA but drop the
# falling knives: anything more than this fraction below its 52-week high is
# usually a broken thesis, not a reboundable correction.
DEFAULT_DIP_DRAWDOWN_FLOOR = 0.55
US_COUNTRY = "United States"

# ── Earnings mode (stage 5/5b/5c) ────────────────────────────────────────────
# How far ahead to look for the scheduled print. 7 days is the default because
# the doctrine is "position into THIS week's report" — the thesis and the
# catalyst have to be close enough together that nothing else moves the stock
# first. Widen with --earnings-within when a week is empty (mid-quarter weeks
# routinely have <5 S&P names reporting).
DEFAULT_EARNINGS_WITHIN_DAYS = 7
# Size floor, replacing the stage-8 niche-leadership rule. An earnings print is
# a binary event with a fat left tail; on a $5B company a miss can take 30% off
# in one session with no liquidity to exit into. $20B is not a quality proxy —
# the quality gates above do that — it is a survivability-of-the-gap floor.
DEFAULT_MIN_MARKET_CAP = 20e9
# Track-record gate. 2+ consensus misses in the last four quarters means
# management cannot reliably clear a bar it set itself — the exact profile you
# do not want to hold into a print. One miss is allowed: it is common, often
# macro, and the research phase can judge it in context.
DEFAULT_MAX_MISSES_4Q = 2
# Minimum reported quarters with surprise data before the record is judgeable.
MIN_EARNINGS_HISTORY = 4

# Category-leader stage (7). GICS sub-industries are coarse — "Semiconductors"
# holds NVDA, AVGO, MU, AMD together — so a single #1-per-bucket rule throws away
# genuine niche leaders. We keep the union of THREE rules: the top-N by market
# cap; any "co-leader" whose market cap is at least COLEADER_RATIO of its
# sub-industry's biggest name; and any name at least COLEADER_2ND_RATIO of its
# sub-industry's SECOND-biggest name.
#
# The third rule exists because the second one quietly expires. It is measured
# against the leader, so a runaway #1 raises the bar for everyone else: at
# NVDA's $5T the 20% bar is $1.0T, which evicted MU ($937B, #3 semiconductor)
# on 2026-08-04 — while the same 20% bar in Insurance Brokers is just $18B. The
# rule was hardest to pass exactly where leadership means most. Measuring
# against #2 is immune to that (MU is 0.50 of AVGO regardless of NVDA) and
# never needs recalibrating as the market grows.
DEFAULT_LEADERS_PER_SUBINDUSTRY = 2
DEFAULT_COLEADER_RATIO = 0.20
DEFAULT_COLEADER_2ND_RATIO = 0.50


# ─────────────────────────────────────────────────────────────────────────────
# Derived metrics
# ─────────────────────────────────────────────────────────────────────────────


def _add_derived(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Net debt and leverage. net_debt < 0 == net cash (a good thing).
    df["net_debt"] = df["totalDebt"].fillna(0) - df["totalCash"].fillna(0)
    df["net_debt_ebitda"] = np.where(
        (df["ebitda"].notna()) & (df["ebitda"] > 0),
        df["net_debt"] / df["ebitda"],
        np.nan,
    )
    # Leverage as used by the composite score: a net-cash company with no
    # usable EBITDA has the best possible balance sheet, not a neutral one —
    # rank it best instead of letting NaN fall to the 0.5 neutral fill.
    df["net_debt_ebitda_rankable"] = np.where(
        (df["net_debt"] <= 0) & df["net_debt_ebitda"].isna(),
        -np.inf,
        df["net_debt_ebitda"],
    )
    # Growth as used by gate + score: smoothed TTM YoY when statements gave us
    # one, else Yahoo's single-quarter YoY.
    ttm = df["rev_growth_ttm"] if "rev_growth_ttm" in df.columns else pd.Series(np.nan, index=df.index)
    df["rev_growth"] = ttm.fillna(df["revenueGrowth"])
    # Analyst implied upside (sanity signal, not a gate).
    df["analyst_upside"] = np.where(
        (df["targetMeanPrice"].notna()) & (df["price"].notna()) & (df["price"] > 0),
        df["targetMeanPrice"] / df["price"] - 1,
        np.nan,
    )
    # Forward P/E restated on the SAME price as every other signal. Yahoo builds
    # forwardPE as currentPrice/forwardEps, and currentPrice comes from the info
    # cache (~3-day TTL) while the funnel's price signals use `price` from the
    # price cache (~1-day TTL) — so the multiple can sit on a quote days older
    # than the momentum it is judged beside (the gap ran to ~8% on LRCX in the
    # 2026-08-04 run). Rescaling by price/currentPrice is algebraically just
    # price/forwardEps. Rows missing either price keep Yahoo's value unchanged
    # rather than going NaN, since NaN is a drop at gate 7.
    #
    # This fixes the PRICE only. Which fiscal year Yahoo's forwardEps refers to
    # still varies by company (GE/HWM point a year out, CF points nearer than
    # the current year) and is NOT correctable from the info dict — treat
    # forwardPE as indicative, and prefer a bottom-up multiple when it matters.
    _fwd_ok = (
        df["forwardPE"].notna()
        & df["currentPrice"].notna() & (df["currentPrice"] > 0)
        & df["price"].notna() & (df["price"] > 0)
    )
    df["forwardPE"] = np.where(
        _fwd_ok,
        df["forwardPE"] * df["price"] / df["currentPrice"],
        df["forwardPE"],
    )
    # Niche leadership, measured against the FULL universe (everything fetched),
    # before any gate: a name's sub-industry rank and its size relative to the
    # sub-industry's biggest member must not depend on which peers happen to
    # survive the funnel (e.g. in dip mode the true leader is usually NOT in a
    # dip — the #4 name must not inherit "leader" status by default).
    g = df.groupby("gics_sub_industry")["marketCap"]
    df["subind_rank"] = g.rank(method="first", ascending=False)
    df["mc_vs_subind_leader"] = df["marketCap"] / g.transform("max")
    # Size relative to the bucket's RUNNER-UP, not its leader. The vs-leader
    # ratio silently breaks when one name runs away with a bucket: NVDA at $5T
    # pushed the 20%-of-leader bar to $1.0T, which evicted MU ($937B, the #3
    # semiconductor and the doctrine's founding example) on 2026-08-04 — while
    # a 20% bar in Insurance Brokers is only $18B. The rule was hardest to pass
    # exactly where leadership means most. Measuring against #2 is immune to
    # that: MU is 0.50 of AVGO whether NVDA is worth $5T or $10T.
    second = g.apply(lambda s: s.nlargest(2).iloc[-1] if len(s) >= 2 else s.max())
    df["mc_vs_2nd"] = df["marketCap"] / df["gics_sub_industry"].map(second)
    # Revenue acceleration (earnings mode): the latest quarter's YoY growth
    # against the smoothed trailing-year growth. Positive = the business is
    # growing faster now than it averaged over the past year, which is the
    # setup that produces a beat-and-raise; negative = decelerating into the
    # print even though the annual growth gate still passes.
    if "rev_yoy_q" in df.columns:
        df["rev_accel"] = df["rev_yoy_q"] - df["rev_growth"]
    else:
        df["rev_accel"] = np.nan
    return df


# ─────────────────────────────────────────────────────────────────────────────
# Gate helpers
# ─────────────────────────────────────────────────────────────────────────────


def _leverage_ok(row: pd.Series, cap: float) -> bool:
    # Net cash is always fine.
    if pd.notna(row["net_debt"]) and row["net_debt"] <= 0:
        return True
    nde = row["net_debt_ebitda"]
    if pd.isna(nde):
        return False  # have positive net debt but no usable EBITDA -> conservative drop
    return nde < cap


def _rank_pct(s: pd.Series, ascending: bool = True) -> pd.Series:
    """Cross-sectional percentile rank in [0,1]; NaN -> 0.5 (neutral)."""
    r = s.rank(ascending=ascending, pct=True)
    return r.fillna(0.5)


# Composite weight tables (documented in README — keep in sync). Each metric
# maps to (weight, ascending) for _rank_pct; weights per mode MUST sum to 1.0
# (asserted below).
#   momentum: growth and 12-month momentum first, then quality, then valuation
#             headroom — the explosive-compounder thesis.
#   dip:      rebound headroom (analyst upside) and drawdown depth first, then
#             quality and balance-sheet survival — the reboundable-dip thesis.
#             Deliberately does NOT reward momentum (beaten down by construction).
COMPOSITE_WEIGHTS = {
    "momentum": {
        "rev_growth": (0.30, True),
        "ret_12m": (0.20, True),
        "operatingMargins": (0.15, True),
        "returnOnEquity": (0.15, True),
        "analyst_upside": (0.10, True),
        "net_debt_ebitda_rankable": (0.10, False),  # less leverage better
    },
    "dip": {
        "analyst_upside": (0.25, True),             # headroom to mean target
        "dist_52w_high": (0.20, False),             # more beaten-down = more room
        "operatingMargins": (0.15, True),           # quality intact
        "returnOnEquity": (0.15, True),             # quality intact
        "rev_growth": (0.15, True),                 # still growing (not a trap)
        "net_debt_ebitda_rankable": (0.10, False),  # survival: less leverage better
    },
    #   earnings: the track record of clearing the bar comes first (40% across
    #             the three surprise factors), then the revenue line that has to
    #             keep feeding it, then quality. Deliberately does NOT reward
    #             analyst upside or momentum — neither says anything about what
    #             a company does with next week's print, and rewarding either
    #             would smuggle the momentum doctrine into an event screen.
    "earnings": {
        "eps_surprise_avg_4q": (0.20, True),        # SIZE of the beats
        "eps_beats_4q": (0.15, True),               # the streak itself
        "eps_surprise_trend": (0.05, True),         # beats growing, not shrinking
        "rev_growth": (0.20, True),                 # the top line still rising
        "rev_accel": (0.10, True),                  # and rising faster than trend
        "operatingMargins": (0.15, True),           # quality
        "returnOnEquity": (0.10, True),             # quality
        "net_debt_ebitda_rankable": (0.05, False),  # survives a bad print
    },
}
# Earnings-quality penalty on the composite (both modes): percentile points off
# per red flag, capped. A penalty, not a weight — flags are sparse and the
# composite must stay a 0-1 percentile blend for the un-flagged majority.
EQ_PENALTY_PER_FLAG = 0.03
EQ_PENALTY_CAP = 0.06


def _n_eq_flags(df: pd.DataFrame) -> pd.Series:
    """Red-flag count per row, for the 6b gate and the composite penalty.
    Financials are exempt (count 0): banks/insurers structurally 'fail'
    CFO/NI and receivables-vs-revenue (their receivables are loans, their
    cashflow isn't working-capital-driven) — the working-capital framework
    doesn't apply. Their metrics still ride into shortlist.json so the
    research brief can interrogate them."""
    if "eq_flags" not in df.columns:
        return pd.Series(0, index=df.index)
    n = df["eq_flags"].fillna("").map(lambda s: len([f for f in str(s).split(",") if f]))
    return n.where(df["gics_sector"] != "Financials", 0)


def _composite_score(df: pd.DataFrame, mode: str = "momentum") -> pd.Series:
    """Rank-based blend (scale-robust, NaN-tolerant) minus the earnings-quality
    penalty. Higher = more attractive. Used only to trim/rank, never to gate."""
    weights = COMPOSITE_WEIGHTS[mode]
    total = sum(w for w, _ in weights.values())
    assert abs(total - 1.0) < 1e-9, f"{mode} composite weights sum to {total}, not 1.0"
    score = sum(w * _rank_pct(df[col], ascending=asc)
                for col, (w, asc) in weights.items())
    penalty = (_n_eq_flags(df) * EQ_PENALTY_PER_FLAG).clip(upper=EQ_PENALTY_CAP)
    return score - penalty


# ─────────────────────────────────────────────────────────────────────────────
# The funnel
# ─────────────────────────────────────────────────────────────────────────────


def run_screen(
    target: int = DEFAULT_TARGET,
    max_net_debt_ebitda: float = DEFAULT_MAX_NET_DEBT_EBITDA,
    max_forward_pe: float = DEFAULT_MAX_FORWARD_PE,
    leaders_per_subindustry: int = DEFAULT_LEADERS_PER_SUBINDUSTRY,
    coleader_ratio: float = DEFAULT_COLEADER_RATIO,
    coleader_2nd_ratio: float = DEFAULT_COLEADER_2ND_RATIO,
    trim: bool = True,
    mode: str = "momentum",
    dip_drawdown_floor: float = DEFAULT_DIP_DRAWDOWN_FLOOR,
    eq_gate: bool = True,
    earnings_within_days: int = DEFAULT_EARNINGS_WITHIN_DAYS,
    min_market_cap: float = DEFAULT_MIN_MARKET_CAP,
    max_misses_4q: int = DEFAULT_MAX_MISSES_4Q,
) -> tuple[pd.DataFrame, list[dict]]:
    df = load_metrics()
    if df.empty:
        raise SystemExit("No metrics found. Run `python scripts/fetch.py` first.")
    df = _add_derived(df)
    # Kept for benchmarks that must be measured against the whole market rather
    # than against whoever survived the gates above them (stage 6 in earnings
    # mode; stage 8's leadership ratios are precomputed in _add_derived for the
    # same reason).
    full_universe = df.copy()

    funnel: list[dict] = []

    def stage(name: str, mask: pd.Series, frame: pd.DataFrame) -> pd.DataFrame:
        kept = frame[mask].copy()
        funnel.append({"stage": name, "in": len(frame), "out": len(kept), "dropped": len(frame) - len(kept)})
        print(f"  {name:<22} {len(frame):>4} -> {len(kept):>4}  (dropped {len(frame) - len(kept)})", flush=True)
        return kept

    print(f"\nFunnel (start: {len(df)} S&P 500 members with data):", flush=True)

    # 1. Profitable — TTM net income > 0 (fall back to profit margin sign).
    profitable = df["netIncomeToCommon"].fillna(
        df["profitMargins"].apply(lambda m: 1.0 if pd.notna(m) and m > 0 else (-1.0 if pd.notna(m) else np.nan))
    ) > 0
    df = stage("1 profitable", profitable, df)

    # 2. US company — momentum and dip only. The US gate comes from the founding
    #    momentum doctrine ("a profitable US company biggest in its niche") and
    #    is about who you want to own for years: domestic reporting standards,
    #    no FX translation on a multi-year thesis, no foreign policy risk on the
    #    moat. None of that has any bearing on whether a company beats its
    #    number next Tuesday, so earnings mode skips it. In practice this
    #    readmits the ~22 S&P members domiciled in Ireland/UK/Switzerland etc.,
    #    which are American businesses by operation and foreign only by charter.
    if mode == "earnings":
        funnel.append({"stage": "2 US company", "in": len(df), "out": len(df),
                       "dropped": 0, "skipped": "not applicable in earnings mode "
                                                "(domicile does not affect a print)"})
        print(f"  {'2 US company':<22} {len(df):>4} -> {len(df):>4}  "
              f"(skipped — domicile is irrelevant to an event trade)", flush=True)
    else:
        df = stage("2 US company", df["country"] == US_COUNTRY, df)

    # 3. Revenue growth YoY > 0, on the smoothed TTM measure (rev_growth falls
    #    back to Yahoo's single-quarter revenueGrowth where statements are
    #    missing — see _add_derived).
    n_fallback = int((df["rev_growth_ttm"].isna() & df["revenueGrowth"].notna()).sum()) \
        if "rev_growth_ttm" in df.columns else len(df)
    if n_fallback:
        print(f"  (growth gate: {n_fallback} names lack TTM statements, using quarterly YoY fallback)", flush=True)
    df = stage("3 TTM rev growth>0", df["rev_growth"].fillna(-1) > 0, df)

    # 4. Manageable leverage.
    df = stage("4 leverage ok", df.apply(lambda r: _leverage_ok(r, max_net_debt_ebitda), axis=1), df)

    # 5. Price/event gate. momentum buys strength (above 200d SMA); dip buys
    #    weakness (below 200d SMA) but drops falling knives via a drawdown
    #    floor; earnings has NO price gate — the catalyst is the scheduled
    #    print, so trend direction is deliberately not a criterion — and gates
    #    on the calendar, a size floor, and the beat record instead.
    if mode == "dip":
        df = stage("5 below 200d SMA", (df["dist_sma200"] < 0).fillna(False), df)
        within_floor = df["dist_52w_high"] >= -dip_drawdown_floor
        df = stage(f"5b drawdown >=-{dip_drawdown_floor:g}", within_floor.fillna(False), df)
    elif mode == "earnings":
        dte = df["days_to_earnings"]
        no_date = sorted(df.loc[dte.isna(), "ticker"])
        if no_date:
            print(f"  (earnings gate: {len(no_date)} names have NO scheduled earnings "
                  f"date cached and cannot be windowed)", flush=True)
        in_window = (dte >= 0) & (dte <= earnings_within_days)
        df = stage(f"5 reports <={earnings_within_days}d", in_window.fillna(False), df)
        if df.empty:
            print(f"\n  NOTE: no S&P 500 name that passed gates 1-4 reports within "
                  f"{earnings_within_days} days. Mid-quarter weeks are routinely "
                  f"empty — widen with --earnings-within.", flush=True)
        else:
            cal = df.groupby("next_earnings")["ticker"].apply(lambda s: ", ".join(sorted(s)))
            print("  (earnings calendar in window:)", flush=True)
            for d, names in cal.items():
                print(f"     {d}  {names}", flush=True)

        df = stage(f"5b mktcap>=${min_market_cap/1e9:g}B",
                   (df["marketCap"] >= min_market_cap).fillna(False), df)

        # 5c. Earnings track record. Two separate drops, reported separately so
        #     "we have no data on it" is never confused with "its record is bad".
        n_hist = df["n_reported"].fillna(0)
        thin = n_hist < MIN_EARNINGS_HISTORY
        for t in sorted(df.loc[thin, "ticker"]):
            print(f"  (record gate: dropping {t} — under {MIN_EARNINGS_HISTORY} "
                  f"reported quarters cached)", flush=True)
        df = stage(f"5c has >={MIN_EARNINGS_HISTORY}q history", ~thin, df)

        misses = df["eps_misses_4q"].fillna(99)
        for _, r in df[misses >= max_misses_4q].iterrows():
            print(f"  (record gate: dropping {r['ticker']} — {int(r['eps_misses_4q'])} "
                  f"consensus miss(es) in the last 4 quarters)", flush=True)
        df = stage(f"5c misses<{max_misses_4q} of 4q", misses < max_misses_4q, df)
    else:
        df = stage("5 above 200d SMA", df["above_sma200"].fillna(False), df)

    # 6. Operating margin above the company's GICS-sector median.
    #    In momentum/dip the median is computed over the survivors of 1-5 (see
    #    the README TODO — that is a known leakage: the bar moves with whatever
    #    happened upstream). Earnings mode CANNOT use that: its stage-5 survivor
    #    pool is "whoever happens to report this week", so a sector median over
    #    it would be computed from two or three arbitrary names — a company
    #    could pass or fail purely on which peers share its reporting week.
    #    Here the median is taken over the FULL universe, the same way stage 8
    #    measures leadership.
    if mode == "earnings":
        full_median = full_universe.groupby("gics_sector")["operatingMargins"].median()
        sector_median = df["gics_sector"].map(full_median)
    else:
        sector_median = df.groupby("gics_sector")["operatingMargins"].transform("median")
    strong_margin = df["operatingMargins"] > sector_median
    df = stage("6 op margin>sector med", strong_margin.fillna(False), df)

    # 6b. Earnings quality (dip + earnings modes, soft gate): a name triggering
    #     2+ of the red flags (high accruals / low cash conversion / receivables
    #     or inventory outrunning revenue — see fetch.py) is the quantitative
    #     signature of the value trap the dip doctrine hunts. It matters just as
    #     much walking into a print: accruals running ahead of cash is how a
    #     beat streak gets manufactured, and the quarter that reverses it is the
    #     one you'd be holding. ONE flag never gates (business-model context
    #     needed — that's the research brief's job); flags always feed the
    #     composite penalty in every mode. Disable with --no-eq-gate.
    if mode in ("dip", "earnings") and eq_gate:
        n_flags = _n_eq_flags(df)
        for _, r in df[n_flags >= 2].iterrows():
            print(f"  (eq gate: dropping {r['ticker']} — flags: {r['eq_flags']})", flush=True)
        df = stage("6b earnings quality", n_flags < 2, df)

    # 7. Forward profitability + valuation sanity. 0 < forwardPE enforces
    #    positive forward earnings ("makes money next year"); the high ceiling is
    #    a backstop against absurd valuations, not a value screen — it sits well
    #    above the legit growth range so it never bites a real franchise. NaN
    #    forward P/E (no estimate) is dropped, consistent with the leverage gate
    #    — but those tickers are named, so a missing Yahoo estimate never costs
    #    a candidate invisibly.
    fwd = df["forwardPE"]
    no_estimate = sorted(df.loc[fwd.isna(), "ticker"])
    if no_estimate:
        print(f"  (fwdPE gate: dropping {len(no_estimate)} with NO forward-PE estimate: "
              f"{', '.join(no_estimate)})", flush=True)
    forward_ok = (fwd > 0) & (fwd < max_forward_pe)
    df = stage(f"7 0<fwdPE<{max_forward_pe:g}", forward_ok.fillna(False), df)

    # 8. Category leader — keep the niche's genuine leaders, drop the also-rans.
    #    GICS sub-industries are coarse (NVDA, AVGO, MU, AMD all = "Semiconductors")
    #    so a single #1-per-bucket rule discards real franchises like MU's memory
    #    business. Keep the UNION of:
    #      (a) top-N by market cap in the sub-industry (the clear leaders), and
    #      (b) any "co-leader" whose market cap ≥ coleader_ratio × the bucket's
    #          biggest name (proportional → keeps a giant like MU at 25% of NVDA,
    #          drops small tag-alongs like SNDK; "between MU and SNDK, pick MU").
    #    subind_rank / mc_vs_subind_leader come from _add_derived and are
    #    measured against the FULL universe, not the survivors — otherwise (esp.
    #    in dip mode, where the true leader is usually not dipping) a #4 name
    #    would inherit "leader" status just because its betters failed a gate.
    #      (c) any name ≥ coleader_2nd_ratio × the bucket's SECOND-biggest name.
    #          (b) is measured against the leader, so a runaway #1 mechanically
    #          evicts genuine leaders — see the note on mc_vs_2nd in
    #          _add_derived. (c) is scale-free w.r.t. the leader and needs no
    #          recalibration as the market grows.
    #    SKIPPED in earnings mode. "Biggest in its niche" answers "can this
    #    company hold its pricing for years" — the right question for a
    #    multi-year shortage thesis, the wrong one for a print eight days out.
    #    A #3 name with four straight beats is a better earnings candidate than
    #    a #1 name that keeps missing, and the stage-5b market-cap floor already
    #    keeps the run out of the small caps this rule was really excluding.
    if mode == "earnings":
        funnel.append({"stage": "8 niche leaders", "in": len(df), "out": len(df),
                       "dropped": 0, "skipped": "not applicable in earnings mode "
                                                "(stage 5b market-cap floor instead)"})
        print(f"  {'8 niche leaders':<22} {len(df):>4} -> {len(df):>4}  "
              f"(skipped — earnings mode gates on market cap at 5b)", flush=True)
    else:
        keep = (
            (df["subind_rank"] <= leaders_per_subindustry)
            | (df["mc_vs_subind_leader"] >= coleader_ratio)
            | (df["mc_vs_2nd"] >= coleader_2nd_ratio)
        )
        label = (f"8 niche leaders (N={leaders_per_subindustry},R={coleader_ratio:g},"
                 f"R2={coleader_2nd_ratio:g})")
        df = stage(label, keep.fillna(False), df)
        funnel[-1].update({
            "leaders_per_subindustry": leaders_per_subindustry,
            "coleader_ratio": coleader_ratio,
            "coleader_2nd_ratio": coleader_2nd_ratio,
        })

    # 9. Composite score + optional trim to target. An empty survivor set is a
    #    real outcome in earnings mode — a mid-quarter week can have nobody
    #    reporting — so it exits cleanly with empty outputs rather than blowing
    #    up in the rank math on zero-length columns.
    if df.empty:
        df["composite_score"] = pd.Series(dtype=float)
    else:
        df["composite_score"] = _composite_score(df, mode=mode)
    df = df.sort_values("composite_score", ascending=False).reset_index(drop=True)
    n_in = len(df)
    if trim and len(df) > target:
        df = df.head(target).copy()
        funnel.append({"stage": "9 trim to target", "in": n_in, "out": len(df),
                       "dropped": n_in - len(df), "target": target})
        print(f"  {'9 trim to target':<22} {n_in:>4} -> {len(df):>4}  (top {target} by composite score)", flush=True)
    else:
        funnel.append({"stage": "9 trim to target", "in": n_in, "out": len(df),
                       "dropped": 0, "target": target, "trimmed": False})

    df.insert(0, "rank", range(1, len(df) + 1))
    return df, funnel


# ─────────────────────────────────────────────────────────────────────────────
# Output
# ─────────────────────────────────────────────────────────────────────────────

# Columns surfaced in the human-readable CSV (full record goes to JSON).
# dist_52w_high is the dip-depth signal — useful in momentum CSVs too, central
# to the dip screen.
CSV_COLS = [
    "rank", "ticker", "security", "gics_sector", "gics_sub_industry",
    "marketCap", "composite_score",
    "next_earnings", "days_to_earnings",
    "eps_beats_4q", "eps_misses_4q", "eps_surprise_avg_4q", "eps_surprise_trend",
    "eps_yoy_q", "rev_yoy_q", "rev_accel", "rev_up_years",
    "rev_growth_ttm", "revenueGrowth", "operatingMargins", "profitMargins", "returnOnEquity",
    "net_debt_ebitda", "dist_sma200", "dist_52w_high", "ret_12m", "analyst_upside",
    "trailingPE", "forwardPE", "recommendationKey",
    "accrual_ratio", "cfo_ni", "eq_flags",
]

_DOCTRINE = {
    "momentum": "profitable + US + TTM-revenue-growth + manageable-leverage + "
                "positive-momentum (price ABOVE 200d SMA) + strong-margins + "
                "positive-forward-earnings (0<fwdPE<cap), then category leaders "
                "per GICS sub-industry (leadership measured vs the full "
                "universe), trimmed by composite quality/explosive "
                "(growth + momentum) score.",
    "dip": "profitable + US + TTM-revenue-growth (anti-value-trap) + "
           "manageable-leverage + IN A DIP (price BELOW 200d SMA, drawdown from "
           "52w high within floor) + strong-margins + positive-forward-earnings "
           "(0<fwdPE<cap, tighter for cheapness), then category leaders per GICS "
           "sub-industry (leadership measured vs the full universe), trimmed by "
           "composite rebound score (analyst upside + drawdown room + quality + "
           "balance-sheet survival).",
    "earnings": "profitable + ANY DOMICILE (the US gate is skipped — domicile "
                "does not affect a print) + TTM-revenue-growth + manageable-leverage + "
                "REPORTING WITHIN THE WINDOW (no SMA/trend gate at all — the "
                "catalyst is the scheduled print, so the name qualifies above "
                "OR below its 200d average) + market cap above the size floor "
                "(replaces the niche-leadership rule: a print is not a "
                "leadership question, and size is what makes a bad gap "
                "survivable) + a clean 4-quarter consensus record (fewer than "
                "MAX_MISSES misses, enough history to judge) + strong margins "
                "vs the FULL-universe sector median + earnings-quality soft "
                "gate + positive-forward-earnings, trimmed by composite "
                "beat-streak score (size of beats + streak + beat trend + "
                "revenue growth and acceleration + quality).",
}


def _write_outputs(df: pd.DataFrame, funnel: list[dict], mode: str = "momentum") -> None:
    output_dir = _output_dir(mode)
    os.makedirs(output_dir, exist_ok=True)

    csv_cols = [c for c in CSV_COLS if c in df.columns]
    csv_path = os.path.join(output_dir, "shortlist.csv")
    df[csv_cols].to_csv(csv_path, index=False)

    json_path = os.path.join(output_dir, "shortlist.json")
    records = json.loads(df.replace({np.nan: None}).to_json(orient="records"))
    # Nest the flat earnings-quality fields into one block per record; a
    # missing metric stays an explicit null with the reason in `note`.
    from fetch import EQ_FIELDS, EARN_FIELDS
    # The beat-streak block, same treatment. next_earnings/days_to_earnings stay
    # at the top level too — the ledger records the date for every mode, not
    # just this one.
    trend_fields = [f for f in EARN_FIELDS if f not in ("next_earnings", "days_to_earnings")]
    for rec in records:
        flags = rec.pop("eq_flags", None) or ""
        rec["earnings_quality"] = {
            **{k: rec.pop(k, None) for k in EQ_FIELDS},
            "flags": [f for f in flags.split(",") if f],
            "note": rec.pop("eq_note", None),
        }
        rec["earnings_trend"] = {
            "next_earnings": rec.get("next_earnings"),
            "days_to_earnings": rec.get("days_to_earnings"),
            **{k: rec.pop(k, None) for k in trend_fields},
            **{k: rec.pop(k, None) for k in ("rev_yoy_q", "rev_accel", "rev_up_years")},
            "note": rec.pop("earn_note", None),
        }
    payload = {
        "generated": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mode": mode,
        "count": len(df),
        "doctrine": _DOCTRINE.get(mode, _DOCTRINE["momentum"]),
        "candidates": records,
    }
    with open(json_path, "w") as f:
        json.dump(payload, f, indent=2)

    with open(os.path.join(output_dir, "funnel.json"), "w") as f:
        json.dump(funnel, f, indent=2)

    print(f"\nWrote {len(df)} candidates ({mode} mode) to:")
    print(f"  {csv_path}")
    print(f"  {json_path}")


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--mode", choices=MODES, default="momentum",
                    help="momentum (default): buy strength, price ABOVE 200d SMA, "
                         "writes output/momentum/. dip: buy a reboundable quality "
                         "dip, price BELOW 200d SMA within the drawdown floor, "
                         "writes output/dip/. earnings: buy into a scheduled "
                         "print — no SMA gate, gates on the earnings window + a "
                         "market-cap floor + the 4-quarter beat record, writes "
                         "output/earnings/.")
    ap.add_argument("--target", type=int, default=DEFAULT_TARGET, help="Shortlist size to trim to.")
    ap.add_argument("--max-net-debt-ebitda", type=float, default=DEFAULT_MAX_NET_DEBT_EBITDA)
    ap.add_argument("--max-forward-pe", type=float, default=None,
                    help="Forward-P/E ceiling. Names must have 0 < forwardPE < this "
                         "— positive forward earnings and not an absurd valuation. "
                         "Defaults to 60 (momentum) / 35 (dip, cheapness tilt) when "
                         "not given.")
    ap.add_argument("--dip-drawdown-floor", type=float, default=DEFAULT_DIP_DRAWDOWN_FLOOR,
                    help="Dip mode only: drop names down more than this fraction "
                         "from their 52-week high (default 0.55 → keeps corrections, "
                         "rejects falling knives).")
    ap.add_argument("--earnings-within", type=int, default=DEFAULT_EARNINGS_WITHIN_DAYS,
                    help="Earnings mode only: keep names whose next scheduled "
                         "report is within this many days (default 7). Widen it "
                         "when a mid-quarter week comes back nearly empty.")
    ap.add_argument("--min-market-cap", type=float, default=DEFAULT_MIN_MARKET_CAP,
                    help="Earnings mode only: market-cap floor in dollars "
                         "(default 20e9). Replaces the stage-8 niche-leadership "
                         "rule — don't gamble a print on a small cap.")
    ap.add_argument("--max-misses-4q", type=int, default=DEFAULT_MAX_MISSES_4Q,
                    help="Earnings mode only: drop names with this many or more "
                         "consensus EPS misses in the last 4 quarters (default 2 "
                         "→ one miss is tolerated). Set to 1 to demand a clean "
                         "4-for-4 beat streak.")
    ap.add_argument("--leaders-per-subindustry", type=int, default=DEFAULT_LEADERS_PER_SUBINDUSTRY,
                    help="Keep at least the top-N market-cap names per GICS "
                         "sub-industry (default 2).")
    ap.add_argument("--coleader-ratio", type=float, default=DEFAULT_COLEADER_RATIO,
                    help="Also keep any name whose market cap is ≥ this fraction "
                         "of its sub-industry leader (default 0.20). Set to 1.0 "
                         "to disable and rely on the other two rules.")
    ap.add_argument("--coleader-2nd-ratio", type=float, default=DEFAULT_COLEADER_2ND_RATIO,
                    help="Also keep any name whose market cap is ≥ this fraction "
                         "of its sub-industry's SECOND-biggest name (default 0.50). "
                         "Immune to a runaway #1 inflating the --coleader-ratio bar "
                         "(this is what keeps MU in when NVDA is worth $5T). Set to "
                         "1.0 to disable.")
    ap.add_argument("--no-trim", action="store_true", help="Keep all category leaders (skip the stage-9 trim).")
    ap.add_argument("--no-eq-gate", action="store_true",
                    help="Dip and earnings modes: disable the stage-6b "
                         "earnings-quality soft gate (2+ red flags drops a "
                         "name). Flags still penalize the composite and appear "
                         "in the shortlist.")
    args = ap.parse_args()

    max_forward_pe = args.max_forward_pe
    if max_forward_pe is None:
        max_forward_pe = DEFAULT_MAX_FORWARD_PE_DIP if args.mode == "dip" else DEFAULT_MAX_FORWARD_PE

    df, funnel = run_screen(
        target=args.target,
        max_net_debt_ebitda=args.max_net_debt_ebitda,
        max_forward_pe=max_forward_pe,
        leaders_per_subindustry=args.leaders_per_subindustry,
        coleader_ratio=args.coleader_ratio,
        coleader_2nd_ratio=args.coleader_2nd_ratio,
        trim=not args.no_trim,
        mode=args.mode,
        dip_drawdown_floor=args.dip_drawdown_floor,
        eq_gate=not args.no_eq_gate,
        earnings_within_days=args.earnings_within,
        min_market_cap=args.min_market_cap,
        max_misses_4q=args.max_misses_4q,
    )
    _write_outputs(df, funnel, mode=args.mode)

    if df.empty:
        print(f"\nNo candidates survived the {args.mode} funnel.")
        return

    print(f"\nTop 15 by composite score ({args.mode} mode):")
    if args.mode == "earnings":
        show = ["rank", "ticker", "security", "gics_sub_industry", "marketCap",
                "next_earnings", "days_to_earnings", "eps_beats_4q",
                "eps_surprise_avg_4q", "rev_growth", "rev_accel",
                "operatingMargins", "composite_score"]
    else:
        perf_col = "dist_52w_high" if args.mode == "dip" else "ret_12m"
        show = ["rank", "ticker", "security", "gics_sub_industry", "marketCap",
                "rev_growth", "operatingMargins", perf_col, "analyst_upside",
                "composite_score"]
    show = [c for c in show if c in df.columns]
    with pd.option_context("display.max_rows", None, "display.width", 200,
                           "display.float_format", lambda x: f"{x:,.3f}"):
        print(df[show].head(15).to_string(index=False))


if __name__ == "__main__":
    main()
