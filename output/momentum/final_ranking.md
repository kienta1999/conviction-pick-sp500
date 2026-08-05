# Momentum — Ranked Top 10 (S&P 500)
**Run date:** 2026-08-04 · **Mode:** momentum (above 200d SMA + structural shortage doctrine) · **N = 10, R = 1**
**Screen:** `output/momentum/shortlist.json`, generated 2026-08-04 19:44:47 — 50 candidates from 503 S&P 500 members, triaged to 14 for deep research
**Panel:** 4 independent Opus subagents (one per lens), dispatched sequentially, all reading the same dossier
**Scoring:** Borda — rank 1 = 10 pts … rank 10 = 1 pt, unranked = 0, summed across 4 ballots (max 40)

---

## The ranking

| # | Ticker | Company | Sub-industry | Price | Mean target (upside) | Fwd P/E *(corrected)* | Short. | Irrepl. | Borda | Appear. | #1s | Avg place | The case in one line |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **AVGO** | Broadcom | Semiconductors | $418.16 | $527.88 (**+26.2%**) | ~24x FY27 / ~36x FY26 | 9 | 7 | **28** | 3/4 | **2** | 1.67 | Only computable forward ratio in the field — >$30B AI bookings vs $10.8B shipped — and it profits *from* the trap that threatens the rest. ⚠️ One lens excluded it outright on customer graduation. |
| **2** | **LRCX** | Lam Research | Semi Materials & Equip | $317.74 | $368.13 (+15.9%) | ~25.6x *(the one the screen got right)* | 9 | 8 | **26** | 4/4 | 1 | 4.50 | Purest memory-shortage exposure: DRAM contract prices +90% q/q forcing WFE spend, +20% sequential guide, 52% gross margin at a 20-year high — and its five customers have never built an etcher. |
| **3** | **MSFT** | Microsoft | Systems Software | $492.81 | $563.05 (+14.3%) | 20.8x | 8 | 7 | **25** | 4/4 | 1 | 4.75 | The uncrowded AI trade: −5% over 12 months while RPO hit $678B (+84%, **+25% ex-OpenAI**) and Azure beat its own guide at +43%. ⚠️ Headline EPS growth is OpenAI-inflated — see verification. |
| **4** | **APH** | Amphenol | Electronic Components | $171.33 | $198.06 (+15.6%) | 25.3x | 8 | 7 | **22** | 4/4 | 0 | 5.50 | Record $10.7B orders, 1.23 book-to-bill, and a second 2026 price increase (+5–15%) effective 2026-07-01 — nobody in-sources connectors. ⚠️ ~25 of 55 growth points are acquired. |
| **5** | **GOOGL** | Alphabet (A) | Interactive Media | $377.65 | $426.95 (+13.1%) | 25.3x | 9 | **9** | **21** | 3/4 | 0 | 4.00 | $514B cloud backlog (~5 years of run-rate, up from $106B a year ago), CFO admits "supply-constrained," and its two AI rivals rent its TPUs. ⚠️ $4.6T cap arithmetically caps the return. |
| **6** | **NVDA** | Nvidia | Semiconductors | $211.94 | $302.83 (**+42.9%**) | ~23x *(not the screen's 16x)* | 9 | 7 | **21** | 4/4 | 0 | 5.75 | Widest consensus gap in the field at the cheapest mega-cap multiple after a year of compression, on $119B of audited supply commitments. 🚩 **TRAP FLAG: four customers ≈40% of revenue, all shipping rival silicon.** |
| **7** | **GE** | GE Aerospace | Aerospace & Defense | $377.28 | $404.90 (+7.3%) | ~49x FY26 *(not 40.7x)* | 9 | **9** | **17** | 3/4 | 0 | 5.33 | Doctrine-perfect — $210B backlog (4.4x revenue), shop visits 40% oversubscribed, sole-source engine on every 737 MAX. ⚠️ And almost entirely priced: margins −130bps and only +7.3% to target. |
| **8** | **LLY** | Lilly (Eli) | Pharmaceuticals | $1,115.68 | $1,276.96 (+14.5%) | ~31x FY26 *(not 24.9x)* | **4** | 7 | **15** | 3/4 | 0 | 6.00 | Best business here — 60% US incretin share, patents to 2036, retatrutide — and the cheapest quality. 🚩 **DOCTRINE FLAG: the FDA formally ended the GLP-1 shortage; prices are falling by policy.** Q2 lands 2026-08-05. |
| **9** | **KLAC** | KLA Corporation | Semi Materials & Equip | $195.45 | $230.85 (+18.1%) | ~36x FY27 *(not 27.9x)* | 8 | **9** | **12** | 3/4 | 0 | 7.00 | 58% process-control share in a category no architecture can route around, 87% ROE, advanced packaging +70%. ⚠️ Slowest growth, most expensive growth-adjusted, and the last analyst action was a *cut*. |
| **10** | **VRT** | Vertiv | Electrical Comp & Equip | $269.93 | $339.35 (+25.7%) | 29.0x | 8 | 6 | **10** | 2/4 | 0 | 6.00 | Sits on the hardest physical bottleneck in AI — power and heat — with pricing above inflation and chiller capacity doubling. 🚩 **FLAG: management stopped publishing backlog on 2026-02-11**, and Q2 missed revenue (−14/−17%). |

*Fwd P/E "corrected" = the research's bottom-up figure. The screen's `forwardPE` field is Yahoo's,
indicative only, and is not what these names were ranked on — see the note under "What was verified".*

---

## Per-name thesis — the top 5

### 1. AVGO — Broadcom · Borda 28 · 2 of 4 #1 votes
The single hardest forward number in the field: **over $30B of AI semiconductor bookings against
$10.8B shipped** in Q2 FY26 (verified verbatim from the 2026-06-03 call). Unlike every other forward
claim in this dossier, *both halves* of that ratio are company-disclosed for the identical period, so
the ~3x book-to-bill is computable rather than asserted. Behind it: an implied $200B+ 18-month backlog,
FY26 AI revenue of ~$56B guided to **$100B+ from FY2027**, a Q3 guide of ~$29.4B (+84% y/y) with AI at
$16.0B (+200%), and a **$35B Apollo/Blackstone vehicle** (2026-06-09) purpose-built to finance 20GW of
the demand — an order book that arrives with its buyers pre-funded. **Why it's the leader:** #1 custom
XPU design partner with Marvell the only credible #2; the "70%+ share" figure is an analyst estimate
(60–80% range), not a company number. **The honest caveat:** there is no CUDA here — only IP and
program inertia — and Google, the anchor customer, has progressively internalized TPU design. Program
losses are binary. Agent C excluded the name entirely on exactly this.

### 2. LRCX — Lam Research · Borda 26 · 1 #1 vote
The cleanest structural shortage in the field, and the only name whose screen multiple survived
verification. DRAM contract prices rose **+90–95% q/q** and NAND +55–60%, with HBM sold out for 2026 —
and memory makers convert that windfall straight into wafer-fab-equipment capex, where Lam has the
highest beta. It raised its CY2026 WFE forecast twice, to the **"low $150B range"** on the 2026-07-29
call, and guided the September quarter to **$8.1B ±$400M against $6.72B just delivered** — a >20%
sequential step off a fourth consecutive record, at a **52% gross margin, its highest in 20 years**.
**Why it's the leader:** #1 in etch, co-#1 in deposition, mid-30s% share of its served market.
**Why irreplaceable:** its customers are five memory and foundry firms — not hyperscalers — and none
has ever built its own etcher; recipes are co-developed and qualified per node, so switching risks
yield on a multi-billion-dollar fab. **The caveat:** this is a cyclical at peak margins that already
fell 27% from its June high *while printing records* — the market is arguing about durability, not
about the quarter.

### 3. MSFT — Microsoft · Borda 25 · 1 #1 vote
The un-crowded way to own the compute shortage: a **−5% twelve-month return** while the business
compounded. Commercial RPO reached **$678B, +84% y/y — and critically +25% excluding OpenAI**, with
nearly 90% of Microsoft Cloud revenue coming from outside the frontier labs, which rebuts the
"Microsoft is an OpenAI SPV" bear case directly. Azure grew **+43% against its own 39–40% guide**, and
CFO Amy Hood said plainly that **"demand continues to exceed available supply."** **Why irreplaceable:**
the moat is not compute — an enterprise can move a GPU workload but cannot move its identity graph and
400M Office seats. **The caveats, and they are real:** verification showed the headline **+32% EPS
growth is GAAP and inflated by OpenAI investment accounting — the adjusted figure is +23%, and
operating income grew only 18%**. Management has *guided FY27 margins down*. The de-rate from
asset-light software compounder to capital-intensive infrastructure was rational, so the return has to
come from earnings, not from re-rating.

### 4. APH — Amphenol · Borda 22 · ranked by all four lenses
The most consistently ranked name on the board — every lens had it, none had it first. Record **$10.7B
orders with a 1.23 book-to-bill**, Q2 revenue +55% (**+30% organic**), and a second 2026 price increase
of **+5–15% effective 2026-07-01** while upstream inputs ran +70% to +300% — pricing power evidenced by
action, not narrative. IT datacom is 43% of sales growing 89%. Hyperscalers cannot in-source
connectors: it is a high-mix precision stamping and plating business where 224G-per-lane signal
integrity is designed *into* the board stack-up. **The caveat:** ~25 of the 55 growth points are
acquired (CommScope, now raised to $4.6B), and essentially all organic growth is one AI datacom bet —
more concentrated than its diversified-industrial reputation implies.

### 5. GOOGL — Alphabet · Borda 21 · best average placement of any non-winner (4.00)
The highest-quality expression of the shortage, and the only 9/9 name that isn't priced like GE.
**$514B of contracted Google Cloud backlog** — verified, and up from $460B in Q1 and just **$106B a
year ago** — with more than half converting inside 24 months, about 5 years of current cloud run-rate.
The CFO admits Alphabet is **supply-constrained** and is renting third-party capacity as a bridge, and
cloud grew +82% while cloud operating margin expanded from 20.7% to 35.6% — you do not expand margin
15 points into a discounting environment. **Why irreplaceable:** it owns TPU, Gemini, GCP and the
Search/YouTube demand sink end-to-end, and its two most capable AI rivals — Anthropic and Meta — now
pay it rent for TPU capacity, won on price-performance in an open bake-off. **The cap is arithmetic:**
at $4.6T, doubling requires adding $4.6T. Superb compounder, structurally not an explosive-return bet.

### 6–10, one line each

- **NVDA** — the biggest consensus gap in the field (+42.9%) at ~23x after a year of multiple
  compression, on $119B of *audited* supply commitments; but it is the doctrine's trap in its purest
  form, and custom-ASIC shipments are growing 44.6% y/y against 16.1% for merchant GPUs.
- **GE** — the best business and the worst entry price: a $210B contracted backlog and a 737 MAX
  engine monopoly, against ~49x current-year earnings, margins down 130bps, and only +7.3% to the
  mean target *(one aggregator puts consensus at $365.61 — below the current price)*.
- **LLY** — ranked on business quality alone; it fails this screen's doctrine outright now that the
  FDA has declared the GLP-1 shortage resolved and Lilly guides to a low-to-mid-teens % price drag.
  Q2 reports 2026-08-05, unreported at ranking time.
- **KLAC** — the field's most dominant franchise (58% share, sustained for decades) attached to its
  weakest momentum setup: −35% from its high, slowest growth, ~36x, and a post-print target cut.
- **VRT** — a genuine bottleneck thesis whose evidence went dark: backlog and orders disclosure was
  switched off on 2026-02-11, and the last hard number ($15.0B, +109%) is now eight months stale.

## Just-missed names

- **FCX** (Borda 8, 3/4 ballots) — the contrarian's favourite structure: copper +51.6% y/y while
  Grasberg runs with one engine out, and 2027 guided +>20% copper and +>50% gold onto that price. It
  missed the cut because two lenses saw ~1% TTM revenue growth and only +6.6% to target, and because
  the whole case rests on one binary ramp that has already slipped once (H2 2026 cut from ~85% to ~65%
  of nameplate).
- **HWM** (Borda 8, 3/4) — owns the aerospace chokepoint with 20–50 week lead times and prohibitive
  re-qualification, and growth is *accelerating* 9%→19% with EBITDA margin +320bps. At ~58x
  current-year with only +8.6% to target and Q2 unreported (2026-08-06), no lens would put it high.
- **ANET** (Borda 7, **1/4** — the most polarizing name) — the best single print of the day (first $3B
  quarter, EPS beat 15%, Q3 guided 12% above consensus, +11% after hours), ranked 4th by the momentum
  lens and *refused entirely* by the other three. It has lost the #1 datacenter Ethernet share
  position to NVIDIA (21.5% vs 20.7%), two customers who build their own switches are ~42% of revenue,
  and post-pop it trades at or above freshly raised $200–210 targets.
- **CF** (Borda 0, **0/4** — unanimously unranked) — cheapest name in the field at ~7.4x FY26
  consensus, but no order book, a fungible commodity, new Gulf Coast supply it is itself building, and
  urea already cooling on affordability. No lens found a shortage.

## What the panel revealed

**Where they agreed.** Only **APH, MSFT, NVDA and LRCX** appeared on all four ballots — the consensus
core, though none was anyone's runaway favourite. Nobody ranked **CF** at all.

**Where they split — and it was sharp.** The four lenses produced four *different* top picks
(AVGO, AVGO, LRCX, MSFT), and the two most interesting disagreements are structural:

- **AVGO scored 28 Borda points while being excluded entirely by one lens.** Agent C (quality/moat)
  would not rank it: "a business whose product is teaching hyperscalers to build their own silicon
  eventually watches them graduate — Google already largely has." Every other lens had it top-3. That
  is conviction and controversy in the same name.
- **The valuation lens inverted the doctrine.** Agent D observed that five names (ANET, CF, FCX, GE,
  HWM) have **under 10% consensus headroom** after the sell side already raised targets, and argued
  those trades are over regardless of story quality. That is why GE — a 9/9 doctrine-perfect business —
  finished 7th rather than 1st.

**Conviction vs consensus.** AVGO is the **conviction** name: 2 first-place votes and the best average
placement (1.67), but only 3 of 4 ballots. NVDA and APH are the **consensus** names: on every ballot,
first on none. MSFT is the only name to combine a #1 vote with a 4/4 appearance.

**Strict doctrine would reorder the bottom half.** The Borda order puts **LLY (#8)** and **VRT (#10)**
above **FCX** and **HWM**, which are just outside. On the doctrine's own scores that is backwards:
FCX (8/8) and HWM (8/8) both beat LLY (**4**/7) and VRT (8/**6**). LLY rides on business quality that
the doctrine does not reward, and VRT's shortage evidence is unauditable since disclosure stopped. A
strict-doctrine top 10 would swap FCX and HWM in for LLY and VRT.

## If forced to ONE

**AVGO**, and it is also the Borda #1 — the vote and the doctrine agree here, which is not always the
case. It was the **only one of the panel's four nominees whose expected value cleared the +15%
guardrail** (+17.7%, vs +12.0% for LRCX and +12.6% for MSFT).

The trap filter is what could have overturned it, and it was applied rather than waved through: Agent
C's veto was tested directly and judged **medium risk, not high** — a hyperscaler graduating from
Broadcom must first replicate SerDes, advanced packaging and IP at scale, the contracted programs run
through the entire holding period, and the same in-sourcing wave is *additive* to Broadcom across five
other named programs. That is a different risk class from Nvidia, whose four largest customers ship
direct substitutes today.

**The honest alternative:** if you weight C's dissent more heavily than I did, the answer is **LRCX** —
a name whose customers are five fabs that *cannot* in-source it, where the trap simply does not exist
as a risk class. You would be trading the trap for full cycle risk, and accepting an EV below the
guardrail. Full reasoning in `final_pick.md`.

## Return scenarios — the top 3

All numbers are research scenarios, not guarantees. Built on driver-level math, not bare multiples.

### AVGO — $418.16 · mean target $527.88
| Scenario | Target | By | Prob | Reasoning |
|---|---|---|---|---|
| **Bear (stop)** | **$285** (−31.8%) | 2027-06 | **25%** | FY27 AI lands ~$75–80B not $100B+ — the hole one lost XPU program makes. EPS ~$13.5 at ~21x. Full 25% despite great evidence, because concentration is sharpest here and losses are binary. |
| **Base** | **$505** (+20.8%) | 2027-11 | **45%** | The 18-month book converts on schedule; FY27 AI ≈$100B, EPS ≈$17.50 at ~29x. |
| **Bull** | **$645** (+54.2%) | 2027-12 | **30%** | AI clears ~$110B as XPV's 20GW converts and Anthropic scales 1GW→3GW. EPS ~$19.5 at ~33x. Above-default weight: bookings at 3x shipments have historically preceded upward revisions. |

**EV = $492.00 → +17.7%. Clears the +15% guardrail.** Price sits ~60% of the way from bear to base —
closest to base — and below the mean target. No red flag.

### LRCX — $317.74 · mean target $368.13
| Scenario | Target | By | Prob | Reasoning |
|---|---|---|---|---|
| **Bear (stop)** | **$200** (−37.0%) | 2027-06 | **30%** | The memory cycle turns. The 2022–23 downturn cut Lam's revenue by roughly a third; 52% gross margin is a 20-year high with only one direction to mean-revert. EPS ~$8 at ~25x. Weighted above default because this is a late-cycle cyclical at peak margins. |
| **Base** | **$380** (+19.6%) | 2027-11 | **45%** | FY27 EPS ~$12.4 (the WFE cycle runs through 2027 as guided) at ~31x. |
| **Bull** | **$500** (+57.4%) | 2027-12 | **25%** | WFE sustains $150B+, NAND conversion spend lands, EPS ~$14 at ~36x — Cantor's street-high target. |

**EV = $356.00 → +12.0%. ⚠️ BELOW the +15% guardrail** — it stays in the ranking (the guardrail only
blocks actionable *single* picks) but a reader should see that the modeled edge does not clear the bar.
Price sits closest to base. *Verification correction: FY26 EPS of $5.82 is **non-GAAP**; filed GAAP is
$5.76. Consensus target $368.13 is visibly stale post-print — a second aggregator shows $327.15.*

### MSFT — $492.81 · mean target $563.05
| Scenario | Target | By | Prob | Reasoning |
|---|---|---|---|---|
| **Bear (stop)** | **$380** (−22.9%) | 2027-06 | **25%** | The depreciation wave lands, FY27 margins decline as guided, AI capex digests. ~18x on ~$21. Within recent experience — the stock traded ~$356 in April 2026. |
| **Base** | **$580** (+17.7%) | 2027-11 | **50%** | RPO converts, Azure holds 35–40%, FY27 EPS ~$21.5 at ~27x. |
| **Bull** | **$680** (+38.0%) | 2027-12 | **25%** | Copilot proves AI *software* margins and the multiple re-expands to ~30x on ~$22.5. |

**EV = $555.00 → +12.6%. ⚠️ BELOW the +15% guardrail.** Price sits between bear and base, below the
mean target. *Verification correction: the +32% FY26 EPS growth is GAAP and OpenAI-inflated — adjusted
is **+23%** and operating income grew **18%**, so this is not evidence of operating leverage.*

## What was verified (Phase 3.5)

An independent verifier subagent that had **not** read the dossier checked 14 claims across the top 3
against primary sources: **12 CONFIRMED, 1 UNVERIFIED, 0 CONTRADICTED.** Confirmed: AVGO's $30B
bookings vs $10.8B shipped (verbatim), $22.2B/+48% and 67.3% record margin, the Q3 $29.4B/$16.0B
guide, the $100B+ FY27 target, the $35B/20GW XPV platform (dated 2026-06-09), and next earnings
2026-09-02; LRCX's Q4 figures and $8.1B guide and the low-$150B WFE raise; MSFT's $678B RPO (+84%,
+25% ex-OpenAI), Azure +43%, and Hood's "demand continues to exceed available supply."

**Four corrections logged and carried into this document:** (1) AVGO's "70%+ XPU design-services
share" is an **analyst estimate, not a company figure** — ranges are 60–80%; (2) AVGO's $56B FY26 AI
number was **reiterated, not raised**; (3) LRCX's $5.82 FY26 EPS is **non-GAAP** (GAAP $5.76), and the
$140B WFE step dates to **2026-04-22**, not June; (4) MSFT's **+32% EPS growth is GAAP and
OpenAI-inflated** versus +23% adjusted. Full detail: `parts/2026-08-04/verification.md`.

**Also flagged:** the screen's `forwardPE` field is indicative only and should not be read as the
multiple you pay today. It is Yahoo's figure passed straight through; the screen does no valuation
arithmetic of its own and **does not rank on it** (`forwardPE` is not in the composite), so nothing in
this ranking was ordered by it. Two separate distortions sat in it: (1) Yahoo builds the multiple
against a price up to three days staler than the funnel's own — **now fixed**, `screen.py` rescales
onto the same price, which is why AVGO reads 21.5 rather than 20.1; and (2) which *fiscal year* the
forward EPS refers to varies by company — GE and HWM point a year out, while CF points *nearer* than
the current year — which is **not** correctable from that field. The bottom-up figures in the table
above are the ones to use.

## Risk lens & leverage-safety note

**Sector concentration is extreme and should be read as a single bet.** Eight of the ten names are
levered to one variable: AI datacenter capital expenditure. AVGO, LRCX, NVDA, KLAC and APH are the
supply chain; MSFT and GOOGL are the spenders; VRT is the physical plant. If hyperscaler capex pauses,
**this list falls together** — the diversification implied by ten tickers is largely illusory. Only
LLY (pharma) and GE (aerospace) are driven by something else.

**Highest-risk:** VRT (order book undisclosed, revenue already missed once), NVDA (the trap, named and
active), AVGO (binary program concentration), LRCX and KLAC (violent capex cyclicals — LRCX fell 27%
in five weeks *while printing records*).
**Steadier compounders:** MSFT, GOOGL, GE, LLY — lower ceilings, and GE and LLY carry their own
distinct flags.

**Leverage-safety (risk education, never a recommendation).** These are high-beta cyclicals. LRCX gave
back 27% in five weeks with fundamentals accelerating; KLAC is −35% from its high; VRT fell 14–17% in a
day on a 3% revenue miss. Drawdowns of that speed are brutal on borrowed money, because a position can
be liquidated at the bottom before the thesis has been disproven. `POLICY.md` makes this system's picks
**cash-only — no margin, no options as leverage substitutes, no borrowing against the position.** No
position size or leverage multiple is recommended here for anyone.

## Thesis-break / trap triggers to watch across the list

- **The order book rolling over** — AVGO book-to-bill under ~1.5x; APH book-to-bill under 1.0; GE
  backlog shrinking; VRT resuming disclosure at a *lower* number.
- **A named in-sourcing announcement** — any hyperscaler taking an XPU program in-house (AVGO), or a
  top-2 customer standardizing on whitebox/SONiC (ANET, already the reason it missed the cut).
- **Pricing rolling over** — DRAM/NAND contract prices turning (LRCX, KLAC); connector price increases
  failing to stick (APH); copper reversing (FCX).
- **Margins peaking sequentially** — AVGO off 67%, LRCX off 52% gross, APH off ~30% operating. In this
  doctrine the margin peak usually precedes the revenue peak.
- **AI capex guidance cuts** from Microsoft, Alphabet, Meta or Amazon — the single event that would hit
  eight of these ten names at once.
- **Financing stress** — AI-infrastructure credit spreads widening, or the XPV/vendor-financing
  structures failing to fund (AVGO, and by read-through NVDA).

---

## Disclaimer

**2026-08-04.** This is AI-generated research output for education and personal decision support. It is
**not financial advice**, not a recommendation to buy or sell any security, and not personalized to
anyone's circumstances. Every price target, probability and expected value above is a modeled research
scenario, not a forecast or a guarantee. Figures were verified against primary sources where stated,
but errors are possible and several claims are explicitly marked unverified or corrected. Three names
in this list (LLY, HWM, CF) had unreported quarters at ranking time. Do your own research and consider
consulting a licensed financial adviser.
