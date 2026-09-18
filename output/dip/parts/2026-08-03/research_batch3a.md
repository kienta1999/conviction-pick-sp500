# Buy-the-Dip Research Dossier — Batch 3a
**Date:** 2026-08-03
**Tickers:** HOOD (Robinhood Markets), NEM (Newmont)

---

## Methodology & source note (read this first)

The session's web-search quota was exhausted before this run began (200/200 `WebSearch` calls
already consumed), so **no keyword search was available**. All research below was done by
fetching **primary sources directly**:

- SEC EDGAR submissions API and filing archives (`data.sec.gov`, `www.sec.gov/Archives`)
- **HOOD Q2 2026 earnings release** — 8-K exhibit 99.1, accession `0001783879-26-000113`, filed 2026-07-29
- **HOOD Q2 2026 Form 10-Q** — accession `0001783879-26-000114`, filed 2026-07-30 (period ended 2026-06-30)
- **NEM Q2 2026 earnings release** — 8-K exhibit 99.1, accession `0001164727-26-000034`, filed 2026-07-23
- Robinhood newsroom (`robinhood.com/newsroom`)
- stockanalysis.com quote/statistics pages for HOOD, NEM, GLD (market data as of 2026-08-03 close)

**Consequence:** the *financial and legal facts* below are primary-source and high-confidence.
What is weaker is **dated financial-press narrative** — I could not retrieve articles explaining
day-by-day why the stocks sold off, nor the exact date each 52-week high was set. Where I infer
the drawdown driver from filings rather than read it in press coverage, I say so explicitly.
Anything I could not confirm is marked **not found** rather than guessed.

---
---

# HOOD — Robinhood Markets, Inc.

**Screen inputs:** Price $90.34 · mkt cap $81B · −40.7% off 52w high · −8.8% vs 200d SMA ·
−12.3% 12m return · fwd PE 28.4 · trailing PE 40.0 · analyst mean target $119.51 (+32.3%) ·
TTM rev growth 28.2% · op margin 43.9% · ROE 23.6% · net cash $0.98B
**Confirmed 52-week range (2026-08-03):** $63.52 – $153.86. Stock closed **+3.78% on 2026-08-03**.

---

## 1. Why it's down — transitory vs permanent

**The single most important fact: the business did not break. The multiple did.**

Q2 2026, reported **2026-07-29**, was a large beat on essentially every operating line
(source: 8-K Ex-99.1, 2026-07-29):

| Metric | Q2 2026 | YoY |
|---|---|---|
| Total net revenues | **$1.308B** (record) | +32% |
| Transaction revenues | $776M | +44% |
| Net interest revenues | $389M | +9% |
| Other revenues | $143M | +54% |
| Net income | $573M | +48% |
| Diluted EPS | **$0.62** (consensus ~$0.43) | +48% |
| Adjusted EBITDA | $741M | +35% |
| Net Deposits | **$21.7B** (record) | — |
| Total Platform Assets | $369B | +32% |
| Gold Subscribers | **4.8M** (record) | +39% |
| ARPU | $187 | +24% |
| Funded Customers | 28.4M | **+7%** |

So the −40.7% drawdown happened **before** this print, and against improving fundamentals.
Working from the filings, four forces explain it:

**(a) The crypto cycle rolled over — this is the one genuinely deteriorating line.**
From the Q2 release: cryptocurrencies revenue **$100M, down 38% YoY**; **Robinhood App crypto
notional volumes $18B, down 35% YoY** (total crypto notional $40B including $22B from Bitstamp).
The company also states Total Platform Assets growth was "partially offset by **lower
cryptocurrency valuations**." Crypto was the marquee growth engine of the 2025 story and it is
now the only shrinking revenue line. This is a **volume/price cycle**, not an asset impairment.

**(b) A speculative-multiple de-rate, not a HOOD-specific event.** At the $153.86 high the market
cap was roughly $138B on ~$4.9B TTM revenue — about **28x sales**. Today it trades at
**16.47x sales / 33.99x EV/EBITDA** (stockanalysis, 2026-08-03). Corroborating that this was a
broad risk-asset unwind rather than a HOOD problem: **gold is also ~27% off its own 52-week high
over the same window** (GLD $371.71 vs 52w high $509.70). Two utterly unrelated assets both
de-rating ~27–40% points to a market-wide compression of speculative multiples in H1 2026.

**(c) Decelerating user growth.** Funded Customers grew only **+7% YoY to 28.4M**. The story has
shifted from customer acquisition to monetization (ARPU +24%). A market paying 28x sales for a
user-growth story will re-rate hard when user growth prints 7%, even if revenue prints +32%.

**(d) Regulatory overhang on the fastest-growing line.** Event contracts went from nothing to
**$156M of quarterly revenue (up >10x YoY, ~12% of total revenue)** — and are being attacked in
courts in at least a dozen states (detail in §7). The market is discounting a business line that
is simultaneously the biggest growth driver and the biggest legal tail risk.

There is also housekeeping noise: a **reduction in force announced June 2026** (one-time
restructuring charges) and a **CFO transition** (Shiv Verma is now CFO; the release references
"equity modifications of restructuring and executive awards in connection with our CFO
transition"). Post-earnings, **Goldman Sachs cut its target to $118 from $137**.

**VERDICT: TRANSITORY.** Nothing in the 10-Q or the earnings release describes an impaired
franchise. Revenue +32%, record deposits, record Gold subs, record equity/options/event volumes,
13 business lines above $100M annualized, and management *lowered* its 2026 expense outlook
(to $2.675–2.775B from $2.7–2.825B) — the sign of a company with more operating leverage than
expected, not less. The drawdown is (i) a crypto volume trough and (ii) compression of a
euphoric multiple. **The one non-transitory element is the event-contracts legal question**,
which is binary rather than cyclical and is the reason this is not a clean 9/10 setup.

---

## 2. Moat / AI-irreplaceability

**Named moat — four layers, in increasing order of durability:**

1. **Brand + demographic lock with the next generation.** 28.4M funded customers, 29.9M
   investment accounts, and a genuinely differentiated position as the default first brokerage
   for young US investors. Trump Accounts illustrate the reach: **over 7M account sign-ups and
   nearly $1.5B deposited** since the 2026-07-04 launch.
2. **Switching costs, and they are compounding.** Retirement AUC **+82% YoY to $34.5B**, margin
   book **$21.6B**, Gold subscriptions 4.8M, Gold Card 1M+ customers, Robinhood Banking $3B
   deposits with ~40% of those customers on direct deposit, TradePMR at $50B AUM. Every one of
   these is stickier than a brokerage trade. Direct deposit and an IRA are not things a customer
   moves for 3bps.
3. **Regulatory licences — the real barrier.** Broker-dealer, clearing (RHS self-clears), FCM,
   crypto, banking partnerships, MAS capital markets services licence (2026-07-01), CIRO via
   WonderFi in Canada, MiCA/MiFID in the EU. Most decisive: **Rothera, a CFTC-licensed exchange
   *and* clearinghouse** (formerly LedgerX/MIAXdx), run as a JV with Susquehanna, launched June
   2026 with **over 3.5 billion contracts traded to date**. Owning the exchange and the clearing
   layer — not just routing to Kalshi — is a structural, hard-to-replicate asset.
4. **Network/liquidity effects in event contracts.** Prediction markets are a liquidity business:
   the venue with the tightest spreads wins order flow, which tightens spreads. **13.6 billion
   event contracts traded in Q2, up >10x YoY.** Combined with owning Rothera, this is the closest
   thing HOOD has to a true network-effect moat.

**Can AI route around it?** Essentially no — and HOOD is on the right side of this. You cannot
build an AI that is a registered broker-dealer, a self-clearing firm, and a CFTC-licensed
clearinghouse; the binding constraints are regulatory licences, capital, and custody, none of
which AI commoditizes. Retail brokerage commissions were already zero, so AI cannot destroy a
fee that does not exist. More to the point, **HOOD is the one deploying it**: Agentic Trading
launched May 2026 (equities, options, crypto through AI agents), with **~100,000 accounts opened
and over $100M AUC** as of Q2 — AI is a customer-acquisition feature here, not a substitution
threat. Robinhood Chain (an "AI-native" Ethereum L2) is the same bet.

The real threats are **competitive and regulatory, not technological**: Kalshi and Coinbase in
event contracts; Schwab/Fidelity/IBKR in core brokerage; and state gambling law.

**IRREPLACEABILITY SCORE: 7/10.** Licence stack, clearing infrastructure, and compounding
switching costs are genuinely hard to replicate, and AI is an accelerant rather than a solvent.
Held below 8 because a meaningful share of revenue (options, event contracts, crypto) is
*flow* revenue that follows retail risk appetite, and retail risk appetite is not a moat.

---

## 3. Rebound catalyst

**NEXT SCHEDULED EARNINGS DATE: not found.** Q2 2026 was reported **2026-07-29** (already past);
Q3 2026 has not been formally scheduled as of 2026-08-03. Based on HOOD's pattern (Q1 reported
2026-04-28, Q2 on 2026-07-29), **late October / early November 2026 is the likely window** —
treat as an estimate, not a confirmed date.

**Concrete catalysts, roughly in time order:**

- **Immediate (days):** **Robinhood Ventures Fund II (RVII) IPO on the NYSE, expected 2026-08-13
  at ~$25/share.** RVI's deconsolidation already produced a $129M gain in Q2; RVII scales the
  private-markets franchise. The stock rose **+3.78% on 2026-08-03**, the day the RVII offering
  opened to customers.
- **Q3 2026 (now):** Event contracts annualize. Q2 alone was $156M of revenue from a line that
  barely existed a year ago, and **Rothera only launched in June** — Q3 is the first full quarter
  with HOOD capturing exchange *and* clearing economics rather than paying a third-party venue.
  Q2 also included the **2026 FIFA World Cup** contracts (tradable from 2026-06-04); note the
  seasonal cliff risk on the other side of that.
- **Q3–Q4 2026:** **Trump Accounts** compounding — 7M+ sign-ups and ~$1.5B deposited since
  2026-07-04, already contributing to the +54% "other revenues" line. This is a
  government-blessed customer-acquisition channel with essentially zero CAC.
- **H2 2026:** **International inflection.** International Funded Customers crossed **1M** in Q2.
  WonderFi (Canada) closed; Singapore MAS licence granted 2026-07-01; UK crypto approval
  received; perpetual futures live in the EU; Stock Tokens available in 120+ countries via
  Robinhood Wallet. Each is a new revenue pool off a ~1M-customer base against 28.4M in the US.
- **Operating leverage, already guided:** management **lowered and tightened** 2026 Adjusted
  Opex + SBC guidance to **$2.675–2.775B** (from $2.7–2.825B at Q1 on 2026-04-28) *while
  absorbing* two new businesses (Rothera, WonderFi). Revenue +32% against opex guided down is
  the cleanest earnings-upside setup in the file.
- **Buyback:** $414M repurchased in Q2 at ~$94/share average; $1.3B cumulative since Q3 2024 at
  a ~$47 average. Management is buying at these levels.
- **The crypto option:** crypto revenue is down 38% and app volumes down 35%. This line is at or
  near a cyclical trough. Any crypto recovery is pure incremental upside on a cost base that has
  already been reset — and note the *rest* of the business grew 32% with crypto shrinking.

- **Legal catalyst (two-sided):** the **Third Circuit ruled in favor of KalshiEx in April 2026**,
  extending a preliminary injunction against state gaming enforcement. Federal CEA preemption
  winning on appeal is the single biggest de-risking event available to the event-contracts
  thesis, and it has already started going HOOD's way.

---

## 4. Balance-sheet survival

**Not a survival question in any scenario.**

From the Q2 2026 balance sheet (2026-06-30, 8-K Ex-99.1):

| Item | 2025-12-31 | 2026-06-30 |
|---|---|---|
| Cash & cash equivalents | $4,261M | **$5,362M** |
| Cash/securities segregated (customer) | $5,749M | $12,023M |
| Receivables from users, net | $17,994M | $22,799M |
| Securities borrowed | $2,408M | $6,036M |
| Total assets | $38,137M | $56,550M |
| Payables to users | $11,986M | $17,243M |
| Securities loaned | $11,626M | $20,536M |
| **Long-term borrowings** | **$0M** | **$2,170M** |
| Total stockholders' equity | $9,151M | $9,541M |

- **Corporate debt:** zero until June 2026, when HOOD issued **convertible senior notes**
  ($2,170M carrying value). Cash $5,362M − debt $2,170M = **+$3.19B net cash** on the face of
  the balance sheet. *Note the screen's "net cash $0.98B" does not reconcile to this;* the
  screen is presumably netting additional items. Either figure is a comfortable net-cash position.
- **Cash generation:** net cash from operating activities **$720M in Q2 2026** and **$2,758M in
  H1 2026** against H1 net income of $919M — i.e. **CFO ≈ 3.0x net income for the half**.
- **Adjusted EBITDA $741M/quarter** against a fully-guided 2026 opex base of $2.675–2.775B.
- **Accumulated deficit shrank** from $(2,152)M to $(1,241)M in six months.
- Regulatory net capital: RHS is a self-clearing broker-dealer subject to Rule 15c3-1; no capital
  deficiency is disclosed.
- **Legal contingency accrual: only $89M** as of 2026-06-30 (vs $71M at 2025-12-31) — trivial
  against $81B of market cap, and a signal management does not currently view any of the
  litigation in §7 as a probable material loss.

**Rating: very strong.** Net cash, no maturity wall, CFO well above net income, and the only debt
is a convertible issued opportunistically (with $290M of the $414M Q2 buyback executed alongside
it — a standard concurrent-repurchase structure, not distress).

---

## 4b. EARNINGS-QUALITY FLAG — RECEIVABLES_OUTRUN — **VERDICT: BENIGN (explained)**

**The screen flagged:** receivables/revenue divergence **0.820 (very large)**, accrual ratio
**−0.031**, CFO/NI **1.599**.

**One-line verdict: BENIGN — the divergence is a 127% expansion of the margin-lending book plus
securities-borrowed balances, i.e. balance-sheet *lending assets* funded by customer cash, not
uncollected revenue; CFO exceeds net income and the accrual ratio is negative, which is the
mirror image of the value-trap signature.**

**Evidence:**

1. **The company discloses the cause outright.** Q2 2026 release, "Additional Operating Data":
   **"Margin Book increased 127% year-over-year to a record $21.6 billion."** That single line
   accounts for essentially the entire receivables move. Receivables from users, net went
   $17,994M → $22,799M (Dec-25 → Jun-26); securities borrowed went $2,408M → $6,036M.
   Quarter-over-quarter total receivables ran ~$10.1B (Q2 2025) → ~$23.5B (Q2 2026).
2. **For a broker these are assets, not revenue.** Margin loans are *collateralized loans to
   customers*, carried as receivables and earning net interest revenue. They grow when customers
   borrow more, and they scale with platform assets ($369B, +32%) — not with invoices unpaid.
   Revenue growing 32% while a *loan book* grows 127% is mechanically expected and is not an
   accrual.
3. **It is explicitly funded, and the funding is disclosed.** On the liability side over the same
   six months: **securities loaned $11,626M → $20,536M (+$8.9B)** and **payables to users
   $11,986M → $17,243M (+$5.3B)**. The asset growth is matched by customer credit balances and
   securities lending — this is a self-funding broker balance sheet inflating, not a company
   booking sales it cannot collect. Management even describes the deliberate funding shift:
   *"In February 2026, we updated our brokerage High-Yield Cash program to fund growth in margin
   lending, resulting in over $6 billion of Cash Sweep balances that moved to Cash and Deposits."*
   (Cash Sweep −9% to $29.7B; Cash and Deposits +34% to a record $18.7B.)
4. **The cash-flow statement confirms it.** H1 2026 operating section: *Receivables from users,
   net* **−$4,476M** (use of cash) offset by *Securities loaned* **+$8,910M** and *Payables to
   users* **+$5,196M**. Net cash from operations was still **+$2,758M for H1 against $919M of net
   income**. A company whose earnings were running ahead of cash cannot post CFO at 3x NI.
5. **The corroborating ratios point the right way.** Accrual ratio **−0.031** (negative =
   conservative, cash-backed earnings) and **CFO/NI 1.599** (cash *exceeds* earnings). The
   value-trap signature is the opposite: CFO/NI well below 1 with a positive accrual ratio.

**Two genuine earnings-quality caveats that the screen did *not* flag, and that matter more:**

- **~23% of Q2 EPS was a one-off non-cash gain.** Net income of $573M **"included $129 million of
  gains primarily related to the deconsolidation of Robinhood Ventures Fund I,"** equal to
  **$0.14 of the $0.62 diluted EPS**. Clean underlying EPS is therefore ~$0.48 — still a beat vs
  ~$0.43 consensus, but a materially smaller one than the headline suggests. The cash-flow
  statement backs out $106M as a non-cash adjustment.
- **Credit provisioning is rising fast.** Provision for credit losses **$56M in Q2 2026 vs $28M
  in Q2 2025 — doubled YoY**, and $92M for H1 vs $52M. That is the honest cost of a margin book
  up 127% and a credit-card business now over $100M annualized with **$17B+ annualized purchase
  volume**. This is the line to watch: the receivables growth is benign *today* because it is
  collateralized, but a sharp equity drawdown would test both the margin book and the unsecured
  card book at once. Management flags exactly this by excluding "provision for credit losses"
  from its opex guidance.

---

## 5. Margin of safety / valuation — **the weak link**

| Multiple (2026-08-03) | HOOD |
|---|---|
| Trailing P/E | 40.01 |
| Forward P/E | **38.23** (stockanalysis) vs **28.4** (screen) — see note |
| P/S | 16.47 |
| Forward P/S | 13.88 |
| EV/EBITDA | 33.99 |
| Short interest | 38.09M shares, 4.24% of shares out |

**Note the forward-PE conflict:** the screen carries 28.4x, stockanalysis shows 38.23x. I could
not reconcile these without consensus-estimate access — **flagged as unresolved**. The gap is
large enough to matter to the thesis: at 28x this is a reasonable growth multiple; at 38x it is
not. Treat 28.4x as the optimistic case.

**Own multi-year history: not found.** I could not retrieve HOOD's historical average forward P/E
or EV/EBITDA bands (no search access, and the statistics page does not publish historical
averages). What *is* anchored: at the $153.86 high the stock was ~28x sales; it is now 16.5x.

**Peer context:** at ~34x EV/EBITDA and 16.5x sales, HOOD trades at a large premium to
traditional brokers (Schwab, IBKR) — justified in direction by 32% revenue growth, 43.9% op
margins and 23.6% ROE, but the *magnitude* of the premium is the debate.

**Analyst view:** mean target **$119.51 = +32.3% upside**, "Buy" consensus. But targets are being
cut into the strength — **Goldman Sachs to $118 from $137** post-Q2.

**Honest answer: cheaper, but not cheap.** A −40.7% drawdown took HOOD from an indefensible
multiple to a demanding one. There is **no valuation margin of safety here** — the entire return
case rests on the growth continuing (32% revenue growth, opex guided *down*, event contracts and
international compounding). If growth decelerates to 15%, a 34x EV/EBITDA multiple has a very
long way to fall. Contrast with NEM below, where you are paid to wait.

---

## 6. Category position

**#1 and gaining — this is the strongest part of the file.**

Management's claim is aggressive but the disclosed data supports it: *"We delivered record
revenues and drove new highs across equity, option, and event contract volumes, as we continue to
win market share."* (CFO Shiv Verma, 2026-07-29.)

- **Equity notional volumes +85% YoY to a record $956B.** Equities revenue **+95% to $129M**.
  You do not grow equity volumes 85% in a flat tape without taking share.
- **Options contracts traded +50% YoY to a record 774M**; options revenue +29% to $342M.
- **Event contracts +>10x YoY to 13.6B contracts**, $156M revenue — and via Rothera, HOOD now
  owns the exchange and clearinghouse rather than renting them.
- **Robinhood Legend** (active-trader platform) crossed **$100M annualized revenue ~18 months
  after launch** — evidence HOOD is now competing for the *professional-adjacent* trader, the
  segment it historically ceded to IBKR/thinkorswim.
- **13 separate business lines above $100M annualized revenue.** In 2021 this was effectively a
  one-product company (PFOF on equities/options/crypto). That diversification is the answer to
  the old bear case.
- **Pricing power evidence:** ARPU **+24% to $187** while funded customers grew only 7%, and Gold
  adoption hit **17% overall with ~40% of *new* funded customers signing up for Gold**. Customers
  are paying more, voluntarily, for subscriptions.

**Where share is genuinely being lost: crypto.** App crypto notional −35% YoY. Some of that is
the cycle, but Coinbase and offshore/DeFi venues are real competitors, and the response
(Bitstamp, WonderFi, Robinhood Chain, perpetual futures in the EU, Stock Tokens, Robinhood Earn)
is a build-out rather than a defense of the existing US app franchise.

**The one number that argues the dip is a warning: Funded Customers +7%.** The US retail
brokerage TAM for HOOD's core demographic is maturing. Future growth must come from ARPU,
international, and new products — all of which are working, but it is a harder, less automatic
growth engine than adding users.

---

## 7. Value-trap risk — the honest bear case

**1. The event-contracts business could be legislated or litigated out of existence — and it is
now ~12% of revenue and the entire growth narrative.** This is the real risk, and the 10-Q
(filed 2026-07-30) discloses a remarkable volume of active litigation:

- **State of Wisconsin sued RHD, RHM, RHS, Kalshi and Coinbase on 2026-04-23** in Wisconsin state
  court, alleging sports-related event contracts are **illegal sports betting and a public
  nuisance**, seeking declaratory judgment and a permanent injunction.
- **Tribal RICO suits:** Blue Lake Rancheria, Chicken Ranch Rancheria and Picayune Rancheria sued
  in N.D. Cal. (2025) alleging unlawful sports gambling — claims under the **Indian Gaming
  Regulatory Act, tribal gaming ordinances, civil RICO, infringement of tribal sovereignty, and
  the Lanham Act**, seeking treble damages. Preliminary injunction denied; **on appeal to the
  Ninth Circuit**, district case stayed pending that appeal.
- **Consolidated consumer class actions:** three further putative class actions filed in N.D. Cal.
  in **June 2026** (consolidated into four total) alleging sports event contracts are illegal
  gambling under state gambling-loss-recovery acts and consumer-protection acts, seeking treble
  and punitive damages, restitution and disgorgement. Robinhood has moved to compel most
  plaintiffs to arbitration.
- **Six-state "Statute of Anne" gambling-recovery suits** (Georgia, Illinois, Kentucky,
  Massachusetts, Ohio, South Carolina), filed June 2025, seeking recovery of customer gambling
  losses with damage multipliers.
- **Robinhood is suing states pre-emptively** for injunctive relief from gaming-law enforcement:
  Nevada and New Jersey (Aug 2025), Massachusetts (Sep 2025), **Michigan and Washington (March
  2026)** — an expanding, not contracting, front.
- **Massachusetts Securities Division** is examining "the offerings of presidential election and
  sports event contracts."

*The offsetting fact — and it is a big one:* the **CFTC is on Robinhood's side**, having sued
multiple states asserting that the Commodity Exchange Act **preempts** state gambling law
(including a complaint against **Connecticut in April 2026**, in which RHD moved to intervene as
a plaintiff in June 2026). And **in April 2026 the Third Circuit ruled in favor of KalshiEx**,
extending the preliminary injunction. Federal preemption is currently winning. But this is a
**binary legal outcome, not a cyclical one** — no amount of operational execution hedges it.

**2. Other live regulatory matters:**
- **New York AG** investigating brokerage execution quality and "collaring the prices of certain
  trade orders" (ongoing since July 2023).
- **FINRA** enforcement investigation into the **BOATS 24 Hour Market outage of 2024-08-04/05**.
- **FDIC** investigating Electronic Fund Transfer Act compliance.
- **PFOF structural risk:** SEC Rule 605 Order Execution Disclosure Rules **apply to RHF and RHS
  for the first time beginning 2026-08-01** (two days ago). Greater execution-quality
  transparency is a slow-burn threat to PFOF economics, which still underpin the equities and
  options lines. Management explicitly warns 2026 opex guidance excludes "**potential significant
  regulatory matters**" — language repeated twice in the release.

**3. Revenue is pro-cyclical and reflexive.** Transaction revenue (59% of the total) is a
leveraged bet on retail risk appetite. Net interest revenue (30%) is a leveraged bet on rates
*and* margin balances — and management already flagged **"lower short-term interest rates"** as a
Q2 headwind. In a genuine bear market you lose transaction revenue, net interest revenue,
platform assets and margin balances **simultaneously**, while the credit-loss provision (already
doubled YoY) spikes. The business has never been tested through a real recession at this size.

**4. Valuation offers no protection.** 34x EV/EBITDA and 16.5x sales after a 41% decline means
the stock can fall another 40% and still not be statistically cheap. There is no asset value,
no dividend, and no book-value floor to catch it — equity is $9.5B against an $81B market cap.

**5. Growth-quality erosion.** Funded customers +7%; $0.14 of $0.62 EPS from a one-off
deconsolidation gain; a June 2026 RIF; a CFO transition. None is damning alone; together they
describe a company transitioning from hypergrowth to execution — a phase in which multiples
usually compress further.

**What would make this a true falling knife:** an adverse Ninth Circuit ruling (or a Supreme
Court split) killing federal preemption for sports event contracts, arriving at the same time as
a crypto winter extension and a retail risk-off cycle. That combination removes the growth line,
the crypto line and the transaction line at once — against a 34x multiple.

---

## 8. Rebound score & verdict

### **REBOUND SCORE: 7.0 / 10**

**Verdict:** A high-quality, genuinely-winning franchise whose 41% drawdown is a
multiple de-rate plus a crypto-volume trough rather than a broken story — record revenue,
record deposits, record Gold subs and *lowered* expense guidance prove the business is
compounding — but it earns a 7 rather than a 9 because at 34x EV/EBITDA there is no valuation
cushion, and the fastest-growing line is the subject of active litigation in a dozen states
whose outcome is binary and outside management's control.

**Scoring logic:** business quality and catalysts argue 8.5–9 (32% revenue growth, 43.9% op
margins, net cash, buybacks at $94, opex guided down, six distinct catalysts inside 6 months).
Deducted ~1.5 points for the absence of any margin of safety, and ~0.5 for the event-contracts
legal tail. Upgrade to 8+ on a favorable Ninth Circuit preemption ruling or evidence the crypto
line has troughed; downgrade to 5 if funded-customer growth goes negative or credit provisions
keep doubling.

---
---

# NEM — Newmont Corporation

**Screen inputs:** Price $95.37 · mkt cap $100B · −27.4% off 52w high · −8.2% vs 200d SMA ·
**+55.2% 12m return** · fwd PE 9.0 · trailing PE 12.0 · analyst mean target $129.27 (+35.5%) ·
TTM rev growth 22.5% · op margin 51.6% · ROE 25.9% · net cash $3.41B · net debt/EBITDA −0.20 ·
FCF $8.82B
**Confirmed 52-week range (2026-08-03):** $63.13 – $134.88. Stock closed **+1.77% on 2026-08-03**.

---

## 1. Why it's down — transitory vs permanent

**Answer: it is down because gold is down, almost exactly 1-for-1. This is not a company problem.**

The cleanest evidence in this entire dossier:

| | Off 52-week high |
|---|---|
| **Gold (GLD proxy)** — $371.71 vs 52w high $509.70 | **−27.1%** |
| **NEM** — $95.37 vs 52w high $134.88 | **−29.3%** (screen: −27.4%) |

NEM's drawdown tracks the metal's drawdown almost perfectly. For a gold miner with 51.6%
operating margins and net cash, that is the definition of a **price-driven, non-company-specific**
decline.

**The gold path, from NEM's own realized prices** (Q2 2026 release, 2026-07-23):

| | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY25 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|---|
| Avg realized gold ($/oz) | 2,944 | 3,320 | 3,539 | 4,216 | **3,498** | **4,900** | **4,414** |

Gold peaked in **Q1 2026** (NEM realized **$4,900/oz**, with spot peaking around **$5,400–5,500/oz**
implied by GLD's $509.70 high), then corrected to **$4,414/oz realized in Q2 2026** (−$486/oz QoQ)
and sits **near $4,000/oz today** (GLD $371.71; press commentary describes gold as "range-bound
near $4,000"). So the correction has run roughly **two quarters, from Q1 2026 to now, ~−27%**.

**Critical framing: gold at ~$4,000 is still enormously profitable for NEM.** It is +14% above
the FY2025 average realized price of $3,498 and +36% above Q1 2025's $2,944. NEM is not
correcting into distress; it is correcting from euphoria back to still-excellent.

**Is any of it NEM's own execution?** Partly, and honestly:

- **Cadia seismic events in April 2026** caused downtime — copper production fell 43% QoQ to
  17kt, gold production dipped, and AISC absorbed "incremental costs incurred at Cadia during the
  downtime." **Operations returned to normal by mid-June 2026.** Clearly transitory, and disclosed.
- **Cost inflation is real.** Gold **by-product AISC jumped 58% QoQ to $1,621/oz** in Q2. That
  headline overstates it — by-product AISC is distorted by co-product credits, and Q1's $1,029/oz
  was flattered by high silver/copper credits. The cleaner series is **gold co-product AISC:
  $1,609/oz FY2025 → $1,709 Q1'26 → $1,938 Q2'26**, YTD $1,822. That is **~13% real cost
  inflation YTD** — driven by higher Ghana royalties (a full quarter of the increase), higher
  diesel prices, lower co-product volumes and lower silver pricing. Real, but management states
  **"year-to-date costs tracking well below Newmont's full year cost guidance."**
- **Production is declining by plan:** FY2025 was 5.89Moz; **FY2026 guidance is 5.3Moz** (−10%).
  H1 2026 delivered 2.59Moz (1.30 + 1.29), so H2 must deliver **2.71Moz** — a ~5% step-up per
  quarter — to hit guidance. Management says **"on track"**, but this is the number to watch.

**VERDICT: TRANSITORY — and arguably not a "dip" at all.** This is a **~27% pullback within a
powerful uptrend**: the stock is **+55.2% over 12 months** and +52.4% over 52 weeks. Nothing is
impaired: production guidance reaffirmed, record Q2 free cash flow, net cash rising, buyback
accelerating. The drawdown is a **commodity-price mean-reversion after a parabolic move**, plus a
one-quarter seismic event that has already resolved. The honest caveat: because the cause is the
gold price, the *recovery* also depends on the gold price — NEM has no control over the variable
that caused the decline.

---

## 2. Moat / AI-irreplaceability

**Named moat: irreplaceable physical orebodies + capital intensity + permitting/social licence.
This is the strongest structural moat in this dossier — with one large asterisk.**

- **Tier-1 orebodies cannot be manufactured, relocated, or invented.** NEM's managed portfolio
  (Cadia, Boddington, Lihir, Peñasquito, Ahafo, Yanacocha, Red Chris) plus non-managed interests
  (**Nevada Gold Mines 38.5%**, **Pueblo Viejo 40%**, **Lundin Gold / Fruta del Norte 32%**) is
  the largest collection of long-life, low-cost gold assets on earth. There is no substitute
  good. You cannot make more of a Tier-1 deposit.
- **Permitting and social licence are a decade-scale barrier — and NEM has just demonstrated it.**
  The Q2 release highlights **regulatory approvals from British Columbia for the Red Chris Block
  Cave project, including an amended Environmental Assessment Certificate achieved through a
  consent-based process with the Tahltan Nation**, plus an amended Mines Act permit. That kind of
  indigenous-consent-based approval takes years and cannot be bought or accelerated. It is a moat
  against *new entrants* specifically.
- **Capital intensity:** $1.95B sustaining capital and $1.4B development capital budgeted for
  2026 alone. Few entities on earth can fund that.
- **Scale in a scarce commodity:** ~5.3Moz/year of attributable production.

**Can AI route around it?** **No — this is the most AI-proof asset class available.** AI cannot
synthesize gold, cannot conjure a new Tier-1 orebody, cannot shorten a 10–20 year permitting
cycle, and cannot substitute for the physical monetary/jewellery/central-bank demand that sets
the gold price. If anything the causality runs the other way: AI-driven fiscal expansion, energy
demand and geopolitical instability are *supportive* of gold. AI's effect on NEM is a modest
**cost tailwind** (autonomous haulage, predictive maintenance, ore-sorting, grade control), not a
disruption threat.

**THE ASTERISK — and it is important:** an irreplaceable asset is *not* the same as pricing power.
**NEM is a pure price-taker.** It sells an undifferentiated global commodity at a price set by
macro forces it cannot influence. Its "moat" protects *margins per ounce relative to other
miners* and protects against new supply — it does **not** protect revenue. That is precisely why
the stock fell 27% while executing well.

**IRREPLACEABILITY SCORE: 9/10.** The physical assets are as close to irreplaceable as anything
in the S&P 500 and are structurally immune to AI substitution. Docked one point solely because
zero pricing power means irreplaceability does not translate into revenue control.

---

## 3. Rebound catalyst

**NEXT SCHEDULED EARNINGS DATE: not found.** Q2 2026 was reported **2026-07-23** (already past).
Q3 2026 is not yet formally scheduled as of 2026-08-03; NEM's pattern (Q1 call ~2026-04-23,
Q2 on 2026-07-23) points to **late October 2026** — an estimate, not confirmed.

**Confirmed, dated catalysts:**

- **The buyback is large, active and accelerating.** **$1.7B of stock repurchased since the
  2026-04-23 earnings call, including over $600M in July 2026 alone.** **$4.3B remains of a $6B
  authorization**, and management "intends to request additional approval from its Board as the
  current authorization approaches completion." Since **February 2024 NEM has retired more than
  100 million shares, ~9% of shares outstanding.** At a $100B market cap, $600M/month is roughly
  **7% of market cap annualized** being bought back — into the dip.
- **Total shareholder returns of $1.9B since the last earnings call** (buybacks + dividends).
- **Dividend:** **$0.26/share declared for Q2 2026, payable 2026-09-28 to holders of record
  2026-09-03** = $1.04 annualized, 1.09% yield. Structurally designed to **grow per share
  without increasing cash outlay**, because buybacks shrink the count — the annual per-share
  target is reset each February.
- **H2 2026 production step-up.** Guidance of 5.3Moz requires 2.71Moz in H2 vs 2.59Moz in H1.
  With **Cadia back to normal levels as of mid-June 2026** after the April seismic events, and
  Peñasquito/Ahafo South/Yanacocha grade sequencing normalizing, H2 should mechanically produce
  more ounces at better unit costs. **Operational leverage on the way up.**
- **Costs already tracking favorably:** management states YTD costs are "tracking **well below**
  Newmont's full year cost guidance" — setting up a possible cost beat.
- **Red Chris Block Cave FID.** BC approvals now secured (amended EA Certificate + Mines Act
  permit); the project "advances toward a final investment decision." An FID announcement is a
  discrete, dateable catalyst for the growth profile.
- **Gold itself.** With gold "range-bound near $4,000" and consolidating rather than collapsing,
  any resumption of the uptrend flows almost entirely to the bottom line: at ~1.2Moz of quarterly
  sales, **every $100/oz on the gold price is roughly $120M of quarterly pre-tax income.**
- **Balance-sheet optimization:** management targets a $1B net cash position (±$2B) and a $5B
  minimum cash balance; sitting at **$9.0B cash / $3.4B net cash**, NEM is explicitly *above* its
  own target — i.e. it has stated excess capital to deploy into more buybacks or debt reduction.

---

## 4. Balance-sheet survival

**Fortress. The strongest balance sheet in this dossier by a wide margin.**

From the Q2 2026 release (2026-06-30):

- **Cash and cash equivalents: $9.0B**
- **Total liquidity: $13.0B** (including $4.0B available on the revolving credit facility)
- **Net cash position: +$3.4B** — confirms the screen's $3.41B exactly
- **Net debt/EBITDA: −0.20** (negative; the screen figure is consistent with net cash)
- Stated policy: **maintain a minimum $5B cash balance through the cycle**, anchored to a $1B net
  cash target with ±$2B flexibility

**Cash generation:**

| ($M) | Q1'26 | Q2'26 | H1'26 | FY2025 |
|---|---|---|---|---|
| Net cash from operating activities | 3,785 | **2,924** | **6,709** | 10,334 |
| Capital expenditures | 641 | 719 | 1,360 | 3,035 |
| **Free cash flow** | 3,144 | **2,205** (record Q2) | **5,349** | **7,299** |
| Adjusted EBITDA | 5,154 | 3,757 | 8,911 | 13,480 |

- **TTM FCF from the disclosed quarters** (Q3'25 1,571 + Q4'25 2,813 + Q1'26 3,144 + Q2'26 2,205)
  = **$9.73B**. *The screen carries $8.82B*; the difference is presumably a definitional one
  (capitalized interest treatment). **Either figure is extraordinary** against a $100B market cap
  — roughly a **9–10% free cash flow yield**.
- Q2 working capital was only a **$90M net use of cash**, including $249M of previously-accrued
  reclamation spend and $131M of inventory/stockpile builds, offset by **$461M of favorable
  accounts-receivable movements** (Peñasquito, Cadia). Clean, unremarkable working capital.
- Income and mining cash taxes paid **$1.1B in Q2** — NEM is a large cash taxpayer, i.e. the
  earnings are real and being collected by governments in cash.

**Downside stress:** at YTD co-product AISC of ~$1,822/oz and gold at ~$4,000/oz, the cash margin
is still **~$2,180/oz**. On 5.3Moz that is **~$11.5B of annual gross cash margin** against
~$3.35B of total capex. **Gold would need to fall below roughly $2,000/oz — a further ~50%
decline — before NEM's sustaining economics came under real pressure.** With $9B of cash and no
net debt, survival is not a question that needs asking.

---

## 5. Margin of safety / valuation — **genuinely cheap**

| Multiple (2026-08-03) | NEM |
|---|---|
| Trailing P/E | 12.07 |
| Forward P/E | 9.0 (screen) / 9.34 (stockanalysis) |
| **EV/EBITDA** | **5.83** |
| **P/FCF** | **10.32** |
| Dividend yield | 1.09% ($1.04/share) |
| Short interest | 19.92M shares, **1.89%** of shares out (very low) |

**Own multi-year history: not found** (could not retrieve NEM's historical forward-P/E band
without search access). **Peer comparison: not found** — I could not pull Barrick/Agnico/AngloGold
multiples. Both are gaps; flagging honestly rather than guessing.

**What I can assert with confidence:** **EV/EBITDA of 5.83 with a net cash balance sheet is cheap
in absolute terms for any business**, let alone one running a 51.6% operating margin and a 25.9%
ROE. A ~10x P/FCF (≈10% FCF yield) on $9.7B of TTM free cash flow, with ~7% of market cap being
retired annually via buyback, is a legitimate margin of safety. **You are paid to wait here.**

**The honest caveat on that 9x forward P/E — it is flattered by H1.** H1 2026 adjusted EPS was
**$5.01** ($2.90 Q1 + $2.10 Q2), but Q1 was earned at **$4,900/oz** and Q2 at **$4,414/oz**, while
gold is now **~$4,000/oz**. Rough sensitivity: ~1.2Moz of quarterly sales × $400/oz lower
realization ≈ $480M pre-tax ≈ ~$0.32/share per quarter. So a *spot-gold* run-rate is closer to
**~$1.75–1.85 adjusted EPS per quarter**, or **~$7.00–7.40 annualized** — implying a
**run-rate P/E nearer 13x, not 9x**, at $95.37. FY2026 as reported will land between the two
(H1 $5.01 actual + H2 at spot ≈ $3.7 → ~$8.7, i.e. ~11x).

**Conclusion: genuinely cheap, but not as cheap as the 9x headline implies.** The forward P/E
embeds either a gold recovery or the H2 production step-up (or both). The more robust cheapness
signals are the ones that do not depend on an EPS estimate: **5.83x EV/EBITDA and ~10x P/FCF with
$3.4B of net cash.** Analyst mean target **$129.27 = +35.5% upside** (22 analysts, "Buy"), with
post-earnings targets in a $124–$175 range. Very low short interest (1.89%) means there is no
crowded-short setup to squeeze — but equally, no bear consensus to fight.

---

## 6. Category position

**#1 in the category, decisively — but the category confers no pricing power.**

- **Largest gold producer in the world**, ~5.3Moz attributable in 2026, with the deepest Tier-1
  asset base (Cadia, Boddington, Lihir, Peñasquito, Ahafo, Yanacocha, Red Chris, plus 38.5% of
  Nevada Gold Mines, 40% of Pueblo Viejo, 32% of Lundin Gold).
- **Cost position is competitive**, not best-in-class: FY2025 gold co-product AISC $1,609/oz,
  YTD 2026 $1,822/oz. For reference, non-managed **NGM ran $1,805/oz AISC** and **CAS of
  $1,473/oz** in Q2 2026 — NEM's managed portfolio is broadly in line with the industry's best
  joint venture.
- **The dip is emphatically *not* a share-loss signal.** Production guidance of 5.3Moz was
  **reaffirmed**; costs are tracking **below** guidance YTD; Q2 free cash flow was a **record for
  a second quarter**; and the company is buying back stock at a $600M/month pace. Nothing here
  looks like a company losing position.
- **Portfolio is being high-graded, not shrunk in distress.** The FY2025 5.89Moz → FY2026 5.3Moz
  decline reflects divestitures and planned mine sequencing following the Newcrest integration,
  not asset failure — Newmont is deliberately concentrating on Tier-1 assets rather than
  maximizing ounces.
- **Capital-allocation discipline is genuinely differentiated.** A published, repeatable framework
  (sustaining capital → sustainable dividend → disciplined development capital → optimized
  capital structure → ratable buyback), a dividend engineered to grow per share without growing
  the cash commitment, and **>100M shares (~9%) retired since February 2024.** Gold miners have
  historically destroyed capital in exactly this part of the cycle by chasing acquisitions at the
  top; NEM is buying its own stock instead. That is the single most encouraging governance fact
  in this file.

**No pricing power, by definition.** NEM sells a fungible global commodity at the spot price. Its
"category position" translates into cost advantage, asset longevity and optionality — never into
the ability to raise price.

---

## 7. Value-trap risk — the honest bear case

**1. The obvious one: this is a leveraged bet on the gold price, and gold just broke a parabola.**
Gold ran from ~$2,944/oz realized (Q1 2025) to ~$5,400–5,500/oz spot (Q1 2026) — an ~85% move in
twelve months. That is a parabolic advance, and parabolas usually correct *further and longer*
than the first 27%. If gold mean-reverts toward $3,000/oz, NEM's adjusted EPS roughly halves
again and the "cheap" 12x trailing P/E becomes ~25x on collapsed earnings. **Every bull point in
this write-up is downstream of the gold price**, and NEM controls none of it.

**2. "It's +55% in 12 months" — this may not be a dip at all.** Unlike HOOD (−12.3% over 12m,
i.e. a genuine round-trip), NEM is **up 52–55% over the last year** and only 8.2% below its 200d
SMA. Buying here is not buying a beaten-down asset; it is **buying a pullback in a strong
uptrend after a parabolic run**. If the screen's premise is "quality that has been unfairly
discarded," NEM does not really fit — it has been *rewarded*, and is merely giving some back. The
risk of buying the first 27% off a parabolic top is well documented.

**3. Cost inflation is real and it compresses the margin.** Gold co-product AISC: **$1,609/oz
FY2025 → $1,709 Q1'26 → $1,938 Q2'26**. Named drivers include **increased Ghana royalties** (a
sovereign, permanent step-up, not a cycle), **higher diesel prices**, and lower co-product
credits. Gold miners are notorious for letting costs inflate to absorb the gold price — margins
compress on the way up *and* on the way down. If gold sits at $4,000 while AISC keeps climbing
toward $2,100, the FCF story degrades quickly.

**4. Production is *declining*, and the H2 guidance needs a step-up.** 5.89Moz (FY25) → 5.3Moz
(FY26 guidance) is a 10% decline. H1 delivered 2.59Moz, so H2 must deliver **2.71Moz** — about
5% more per quarter than either Q1 or Q2 achieved. Management says "on track," but a miss here
would be the first crack in the execution story and would hit at the same time as lower realized
prices. **This is the single most checkable near-term risk.**

**5. Operational/geological risk is chronic and unhedgeable.** The **April 2026 Cadia seismic
events** cut copper production 43% QoQ and inflated AISC for a full quarter. That is the *normal*
run-rate of surprise in large-scale block-cave and open-pit mining — Peñasquito grade
variability, Lihir processing, Yanacocha reclamation, and the **$249M of reclamation cash spend
in Q2 alone** are all recurring. Reclamation and closure liabilities are a structural, permanent
cash drag that never appears in AISC headlines.

**6. Jurisdictional and sovereign risk.** Ghana (royalty increase already imposed), Peru
(Yanacocha), Mexico (Peñasquito), Papua New Guinea (Lihir), Argentina, Dominican Republic,
Australia, Canada. Resource nationalism rises precisely when metal prices are high — the Ghana
royalty step-up is the template, and there is no reason to expect it to be the last.

**7. The structural bear case on the sector: gold miners chronically fail to convert gold-price
upside into shareholder returns.** Decades of evidence show the sector dilutes, overpays for
M&A at cycle peaks, and lets costs inflate. NEM's current capital allocation is the *opposite* of
that (9% of shares retired, disciplined capex) — but the risk is that a new management team
(**Natascha Viljoen is President & CEO**, with "key executive appointments" announced in Q2 2026)
reverts to type and does a large acquisition instead of buying back stock.

**What would make this a true falling knife:** gold retracing to $3,000/oz while AISC holds above
$1,900/oz and NEM misses the 5.3Moz guidance — margin compression, volume decline and multiple
compression simultaneously. Note this is a *lower-probability but structurally real* scenario;
unlike HOOD's binary legal risk, it is continuous and would be visible quarter by quarter.

---

## 8. Rebound score & verdict

### **REBOUND SCORE: 7.5 / 10**

**Verdict:** The highest-quality *setup* in this pair — a 27% drawdown caused almost entirely by
a 27% gold correction rather than by anything Newmont did wrong, against reaffirmed 5.3Moz
guidance, record second-quarter free cash flow of $2.2B, $3.4B net cash, a ~10% FCF yield and a
buyback retiring roughly 7% of market cap annually — but it scores 7.5 rather than 9 because it
is a pullback in a +55% uptrend rather than a true dip, and because the entire recovery thesis
depends on a gold price that Newmont cannot influence.

**Scoring logic:** valuation, balance sheet, capital allocation and asset quality argue 8.5–9
(5.83x EV/EBITDA, net cash, $9.7B TTM FCF, 9% of shares retired since Feb 2024, moat 9/10).
Deducted ~1 point because the drawdown driver is exogenous and could easily extend — parabolas
rarely bottom 27% down — and ~0.5 for the real cost inflation (co-product AISC $1,609 → $1,822
YTD) and the H2 production step-up that guidance still requires. Upgrade to 8.5 if gold holds
$4,000 and Q3 shows the production step-up; downgrade to 5.5 if gold breaks below $3,500 or Q3
production comes in below ~1.35Moz.

---
---

# Two-ticker comparison

| | **HOOD** | **NEM** |
|---|---|---|
| Price / mkt cap | $90.34 / $81B | $95.37 / $100B |
| Off 52w high | −40.7% ($153.86 high) | −27.4% ($134.88 high) |
| 12-month return | **−12.3%** (real round-trip) | **+55.2%** (pullback in uptrend) |
| Cause of drawdown | Multiple de-rate + crypto volume trough | Gold −27% from a parabolic peak |
| Temporary vs permanent | **Transitory** (legal tail is the exception) | **Transitory** (but exogenous) |
| Moat type | Licences, clearing infra, switching costs, network effects | Irreplaceable Tier-1 orebodies, permitting, capital intensity |
| **Irreplaceability** | **7 / 10** | **9 / 10** |
| Pricing power | **Yes** — ARPU +24%, Gold at 17% adoption | **None** — pure price-taker |
| Growth | Revenue **+32% YoY**, 13 lines >$100M | Production **−10%** (5.89 → 5.3Moz guided) |
| EV/EBITDA | **33.99** | **5.83** |
| P/FCF | not found | **10.32** |
| Balance sheet | Net cash ~$3.2B (post-convert), CFO 3.0x NI H1 | Net cash **$3.4B**, $9.0B cash, $13.0B liquidity |
| TTM FCF | not found | **~$9.7B** (screen: $8.82B) |
| Shareholder return | $414M buyback in Q2 @ ~$94 | **$1.9B** returned since April; ~9% of shares retired since Feb-24 |
| Dividend | None | $1.04/yr, 1.09% yield |
| Margin of safety | **None** — cheaper, not cheap | **Yes** — ~10% FCF yield, 5.8x EBITDA |
| Analyst upside | +32.3% (to $119.51) | +35.5% (to $129.27) |
| Short interest | 4.24% | 1.89% |
| Key risk | **Binary**: event-contract gambling litigation across ~12 states | **Continuous**: gold price + cost inflation + H2 volume step-up |
| Last reported | **2026-07-29** (big beat) | **2026-07-23** (beat, guidance reaffirmed) |
| Next earnings | not found (~late Oct 2026 est.) | not found (~late Oct 2026 est.) |
| **Rebound score** | **7.0 / 10** | **7.5 / 10** |

**Which is the better buy-the-dip candidate?**

**NEM edges it, on margin of safety and asset quality.** The two names have almost identical
analyst-implied upside (+32% vs +36%), but they are opposite kinds of bet:

- **NEM is the *value* dip.** You are buying a fortress balance sheet at 5.8x EBITDA and a ~10%
  FCF yield, where the operator is demonstrably executing (guidance reaffirmed, costs below
  guidance, record Q2 FCF) and is retiring ~7% of the market cap per year into the weakness. If
  gold merely stays flat at $4,000, you still earn a double-digit FCF yield and a shrinking share
  count. **The downside is protected by assets, cash and buyback.**
- **HOOD is the *growth* dip.** You are buying a franchise that is unambiguously winning share
  (equity volumes +85%, options +50%, event contracts +10x, revenue +32%, opex guided *down*) at
  a price that still requires all of that to continue. **There is no downside protection at all** —
  no dividend, no asset value, $9.5B of book against $81B of cap, and 34x EV/EBITDA.

**The decisive distinctions:**

1. **Is it actually a dip?** HOOD yes (−12.3% over 12m — a genuine round-trip from a euphoric
   peak). NEM, honestly, no — it is +55% over 12 months and merely 8.2% below its 200d SMA. If
   the mandate is strictly "quality that has been discarded," **HOOD fits the *screen's* premise
   better**; if the mandate is "best risk-adjusted forward return," NEM does.
2. **Risk shape.** HOOD's principal risk is **binary and legal** — a single adverse appellate
   ruling on CEA preemption could impair the fastest-growing 12% of revenue overnight, and no
   operational excellence hedges it. NEM's principal risk is **continuous and observable** — the
   gold price, watchable daily, with cost and volume checkpoints each quarter. Continuous,
   monitorable risk is more manageable than binary legal risk in a rules-based process.
3. **Earnings quality.** Both clear. HOOD's RECEIVABLES_OUTRUN flag resolves **benign** (margin
   book +127% to $21.6B, funded by securities loaned and customer credit balances; CFO/NI 1.599;
   negative accrual ratio) — though note $0.14 of the $0.62 Q2 EPS was a one-off deconsolidation
   gain, and credit provisions doubled YoY. NEM's earnings are cash-backed and heavily
   cash-taxed ($1.1B paid in Q2 alone).

**If forced to hold only one for a 12-month rebound: NEM**, because you are paid a ~10% FCF yield
and a 7%-of-cap buyback to wait, with a genuine asset floor beneath you. **If holding both:** they
are close to uncorrelated — HOOD is a leveraged bet on retail risk *appetite*, NEM a leveraged bet
on the hedge *against* risk appetite. That pairing is a feature, not a redundancy, and each hedges
the other's worst scenario.

---

## Open items / could not confirm (honest gaps)

- **Next scheduled earnings dates for both** — not announced as of 2026-08-03; late-October
  estimates are inferred from prior-quarter cadence, not confirmed.
- **Exact dates of each 52-week high** — not found (no search access; statistics pages omit dates).
  NEM's peak is inferable as Q1 2026 from realized gold prices; HOOD's is not.
- **HOOD forward P/E is contradictory**: 28.4x (screen) vs 38.23x (stockanalysis). Unresolved and
  material to the valuation conclusion.
- **Multi-year historical valuation bands** for both, and **direct peer multiples** (Schwab/IBKR
  for HOOD; Barrick/Agnico/AngloGold for NEM) — not retrievable without search.
- **Q3/Q4 2025 quarterly revenue for HOOD** — not pulled, so TTM revenue (~$4.9B) is implied from
  the 16.47 P/S ratio rather than summed from filings.
- **NEM TTM FCF discrepancy**: $9.73B summed from disclosed quarters vs $8.82B in the screen —
  likely a capitalized-interest definitional difference, not reconciled.
- No earnings-call transcripts were read for either name (only the press releases and the 10-Q);
  management Q&A commentary on crypto outlook and gold hedging policy is therefore missing.
