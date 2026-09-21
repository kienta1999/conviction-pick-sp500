# Independent Verification — EARNINGS panel, run date 2026-09-21

Verifier role: independent of the research and ballot agents. Every figure below was
re-checked against primary or reputable secondary sources; the panel's own files
(`shortlist.json`, `shortlist.csv`, `research_batch*.md`) were used only as the
claim set, never as evidence.

Verdict key: **CONFIRMED** / **CORRECTED** (right value given) / **CONTRADICTED** /
**NOT FOUND** / **ESTIMATED** (best available, unconfirmed).

---

## ★ LOAD-BEARING FINDING — GS reaction record is overstated

The screen's `beat_up_rate` of **0.875 for GS is wrong on a print-day basis**.
The Q1 2026 print (2026-04-13, BMO) shows **+2% in the screen, but the stock
FELL that day**:

- Finnhub daily candles: GS closed 2026-04-13 at **$890.79 vs $907.80 prior
  close = −1.87%** on the print day; the **+2.11%** move was the *next* session's
  recovery. The screen's `_reaction_at` heuristic takes max-abs of the two
  sessions and recorded the recovery day, not the print reaction.
- Cross-check: Reuters (Apr 13) — "shares fell 1.9%"; Quiver — "down 3.5%
  today"; BBN Times — "fell approximately 3–4.5% on the session" on the FICC
  miss ($4.01B vs ~$4.83B FactSet consensus).

Corrected GS record (print-day, BMO reporter → report-date session):

| Print | Screen | Verified print-day |
|---|---|---|
| Q2 2026 (2026-07-14) | +9% | **+9.00%** — CONFIRMED (Reuters: "last up 7.2%"; StockStory: +7.5% morning; close $1,140.00 vs $1,045.91 prior) |
| Q1 2026 (2026-04-13) | +2% | **−1.87%** — CORRECTED (wrong sign; screen captured the next-day rebound) |
| Q4 2025 (2026-01-15) | +5% | **+4.63%** — CONFIRMED (rounds to +5%) |
| Q3 2025 (2025-10-14) | −2% | **−2.04%** — CONFIRMED |

Consequences:
- **beat_up_rate: 0.875 (7/8) → 0.75 (6/8)** on the print-day basis. Two of the
  last four beats were sold (Q1'26 −1.87%, Q3'25 −2.04%).
- The doctrine's Plan-A disqualifier — *"Either of the last two prints was a
  beat that the stock fell on"* — is **TICKED for GS** (Q1'26: EPS $17.55 vs
  $16.47, +6.6% beat, stock fell). The tentative pick is Plan B (queued), so no
  plan flip, but the "best reward-to-beat profile in the batch" claim the panel
  relied on is materially weaker than stated. The Q1'26 episode the dossier
  describes ("even record numbers get sold when the mix disappoints") is in fact
  a *fall-on-beat*, not a +2% reward.
- Note the heuristic bias for the whole run: `reaction_avg_abs_move` is
  documented as an upper-ish bound, but the max-abs selection can also flip the
  *sign* of a reaction (as here), which corrupts `beat_up_rate`, not just
  magnitude. Verified the same ambiguity does not flip AME (see below).

---

## 1. Report date + BMO/AMC vs company IR (priority 1)

### GS — CONFIRMED 2026-10-13 BMO
Goldman Sachs' own press release "Conference Call Dates to Announce 4Q25 and
2026 Earnings Results" (NEW YORK, August 18, 2025):
"Third quarter 2026 – **Tuesday, October 13, 2026** … Our financial results will
be announced at approximately **7:30 am (ET)**" — i.e. **BMO**; call 9:30 am ET.
Source: https://www.goldmansachs.com/pressroom/press-releases/2025/conference-call-dates-to-announce-4q25-and-2026-earnings-results
The researcher's date claim is confirmed; this is the panel's load-bearing fact
and it holds.

### BLK — ESTIMATED, CONFLICTED (10/13 vs 10/14), no IR confirmation
- Zacks earnings calendar: **10/13/2026**, explicitly labeled "an estimated date
  of earnings release."
- MarketBeat: Q3 2026 **estimated Tuesday, October 13, 2026**, "based on past
  reporting schedules," conference call 7:30 AM ET (BMO on history).
- Investing.com: estimate 2026-10-13. Optionslam: estimated 2026-10-14.
- No Q3 2026 earnings-date announcement found on BlackRock's IR/press pages as
  of 2026-09-21 (the IR events page could not be fetched; no announcement
  surfaced in news search either).
- **Resolution of conflict (a):** the weight of estimates favors **10/13 BMO**,
  but it is an estimate, not a company confirmation. The 10/14 figure appears to
  be a naive same-weekday rollover of Q3 2025 (reported Tue 2025-10-14). The
  researcher's "ESTIMATED / CONFLICTED" status is upheld — date remains
  unconfirmed and the Plan-A disqualifier for an unconfirmed date stands.

### HWM — ESTIMATED ~2026-10-29 BMO, no IR announcement
- Zacks: **10/29/2026** estimated. MarketBeat: "Howmet Aerospace has not
  confirmed its next earnings publication date, but the company's estimated
  earnings date is **Thursday, October 29th, 2026** based off last year's report
  dates." No announcement on howmet.com/IR as of 2026-09-21.
- Howmet reports BMO on history (Q2'26 2026-08-06 BMO; Q1'26 2026-05-07 BMO;
  Q3'25 2025-10-30 BMO), and the prior-year Q3 (2025-10-30) was a Thursday —
  consistent with Thu 2026-10-29 BMO.
- **Resolution of conflict (b):** the cached screen date **2026-11-05 is stale**;
  the researcher's **~10/29 BMO estimate is the better-supported figure**, but it
  remains an estimate. Note: on the Aug 6, 2026 call CEO John Plant said "In
  November, at our Q3 earnings call" — loose calendar language, not a date
  announcement; it does not contradict a late-October call. Date stays
  unconfirmed → the Plan-A disqualifier stands.

---

## 2. GS Q3 2026 consensus (the bar)

- **EPS: $15.62 — CONFIRMED.** Zacks detailed estimates (crawled ~2026-09-15):
  current quarter (09/2026) consensus **$15.62**, 7 estimates, high $17.45 / low
  $12.69. Barchart earnings-estimates page shows the identical $15.62 (7 est).
- **Revenue: $17.04B — CORRECTED (researcher wrote "not found").** Zacks: current
  quarter revenue consensus **$17.04B**, 6 estimates, high $18.10B / low $15.59B,
  vs $15.18B a year ago (+12.2% est). Barchart/Zacks sharewise snippet confirms
  $17.04B.
- Dispersion note: aggregators disagree more than usual — TipRanks-derived
  preview cites ~$13.33; AInvest shows $16.14. Zacks/Barchart $15.62 is the
  standard reference and matches the dossier.
- As-of: consensus pages current as of ~mid-September 2026 (run date 2026-09-21).

## 3. GS last-quarter surprise and reaction

- **Q2 2026 surprise — CONFIRMED:** reported **$20.98 vs $14.47 consensus
  (+44.99%)**, revenue **$20.34B vs $16.22B**. Sources: Barchart earnings history
  (Reported $20.98 / Estimate $14.47 / Surprise +44.99%); Zacks (Jul 14, 2026)
  "reported second-quarter 2026 earnings per share of $20.98, which topped the
  Zacks Consensus Estimate of $14.47"; Reuters via LA Post: EPS $20.98 vs $14.48
  LSEG. Record quarter: highest net revenues ($20.3B) and highest EPS in firm
  history; ROE 23.5%.
- **Reaction — CORRECTED as detailed above:** the two most recent entries of
  `reaction_last4` are **+9.00% (Q2'26, confirmed)** and **−1.87% (Q1'26,
  corrected from screen's +2%)**. The screen's Q1 figure is the next-day
  recovery, not the print reaction.

## 4. GS next-quarter consensus (what the guide is judged against)

- **Q4 2026 (12/2026): EPS $15.43, revenue $16.71B** — Zacks detailed estimates,
  6 estimates each (EPS high $16.86 / low $12.79). Barchart shows the same $15.43
  (6 est). Year-ago Q4'25: $14.01. FY2026 consensus: EPS $68.89 / revenue
  $70.58B. GS is a non-guider; this is the number the market's forward bar
  sits at.
- Status: **CONFIRMED / found** (the dossier did not record a Q4 figure).

## 5. GS moat's central factual claim — CONFIRMED

Claim: premier investment-banking franchise, #1 M&A advisory share, not
AI-replaceable in origination/principal risk.
- **LSEG "United States Investment Banking Review 1H 2026":** "Goldman Sachs
  took the top spot in the any US involvement M&A financial advisor league table
  in the first half of 2026, followed by Morgan Stanley and JP Morgan."
- **GlobalData H1 2026 league table:** Goldman Sachs **#1 by deal value,
  advising on $597.4B** (Morgan Stanley $420B, JPMorgan $382.2B); advised on 61
  billion-dollar-plus deals incl. 20 mega deals >$10B; climbed from 3rd in H1
  2025.
- **Goldman's own Q2'26 call (CFO Denis Coleman):** "we extended our number one
  league table position for announced and completed M&A volume… advised on
  **$1.2 trillion** in announced deal volumes with a lead of approximately
  **$425 billion** ahead of our closest peer"; IB backlog at a five-year high.
The #1-share claim is confirmed by two independent league-table providers and
the company's own disclosure. (The dossier's "$150B lead" was the Q1 figure;
the H1 lead is ~$425B — the claim strengthened, not weakened.)

---

## 6. Flagged conflict (c): AME beat-up rate — screen is right, researcher is wrong

- **Screen (`shortlist.csv`/`shortlist.json`): beat_up_rate 0.875,
  n_beats_measured 8, reaction_last4 "+4%, +3%, +1%, +8%".**
- **Batch-2 researcher recorded "beat-up 0.333 (2 of 6)".** That figure appears
  nowhere in the screen output and matches no actual record — it is a researcher
  error.
- Reconciliation from actual prints (AME reports BMO; all 8 were EPS beats):
  - Q2'26 (2026-08-04): +4.22% print-day (Finnhub) — up
  - Q1'26 (2026-04-30): +3.35% print-day — up
  - Q4'25 (2026-02-03): +0.53% print-day — up
  - Q3'25 (2025-10-30): +7.67% print-day — up
  - Q1'25 (2025-05-01): beat ($1.75 vs $1.69); positive post-earnings action
    (AInvest: "generally positive"; Simply Wall St: shares +2.3% in the week) — up
  - Q4'24 (2025-02-04): beat ($1.87 vs $1.84); StockStory: "stock is up 3.2%
    since reporting" — up
  - Q3'24 (2024-10-31): beat ($1.66 vs $1.62); Barchart: "stock prices soared
    over 8.5% after the release" — up
  - Q2'24 (2024-08-01): beat ($1.66 vs $1.64, +1.22%) but revenue miss + soft
    Q3 guide; StockStory: "fell 9.3% in the afternoon session"; Barchart:
    "plummeted 8.3% after the release" — **down**
- **Verdict: 7 of 8 beats rewarded → 0.875 CONFIRMED.** The screen's figure is
  correct; the researcher's 0.333 is contradicted. AME's last-4 print-day moves
  from Finnhub (+4.22%, +3.35%, +0.53%, +7.67%) also confirm the screen's
  "+4%, +3%, +1%, +8%" — no sign-flip issue for AME.

---

## Summary of verdicts

| # | Claim | Verdict |
|---|---|---|
| 1a | GS date 2026-10-13 BMO | **CONFIRMED** — Goldman IR press release, 7:30 am ET |
| 1b | BLK date | **ESTIMATED, CONFLICTED** — 10/13 (Zacks/MarketBeat/Investing.com) vs 10/14 (optionslam); no BlackRock IR announcement; weight of estimates favors 10/13 BMO |
| 1c | HWM date | **ESTIMATED ~10/29 BMO** — Zacks/MarketBeat estimate; no Howmet IR announcement; cached 11/05 stale |
| 2 | GS Q3'26 consensus $15.62 EPS | **CONFIRMED** (Zacks/Barchart); revenue **$17.04B found** (researcher: not found) |
| 3a | GS Q2'26 surprise +45% | **CONFIRMED** ($20.98 vs $14.47) |
| 3b | GS Q2'26 reaction +9% | **CONFIRMED** (+9.00% print-day) |
| 3c | GS Q1'26 reaction +2% | **CORRECTED → −1.87%** (screen captured next-day rebound; print day fell per Reuters/Finnhub) |
| 4 | GS Q4'26 consensus | **$15.43 EPS / $16.71B revenue** (Zacks; not in dossier) |
| 5 | GS #1 M&A franchise moat | **CONFIRMED** (LSEG, GlobalData, company: #1, $1.2T advised H1'26, ~$425B lead) |
| 6c | AME beat_up_rate | **0.875 CONFIRMED**; researcher's 0.333 **CONTRADICTED** |

## Impact on the pick

- The load-bearing date for the tentative single pick (GS, 2026-10-13 BMO) is
  **company-confirmed** — the trade's calendar premise holds.
- **But the central doctrine evidence for GS is overstated:** beat_up_rate is
  0.75, not 0.875, on print-day reactions; two of the last four beats were sold
  (−1.87%, −2.04%); and the skill's own Plan-A disqualifier ("either of the
  last two prints was a beat that the stock fell on") is **ticked** for GS.
  The pick is Plan B (queued), so the plan stands, but any writeup that leans on
  GS's "best reward-to-beat profile" must be rewritten against the corrected
  record.
- BLK and HWM remain watchlist-only: dates unconfirmed by either company's IR.
- AME's screen record is vindicated; the batch-2 researcher's 0.333 should be
  disregarded wherever it propagated (ballots/final ranking should use 0.875).

*Methods: Goldman Sachs IR press release (fetched); Zacks/Barchart detailed
estimates (crawled ~Sep 2026); Finnhub daily candles via runtime finance data
(GS 2025-09-08→2026-09-18; AME same window) cross-checked against Reuters, Zacks,
Barchart, StockStory, Simply Wall St, AInvest; LSEG and GlobalData H1 2026 M&A
league tables; MarketBeat/Zacks/Investing.com/optionslam earnings calendars for
BLK and HWM. BlackRock IR events page could not be fetched; no IR announcement
found for either BLK or HWM in news search.*
