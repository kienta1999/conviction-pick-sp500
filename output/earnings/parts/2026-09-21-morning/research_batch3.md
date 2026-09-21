# EARNINGS-mode research — batch 3/3
**Run date:** 2026-09-21 (PDT). **Tickers:** HWM, BNY, PEP, BAC, FOXA.
**Skill:** `.claude/skills/stock-pick-earnings/SKILL.md` (read 2026-09-21, obeyed).
**Screen baseline:** `output/earnings/shortlist.json` (read 2026-09-21). Screen figures are cited as baseline
throughout; where researched figures disagree they are flagged and the researched figure is preferred.
"not found" = could not verify; never invented.

## Cross-ticker notes
- **Date status:** PEP **CONFIRMED 2026-10-08 BMO** (PepsiCo IR); BAC **CONFIRMED 2026-10-14 BMO**
  (BofA IR calendar). HWM **ESTIMATED ~2026-10-29 BMO** (calendars; cached 2026-11-05 unconfirmed by
  company IR). BNY **ESTIMATED ~2026-10-15 BMO** (no primary IR announcement found). FOXA **ESTIMATED
  ~2026-10-28/29 BMO** (calendars conflict). Unconfirmed dates = automatic Plan B.
- **Actionable window:** doctrine treats events within ~10 calendar days as actionable. On 2026-09-21
  **none of the five are actionable** (nearest is PEP at 17 days); all are watchlist until the window.
- **Options-implied vs realized:** HWM — OptionsAI historical page (captured 2026-07) showed ~7.3–8.0%
  expected move ahead of the Aug 6 print, average realized 1D move **5.43%** (screen: 5.86% absolute);
  current-October implied not verified. PEP — OptionsAI average realized **2.77%** 1D (screen: 4.18%);
  TipRanks had ±4.54% implied for the Oct 2025 print; current implied not captured. BAC — OptionsAI
  average realized **2.51%** (screen: 2.52%); a January-2026 preview showed ±3.2% expected for the Q4 2025
  print; current implied not verified. BNY and FOXA: ticker-specific implied move **not found**.
  (Sources: tools.optionsai.com per-ticker earnings pages; tipranks.com; asktraders.com.)
- **HWM vendor disagreement (flagged):** screen reaction_last4 for HWM is `-3%, +6%, +6%, +2%`. OptionsAI's
  per-event table shows the Q3 2025 (2025-10-30) print-day move as **-0.84%**, not +2%. Screen numbers are
  used as baseline per the no-replace rule, but that Q3 2025 reaction is contested (definition/window
  difference) — do not lean on it for Plan A.
- **Bank EQ flags:** BNY `LOW_CASH_CONVERSION` and BAC/FOXA `RECEIVABLES_OUTRUN` are largely screen-model
  artifacts. BNY's operating cash flow is dominated by custody-bank settlement balances and securities
  financing, not industrial working capital. BAC's "receivables" divergence reflects loan/trading-asset
  classification. FOXA's divergence may be ad-billing seasonality around event quarters. For banks, EQ
  analysis should weight provisions, CET1, and reserve methodology instead.

---

# HWM — Howmet Aerospace Inc.

## 1. Date: ESTIMATED ~2026-10-29 BMO (Q3 2026)
No Q3 2026 company announcement found on howmet.com or IR. Zacks/MarketBeat estimate **2026-10-29**
(likely BMO on history); the cached shortlist date 2026-11-05 is unconfirmed. **MOVED/unconfirmed →
automatic Plan B.**
Source: https://www.marketbeat.com/stocks/NYSE/HWM/earnings/

## 2. Consensus bar & revisions
- EPS consensus Q3 2026: **$1.36 avg** (4 analysts, $1.35–$1.38) — sits **at the top** of the company's own
  guide ($1.34–$1.36). Q4 2026 EPS $1.41 (5 est). FY26 EPS $5.33 ($5.29–$5.40); FY27 $6.22.
  Source: barchart.com earnings-estimates (page crawled ~2026-09-02).
- Revenue Q3 2026: ~$2.58B per earlier public estimates (single-source; exact figure **not found** on the
  Barchart estimate table).
- 30-day revision trend: **not found**.
- Company FY26 guide (raised 2026-08-06): EPS $5.23–$5.31, revenue $10.00–$10.10B, EBITDA $3.21–$3.25B,
  FCF ~$1.9B — consensus FY26 ($5.33) sits **above** the company range top.

## 3. Last four prints (reported vs consensus, guide outcome, reaction)
| Print | Date | Adj EPS | Revenue | Guide outcome | Reaction |
|---|---|---|---|---|---|
| Q2 2026 | 2026-08-06 BMO | $1.33 vs ~$1.24–1.25 (+6–7%) | $2.547B vs ~$2.41–2.43B (+24.1%) | FY26 **raised** (rev $10.00–10.10B, EBITDA $3.21–3.25B, EPS $5.23–5.31) | **-0.58%** print-day / **-2.71%** next session (Finnhub closes); screen -3% — beat, sold |
| Q1 2026 | 2026-05-07 BMO | $1.22 vs $1.11 (+9.9%) | $2.313B vs $2.24B (+19%) | FY26 guide increased (rev ~$9.65B, EPS ~$4.94 per call summary) | **+6.3%** (Barchart); screen +6% |
| Q4 2025 | 2026-02-12 | $1.05 vs $0.97 (+8.3%) | $2.17B, beat (+14.6%); gas turbines +32%, defense +20% | Initial FY26 guide: Q1 rev $2.22–2.24B, EPS $1.09–1.11; FY EPS $4.35–4.55 | **+6.0%** (OptionsAI); screen +6% |
| Q3 2025 | 2025-10-30 BMO | $0.95 vs $0.91 (+4.4%) | $2.09B vs $2.04–2.05B (+14%) | FY25 **raised** on all metrics (rev $8.175–8.195B, EPS $3.66–3.68); initial FY26 rev ~$9B | Screen **+2%**, but OptionsAI print-day shows **-0.84%** — contested, flagged above |

Serial beater (screen 4/4, avg surprise 7.55%, improving +1.92), but the two most recent raise-and-beat
prints got opposite treatment: Q1 +6.3%, Q2 −3%. Screen: 75% positive, avg +3.59%, absolute 5.86%.

## 4. Revenue/margin trend (4 quarters, verified)
| Quarter | Revenue | Adj op margin | Adj EBITDA margin |
|---|---|---|---|
| Q3 2025 | $2.09B (+14% YoY) | 25.9% (+~310 bps) | 29.4% |
| Q4 2025 | $2.17B (+14.6%) | n/a | 30.1% |
| Q1 2026 | $2.313B (+19%) | 28.8% (+350 bps) | 32.0% |
| Q2 2026 | $2.547B (+24.1%) | 27.9% (+250 bps) | 32.1% |
Accelerating growth and expanding margins; screen latest revenue growth +24.06%, acceleration +10.44 pp.
Sources: company earnings releases (quartr.com mirrors), zacks.com.

## 5. Eight-quarter guide history
| Quarter | Guide action |
|---|---|
| Q3 2025 (2025-10-30) | FY25 raised on all metrics; initial FY26 revenue ~$9B (+~10%); Q4 2025 guide rev $2.09–2.11B, EPS $0.94–0.96 |
| Q4 2025 (2026-02-12) | Initial FY26 guide: EPS $4.35–4.55; Q1 2026 guide rev $2.22–2.24B, EPS $1.09–1.11 |
| Q1 2026 (2026-05-07) | FY26 guide increased (~$9.65B rev, ~$4.94 EPS per call summary) |
| Q2 2026 (2026-08-06) | FY26 **raised again**: rev $10.00–10.10B, EBITDA $3.21–3.25B, EPS $5.23–5.31, FCF ~$1.9B; Q3 guide rev ~$2.58B, EPS $1.34–1.36 |
| Q2 2025 and earlier | **not found** |
Pattern: guide, beat, raise, repeat — but the bar is now high: consensus sits above the company's own
FY26 EPS range top and at the top of Q3 EPS guidance.

## 6. Moat / AI irreplaceability
Certification-gated engine components, proprietary metallurgy/IP, multi-year OEM qualification cycles,
capacity intensity, and spares exposure (~21% of revenue vs 17% in 2024). Gas-turbine business (~$1B,
expected to double in 3–5 years on data-center power demand) adds a second growth engine. AI cannot
replace certified mission-critical hardware — **high irreplaceability**.

## 7. Print-specific risks
- Consensus Q3 EPS ($1.36) at the **top** of company guide ($1.34–1.36): beat-or-meet must clear the
  company's own ceiling, not just the number.
- Last beat-and-raise was **sold** (−3%): multiple compression risk at ~35.6x forward P/E (baseline).
- Stock −18.98% in 21 sessions / −15.46% in 1 month (Finnhub, as-of 2026-09-21) despite beats —
  market is de-risking aerospace multiples; another raise may not be rewarded.
- 2026-09-02: unusually heavy put volume (8,120 puts, +184% vs average) — hedging demand building
  (tickerreport.com).
- Next-quarter/full-year guide risk is the real event: Q2 2026 raised FY26 twice in a row; a third raise
  is largely expected.

## 8. Scores (0–10)
- **Beat likelihood: 7** — serial beater with accelerating revenue, but consensus already at guide top.
- **Guide risk: 6** — medium; raised twice consecutively, FY26 consensus above company range; the guide
  is the event.
- **Priced-in: 5** — −19% 21-session selloff has de-risked some expectations, but 35.6x forward P/E
  leaves little room for a mere meet-and-raise.

## 9. Verdict
A serial beat-and-raise industrial into an unconfirmed date, with consensus parked at the top of its own
guide and the last raise sold off — **Plan B**; the trade is post-print, after the guide clears.

## 10. Plan A/B
**Plan B.** Disqualifiers for Plan A: (a) date unconfirmed by company IR (ESTIMATED, possibly moved);
(b) last print was a beat-and-raise that fell −3%; (c) no verified current options-implied move to compare
against the ~5.4–5.9% realized range.

---
# BNY — Bank of New York Mellon Corp.

## 1. Date: ESTIMATED ~2026-10-15 BMO (Q3 2026)
TipRanks expects before-open on 2026-10-15 (prior schedule). **No primary company IR announcement found** →
ESTIMATED, automatic Plan B.
Source: https://www.ainvest.com/stocks/NYSE-BNY/financials/earnings/

## 2. Consensus bar & revisions
- EPS consensus Q3 2026: **~$2.25** (TipRanks; AInvest $2.2537, +19.88% YoY).
- Revenue consensus: **$5.53B** (+9.04% YoY, AInvest).
- FY26 EPS consensus: **~$9.26** (analysts, per americanbankingnews.com 2026-09-18/15).
- Q4 2026 consensus: **not found**. 30-day revision trend: **not found**.

## 3. Last four prints (reported vs consensus, guide outcome, reaction)
| Print | Date | Adj EPS | Revenue | Guide outcome | Reaction |
|---|---|---|---|---|---|
| Q2 2026 | 2026-07-15 BMO | $2.45–2.46 vs $2.16–2.20 (+12–14%) | $5.698B vs ~$5.35B (+13%); pre-tax margin 39.8%; NII +20% | FY26 **raised**: revenue growth 10–11%, NII +12–13%, expenses +6–7%, ~400 bps operating leverage | **+5.08%** (Finnhub $154.50→$162.35); screen +5% |
| Q1 2026 | 2026-04-16 BMO | $2.25 vs $1.93–1.94 (+16–17%) | $5.409B vs ~$5.17–5.19B (+13%) | No explicit guide change found | **~+2.2%** |
| Q4 2025 | 2026-01-13 BMO | $2.08 vs $1.96–1.99 (+5–6%) | $5.18B vs $5.11–5.15B (+7%) | **Medium-term targets raised** (pre-tax margin 38%, ROTCE 28%); 2026 revenue guide **+5%** (deceleration → market caution) | **+1.4%** day (watchlistnews); screen +2% — beat with a cautious forward message |
| Q3 2025 | 2025-10-16 BMO | $1.91 vs $1.76–1.77 (+8.5%) | $5.081B vs $4.96–4.97B (+9.3%); op margin 37.7% | No explicit guide change found | **−2%+** (closed down >2%, barchart); screen −2% — beat, sold on sustainability worries |

Screen: 4/4 beats, avg surprise 10.06% (trend +7.12), 87.5% positive reactions, avg +2.51%, absolute
3.01%, worst −2.03%. Note the Q3 2025 template: big beat sold on "sustainability of growth drivers."

## 4. Revenue/margin trend (4 quarters, verified)
| Quarter | Revenue | Pre-tax margin |
|---|---|---|
| Q3 2025 | $5.081B (+9.3%) | ~37–38% |
| Q4 2025 | $5.18B (+7%) | 36% (ROTCE 26.6%) |
| Q1 2026 | $5.409B (+13%) | ~37–38% |
| Q2 2026 | $5.698B (+13%) | 39.8% |
AUC/A $57.8T → $59.3T; AUM ~$2.1–2.2T; CET1 11.9%. Eight consecutive quarters of positive operating
leverage through Q4 2025. Sources: company releases (quartr.com / bny.com), fool.com transcript.

## 5. Eight-quarter guide history
| Quarter | Guide action |
|---|---|
| Q4 2025 (2026-01-13) | Medium-term targets **raised** (pre-tax margin 38%, ROTCE 28%); 2026 revenue growth guided **~5%** — a deceleration vs 8% in 2025; stock slipped on the slowdown framing |
| Q1 2026 (2026-04-16) | **not found** (no explicit guide change located) |
| Q2 2026 (2026-07-15) | FY26 guidance **raised**: revenue growth 10–11% (from ~5%), NII +12–13%, expenses +6–7% |
| Q3 2025 (2025-10-16) | **not found** |
| Earlier | **not found** |
BNY is a soft guider (revenue/NII/expense growth rates, medium-term margin targets) — the forward
message, not the beat, moves the stock, in both directions (Q4 2025 caution → slip; Q2 2026 raise → +5%).

## 6. Moat / AI irreplaceability
World's largest custodian ($59.3T AUC/A), clearing infrastructure, regulatory charter, network and
switching costs for institutional clients. AI (>100 deployed solutions per management, Google Cloud
Eliza partnership) is an efficiency/cost-structure tool — it does not replace trusted market plumbing.
**High irreplaceability.**

## 7. Print-specific risks
- The bar was just **raised in Q2**: FY26 revenue growth 10–11% and NII +12–13% are now the bogey; a
  mere in-line Q3 reads as a guide cut risk.
- +33.8% in 6 months (Finnhub, as-of 2026-09-21), 6.7% below the 52-week high — expectations elevated.
- Q3 2025 precedent: +8.5% EPS beat **fell 2%** on sustainability questions — the same framing risk
  exists now after two raises.
- NII sensitivity to Fed policy; AUM net outflows (Q4 2025: −$3B) offset by market appreciation.
- Screen `LOW_CASH_CONVERSION` (CFO/NI 0.554): custody-bank cash-flow classification artifact, not an
  industrial EQ red flag.

## 8. Scores (0–10)
- **Beat likelihood: 7** — 4/4 beats, avg surprise 10%, improving trend.
- **Guide risk: 7** — medium-to-high; the print matters less than whether the raised FY26 outlook holds.
- **Priced-in: 7** — strong run, bar raised in July, and the last big beat of this type was sold.

## 9. Verdict
A quality compounder whose beat record is intact but whose bar was just raised — the setup mirrors
Q3 2025 (beat, sold on guide), so **Plan B**; only a decisive guide hold/raise with a selloff is
actionable post-print.

## 10. Plan A/B
**Plan B.** Disqualifiers: (a) date unconfirmed (ESTIMATED, no IR announcement); (b) ticker-specific
options-implied move **not found**, so implied > realized (3.01%) cannot be verified; (c) raised-bar
guide risk after the Q2 FY26 increase.

---

# PEP — PepsiCo, Inc.

## 1. Date: CONFIRMED 2026-10-08 BMO (Q3 2026)
PepsiCo IR announcement dated **2026-08-25**: results materials at 6:00 a.m. EDT, Q&A at 8:15 a.m.
Source: https://www.pepsico.com/newsroom/press-releases/2026/pepsico-announces-timing-and-availability-of-third-quarter-2026-financial-results

## 2. Consensus bar & revisions
- EPS consensus Q3 2026: **$2.30** (Zacks, as of 2026-09-04); MarketBeat's thin table shows $2.32
  (single estimate) — **vendor spread flagged**.
- Revenue consensus: **$24.92B** (Zacks 2026-09-04). Zacks consensus unchanged over prior 30 days
  (as of 2026-09-18).
- Q4 2026 EPS $2.43, FY26 $8.56–8.57, FY27 $8.98 (Zacks via americanbankingnews, Jul 2026).
- Company FY26 guide: core EPS $8.55–8.71, revenue $97.7–99.6B (reaffirmed 2026-07-09; "tracking toward
  the low end").
- Note: Zacks **cut** Q3 2026 EPS $2.43 → $2.32 in July 2026 — bar was lowered into the print.

## 3. Last four prints (reported vs consensus, guide outcome, reaction)
| Print | Date | Core EPS | Revenue | Guide outcome | Reaction |
|---|---|---|---|---|---|
| Q2 2026 | 2026-07-09 BMO | $2.20 (vendors split: $2.19 beat / $2.20 in-line / $2.23 miss) | $24.181B vs ~$23.87–23.95B (+6.4%); organic +2.4%; core op margin 16.8% (−40 bps) | FY26 **reaffirmed**, "tracking toward the **low end**" | **−3.3%** (OptionsAI −3.26%); screen −3% — beat/reaffirm sold |
| Q1 2026 | 2026-04-16 BMO | $1.61 vs $1.55 (+3.9%) | $19.443B vs $18.94B (+8.5%); organic +2.6%; op margin 16.5% vs 15.8% | FY26 reaffirmed | Premarket +0.8%; full-session **not found**; screen +2% |
| Q4 2025 | 2026-02-03 BMO | $2.26 vs $2.24 (+0.9%) | $29.34B vs $28.9–28.97B (+5.6%); organic +2.1% | FY26 **affirmed** (Dec initial: organic +2–4%, core EPS $8.55–8.71); dividend +4% to $5.92; $10B buyback through 2030 | **+4.9%** (OptionsAI +4.93%); screen +5% |
| Q3 2025 | 2025-10-09 BMO | $2.29 vs $2.26–2.27 (+0.9%) | $23.94B vs $23.83–23.85B (+2.6%); organic **+1.3%, missed ~2% target** | FY25 reaffirmed (low-single-digit organic, ~flat core cc EPS) | **+4.2%** (OptionsAI +4.23%); screen +4% |

Screen: 3 beats / 1 miss, avg surprise 1.43%, 83.3% positive on 6 measured beats, avg +1.02%,
absolute 4.18%, worst −4.89%. Beats are tiny; the market punishes guide conservatism (Q2 2026).

## 4. Revenue/margin trend (4 quarters, verified)
| Quarter | Revenue | Organic | Core op margin |
|---|---|---|---|
| Q3 2025 | $23.94B (+2.6%) | +1.3% (miss) | n/a |
| Q4 2025 | $29.34B (+5.6%) | +2.1% | margin expansion, "strong productivity savings" |
| Q1 2026 | $19.443B (+8.5%) | +2.6% | 16.5% vs 15.8% |
| Q2 2026 | $24.181B (+6.4%) | +2.4% | 16.8% (−40 bps) |
Growth is price-driven; volumes declined (NA foods −4%, beverages −3% in Q3 2025; global food volume
−2% in Q4 2025). WSJ reports planned **price cuts on Doritos and other snacks** to regain volume —
margin risk if sustained. Sources: company releases (SEC 8-K exhibits, pepsico.com), zacks.com.

## 5. Eight-quarter guide history
| Quarter | Guide action |
|---|---|
| Q3 2025 (2025-10-09) | FY25 reaffirmed (low-single-digit organic, ~flat core cc EPS) |
| Q4 2025 (2026-02-03) | FY26 **affirmed** per December initial: organic +2–4%, core EPS $8.55–8.71, rev $97.7–99.6B; dividend +4% |
| Q1 2026 (2026-04-16) | FY26 **reaffirmed** |
| Q2 2026 (2026-07-09) | FY26 **reaffirmed**, tracking toward the **low end** |
| Q2 2025 and earlier | **not found** |
PepsiCo is a **steady reaffirmer** — it has not raised FY26 once. The risk is a guidance cut to the
low end or below if volumes keep softening.

## 6. Moat / AI irreplaceability
Global brands, distribution and shelf-space scale, bottling network, and portfolio breadth. But
consumers substitute freely (private label, healthier options) — pricing power is showing its limits.
**Moderate-high moat, not absolute.** AI exposure is operational (supply chain, marketing), not
existential either way.

## 7. Print-specific risks
- **Guide risk is the highest in this batch**: "tracking toward the low end" + snack price cuts = the
  market will read any conservatism as a prelude to a cut.
- Organic volume growth is anemic and missed targets; price-driven growth is exhausted.
- Activist overhang: Elliott Management's ~$4B stake (announced 2025-09-02) creates expectations of
  portfolio/structural action — a quiet quarter disappoints that crowd too.
- Stock −21.58% below 52-week high, forward P/E 14.46 — cheap, but the derating reflects the volume
  problem, not a mispricing.
- Last beat-and-reaffirm was **sold** (−3%).

## 8. Scores (0–10)
- **Beat likelihood: 5** — small, inconsistent beats (3/4); bar was cut into the print, which helps.
- **Guide risk: 8** — high; affirmed-but-low-end with deteriorating volumes is one step from a cut.
- **Priced-in: 4** — heavily derated (−21.6% off high), so pessimism is partially priced; but the
  guide, not the multiple, is the risk.

## 9. Verdict
A confirmed date but a deteriorating guide trajectory — the last reaffirm was sold, and "low end"
language rarely improves. **Plan B**; only post-print, and only if the guide holds without a cut.

## 10. Plan A/B
**Plan B.** Disqualifiers: (a) Plan A needs a strong reaction record — PEP's last two guide-affirmed
prints went +5% then −3%, no consistent reward pattern; (b) current options-implied move **not found**,
so implied > realized (4.18% absolute) cannot be verified; (c) guide-risk 8 with volumes weakening.

---
# BAC — Bank of America Corp.

## 1. Date: CONFIRMED 2026-10-14 BMO (Q3 2026)
BofA IR calendar published **2025-05-07**: results ~6:45 a.m. ET, investor call 8:30 a.m. ET.
Source: https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/05/bank-of-america-announces-2026-financial-reporting-dates.html
(Note: the cached 2026-10-14 date matches company IR; the older 2026-10-13 brief was stale.)

## 2. Consensus bar & revisions
- EPS consensus Q3 2026: **$1.18** (6 analysts, $1.13–$1.22) — Barchart.
- Revenue consensus: **~$31.22B** (AInvest); an older Seeking Alpha figure was $31.31B — **vendor
  spread flagged**.
- Q4 2026 EPS $1.15; FY26 $4.68; FY27 $5.27 (Barchart, 9 estimates).
- 30-day revision trend: **not found**.

## 3. Last four prints (reported vs consensus, guide outcome, reaction)
| Print | Date | EPS | Revenue | Guide outcome | Reaction |
|---|---|---|---|---|---|
| Q2 2026 | 2026-07-14 BMO | $1.21 vs $1.13 (+7.1%) | $31.6B; NII $16.2B (+9%); trading $7.1B (+34%) | NII growth guide **raised to upper end of 6–8%** | **+1.88%** print-day (Finnhub $59.50→$60.62); screen +2% |
| Q1 2026 | 2026-04-15 BMO | $1.11 vs $1.00–1.01 (+10–11%) | $30.27–30.43B vs ~$29.72–29.93B; NII $15.9B (+9%); efficiency 61% | NII growth guide **raised 5–7% → 6–8%** | Premarket ~+2%; exact close **not found**; screen +2% |
| Q4 2025 | 2026-01-14 BMO | $0.98 vs $0.96 (+2.1%) | $28.37B vs $27.55–27.59B; NII $15.75–15.9B; efficiency 61.5% | No guide change found | Contested: −1.2% premarket, later **−3.7%** tied partly to credit-card-rate-cap/regulatory headlines; screen −4% |
| Q3 2025 | 2025-10-15 BMO | $1.06 vs $0.94–0.95 (+12.8%) | $28.09B vs $27.58B (+10.8%); NII $15.39B record (+9%); IB fees +43% | No guide change found | **+3.9–4.4%** intraday (ainvest); screen +4% |

Screen: 4/4 beats, avg surprise 7.55% (+1.43 trend), 75% positive, avg +1.33%, absolute 2.52%,
worst −3.78%. OptionsAI per-event table matches: +1.9%, +1.8%, −3.8%, +4.4%. Moves are small —
banks need a guide or macro kicker to move.

## 4. Revenue/margin trend (4 quarters, verified)
| Quarter | Revenue | NII | Efficiency ratio |
|---|---|---|---|
| Q3 2025 | $28.09B | $15.39B (+9%) | n/a |
| Q4 2025 | $28.37B | $15.75–15.9B | 61.5% |
| Q1 2026 | $30.27–30.43B | $15.9B (+9%) | 61% |
| Q2 2026 | $31.6B | $16.2B (+9%) | n/a |
NII compounding steadily (+9% YoY three prints running); screen revenue growth +7.17%,
acceleration +4.61 pp. Sources: zacks.com, indexbox.io, company materials.

## 5. Eight-quarter guide history
| Quarter | Guide action |
|---|---|
| Q1 2026 (2026-04-15) | NII growth guide **raised 5–7% → 6–8%** |
| Q2 2026 (2026-07-14) | NII growth guide **raised to the upper end of 6–8%** |
| Q3 2025 (2025-10-15) | **not found** |
| Q4 2025 (2026-01-14) | **not found** |
| Earlier | **not found** |
BAC is a **nontraditional guider**: no consolidated quarterly EPS/revenue guide; it guides NII,
expenses, and capital/credit outlook. The NII bar has now been raised twice — a third raise is
unlikely, and a hold at "upper end of 6–8%" is the likely base case.

## 6. Moat / AI irreplaceability
Deposit franchise, balance-sheet scale, digital distribution (Erica), capital/regulatory barriers.
Products remain substitutable; pricing is rate-driven. AI is a cost/efficiency lever (Erica,
operations), not a moat threat. **Moderate-high moat.**

## 7. Print-specific risks
- NII guide already raised twice; the marginal surprise must come from trading, IB fees, or credit —
  all lumpy.
- Regulatory overhang: credit-card interest-rate-cap proposals pressured the stock around the Q4 2025
  print; headline risk persists into Q3 2026.
- Screen `RECEIVABLES_OUTRUN` (receivables divergence +0.1244): bank-model artifact (loan/trading-asset
  classification), not an industrial EQ flag; accrual −0.00725 and CFO/NI 1.782 are otherwise clean.
- Finnhub 1-month return −6.42% / 5-day −7.91% (as-of 2026-09-21): the stock has pulled back into the
  print — reduces priced-in risk, but also signals cautious positioning.

## 8. Scores (0–10)
- **Beat likelihood: 7** — 4/4 beats, NII compounding, efficiency stable.
- **Guide risk: 5** — medium; NII bar raised twice already, limited room for a third raise; risk is a
  hold-guide plus macro/regulatory noise.
- **Priced-in: 5** — −8.15% 21-session pullback and 10.47% below high offset an elevated NII bar.

## 9. Verdict
A confirmed-date bank with a clean beat record but a twice-raised NII bar and tiny realized moves —
**Plan B**; nothing in the setup clears the Plan A bar (implied > realized unverifiable).

## 10. Plan A/B
**Plan B.** Disqualifiers: (a) Plan A requires expected move exceeding historical realized movement
(2.52% absolute) — current ticker-specific implied move **not found** (only a stale Jan-2026 preview at
±3.2% and an average realized of 2.51%); (b) no disqualifier-free strong reaction record (last four:
+2%, +2%, −4%, +4%).

---

# FOXA — Fox Corporation (Class A)

## 1. Date: ESTIMATED ~2026-10-28/29 BMO (fiscal Q1 2027)
Calendars conflict between **2026-10-28 and 2026-10-29** (MarketBeat labels 10-29 estimated; usually
BMO). No primary company announcement found → ESTIMATED, automatic Plan B.
Source: https://www.marketbeat.com/earnings/reports/ (FOX earnings calendar pages)

## 2. Consensus bar & revisions
- FQ1 2027 EPS: **$2.04** (Zacks) vs **$2.11** (FXEmpire) — **vendor spread flagged**; another source
  $2.01.
- Revenue: **$4.39B** (FXEmpire) vs $4.29B (other source) — **vendor spread flagged**.
- FQ2 2027 EPS $0.94; FY27 $5.99 (Zacks). Zacks showed **zero 30-day revisions**.
- Fox issues no quantitative company guidance to compare against.

## 3. Last four prints (reported vs consensus, guide outcome, reaction)
| Print | Date | Adj EPS | Revenue | Guide outcome | Reaction |
|---|---|---|---|---|---|
| FQ4 2026 | 2026-08-06 BMO | $1.79 vs $1.44–1.45 (+24%) | $4.21B vs $3.64–3.72B (+13–16%) | No quantitative guide (buybacks continued) | **+6.07%** researched; screen positive |
| FQ3 2026 | 2026-05-11 | $1.32 vs $1.02 (+29%) | $3.99B vs $3.79B (−8.6% YoY — no prior-year Super Bowl); adj EBITDA $954M (+11%); Tubi digital ads double-digit | No quantitative guide | **+3.5%** (AlphaStreet) |
| FQ2 2026 | 2026-02-04 BMO | $0.82 vs $0.47–0.51 (+60–75%) | $5.18B vs $5.05–5.09B (+2%); adj EBITDA $692M (−11%, higher sports rights costs); $1.55B buybacks in quarter | No quantitative guide | Premarket positive, full-day **−4%** (screen) — big beat sold |
| FQ1 2026 | 2025-11 | $2.32 vs $2.05–2.14 (+8–13%) | n/a | No quantitative guide | **+8%** (screen) |

Screen: 4/4 beats, avg surprise **40.42%** (trend shrinking −15.19 — estimates are catching up),
75% positive, avg +3.32%, absolute 5.14%, worst −3.67%. Big beats partly reflect low-balled
estimates; the FQ2 2026 print shows a +60–75% beat can still fall.

## 4. Revenue/margin trend (lumpy by design)
| Quarter | Revenue | Note |
|---|---|---|
| FQ1 2026 | n/a | EPS $2.32 — political-ad cycle quarter |
| FQ2 2026 | $5.18B (+2%) | 7-game World Series; Tubi revenue +19%; adj EBITDA −11% on sports rights costs |
| FQ3 2026 | $3.99B (−8.6%) | No prior-year Super Bowl; adj EBITDA +11% |
| FQ4 2026 | $4.21B | Big revenue beat |
Comparisons are event-cycle-driven (Super Bowl, political, MLB postseason); screen revenue growth
+28.14% with +24.27 pp acceleration reflects the FQ4 beat, not a run-rate. Sources: SEC 8-K exhibit
(foxearningsreleaseq226.htm), alphastreet.com, zacks.com, thewrap.com.

## 5. Eight-quarter guide history
| Quarter | Guide action |
|---|---|
| FQ1–FQ4 2026 | **No quantitative EPS/revenue guidance issued** — qualitative segment/event commentary, dividend, and buybacks only (e.g., $1.55B repurchased in FQ2 2026) |
| Earlier | **not found** |
Fox is a **non-guider** in the quantitative sense. The print risk is estimate-vs-actual and
management's qualitative tone on affiliate renewals, sports rights costs, and Tubi.

## 6. Moat / AI irreplaceability
Live sports/news rights, affiliate distribution, broadcast footprint, and Tubi scale (most-watched
quarter ever in FQ2 2026; view time +27%). Offset by sports-rights cost inflation and cord-cutting
(cable news subscribers −6.3% in FQ2 2026). AI exposure is limited — live rights are the moat, and
AI doesn't replace live sports. **Moderate moat, eroding at the edges.**

## 7. Print-specific risks
- No quantitative guide means the bar is whatever analysts set — and the avg surprise trend is
  **shrinking** (−15.19): estimates are catching up, so the "low-ball beat" engine is weakening.
- Event lumpiness: FQ1 is a comp against the political-ad cycle; affiliate-fee and rights-cost
  commentary can swing the stock without an EPS signal.
- FQ2 2026 precedent: a +60–75% EPS beat **fell 4%** — the market punishes margin/rights-cost
  developments even on huge beats.
- Screen `RECEIVABLES_OUTRUN`: possibly ad-billing seasonality around event quarters; accrual
  −0.0125 and CFO/NI 1.169 are otherwise healthy.
- Finance data found is **FOX class B**, not FOXA — do not apply to FOXA without the proxy label.

## 8. Scores (0–10)
- **Beat likelihood: 6** — 4/4 beats but inflated by low-balled estimates that are now catching up.
- **Guide risk: 6** — medium-high; no quantitative guide to underwrite, event-cycle lumpiness, and the
  FQ2 precedent of a huge beat being sold.
- **Priced-in: 5** — −4.75% 21-session, 14.53% below high; but the last big beat fell, so positioning
  is not the binding constraint.

## 9. Verdict
A no-guide media name with a shrinking estimate-catch-up tailwind and a conflicted calendar date —
**Plan B**; the event-cycle lumpiness makes pre-print positioning a coin flip.

## 10. Plan A/B
**Plan B.** Disqualifiers: (a) date **conflicted** (10-28 vs 10-29) and unconfirmed by company IR;
(b) ticker-specific options-implied move **not found** (FOX class-B proxy ~2.8% is not FOXA's chain);
(c) Plan A requires a strong reaction record — FQ2 2026's +60–75% beat falling 4% breaks it.

---

## Batch 3 source list (all accessed 2026-09-21)
- PepsiCo IR: https://www.pepsico.com/newsroom/press-releases/2026/pepsico-announces-timing-and-availability-of-third-quarter-2026-financial-results
- BofA IR calendar: https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/05/bank-of-america-announces-2026-financial-reporting-dates.html
- Howmet Q1 2026 release: https://www.howmet.com/wp-content/uploads/sites/3/2026/05/Howmet-Aerospace-Reports-First-Quarter-2026-Results.pdf
- BNY Q4 2025 release (bny.com mirror): https://prodcs.bny.com/assets/corporate/documents/pdf/investor-relations/earnings/earnings-press-release-4q-2025.pdf
- BNY Q1 2026 8-K mirror: https://api-gw-prd.stocktwits.com/earnings-api/v1/documents/ba8b7fce-6ed4-4fa1-9735-1392aaeab5af/8-K.pdf
- Fox FQ2 2026 8-K exhibit (SEC): https://www.sec.gov/Archives/edgar/data/1754301/000162828026005277/foxearningsreleaseq226.htm
- PepsiCo Q4 2025 release (SEC mirror): https://files.quartr.com/reports/84c84-2026-02-03-11-11-01.pdf?ref=U3RvY2tBbmFseXNpcw==
- OptionsAI per-ticker earnings pages: https://tools.optionsai.com/companies/HWM/earnings, https://tools.optionsai.com/companies/PEP/earnings/bullish-trades, https://tools.optionsai.com/companies/BAC/earnings/bullish-trades
- Barchart earnings estimates: https://barchart.com/stocks/quotes/HWM/earnings-estimates, https://barchart.com/stocks/quotes/BAC/earnings-estimates
- Zacks earnings recaps (zacks.com): HWM Q3 2025, PEP Q3/Q4 2025, BAC Q3 2025, BNY Q3 2025, FOX FQ2/FQ3 2026
- MarketBeat earnings pages; Finnhub quote/returns (via browser search snippets, as-of 2026-09-21);
  tipranks.com options piece; asktraders.com BAC preview; alphastreet.com; thewrap.com; ainvest.com.
