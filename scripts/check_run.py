#!/usr/bin/env python3
"""Is this run actually finished? -- uv run python scripts/check_run.py [MODE ...]

A run is finished when every artifact it generated is COMMITTED, not when the memo is written.
On 2026-09-21 all three modes published picks and left their screen uncommitted; the repo kept
2026-09-17's shortlist and those picks lost their inputs for good (output/gaps.md).

Two failures, both of which happened that day:
  1. the newest ranking is dated later than the newest shortlist/funnel/dossier, i.e. the screen
     behind the published picks was never committed;
  2. something under output/ is uncommitted or untracked.

Exits non-zero on either. The run is not done until this exits 0."""
import subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import artifacts

ROOT = Path(__file__).resolve().parent.parent
MODES = ("dip", "momentum", "earnings")
# stem, ext, does a published run require it?
REQUIRED = [("shortlist", ".csv"), ("shortlist", ".json"), ("funnel", ".json"),
            ("research_dossier", ".md")]
GAPS = ROOT / "output" / "gaps.md"


def _last_commit(pathspec):
    r = subprocess.run(["git", "log", "-1", "--format=%ct", "--", pathspec],
                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return int(r) if r else 0


def gap_is_stale(mode):
    """True once output/<mode>/ has been committed more recently than gaps.md was written.

    A gaps.md row describes one historical run. Dates repeat: a rerun on the SAME date inherited
    the suppression and hid a fresh miss (the 2026-09-21 earnings rerun published a pick off
    research batches it never consolidated into a dossier, and this check passed it). Once a mode
    has moved on, the recorded gap no longer describes its current state, so stop forgiving it."""
    return _last_commit(f"output/{mode}") > _last_commit("output/gaps.md")


def known_gaps():
    """Runs already recorded as unrecoverable in output/gaps.md: (mode, date) pairs.

    A gap you have written down is history, not an open defect — it warns, it does not fail, or
    the check would stay red forever and stop meaning anything."""
    import re
    if not GAPS.exists():
        return set()
    out = set()
    for ln in GAPS.read_text().splitlines():
        if not ln.strip().startswith("|"):
            continue
        dates = re.findall(r"\d{4}-\d{2}-\d{2}", ln)
        modes = [m for m in MODES if re.search(rf"\b{m}\b", ln)]
        for d in dates:
            for m in modes:
                out.add((m, d))
    return out


def check_mode(mode, gaps=frozenset()):
    errs, warns = [], []
    if not artifacts.mode_dir(mode).is_dir():
        return errs, warns
    pub = artifacts.latest_date(mode, "final_ranking", ".md") or \
          artifacts.latest_date(mode, "final_pick", ".md")
    if not pub:
        return errs, warns
    for stem, ext in REQUIRED:
        d = artifacts.latest_date(mode, stem, ext)
        if d is None:
            errs.append(f"{mode}: published run {pub} has no dated {stem}{ext} at all")
        elif d < pub:
            msg = (f"{mode}: {stem}{ext} is dated {d} but the published run is {pub} — "
                   f"the screen behind those picks was never committed")
            forgiven = (mode, pub) in gaps and not gap_is_stale(mode)
            (warns if forgiven else errs).append(
                msg + (" [recorded in output/gaps.md]" if forgiven else
                       " — output/gaps.md records this date, but this mode has been committed "
                       "since, so the record no longer describes it"))
    return errs, warns


def main(modes, explicit=False):
    gaps = known_gaps()
    errs, warns = [], []
    for m in modes:
        e, w = check_mode(m, gaps)
        errs += e
        warns += w

    # Scope the commit check to the modes being checked. Running one mode is normal, and a stray
    # file under another mode is that mode's problem, not a reason to block this run. With no
    # args every mode is checked, and so is output/ itself (gaps.md and anything else top-level).
    paths = [f"output/{m}" for m in modes] if explicit else ["output/"]
    dirty = subprocess.run(["git", "status", "--porcelain", *paths], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        errs.append("uncommitted files under output/ — a run is not finished until this is empty:\n"
                    + "\n".join("    " + ln for ln in dirty.splitlines()))

    for w in warns:
        print(f"WARN    {w}")
    for e in errs:
        print(f"ERROR   {e}")
    if errs:
        print(f"\n{len(errs)} problem(s). The run is NOT finished. Commit what is listed, then "
              f"re-run this until it exits 0.")
        return 1
    print(f"run check passed for {', '.join(modes)}: every published run's inputs are dated to "
          f"match, and output/ is fully committed"
          + (f" ({len(warns)} recorded gap(s) ignored)" if warns else ""))
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    bad = [a for a in args if a not in MODES]
    if bad:
        sys.exit(f"unknown mode(s): {', '.join(bad)} — pick from {', '.join(MODES)}")
    sys.exit(main(args or list(MODES), explicit=bool(args)))
