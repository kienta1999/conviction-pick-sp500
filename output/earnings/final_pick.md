# Final pick — stock-pick-earnings 2026-09-17 (full panel)

- **Pick:** FSLR (First Solar)
- **Plan:** **B (queued)** — no position into the print; enter only after the number on the trigger below
- **Price at pick:** $201.16 (screen cache 2026-09-18)
- **Report date:** ~2026-10-29, vendor-estimated, BMO/AMC unconfirmed (verifier: no company IR announcement found)

## Why this one

The panel's single-pick tally: FSLR 3 (B's nomination + D's runner-up) vs REGN 2, MS 2, CTAS 2 — plus two of the four #1 ranked votes and a unanimous top-4 Borda presence (29 pts, 4/4 appearances). It is the field's one genuine "bar too low" mis-model (D): Q3 consensus was **cut from $5.29 to $4.56** after analysts overshot Q2, the stock sits **37% below its high at 8.7x forward** (PEG 0.45), FY guidance was **reaffirmed** (shipments bar ~3.9 GW, adjusted EBITDA $625–775M, backlog ≥45 GW), and it owns the **only perfect beat→up record (1.00) in the 48-name screen**. B — the setup skeptic, the lens built to kill Plan A trades — nominated it as the one name where pre-print risk is arguably compensated.

## Why Plan B, not Plan A

Gate A1 box 4: the report date is **not confirmed on the company's own IR page** (verifier 2026-09-18: vendor-estimated only). Any single box ticked means no Plan A trade. The entry is therefore queued: wait for the number, then buy the confirmed beat-and-raise plus a positive first session.

## Event plan

**Trigger (all three required, evaluated on the ~10/29 print):**
1. Q3 beat vs $4.56 consensus (EPS) with shipments ≥3.9 GW and clean U.S. mix
2. FY2026 guidance reaffirmed or raised — volume AND EBITDA; **any cut to volume or EBITDA guidance is an automatic pass**
3. Positive first session (no gap-down on the headline)

**If triggered:** enter post-print; hold through the drift horizon (~30 trading sessions, ~mid-December 2026); record `event_exit` then. No stop on the event — the bear target below is the 12–18-month fallback, not the event stop.

**Gap-down treatment:** if it gaps down >10% on the print *without* a guide cut, treat as a Plan B entry review (fallback quality: net-cash, domestic backlog, policy-proof chain); if the guide was cut, pass — the thesis is broken.

**No-trigger Plan B:** if the print doesn't clear the trigger, no trade; record a `kind=close`, `exit_reason=event_exit` row marking no-trigger.

## Pre-registered event prediction

- `event_pred_dir`: **up**
- `event_pred_move`: **+7.5** (≈ reaction_avg_abs_move 7.47%)
- `event_implied_move`: **not found** (no options-implied move sourced for any name in this run)

## Targets (12–18 month fallback frame)

- Base target: **$273** (~+36%, analyst mean; screen analyst_upside 35.7%)
- Bull target: **$310** (~+54%, prior-high zone on reaffirmed guide + policy clarity)
- Bear target: **$150** (~−25%, fallback — guide/policy shock scenario; **not** an event stop)
- P: base 0.50 / bull 0.25 / bear 0.25 → EV ≈ $251.50

## Fallback if the print disappoints

Would I hold it 12–18 months? Yes — conditionally. Net-cash balance sheet, ≥45 GW contracted backlog, and the only domestic thin-film chain at scale give it a policy moat no Chinese import can route around near-term. The disaster case is a volume/EBITDA guide cut or an adverse subsidy ruling — either breaks the thesis and the position is a pass, not a hold.

## Top risk

Trade-policy headline in the final weeks before the print, or a backlog deferral that reads as demand softness. The −14% print in the last4 proves the gap-down is real even with a perfect beat→up record.

## Dissent

- A nominated REGN (Plan B): the Sanofi "meaningful step-up" catalyst is confirmed verbatim and real, but the Q1'26 beat-sold-6.5% precedent plus the unresolved 10/27-vs-10/28 date split keep it behind FSLR's lowered bar.
- C nominated CTAS (Plan B): the best 18-month fallback in the field (moat 9), but consensus at the top of the guide at 40x P/E makes the 9/23 print a sell-the-news trap — it's a post-print buy, and 42 days of optionality favor FSLR's cleaner trigger.
- D nominated NO TRADE on the actionable names (7/10 conviction holding PAYX/CTAS through 9/23 is negative-EV) — agreed, which is why nothing actionable-now is the pick.

**Return date:** come back **2026-10-30** (day after the ~10/29 print) to score the trigger and record the entry or the no-trigger close. If entered, return ~**2026-12-11** (~30 trading sessions later) to record `event_exit`.

Conviction: 7/10.
