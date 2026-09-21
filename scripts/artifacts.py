#!/usr/bin/env python3
"""Dated run artifacts: every file a run writes is born with its run date in the name.

Why: on 2026-09-21 all three modes committed only the files whose path was NEW that day
(parts/<DATE>/…, and the memos archived into old/). shortlist.csv, shortlist.json,
funnel.json and research_dossier.md had to be OVERWRITTEN in place, so `git add` of the new
paths missed them and the repo kept 2026-09-17's screen. Those picks now have no recoverable
inputs — the 29-name shortlist the panel actually ranked from only ever existed on disk.

A rule you have to remember ("also commit the four that look unchanged") breaks. A filename
that is different every run cannot be missed the same way: it shows up as untracked.

    shortlist_2026-09-21.csv   funnel_2026-09-21.json   final_ranking_2026-09-21.md

`latest()` finds the newest one so consumers never hardcode a date, and falls back to the old
undated name so nothing breaks mid-transition. `archive_superseded()` moves every older dated
file into old/ once a newer run exists — and if that step is ever skipped, the cost is a tidy-up,
not a lost audit trail."""
import os, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE_RE = re.compile(r"^(?P<stem>.+)_(?P<date>\d{4}-\d{2}-\d{2})(?P<ext>\.[A-Za-z0-9]+)$")


def mode_dir(mode):
    return ROOT / "output" / mode


def dated(mode, stem, ext, date):
    """output/<mode>/<stem>_<date><ext> — the path a run writes to."""
    return mode_dir(mode) / f"{stem}_{date}{ext}"


def _candidates(mode, stem, ext):
    d = mode_dir(mode)
    if not d.is_dir():
        return []
    out = []
    for p in d.iterdir():
        m = DATE_RE.match(p.name)
        if m and m.group("stem") == stem and m.group("ext") == ext:
            out.append((m.group("date"), p))
    return sorted(out)


def latest(mode, stem, ext):
    """Newest dated file for this stem, else the legacy undated name, else None."""
    c = _candidates(mode, stem, ext)
    if c:
        return c[-1][1]
    legacy = mode_dir(mode) / f"{stem}{ext}"
    return legacy if legacy.exists() else None


def latest_date(mode, stem, ext):
    c = _candidates(mode, stem, ext)
    return c[-1][0] if c else None


def archive_superseded(mode, stem=None, ext=None):
    """Move every dated file that a newer run has superseded into output/<mode>/old/.

    Per stem: keep the newest, archive the rest. Skipping this only leaves clutter at the top
    level — it can never delete the newest run's inputs."""
    d, old = mode_dir(mode), mode_dir(mode) / "old"
    if not d.is_dir():
        return []
    groups = {}
    for p in d.iterdir():
        m = DATE_RE.match(p.name)
        if not m or not p.is_file():
            continue
        if (stem and m.group("stem") != stem) or (ext and m.group("ext") != ext):
            continue
        groups.setdefault((m.group("stem"), m.group("ext")), []).append((m.group("date"), p))
    moved = []
    for (_s, _e), items in groups.items():
        for _date, p in sorted(items)[:-1]:          # everything but the newest
            old.mkdir(exist_ok=True)
            shutil.move(str(p), str(old / p.name))
            moved.append(p.name)
    return moved


def selftest():
    import tempfile, json
    global ROOT
    keep = ROOT
    try:
        ROOT = Path(tempfile.mkdtemp())
        d = mode_dir("dip"); d.mkdir(parents=True)
        for dt in ("2026-09-17", "2026-09-21"):
            dated("dip", "shortlist", ".csv", dt).write_text("ticker\n")
        (d / "notes.md").write_text("not a dated artifact")
        assert latest("dip", "shortlist", ".csv").name == "shortlist_2026-09-21.csv"
        assert latest_date("dip", "shortlist", ".csv") == "2026-09-21"
        assert latest("dip", "funnel", ".json") is None
        (d / "funnel.json").write_text("[]")                       # legacy undated
        assert latest("dip", "funnel", ".json").name == "funnel.json"
        moved = archive_superseded("dip")
        assert moved == ["shortlist_2026-09-17.csv"], moved
        assert (d / "old" / "shortlist_2026-09-17.csv").exists()
        assert latest("dip", "shortlist", ".csv").name == "shortlist_2026-09-21.csv"
        assert (d / "notes.md").exists() and (d / "funnel.json").exists()   # untouched
        assert archive_superseded("dip") == []                     # idempotent
        print("artifacts selftest ok")
    finally:
        ROOT = keep


if __name__ == "__main__":
    selftest()
