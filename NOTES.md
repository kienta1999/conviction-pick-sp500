# Session breadcrumbs

Claude Code sessions behind each artifact (resume with `claude --resume <id>`):

- First session: `c01dbd4f-0dd7-47d1-b0ff-9a43214fae0f`
- HWM pick (momentum single, 2026-06-21): `8d5c4fe5-2e66-49af-881e-f01fce67623e`
- Pick 10 stocks (momentum rank10, 2026-06-23): `4baf5057-d47b-4050-8ab1-772d56ea55d6`
- Buy dip (skill build): `000cc485-9eeb-4751-9424-6db1e65ab0ee`
- Buy dip actual run (dip rank10 + SPGI pick, 2026-06-29): `1cde50b6-c2f1-4565-8352-6a824264f2c8`
- Fable session: claude --resume 52eab3f4-f5cf-4466-9856-6dee096ace57
- Built the real-money guardrails — exit rules + realized scorecard (WS-6), sizing policy (WS-7), earnings-quality value-trap flags (WS-1), and bear/base/bull + EV-or-pass writeup discipline (WS-3): claude --resume bcc1bcb1-4d1d-492b-b195-3c3922350919
- Buy dip run again after above: claude --resume c01c08be-d2fa-4aad-96f0-4613796cb4b1
- Build UI: claude --resume 16f43385-f547-411b-9582-6f37c04e49ac
- Buy dip TO BE CONTINUE: claude --resume 96d0345c-421b-4610-a4c7-c60362b86f82
- Dip run 2026-08-03 (BR single pick + rank10) — also hardened the shared protocol to SEQUENTIAL
  subagent dispatch with mandatory per-agent `WRITE_TO` files after two runs were killed mid-fan-out
  by the monthly spend limit: claude --resume b10c4a22-aca2-4a03-9140-e1d3e59318c3
- Momentum run 2026-08-04 (AVGO single pick + rank10) — the panel died at agent B on the monthly spend
  limit; the orchestrator began filling the missing lenses in its own context and the owner stopped it,
  so dispatch rule 4 was rewritten to **HALT instead of self-substitute** (no orchestrator-authored
  ballots / dossier sections / verification, never publish off a partial panel, resume with real agents
  via rule 3). B/C/D + verifier were then re-run properly. Also chased the `forwardPE` oddity to its
  actual cause: `screen.py` does no valuation arithmetic and never ranks on it (not in the composite);
  Yahoo's value was (a) computed against a price up to 3 days staler than the funnel's — **fixed**, now
  rescaled onto `price` — and (b) referenced to a fiscal year that varies by company (GE/HWM a year out,
  CF *nearer* than the current year), which is **not fixable** from the info dict, so the field is
  indicative only: claude --resume 4b22a9e7-275d-487f-9c1d-f71b9c41da42
- **Built the third mode, `/stock-pick-earnings` (2026-08-15)** — an event trade into a scheduled
  print, no research run yet. `claude --resume da63e60e-23e0-469d-840b-3610449ed682`

  **What shipped.** `--mode earnings`: no SMA gate (the catalyst is the event, not the trend), no
  stage-8 niche-leadership rule (replaced by a $20B market-cap floor at 5b), no US-domicile gate
  (domicile shapes a multi-year hold, not a print — readmits LIN/STX/ETN/CB/MDT/ACN/TT/NXPI…), plus
  a new track-record gate (5c: <2 consensus misses in 4 quarters) and a beat-streak composite.
  `fetch.py` grew a fifth cache — Yahoo's earnings calendar + 12 quarters of estimate/reported/
  surprise on a 1-day TTL. Stage 6's sector median is computed over the **full universe** in this
  mode (its stage-5 pool is "whoever reports this week", so a survivor-relative median would be
  built from 2-3 arbitrary names). Horizon per the owner: **ride the print and sell immediately** —
  writeup leads with an event plan and a pre-written exit rule, 12-18mo scenarios demote to the
  fallback, `kind=close` with `exit_reason=event_exit` mandatory within days. POLICY.md §1.5: 2%
  cap, halved again, one open earnings position at a time.

  **State to come back to.** `output/earnings/shortlist.json` currently holds the **30-day** run
  (9 names), not the 7-day default — regenerate with `screen.py --mode earnings` for the default.
  Field sizes on 2026-08-15: 1 name at 7d (ADI), 6 at 14d, 9 at 30d. Full findings, including the
  measured case for/against expanding beyond the S&P 500 (+1 at 7d / +4 at 14d, blocked on the
  GICS-taxonomy mismatch) are written up in the README's earnings section.

  **Open, decided against for now.** (a) The 6b earnings-quality gate drops **NVDA and AVGO** —
  two of the three biggest prints in the 30-day window, both on inventory outrunning revenue.
  Verified this is *not* a hypergrowth artifact (MU at +145% revenue has an accrual ratio of
  −0.009); the flag is picking up something specific. `--no-eq-gate` readmits them with the flags
  still visible for the panel to adjudicate. (b) Universe expansion — see README. (c) Did **not**
  retune any threshold, per the TODO's rule that gate tuning is unfalsifiable until the
  point-in-time backtest exists.

  **Never run.** No earnings pick has been made, no ledger row written. The first real run is the
  next step.
