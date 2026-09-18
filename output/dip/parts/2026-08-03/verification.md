# Fact Verification — DIP writeup claims
**Verification date:** 2026-08-03
**Method:** primary sources only — SEC EDGAR filings/exhibits (curl), SEC.gov statements, FDA De Novo database, PJM Inside Lines, stockanalysis.com. No WebSearch used.

## Scorecard

| # | Claim | Verdict |
|---|---|---|
| 1 | BR raised FY26 guidance at Q3 FY26 | **CONFIRMED** |
| 2 | BR closed-sales guidance cut | **CONFIRMED w/ one wrong number** (pipeline stat UNVERIFIED) |
| 3 | BR reports Q4 FY26 Aug 4, 2026 BMO | **CONFIRMED** (FY27 guide = inference) |
| 4 | BR fwd P/E ~15.1 vs 10-yr avg 30.85 / trough 21.93 | **PARTIALLY CONFIRMED — numbers differ, method flawed** |
| 5a | BR live with on-chain governance for tokenized equities | **CONFIRMED** |
| 5b | SEC affirmed tokenized securities = same obligations | **PARTIALLY CONFIRMED — overstated ("SEC" = one Commissioner)** |
| 6a | VST trailing FCF ~+$1.8B (OCF $4,670M, capex $2,867M) | **CONFIRMED EXACTLY** |
| 6b | VST total debt ~$19.9B gross, net ~$19.28B, lev 2.5–2.8x | **CONTRADICTED** |
| 7 | PJM auction: ~525 MW new supply at $325/MW-day cap | **CONFIRMED EXACTLY** |
| 8 | VST next earnings Aug 7, 2026 | **CONFIRMED** |
| 9 | ISRG Q2: $2.89B/+19%, EPS $2.80/+28%, guide 13.5–15.5%, stock −11.6% | **CONFIRMED except the drop — actual −14.15%** |
| 10 | J&J OTTAVA FDA De Novo Jul 22, 2026 | **CONFIRMED — decision date is Jul 21, 2026** |
| 11a | ISRG da Vinci installed base ~11,710 | **CONFIRMED EXACTLY** |
| 11b | ISRG recurring revenue ~85% | **UNVERIFIED — disclosed floor is 76.3%** |

---

# BR — Broadridge Financial Solutions

**Source of record:** SEC 8-K filed 2026-04-30, accession 0001383312-26-000013, Exhibit 99.1
`https://www.sec.gov/Archives/edgar/data/1383312/000138331226000013/ex991earningsrelease3q2026.htm`
Dated NEW YORK, April 30, 2026.

## Claim 1 — guidance RAISED at Q3 FY26 → **CONFIRMED**

Press release headline verbatim: *"Raising FY'26 guidance for Recurring revenue growth constant currency to At or above 7% and Adjusted EPS growth to 10-12%."*

Guidance table in the release:
- Recurring revenue growth cc: **At or above 7%** — "Raised from higher end of 5 - 7%" ✓
- Adjusted EPS growth: **10 - 12%** — "Raised from 9 - 12%" ✓
- Adjusted Operating income margin: 20 - 21% — No Change

Q3 FY26 actuals:
- Recurring revenues **$1,288M** (claim said $1.29B ✓), +7% reported, **+6% constant currency** ✓
- Adjusted EPS **$2.72**, **+11%** vs $2.44 ✓
- (Also: total revenue $1,954M +8%; diluted GAAP EPS $2.36 +15%)

**The "down against rising guidance" framing holds.** Corroborating price data (stockanalysis, Aug 3 2026 close): BR $157.34, 52-week range $133.83–$271.91 → **~42% off the 52-week high**; market cap $18.20B, **−37.2% y/y**. BR also appears in a MarketWatch piece "20 stocks in the S&P 500 that plunged the most in 2026's first half."

CEO Tim Gokey quote available for the writeup: *"Broadridge is on track to deliver another year of strong financial performance... we are set to deliver on our long-term targets for top- and bottom-line growth for the three-year period ending in fiscal 2026."*

## Claim 2 — closed sales CUT → **CONFIRMED, but one number is wrong**

Confirmed from the same release:
- Closed sales guidance **$240 - $290M** ✓ — but **"Revised from $290 - $330M"**, NOT $290–$340M.
  → **Correct the writeup: the old range was $290–$330M.**
- YTD (nine-month) closed sales **$147M**, **−16%** y/y (vs $174M) ✓
- Q3 standalone closed sales $58M, −19% y/y (vs $71M) — extra detail, not claimed

**UNVERIFIED:** the pipeline >$1B (+20% y/y) and deal origination +25% figures do **not** appear anywhere in the earnings press release. These are almost certainly from the Q3 FY26 earnings call, which I could not retrieve within budget. **Do not present these as filed figures** — attribute to "management commentary on the Q3 call" or drop them.

## Claim 3 — Q4 FY26 on Aug 4, 2026 BMO → **CONFIRMED**

Two independent sources:
1. Broadridge PR, **July 21, 2026** (PRNewswire): *"Broadridge Schedules Webcast and Conference Call to Review Fourth Quarter and Fiscal Year 2026 Results on August 4, 2026"* — "scheduled to release its financial results for the fourth quarter and fiscal year 2026 on Tuesday, August 4, 2026."
2. stockanalysis.com/stocks/br/statistics (retrieved 2026-08-03): *"The next confirmed earnings date is Tuesday, August 4, 2026, **before market open**."*

**Timing note: this is TOMORROW.** The writeup is being published the day before the catalyst.

**"Carries initial FY27 guidance" — not independently confirmed.** This is an inference from Broadridge's consistent practice of issuing initial full-year guidance with the Q4/FY print. High confidence but flag as expectation, not fact.

## Claim 4 — valuation → **PARTIALLY CONFIRMED; numbers differ and the comparison is apples-to-oranges**

Actual, as of **Aug 3, 2026 close ($157.34)**, per stockanalysis.com/stocks/br/statistics:
- **Forward P/E = 15.77** (claim said ~15.1 — close but **not exact**; at the Jul 31 close of $153.95 it would have been ~15.4)
- Trailing P/E = 16.82
- P/FCF 13.82, EV/EBITDA 12.09, PEG 1.97

**10-year average P/E of 30.85 and 10-year trough of 21.93: UNVERIFIED.** Only 5 fiscal years of ratio history are available free. What I could confirm (stockanalysis.com/stocks/br/financials/ratios, fiscal-year-end snapshots):

| FY | Trailing P/E | Forward P/E |
|---|---|---|
| Current (Aug '26) | **16.82** | **15.77** |
| FY2025 | 34.23 | 27.57 |
| FY2024 | 33.62 | 24.04 |
| FY2023 | 31.25 | 22.91 |
| FY2022 | 31.33 | 20.79 |
| FY2021 | 34.74 | 26.37 |

5-year average trailing P/E = **33.0**, so a 10-year average of ~30.85 is plausible and consistent. No fiscal-year-end trailing P/E in the last 5 years went below 31.25, so a 21.93 trough would have to be an intra-year low from the 2016–2017 era — plausible, unverified.

**⚠ METHOD FLAW to fix in the writeup:** the claim compares BR's **forward** P/E (15.1/15.77) against a **trailing** 10-year average P/E (30.85). That is not a like-for-like comparison and inflates the discount. Two clean framings that *are* supported:
- Trailing vs trailing: **16.82 now vs 31.25–34.74 in each of FY21–FY25** — roughly half.
- Forward vs forward: **15.77 now vs a FY21–FY25 range of 20.79–27.57** — below the 5-year low of 20.79.

So the *substance* ("trades below its own decade-low multiple") is directionally supported on both bases within the verifiable window. The specific 30.85 / 21.93 figures should be sourced or dropped.

## Claim 5 — tokenization moat → **SPLIT**

### 5a. Broadridge live with on-chain governance for tokenized equities → **CONFIRMED**

Primary evidence, all 2026 press releases:
- **July 20, 2026** — *"Alpaca and Broadridge Announce Governance Solution for Tokenized Securities."* Subhead: *"Broadridge enables proxy voting, investor communications, and voting entitlement reconciliation across Alpaca's platform."*
- **~July 6, 2026** — *"Ondo Finance Launches First-Ever Custodial Tokenized Securities in the U.S., Broadridge Partners to Integrate World Class Governance."* Covers U.S.-listed securities including BlackRock's iShares Core S&P 500 (IVV) ETF.
- **July 16, 2026** — Broadridge Tokenization Pulse Survey: tokenized assets a key priority for financial services firms; firms focused on hybrid market infrastructure.
- **June 23, 2026** — Broadridge names Mark Nichols **Co-President, Digital Assets**.
- **July 7, 2026** — Broadridge Distributed Ledger Repo processed **$7.5 trillion in June 2026**; ADV $357B; DLR market data now on Bloomberg Terminal. (May 2026: $7.2T, +220% y/y.)
- Q3 FY26 release, CEO Gokey: *"putting in place the building blocks of future growth by **leading in tokenization**, driving the digitization of communications, and scaling AI."*

**Caveat on "all models of tokenized securities":** that exact universality claim is **UNVERIFIED**. What is confirmed is coverage of at least two distinct models — the third-party/custodial-token model (Ondo) and a brokerage-platform model (Alpaca). Soften to "across multiple tokenization models, including custodial and platform-brokerage structures."

### 5b. "The SEC has affirmed tokenized securities carry the same governance and compliance obligations" → **PARTIALLY CONFIRMED — materially overstated**

**Source:** SEC Commissioner **Hester M. Peirce**, *"Enchanting, but Not Magical: A Statement on the Tokenization of Securities,"* **July 9, 2025**.
`https://www.sec.gov/newsroom/speeches-statements/peirce-statement-tokenized-securities-070925`

Verbatim, and it does support the substance:
> *"As powerful as blockchain technology is, it does not have magical abilities to transform the nature of the underlying asset. **Tokenized securities are still securities.** Accordingly, market participants must consider—and adhere to—the federal securities laws when transacting in these instruments."*
> *"Distributors of tokenized securities must consider their **disclosure obligations** under the federal securities laws..."*
> *"While blockchain-based tokenization is new, the process of issuing an instrument representing a security is not. **The same legal requirements apply to on- and off-chain versions of these instruments.**"*

**Three caveats the writeup must respect:**
1. This is an **individual Commissioner's statement**, not a Commission rule, order, or vote. "The SEC has affirmed" overstates its legal weight. Correct phrasing: *"SEC Commissioner Hester Peirce stated..."*
2. It is dated **July 9, 2025** — ~13 months old, not a recent catalyst.
3. It does **not** specifically address proxy voting or corporate governance mechanics; it addresses securities-law status and disclosure. The leap from "same legal requirements" to "same governance obligations → Broadridge is required infrastructure" is the writeup's own inference, not the SEC's language.

---

# VST — Vistra

## Claim 6 — cash flow and leverage → **SPLIT: FCF confirmed exactly, DEBT contradicted**

### FCF: **CONFIRMED EXACTLY** (this correction to the screen is right)
Quarterly data, stockanalysis.com/stocks/vst/financials (4 most recent reported quarters):
- Operating cash flow: 1,199 + 1,432 + 1,467 + 572 = **$4,670M** ✓ (matches claim to the dollar)
- Capital expenditures: 883 + 836 + 458 + 690 = **$2,867M** ✓ (matches claim to the dollar)
- **TTM FCF = +$1,803M ≈ +$1.8B** ✓
Cross-check: P/FCF 29.16 × $52.58B market cap → ~$1.80B FCF. Consistent.
**Trailing FCF is strongly positive, not negative. The claim is correct.**

### Debt: **CONTRADICTED**
Most recent reported quarter balance sheet:
- **Total Debt = $21,000M** (gross) — claim said ~$19.9B
- Cash & equivalents = $671M
- **Net Debt = $20,329M** — claim said ~$19.28B

The claimed figures look **2–3 quarters stale**: gross debt was $19,496M and $19,188M in earlier quarters in the series (sequence, newest first: 21,000 / 21,144 / 18,977 / 19,496 / 19,188 …).
**Correct figures: gross debt ~$21.0B, net debt ~$20.3B.** The claim's *direction* (that $19.9B was a gross figure, and net is lower than gross) is right; both magnitudes are wrong and net debt is ~$1.05B higher than stated.

### Leverage 2.5–2.8×: **NOT SUPPORTED on trailing reported numbers**
stockanalysis reports Debt/EBITDA = **3.14×** (gross) → implied TTM EBITDA ~$6.7B → **net-debt/EBITDA ≈ 3.0×**.
The claimed 2.5–2.8× is below this and can likely only be reconciled against Vistra's own forward *"Ongoing Operations Adjusted EBITDA"* guidance — a non-GAAP, forward-looking measure. **On trailing reported figures leverage is ~3.0–3.1×.** If the writeup keeps 2.5–2.8×, it must say it is against forward guided adjusted EBITDA.

Other context: EV $72.49B, market cap $52.58B, interest coverage 3.43×, 52-week price change −25.05%, 200-day MA $163.55.

## Claim 7 — PJM capacity auction → **CONFIRMED EXACTLY**

**Source:** PJM Inside Lines, **July 14, 2026** — *"PJM Capacity Auction Procures 138,318 MW of Generation Resources as Work Continues To Address Growing Electricity Demand"* (2028/2029 Base Residual Auction).

- Clearing price: **$325/MW-day (UCAP)** ✓
- **Cleared AT the FERC-approved cap** ✓ — down 2.5% from the prior year's $333.44/MW-day cap
- **New generation and generation uprates cleared: 525 MW** ✓ (matches the claim exactly)
- Delivery year 2028/2029

**Bonus fact the writeup is not using and probably should:** PJM procured 138,318 MW UCAP plus 10,864 MW from FRR regions = 149,182 MW, which fell **6,831 MW SHORT of the reliability requirement — "the first in PJM history in which the entire RTO fell short."** PJM plans a special backstop procurement. This is materially more bullish for VST than the 525 MW figure alone.

## Claim 8 — VST next earnings Aug 7, 2026 → **CONFIRMED**

- Vistra PR, **July 6, 2026** (PRNewswire): *"Vistra to Report Second Quarter Results on Aug. 7, 2026"* — "plans to report its second quarter 2026 financial and operating results on Friday, Aug. 7, 2026, during a live conference call and webcast."
- stockanalysis: *"The next confirmed earnings date is Friday, August 7, 2026, before market open."*

---

# ISRG — Intuitive Surgical

**Source of record:** SEC 8-K filed 2026-07-16, accession 0001035267-26-000047, Exhibit 99.1
`https://www.sec.gov/Archives/edgar/data/1035267/000103526726000047/q226ex-991earningsrelease.htm`
Dated SUNNYVALE, CALIF., July 16, 2026.

## Claim 9 — Q2 2026 print → **CONFIRMED except the stock move**

Confirmed from the filed release:
- Revenue **$2,892.3M = $2.89B, +19%** vs $2,440.0M ✓
- Non-GAAP EPS **$2.80** vs $2.19 = **+27.9% ≈ +28%** ✓ (non-GAAP net income $1.00B)
- FY26 outlook: *"Worldwide da Vinci procedure growth of **approximately 13.5% to 15.5%** in 2026. The Company expects to be closer to the midpoint of this range."* ✓
- Reported **July 16, 2026 — AFTER market close** (so the reaction day is Jul 17)
- Extra context: GAAP EPS $2.29; Q2 worldwide procedures +~16% (da Vinci +~15%, Ion +~36%); 468 da Vinci placements vs 395; $28M net IEEPA tariff refund benefit (+$0.08/sh); guidance includes ~1.0% of revenue tariff drag.

### ⚠ **CONTRADICTED: the stock fell −14.15%, not ~−11.6%**
Daily closes (stockanalysis.com/stocks/isrg/history):
- Jul 16, 2026: $402.33 (+3.43%)
- **Jul 17, 2026: $345.42 — −14.15% on 11.56M shares** (~3x normal volume)

Intraday wire snapshots on Jul 17 quoted −10.7% ($359.41) and −12.5% ($352.00) at different points, which is likely where an ~11.6% figure came from — but **the closing move was −14.15%.** Use −14.2%.

Current: ISRG $375.41 (Aug 3, 2026, +6.25%), 52-week price change −22.29%, 200-day MA $481.57, trailing P/E 43.05, forward P/E 33.23. Note the stock has already recovered ~8.7% off the Jul 17 close. Recent sell-side: UBS upgraded to Buy (PT $500, cut from $550); HSBC downgraded to Hold (PT $391); BofA PT $470 from $515.

## Claim 10 — J&J OTTAVA FDA De Novo → **CONFIRMED; date is Jul 21, not Jul 22**

**Source:** FDA De Novo database (accessdata.fda.gov), retrieved 2026-08-03:
- Device Name: **OTTAVA™ Robotic Surgical System**
- Requester: **Auris Health, Inc., part of Johnson & Johnson**
- De Novo Number: **DEN250068**
- **Decision Date: 07/21/2026**

The regulatory action is real and is De Novo marketing authorization. **FDA's decision date is July 21, 2026**, one day earlier than claimed. J&J's public announcement may well have been July 22 (ISRG fell −2.68% on Jul 22), so "announced July 22" would be defensible — but "received authorization on July 22" is off by a day. Safest phrasing: *"FDA granted De Novo marketing authorization on July 21, 2026 (DEN250068)."*

## Claim 11 — recurring revenue and installed base → **SPLIT**

### Installed base 11,710: **CONFIRMED EXACTLY**
Verbatim: *"The Company grew its da Vinci surgical system installed base to **11,710 systems as of June 30, 2026**, an increase of 12% compared with 10,488 as of June 30, 2025."*
(Also: Ion installed base 1,096, +21% vs 905.)

### Recurring revenue ~85%: **UNVERIFIED — the disclosed floor is 76.3%**
Q2 2026 income statement, verbatim line items:
- Instruments and accessories: $1,734.9M
- Systems: $685.0M
- Services: $472.4M
- Total revenue: $2,892.3M

I&A + Services = $2,207.3M = **76.3% of total.** That is the hard, derivable recurring floor.

To reach ~85% you need ~$254M of **operating-lease** revenue booked inside the $685.0M Systems line. That is plausible — the release states **254 of the 468** da Vinci placements were under operating lease arrangements (131 of those usage-based) — and Intuitive's own definition of recurring revenue does include lease revenue. But **Intuitive did not state an 85% figure in the Q2 release, and it is not derivable from the disclosed statements.** Either source the 85% to an Intuitive investor deck/10-Q, or state the conservative, filing-backed version: *"~76% of revenue is instruments, accessories and service, before adding lease revenue."*

---

## Net assessment for the writeup

**Must fix before publishing:**
1. BR closed-sales prior guidance: **$290–$330M**, not $290–$340M.
2. BR pipeline >$1B / +20% / origination +25% — not in the filed release; attribute to the call or drop.
3. BR valuation: use **forward 15.77** (or trailing 16.82); stop comparing forward P/E to a trailing 10-yr average; the 30.85 / 21.93 figures are unsourced.
4. "The SEC has affirmed" → **"SEC Commissioner Hester Peirce stated (July 9, 2025)"**.
5. VST debt: gross **$21.0B**, net **$20.3B**, trailing net leverage **~3.0×** — the claimed $19.9B/$19.28B/2.5–2.8× is stale/optimistic.
6. ISRG drop: **−14.15%**, not −11.6%.
7. OTTAVA De Novo decision date: **July 21, 2026**.

**Strongest verified pillars (safe to lean on):**
- BR raised FY26 guidance while the stock fell ~42% from its high — fully confirmed, filed.
- BR Q4 FY26 catalyst tomorrow, Aug 4, 2026, before market open — confirmed twice.
- BR tokenized-securities governance is live and commercial (Alpaca Jul 20, Ondo ~Jul 6, DLR $7.5T June) — confirmed.
- VST trailing FCF +$1.8B, OCF $4,670M / capex $2,867M — confirmed to the dollar.
- PJM 525 MW new supply at the $325/MW-day cap — confirmed exactly, **plus** the unused and stronger fact that the RTO fell 6,831 MW short of its reliability requirement for the first time ever.
- ISRG Q2 revenue/EPS/guidance/installed base — all confirmed from the 8-K.
