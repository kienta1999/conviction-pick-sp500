# Runs whose inputs are missing, and why

A permanent record, so a gap in the audit trail reads as a known loss rather than an oversight
nobody noticed. One row per run whose committed inputs do not match its published picks.

| run | missing | why | recoverable? |
|---|---|---|---|
| 2026-09-21 (dip, momentum, earnings) | `shortlist_*.csv`, `shortlist_*.json`, `funnel_*.json`, `research_dossier_*.md` | The run committed only files whose path was new that day. These four had to be overwritten in place, so `git add` skipped them in all three modes and the repo kept 2026-09-17's screen. | **No.** See below. |
| 2026-10-18 (momentum) | `shortlist_2026-10-18.*`, `funnel_2026-10-18.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-10-17.json` (generated 2026-10-17 08:57 UTC), reused under the protocol Phase 0 rule at ~23.0h old at the 08:00 PT run start, inside the <24h freshness window — the screen-of-record is committed under its own date. A same-day regeneration was attempted post-panel: identical prices but a different candidate set (APH, PH dropped on Yahoo snapshot-fundamentals drift), so it was not substituted for the screen the panel actually scored. | Inputs are committed (dated 2026-10-17); the 2026-10-18 regeneration was discarded, not lost. |
| 2026-11-03 (dip) | `shortlist_2026-11-03.*`, `funnel_2026-11-03.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-11-02.json` (generated 2026-11-02 09:23:21 UTC pre-market), reused under the protocol Phase 0 1-day cache rule — the screen-of-record is committed under its own date, and the finals disclose the price-base caveat (Friday 2026-10-30 closes; the Monday 2026-11-02 session is not reflected). No same-day regeneration was substituted, per the 2026-10-18 precedent (a regeneration could drift the candidate set away from the screen the panel actually scored). | Inputs are committed (dated 2026-11-02); no regeneration substituted. |
| 2026-11-02 (momentum) | `shortlist_2026-11-02.*`, `funnel_2026-11-02.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-11-01.json` (generated 2026-11-01 08:36), reused under the protocol Phase 0 rule at ~17h old at run start, inside the <24h freshness window — the screen-of-record is committed under its own date. No same-day regeneration was substituted, per the 2026-10-18 precedent (a regeneration could drift the candidate set away from the screen the panel actually scored). | Inputs are committed (dated 2026-11-01); no regeneration substituted. |
| 2026-11-05 (dip) | `shortlist_2026-11-05.*`, `funnel_2026-11-05.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-11-04.json` (generated 2026-11-04 09:21:07), reused under the protocol Phase 0 1-day cache rule at ~16h old at run start, inside the <24h freshness window — the screen-of-record is committed under its own date, and the finals disclose the price-base caveat (batch-verified 2026-11-04 closes; the screen was built from partially refreshed cache after the full fetch.py refresh stalled on Yahoo 401 "Invalid Crumb" errors). No same-day regeneration was substituted, per the 2026-10-18 precedent (a regeneration could drift the candidate set away from the screen the panel actually scored). | Inputs are committed (dated 2026-11-04); no regeneration substituted. |
| 2026-11-07 (dip) | `shortlist_2026-11-07.*`, `funnel_2026-11-07.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-11-06.json` (generated 2026-11-06 09:24:26), reused under the protocol Phase 0 1-day cache rule at ~16h old at run start, inside the <24h freshness window — the screen-of-record is committed under its own date, and the finals disclose the price-base caveat (batch-verified Fri 6 Nov 2026 closes; the screen was built from partially refreshed cache). No same-day regeneration was substituted, per the 2026-10-18 precedent (a regeneration could drift the candidate set away from the screen the panel actually scored). | Inputs are committed (dated 2026-11-06); no regeneration substituted. |
| 2026-11-05 (earnings) | `shortlist_2026-11-05.*`, `funnel_2026-11-05.*` (post-panel regeneration, not the screen the panel scored) | The panel ran on `shortlist_2026-11-04.json`, reused under the protocol Phase 0 1-day cache rule — the screen-of-record is committed under its own date in `output/earnings/old/`, and the finals disclose the price-base caveat (batch-verified 2026-11-04 closes; the full fetch.py refresh stalled on Yahoo 401 "Invalid Crumb" errors). A same-day regeneration was run post-panel (09:39 PT) to satisfy the check_run date rule, writing `shortlist_2026-11-05.json`; it drops MNST at stage 1 on NaN profitability fields — a cache artifact from the stalled fetch, not a fundamental change — so the committed 2026-11-05 screen does not match the field the panel actually ranked (MNST #4). | Panel inputs committed (dated 2026-11-04, in old/); the 2026-11-05 screen is a post-panel regeneration, disclosed in the dossier and finals. |
| 2026-11-07 (earnings) | `shortlist_2026-11-07.*`, `funnel_2026-11-07.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-11-06.json` (generated 2026-11-06 09:24:33), reused under the protocol Phase 0 1-day cache rule at ~16h old at run start, inside the <24h freshness window — the screen-of-record is committed under its own date, and the finals disclose the price-base caveat (screen prices are the 2026-11-05 closes; the 2026-11-06 session is not reflected). No same-day regeneration was substituted, per the 2026-10-18 precedent (a regeneration could drift the candidate set away from the screen the panel actually scored). | Inputs are committed (dated 2026-11-06); no regeneration substituted. |
| 2026-11-07 (momentum) | `shortlist_2026-11-07.*`, `funnel_2026-11-07.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-11-06.json` (generated 2026-11-06 09:24:29), reused under the protocol Phase 0 1-day cache rule at ~16h old at run start, inside the <24h freshness window — the screen-of-record is committed under its own date, and the finals disclose the price-base caveat (screen prices are the 2026-11-05 closes — the last bar in the price cache, refreshed 2026-11-06 09:21; the 2026-11-06 session is not reflected). No same-day regeneration was substituted, per the 2026-10-18 precedent (a regeneration could drift the candidate set away from the screen the panel actually scored). | Inputs are committed (dated 2026-11-06); no regeneration substituted. |

| 2026-11-11 (dip) | `shortlist_2026-11-11.*`, `funnel_2026-11-11.*` (no screen dated for the run day) | The panel ran on `shortlist_2026-11-10.json` (generated 2026-11-10 16:41 UTC), reused under the protocol Phase 0 1-day cache rule at ~17h old at run start, inside the <24h freshness window — the screen-of-record is committed under its own date, and the finals disclose the price-base caveat (screen prices are Tue 10 Nov 2026 intraday snapshots). No same-day regeneration was substituted, per the 2026-10-18 precedent (a regeneration could drift the candidate set away from the screen the panel actually scored). | Inputs are committed (dated 2026-11-10); no regeneration substituted. |

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
