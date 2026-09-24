# Research dossier — earnings mode — 2026-09-24

This run produced no pick (0 actionable names — see triage.md). This dossier is the
run's research record: the screened field, the actionable-set determination, and the
prior-pick bookkeeping research that this run's close row rests on.

## The field (fresh screen, `shortlist_2026-09-24.json`, built 2026-09-24 08:26:19 UTC)

50 candidates in the 45-day window; nearest print is PEP on 2026-10-08 (dte 14). Full
funnel and watchlist table in `output/earnings/parts/2026-09-24/triage.md`.

Notable: PAYX and CTAS dropped out of the field (both reported 2026-09-23); nine new
names entered (KO, CSX, ADP, AMGN, EBAY, CAT, CBOE, CPAY, APP) as Yahoo's earnings
calendar rolled.

## Prior-pick bookkeeping — the 9/22 PAYX Plan B outcome

The 2026-09-22 run published a Plan B pick on PAYX (writeup `final_pick_2026-09-22.md`)
but recorded no ledger row. This run recorded the pick row and the mandatory close row.
Trigger evaluation against the 2026-09-23 BMO print (FQ1 FY27, quarter ended Aug 31, 2026):

- **Trigger 1 — EPS AND revenue beat.** EPS $1.34 vs $1.32–1.33 consensus (18 analysts at
  $1.32) → BEAT (+1.5%). Revenue $1.63B (+5.9% YoY) vs $1.63B consensus → IN-LINE, not a
  beat. Sources: MarketBeat PAYX earnings summary; Seeking Alpha headline via TradingView
  ("Non-GAAP EPS of $1.34 beats by $0.02, revenue of $1.63B in-line", 9/23 8:31 AM).
- **Trigger 2 — guide raised or reaffirmed ABOVE consensus.** FY27 guide reaffirmed:
  revenue growth 5–6%, adjusted EPS growth 7–9% (implies $5.90–6.01 / $6.84–6.90B,
  midpoint $5.96/$6.87B — in line with consensus, not above). Segment PEO/insurance
  growth raised to 7–8% from 6–7%, and funds-held-for-clients interest raised to
  $200–210M, but the headline FY27 EPS/revenue guide was NOT raised. Also: total
  expenses $1.01B exceeded the Visible Alpha consensus of $996.3M; adjusted EBITDA
  $738.3M trailed the $740.1M S&P CapIQ consensus. Source: Seeking Alpha via TradingView
  (9/23); tickerreport/thestockobserver summaries.
- **Trigger 3 — positive first session.** The 9/23 session closed at **$104.49, −8.77%**
  (−$10.04). MarketBeat data 9/23. Extended hours +0.91% to $105.44 — still far below
  the prior close.

**Verdict: trigger did NOT fire (all three required; only 1 of 3 held — and the revenue
half of trigger 1 failed).** No trade was taken. Close row: `exit_reason=event_exit`,
`exit_price = price_at_pick = 116.14`, `exit_date = 2026-09-23`. This is the
trigger-never-fired outcome the design expects, not a failure of the run.

## What stays open

- 2026-09-17 `earnings,rank10,8` PAYX row (ranked-mode entry, next_earnings 2026-09-23)
  is past its print with no close row. Ranked-mode rows carry no event plan; flagged
  for the coordinator, not closed by this run.
