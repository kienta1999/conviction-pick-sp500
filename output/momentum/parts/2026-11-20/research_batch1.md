> Run by: Muse Spark (muse-spark-1.3) — full panel

# Momentum research — batch 1 — run date 2026-11-20

Screen prices (from `output/momentum/shortlist_2026-11-20.json`): ANET `\$189.59`, APH `\$75.61`, MSFT `\$498.30`. All three latest prints are for the quarter ended 30 Sep 2026. Sources are primary (company releases / earnings calls / 10-Qs) where stated; secondary press is labelled as such. No figure is fabricated — "not found" is stated where a figure could not be verified.

| Ticker | Screen price | Rev growth TTM | Fwd P/E | Ret 12m | Next earnings |
| --- | --- | --- | --- | --- | --- |
| ANET | `\$189.59` | 35.4% | 31.4 | +53.6% | 2027-02-09 |
| APH | `\$75.61` | 48.8% | 20.9 | +15.0% | 2027-01-27 |
| MSFT | `\$498.30` | 15.0% | 20.6 | +1.9% | 2027-01-27 |

## ANET — Arista Networks

### 1. Shortage thesis

Yes — AI datacentre networking is the bottleneck after compute. CEO Jayshree Ullal on the Q3 2026 call (3 Nov 2026) called 2026 "the AI super cycle, with more than 100 Ethernet AI customers" (up from 4–5 at the start of the cycle) and forecast "more than 10 gigawatts of deployments across more than 10 different types of compute accelerators" by end-2027. Demand is outrunning supply on Arista's side too: management said it had made "large-scale long-term strategic agreement investments in silicon, PCB capacity and memory" and expressed "very high confidence" in supply execution — i.e. supply had to be locked in contractually, not bought spot. The Q3 2025 call had already flagged component lead times of 38–52 weeks; the 2026 call still cited "longer hyperscale lead times" and supply-driven revenue-recognition volatility. Dell'Oro (via SDxCentral, Nov 2026) found Ethernet switch sales in AI back-end networks "more than tripled in 2025", capturing over two-thirds of the datacentre switch market for AI clusters. Driver: AI datacentre buildout — every GPU cluster needs a high-speed Ethernet fabric, and the shift from proprietary InfiniBand to open Ethernet is the structural tailwind.

### 2. Backlog / order book

Arista does not disclose a headline backlog total. The closest hard proxies, Q3 2026 (3 Nov 2026):

- Purchase commitments: USD 11.4 billion, up from USD 9.7 billion in Q2 2026 — management said commitments "could rise further" and they secure silicon/memory for FY2027 deployments.
- Inventory: USD 3.2 billion, up from USD 2.5 billion in Q2, an intentional build for demand.
- Deferred revenue: reported in secondary coverage at about USD 6.9 billion (majority product-related); a Wells Fargo 10-K note put RPO (incl. deferred) at about USD 6.1 billion exiting Q4 2025, ~90% to be recognised within two years. Treat the 2026 deferred figure as secondary-sourced, not primary-verified.
- How far out it is booked: not disclosed as a backlog duration; the FY2027 revenue outlook (USD ~18.5 billion) is the visibility anchor, and purchase commitments are explicitly tied to FY2027 silicon/memory.

### 3. Category position

Not outright #1 in datacentre Ethernet by the latest IDC tracker — it is a tight three-way race, and the leader depends on the quarter and the segment cut:

- IDC Q2 2026 (via EasyFinanceLive, Nov 2026): Nvidia 20.4%, Arista 18.7%, Cisco 18.2% in datacentre Ethernet switching.
- IDC Q1 2026: Nvidia 21.5% (USD 2.1 billion), Arista 20.7% (USD 2.2 billion revenue, +37.3% YoY) — Arista was the top seller of datacentre Ethernet switches from Q4 2023 until Nvidia overtook it.
- Dell'Oro AI back-end ranking (2025): Celestica and Nvidia combined ~50%, Arista third — but Dell'Oro itself notes Arista "would have been more closely tied if deferred AI revenue were included".
- Overall Ethernet (incl. campus): Cisco still leads (~29–30%). Arista is #1 in the cloud/AI datacentre niche historically, now effectively co-leader with Nvidia.

### 4. Irreplaceability / disintermediation risk

Moat: EOS — a single operating system across every product, plus CloudVision as the network system-of-record (configuration, telemetry, compliance state). Switching means re-qualifying and re-automating the whole fleet; Gartner named Arista a Leader with the highest "ability to execute" (Mar–Apr 2025 reports). 150 million cumulative ports shipped (2025) deepen the installed-base lock-in. Open Ethernet / Ultra Ethernet Consortium backing (AMD, Intel, Microsoft, Meta, Google) makes Arista the default non-Nvidia fabric.

Threats are concrete, not theoretical:

- Nvidia Spectrum-X is the #1 datacentre Ethernet vendor by IDC's latest cut and is bundled with the GPU sale — Meta, Microsoft and Oracle are adopting Spectrum-X (Nvidia Q3 FY2026 disclosure, 19 Nov 2025). Two of those three are Arista's only 10%-plus customers.
- Arista makes no switching silicon: its 10-K states it is "primarily reliant upon our predominant merchant silicon vendor, Broadcom, for our switching chips", with no written supply guarantee. Broadcom sells the same merchant silicon to rivals/white-box makers.
- Its two biggest customers run their own switch operating systems and could in-source more; Microsoft and Meta were 26% and 16% of 2025 revenue respectively (10-K, Feb 2026), and management expects 3–4 customers at 10%+ by end-2026.

**Irreplaceability score: 7/10** — EOS/CloudVision lock-in and the open-Ethernet position are real, but the silicon is bought in, the #1 rival is also the GPU supplier, and the two anchor customers can and do run competing fabrics.

### 5. Recent catalysts (last ~3 months)

- Q3 2026, 3 Nov 2026: revenue USD 3.66 billion, +58.5% YoY — "largest year-over-year growth in Arista's history as a public company" — vs. USD 3.33 billion consensus and USD ~3.3 billion guide; non-GAAP EPS USD 1.20 vs. USD 1.08 expected. Shares rose ~11.5% premarket / ~8% after-hours.
- FY2026 guidance raised for the fourth time in 2026, to USD 13.3 billion (+48%); Q4 guide USD 3.9–4.0 billion, non-GAAP EPS USD 1.26–1.30, above consensus.
- First FY2027 outlook: revenue ~USD 18.5 billion (+38–40%), well above USD 16.44 billion consensus; AI fabrics to ~USD 7 billion (double the 2026 target of USD 3.5 billion); cognitive campus +60% to ~USD 2 billion.
- Etherlink AI customers surpassed 100 in 2026 (from 4–5); open rack-scale architectures launched with AMD, Broadcom, Meta and Microsoft; added to the S&P 100 in Sep 2026.

### 6. Risks

Customer concentration (42% from two customers in 2025, rising to 3–4 at 10%+); Nvidia bundling Spectrum-X with GPUs; Broadcom single-source silicon with no supply guarantee; deferred-revenue / acceptance-clause volatility making recognised revenue lumpy (Dell'Oro ranking already penalises it); gross margin slipping (non-GAAP 64.0% in Q3 2026 vs. 65.2% a year earlier; FY2027 guide 62–64%); Q4 guide implies only +7–9% sequential growth after +20.5% in Q3 — the market has already flagged a sharp deceleration; valuation at 31.4x forward earnings on the screen, the highest of the three names here, prices in the USD 18.5 billion FY2027 outlook.

### 7. Scores and verdict

- **Shortage score: 8/10**
- **Verdict:** The purest open-Ethernet play on the AI super-cycle, with a record quarter and a FY2027 guide far above consensus — but it is a co-leader, not a monopolist, and Nvidia plus two concentrated customers cap the moat.

## APH — Amphenol

### 1. Shortage thesis

Yes — the strongest demand-vs-supply signal of the three names. The bottleneck has moved from compute to the physical interconnect: at 224 Gb/s per lane, signals degrade on PCB traces, so traffic must move into precisely engineered cable assemblies (Amphenol's OverPass cables carry up to 12.8 Tb/s). Orders are running ahead of shipments for three straight quarters, which is the cleanest evidence demand exceeds current capacity. AI is ~75% of IT Datacom revenue, and IT Datacom is 48% of sales. Fibre supply is also constrained industry-wide: a Nov 2026 market report notes "preform and fiber production capacity has not kept pace with demand, contributing to higher prices and longer lead times since mid-2025", with new preform plants taking up to two years to build. Driver: AI datacentre buildout — every accelerator, rack and row needs more, denser, higher-speed interconnect, plus rising chip power driving power-interconnect demand (shift to 800V+ formats).

### 2. Backlog / order book

- Q3 2026 orders: USD 12.17 billion, +99% YoY and +13% sequentially — a record (company release, 28 Oct 2026; 8-K / 10-Q filed 28–30 Oct 2026).
- Book-to-bill: 1.19:1 in Q3 (1.23:1 in Q2, 1.24:1 in Q1, 1.31:1 in Q4 2025) — orders exceeded sales by ~USD 2.0 billion in the quarter.
- Sales in the same quarter: USD 10.23 billion, +65% YoY (+37% organically).
- Amphenol does not disclose an aggregate backlog total: its 10-Q states a substantial portion of remaining performance obligations is expected to be fulfilled within three months, so it has "not disclosed the aggregate amount". On the Q3 call, management said longer-dated IT Datacom orders are normal and most demand comes from highly capitalised companies, not neoclouds (in answer to a BofA question on neocloud funding risk).
- How far out: orders reflect customers "reserving capacity well into next year" (Zacks/TipRanks call summaries, Oct 2026); no precise duration disclosed.

### 3. Category position

#1 in AI datacom interconnect by the estimates available: ~33% market share in the AI datacom segment (AInvest, 2025 analysis, repeated Jan 2026). In the broader fibre-optic connector market Amphenol led with over 12.5% share in 2025 (Global Market Insights), ahead of Corning, TE Connectivity, Molex and 3M (top 5 combined 45.5%). In datacentre fibre cabling/connectivity, Corning ranked first in 2025, followed by Fujikura, then Amphenol — so Amphenol is #1 in AI datacom connectors specifically, but not #1 in all fibre. Main rivals: TE Connectivity (strongest in 224G/lane copper, expanding into optics via RAM Photonics) and Molex (Koch-owned, deep co-design with Microsoft and Meta).

### 4. Irreplaceability / disintermediation risk

Moat: co-development/qualification lock-in. High-speed interconnect is designed into rack/shelf architectures with the chip vendor and hyperscaler, then qualified there; a failed link can take down an entire training run, so "nobody chases the cheapest cable" (AInvest, Aug 2026). Only a short list of firms — Amphenol, TE Connectivity, Molex — have decades of signal-integrity process knowledge at 224G. Amphenol is also architecture-neutral: it sells high-speed copper, power, active copper cable, passive fibre and active optics, so it wins whether the rack goes copper or optical; CEO Adam Norwitt's answer on co-packaged optics displacing copper was that customers want more interconnect across both. The CommScope CCS acquisition (closed 9 Jan 2026, announced 12 Jan 2026) added the fibre capability it previously lacked. A University of Chicago memo (Nov 2025) adds that Amphenol is "the sole provider capable of fulfilling DC interconnect needs at sufficient capacity and speed of execution" — treat that as an analyst claim, not a company statement.

Threats: hyperscalers qualify multiple suppliers for every next-gen architecture (TE is the live second source); Molex co-designs directly with Microsoft/Meta; co-packaged optics / silicon photonics could over time reduce discrete connector content per rack; and the product is ultimately a component, not a platform — no software lock-in comparable to EOS or M365.

**Irreplaceability score: 7/10** — a genuine narrow node (few firms on earth can qualify at 224G at hyperscale volume), but with two credible second sources and no software moat, a determined hyperscaler can dual-source around it.

### 5. Recent catalysts (last ~3 months)

- Q3 2026, 28 Oct 2026: record sales USD 10.23 billion (+65% YoY) vs. USD 9.49 billion consensus and USD 9.3–9.4 billion guide; adjusted EPS USD 0.80 vs. USD 0.73 expected (+74% YoY); adjusted operating margin 29.7% (+220 bps YoY). Shares rose ~7% on the day.
- Guidance raised: Q4 sales USD 10.3–10.5 billion, adjusted EPS USD 0.81–0.83 (consensus USD 9.83 billion / USD 0.76); FY2026 sales USD 36.9–37.1 billion and adjusted EPS USD 2.82–2.84 vs. consensus USD 35.66 billion / USD 2.69 — a ~60% jump on 2025's USD 23.1 billion.
- IT Datacom sales +100% YoY (+77% organic); AI-related datacom revenue +117%; full-year 2026 IT Datacom sales expected to more than double.
- CommScope CCS outlook raised again: 2026 sales now USD 5.1 billion (from USD 4.6 billion, originally USD 4.1 billion at close); expected accretion USD 0.18 (from USD 0.15); CCS operating margin in the low-20% range.
- Capital returns: new USD 4 billion buyback approved 27 Oct 2026 (starts 1 Jan 2027, ~2% of market value); quarterly dividend raised to USD 0.15 from USD 0.125, payable 13 Jan 2027. Analysts JPMorgan, BNP Paribas Exane, UBS and Truist raised price targets to USD 111–115 post-print (MarketBeat summary); 16 Buy / 3 Hold per MarketBeat.
- M&A pipeline continuing: Empire Electronics closed (expected ~USD 320 million of 2026 revenue); definitive deals signed for Advanced PCB (per Q3 call summary).

### 6. Risks

AI concentration is now the company: IT Datacom is 48% of sales and ~75% AI — a hyperscaler capex pause hits APH in the same quarter as everyone else. Communications networks fell 28% organically (weak broadband/operator demand); industrial/automotive moderating near-term. Orders growing faster than sales for three quarters is bullish, but the Q3 call had to field a neocloud funding-risk question — some longer-dated orders may be from less-capitalised buyers. Integration/execution risk on the USD 10.5 billion CommScope deal (debt was USD 8.07 billion at Sep 2025, before CCS); TE Connectivity and Bel Fuse competition; valuation — shares fell ~5.7% in the week after the print to USD 75.43 on 16 Nov 2026 (Trefis), suggesting the beat was already priced; fwd P/E of 20.9 on the screen is the lowest of the three, but that is post-split and post-rally. Copper-to-optics migration is a slow-burn substitution risk even if APH now owns both sides.

### 7. Scores and verdict

- **Shortage score: 9/10**
- **Verdict:** The cleanest shortage signal in the batch — record orders at 1.19x sales, AI datacom doubling, and a fibre/copper portfolio that wins either way — but it is now a concentrated AI-cycle bet, not a diversified compounder.

## MSFT — Microsoft

### 1. Shortage thesis

Yes — Azure capacity is the scarce resource, and Microsoft says so itself. On the Q1 FY2026 call (29 Oct 2025): "demand remains significantly ahead of the capacity we have available" and "we expect to be capacity constrained through at least end of fiscal year [June 2026]". The FY2027 Q1 call (28 Oct 2026) carried the same message: capex is rising because demand exceeds capacity, with Q2 capex expected above USD 50 billion. Independent channel checks (Uncover Alpha, Q3 2026) report "cloud capacity is still sold out, and if anything, the sold-out window is getting longer" — Andy Jassy (via Ben Horowitz) corrected "out of capacity until 2028" to "beyond 2028, end of 2028, maybe", and Sundar Pichai said a customer "asking us for compute in '27, that is incredibly difficult to do". AWS raised reserved GPU pricing 15% on 7 Oct 2026, the fourth consecutive quarterly hike (cumulative +40–75% in 2026) — pricing power that only exists when supply is short. Microsoft is "adding capacity at an unprecedented scale": total AI capacity +80% this year, total datacentre footprint roughly doubling over two years. Driver: AI datacentre buildout plus enterprise Copilot/agent demand — Azure AI Foundry has 80,000 customers incl. 80% of the Fortune 500, and 900 million monthly active users of Microsoft AI features.

### 2. Backlog / order book

- Commercial remaining performance obligation (RPO): USD 677 billion at 30 Sep 2026, +73% YoY (company release, 28 Oct 2026). Note the nuance: RPO was USD 678 billion at 30 Jun 2026, so it was flat sequentially, and commercial bookings fell 12% YoY in the quarter against a tough comparison.
- The Dec 2025 quarter jump (+USD 233 billion) was mostly one customer: OpenAI's incremental USD 250 billion Azure commitment (Oct 2025). In Jan 2026 Microsoft said ~45% of the then-USD 625 billion RPO was OpenAI; by the Jun 2026 quarter, CFO Amy Hood said all of that quarter's backlog growth came from customers outside the frontier model companies, and ex-OpenAI backlog grew 25% YoY. No such split was repeated in Oct 2026.
- AI is ~30% of the cloud backlog (RPO), per Hood's commentary (AInvest, Oct 2026).
- Duration: weighted average duration ~2 years (Q1 FY2026 call) — the backlog converts to revenue fast, so it is a ~2-year forward book, not a decade-long one.
- OpenAI concentration in the flow: USD 10.0 billion of revenue from commercial arrangements with OpenAI in the Sep 2026 quarter alone (~11% of total revenue; FY2026 total USD 24.1 billion), with USD 7.2 billion in receivables from OpenAI at 30 Sep 2026.

### 3. Category position

#2 in cloud infrastructure, taking share but not #1:

- Synergy Research Group, Q3 2026 (quarter ended Sep 2026): AWS 26%, Microsoft (Azure) 19%, Google Cloud 16% of a USD 167.7 billion market (+55% YoY). Q2 2026 was AWS 28%, Microsoft 20%, Google 15%.
- Growth: Azure +48% YoY in the Sep 2026 quarter (USD 33.2 billion, first-ever dollar disclosure) vs. AWS +39% (USD 46.0 billion) and Google Cloud +103% (USD 30.7 billion). Azure is now ~72% of AWS's size, up from 58% two years ago (CNBC via Die Signal).
- In productivity software Microsoft is #1 outright (M365 commercial cloud +17–18% YoY; Copilot passed 30 million paid subscribers), and in the enterprise AI-agent layer it is the distribution leader via M365/GitHub Copilot — but in raw cloud it remains the challenger.

### 4. Irreplaceability / disintermediation risk

Moat: the enterprise stack, not any single product. M365/Windows/Active Directory identity, GitHub, and Azure are bundled into the same procurement relationship; 80% of the Fortune 500 are Azure AI Foundry customers; switching clouds means re-platforming identity, productivity, security and data. Microsoft also owns ~24% of OpenAI (equity method, USD 12.0 billion of USD 13.0 billion committed funded) with rev-share and API exclusivity for Azure through 2030 (model/product IP rights through 2032) — though it gave up its right of first refusal on OpenAI compute in Oct 2025, and OpenAI may now use other clouds (Apr 2026 agreement). Own silicon (Maia 200 in production serving Copilot; Maia 300 detailed Oct 2026, production deployments from 2027; Cobalt 200 VMs) reduces Nvidia dependence.

Threats — the disintermediation runs the other way for Microsoft than for ANET/APH: Microsoft is the customer that could in-source, but its own customers can also route around it. OpenAI is now free to buy compute from AWS/Google; Google Cloud is growing at 2x Azure's rate; AWS remains larger and more profitable; and the AI model layer is increasingly multi-model (Microsoft now offers Anthropic models too, and builds its own MAI Base 2) — if models commoditise, the Azure premium rests on distribution and capacity, not on exclusive models. No single customer can replicate Azure's fleet, but no customer needs to: they can multi-cloud.

**Irreplaceability score: 8/10** — the enterprise identity/productivity/Azure bundle is the hardest stack in software to rip out, but Azure itself is substitutable cloud capacity, and the OpenAI exclusivity that once differentiated it is gone.

### 5. Recent catalysts (last ~3 months)

- Q1 FY2027, 28 Oct 2026: revenue USD 92.3 billion (+19%) vs. USD 90.63 billion consensus; non-GAAP EPS USD 4.89 vs. USD 4.73 expected; operating income USD 45.9 billion (+21%). Azure USD 33.2 billion, +48% — first-ever dollar disclosure, beating the 44–45% guided range. Microsoft Cloud USD 63.9 billion (+30%). Shares rose ~5% after hours.
- Guidance: Q2 FY2027 revenue USD 96–97.1 billion (+18–19%); Azure growth 49–50% in constant currency.
- Maia 300 detailed Oct 2026 (TSMC N2P chiplets, 96 chips per rack, production deployments from 2027); Maia 200 in production in Azure US Central serving Copilot; Cobalt 200 VMs showcased Nov 2026; Microsoft Ignite 17–20 Nov 2026 (agent/infrastructure announcements expected at the time of writing).
- M365 Copilot passed 30 million paid subscribers; MAI Base 2 pre-training completed.
- Capital returns: USD 10.2 billion returned in the quarter (dividends + buybacks).

### 6. Risks

The capex bill is the thesis risk: Q1 FY2027 capex incl. finance leases USD 45.2 billion (below the ~USD 50 billion plan, partly on delivery delays), Q2 expected above USD 50 billion, calendar-2026 spending ~USD 170 billion. Free cash flow was USD 18.6 billion in the quarter, down 27% YoY; Microsoft Cloud gross margin fell to ~66% on AI mix shift. The stock's 12-month return on the screen is only +1.9% despite Azure +48% — the market is repricing the payback period on that spend, not doubting demand. OpenAI concentration: ~45% of RPO at one point, USD 10 billion of quarterly revenue from one related party, and OpenAI can now multi-cloud; if OpenAI's funding or demand falters, the backlog's largest block is exposed. Devices and Consumer fell 3% YoY. Model risk: Microsoft's Copilot depends partly on outside models (OpenAI, Anthropic) — its latest filing expanded risk language on dependence on outside AI providers. Valuation is not stretched on the screen (fwd P/E 20.6), but that reflects the whole-company multiple, not an Azure pure-play.

### 7. Scores and verdict

- **Shortage score: 8/10**
- **Verdict:** Demand is provably ahead of supply — a USD 677 billion backlog, capacity sold out into 2028, Azure +48% — but the explosive-return case is diluted by the USD 170 billion capex bill, OpenAI concentration, and a whole-company multiple that already reflects a lot of it.

## Cross-name summary

| Ticker | Shortage | Irreplaceability | One-line takeaway |
| --- | --- | --- | --- |
| ANET | 8/10 | 7/10 | Record AI fabric growth, co-leader with Nvidia, capped by concentration and bought-in silicon. |
| APH | 9/10 | 7/10 | Strongest order-book signal in the batch; a concentrated AI-cycle bet wearing a compounder's clothes. |
| MSFT | 8/10 | 8/10 | Real capacity shortage and the deepest moat, but the explosive upside is blunted by capex and scale. |

Ranking on shortage alone: APH > ANET = MSFT. Ranking on irreplaceability: MSFT > ANET = APH. For an explosive-return bet, APH has the sharpest demand-vs-supply evidence (1.19x book-to-bill, orders +99%); ANET has the sharpest growth print (+58.5% revenue, FY2027 guide USD 18.5 billion vs. USD 16.44 billion consensus); MSFT has the safest shortage, but the weakest explosive-return shape of the three.

## Sources and dates

- Arista Q3 2026 release and earnings call, 3–4 Nov 2026 (company IR; Motley Fool transcript; TipRanks/TradingView call summaries).
- Arista 2025 10-K, Feb 2026 — Microsoft ~26%, Meta ~16% of 2025 revenue (Wells Fargo 10-K review, 17 Feb 2026).
- IDC Ethernet Switch Tracker Q1/Q2 2026 via NextPlatform (Jun 2026), SDxCentral (Nov 2026); Dell'Oro AI back-end ranking via SDxCentral (Nov 2026).
- Amphenol Q3 2026 release, 28 Oct 2026 (8-K 0001104659-26-119421; 10-Q 30 Oct 2026, 0001104659-26-120646) via EvidInvest read-back, 11 Nov 2026; TIKR / Zacks / Finimize summaries, 28–30 Oct 2026.
- Amphenol CommScope CCS close: 9 Jan 2026 per Q3 2026 10-Q (announced 12 Jan 2026); USD 10.5 billion cash, Aug 2025 agreement.
- Microsoft Q1 FY2027 release, 28 Oct 2026 (news.microsoft.com); Q1 FY2026 earnings call transcript, 29 Oct 2025; GeekWire / AInvest / InvestMoat analyses, Oct–Nov 2026.
- Synergy Research Group cloud share, Q3 2026 (29 Oct 2026) via Sotkn / Die Signal / CRN.
- Uncover Alpha Q3 2026 channel checks (capacity sold out beyond 2028; AWS reserved GPU price hikes).
- Microsoft Maia/Cobalt: Microsoft Ignite announcement (2023, Maia 100/Cobalt 100); Maia 200 announced Jan 2026; Maia 300 detailed 12 Oct 2026 (The Information via AInvest; BloFin summary).

## Gaps / not found

- Arista: no disclosed aggregate backlog/RPO total for Q3 2026 from a primary source — purchase commitments (USD 11.4 billion) and deferred revenue are used as proxies; the USD ~6.9 billion deferred-revenue figure is secondary-sourced.
- Amphenol: no aggregate backlog total disclosed (10-Q explicitly declines to disclose it); no precise "booked through" date for the order book.
- Microsoft: no ex-OpenAI RPO split was repeated on the Oct 2026 call (last given Jun 2026); the ~30% AI share of cloud backlog is CFO commentary as reported by AInvest, not a line in the release.
