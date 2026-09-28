#!/usr/bin/env python3
"""Cross-run consensus: the official pick is what survives several panels, not one day's #1.

    uv run python scripts/consensus.py                      # dip + momentum, last 5 runs, print
    uv run python scripts/consensus.py --mode dip --write   # also write output/dip/consensus_<asof>.md
    uv run python scripts/consensus.py --asof 2026-09-26 --runs 5
    uv run python scripts/consensus.py --selftest

Why: in the 2026-09-22 → 09-28 consistency runs the daily #1 changed on near-ties
(BR 30 vs IDXX 29 on 09-24; a four-way 3-3-3-3 momentum tie the same day), while the top 10
around it kept 6-9 of 10 names day to day. Taking the argmax of noisy scores publishes the
noise. This re-scores the last N rank10 lists in picks/ledger.csv with Borda points
(rank 1 = 10 … rank 10 = 1), and a name QUALIFIES only if it made the top 10 in at least
`ceil(0.8 * N)` of them (4 of 5). The consensus top 3 is the three highest-scoring qualifiers.

It also prints the screen-only top 3 — the deterministic composite ranking in that run's
shortlist, no AI — as a baseline, so the scorecard can eventually say whether the panels
beat the screen they start from. Read-only on the ledger; trades nothing."""
import argparse
import csv
import math
import os
from collections import defaultdict

import artifacts

LEDGER = artifacts.ROOT / "picks" / "ledger.csv"
MODES = ("dip", "momentum")


def rank10_runs(rows, mode, asof=None):
    """{date: [ticker by rank]} for every rank10 run of `mode` on or before `asof`."""
    runs = defaultdict(dict)
    for r in rows:
        if r["mode"] == mode and r["kind"] == "rank10" and (asof is None or r["date"] <= asof):
            runs[r["date"]][int(r["rank"])] = r["ticker"]
    return {d: [v[k] for k in sorted(v)] for d, v in sorted(runs.items())}


def consensus(runs, n=5):
    """Score the newest `n` runs. Returns (dates, table) with table sorted by points, best first."""
    dates = sorted(runs)[-n:]
    need = math.ceil(0.8 * len(dates))
    stats = defaultdict(lambda: {"pts": 0, "top10": 0, "top3": 0, "first": 0, "ranks": {}})
    for d in dates:
        for i, t in enumerate(runs[d][:10], start=1):
            s = stats[t]
            s["pts"] += 11 - i
            s["top10"] += 1
            s["top3"] += i <= 3
            s["first"] += i == 1
            s["ranks"][d] = i
    table = [dict(ticker=t, qualifies=s["top10"] >= need, **s) for t, s in stats.items()]
    table.sort(key=lambda s: (-s["pts"], -s["top3"], -s["first"], s["ticker"]))
    return dates, table


def screen_top3(mode, asof):
    """Top 3 of the newest dated shortlist on or before `asof` (the screen's composite rank)."""
    best = None
    for d in (artifacts.mode_dir(mode), artifacts.mode_dir(mode) / "old"):
        if not d.is_dir():
            continue
        for p in d.iterdir():
            m = artifacts.DATE_RE.match(p.name)
            if m and m.group("stem") == "shortlist" and m.group("ext") == ".csv" and m.group("date") <= asof:
                if best is None or m.group("date") > best[0]:
                    best = (m.group("date"), p)
    if best is None:
        return None, []
    with open(best[1]) as f:
        rows = sorted(csv.DictReader(f), key=lambda r: int(r["rank"]))
    return best[0], [r["ticker"] for r in rows[:3]]


def render(mode, dates, table, screen_date, screen):
    n, need = len(dates), math.ceil(0.8 * len(dates))
    top = [s["ticker"] for s in table if s["qualifies"]][:3]
    out = [f"# {mode} consensus — as of {dates[-1]} ({n} runs: {dates[0]} → {dates[-1]})", ""]
    if n < 5:
        out += [f"**Only {n} run(s) on file — thin evidence; treat as provisional.**", ""]
    out += [f"**Consensus top 3:** {', '.join(top) if top else 'none — no name made the top 10 in enough runs'}",
            f"(qualify = in the top 10 in ≥ {need} of {n} runs; ordered by Borda points)", "",
            f"**Daily #1s over the window:** {' → '.join(runs_first(table, dates))}", ""]
    if screen:
        out += [f"**Screen-only top 3** (composite rank, shortlist {screen_date}, no AI): {', '.join(screen)}", ""]
    out += ["| # | ticker | points | top 10 | top 3 | #1 | qualifies | rank by run |", "|---|---|---|---|---|---|---|---|"]
    for i, s in enumerate(table[:15], start=1):
        by_run = " ".join(str(s["ranks"].get(d, "–")) for d in dates)
        out.append(f"| {i} | {s['ticker']} | {s['pts']} | {s['top10']}/{n} | {s['top3']}/{n} | {s['first']} | "
                   f"{'yes' if s['qualifies'] else 'no'} | {by_run} |")
    out += ["", "Borda: rank 1 = 10 pts … rank 10 = 1. Research output, not financial advice."]
    return "\n".join(out) + "\n"


def runs_first(table, dates):
    first = {d: t["ticker"] for t in table for d, r in t["ranks"].items() if r == 1}
    return [first.get(d, "?") for d in dates]


def selftest():
    runs = {"d1": list("ABCDEFGHIJ"), "d2": list("BACDEFGHIK"), "d3": list("ABDCEFGHIL"),
            "d4": list("CBADEFGHIM"), "d5": list("BCAEDFGHIN"), "d0": list("ZYXWVUTSRQ")}
    dates, t = consensus(runs, 5)
    assert dates == ["d1", "d2", "d3", "d4", "d5"]                       # newest 5, d0 dropped
    by = {s["ticker"]: s for s in t}
    assert by["A"]["pts"] == 10 + 9 + 10 + 8 + 8 and by["A"]["top3"] == 5
    assert [s["ticker"] for s in t if s["qualifies"]][:3] == ["B", "A", "C"]   # B 46 > A 45 > C 41
    assert not by["J"]["qualifies"] and by["J"]["top10"] == 1            # one appearance never qualifies
    assert "Z" not in by                                                 # outside the window
    _, t4 = consensus({k: runs[k] for k in ["d1", "d2", "d3", "d4"]}, 5)
    assert all(s["qualifies"] == (s["top10"] >= 4) for s in t4)          # ceil(0.8*4) = 4
    md = render("dip", dates, t, "d5", ["X", "Y", "Z"])
    assert "Consensus top 3:** B, A, C" in md and "Screen-only top 3" in md
    print("consensus selftest ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=MODES + ("all",), default="all")
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--asof", default=None, help="score runs on or before this date (default: all)")
    ap.add_argument("--write", action="store_true", help="write output/<mode>/consensus_<asof>.md")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    with open(LEDGER) as f:
        rows = list(csv.DictReader(f))
    for mode in (MODES if a.mode == "all" else (a.mode,)):
        runs = rank10_runs(rows, mode, a.asof)
        if not runs:
            print(f"{mode}: no rank10 runs on file"); continue
        dates, table = consensus(runs, a.runs)
        sdate, screen = screen_top3(mode, dates[-1])
        md = render(mode, dates, table, sdate, screen)
        print(md)
        if a.write:
            p = artifacts.dated(mode, "consensus", ".md", dates[-1])
            p.write_text(md)
            print(f"wrote {os.path.relpath(p, artifacts.ROOT)}\n")


if __name__ == "__main__":
    main()
