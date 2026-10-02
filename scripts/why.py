#!/usr/bin/env python3
"""Why is a ticker missing from a shortlist? Reads the screen's drops_<date>.csv.

    uv run python scripts/why.py GOOGL                    # every mode, newest run
    uv run python scripts/why.py GOOGL AMZN --mode momentum
    uv run python scripts/why.py --mode dip --stage 6     # everything stage 6 dropped
    uv run python scripts/why.py GOOGL --date 2026-10-01  # a specific run (also searches old/)

A ticker that is neither dropped nor shortlisted is reported as such (e.g. not in
the S&P 500 roster at all)."""
import argparse
import signal
import sys

import pandas as pd

import artifacts

MODES = ("momentum", "dip", "earnings")


def _path(mode, stem, ext, date):
    if date is None:
        return artifacts.latest(mode, stem, ext)
    for p in (artifacts.dated(mode, stem, ext, date),
              artifacts.mode_dir(mode) / "old" / f"{stem}_{date}{ext}"):
        if p.exists():
            return p
    return None


def main() -> int:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # `why.py ... | head` exits quietly
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("tickers", nargs="*", help="Tickers to explain (case-insensitive).")
    ap.add_argument("--mode", choices=MODES, help="Limit to one mode (default: all three).")
    ap.add_argument("--stage", help="List every ticker dropped at stages starting with this, e.g. 6 or 5b.")
    ap.add_argument("--date", help="Run date YYYY-MM-DD (default: newest).")
    args = ap.parse_args()
    if not args.tickers and not args.stage:
        ap.error("give at least one ticker or --stage")

    wanted = [t.upper() for t in args.tickers]
    for mode in ([args.mode] if args.mode else MODES):
        drops_p = _path(mode, "drops", ".csv", args.date)
        if drops_p is None:
            print(f"[{mode}] no drops csv yet — re-run scripts/screen.py --mode {mode}")
            continue
        drops = pd.read_csv(drops_p)
        short_p = _path(mode, "shortlist", ".csv", args.date)
        short = pd.read_csv(short_p) if short_p else pd.DataFrame(columns=["rank", "ticker"])
        print(f"[{mode}] {drops_p.name}")
        if args.stage:
            hit = drops[drops["stage"].astype(str).str.startswith(args.stage)]
            for _, r in hit.iterrows():
                print(f"  {r['ticker']:<6} {r['stage']:<28} {r['reason']}")
            print(f"  ({len(hit)} dropped at stage {args.stage}*)")
        for t in wanted:
            row = short[short["ticker"] == t]
            if len(row):
                print(f"  {t:<6} SHORTLISTED at rank {int(row['rank'].iloc[0])}")
                continue
            d = drops[drops["ticker"] == t]
            if len(d):
                r = d.iloc[0]
                print(f"  {t:<6} dropped at {r['stage']}: {r['reason']}")
            else:
                print(f"  {t:<6} not in this run at all (not an S&P 500 member?)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
