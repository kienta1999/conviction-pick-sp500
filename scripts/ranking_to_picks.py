#!/usr/bin/env python3
"""Build the picks CSV execute_picks.py trades: POLICY.md §6's three slots.

    uv run python scripts/ranking_to_picks.py                              # fresh account: top 3 of latest rank10
    uv run python scripts/ranking_to_picks.py --held reports/web_account.json [--drop SYK]
    uv run python scripts/ranking_to_picks.py --selftest

Slot rule (POLICY §6): a held name keeps its slot unless it is --drop'ed (stop /
target / expiry — the skill passes scorecard.py --check's alerts) or it is still
in output/dip/shortlist.csv but outside the latest run's top SLOTS (outranked
while still a dip). A held name absent from the shortlist recovered above its
200d and is kept. Free slots fill from the latest rank10, top down. META is
excluded (owner's employer compliance). Output schema matches ranker-21d-sp500
picks: ticker, predicted_return (11 − rank), gics_sector, weight (equal).
"""
import argparse
import json
import os

import pandas as pd

from basket_backtest import EXCLUDE, LEDGER, _ROOT

SLOTS = 3
OUT_DIR = os.path.join(_ROOT, "picks")


def build(ledger, shortlist, held, drop, mode="dip", slots=SLOTS):
    d = ledger[(ledger["mode"] == mode) & (ledger["kind"] == "rank10")]
    if d.empty:
        raise SystemExit(f"no {mode} rank10 rows in ledger")
    d = d[d["date"] == d["date"].max()].sort_values("rank")
    d = d[~d["ticker"].isin(EXCLUDE)]
    ranked = d["ticker"].tolist()
    in_screen = set(shortlist["ticker"]) if shortlist is not None else set()

    keep = [t for t in held if t not in drop and t not in EXCLUDE
            and not (t in in_screen and t not in ranked[:slots])]
    fill = [t for t in ranked if t not in keep][:max(slots - len(keep), 0)]
    names = keep + fill
    rank = {t: r for r, t in zip(d["rank"], d["ticker"])}
    out = pd.DataFrame({
        "ticker": names,
        "predicted_return": [11 - rank.get(t, 10) for t in names],   # held-but-unranked sorts last
        "gics_sector": [shortlist.set_index("ticker")["gics_sector"].get(t, "") if shortlist is not None else "" for t in names],
        "weight": 1.0 / len(names),
    })
    out.attrs["date"] = d["date"].iloc[0]
    out.attrs["sold"] = sorted(set(held) - set(names))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="dip")
    ap.add_argument("--held", help="reports/web_account.json from capture_state.js; omit for a fresh account")
    ap.add_argument("--drop", nargs="*", default=[], help="held names whose slot freed (stop/target/expiry)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    sl_path = os.path.join(_ROOT, "output", a.mode, "shortlist.csv")
    sl = pd.read_csv(sl_path) if os.path.exists(sl_path) else None
    held = []
    if a.held:
        held = [t for t, q in json.load(open(a.held))["positions"].items() if float(q) > 0]
    out = build(pd.read_csv(LEDGER), sl, held, set(a.drop), a.mode)
    path = os.path.join(OUT_DIR, f"picks_{a.mode}_{out.attrs['date']}.csv")
    out.to_csv(path, index=False)
    print(out.to_string(index=False))
    print(f"-> {path}  ({len(out)} slots; sold: {out.attrs['sold'] or 'none'})")


def selftest():
    led = pd.DataFrame([dict(date="2026-01-01", mode="dip", kind="rank10", rank=r, ticker=t)
                        for r, t in enumerate(["META", "A", "B", "C", "D"], 1)]
                       + [dict(date="2025-01-01", mode="dip", kind="rank10", rank=1, ticker="OLD")])
    sl = pd.DataFrame({"ticker": ["A", "B", "C", "D", "X"], "gics_sector": "S"})
    out = build(led, sl, held=[], drop=set())
    assert list(out["ticker"]) == ["A", "B", "C"], out                   # fresh: META out, older run ignored
    # held: A (top-3, keep), X (in screen, outranked → sell), R (recovered, not in screen → keep)
    out = build(led, sl, held=["A", "X", "R"], drop=set())
    assert list(out["ticker"]) == ["A", "R", "B"] and out.attrs["sold"] == ["X"], out
    out = build(led, sl, held=["A", "R"], drop={"R"})                     # R stopped → freed, refilled
    assert list(out["ticker"]) == ["A", "B", "C"] and out.attrs["sold"] == ["R"]
    assert abs(out["weight"].sum() - 1) < 1e-9
    print("selftest ok")


if __name__ == "__main__":
    main()
