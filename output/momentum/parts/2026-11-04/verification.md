> Run by: Muse Spark (muse-spark) — full panel

# Phase 3.5 verification — S&P 500 momentum panel — RUN_DATE 2026-11-04

Scope: the 10 load-bearing claims specified in the verifier brief. Screen prices are the 2026-11-03 closes as given in the dossier; no live price was substituted. Verdicts: CONFIRMED / CONTRADICTED / UNVERIFIED.

## Headline result

- CONFIRMED: 10
- CONTRADICTED: 0
- UNVERIFIED: 0

No claim was contradicted and none was left unverified. Four precision caveats below do not overturn any verdict, but the panel should not overstate the wording:

1. The ">75%" Micron figure includes customer allocations and non-SCA contracts, not only formal take-or-pay Strategic Customer Agreements (SCAs cover only ~35% of revenue through 2030).
2. The "only three firms" Micron claim holds only with its qualifier "leading-edge … at scale": CXMT holds roughly 7.6–10% of overall DRAM revenue, largely in mature/lower-end segments, not leading-edge HBM at scale.
3. The Vera Rubin "every major" wording is a category-level management statement ("from major hyperscalers, AI cloud providers, and system OEMs"); no source found enumerates every individual firm.
4. The Nvidia 75–90% share is a convergent analyst-estimate range, not a company-reported figure; training share is higher and inference share lower.

## MU (Micron Technology)

### MU-1 — CONFIRMED
Claim: More than 75% of fiscal 2027 output already committed under formal customer commitments, after price-and-volume agreements for its entire calendar 2026 HBM supply.
- 75% limb: Micron Q4 FY2026 earnings call, 30 Sep 2026 — CEO Sanjay Mehrotra: "more than 75% of our shipments committed for the year" for fiscal 2027, allowing allocation conversations to shift to 2028 (Motley Fool transcript of the 30 Sep 2026 call; corroborated by MarketBeat's 30 Sep 2026 call highlights: "more than 75% of the company's 2027 output was already committed across SCA and non-SCA customers"). Caveat: the transcript wording is "shipments committed" / "under customer allocation or contract" — broader than take-or-pay alone.
- Calendar-2026 HBM limb: Micron FQ1 2026 call / investor presentation, Dec 2025 — "We have completed agreements on price and volume for our entire calendar 2026 HBM supply, including Micron's industry-leading HBM4" (Motley Fool Q1 FY2026 transcript, 17 Dec 2025, as quoted in secondary coverage).
- Chronology holds: the HBM agreements (Dec 2025) precede the >75% fiscal-2027 statement (30 Sep 2026).

### MU-2 — CONFIRMED (with qualifiers)
Claim: Only three firms (Samsung, SK hynix, Micron) make leading-edge DRAM/HBM at scale, and no hyperscaler fabs DRAM itself.
- Trio limb: TrendForce, 2Q26 DRAM report (7 Sep 2026) — "the three major suppliers": Samsung 39.4%, SK hynix 24.9%, Micron 23.3% of DRAM revenue; other suppliers named (Nanya, Winbond, PSMC) are "focused on mature-process products". Syz Private Banking research (25 Feb 2026, citing Counterpoint): at the advanced end including HBM, capability "remains confined to Samsung Electronics, SK hynix and Micron", while CXMT/YMTC at an estimated 5–10% are "largely in lower-end segments" and lack advanced HBM capability. TrendForce Q1 2026: trio held 89.7% of DRAM revenue, CXMT fourth at 7.6%.
- No-hyperscaler-fab limb: confirmed by enumeration rather than by a single negative assertion — every supplier list found names only the trio (plus mature-process makers) as DRAM/HBM fabricators, while hyperscalers appear only as buyers: e.g. Z2Data's account of hyperscalers (AWS, Azure, Google Cloud) "absorbing price increases … on DRAM orders … from memory chip manufacturers" and receiving only partial fulfilments, and HBM described as "made by SK Hynix, Micron, or Samsung". No source found shows any hyperscaler fabricating DRAM. Note this limb rests on exhaustive supplier enumeration, not on one source stating the negative in those words.

### MU-3 — CONFIRMED
Claim: Management guided that 2027–2028 could be tighter than 2026 for memory supply.
- Micron Q4 FY2026 prepared remarks / call, 30 Sep 2026 — CEO Sanjay Mehrotra: "we expect memory and storage supply-demand conditions to be much tighter in fiscal 2027 and 2028 than they were in 2026" (Motley Fool, 1–2 Oct 2026); repeated for calendar years: "In calendar 2027 as well as 2028, we see demand exceeding supply. In fact, we see greater tightness in the industry in 2027 and in 2028 versus 2026" (The Register / Tom's Hardware reporting of the call). Also: "we do not have line of sight to when supply and demand will return to balance."
- Wording note: some sections of the call use "fiscal" 2027/2028 and others "calendar" 2027/2028; the substance (both following years tighter than 2026) is identical in both framings.

### MU-4 — CONFIRMED (dossier arithmetic internally consistent)
Claim: Screen figure — analyst mean target implies roughly 83% upside from the 2026-11-03 close.
- Dossier shortlist values: price 855.0999755859, analyst mean target 1561.9111, upside 0.8265830249.
- Independent recomputation: (1561.9111 − 855.0999755859) / 855.0999755859 = 0.8265830249 exactly (82.66%, rounds to ~83%). The dossier's upside column, the "about 83%" ballot wording, and the "82.6%" wording are all consistent with the same two inputs. This verifies the dossier's arithmetic only; it does not verify the underlying analyst targets or the close price against a live source, per the brief.

## NVDA (Nvidia)

### NVDA-1 — CONFIRMED
Claim: Fiscal 2028 revenue growth of approximately 70% described by management as a supply-constrained outlook, with demand higher than that.
- Nvidia Q2 FY2027 earnings call, 26 Aug 2026 — CFO Colette Kress: the ~70% fiscal 2028 growth expectation is a "supply-constrained outlook"; CEO Jensen Huang: demand is "much greater than 70%" / "much higher", but supply "allows us to confidently deliver 70%" (reported by Datafloq, Nasdaq 12 Sep 2026, and Trefis 30 Oct 2026, all summarising the 26 Aug 2026 call). Kress also said customer forecasts pointed to roughly double that growth, and that supply would remain a bottleneck at least through fiscal 2028 (ending late Jan 2028).

### NVDA-2 — CONFIRMED (as an analyst-estimate range, not a company figure)
Claim: Accelerator market share of roughly 75–90% and the CUDA moat claim.
- Share range: multiple secondary estimates converge on the range — Silicon Analysts (updated Aug 2026): ~80–90% of the AI accelerator market by revenue as of 2025, ~75% projected for 2026, training >90%, inference 60–75%; HyperFRAME Research (Dec 2025): "market share estimates ranging from 75 to 90 percent in AI accelerators, depending on the methodology and market segment". No company-reported audited share was found; the dossier itself labels these "secondary estimates", which is accurate.
- CUDA moat: widely described as the structural moat — e.g. Silicon Analysts: "CUDA Ecosystem: 20+ years, 4M+ developers. Every ML framework optimized for CUDA first"; HyperFRAME: "Analysts consistently identify CUDA as NVIDIA's most defensible competitive moat … PyTorch and TensorFlow workflows … are usually optimized for CUDA first". The moat is real but contested at the margin by custom ASICs, as the dossier itself notes.

### NVDA-3 — CONFIRMED (category-level management statement; see caveat 3)
Claim: Vera Rubin purchase orders placed by every major hyperscaler / AI cloud / system OEM.
- Nvidia Q2 FY2027 call, 26 Aug 2026, as reported: CFO Colette Kress stated the company "had received purchase orders from major hyperscale cloud providers, AI cloud service providers, and system OEMs" (kad8 summary of the call; Motley Fool, 26 Oct 2026: "Nvidia says Vera Rubin has entered production shipments, with purchase orders from major hyperscalers, AI cloud providers, and equipment manufacturers"). Production shipments began Aug 2026.
- Caveat: sources confirm the category-level claim ("from major …"), not an enumerated list proving literally every major firm placed an order. The ballot's "every major" is a fair paraphrase of management's category wording, not a verified firm-by-firm roster.

## MSFT (Microsoft)

### MSFT-1 — CONFIRMED (primary source)
Claim: Commercial remaining performance obligations of $677bn at end-September 2026, up 73% year over year.
- Microsoft Q1 FY2027 results release, 28 Oct 2026 (quarter ended 30 Sep 2026), Microsoft News: "Commercial remaining performance obligation increased 73% to $677 billion." Corroborated by the Form 10-Q revenue note (filed 28 Oct 2026): $677bn at 30 Sep 2026 vs $392bn at 30 Sep 2025, ~30% expected within 12 months, weighted-average duration ~2.3 years. Context note (not a contradiction): the balance was essentially flat sequentially vs $678bn at 30 Jun 2026 — the 73% is a year-over-year figure, driven largely by the Dec 2025 quarter jump.

### MSFT-2 — CONFIRMED (primary management statement)
Claim: Management statement that customer demand for Azure continues to exceed available supply.
- Microsoft Q1 FY2027 earnings call, 28 Oct 2026 — CFO Amy Hood, verbatim as reported by GeekWire (28 Oct 2026) and the call transcript: "Customer demand continues to exceed available supply." Hood also said "We still have demand that exceeds supply" and cited delayed third-party capacity deliveries in the quarter.

### MSFT-3 — CONFIRMED (primary management guidance)
Claim: Azure growth guided around 48–50% constant currency.
- Precise figure is Q2 FY2027 guidance of 49–50% constant currency (the dossier/ballot wording "around 48–50%" blends the delivered Q1 print with the guide; both figures check out): Q1 FY2027 Azure revenue $33.2bn, +48% YoY (Microsoft release, 28 Oct 2026); Q2 FY2027 guidance: "Azure growth of 49% to 50% in constant currency" (Motley Fool transcript takeaways, 28 Oct 2026 call; GeekWire 28 Oct 2026). The ballot's "guided 49–50% constant-currency rate" is exact; "around 48–50%" is accurate as a range spanning print + guide.

## Method note
Searches run 2026-11-04. Primary sources used where available: Microsoft's own 28 Oct 2026 results release; earnings-call transcripts (Motley Fool) for Micron 30 Sep 2026 and Microsoft 28 Oct 2026; TrendForce 2Q26 DRAM report. Where the underlying claim is itself a management statement or an analyst estimate, the verification is of the statement/estimate as reported, not of the underlying market fact. No claim required a live price check, and none was substituted.
