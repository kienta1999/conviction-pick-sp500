#!/usr/bin/env python3
"""Roll the dip rank10 baskets forward as a rebalanced portfolio — weight / leverage / vol-target sweep.

Each dip rank10 run in picks/ledger.csv is a basket bought at the close of its run
date and held until the next run date (the rebalance); the last basket runs to
today. Sweeps weighting schemes (equal top-N, rank-linear, single) × leverage cap ×
SPY vol-target, with margin interest charged on gross > 1. META is excluded
(owner's employer compliance — see POLICY.md §6) and weights renormalized.

    uv run python scripts/basket_backtest.py            # table
    uv run python scripts/basket_backtest.py --selftest # synthetic check

ponytail: 5 runs / ~3 months of data. This ranks schemes against each other; it
cannot tell edge from noise. Re-run as the ledger grows.
"""
import argparse
import os

import numpy as np
import pandas as pd

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(_ROOT, "picks", "ledger.csv")
EXCLUDE = {"META"}
MARGIN_APR = 0.0613
SCHEMES = {
    "equal10": lambda n: np.ones(n),
    "equal5": lambda n: (np.arange(n) < 5).astype(float),
    "equal3": lambda n: (np.arange(n) < 3).astype(float),
    "single": lambda n: (np.arange(n) < 1).astype(float),
    "linear": lambda n: (n - np.arange(n)).astype(float),      # 10,9,...,1
    "top5lin": lambda n: np.where(np.arange(n) < 5, 5 - np.arange(n), 0.0),
}


def baskets(ledger, mode="dip"):
    d = pd.read_csv(ledger)
    d = d[(d["mode"] == mode) & (d["kind"] == "rank10") & ~d["ticker"].isin(EXCLUDE)]
    return {pd.Timestamp(k): g.sort_values("rank")["ticker"].tolist() for k, g in d.groupby("date")}


def load_prices(tickers, start):
    import yfinance as yf
    px = yf.download(sorted(tickers) + ["SPY"], start=start, auto_adjust=True, progress=False)["Close"]
    return px.dropna(how="all")


def run(bk, px, scheme, lev, vt):
    """Daily portfolio returns: basket held (d_i, d_{i+1}], gross sized at d_i."""
    rets = px.pct_change()
    spy_vol = np.log(px["SPY"]).diff().rolling(20).std() * np.sqrt(252)
    dates = sorted(bk)
    out = []
    for i, d in enumerate(dates):
        end = dates[i + 1] if i + 1 < len(dates) else px.index[-1]
        names = bk[d]
        w = SCHEMES[scheme](len(names))
        w = w / w.sum()
        gross = lev if vt is None else min(lev, vt / float(spy_vol.asof(d)))
        window = rets.loc[(rets.index > d) & (rets.index <= end), names]
        r = (window @ w) * gross - max(gross - 1, 0) * MARGIN_APR / 252
        out.append(r)
    return pd.concat(out)


def stats(r):
    nav = (1 + r).cumprod()
    dd = (nav / nav.cummax() - 1).min()
    vol = r.std() * np.sqrt(252)
    return dict(ret=nav.iloc[-1] - 1, vol=vol, sharpe=(r.mean() * 252) / vol if vol else np.nan, maxdd=dd)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mode", default="dip")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    bk = baskets(LEDGER, a.mode)
    start = min(bk) - pd.Timedelta(days=45)
    px = load_prices({t for v in bk.values() for t in v}, start)
    print(f"{len(bk)} {a.mode} rank10 runs: {', '.join(str(d.date()) for d in sorted(bk))} → {px.index[-1].date()}")
    spy = px["SPY"].pct_change().loc[px.index > min(bk)]
    s = stats(spy)
    print(f"SPY same window: ret {s['ret']:+.1%}  vol {s['vol']:.0%}  maxdd {s['maxdd']:.1%}\n")
    rows = []
    for scheme in SCHEMES:
        for lev in (1.0, 1.33, 1.5):
            for vt in (None, 0.15, 0.20, 0.25):
                if lev == 1.0 and vt not in (None, 0.20):
                    continue
                r = run(bk, px, scheme, lev, vt)
                rows.append(dict(scheme=scheme, lev=lev, vt=vt or "-", **stats(r), alpha=stats(r)["ret"] - s["ret"]))
    t = pd.DataFrame(rows)
    pd.set_option("display.width", 200)
    print(t.sort_values("sharpe", ascending=False).to_string(index=False, float_format=lambda x: f"{x:+.3f}"))


def selftest():
    idx = pd.bdate_range("2026-01-01", periods=60)
    px = pd.DataFrame({"A": np.linspace(100, 160, 60), "B": np.full(60, 50.0), "SPY": np.linspace(100, 110, 60)}, index=idx)
    bk = {idx[25]: ["A", "B"]}
    r = run(bk, px, "single", 1.0, None)                          # 100% A, no leverage
    assert abs((1 + r).prod() - px["A"].iloc[-1] / px["A"].iloc[25]) < 1e-9
    r = run(bk, px, "equal10", 1.0, None)                         # 50/50, B flat → half of A's daily move
    assert np.allclose(r.values, (px["A"].pct_change().iloc[26:] / 2).values)
    r2 = run(bk, px, "equal10", 2.0, None)                        # 2x gross minus one day of margin
    assert np.allclose(r2.values, 2 * r.values - MARGIN_APR / 252)
    print("selftest ok")


if __name__ == "__main__":
    main()
