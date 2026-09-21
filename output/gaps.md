# Runs whose inputs are missing, and why

A permanent record, so a gap in the audit trail reads as a known loss rather than an oversight
nobody noticed. One row per run whose committed inputs do not match its published picks.

| run | missing | why | recoverable? |
|---|---|---|---|
| 2026-09-21 (dip, momentum, earnings) | `shortlist_*.csv`, `shortlist_*.json`, `funnel_*.json`, `research_dossier_*.md` | The run committed only files whose path was new that day. These four had to be overwritten in place, so `git add` skipped them in all three modes and the repo kept 2026-09-17's screen. | **No.** See below. |

## Why 2026-09-21 cannot be regenerated

The screen was run at 08:30 UTC, before the US open, so it saw the 2026-09-18 close. It produced
29 dip candidates; the panel ranked BR (#7) and BKNG (#10) out of them. The committed 2026-09-17
shortlist has 32 names and contains neither, which is how the gap was found.

Re-running the screen later the same day does **not** reproduce it:

- **Prices have moved.** A re-run picks up the live 2026-09-21 bar, not the 2026-09-18 close the
  panel screened on.
- **Fundamentals are point-in-time and cannot be rewound.** `forwardPE`, `marketCap`,
  `operatingMargins` and `country` come from Yahoo's current snapshot. There is no historical
  endpoint for them.
- **A re-run measured on 2026-09-21 was also materially incomplete.** Of 150 cached records,
  `operatingMargins` and `country` were present in only 110. Those feed stage 2 (US company) and
  stage 6 (op margin above sector median), both hard gates, so roughly a quarter of the universe
  would drop for *missing data* rather than for failing a test. The resulting shortlist would be
  a different screen wearing the same date.

Writing that file as `shortlist_2026-09-21.csv` would have produced something that looks like the
panel's inputs and is not. The picks stay unreproducible, and this file says so.

## What stops it recurring

`scripts/artifacts.py` dates every artifact, so each run writes new paths that show up as
untracked. `scripts/ranking_to_picks.py` refuses to run when the newest shortlist and the newest
ranking carry different dates. See POLICY.md, "Scheduled runs".
