> Run by: Muse Spark 1.3 (muse-spark-1.3) — full panel

# Stock-pick-momentum — Research Batch 1 — Run date 2026-11-11

Tickers: ANET (Arista Networks), LLY (Eli Lilly), NEM (Newmont), VLO (Valero Energy).
Screen context (2026-11-11 screen run, supplied in brief): ANET $188.26, rev +36.2%, op margin 44.9%, 12m +39.8%, analyst upside +32.3%, fwd PE 31.4x, next earnings 2027-02-09. LLY $1,415.22, rev +38.5%, op margin 53.7%, 12m +54.1%, analyst upside +2.7%, fwd PE 28.0x, next earnings 2027-02-03. NEM $119.61, rev +20.3%, op margin 50.0%, 12m +44.8%, analyst upside +13.1%, fwd PE 12.0x, next earnings 2027-02-18. VLO $349.94, rev +18.5%, op margin 20.5%, 12m +103.5%, analyst upside +22.0%, fwd PE 6.5x, next earnings 2027-01-28.
Prices verified 2026-11-10 close (Finnhub / MarketBeat / FundSpec): ANET $185.02 (-0.62%), LLY $1,432.29 (+1.44%), NEM $119.96, VLO $350.71 (-1.69%). All four close to screen prices; ANET ~15% below its 52-week high $217.41 (10 Oct 2026), VLO ~24% below its 52-week high $461.52 (14 Oct 2026), LLY ~1% below its 52-week high $1,453.00 (5 Nov 2026), NEM ~11% below its 52-week high $135.29 (25 Aug 2026).
Sources: primary — company Q3 2026 earnings releases / calls (ANET 3 Nov 2026, LLY 29–30 Oct 2026, NEM 22 Oct 2026, VLO 22 Oct 2026); secondary — reputable press / SEC-filing analyses cited with dates. "Not found" is stated where a figure could not be verified. No numbers fabricated.

---

## 1. ANET — Arista Networks

**Price:** $185.02 at 2026-11-10 close (Finnhub/MarketBeat); screen $188.26. 52-week range $114.52–$217.41.

### 1. Shortage thesis
Yes — AI-datacenter Ethernet fabric demand is outrunning supply, and Arista is the bottleneck beneficiary, not the bottleneck itself. CEO Jayshree Ullal on the Q3 call (3 Nov 2026): "In 2026, we are in the AI super cycle, with more than 100 Ethernet AI customers. By the end of 2027, we forecast more than 10 gigawatts of deployments across more than 10 different types of compute accelerators." That is up from "four or five" Ethernet AI customers at the start of the AI journey. The market corroborates: Dell'Oro via secondary reporting — AI back-end switch spending exceeded traditional front-end switch spending for the first time in Q2 2026; the data-center Ethernet switch market hit $15.4bn in Q1 2026 alone, +39.8% YoY, "a growth rate almost entirely attributable to AI cluster build-outs." Arista's own constraint is upstream silicon/memory/PCB capacity, not end demand: COO Todd Nightingale said Arista has "made large-scale long-term strategic agreement investments in silicon, PCB capacity and memory" and "we don't place orders five quarters ahead for all orders" — i.e. it is pre-buying scarce inputs. CFO Chantelle Breithaupt: purchase commitments rose to $11.4bn at 30 Sep 2026 (see §2). Demand visibility is only ~2 quarters, so the "shortage" is a demand surge with a supply race, not a multi-year locked order book.

### 2. Backlog / order book
Arista does not publish a formal backlog figure. Closest proxies, all from the Q3 2026 release/call (3 Nov 2026):
- Purchase commitments (Arista's own orders to suppliers, a demand-confidence proxy): **$11.4bn at 30 Sep 2026**, up from $9.7bn at 30 Jun 2026 (+17.5% QoQ) and $6.8bn at 31 Dec 2025 (+68% in 9 months). CFO said commitments "mostly represented chip purchases for new products and AI deployments" and are expected to rise somewhat further by end-Q4.
- Deferred revenue: **$6.84bn** at 30 Sep 2026, first quarterly decline since 2024 (was ~$6.87bn in Q2); management declined to forecast it and said it should end 2026 higher than the prior year.
- Inventory: $3.21bn, +$674.5m in Q3, built ahead of demand.
- Forward revenue guide as a demand proxy: FY2026 raised to ~$13.3bn; **first-time FY2027 revenue guidance ~$18.5bn (+38–40% YoY)**, vs Bloomberg consensus ~$16.4bn — a ~$2.1bn beat on guidance alone. AI networking targeted at ~$7.0bn in 2027, doubling from ~$3.5bn in 2026; cognitive campus ~$2.0bn in 2027 (+60% vs ~$1.25bn in 2026).
- How far out booked: not found as a stated backlog duration. Management explicitly has only ~2 quarters of demand visibility; the rest of 2027 rests on "customer conversations."

### 3. Category position
#1 in high-performance / high-speed data-center switching; not #1 in overall data-center switching by revenue. Verified Market Research (Feb 2026, Q1 2026 report): Cisco ~21.4% share, Arista ~18.2% in the overall data-center switch market. But in the hyperscale / AI segment Arista is the leader: "Arista has surpassed Cisco in market share for high-speed data center switching" (Network World via Free Library, 2026); "the definitive leader in high-performance cloud networking… the primary beneficiary of the 800G transition" (VMR). The disruptor to watch: Nvidia's Spectrum-X pushed its data-center Ethernet share "from under 4% to roughly 21.5% in about a year, per IDC data" (The CODEW, 5 Aug 2026) — i.e. Nvidia is now roughly tied with Cisco at the top on that IDC cut, ahead of Arista on total Ethernet revenue. Cisco is catching up: ~$9.3bn in hyperscaler AI infrastructure orders in fiscal 2026, ~4.5x fiscal 2025 (Active Trader Daily, 2 Nov 2026).

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 6/10.**
Moat: EOS (Extensible Operating System) software + CloudVision, deep co-design with Microsoft/Meta/Oracle, ultra-low-latency engineering, and the spine-leaf architecture Arista pioneered — now standard in large data centers. Switching at 800G/1.6T (Etherlink portfolio, June 2026 1.6T launch on Broadcom Tomahawk 6, up to 100 Tbps) is genuinely hard; only a handful of firms can ship it at hyperscale quality.
Threat — concrete and live: (a) Arista does **not** own the silicon. Its switches run on Broadcom merchant silicon (Tomahawk 5/6); Broadcom "indirectly influences over 60% of all data center switch ports globally through silicon supply" (VMR). A hyperscaler can buy the same Broadcom ASIC, a Celestica white-box switch, third-party optics and open software — "One customer can combine a Broadcom ASIC, a Celestica switch, third-party optics and open software" (NewMarketPitch, 6 Oct 2026). Celestica already leads AI Ethernet switch shipments by volume, albeit at single-digit margins. (b) Nvidia is the in-sourcing threat in another form: Spectrum-X + InfiniBand bundles switching with its GPUs, and hyperscalers buying Nvidia racks get Nvidia networking by default. (c) Hyperscalers design their own networks — "Hyperscalers designing more of their own networks will hurt vendors whose main advantage is selling an expensive proprietary box" (same source). Arista's defence is that its value is software + integration + proven scale, not the box — but that is a softer moat than a silicon or patent monopoly. Scale-up fabrics (production expected 2028) are still in early trials for 2027, so the next architecture battle is unsettled. Open CPO (co-packaged optics) not expected until 2028–2030.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, 3 Nov 2026 — large beat + guidance bombshell:** revenue $3.66bn, +58.5% YoY (highest YoY growth since IPO), vs guidance ~$3.3bn and consensus $3.33bn; non-GAAP EPS $1.20 vs $1.08 consensus; GAAP operating margin 44.9%; product revenue $3.19bn, +66.9%. Non-GAAP net income $1.53bn, +56% YoY.
- **First-time FY2027 guidance ~$18.5bn (+38–40%)**, well above ~$16.4bn consensus; AI fabrics ~$7bn (2x 2026), campus ~$2bn; gross margin 62–64%, operating margin ~49%.
- FY2026 guidance raised (fourth raise of the year, per AlCapitalAdvisory 10 Nov 2026) to ~$13.3bn.
- 800G/1.6T Etherlink momentum; >100 Ethernet AI customers; >10 GW deployments forecast by end-2027.
- Stock paradox: despite the beat, ANET is ~15% off its 9 Oct 2026 high ($217.41) and -12.3% over 1 month to 10 Nov — the market had priced much of it, and the Q3 print came after a ~20% drawdown from the high (Active Trader Daily, 2 Nov 2026).

### 6. Risks
- **Customer concentration is extreme:** two largest end customers were 26% + 16% = 42% of FY2025 revenue (10-K), up from 35% in FY2024; management expects 3–4 customers above 10% of 2026 revenue. Losing or delaying one hyperscaler program moves the year.
- **No moat on silicon;** Broadcom, Nvidia (Spectrum-X/InfiniBand), Cisco (Silicon One G300) and white-box/Celestica all attack the same socket; open standards (Ultra Ethernet Consortium 1.0, June 2025) commoditise the fabric over time.
- **Visibility only ~2 quarters;** H2 2027 depends on conversations, not orders. Any AI-capex pause, GPU-supply delay, or power/cooling constraint (liquid cooling now a mainstream requirement) hits Arista first.
- **Valuation already prices a super-cycle:** ~45x trailing earnings (Finnhub, 10 Nov 2026), fwd PE 31.4x per screen; the stock fell ~20% from its high into earnings despite a record quarter — expectations are the risk.
- Gross margin guided down to 62–64% (from 64.0% non-GAAP in Q3) on large-order discounts and product costs.

### 7. Shortage score & verdict
**Shortage score: 8/10. Irreplaceability: 6/10.**
**Verdict:** The purest AI-networking demand surge in this batch — record growth, a $2bn-above-consensus 2027 guide and $11.4bn of supplier commitments — but it is a demand surge Arista must keep winning quarter by quarter against Nvidia, Cisco and white-box, with only ~2 quarters of visibility and 42% of revenue in two customers.

---

## 2. LLY — Eli Lilly

**Price:** $1,432.29 at 2026-11-10 close (Finnhub/MarketBeat); screen $1,415.22. 52-week range $850.51–$1,453.00; ~1% below the high.

### 1. Shortage thesis
Yes — structural demand surge for tirzepatide (Mounjaro/Zepbound) that supply is still racing to meet, now amplified by coverage expansion. Q3 2026 (reported 29 Oct 2026): worldwide volume +53% YoY, revenue +39% to $24.40bn. CFO Lucas Montarce: incretin penetration is only ~1 in 10 eligible patients in the US and ~2 in 100 internationally — "substantial opportunities for future expansion." The Medicare GLP-1 Bridge programme (launched 1 July 2026) has already filled >500,000 Lilly prescriptions; ~70% of new Bridge patients choose a Lilly medicine, ~80% are new to incretins. Capacity is the constraint Lilly is spending to remove: broke ground on a **$6.5bn site in Houston and a $5bn site in Richmond**; ten new US sites announced since 2020 (Medium GLP-1 update, Nov 2026; Zacks, 30 Oct 2026). A secondary source notes the new Texas/Virginia capacity is being built "to meet persistent global supply constraints" (Panabee, Q3 2026 summary). Note the nuance: this is no longer the 2023–24 FDA-shortage-list scarcity — it is demand growth + access expansion outrunning a multi-year capacity build, with realised prices falling as access widens (see §6).

### 2. Backlog / order book
Not applicable in the usual sense — pharma has no order backlog; demand is measured in prescriptions and volume. Closest equivalents:
- **Tirzepatide Q3 2026: $16.1bn in the quarter** (Mounjaro $10.72bn, +65% YoY; Zepbound $5.35bn, +49% YoY), ~66% of Lilly's total revenue. Mounjaro is "likely the best-selling drug in the world right now" (The Closing Print, 29 Oct 2026); non-US Mounjaro sales +93% to $5.7bn, now >50% of Mounjaro total; first medicine in China to exceed $1bn in its first full year.
- **Oral Foundayo (orforglipron): $184m in Q3**, below ~$217–229m expected; Lilly says Foundayo wins ~4 in 10 new oral starts (Medium, Nov 2026).
- **Guidance as forward demand:** 2026 revenue guidance raised to **$91–92bn** from $85–87bn (+$5.5bn at midpoint) — the third raise this year; cumulative increase since January ~$10bn (Medium, Nov 2026).
- Prescription share: Lilly ~6 in 10 US obesity incretin prescriptions, >7 in 10 injectable prescriptions, >60% of type-2-diabetes incretin prescriptions; ~58% share outside the US by IQVIA gross sales (Medium, Nov 2026).
- No backlog duration figure exists — not found, and not a meaningful metric for this name.

### 3. Category position
#1, and pulling away. Q3 2026 GLP-1 revenue: **Lilly ~$16.3bn vs Novo Nordisk ~$9.4bn (DKK 60.9bn)** — Lilly leads ~1.7x; Lilly revenue +39% vs Novo adjusted sales +4% at constant exchange rates (Medium, Nov 2026). Tirzepatide's dual GIP/GLP-1 mechanism beats semaglutide head-to-head (SURMOUNT-5: greater average weight reduction than semaglutide). Retatrutide (next-gen triple agonist) "roughly doubled Ozempic's weight loss head to head" and has now succeeded in six Phase 3 trials (The Closing Print, 29 Oct 2026). The only segment where Lilly trails: oral — Novo's Wegovy pill still leads in US prescriptions, and Foundayo missed Q3 expectations.

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 8/10.**
Moat: (a) **Patents:** tirzepatide US composition-of-matter patent (US 10,034,938) runs to **13 May 2036** (US), 2037 in major European countries, 2040 in Japan; later method patents to 2041 (Patenta.ai, sources checked 22 Oct 2026; DrugPatentWatch, updated 10 Aug 2026). Generic challengers filed Paragraph IV from May 2026; Lilly sued 14 generic companies in Delaware on 6 Aug 2026; 30-month stay ends 13 Nov 2029 — but the dispute is over the 2039–41 patents, with the compound patent to 2036 unchallenged in those cases. (b) **Manufacturing scale as a moat:** peptide manufacturing at this volume, plus the $11.5bn Houston+Richmond build and ten new US sites since 2020, is a capital-intensity barrier few can replicate quickly; Novo actually cut 2026 capex guidance (DKK ~55bn → ~50bn). (c) **Clinical superiority:** dual-agonist efficacy + retatrutide pipeline.
Threats: no customer can "in-source" a patented drug — disintermediation here means substitution, not self-manufacture. Real substitutes: Novo's semaglutide (patent to 2031–32 US; generics already in India/Canada/Brazil since Mar 2026), oral Wegovy (FDA-approved 22 Dec 2025), and future oral/next-gen entrants; compounded tirzepatide (legally contested); and eventual 2036 patent expiry. Also payer power: realised prices fell 15% globally in Q3 (US -7%, ex-US -29%) as access expanded — the "customer" (payers/governments) can squeeze price even if it cannot make the drug. Score 8, not 10, because the moat is time-limited (2036) and price is set by negotiation, not by Lilly alone.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, 29 Oct 2026 — big beat + guidance raise:** revenue $24.40bn (+39% YoY) vs ~$22.1–22.6bn expected; non-GAAP EPS $7.48 vs ~$5.38–6.36 expected (+39% vs Zacks consensus, +7% YoY despite $4.57/share of acquired IPR&D charges); Mounjaro +65%, Zepbound +49%; 2026 revenue guidance raised $5.5bn to $91–92bn. Non-GAAP gross margin 84.4% (+80 bps).
- **Retatrutide head-to-head win** vs Ozempic 2 mg announced a day before earnings (28 Oct 2026) — roughly double the weight loss; six Phase 3 wins including sleep-apnoea severity cuts.
- **Foundayo (oral orforglipron) FDA-approved 1 Apr 2026**, commercial ramp underway ($184m Q3); ~4 in 10 new oral starts.
- **Manufacturing:** Houston $6.5bn + Richmond $5bn groundbreakings; ten new US sites since 2020.
- **Medicare GLP-1 Bridge:** >500,000 fills since 1 July 2026 — a coverage catalyst still scaling.
- Acquisitions (AtaiBeckley, Merida Biosciences) for pipeline beyond obesity — $4.2bn IPR&D charges in Q3.
- Stock: +21.5% in 1 month to 10 Nov 2026, +54.9% over 1 year (Finnhub); at $1,432 it sits ~1% below its 52-week high.

### 6. Risks
- **Price, not volume, is the leak:** realised prices -15% globally in Q3 (US -7%, ex-US -29%, incl. China NRDL listing); if volume growth normalises, margin expansion stalls. ~$900m of Q3 revenue was one-off (Jardiance milestones $410m + rebate adjustments) and won't repeat.
- **Concentration:** tirzepatide is ~66% of revenue; the whole thesis is one molecule (plus its follow-ons).
- **Oral race:** Foundayo missed expectations and Novo's oral Wegovy leads US oral prescriptions; orforglipron's ~11.2% weight loss at top dose (ATTAIN-1, 72 weeks) is well below injectable tirzepatide's ~21%.
- **Generics / compounding / patent challenges:** semaglutide generics already live in India, Canada, Brazil; tirzepatide Paragraph IV litigation underway (stay to Nov 2029); political/payer pressure on GLP-1 prices is a standing risk.
- **Valuation:** ~46x trailing earnings (Finnhub, 10 Nov 2026), fwd PE 28.0x per screen, market cap ~$1.27–1.35tn; analyst upside only +2.7% per screen — the market has largely priced the beat, and the stock is at its highs.

### 7. Shortage score & verdict
**Shortage score: 7/10. Irreplaceability: 8/10.**
**Verdict:** The strongest moat in the batch — #1 by 1.7x, patented to 2036, with a demand runway (1-in-10 US penetration) and a $5.5bn guidance raise — but the "shortage" is now a capacity race with falling realised prices, not a price-setting scarcity, and at ~1% below its all-time high with only +2.7% analyst upside, the explosive-return case needs the retatrutide / oral leg to re-rate it, not just another tirzepatide beat.

---

## 3. NEM — Newmont

**Price:** $119.96 at 2026-11-10 close (Finnhub); screen $119.61. 52-week range $81.34–$135.29.

### 1. Shortage thesis
Indirect — Newmont sells gold, and gold is in a demand surge, but Newmont itself cannot make more gold quickly; the "shortage" is in the commodity, and Newmont is a price-taker on it. The demand facts are strong: spot gold touched an intraday record **$5,594.82/oz on 29 Jan 2026**; central banks bought an estimated **321 tonnes in Q3 2026, +42% YoY**, well above the 5-year quarterly average of 227 tonnes, 675 tonnes in the first 9 months of 2026 (World Gold Council, Gold Demand Trends Q3 2026, published 3 Nov 2026); China added 25.8 tonnes in October, its 24th straight month of buying; gold ETFs took in 211 tonnes in Q3 (a record $31bn) and holdings hit a month-end record 4,275 tonnes in October (Discovery Alert / Bloodstone Research, Nov 2026). Bank forecasts cluster $4,800–$5,400/oz by end-2027 (Goldman cut to $4,800 on 5 Nov; UBS $5,400 by Sep 2027). But the timing cuts against a simple shortage story: gold is **~27% below its January record** — $4,060.20 at the 6 Nov 2026 close, after breaking below $4,000 on 30 Oct 2026 on margin calls / liquidations (~$8bn of positions liquidated 20–27 Oct). Newmont's realised price in Q3 was $4,317/oz (vs $3,539 a year ago), still far above its $1,454/oz AISC — the margin is the story, not volume growth. Mine supply is structurally slow: "It takes years to get gold out of the ground" and senior-producer output is in long-term decline (Q2 2026 peer output -5% YoY).

### 2. Backlog / order book
Not applicable — gold miners have no order backlog; gold sells at spot. The analogue is **reserves + production guidance**:
- **Reserves: 118.2 million attributable gold ounces at end-2025** (reported 19 Feb 2026), down from 134.1 Moz at end-2024 mainly on 2025 divestments; plus 12.5 Mt copper and 442 Moz silver reserves. Newmont states this is "the industry's largest gold reserve base… representing decades of production life" and "gold reserve life of ten years or more" at ten named sites (Lihir, Cadia, Tanami, Boddington, Ahafo North, Merian, Cerro Negro, Brucejack, Nevada Gold Mines, Pueblo Viejo). At ~5.3 Moz/year production, 118.2 Moz ≈ ~22 years of output.
- Measured & Indicated resources 88.1 Moz + Inferred 60.6 Moz (at $2,300/oz).
- **Production guidance 2026: ~5.3 Moz** (5.26 Moz per Q3 release); Q3 produced 1.30 Moz (-8.4% YoY), plus 11 Moz silver and 23 kt copper. Q4 guided ~1.4 Moz (strongest quarter of the year). **2027: production growth of only low- to mid-single-digit %** vs 2026, with unit costs expected to rise.
- Growth projects: Tanami Expansion 2 — shaft construction complete, commercial production now expected H1 2027 (ahead of schedule); Red Chris Block Cave — investment decision early 2027, development capital **$4.2–4.8bn (100% basis)**, commercial production **2033** — i.e. the next big volume leg is seven years out.
- No backlog figure — not found, and not a meaningful metric for a gold miner.

### 3. Category position
#1 by production and by reserves. **2025 attributable production 5.89 Moz**, "comfortably the largest in the world and roughly 80% more than Barrick" (3.26 Moz); #2 is Agnico Eagle at 3.45 Moz (MoatExplorer / peer comparison, 2025 results). Largest reserve base in the industry (118.2 Moz, Newmont, 19 Feb 2026). UBS identified Newmont as "the preferred senior producer" heading into 2027 on clearer cash-return visibility and reduced M&A risk (Natural Resource Stocks, Nov 2026). Caveat: 2026 production is deliberately lower (~5.3 Moz vs 5.89 Moz in 2025, -10%) after divestments — a "production dip" — so the #1 lead is narrowing on volume even as reserves stay #1.

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 4/10.**
Gold itself is irreplaceable as a monetary/reserve asset — central banks cannot synthesise it, and no substitute (Bitcoin, other metals) has displaced central-bank gold buying. But **Newmont is not irreplaceable**: gold is a fungible commodity; any miner's ounce sells at the same spot price, and buyers (central banks, ETFs, jewellers) do not care whose mine it came from. There is no customer lock-in, no patent, no qualification moat — the moat is scale, reserve life and low costs, all replicable in principle by Agnico, Barrick or a new discovery (in practice slow: years to permit and build a mine, which is a real but weak barrier). No customer can "in-source" gold mining in the hyperscaler sense, but equally Newmont has no pricing power: if gold falls, Newmont falls with it, one-for-one. The score reflects the commodity's irreplaceability (high) discounted by the company's replaceability (high) — the panel question asks about the company, so 4.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, 22 Oct 2026 — beat on every priced line:** adjusted EPS $2.20 vs $1.94–2.05 consensus; revenue $6,363m vs $6.01–6.27bn; record Q3 adjusted net income $2.3bn; adjusted EBITDA $4.0bn; free cash flow $1.9bn in Q3, $7.3bn in the first 9 months of 2026; dividend $0.261/share declared.
- **Cost guidance improved:** full-year by-product AISC cut ~10% to ~$1,520/oz (from $1,680); Q3 AISC $1,454/oz (by-product basis). Note: the improvement came from co-product credits (57% more silver, copper at $6.91/lb), not cheaper gold mining — co-product AISC rose for a fourth straight quarter to $1,963/oz, and Q4 AISC is guided up to ~$1,900/oz (Aardvark Labs, Oct 2026).
- **Nevada dispute settled:** 10 Aug 2026 agreement with Barrick — $1.95bn payment (Q4) puts Fourmile/Fiberline/Mike into Nevada Gold Mines, settles all disputes, modernises governance; removes a major overhang and M&A risk.
- **Tanami Expansion 2 ahead of schedule** (commercial production H1 2027); Red Chris feasibility being finalised for an early-2027 investment decision.
- Gold-macro tailwind: record central-bank buying (Q3) and record ETF holdings (Oct) — see §1.

### 6. Risks
- **Pure gold-price beta:** realised price already fell from $4,317/oz (Q3 avg) toward ~$4,060 (6 Nov close); gold is 27% off its January record after an Oct margin-call sell-off; a stronger US economy / higher-for-longer rates could trigger Western ETF outflows that overwhelm central-bank buying (the stated bear case).
- **Falling production:** Q3 output -8.4% YoY; 2026 guidance ~5.3 Moz vs 5.89 Moz in 2025; 2027 growth only low- to mid-single-digit % with higher unit costs (inflation + lower co-product credits; 2027 silver -30%).
- **Cost creep:** co-product AISC rising four quarters running; Q4 AISC guided ~$1,900/oz; copper Q4 needs +39% vs Q3 to hit guidance — "the guide line most at risk" (Aardvark Labs).
- **Balance sheet:** the $1.95bn Barrick payment in Q4 takes pro-forma net cash to ~$1.3bn, near the $1bn target — the excess that funded 107%-of-FCF shareholder returns in Q3 is now spent.
- **No pricing power, no backlog:** a gold miner cannot raise prices, pre-sell years of output at a premium, or lock in customers. Explosive return requires gold itself to explode.

### 7. Shortage score & verdict
**Shortage score: 5/10. Irreplaceability: 4/10.**
**Verdict:** A leveraged, well-run bet on the gold price — record Q3 profit, $1.9bn quarterly FCF, the world's largest reserve base and a settled Nevada dispute — but production is falling, the next growth mine produces in 2033, and gold itself is 27% off its January high; the "shortage" belongs to gold, not to Newmont, and Newmont cannot price it.

---

## 4. VLO — Valero Energy

**Price:** $350.71 at 2026-11-10 close (Finnhub/MarketBeat); screen $349.94. 52-week range $159.90–$461.52; ~24% below the 14 Oct 2026 high, -19.1% in 1 month.

### 1. Shortage thesis
Yes — the strongest physical-shortage story in the batch, in refined products (especially diesel), not crude. Q3 2026 (reported 22 Oct 2026): Valero's refining margin was **$39.24/bbl of throughput vs $13.14 a year earlier (nearly 3x)**; Gulf Coast margin $37.55/bbl (vs $12.21 in Q3 2025); the Gulf Coast ULSD-over-Brent benchmark averaged **$72.27/bbl vs $21.05** a year ago; the 3-2-1 crack spread was >150% higher on average in Jul–Sep than a year earlier. Drivers (company call + press, Oct 2026): Middle East conflict since late Feb disrupting Strait of Hormuz flows and cutting Middle East product shipments to "below half of pre-war levels" (IEA, Oct Oil Market Report); Russia restricting diesel exports; US diesel hit a record **$5.85/gal in early Sep** (above the 2022 peak), $6.31–6.32/gal national average by late Oct (AAA); US distillate stocks ~102.6–104.3m bbl, well below the 5-year average. Structural: US operable refining capacity **18.04m b/d, down from 18.16m a year earlier** (EIA); refinery utilisation hit **98.0% in late Aug 2026** (EIA weekly), 93.4% in the week to 16 Oct; API CEO: US refiners running at "95% to 100% of capacity" and deferring maintenance. COO Gary Simmons: simpler Asian refiners make only ~$2–3/bbl after freight — "high confidence that this current crack spread environment is very sustainable." IEA expects the diesel market to stay tight "well into 2027" but swing to surplus in Q1 2027. Valero ran at near-record utilisation, ~2.97–3.0m b/d throughput. The shortage is real but war-driven and therefore reversible — see §6.

### 2. Backlog / order book
Not applicable — refiners sell fungible fuel at spot/contract prices; there is no backlog. Closest equivalents:
- **Throughput / utilisation as the demand proxy:** Q3 throughput ~2.97m b/d at near-record utilisation; Q4 throughput guided slightly below Q3 at **2.875–2.975m b/d** (light maintenance quarter).
- **Capacity:** 15 refineries (US, Canada, UK), ~3.2m b/d combined throughput capacity; Gulf Coast >50% of throughput; Port Arthur (435,000 b/d) is the largest in the system. Diamond Green Diesel JV: ~1.2bn gal/year renewable diesel capacity; 12 ethanol plants, ~1.7bn gal/year.
- **Forward margin signal:** none published as a backlog; management's Q4 guidance is conservative (seasonal weakness conceded) and diesel cracks had already dipped below $100 after a record near $112 (Finvestly, Oct 2026).
- No backlog figure — not found, and not a meaningful metric for a refiner.

### 3. Category position
One of the world's largest independent refiners; #1 independent refiner in the US by throughput. Valero operates ~3.0–3.2m b/d across 15 refineries; by comparison Marathon is the largest US refiner overall (~3.0m b/d crude capacity) — Valero vs Marathon for the top independent spot is close and depends on the capacity definition, so "largest independent refiner" is the safe claim, not an unqualified #1. Its edge is complexity and feedstock flexibility: heavy-sour crude processing (514,000 b/d in Q2 2026), Gulf Coast feedstock advantage, and the DGD renewable-diesel JV (one of the world's largest renewable diesel producers). No market-share figure in the sources that is clean enough to quote — not found as a single % share; the US refining market is fragmented among Valero, Marathon, ExxonMobil, Chevron, Phillips 66 and others.

### 4. Irreplaceability / disintermediation risk
**Irreplaceability score: 5/10.**
Moat: (a) **Capital intensity + permitting:** a new refinery takes years and billions and essentially no new US refinery has been built in decades; US capacity is shrinking as older plants close (Benicia 145,000 b/d idled Apr 2026; six large refineries shut/idled since 2020 total ~1.2m b/d, ~7% of US capacity). That scarcity is Valero's moat — it owns scarce, complex, permitted capacity that cannot be built quickly. (b) **Complexity/feedstock flexibility:** heavy-sour, discounted crudes (incl. Venezuelan intake — up to 6.5m bbl planned in March 2026, largest since sanctions began 2019) widen its margin vs simple refiners earning $2–3/bbl. (c) Gulf Coast export optionality (jet-fuel arbitrage to Europe).
Threats: the product is a pure commodity — gasoline/diesel molecules are identical whoever refines them; no customer is locked in, no patent, no brand premium. Customers (drivers, airlines, traders) cannot "in-source" refining at scale, but they can buy from any refiner, import product, or — over time — substitute (EVs, SAF, renewable diesel). Policy can also disintermediate: a US refined-product export ban was discussed ahead of the midterms, and the Trump administration's 16 Oct 2026 waiver for Russian petroleum products (Graham Act) directly narrows the diesel shortage — Simmons said Russian diesel exports would only bring volume back to July levels and the market would still be short 600,000–700,000 b/d, but the direction is against Valero. Score 5: scarce physical capacity that is hard to replicate, selling a fully fungible product with zero pricing power beyond the crack spread.

### 5. Recent catalysts (last ~3 months)
- **Q3 2026 earnings, 22 Oct 2026 — record quarter:** net income **$6.8bn ($23.89/share)** vs $1.1bn ($3.53) a year earlier; adjusted EPS $23.90 vs $21.28 consensus (Zacks) and $3.66 a year ago; revenue $46.1bn, +43.3% YoY; refining operating income $8.8bn (vs $1.6bn); operating cash flow ~$6.9bn. Net debt-to-capitalisation 4% at 30 Sep 2026.
- **Renewable diesel turnaround:** DGD operating income $353m vs -$28m loss a year ago; ethanol $272m (vs $183m) on record production 4.8m gal/day.
- **St. Charles FCC optimisation completed** on schedule and within budget; Port Arthur diesel hydrotreater (damaged Mar 2026, ~$250m repair, largely insurance-covered) expected back by year-end.
- **2026 capex guidance maintained ~$2.0bn;** Q4 is a light-maintenance quarter, supporting high utilisation.
- Stock action cuts the other way: VLO hit a 52-week high $461.52 on 14 Oct 2026, then fell ~24% to $350.71 by 10 Nov (-19.1% in 1 month, -8.1% in 5 sessions) as diesel cracks cooled from their peak — the market is already pricing mean reversion.

### 6. Risks
- **Cyclicality is the whole thesis in reverse:** crack spreads are set by markets, not refiners; the Q3 margin ($39.24/bbl) is ~3x a year ago and driven by war (Iran, Ukraine/Russia) — a ceasefire, a Russian-export waiver, an SPR release, or an export ban compresses it fast. Diesel cracks already dipped below $100 from ~$112; IEA sees a diesel surplus in Q1 2027.
- **Valuation on peak earnings is a trap:** fwd PE 6.5x per screen looks cheap only if $23.90/quarter EPS persists — it will not if cracks normalise; TTM PE ~7.9x (Finnhub) on the same peak earnings. Consensus 2026 EPS ~$51 (Tamim, Oct 2026) embeds the windfall.
- **Demand destruction / policy:** $6.31/gal diesel invites political intervention (Washington pushing refiners for more diesel; export-ban discussion; Russian-product waiver on 16 Oct 2026); high prices also accelerate EV/SAF substitution at the margin.
- **Operational:** Port Arthur DHT repair (~$250m), Benicia idled Apr 2026 (145,000 b/d, restart "a tough challenge" per Argus via ENB); unplanned outages at high utilisation are more likely when maintenance is deferred.
- **Renewable diesel exposure:** DGD margins hinge on D4 RIN values, feedstock-pricing lags, tax-credit eligibility for foreign feedstocks, and the DGD 3 outage — all flagged by management on the Q3 call.

### 7. Shortage score & verdict
**Shortage score: 9/10. Irreplaceability: 5/10.**
**Verdict:** The most acute physical shortage in the batch — diesel at record pump prices, 98% refinery utilisation, shrinking US capacity and a $39.24/bbl margin — but it is a war-driven, mean-reverting crack spread, not a structural moat: the stock is already -24% off its October high as cracks cool, and a single policy headline (Russian waiver, export ban, SPR release) can cut the thesis in half.

---

## Summary table

| Ticker | Shortage score | Irreplaceability | Verdict in one line |
|---|---|---|---|
| ANET | 8/10 | 6/10 | Purest AI-networking demand surge — record growth and a $2bn-above-consensus 2027 guide — but only ~2 quarters of visibility, 42% of revenue in two customers, and no silicon moat. |
| LLY | 7/10 | 8/10 | Strongest moat in the batch (#1 by 1.7x, patented to 2036, 1-in-10 penetration) — but the shortage is now a capacity race with falling prices, and the stock is at its highs. |
| NEM | 5/10 | 4/10 | Leveraged bet on gold with record FCF and the largest reserves — but production is falling, the next mine is 2033, and gold is 27% off its January high. |
| VLO | 9/10 | 5/10 | Most acute physical shortage (record diesel, 98% utilisation, $39/bbl margin) — but a war-driven crack spread already mean-reverting, -24% off its October high. |

**Ranking by shortage score:** VLO (9) > ANET (8) > LLY (7) > NEM (5).
**Ranking by irreplaceability:** LLY (8) > ANET (6) > VLO (5) > NEM (4).
**Explosive-return read (shortage × irreplaceability, qualitative):** ANET and LLY are the two names where a genuine demand surge meets a defensible position; VLO has the hottest shortage but the weakest claim to keep it; NEM is a gold-price proxy, not a company-level shortage.

## Caveats / not found
- No formal backlog/order-book figure is published by any of the four: ANET (purchase commitments $11.4bn used as proxy), LLY/NEM/VLO (no backlog concept; reserves / guidance / throughput used instead). No backlog duration was found for ANET.
- No clean single-% market-share figure was found for VLO (US refining is fragmented); the "#1 independent refiner" claim is used instead.
- ANET's 52-week-high date (9–10 Oct 2026) and VLO's (14 Oct 2026) are from Finnhub/MarketBeat snapshots; LLY's 52-week high $1,453.00 is dated 5 Nov 2026 per Finnhub.
- Analyst-upgrade specifics in the last 3 months were not separately verified for each name beyond the screen's analyst-upside figures (+32.3% ANET, +2.7% LLY, +13.1% NEM, +22.0% VLO); do not treat those as fresh upgrades.
- Prices are 2026-11-10 closes unless stated; pre-market 2026-11-11 prints (ANET ~$193.51, LLY ~$1,417.55, NEM ~$121.96) were volatile and are not used as closes.

## Sources (accessed 2026-11-11)
- ANET Q3 2026: SEC-API filing analysis (results 8-K, 3 Nov 2026); StockRow earnings summary (call 3 Nov 2026); GMT8 Press call summary (4 Nov 2026); Gloom.sh transcript summary (Q3 2026); Active Trader Daily (2 Nov 2026); Verified Market Research data-center switch share (Feb 2026); The CODEW (5 Aug 2026, IDC Nvidia Spectrum-X ~21.5%); NewMarketPitch (6 Oct 2026); Finnhub/MarketBeat/FundSpec price snapshots (10 Nov 2026).
- LLY Q3 2026: Zacks call highlights (30 Oct 2026); The Closing Print (29 Oct 2026); Panabee earnings summary; Medium GLP-1 market update Q3 2026 (Nov 2026); Patenta.ai GLP-1 patent landscape (sources checked 22 Oct 2026); DrugPatentWatch tirzepatide (updated 10 Aug 2026); Finnhub/MarketBeat price snapshots (10 Nov 2026).
- NEM Q3 2026: Newmont press release (22 Oct 2026); Aardvark Labs Q3 recap (Oct 2026); TradingKey call summary (Oct 2026); Newmont 2025 reserves release (19 Feb 2026); World Gold Council Gold Demand Trends Q3 2026 via Discovery Alert / Bloodstone Research (Nov 2026); Finnhub price snapshot (10 Nov 2026).
- VLO Q3 2026: Valero Q3 release via SourceFirst News / Tickeron / Energy News Beat (22 Oct 2026); TradingKey call summary (Oct 2026); Finvestly (Oct 2026); Energy News Beat diesel/restart analysis (19–21 Oct 2026); Tamim (Oct 2026); EIA weekly petroleum data via ENB (weeks to 9/16 Oct 2026); Finnhub/MarketBeat price snapshots (10 Nov 2026).
