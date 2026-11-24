> Run by: Muse Spark 1.3 — full panel

# Phase 3.5 verification — stock-pick-momentum, run 2026-11-24

Scope: the nine claims specified in the verifier brief (top 3 names only: APH, WST, LLY), checked against independent sources — primary sources where possible (SEC filings / company press releases, earnings-call transcripts, FDA orders) plus reputable financial press. The dossier (`research_dossier_2026-11-24.md`) was used only to locate the claims, not as evidence for them. Verification date: 2026-11-24.

Verdict key: **CONFIRMED** = independent source(s) agree on every sub-element; **CONTRADICTED** = an independent source disagrees on at least one sub-element (corrected figure given); **UNVERIFIED** = no source found for a sub-element.

## Summary

| # | Ticker | Claim (short) | Verdict |
|---|---|---|---|
| 1 | APH | Q3 2026 orders $12.17B (+99%), book-to-bill 1.19:1, backlog +$1.94B in quarter, +$5.7B YTD | **CONFIRMED** |
| 2 | APH | Only ~3 firms can supply qualified 224G interconnect at scale; high-speed assembly lead times >12 weeks | **CONTRADICTED (in part)** |
| 3 | APH | Q3 2026 sales $10.23B (+65%, +37% organic), adj EPS $0.80 (+74%); FY26 guide $36.9–37.1B sales, $2.82–2.84 EPS | **CONFIRMED** |
| 4 | WST | HVP Components $466.7m (+20.3% organic), GLP-1-linked HVP "well into the 30% range", pricing just over 4 pts of Q3 growth | **CONFIRMED** |
| 5 | WST | New finishing capacity takes 18–24 months to come online | **CONFIRMED** |
| 6 | WST | Q3 2026 sales $874.5m, adj EPS $2.66 (+35.7%); FY26 guide $3.41–3.42bn sales, $9.38–9.48 adj EPS | **CONFIRMED** |
| 7 | LLY | FDA declared tirzepatide/semaglutide GLP-1 shortage ended Dec 2024; no Zepbound shortage currently | **CONTRADICTED (in part)** |
| 8 | LLY | Q3 2026 revenue $24.4B (+39%); Mounjaro $10.7B (+65%), Zepbound $5.35B (+49%) | **CONFIRMED** |
| 9 | LLY | Retatrutide beat semaglutide head-to-head in Phase 3 (~20–21% vs ~9.4% weight loss), FDA filing planned Q1 2027 | **CONFIRMED** (with trial-name correction) |

**Bottom line:** 7 of 9 claims confirmed in full. Two claims are contradicted in part — both are date/count conflations, not fabrications: claim 2 overstates supplier exclusivity (four, not ~three, firms completed first-batch 224G certification), and claim 7 merges two separate FDA shortage resolutions into one December 2024 date (semaglutide was resolved February 2025). Neither contradiction overturns the underlying investment point, but both should be corrected in the memo before the panel relies on them.

---

## APH — Amphenol

### Claim 1 — CONFIRMED
**Claim:** Record Q3 2026 orders of $12.17B (+99% YoY), book-to-bill 1.19:1, backlog up $1.94B in the quarter and $5.7B year-to-date (Q3 2026 earnings, Oct 28, 2026).

**Evidence:**
- Amphenol Q3 2026 earnings call transcript, Oct 28, 2026 (Motley Fool / AlphaStreet / MarketBeat): "Orders in the quarter were a record $12,170,000,000, up a strong 99% compared to the third quarter of 2025 and up 13% sequentially, resulting in another very strong book-to-bill ratio of 1.19 to 1."
- Aardvark Labs Q3 2026 recap (Oct 28, 2026): "Orders of $12.17B (+99%) set a 1.19 book-to-bill and added $1.94B to backlog, $5.7B year to date." The $1.94B is arithmetic (orders $12.17B − sales $10.23B = $1.94B); the $5.7B YTD figure is the recap's derived cumulative, not a backlog total stated by the company in the press release — but it is internally consistent with the quarterly order/sales figures.
- Trefis, Nov 19, 2026, corroborates: "Amphenol took in a record $12.17 billion of orders in the third quarter, up 99% from a year earlier. The company booked $1.19 of orders for every $1 of sales."

No correction needed. Minor note: the dossier's "book-to-bill >1.2 for three straight quarters" framing elsewhere is slightly loose — Q3 was 1.19, i.e. just under 1.2 — but that is outside this claim.

### Claim 2 — CONTRADICTED (in part)
**Claim:** Only ~3 firms (Amphenol, TE Connectivity, Molex) can supply qualified 224G interconnect at scale; high-speed assembly lead times exceed 12 weeks.

**Evidence — supplier count (contradicted as stated):**
- PNA Fiber, "224G/448G Interconnects" industry analysis, July 26, 2026: "Amphenol, Molex, TE Connectivity, **Samtec**: The first batch of manufacturers to complete 224G certification by NVIDIA and ultra-large-scale North American cloud vendors." That is **four** firms in the first certified batch, not three.
- The same analysis lists Chinese suppliers already in 224G sample/small-batch production (Luxshare, Zhaolong) and, per NexPCB's Week 41 (Oct 9, 2026) supply-chain note, AVIC Jonhon's 224G high-speed connectors "passed validation at a leading server maker and are now in volume supply" for GB200/B300 platforms, with Huafeng in volume delivery. So the qualified-at-scale set is wider than three and growing.
- **Correction:** the concentration point is directionally right — Amphenol, TE and Molex are the three largest / first-mover suppliers and the certification cycle (12–24 months per PNA Fiber) is a real barrier — but "only ~3 firms" is not literally true. Samtec is a fourth certified supplier, and Chinese vendors are entering volume supply. The memo should say "a handful of firms (Amphenol, TE, Molex, Samtec) completed first-batch 224G certification" rather than "only ~3 firms can supply."

**Evidence — lead times (confirmed as a sourced claim, with a sourcing caveat):**
- Markets NXT, "U.S. Cable Connector Market Size, Share & Forecast 2026–2032": "Lock multi-year volume agreements with Amphenol or TE Connectivity for 2027 delivery, as high-speed assembly lead times exceed twelve weeks." Verbatim confirmation of the >12-week element.
- Caveat: this is a single market-research report, not a manufacturer or primary source, and lead times are product-dependent — Amphenol's own HSIO connector materials cite "industry-leading lead times (6–10 weeks)" for standard parts (element14/Amphenol), and a custom-cable vendor cites 12–16 weeks for custom assemblies. The >12-week figure is best read as applying to custom/high-speed assemblies, not all 224G parts.

**Overall verdict:** CONTRADICTED on the supplier count as stated; the lead-time half is confirmed from its cited source. The dossier's "only three firms on earth" phrasing should be softened.

### Claim 3 — CONFIRMED
**Claim:** Q3 2026 sales $10.23B (+65%, +37% organic), adj EPS $0.80 (+74%); FY2026 guidance $36.9–37.1B sales, $2.82–2.84 EPS.

**Evidence:**
- Amphenol press release / SEC Form 8-K Ex. 99.1, Oct 28, 2026: "Sales of $10.2 billion, up 65% in U.S. dollars and 37% organically compared to the third quarter of 2025"; "Adjusted Diluted EPS of $0.80, up 74% compared to prior year." Full-year outlook: "sales to be in the range of $36.9 billion to $37.1 billion… Adjusted Diluted EPS… in the range of $2.82 to $2.84."
- Morningstar/Dow Jones, Oct 28, 2026: "Revenue jumped 65% to $10.23 billion… adjusted per-share earnings were 80 cents… For the full year, the company anticipates $36.9 billion to $37.1 billion in sales with $2.82 to $2.84 in adjusted earnings per share."
- Zacks, Oct 28, 2026: "adjusted earnings of 80 cents per share, up 73.9% year over year… Revenues surged 65.1% to $10.23 billion."

No correction needed (the +74% is rounded; precise figure +73.9%).

---

## WST — West Pharmaceutical Services

### Claim 4 — CONFIRMED
**Claim:** HVP Components revenue $466.7m in Q3 2026 (+20.3% organic), GLP-1-linked HVP growing "well into the 30% range" organically; pricing contributed just over 4 points of Q3 growth.

**Evidence:**
- West Q3 2026 earnings call transcript, Oct 29, 2026 (Motley Fool): "HVP Components Revenue — $466.7 million, growing 20.3% organically and accounting for 53% of total company net sales"; "Our GLP-1 HVP business… growing well into the [30s] organically. HVP GLP-1s represented just under 12% of total revenues in the quarter"; "Price contributed just over 4 percentage points of growth in the quarter."
- West Q3 2026 earnings presentation (company deck, Oct 29, 2026): HVP Components net sales $466.7M, +19.7% reported / +20.3% organic, 53% of total sales.
- Nasdaq summary of the call: "GLP-1-related HVP revenue grew well into the 30% range organically and represented just under 12% of West's total quarterly revenue"; "Price contributed slightly more than four percentage points to third-quarter growth."

No correction needed. Note: the "just over 4 points" is total-company pricing contribution, not HVP-specific — the dossier's wording is consistent with that.

### Claim 5 — CONFIRMED
**Claim:** New finishing capacity takes 18–24 months to come online (Q3 2026 call, Oct 29, 2026).

**Evidence:**
- West Q3 2026 earnings call transcript, Oct 29, 2026 (Motley Fool summary): "The company expects the new finishing capacity expansion to take approximately 18 to 24 months to come online and deliver a meaningful contribution to growth."
- Nasdaq summary: "West is beginning a new round of investments to expand HVP finishing capacity in Europe and the U.S.… the projects… should take about 18 to 24 months to provide a meaningful contribution."
- TipRanks/TradingKey call summaries corroborate the 18–24 month figure.

No correction needed. Precision note: management's wording is "approximately 18 to 24 months to come online and deliver a meaningful contribution" — i.e. to *meaningful contribution*, not necessarily first output. The dossier's phrasing matches.

### Claim 6 — CONFIRMED
**Claim:** Q3 2026: sales $874.5m, adj EPS $2.66 (+35.7%); FY26 guidance raised to $3.41–3.42bn sales and $9.38–9.48 adj EPS.

**Evidence:**
- West press release, Oct 29, 2026 (PR Newswire / Nasdaq): "Net sales of $874.5 million increased 8.7%; organic growth was 11.9%"; "Adjusted-diluted EPS of $2.66 increased 35.7%"; "Full-year 2026 net sales guidance increased to a range of $3.41 billion to $3.42 billion, up from the previous range of $3.345 billion to $3.380 billion"; "Full-year 2026 adjusted-diluted EPS guidance increased to a range of $9.38 to $9.48, up from the previous range of $8.85 to $9.05."
- Zacks, Oct 29, 2026, corroborates all four figures.

No correction needed.

---

## LLY — Eli Lilly

### Claim 7 — CONTRADICTED (in part)
**Claim:** The FDA declared the tirzepatide/semaglutide GLP-1 shortage ended in Dec 2024; there is currently no Zepbound shortage.

**Evidence — tirzepatide (confirmed):**
- FDA Declaratory Order / Decision Memorandum, Dec 19, 2024: "FDA determines that the tirzepatide injection product shortage is resolved." The FDA had first removed tirzepatide from the shortage list on Oct 2, 2024, then re-evaluated and reaffirmed the resolution on Dec 19, 2024.

**Evidence — semaglutide (contradicted date):**
- FDA Declaratory Order, **Feb 21, 2025**: "FDA has determined that the semaglutide injection product shortage is resolved" (Ozempic/Wegovy). The semaglutide shortage was **not** declared ended in December 2024.
- **Correction:** tirzepatide shortage resolved Dec 19, 2024; semaglutide shortage resolved Feb 21, 2025. The claim conflates the two molecules' resolutions into a single December 2024 date.

**Evidence — no current Zepbound shortage (confirmed in substance):**
- The FDA's December 2024 determination stands; tirzepatide remains off the FDA shortage list. Practical Telehealth (2026): "According to the federal government, there is no Zepbound shortage right now… FDA determined that the tirzepatide injection shortage… was resolved on December 19, 2024." WeightWatchers (updated Nov 5, 2026), cited in the dossier, notes "the FDA reports that there is not currently a shortage of Zepbound."
- Caveat (from the FDA's own Dec 2024 memorandum): the FDA acknowledged that "some individuals may still be currently encountering" difficulty filling prescriptions at individual pharmacies — the resolution is a national supply/demand determination, not a guarantee of local availability for every dose/strength.

**Overall verdict:** CONTRADICTED on the combined December 2024 date; the "no Zepbound shortage currently" half is confirmed. The dossier's underlying point (the shortage thesis is over) survives the correction.

### Claim 8 — CONFIRMED
**Claim:** Q3 2026 revenue $24.4B (+39% YoY); Mounjaro $10.7B (+65%), Zepbound $5.35B (+49%).

**Evidence:**
- Lilly press release / SEC Form 8-K Ex. 99.1, Oct 29, 2026: "Revenue in Q3 2026 increased 39% to $24.4 billion"; total revenue $24,397m vs $17,601m (+39%); Mounjaro $10,723m (+65%); Zepbound $5,352m (+49%).
- WSJ, Oct 29, 2026: "sales for Mounjaro gained 65% year over year to $10.72 billion, while Zepbound sales climbed 49% to $5.35 billion… overall revenue up 39% to $24.4 billion."
- Zacks/Nasdaq corroborate: "Revenues surged 39% year over year to $24.40 billion… Mounjaro revenues climbed 65% to $10.72 billion, while Zepbound sales increased 49% to $5.35 billion."

No correction needed. Minor precision note: the +49% is the worldwide Zepbound figure; U.S.-only Zepbound grew 48% — the dossier's 49% is the correct worldwide number.

### Claim 9 — CONFIRMED (with trial-name correction)
**Claim:** Retatrutide beat semaglutide head-to-head in Phase 3 (weight loss ~20–21% vs ~9.4%) with FDA filing planned Q1 2027.

**Evidence:**
- Lilly topline results, Oct 28, 2026 (reported by AJMC and others): in **TRANSCEND-T2D-2**, the first Phase 3 head-to-head trial of retatrutide vs semaglutide, 1,298 adults with type 2 diabetes — retatrutide 12 mg: **20.9%** weight loss at 80 weeks; retatrutide 9 mg: 19.5%; semaglutide 2 mg (Ozempic): **9.4%**. HbA1c fell 2.2 points on retatrutide vs 1.8 on semaglutide. All figures on the efficacy estimand (as if participants stayed on treatment 80 weeks).
- Filing timing: Lilly's Sep 29, 2026 release (TRIUMPH-1/TRIUMPH-2 publications) repeated the plan "to submit retatrutide to the FDA in the first quarter of 2027"; TalkMarkets (Nov 2026) and retaweightloss.com tracking confirm "US filing planned for the first quarter of 2027" and that, as of Nov 18, 2026, retatrutide had not yet been submitted.

**Corrections / caveats for the memo:**
1. **Trial name:** the head-to-head trial is **TRANSCEND-T2D-2**, not TRIUMPH-1. TRIUMPH-1 was placebo-controlled (retatrutide 12 mg 28.3% vs placebo 2.2% at 80 weeks, efficacy estimand). The dossier attributes the head-to-head win to the right programme but the wrong trial name in places.
2. The dossier's "up to 22.6% weight loss in TRIUMPH-1" does not match any published TRIUMPH-1 figure I found (28.3% efficacy estimand / 25.0% treatment-regimen estimand at 12 mg, NEJM Sep 29, 2026). That 22.6% figure is unverified and should be dropped or re-sourced.
3. The Oct 28, 2026 results are **topline press-release data**, not yet published in a peer-reviewed journal; detailed results were promised for a future medical meeting/publication.
4. The trial population was adults **with type 2 diabetes** (on metformin ± SGLT2 inhibitor), not the general obesity population — the ~20.9% figure should not be quoted as the obesity-population result (that is TRIUMPH-1's 28.3%).

---

## Observations outside the nine claims (for the panel, not verdicts)

- **APH screen price is stale:** the dossier's screen price for APH ($69.72) is the Fri Nov 20 close; Finnhub data shows APH closed at $77.41 on Mon Nov 23 (+11.0% in one session). The panel's upside/valuation framing for the tentative pick is therefore based on a stale price — worth flagging, though it was not one of the nine claims.
- **Claim 1's $5.7B YTD backlog figure** is a secondary-source derivation (Aardvark Labs), not a company-stated total; it checks out arithmetically but should be cited as such if repeated.
- No claim required a fabrication warning: every figure except the two noted conflations traced to a primary source (SEC filing, company release/transcript, or FDA order) or a close secondary summary of one.

## Sources consulted (independent of the dossier)

- Amphenol Q3 2026 earnings call transcript, Oct 28, 2026 (Motley Fool; AlphaStreet; MarketBeat)
- Amphenol press release, SEC Form 8-K Ex. 99.1, Oct 28, 2026 (sec.gov)
- Aardvark Labs, "Amphenol (APH) Q3 2026 Earnings Recap," Oct 28, 2026
- Trefis, "How Much Of Amphenol Stock Rides On One Market?", Nov 19, 2026
- Morningstar/Dow Jones, "Amphenol Ramps Acquisitions as 3Q Sales Climb," Oct 28, 2026
- Zacks, Amphenol Q3 2026 coverage, Oct 28 / Nov 6, 2026
- Markets NXT, "U.S. Cable Connector Market Size, Share & Forecast 2026–2032"
- PNA Fiber, "224G/448G Interconnects: 800G Optics & MPO Cabling," July 26, 2026
- NexPCB, Week 41 supply-chain note (data as of Oct 9, 2026)
- West Pharmaceutical Q3 2026 earnings call transcript, Oct 29, 2026 (Motley Fool; AlphaStreet; StockAnalysis)
- West Pharmaceutical Q3 2026 earnings presentation (company deck), Oct 29, 2026
- West Pharmaceutical press release, Oct 29, 2026 (PR Newswire; Nasdaq; SEC 8-K)
- Zacks, "West Pharma Q3 Earnings Rise on HVP Strength," Oct 29, 2026
- FDA Declaratory Order: Resolution of Shortages of Tirzepatide Injection Products, Dec 19, 2024 (fda.gov)
- FDA Declaratory Order: Resolution of Shortages of Semaglutide Injection Products, Feb 21, 2025 (fda.gov)
- Practical Telehealth, "Zepbound Shortage 2026," 2026
- Eli Lilly press release / SEC Form 8-K Ex. 99.1, Q3 2026 results, Oct 29, 2026 (sec.gov)
- WSJ, "Eli Lilly Revenue Climbs on Demand for Obesity Drugs," Oct 29, 2026
- Zacks/Nasdaq, LLY Q3 2026 earnings coverage, Oct 29, 2026
- Lilly retatrutide TRANSCEND-T2D-2 topline results, Oct 28, 2026 (via AJMC; rxpeptideswatchdog; getmealcoach)
- Lilly retatrutide filing-plan tracking, Sep 29 / Nov 18, 2026 (retaweightloss.com; TalkMarkets)
