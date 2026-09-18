#!/usr/bin/env python3
"""Turn the latest rank10 run in picks/ledger.csv into a picks CSV execute_picks.py can trade.

    uv run python scripts/ranking_to_picks.py                    # dip, equal3 → picks/picks_dip_<date>.csv
    uv run python scripts/ranking_to_picks.py --scheme equal10
    uv run python scripts/ranking_to_picks.py --selftest

The ledger is the record the skill wrote from output/dip/final_ranking.md, so it
is the source — not the markdown. Names in basket_backtest.EXCLUDE (META: owner's
employer compliance, POLICY.md §6) are dropped and the rest renormalized to 1.0.
Output schema matches ranker-21d-sp500 picks: ticker, predicted_return (11 − rank,
so --top-n keeps the panel's order), gics_sector, weight.
"""
import argparse
import os

import pandas as pd

from basket_backtest import EXCLUDE, LEDGER, SCHEMES, _ROOT

OUT_DIR = os.path.join(_ROOT, "picks")


def build(ledger: pd.DataFrame, shortlist: pd.DataFrame | None, mode: str, scheme: str) -> pd.DataFrame:
    d = ledger[(ledger["mode"] == mode) & (ledger["kind"] == "rank10")]
    if d.empty:
        raise SystemExit(f"no {mode} rank10 rows in ledger")
    d = d[d["date"] == d["date"].max()].sort_values("rank")
    d = d[~d["ticker"].isin(EXCLUDE)].reset_index(drop=True)
    w = SCHEMES[scheme](len(d))
    out = pd.DataFrame({
        "ticker": d["ticker"],
        "predicted_return": 11 - d["rank"],
        "gics_sector": d["ticker"].map(shortlist.set_index("ticker")["gics_sector"]) if shortlist is not None else "",
        "weight": w / w.sum(),
    })
    out.attrs["date"] = d["date"].iloc[0]
    return out[out["weight"] > 0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="dip")
    ap.add_argument("--scheme", default="equal3", choices=list(SCHEMES))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    sl_path = os.path.join(_ROOT, "output", a.mode, "shortlist.csv")
    sl = pd.read_csv(sl_path) if os.path.exists(sl_path) else None
    out = build(pd.read_csv(LEDGER), sl, a.mode, a.scheme)
    path = os.path.join(OUT_DIR, f"picks_{a.mode}_{out.attrs['date']}.csv")
    out.to_csv(path, index=False)
    print(out.to_string(index=False))
    print(f"-> {path}  ({a.scheme}, {len(out)} names, weights sum {out['weight'].sum():.3f})")


def selftest():
    led = pd.DataFrame([
        dict(date="2026-01-01", mode="dip", kind="rank10", rank=r, ticker=t)
        for r, t in enumerate(["META", "A", "B", "C", "D"], 1)
    ] + [dict(date="2025-01-01", mode="dip", kind="rank10", rank=1, ticker="OLD")])
    out = build(led, None, "dip", "equal3")
    assert list(out["ticker"]) == ["A", "B", "C"], out          # META dropped, older run ignored, top-3 of the rest
    assert abs(out["weight"].sum() - 1) < 1e-9
    assert list(out["predicted_return"]) == [9, 8, 7]           # panel order preserved for --top-n
    print("selftest ok")


if __name__ == "__main__":
    main()
