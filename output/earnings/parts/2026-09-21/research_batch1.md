# EARNINGS-mode research — batch 1/3
**Run date:** 2026-09-21 (PDT). **Tickers:** PAYX, CTAS, GS, MS, BLK.
**Skill:** `.claude/skills/stock-pick-earnings/SKILL.md` (read 2026-09-21, obeyed).
**Screen baseline:** `output/earnings/shortlist.json` (read 2026-09-21). Screen figures are cited as baseline
throughout; where researched figures disagree they are flagged and the researched figure is preferred.
"not found" = could not verify; never invented.

## Cross-ticker notes
- **Actionable window:** doctrine treats events within ~10 calendar days as actionable. On 2026-09-21 that means
  **PAYX and CTAS (both 2026-09-23) are actionable; GS (2026-10-13), MS (2026-10-14), and BLK (date conflicted,
  ~2026-10-13/14) are watchlist only** — no pre-print positioning yet.
- **Options-implied vs realized:** options move vs screen realized avg absolute move (research date 2026-09-21):
  PAYX 7.56% monthly (10/16 expiry) vs 3.65% realized; CTAS 4.76% weekly (9/25 expiry) vs 4.41%; GS 7.48% vs 3.51%;
  MS 7.49% vs 4.09%; BLK 6.56% vs 4.50%. Implied > realized in all five; implied ≈ 2× realized for PAYX/GS/MS.
  (Sources: optionslam.com tickers/stock pages.)
- **Bank EQ flags:** GS/MS carry screen `LOW_CASH_CONVERSION` and `RECEIVABLES_OUTRUN` flags; BLK carries
  `LOW_CASH_CONVERSION`. For banks these are largely screen-model artifacts: operating cash flow and
  "receivables" are dominated by trading assets/liabilities, secured financing, loans, deposits, and settlement
  balances, not industrial-style working capital. Confirmed from 10-K/10-Q filings (GS 10-K 2025; MS 10-Q Q2 2026),
  which carry no such EQ warnings in their own risk/contingent-liability discussions. Not a green flag for
  earnings quality in the industrial sense — just not the red flag the screen implies. For banks, EQ analysis
  should weight: credit provisions, capital ratios (CET1), and reserve methodology instead.
- **CTAS vendor disagreement (flagged):** screen reaction_last4 for CTAS is `+7%, -5%, +1%, +1%`. Optionslam's
  earnings-trend event table implies roughly **+4.4%** for the Q4 FY26 print (screen: +7%) and roughly **-0.7% to -1%**
  for the Q3 FY26 print (screen: -5%). Screen numbers are used as baseline per the no-replace rule, but the
  verifier should spot-check these two CTAS reactions against daily closes; the true reactions may be smaller.

---

# PAYX — Paychex, Inc.

## 1. Date: CONFIRMED 2026-09-23 BMO (fiscal Q1 2027)
Company press release dated **2026-09-09**: results before markets open; conference call 9:30 AM ET.
Source: https://www.stocktitan.net/news/PAYX/paychex-schedules-first-quarter-fiscal-2027-earnings-conference-call-1c9njls6x9l2.html

## 2. Consensus bar & revisions (as of 2026-09-18/21)
- EPS consensus: **$1.32** (18 analysts; range $1.29–$1.34).
- Revenue consensus: **$1.63B** ($1.6266B per AlphaStreet).
- 30-day EPS estimate: unchanged at $1.32. 90-day: $1.31 → $1.32 (up ~0.8%). No downward revision pressure.
- FY2027 guide implies adjusted EPS $5.90–$6.01 on revenue +5–6% and adj operating margin ~44%.
- Source: https://news.alphastreet.com/paychex-payx-q1-2027-preview-eps-est-1-32-reports-september-23/

## 3. Last four prints (reported vs consensus, guide outcome, reaction)
| Print | Date | Adj EPS | Revenue | Guide outcome | Reaction |
|---|---|---|---|---|---|
| Q4 FY26 | 2026-06-24 | $1.32 vs $1.31 (+0.8%) | $1.61B vs $1.60B (+0.6%) | **New FY27 guide:** rev +5–6%, adj op margin ~44%, adj EPS +7–9% (~$5.90–$6.01) | **-1.7%** (optionslam) / -2% (screen) — small beat punished |
| Q3 FY26 | 2026-03-25 | $1.71 vs ~$1.68 (+~1.8%) | $1.809B, ~+1.4% above consensus | FY26 rev guide reaffirmed 16.5–18.5%; adj EPS guide retained 10–11% | **+3.0%** (optionslam) / +3% (screen) |
| Q2 FY26 | 2025-12-19 | $1.26 vs $1.23–1.24 (+~2%) | $1.558B (+18% YoY), ~$10M light of consensus | FY26 adj EPS guide **raised** 8–9% → 10–11% ($5.48–$5.53); **but** cautioned FY26 revenue growth toward the **low end** of 16.5–18.5% → PT cuts from MS/JPM/Citi | +2% (screen) |
| Q1 FY26 | 2025-09-30 | $1.22 vs $1.20–1.21 (+~1–2%) | $1.54B (+17% YoY), in-line/light | FY26 rev guide **raised** to 16.5–18.5%; adj EPS growth guide **raised** 8.5–10.5% → 9–11% | **-1.4%** day-of (indexbox/coincentral) / -2% (screen) — beat, fell |

Beats are consistently small (0.8–2%). Two of the last four beats fell (Q4 FY26, Q1 FY26).

## 4. Revenue/margin trend (4 quarters, verified)
| Quarter | Revenue | Adj op margin |
|---|---|---|
| Q1 FY26 | $1.54B (+17% YoY) | 40.7% |
| Q2 FY26 | $1.558B (+18%) | 41.7% |
| Q3 FY26 | $1.809B (+18.5%) | 43.8% |
| Q4 FY26 | $1.61B (+18.3%) | 42.1% |
Growth is Paycor-acquisition-driven (~17pp of the +17–18% from Paycor); organic growth described by analysts as
"muted". GAAP margins compressed by acquisition costs (GAAP EPS fell 10% in Q1 FY26 while adj EPS rose 5%).

## 5. Guide analysis & eight-quarter guide history
FY27 guide (June 2026): revenue **+5–6%**, adj operating margin **~44%**, adj EPS **+7–9%** ($5.90–$6.01).
This is a deliberate deceleration from FY26's acquisition-inflated +18% to normalized growth; margin guide ~44%
implies ~200–300 bps expansion vs FY26's ~42–43%.
Verified guide history (earlier than FY26 not found):
- Q1 FY26 (Sep 2025): raised FY26 rev to 16.5–18.5% and adj EPS growth to 9–11%.
- Q2 FY26 (Dec 2025): raised FY26 adj EPS growth to 10–11%, **lowered the bar on revenue** (cautioned low end).
- Q3 FY26 (Mar 2026): reaffirmed rev guide, retained EPS guide (no raise).
- Q4 FY26 (Jun 2026): FY27 initial guide as above (reset, not a raise).
Pattern: conservative raisers on EPS, but revenue tone deteriorated through FY26. The bar for Q1 FY27 is modest
($1.63B rev ≈ +5.9% YoY) — but the stock has fallen on two of the last four beats, so the guide reaction
function is asymmetric. Key tell: whether FY27 revenue guide (+5–6%) is reaffirmed or trimmed.

## 6. Priced-in setup
- 21-day return **-5.19%**; **8.80% below 52-week high**; forward P/E **18.16** (screen).
- Options imply **7.56%** monthly vs 3.65% realized average — the premium is rich relative to a name whose average
  absolute move is 3.65% and whose average move on 7 measured beats is only +0.33%.
- Beat-up rate 71.43%; worst move -9.40%. Setup is not demonstrably unpriced: the options premium already pays
  for more than twice the typical realized move.

## 7. Moat / AI irreplaceability
Embedded HCM/payroll platform serving ~800K clients and ~2.5M worksite employees; compliance complexity and
switching costs are real moats. AI exposure is augmentation, not existential: management's agentic-AI pilots
handled thousands of payroll inquiries at ~100% accuracy — AI lowers cost-to-serve, which helps margins. No
structural displacement threat visible in the next 2–3 years.

## 8. Print-specific risks
- Small beat/miss tolerance: consensus EPS range only $1.29–$1.34; the stock falls on beats with soft revenue.
- FY27 guide trim risk: rev +5–6% and margin ~44% are the whole story; any revenue-guide cut sinks it.
- Paycor integration noise: GAAP vs adjusted divergence; analysts flag muted organic growth.
- Macro sensitivity: HCM revenue tied to SMB employment growth; tight labor market cuts both ways.

## 9. Scores
- **EARN 58** — 7 measured beats, avg surprise +1.76%, trend **-0.30** (declining); beats small, two of last four fell.
- **GUIDE 62** — conservative-raiser history on EPS, but revenue tone weakened in FY26; FY27 is a low-bar reset.
- **RISK 55** — option premium rich vs realized; small organic growth; beat-but-fall precedent.

## 10. Plan
**Plan B.** Date confirmed and the bar is modest, but the setup is not demonstrably unpriced (implied 7.56% vs
realized 3.65%) and two of the last four beats fell — the doctrine's "either of last two beats fell" caution
applies (Q4 FY26 beat and fell). Participation requires a beat plus a clean FY27-guide reaffirmation; neither is
owed to us. Trade only a confirmed strong beat-and-raise.

---

# CTAS — Cintas Corporation

## 1. Date: CONFIRMED 2026-09-23; BMO strongly supported
Company release dated **2026-09-09** confirms the date and a 10:00 AM ET webcast; the release does not
explicitly say "before market open," but multiple market sources (optionslam, Zacks, Barchart) treat it as a
BMO report. Date is confirmed; BMO is strongly supported, not literally in the company's words.
Source mirror: https://www.stocktitan.net/news/CTAS/cintas-corporation-announces-webcast-for-first-quarter-fiscal-year-qk5ohoodcuwz.html

## 2. Consensus bar & revisions (as of 2026-09-21)
- EPS consensus: **$1.35** (8 estimates; next-quarter EPS consensus also $1.35).
- Revenue consensus: **$2.9777B**.
- FY2027 EPS consensus: **$5.49** (11 estimates) — sits **at the top of company guide** ($5.36–$5.50). FY2028: $6.10.
  This matters: the Street is not giving Cintas credit for a raise; consensus already embeds the top of guidance,
  so any non-raise is a disappointment against the bar even if the company "holds" guide.
- Forward revenue consensus not found.
- Source: https://barchart.com/stocks/quotes/CTAS/earnings-estimates

## 3. Last four prints (reported vs consensus, guide outcome, reaction)
| Print | Date | Adj EPS | Revenue | Guide outcome | Reaction |
|---|---|---|---|---|---|
| Q4 FY26 | 2026-07-15 | $1.29 vs $1.24 (+4.0%) | $2.91B vs $2.88B (+1.0%) | **New FY27 guide:** rev $12.10–12.25B, adj EPS $5.36–$5.50 | **+4.4%** (optionslam) / +7% (screen) — vendor disagreement, see header |
| Q3 FY26 | 2026-03-25 | $1.24 vs $1.23 (+0.8%) | $2.84B vs $2.82B (+0.9%) | **Raised** FY26 guide: rev $11.21–11.24B, adj EPS $4.86–$4.90. **UniFirst acquisition announced 2026-03-10** — deal/regulatory overhang | **-0.7% to -1%** (optionslam) / **-5%** (screen) — in-line beat punished, deal overhang; see header |
| Q2 FY26 | 2025-12-19 (per screen date) | $1.21 vs $1.19 (+1.68%) | not found | not found | +1% (screen) |
| Q1 FY26 | 2025-09-24 | $1.20 vs $1.19 (+0.84%) | not found | not found | +1% (screen) |

**The screen's -5% on a beat (answering the task's note):** the -5% belongs to the **Q3 FY26 print of 2026-03-25**
(adj EPS $1.24 vs $1.23, revenue $2.84B vs $2.82B — essentially in-line). Why it fell: (a) the beat was 0.8%, i.e.
no margin of safety; (b) the **$5.1B UniFirst acquisition had been announced two weeks earlier (2026-03-10)**,
adding regulatory and integration-deal-cost overhang that overshadowed an in-line quarter; (c) optionslam's own
event table measures the reaction closer to -1%, so part of the screen's -5% is likely the heuristic's
BMO/AMC-ambiguous window — flag for verifier. Either way, the lesson holds: this name punishes in-line prints.

## 4. Revenue/margin trend (verified)
| Quarter | Revenue | Adj EPS |
|---|---|---|
| Q1 FY26 | not found (EPS $1.20) | $1.20 |
| Q2 FY26 | not found (EPS $1.21) | $1.21 |
| Q3 FY26 | $2.84B | $1.24 |
| Q4 FY26 | $2.91B | $1.29 |
Operating margins for these quarters not found. Revenue growing high-single-digits (FY27 guide midpoint $12.175B
vs FY26 ~$11.22B ≈ +8.5%).

## 5. Guide analysis & eight-quarter guide history
FY27 guide (Jul 2026): revenue **$12.10–12.25B** (+~8.5% at midpoint), adj EPS **$5.36–$5.50** (+~12% at midpoint).
Verified history (earlier than FY26 Q3 not found):
- Q3 FY26 (Mar 2026): **raised** FY26 guide to $11.21–11.24B / $4.86–$4.90 (while digesting UniFirst announcement).
- Q4 FY26 (Jul 2026): FY27 initial guide as above.
The guide posture is a reliable raiser with strong execution, but **the Street is already at the top of the
guidance range** (FY27 consensus $5.49 vs guide top $5.50). The key tell for this print: a beat-and-raise that
lifts the EPS range above consensus is the only bullish surprise path; merely meeting consensus at the top of
guide is priced.

## 6. Priced-in setup
- 21-day return **-2.68%**; **8.49% below 52-week high** ($197.64 vs $219.16 high; 50-day MA $201.91, 200-day $185.67);
  forward P/E **32.3** (screen) — a full premium multiple.
- Options imply **4.76%** weekly (9/25 expiry) vs 4.41% realized — roughly in line, slightly rich.
- Beat-up rate 75%; worst move -10.57%. Small beats (0.8–1.7%) are the norm; execution is excellent but the
  multiple already assumes it.

## 7. Moat / AI irreplaceability
Route-based uniform/facility-services network density — the classic route moat: once the truck is in a metro
daily, marginal-customer cost is near zero. Services are physical and compliance-driven (safety, sanitation),
essentially **immune to AI displacement**. UniFirst acquisition, if cleared, deepens the moat.

## 8. Print-specific risks
- Thin beats: 0.8–1.7% EPS surprises are noise; a 1-cent miss at 32× forward is a real drawdown risk.
- Consensus at top of guide ($5.49 vs $5.50): raise-or-fail dynamics.
- UniFirst deal overhang persists (regulatory review; deal-cost adjustments flow through guidance).
- Prior beat punished: the market has shown it will sell in-line prints.

## 9. Scores
- **EARN 64** — beat-up 75%, avg surprise +1.09%, trend **+0.57** (improving); but beats are tiny.
- **GUIDE 72** — reliable raiser, strong execution; capped because the Street already embeds the top of guide.
- **RISK 50** — premium multiple vs thin beats and a proven willingness to sell good prints.

## 10. Plan
**Plan B.** Confirmed date and the best execution profile in the batch, but no demonstrably unpriced setup:
beats average <2%, the multiple is 32× forward, consensus sits at the top of guidance, and options imply 4.76%
vs a 4.41% realized average. Watch for a beat-and-raise that lifts the EPS range; a mere meet is a sell-the-news
candidate (as Q3 FY26 demonstrated).

---

# GS — Goldman Sachs

## 1. Date: CONFIRMED 2026-10-13 BMO
Goldman's own annual earnings calendar (published 2025-08-18): results around 7:30 AM ET, call 9:30 AM ET.
Source: https://www.goldmansachs.com/pressroom/press-releases/2025/conference-call-dates-to-announce-4q25-and-2026-earnings-results

## 2. Consensus bar & revisions (as of ~2026-09-10/21)
- EPS consensus: **$15.62**. Exact revenue consensus **not found** (one preview cites roughly $17B–$18B —
  insufficient; not used as the bar).
- Full-year context: trailing EPS ~$64.79; MarketBeat expects ~5.3% next-year growth ($68.58 → $72.23). These are
  trailing-twelve-month reference points, not the Q3 bar.

## 3. Last four prints (reported vs consensus, reaction)
| Print | Date | EPS | Revenue | Reaction |
|---|---|---|---|---|
| Q2 2026 | 2026-07-14 | $20.98 vs $14.47 (+45%) | $20.34B vs $16.22B (+25%) | **+9%** (screen) |
| Q1 2026 | 2026-04-13 | $17.55 vs $16.47 (+6.6%) | $17.23B vs $16.97B (+1.5%) | +2% (screen) — 2nd-best quarter in firm history, stock fell 3.5–3.7% intraday/next day on the FICC miss (-10% YoY to $4.01B), then recovered |
| Q4 2025 | 2026-01-15 | not found | not found | +5% (screen) |
| Q3 2025 | 2025-10-14 | not found | not found | -2% (screen) |

Beat-up 87.5%; avg move **+3.00%**; avg absolute 3.51%; worst -2.04%. Avg EPS surprise +20.49%, trend +11.39
(strongest earnings profile in the batch).

## 4. Revenue/margin trend (verified)
| Quarter | Net revenue | EPS | ROE (annualized) |
|---|---|---|---|
| Q1 2026 | $17.23B (+14% YoY, 2nd-best ever) | $17.55 | 19.8% |
| Q2 2026 | $20.34B | $20.98 | not found |
Q1 detail: Global Banking & Markets record $12.7B (segment ROE >22%); record Equities $5.33B (+27%, record
financing); FICC $4.01B (-10%, two straight quarterly misses); A&WM $4.08B (+10%); book value $361.19.
Structural shift in progress: FICC from strength to drag two quarters running; equities financing now ~40% of GBM
with the firm calling it "more durable" revenue. The market is split on valuation framework (cyclical 8–10× vs
hybrid 10–12×).

## 5. Guide analysis & eight-quarter guide history
**Goldman does not give EPS/revenue guidance.** Forward posture is read through: (a) IB backlog (Q1: highest in
four years; #1 in announced/completed M&A with a $150B lead), (b) capital returns ($6.4B returned in Q1 2026),
(c) AUS record $3.65T with 33 straight quarters of fee-based inflows, (d) cautious macro tone from Solomon
("geopolitical landscape remains very complex"). Q3 2026 preview frames: Q3 EPS low-to-mid teens vs prior-year
$9.87 (+44%); Q3 2026 marks the second full quarter since the Feb 2026 "One Goldman 2.0" reorganization
(collapsed from 3 to 2 units; target 15–17% ROTCE, 60% efficiency, ~$1.3B pre-tax savings), and Q3 marks one full
year since the July 2025 divestiture of the GreenSky seller-finance loan portfolio — a cleaner comp.
GUIDE lens score reflects this non-guider reality rather than penalizing it.

## 6. Priced-in setup — **watchlist, not actionable (d=22, beyond ~10-day window)**
- 21-day return **-7.34%**; **17.83% below 52-week high**; forward P/E **12.72** (screen) — cheapest in the batch
  on a forward basis, and ~0.9× forward P/E relative to its hybrid-multiple debate.
- Options imply **7.48%** weekly vs 3.51% realized average — implied is more than 2× the historical absolute move.
- Beat-up 87.5% with avg move +3.00%: the best reward-to-beat profile here, but the Q1 2026 episode shows even
  record numbers get sold when the mix (FICC) disappoints.

## 7. Moat / AI irreplaceability
Premier investment-banking franchise: #1 M&A share, balance-sheet risk capacity, and relationship-driven
advisory/deal flow that cannot be automated away in the near term. AI is a productivity tool (research, code,
ops) not a replacement for origination or principal risk-taking. Moat is strong; cyclicality is the risk, not
AI displacement.

## 8. Print-specific risks
- Q1 2026 taught the lesson: a headline beat with a FICC miss got sold (-3.5%+). Q3 trading/FICC is the risk
  variable.
- Cyclical peak risk: record GBM revenues and 2nd-best-ever quarters raise the bar; capital-markets activity
  (M&A close timing) is lumpy.
- The ~2× rich options premium (7.48% vs 3.51% realized) leaves little edge for a long-gamma setup.

## 9. Scores
- **EARN 85** — 87.5% beat-up, +20.49% avg surprise, +11.39 trend; strongest in batch.
- **GUIDE 50** — non-guider by model; forward read via backlog/capital/AUS, which are strong but not guidance.
- **RISK 58** — cyclicality, FICC-softness precedent, rich implied premium; date beyond actionable window.

## 10. Plan
**Plan B (watchlist).** Nothing to do pre-print on 2026-09-21: event is 22 days out, beyond the ~10-day
actionable window, and the options premium is more than twice the realized average move. Revisit within ~10 days
of 2026-10-13: a cleaner FICC print plus reaffirmed IB backlog on a modestly priced reaction would be the only
setup that could ever qualify for Plan A.

---

# MS — Morgan Stanley

## 1. Date: CONFIRMED 2026-10-14 BMO
Morgan Stanley's annual schedule (published 2025-09-11): release around 7:30 AM ET, call 9:30 AM ET.
Source mirror: https://www.stocktitan.net/news/MS/morgan-stanley-schedules-2026-quarterly-investor-conference-ajrgdc9zzvhz.html

## 2. Consensus bar & revisions (as of 2026-09-18/21)
- EPS consensus: **$3.13**. Revenue consensus: **$20.36B**.
- FY2026 EPS consensus ~$12.82 (Barchart, 14 estimates) — the Street expects the strong H1 run-rate to persist
  (H1 annualized implies upside to this number, i.e. the full-year bar is beatable).

## 3. Last four prints (reported vs consensus, reaction)
| Print | Date | EPS | Revenue | Reaction |
|---|---|---|---|---|
| Q2 2026 | 2026-07-15 | $3.46 vs $2.89–2.92 (+~19%) | $21.35B vs $19.67–19.81B (+~8%) | **-3%** (tickeron) / -2.18% (optionslam) / -4% (screen) — **big beat, fell: "sell the news"** |
| Q1 2026 | 2026-04-15 | $3.43 vs $3.02 (+13.5%) | not found | +5% (screen) |
| Q4 2025 | 2026-01-15 | $2.68 vs $2.43 (+10.4%) | not found | +6% (screen) |
| Q3 2025 | 2025-10-15 | $2.80 vs $2.10 (+33%) | not found | +5% (screen) |

**The Q2 2026 beat-but-fall (load-bearing):** EPS +~19%, revenue +~8%, and the stock declined ~3% on the day.
Why: the stock had run >60% TTM into the print and bullish sentiment was stretched — strong trading/banking was
already priced in, leaving no room for upside surprise ("sell the news"). The day-two session the stock rallied
back to its prior level, confirming the move was positioning, not fundamentals. Management also authorized a
**$20B buyback (up to 5.6% of shares)** on 2026-06-24. Under the doctrine, a beat in either of the last two
prints that fell disqualifies any pre-print Plan A consideration outright.

## 4. Revenue/margin trend
| Quarter | Revenue | EPS |
|---|---|---|
| Q3 2025 | not found | $2.80 |
| Q4 2025 | not found | $2.68 |
| Q1 2026 | not found | $3.43 |
| Q2 2026 | $21.35B | $3.46 |
Margins per quarter not found. Trajectory: strong and accelerating through H1 2026 on trading and banking.

## 5. Guide analysis & eight-quarter guide history
**Morgan Stanley does not give EPS/revenue guidance.** Forward posture: capital return ($20B buyback authorized
June 2026), Wealth Management durability vs Institutional Securities cyclicality. No eight-quarter guide history
exists to score — this is stated explicitly rather than forcing a conventional guide table.

## 6. Priced-in setup — **watchlist, not actionable (d=23, beyond ~10-day window)**
- 21-day return **-5.44%**; **10.88% below 52-week high**; forward P/E **14.85** (screen).
- Options imply **7.49%** weekly vs 4.09% realized average — rich.
- Beat-up 75%, avg move +2.66%, worst -4.45%. The critical data point is not the average but the most recent:
  a 19% EPS beat fell ~3%. The market's bar for MS is now "beat big AND show clean forward," and even that got
  sold.

## 7. Moat / AI irreplaceability
Wealth-management scale (~$7T+ client assets franchise) plus top-tier institutional securities. Fiduciary,
regulatory, and relationship intensity make this AI-resistant: AI improves advisor productivity but does not
replace the fiduciary relationship or the balance-sheet/principal businesses. Moderate-high.

## 8. Print-specific risks
- **Sell-the-news precedent is the dominant risk:** the latest print beat by 19% and fell; any repeat of
  priced-in strength is the base case.
- Trading-revenue cyclicality: Q3 2026 trading comps against a strong 2025 base.
- EQ screen flags (`LOW_CASH_CONVERSION`, `RECEIVABLES_OUTRUN`) are accounting artifacts for a bank (see header)
  — the real quality variables are credit provisions and CET1, which filings show as sound.

## 9. Scores
- **EARN 60** — 75% beat-up, +19.08% avg surprise, but trend **-6.57** (declining) and the latest beat fell.
- **GUIDE 50** — non-guider; forward read via buyback and WM durability only.
- **RISK 62** — beat-but-fell precedent, rich implied premium, beyond the actionable window.

## 10. Plan
**Plan B (watchlist).** Plan A is explicitly blocked twice over: (a) the event is 23 days out, beyond the
~10-day actionable window; (b) the doctrine's beat-but-fell rule — the latest print was a +19% EPS beat that
fell ~3%. Revisit within ~10 days of 2026-10-14 with fresh positioning data; only a reset bar (lowered whisper
after the Q2 selloff) could reopen the question.

---

# BLK — BlackRock

## 1. Date: **ESTIMATED / CONFLICTING — no company-IR confirmation found**
- Screen cached: **2026-10-14** (d=23).
- Zacks earnings calendar: **2026-10-13** (AM). MarketBeat: **2026-10-13** (BMO, unconfirmed; "earnings date estimated").
- Optionslam: estimated **2026-10-14**. Investing.com: estimate **2026-10-13**.
- BlackRock's own IR/press room has published no Q3 2026 earnings-date announcement as of 2026-09-21.
- **Status: ESTIMATED with a one-day conflict (Oct 13 vs Oct 14); treat as unconfirmed. Load-bearing: no Plan A
  while the date is unconfirmed.** Sources: https://www.MarketBeat.com/stocks/NYSE/BLK/earnings/ ;
  https://www.optionslam.com/earnings/stocks/BLK

## 2. Consensus bar & revisions (as of 2026-09-21)
- EPS consensus: **$14.24** (Zacks). Exact revenue consensus **not found**.
- Forward context: expected ~20% EPS growth this year, ~8.7% next (Zacks); FY reference ~$55.9 (Barchart).

## 3. Last four prints (reported vs consensus, reaction)
| Print | Date | Adj EPS | Revenue | Reaction |
|---|---|---|---|---|
| Q2 2026 | 2026-07-15 | $13.91 vs $12.69 (+9.6%) | $7.08B vs $6.73B (+5.2%) | **+7%** (screen) |
| Q1 2026 | 2026-04-14 | $12.53 vs ~$11.48–11.96 (+~7%) | $6.70B vs ~$6.43–6.55B (+~3%) | +3% (screen); +2.4% pre-market reported |
| Q4 2025 | 2026-01-15 | $13.16 vs $12.39 (+6.2%) | $7.01B vs $6.75B (+3.8%) | +6% (screen) |
| Q3 2025 | 2025-10-14 | not found | not found | +3% (screen) |

Fundamentals around the prints: Q2 2026 — AUM $14.08T record, net inflows $171B (Q2 record), adj op income +19%,
tech services +17%; Q1 2026 — net inflows $130B (iShares record $132B), AUM $13.89T, adj op income +31%, adj op
margin 44.5%; Q4 2025 — record AUM $14.04T, record $698B full-year inflows ($342B in Q4), adj op income +22.4%,
dividend raised 10% to $5.73, $1.8B buybacks authorized for 2026. GAAP vs adjusted divergence persists
(acquisition charges: GAAP EPS fell in Q4 2025 while adjusted rose) — watch the adjusted metric the Street trades on.

## 4. Revenue/margin trend (verified)
| Quarter | Revenue | Adj op margin |
|---|---|---|
| Q4 2025 | $7.01B (+23% YoY) | ~40.6% (adj op income $2.85B) |
| Q1 2026 | $6.70B (+27% YoY) | 44.5% (as adjusted) |
| Q2 2026 | $7.08B | not found (adj op income +19%) |
Organic base-fee growth: Q4 2025 +9% full-year / +12% annualized in Q4; Q1 2026 TTM +10% on $744B net inflows.
The engine: fee compounding from market appreciation + record inflows + higher-fee private markets (GIP/HPS) and
tech services (+22–24%) bending the fee-compression curve.

## 5. Guide analysis & eight-quarter guide history
**BlackRock does not give EPS/revenue guidance.** Forward posture is read through: net-inflow momentum
($698B FY2025 record; $744B TTM through Q1 2026), dividend (raised 10%), and buyback authorizations
($1.8B for 2026; 7M shares). No eight-quarter guide history exists — stated explicitly, not forced.

## 6. Priced-in setup — **watchlist, not actionable (d≈22–23, beyond ~10-day window; date unconfirmed)**
- 21-day return **-7.22%**; **9.14% below 52-week high**; forward P/E **16.63** (screen); IV 27.33% vs HV 21.17%.
- Options imply **6.56%** weekly vs 4.50% realized average — rich but less extreme than the banks.
- Beat-up 87.5%; avg move **+3.03%**; worst -5.88%. Beats are well rewarded (all four positive reactions), which
  is the attraction — but the bar moves with markets, and Q3 2026 comped against record inflow quarters.

## 7. Moat / AI irreplaceability
~$14T AUM scale is the moat: iShares distribution, Aladdin enterprise entrenchment, and now private-markets
infrastructure (GIP, HPS, Preqin) creating "whole portfolio" mandates. Data/tech (Aladdin, Preqin) make BlackRock
an AI **beneficiary and distributor**, not a target. High moat.

## 8. Print-specific risks
- **Date conflict is the load-bearing risk:** Oct 13 vs Oct 14 unresolved; no company IR announcement. Do not
  trade around a date that isn't confirmed.
- Flow sensitivity: record inflow quarters set a high bar; a market downdraft hits AUM, base fees, and
  performance fees simultaneously.
- Acquisition integration (HPS/GIP/Preqin): GAAP noise and expense drag; the Street trades the adjusted number,
  but repeated one-timers erode trust.
- GAAP/adjusted divergence (Q4 2025: GAAP net income -32.5% while adjusted EPS +10%) — headline risk if the
  adjusted number ever misses.

## 9. Scores
- **EARN 74** — 87.5% beat-up, +7.30% avg surprise, +4.38 trend; beats consistently rewarded (+3% to +7%).
- **GUIDE 50** — non-guider; forward read via flows/dividends/buybacks only.
- **RISK 60** — unconfirmed date (load-bearing), rich implied premium, high inflow bar.

## 10. Plan
**Plan B (watchlist).** Blocked on two independent grounds: (a) the earnings date is **unconfirmed and
conflicted** (Oct 13 vs Oct 14) — no Plan A without a company-confirmed date; (b) the event is beyond the
~10-day actionable window. If IR confirms a date and the setup reprices closer in (d≤10), the rewarded-beat
history makes BLK the most Plan-A-eligible watchlist name in this batch — but that decision belongs to a later run.

---

## Batch summary for the panel
| Ticker | Date status | EARN | GUIDE | RISK | Plan | One-line |
|---|---|---|---|---|---|---|
| PAYX | CONFIRMED 2026-09-23 BMO | 58 | 62 | 55 | **B** | Modest bar, but beats are 0.8–2% and two of last four fell; implied 7.56% vs 3.65% realized. |
| CTAS | CONFIRMED 2026-09-23 (BMO strongly supported) | 64 | 72 | 50 | **B** | Best execution, but beats <2%, 32× forward, consensus at top of guide; Q3 FY26 showed in-line prints get sold. |
| GS | CONFIRMED 2026-10-13 BMO | 85 | 50 | 58 | **B (watch)** | Strongest beat profile; non-guider; d=22, implied ≈2× realized. Revisit d≤10. |
| MS | CONFIRMED 2026-10-14 BMO | 60 | 50 | 62 | **B (watch)** | Plan A doubly blocked: latest +19% beat fell ~3% (sell-the-news); d=23. |
| BLK | **ESTIMATED/CONFLICTED** (Oct 13 vs 14) | 74 | 50 | 60 | **B (watch)** | Rewarded beats, high moat, but date unconfirmed — load-bearing. |

**Load-bearing flags for the panel:**
1. BLK date unconfirmed/conflicted (Oct 13 vs Oct 14) — no company IR announcement as of 2026-09-21.
2. CTAS screen reactions (+7%, -5%) vs researched (optionslam ~+4.4%, ~-1%) — verifier should spot-check.
3. MS Q2 2026: +19% EPS beat fell ~3% — doctrine beat-but-fell rule blocks Plan A.
4. GS/MS/BLK are beyond the ~10-day actionable window (d=22–23) — watchlist only on 2026-09-21.
5. Options-implied moves exceed realized averages in all five (PAYX 7.56/3.65, CTAS 4.76/4.41, GS 7.48/3.51,
   MS 7.49/4.09, BLK 6.56/4.50) — no demonstrably unpriced setup anywhere in this batch.
6. Revenue consensus not found: GS (only "~$17–18B" preview range, insufficient), CTAS forward revenue. BLK revenue consensus not found.
