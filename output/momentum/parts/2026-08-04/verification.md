# Independent Fact Verification — AVGO / LRCX / MSFT

**Verifier:** independent check, no access to the source dossier
**Date of verification:** 2026-08-04
**Method:** claims traced to company press releases, SEC 8-K exhibits, and earnings-call transcripts where possible. Where a figure exists only in secondary coverage or is an analyst estimate, it is labelled as such.

---

## Scorecard

| # | Ticker | Claim (short) | Verdict | Note |
|---|--------|---------------|---------|------|
| 1 | AVGO | >$30B AI bookings vs $10.8B shipped, ~2.8–3x | **CONFIRMED** | Verbatim CEO statement; "over $30B" is a floor, so 2.8x is a *minimum*, not a point estimate |
| 2 | AVGO | Rev $22.2B +48%, record non-GAAP op margin ~67% | **CONFIRMED** | $22,187M; non-GAAP op inc $14,928M = 67.3% |
| 3 | AVGO | Q3 guide $29.4B (+84%), AI $16.0B (+200%), FY26 AI ~$56B reiterated | **CONFIRMED** | Company said AI "*over* 200%"; $56B was unchanged (a negative catalyst that day) |
| 4 | AVGO | $100B+ annual AI semi revenue starting FY2027 | **CONFIRMED** | Management forecast, not a booked figure. CEO's own words were "significantly in excess of $100B" |
| 5 | AVGO | AI XPV Platform, $35B, >20GW through 2028, Anthropic 1GW+ | **CONFIRMED** | Dated **2026-06-09**, all three elements exact |
| 6 | AVGO | 70%+ share of custom XPU design-services market, Marvell #2 | **UNVERIFIED (directionally CONFIRMED-VIA-SECONDARY)** | No primary source. Third-party estimates range 60–80%; Marvell estimates range 8%–25% |
| 7 | AVGO | Next earnings date (Q3 FY26) | **CONFIRMED** | **Wednesday, 2026-09-02**, after close, call 2:00pm PT |
| 8 | LRCX | Q4 FY26 rev $6.72B, EPS ~$1.81–1.82, GM ~52% 20-yr high; FY26 $23.23B / EPS $5.82 | **CONFIRMED with one label correction** | FY26 **$5.82 is non-GAAP**; GAAP FY26 diluted EPS is **$5.76** |
| 9 | LRCX | Sept-2026 quarter guided $8.1B ±$400M, >20% q/q | **CONFIRMED** | Exact |
| 10 | LRCX | Raised CY26 WFE to "low $150B", from ~$140B around 2026-06-02 | **CONFIRMED with date correction** | $150B raise confirmed 2026-07-29. The $140B number dates from the **2026-04-22** Q3 call; 2026-06-02 (BofA conf) was a restatement, not the original raise |
| 11 | MSFT | Commercial RPO $678B +84%; ~25% ex-OpenAI | **CONFIRMED** | $678B/+84% is in the press release; the ex-OpenAI 25% is **call-only**, not in the filing |
| 12 | MSFT | Azure +43% vs 39–40% guidance | **CONFIRMED** | Guidance issued 2026-04-29 was 39–40% **in constant currency** |
| 13 | MSFT | Amy Hood: "demand continues to exceed available supply" | **CONFIRMED** | Verbatim on the call |
| 14 | MSFT | FY26 rev $331.8B (+18%), EPS $17.95 (+32%) | **CONFIRMED, but +32% needs context** | GAAP. Q4 EPS growth adjusted for the OpenAI investment impact was **23%**, not 32% |

**Nothing was CONTRADICTED.** Three items are materially overstated or mislabelled: **#8** (non-GAAP EPS presented without the label), **#6** (an analyst estimate presented as fact), **#14** (a GAAP growth rate inflated by OpenAI investment accounting). **#10** has a wrong date. **#1**, **#4** are management characterizations, not audited figures.

---

## AVGO — Broadcom

### Claim 1 — >$30B AI bookings against $10.8B shipped (~2.8–3x book-to-bill) — CONFIRMED

Verbatim from the Q2 FY2026 earnings call, 2026-06-03:

> "Bookings for AI semiconductors were over $30 billion against the $10.8 billion we shipped."

Source: Broadcom (AVGO) Q2 2026 earnings call transcript, The Motley Fool, 2026-06-03 — https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/

The $10.8B shipped figure is corroborated in the press release / 8-K (below). $30B ÷ $10.8B = **2.78x**, and because management said "over $30 billion" the true ratio is ≥2.78x. The claim's "roughly 2.8–3x" is therefore fair, but note:

- **Caveat (overstatement risk):** this is a management-disclosed bookings number stated on a call. It is **not** an audited or filed figure, is not defined in the press release, and Broadcom does not publish a book-to-bill metric. Any write-up should attribute it to management, not to "reported results." The upper end (3x) is an inference, not something the company said.
- Asked why the backlog was so large, Hock Tan attributed it to customers needing lead time for compute and to securing HBM/DRAM availability.

### Claim 2 — Q2 FY26 revenue $22.2B +48%; record non-GAAP operating margin ~67% — CONFIRMED

From the Q2 FY2026 press release / Form 8-K Exhibit 99.1 (quarter ended 2026-05-03, released 2026-06-03):

- Revenue: **$22,187 million**, **+48% y/y** (rounds to $22.2B — exact)
- GAAP operating income: $10,788M
- Non-GAAP operating income: **$14,928M**, i.e. **67.3% margin** (~67% — exact)
- Adjusted EBITDA: **$15,244M = 69% of revenue**
- AI semiconductor revenue: **$10.8B, +143% y/y**
- Infrastructure software revenue: $7,178M

Sources:
- Broadcom Q2 FY2026 press release, 2026-06-03 — https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial
- Form 8-K Ex-99.1 — https://www.sec.gov/Archives/edgar/data/1730168/000173016826000051/avgo-05032026x8kxex99.htm (SEC blocked automated fetch; content verified via StockTitan's reproduction of the 8-K: https://www.stocktitan.net/sec-filings/AVGO/8-k-broadcom-inc-reports-material-event-ca5d7db2f903.html)
- "Record" characterization, CFO on the call: "Operating margin was a record 67% and adjusted EBITDA was a record 69% of revenue." (Motley Fool transcript, 2026-06-03)

**Note:** "record" is a management characterization on the call, not a line item in the filing — but the underlying 67.3% is arithmetically correct from the filed non-GAAP reconciliation.

### Claim 3 — Q3 guide $29.4B (+84%), Q3 AI semi $16.0B (+200%), FY26 AI ~$56B reiterated — CONFIRMED

From the same press release and call:

- Q3 FY26 revenue guidance: **~$29.4 billion, +84% y/y** — exact
- Q3 AI semiconductor revenue guidance: **$16.0 billion**, expected to "grow **over 200 percent** year-over-year" — the claim's "+200%" is a slight *understatement* of the company's own wording ("over 200%"), so it is not an overstatement.
- Q3 non-GAAP operating margin guidance: ~67%; adjusted EBITDA ~68% of revenue
- FY2026 AI semiconductor revenue: **"We expect to achieve AI semiconductor revenue of $56 billion, up approximately 180%."** — CFO on the call.

**"Reiterated" is correct and materially important:** the $56B was *unchanged* from the prior quarter's guide, and this — alongside soft infrastructure-software revenue — is why the stock fell on the print. See CNBC, "Broadcom stock plunges on weak software sales, unchanged AI chip forecast for the year," 2026-06-03 — https://www.cnbc.com/2026/06/03/broadcom-avgo-earnings-report-q2-2026.html

Any bull case that cites $56B should not present it as a raise.

### Claim 4 — $100B+ annual AI semiconductor revenue starting fiscal 2027 — CONFIRMED (as a management forecast)

- Q2 FY26 call, 2026-06-03: "We reiterate our AI semiconductor revenue guidance to be in excess of $100 billion," framed as underpinned by multi-year agreements with leading customers.
- Originally given at Q1 FY26 (2026-03-04), where CEO Hock Tan said AI chip revenue in 2027 would be **"significantly in excess of $100 billion"** — CNBC, 2026-03-04 — https://www.cnbc.com/2026/03/04/broadcom-sees-ai-chip-sales-significantly-over-100-billion-in-2027.html
- Named multi-year agreements confirmed on the call: Google (multiple generations of TPUs + AI networking), Anthropic (agreement signed April 2026 for **5 GW** of next-gen TPU-based compute beginning 2027). Six core custom-chip customers, including Google, Meta, Anthropic and OpenAI.

**Flag:** this is a forward forecast by management, not contracted revenue and not a filed figure. Contemporaneous coverage explicitly noted Wall Street skepticism about it (e.g. Sahm Capital, 2026-06-04 — https://www.sahmcapital.com/news/content/broadcom-just-made-bold-100-billion-ai-revenue-forecast-for-next-year-but-wall-street-doesnt-believe-it-is-it-fair-to-assume-2026-06-04). Presenting it as guidance is fine; presenting it as backlog is not.

### Claim 5 — AI XPV Platform: $35B, >20GW through 2028, Anthropic 1GW+ from mid-2026 — CONFIRMED (all elements, date 2026-06-09)

Joint press release, dateline **2026-06-09**: "Broadcom, Apollo, and Blackstone Establish Landmark Strategic Platform to Accelerate More Than 20 Gigawatts of Global AI Deployments."

- Platform name: **"AI XPV Platform"** — confirmed verbatim (Apollo's companion release is titled "Apollo Leads $35 Billion Capital Solution for Broadcom AI XPV Platform in Partnership with Blackstone and Leading Global Banks"). Note some call transcripts render it as "AI XPU platform" — a transcription artifact; the official name is XPV.
- Capital: **$35 billion**, led by Apollo, in partnership with Blackstone's Credit & Insurance Business as anchor investors, plus leading global banks.
- Scale: designed to enable **more than 20 gigawatts** of compute capacity **through 2028**, using Broadcom XPUs and networking, for frontier labs including Anthropic and OpenAI.
- First tranche: the $35B facilitates "**Anthropic's previously-announced capacity expansion of more than 1 gigawatt of compute infrastructure expected to deploy in Fluidstack-based sites starting in mid-2026**."

Sources:
- PR Newswire (joint release), 2026-06-09 — https://www.prnewswire.com/news-releases/broadcom-apollo-and-blackstone-establish-landmark-strategic-platform-to-accelerate-more-than-20-gigawatts-of-global-ai-deployments-302795286.html
- Broadcom IR — https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic
- Blackstone — https://www.blackstone.com/news/press/broadcom-apollo-and-blackstone-establish-landmark-strategic-platform-to-accelerate-more-than-20-gigawatts-of-global-ai-deployments/
- Apollo IR — https://ir.apollo.com/news-events/press-releases/detail/629/apollo-leads-35-billion-capital-solution-for-broadcom-ai

All three challenged elements (size, 20GW, date) are exact. **Interpretive caveat:** the $35B is a *capital solution for the buyers of compute*, i.e. financing that enables deployments — it is not $35B of Broadcom revenue or a Broadcom order. Don't let the number migrate into a revenue column.

### Claim 6 — 70%+ share of custom AI accelerator (XPU) design-services market, Marvell #2 — UNVERIFIED as a precise figure

There is **no primary source**. Broadcom does not disclose a design-services market share, and no filing, press release or call transcript supports 70%.

What the third-party estimates actually say, and they disagree materially:

- **Bloomberg Intelligence** (cited via secondary coverage, early 2026): a **60–80%** range for Broadcom.
- **Counterpoint Research**: Broadcom to hold roughly **60%** share of the custom AI chip market by **2027** — https://finance.yahoo.com/news/broadcom-set-dominate-custom-ai-163116560.html
- Various 2026 trade/industry blogs assert "70%+", but they cite Bloomberg Intelligence/TrendForce rather than doing original measurement (e.g. https://hashrateindex.com/blog/design-partners-ai-asic-market-part-2/, https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia).
- **Marvell as #2 is directionally supportable but the magnitude is disputed:** estimates range from ~**20–25%** share (anchored by AWS Trainium, Microsoft Maia) to a projected slide to ~**8%** by 2027 in other sources.

**Verdict:** the *qualitative* claim — Broadcom is the dominant custom-XPU design partner and Marvell is the clear #2 — is well supported. The *specific* "70%+" is at the optimistic end of a wide estimate band, is analyst-derived, and there is no methodology consensus (design-services share vs. custom-ASIC revenue share vs. unit share are three different denominators, and the sources mix them). Mark it UNVERIFIED and attribute any number used to a named research house with its definition.

### Claim 7 — Next earnings date — CONFIRMED

**Wednesday, 2026-09-02**, after market close; conference call 2:00 p.m. Pacific. Announced by Broadcom.

Sources:
- Broadcom, "Broadcom Inc. to Announce Third Quarter Fiscal Year 2026 Financial Results on Wednesday, September 2, 2026" — https://www.broadcom.com/company/news/financial-releases/64621
- StockTitan — https://www.stocktitan.net/news/AVGO/broadcom-inc-to-announce-third-quarter-fiscal-year-2026-financial-dkaqc3d1n73a.html

---

## LRCX — Lam Research

### Claim 8 — Q4 FY26 and FY26 figures — CONFIRMED with one label correction

Quarter ended 2026-06-28, reported **2026-07-29**. From the press release financial tables:

| Metric | June-2026 quarter | Claim | Status |
|---|---|---|---|
| Revenue | **$6,722,238K = $6.72B** (record) | $6.72B record | exact |
| GAAP gross margin | **51.7%** | ~52% | ok |
| Non-GAAP gross margin | **52.0%** | ~52% | exact |
| GAAP diluted EPS | **$1.81** | $1.81–1.82 | exact |
| Non-GAAP diluted EPS | **$1.82** | $1.81–1.82 | exact |

| Metric | FY2026 (12 mo. ended 2026-06-28) | Claim | Status |
|---|---|---|---|
| Revenue | **$23,232,690K = $23.23B** | $23.23B | exact |
| GAAP gross margin | **50.5%** | — | — |
| **GAAP diluted EPS** | **$5.76** | — | — |
| **Non-GAAP diluted EPS** | **$5.82** (per CFO on call, "up 41% from fiscal 2025") | $5.82 | **non-GAAP — must be labelled** |

**The one correction:** FY26 EPS of **$5.82 is a non-GAAP figure** cited by CFO Doug Bettinger on the call; the **GAAP FY26 diluted EPS in the filed press release is $5.76**. A dossier that prints "$5.82" without the non-GAAP tag is overstating by $0.06 (~1%) and mislabelling the basis. Small in magnitude, but it is exactly the kind of quiet substitution flagged as a failure mode.

**"20-year high" gross margin:** CONFIRMED as a management characterization, not a computed disclosure. CFO Doug Bettinger on the call: "**our highest quarterly gross margin in 20 years**." Note this refers to the **non-GAAP 52.0%** quarterly figure.

Sources:
- Lam Research press release, 2026-07-29 — https://newsroom.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28,-2026
- PR Newswire mirror — https://www.prnewswire.com/news-releases/lam-research-corporation-reports-financial-results-for-the-quarter-ended-june-28-2026-302838154.html
- Form 8-K Ex-99.1 — https://www.sec.gov/Archives/edgar/data/707549/000070754926000033/lrcx_exhibitx991xq4x2026.htm
- Q4 FY2026 earnings call transcript, 2026-07-29 — https://www.investing.com/news/transcripts/earnings-call-transcript-lam-research-posts-record-q4-2026-results-stock-rebounds-93CH-4821978

CEO Tim Archer, press release: "Lam delivered record revenue, operating margin and earnings per share in the June quarter as AI-driven demand continues to reshape the semiconductor industry."

### Claim 9 — September-2026 quarter guided $8.1B ±$400M, >20% sequential — CONFIRMED

Guidance issued 2026-07-29:

- Revenue: **$8.10 billion ± $400 million**
- Gross margin: 52.0% ± 1 ppt
- Operating margin: 39.5% ± 1 ppt
- Non-GAAP diluted EPS: $2.15 ± $0.15, on ~1.255B shares

CEO Tim Archer: "$8.1 billion September quarter revenue guide represents **more than 20% growth quarter-on-quarter**." ($8.10B / $6.72B = +20.5%, consistent.)

Sources: as above, plus Seeking Alpha, 2026-07-29 — https://seekingalpha.com/news/4621252-lam-research-projects-8_1b-september-quarter-revenue-with-wfe-seen-in-low-150b-range

### Claim 10 — CY2026 WFE raised to "low $150 billion range" — CONFIRMED on substance, DATE CORRECTION on the prior step

The raise itself is exact. CEO Tim Archer on the 2026-07-29 call:

> "calendar 2026 wafer fab equipment spending, or WFE, to be in the **low $150 billion range**, up from our prior outlook of **$140 billion with upside bias**"

**Correction to the claim's chronology:** the claim says Lam "had raised it to ~$140B earlier (around 2026-06-02)." The $140B forecast was in fact introduced at the **Q3 FY2026 earnings call on 2026-04-22** (see BigGo's contemporaneous headline, "Raises WFE Forecast to $140B," 2026-04-22 — https://finance.biggo.com/news/US_LRCX_2026-04-22, and TIKR — https://www.tikr.com/blog/lam-research-stock-posts-third-straight-record-quarter-as-wfe-outlook-rises-to-140b). CFO Doug Bettinger then **restated/reinforced** $140B at the **BofA Global Technology Conference on 2026-06-02**, along with commentary that Lam's served-market share had moved to the mid-30% range — which some outlets headlined as a "raise" (https://www.insidermonkey.com/blog/lam-research-lrcx-raises-wfe-forecast-at-bofa-global-technology-conference-1776438/).

Net: two-step $140B → low-$150B is right; the $140B step belongs to **2026-04-22**, not 2026-06-02. Secondary sources conflict on this, so the safest phrasing is "$140B established in April and reiterated at BofA on June 2."

---

## MSFT — Microsoft

Fiscal Q4 FY2026, quarter ended 2026-06-30, reported **2026-07-29**.

### Claim 11 — Commercial RPO $678B +84%; ~25% ex-OpenAI — CONFIRMED (with a sourcing distinction)

- **$678 billion, up 84% y/y** — in the earnings press release. Exact.
- **"RPO increased 25% when excluding OpenAI"** — CFO Amy Hood, earnings call. **This figure is call-only; it does not appear in the press release or the 10-K.**
- Related context from the call: all *sequential* commercial RPO growth was driven by commitments from customers **outside** frontier model companies.

Sources:
- Microsoft FY26 Q4 press release, 2026-07-29 — https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
- Form 8-K Ex-99.1 — https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm
- Q4 FY2026 earnings call transcript — https://www.investing.com/news/transcripts/earnings-call-transcript-microsoft-q4-2026-beats-forecasts-stock-jumps-8-93CH-4822020

**Analytical flag (not a factual error):** the +84% headline and the +25% ex-OpenAI figure describe very different businesses. A dossier citing $678B/+84% as evidence of broad demand should carry the 25% number in the same breath — roughly three-quarters of the y/y RPO growth is OpenAI-related, i.e. concentrated in a single counterparty.

### Claim 12 — Azure +43% vs 39–40% guidance — CONFIRMED

- Reported: **Azure and other cloud services revenue grew 43%** in FQ4 FY2026 (press release).
- Prior guidance: on the Q3 FY26 call (**2026-04-29**) Amy Hood guided Q4 Azure growth of **39% to 40% in constant currency**, above the ~37% StreetAccount consensus at the time. Source: CNBC, 2026-04-29 — https://www.cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html
- So the beat is real, ~3–4 points above the top of guidance.

**Minor precision note:** the guidance was stated **in constant currency**; the reported 43% is the as-reported growth rate in the press release. The comparison is still valid but is not strictly like-for-like. Also for context, Microsoft guided Q1 FY27 Azure growth of ~45% cc — an acceleration.

Full-year: Azure surpassed **$100 billion** in revenue for the first time, up 41%.

### Claim 13 — "demand continues to exceed available supply" — CONFIRMED

Amy Hood, FQ4 FY2026 earnings call, 2026-07-29, verbatim: "**demand continues to exceed available supply**, that certainly remains true," alongside "customer demand continues to exceed available capacity."

Source: Q4 FY2026 transcript — https://www.investing.com/news/transcripts/earnings-call-transcript-microsoft-q4-2026-beats-forecasts-stock-jumps-8-93CH-4822020

### Claim 14 — FY26 revenue $331.8B (+18%), FY26 EPS $17.95 (+32%) — CONFIRMED, but the +32% needs a qualifier

From the FY26 Q4 press release:

- FY2026 revenue: **$331.8 billion, +18%** — exact
- FY2026 GAAP diluted EPS: **$17.95, +32%** — exact
- Q4 alone: revenue $90.0B +18%; operating income $40.6B +18%; net income $35.8B +31%; GAAP diluted EPS $4.81 +32%
- Microsoft Cloud: $59.3B in Q4 (+27%); $214B for the year (+27%)

**Flag — materially overstated if presented without context.** The +32% EPS growth is GAAP and is inflated by the accounting impact of Microsoft's OpenAI investment. On the call Amy Hood gave the underlying figure: Q4 "**earnings per share was $4.74, an increase of 23% when adjusted for the impact from our investment in OpenAI**." Note also that operating income grew only **18%**, in line with revenue — i.e. essentially none of the EPS acceleration above 18% came from operations. A thesis that leans on "+32% EPS growth" as evidence of operating leverage is not supported by the operating line.

Satya Nadella, press release: "We are advancing the frontier on the cost-to-outcome curve, ensuring every customer can turn tokens into business results."

---

## Analyst consensus price targets (as of 2026-08-04)

Sources disagree materially — mostly because they poll different analyst panels. Reporting each with its panel size.

| Ticker | Consensus PT | Panel | Price (2026-08-04 close) | Implied upside | Source / date |
|---|---|---|---|---|---|
| **AVGO** | **$527.88** | 48 analysts (S&P Global) | $418.16 | +26.2% | stockanalysis.com, data as of 2026-08-03/04; latest analyst forecast dated 2026-07-28 — https://stockanalysis.com/stocks/avgo/forecast/ |
| AVGO (alt) | $500.78 | 29 analysts | — | — | Benzinga — https://www.benzinga.com/quote/AVGO/analyst-ratings |
| **LRCX** | **$368.13** | 35 analysts (S&P Global) | $317.74 | +15.9% | stockanalysis.com, 2026-08-04 — https://stockanalysis.com/stocks/lrcx/forecast/ |
| LRCX (alt) | $327.15 | 28 analysts | — | +3% | Benzinga — https://www.benzinga.com/quote/LRCX/analyst-ratings |
| LRCX (alt) | $350.29 | 41 analysts | — | ~+22% (as quoted) | ChartMill/TradingView-sourced |
| **MSFT** | **$562.73** | 56 analysts (S&P Global) | $492.81 | +14.2% | stockanalysis.com, data as of 2026-08-03/04 — https://stockanalysis.com/stocks/msft/forecast/ |
| MSFT (alt) | $553.97 | — | — | ~+12% | public.com |

**Dispersion notes:**

- **AVGO** has the widest absolute range: low $215.88, high $675. A $216 low against a $418 price means at least one covering analyst sees ~50% downside — worth acknowledging in a conviction write-up. Consensus rating: Strong Buy.
- **LRCX** consensus targets are stale relative to the stock. The Benzinga panel ($327) implies only ~3% upside, i.e. the July 29 print and the WFE raise have not yet been fully absorbed into the average. Range $290–$500. Expect upward revisions; do not treat the current mean as a ceiling *or* as validation.
- **MSFT** range is $400–$870 across 56 analysts — an unusually wide band for a mega-cap, reflecting disagreement over AI capex returns and OpenAI exposure. Consensus Strong Buy.
- All price targets are aggregator-derived (S&P Global / Benzinga panels via stockanalysis.com and Benzinga). These are **secondary** by nature; there is no primary source for a consensus figure.

---

## Summary of items needing correction in the source dossier

1. **LRCX FY26 EPS $5.82 is non-GAAP.** GAAP FY26 diluted EPS is **$5.76**. Label it.
2. **LRCX WFE chronology.** The $140B step dates from the **2026-04-22** Q3 call, not 2026-06-02 (that was a BofA-conference reiteration).
3. **AVGO 70%+ XPU design-services share is an analyst estimate with no primary source**, and estimates span 60–80% (Bloomberg Intelligence) with Counterpoint at ~60% for 2027. Attribute or drop the precise number.
4. **MSFT FY26 EPS +32% is GAAP and OpenAI-investment-inflated**; the adjusted growth rate management gave was **23%**, and operating income grew 18%. Do not cite +32% as evidence of operating leverage.
5. **AVGO >$30B bookings and the $100B+ FY27 target are management statements**, not reported or contracted figures. The 2.8x book-to-bill is a floor derived from "over $30 billion."
6. **AVGO FY26 AI revenue of $56B was reiterated, not raised** — and the market treated the lack of a raise as a negative on 2026-06-03.
