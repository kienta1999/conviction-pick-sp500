# Momentum — Final Pick (single-pick mode)
**Run date:** 2026-08-04 · **Mode:** momentum (above 200d SMA + structural shortage doctrine)
**Screen:** `output/momentum/shortlist.json`, generated 2026-08-04 19:44:47 — 50 candidates from 503 S&P 500 members
**Funnel:** 503 → profitable 405 → US 385 → growing 340 → leverage ok 235 → above SMA200 173 → margin leader 84 → fwd-PE gate 84 → niche leader 67 → top 50 by composite
**Panel:** 4 independent Opus subagents, one per lens, dispatched sequentially · **Verification:** independent verifier subagent, 14 claims

---

## THE PICK: **AVGO — Broadcom Inc.**

| | |
|---|---|
| **Sector / sub-industry** | Information Technology / Semiconductors |
| **Price (2026-08-04)** | **$418.16** |
| **Market cap** | ~$1,866B |
| **Analyst mean target** | $527.88 (**+26.2%**), 48 analysts. A second aggregator shows $500.78 (29 analysts); full range $216–$675 |
| **Forward P/E** | **~24x FY27 / ~36x FY26** — *not* the screen's 20.1x (see valuation note) |
| **Rev growth TTM / op margin / ROE** | 24% / 49% / 37% |
| **Net debt / EBITDA** | 1.08 |
| **vs 200d SMA / vs 52w high / 12m return** | +14% / −13% / +46% |
| **Composite score** | 0.701 (rank 12 of 50) |
| **Next earnings** | **2026-09-02, after close** (confirmed) |
| **Panel vote** | Top pick of 2 of 4 lenses; 4 of 8 weighted points |

---

## The thesis, in a paragraph

Broadcom is the arms dealer to Nvidia's competitors. It co-designs the custom XPUs that hyperscalers
use to escape merchant GPUs, and sells the Ethernet and optical silicon that stitches those clusters
together. That makes it the one name in this field standing *on the right side of the doctrine's own
trap*: the momentum screen's fatal failure mode is a supplier whose customers in-source the product —
and Broadcom's entire business **is** that in-sourcing. Its forward book is the hardest evidence
anywhere in the field: **over $30B of AI semiconductor bookings against $10.8B shipped in a single
quarter**, roughly a 3x book-to-bill, with an implied $200B+ 18-month backlog and a purpose-built
**$35B Apollo/Blackstone financing vehicle** that removes the *funding* constraint from its own
demand. It is guiding revenue from $22.2B to ~$29.4B in one quarter — the steepest sequential step in
the field — and targets **$100B+ of annual AI revenue from FY2027**, against ~$56B this year.

---

## The shortage + backlog evidence

Every figure below was independently verified (see *What was verified*).

- **The order book.** Q2 FY26 (reported 2026-06-03): **AI semiconductor bookings over $30 billion
  against $10.8 billion of AI revenue shipped** — Hock Tan's verbatim statement on the call.
  Management effectively confirmed an implied **$200B+ 18-month backlog** covering 2H FY26 through
  FY27. *Caveat from verification: "over $30B" is a floor, so ~2.8x is a **minimum** ratio, and it is
  a call statement, not a filed or audited metric.*
- **Why customers are queuing — the shortage itself.** Tan's stated reason is that customers must
  plan ahead for **chip availability, HBM/DRAM supply, and power infrastructure**. They are not
  ordering for delivery; they are reserving a place in a supply chain that is sold out upstream.
- **The conversion ramp.** Q3 FY26 guided to **~$29.4B (+84% y/y)**, with **AI semiconductor revenue
  guided to $16.0B (+200% y/y)** — up from $10.8B one quarter earlier.
- **The multi-year figure.** **~$56B of FY2026 AI semiconductor revenue** (+~180% y/y), and a stated
  target of **$100B+ annually from FY2027**, underpinned by multi-year agreements with named
  customers: Google, Meta, Anthropic, OpenAI, ByteDance, Apple.
- **The funding.** On **2026-06-09**, Broadcom, Apollo and Blackstone established the **AI XPV
  Platform** — an initial **$35B capital solution** enabling **more than 20GW of AI compute through
  2028**, first tranche funding **Anthropic's 1GW+ expansion from mid-2026**. Order books usually
  assume the customer can pay; this one arrives pre-funded.
- **Margins are expanding into the ramp.** Q2 non-GAAP operating margin **67.3% — a record** — on
  revenue of $22,187M, +48% y/y.

**Honest correction from verification:** the $56B FY26 AI figure was **reiterated, not raised**, and
the market sold off on the print that day for exactly that reason. The acceleration is real; the
*rate of upward revision* paused.

## Why it's the category leader

Broadcom is the #1 custom AI accelerator design partner and #1 in AI datacenter Ethernet networking,
with Marvell the only credible #2 — effectively a duopoly. **The widely cited "70%+ share of custom
XPU design services" did not survive verification as a company figure**: it is an analyst estimate,
with Bloomberg Intelligence giving a 60–80% range and Counterpoint ~60% for 2027, while Marvell's own
share estimates span 8–25%. Treat Broadcom as the clear leader of a two-horse market, not as a
precisely quantified 70% monopolist. What *is* firm is the customer list and the contracted programs:
Anthropic 1GW in 2026 scaling to 3GW in 2027; OpenAI's first-gen XPU shipping 2027 at 1GW+; Meta's
MTIA confirmed still shipping; Apple newly disclosed in 2026.

## Why it's irreplaceable — and the honest caveat

This is the pick's most contested dimension, and one panelist rejected the name outright over it.

**The moat.** To displace Broadcom, a hyperscaler cannot simply buy a different chip — it must build
an entire custom-silicon organization: high-speed SerDes, advanced packaging, IP libraries, and TSMC
relationship management. Broadcom's SerDes is what makes a multi-hundred-thousand-XPU cluster
physically work. An XPU program is a 2–3 year co-development; switching partners mid-program forfeits
schedule, which in this market is the scarcest asset of all. And the contracted programs run through
the entire 12–18 month horizon of this pick.

**The caveat, stated plainly.** Broadcom has no CUDA — there is no software lock-in, only IP and
program inertia. **Google, its anchor customer, has progressively internalized TPU design across
generations**, which is the precise shape of the trap: a customer that graduates. In custom silicon,
program losses are **binary and abrupt**, not gradual. Agent C (the quality/moat lens) refused to rank
Broadcom at all on this basis — "a business whose product is teaching hyperscalers to build their own
silicon eventually watches them graduate." I judged the risk **medium rather than high**, because the
graduation is a multi-year erosion while the contracted book covers the holding period, and because
the same force is *additive* to Broadcom across its five other named programs. A reader who weights
that dissent more heavily than I did should own LRCX instead — see *If forced to ONE* in
`final_ranking.md`.

## Valuation note — the screen's number is wrong

`shortlist.json` reports forward P/E **20.1**. The research could not reproduce that from any
near-term earnings basis. Consensus FY27 EPS is ~**$17.54** → **~23.8x**; on FY26 (~$11.6) it is
**~36x**. The screen appears to be on a two-years-forward basis for several names. **Do not treat AVGO
as a 20x stock.** This affects the whole shortlist and is logged as a bug to fix in `screen.py`.

## Earnings-quality flags — both resolve benign

- **RECEIVABLES_OUTRUN** (+46.8pp over revenue growth): **benign.** DSO is **~44 days** — low for a
  semiconductor company. Receivables outgrow *trailing* revenue arithmetically when the shipment rate
  is accelerating +32% sequentially, and the counterparties are the most creditworthy buyers on earth.
  There is no fragmented channel to stuff.
- **INVENTORY_BUILD** (+66.7pp): **benign, and arguably under-stocked.** Inventory of $4,328M is
  **~55 days** against Q2 COGS, versus a 100–130 day semiconductor norm. A company guiding +32%
  sequentially must build inventory to ship it, and this inventory has a contracted buyer attached
  before it is built.

The genuine earnings-quality question the screen did *not* catch: the GAAP/non-GAAP gap from VMware
amortization and stock comp, and the **circularity** of Broadcom helping finance (via the XPV vehicle)
the customers who buy its chips.

---

## Scenarios & expected value

Built bottoms-up on the shortage math — AI revenue × margin, not a bare multiple. Baseline: FY26 AI
~$56B + non-AI ~$46B ≈ $102–104B total; FY27 AI target $100B+ + non-AI ~$48B ≈ ~$148–150B at a ~67%
non-GAAP operating margin on ~4.46B shares, which reconciles to the $17.54 FY27 consensus EPS.

| Scenario | Target | By | Prob | The driver-level build |
|---|---|---|---|---|
| **Bear (= the stop)** | **$285** (**−31.8%**) | 2027-06 | **25%** | The trap fires or AI capex digests. FY27 AI lands ~$75–80B rather than $100B+ — the size of hole **one lost XPU program** makes. FY27 EPS ~$13.5, and a growth miss de-rates a semi hard, to ~21x. |
| **Base** | **$505** (**+20.8%**) | 2027-11 | **45%** | The $200B+ 18-month book converts roughly on schedule. FY27 AI ≈ $100B, total ≈ $148B, EPS ≈ $17.50. Multiple settles ~29x — a premium to market but below today's ~36x FY26, reflecting deceleration into FY28. |
| **Bull** | **$645** (**+54.2%**) | 2027-12 | **30%** | AI revenue clears ~$110B as the XPV platform's 20GW converts and Anthropic scales 1GW → 3GW. FY27 EPS ~$19.5 at ~33x. |

**Probabilities — reasoning (not a default 25/50/25).** Bull carries an above-default 30% because the
evidence is *accelerating and contracted*: bookings at ~3x shipments, a +200% y/y AI guide for Q3, and
a financing vehicle that removes the demand-side funding constraint — that combination has historically
preceded upward revisions rather than downward ones. Bear is held at a full 25% despite that, because
customer concentration is the sharpest in the field, program losses are binary, and the $100B FY27
target is already embedded in the price with no valuation cushion. Base is the residual 45%.

**Expected value = 0.25($285) + 0.45($505) + 0.30($645) = $492.00 → +17.7% vs $418.16.**
**Clears the +15% EV guardrail.** This is an actionable pick.

**Market-implied scenario:** at $418.16 the price sits **~60% of the way from bear to base** — closest
to base, but not yet at it. It trades **below** the analyst mean target of $527.88, so no red flag on
that test. The market is not paying the bull case today.

*Every number above is a research scenario, not a guarantee.*

---

## Key swing factors

1. **Does FY27 AI revenue actually reach $100B+?** The FY26 $56B was reiterated rather than raised —
   the next update is the tell.
2. **Google's XPU content per generation.** Internalization at the anchor program is the trap's
   specific mechanism.
3. **XPV drawdown pace.** Whether the $35B tranches fund on schedule (Anthropic 1GW mid-2026 → 3GW 2027).
4. **HBM4 / CoWoS supply.** Broadcom sits downstream of the same physical bottleneck as Nvidia; it
   cannot ship what the memory makers cannot supply.
5. **The non-AI drag.** AI grew 143% while total grew 48% — the remainder is close to flat, and VMware
   has already missed once.

## EPIC driver table

| Driver | **E**ffect | **P**redictability | **I**ndependence | **C**onsensus gap |
|---|---|---|---|---|
| **FY27 AI revenue reaching $100B+** | ✓ ~2/3 of the equity value | ✓ bookings 3x shipments; multi-year contracts | — the market watches this number closely | — **none; already in consensus EPS of $17.54** |
| **Custom-ASIC share gain vs merchant GPU** | ✓ decides the terminal market size | ✓ ASIC shipments +44.6% y/y vs 16.1% merchant | ✓ market prices AVGO and NVDA as correlated AI beta | ✓ our view: they are **opposite sides of one trade**; falsifiable by tracking XPU-vs-GPU mix |
| **AI-infrastructure financing availability** | ✓ gates conversion of the whole book | — credit conditions are not forecastable from evidence | ✓ market treats booked backlog as demand-certain | ✓ our view: **this, not customer demand, is the fragility** |

**Why these beat the deprioritized ones.** The consensus gap is **not** in the headline AI number —
buying that is buying consensus, and the table says so honestly. The differentiated view sits in
drivers 2 and 3: that Broadcom is a *hedge against the very trap* threatening most of this field, and
that the real fragility is vendor-adjacent financing rather than end demand. If those two are wrong,
this is just AI beta at 36x.

## Sizing note — POLICY.md applied

The repo's pre-committed policy, with this pick's numbers (not personalized advice):

```
raw  = (EV/price − 1) / (1 − bear/price)
     = (492.00/418.16 − 1) / (1 − 285/418.16)
     = 0.1766 / 0.3185 = 0.554
size = min(5.0%, 2.5 × 0.554) = 1.39%
```

- **Earnings halving:** next earnings **2026-09-02**, 29 days out — **outside** the 10-day window, so
  no halving on that ground.
- **Pilot regime (POLICY §1.4/§5):** the ledger has no realized track record yet, so all sizes run at
  half → **≈0.69% of investable capital.**
- Per-pick cap 5%, system cap 15% across open picks, **cash only**.

The modest size is the formula working as intended: the edge is good (+17.7%) but the modeled downside
is a −32% drawdown, and the ratio of the two is what sets position size.

## Holding period & exit plan

**Recommended hold: ~12–18 months**, tied to the FY27 conversion cycle. The thesis is settled not by a
quarter but by whether the 18-month book converts — FY27 ends November 2027, the natural horizon.

- **Base target $505 by ~2027-11**, as FY27 revenue proves out.
- **Bull target $645 by ~2027-12** if FY27 AI clears ~$110B and estimates re-rate with it.
- **Exit at $285** (the bear = the stop; `scorecard.py` enforces it on a close through), **or
  immediately on any thesis-break trigger below.**

**Thesis-break exit triggers — sell now, the story changed:**
- AI book-to-bill falling **below ~1.5x** in any quarter (the order book is the whole thesis).
- FY27 AI guidance cut **below ~$90B**.
- **A named XPU program loss** — Google, Meta, OpenAI, Anthropic, Apple or ByteDance.
- XPV tranches failing to fund, or AI-infrastructure credit spreads blowing out.
- Non-GAAP operating margin **rolling over sequentially** from the 67% peak.

**Leverage-safety note (risk education, not a recommendation).** This is a high-beta AI cyclical
already −13% from its 52-week high, and the modeled bear is a **−32%** move. Names in this complex
have historically de-rated 40–50% in a capex pause, and they do it in weeks rather than quarters — a
drawdown of that speed is brutal on margin, because the position can be liquidated at the bottom
before the thesis has been disproven. POLICY.md makes this repo's picks **cash-only, no margin, no
options as leverage substitutes**; that is policy here, not advice.

## Key risks / what invalidates the thesis (the trap case)

1. **The trap: customer graduation.** Google has already progressively internalized TPU design. A
   handful of programs drive ~half of revenue, and losses are binary. This is why one panelist
   excluded the name entirely.
2. **Circular financing.** The $35B XPV vehicle funds deployments that generate Broadcom revenue. If
   AI-infrastructure credit tightens, demand and financing fail *together* — the same reflexivity as
   Nvidia's equity stakes, in debt form.
3. **The $100B FY27 target is in the price.** Delivering "only" $80B is a severe de-rating.
4. **Marvell** competes for every socket; a lost socket is unrecoverable for years.
5. **Upstream physical limits.** HBM4/CoWoS constrain what can actually ship.
6. **Valuation.** ~36x FY26 means underwriting the FY27 doubling with no margin for slippage.

## What was verified (Phase 3.5)

An independent verifier subagent — which had *not* read the dossier — checked 14 claims against
primary sources. **12 CONFIRMED, 1 UNVERIFIED, 0 CONTRADICTED.**

| Claim | Verdict |
|---|---|
| >$30B AI bookings vs $10.8B shipped, Q2 FY26 | **CONFIRMED** — verbatim Hock Tan, 2026-06-03 call. Nuance: "over $30B" is a floor, so ~2.8x is a *minimum*; a call statement, not a filed metric |
| Q2 revenue $22.2B +48%, record ~67% non-GAAP op margin | **CONFIRMED** — exactly $22,187M; 67.3% |
| Q3 guide ~$29.4B (+84%); AI $16.0B (+200%); FY26 AI ~$56B | **CONFIRMED** — with the nuance that $56B was **reiterated, not raised**, and the stock sold off that day on it |
| $100B+ annual AI revenue from FY2027 | **CONFIRMED as a management forecast** (not a contracted figure) |
| $35B Apollo/Blackstone AI XPV Platform, >20GW through 2028 | **CONFIRMED**, dated **2026-06-09** |
| Broadcom holds 70%+ of custom XPU design services | **UNVERIFIED** — no primary source; Bloomberg Intelligence 60–80%, Counterpoint ~60% for 2027. **Softened in this writeup.** |
| Next earnings date | **CONFIRMED — 2026-09-02, after close** |

Claims for the ranked #2 and #3 (LRCX, MSFT) were verified in the same pass; two corrections from it
are carried into `final_ranking.md` (LRCX's $5.82 FY26 EPS is non-GAAP vs $5.76 GAAP; MSFT's +32% EPS
growth is GAAP and OpenAI-inflated, versus **+23% adjusted** and +18% operating income). Full detail:
`parts/2026-08-04/verification.md`.

## The panel

Four independent Opus subagents, one per lens, each reading the same dossier, dispatched sequentially.
Weighted vote: top pick 2, runner-up 1.

| Lens | Top pick | Runner-up | Conviction |
|---|---|---|---|
| **A — supply-chain analyst** | **AVGO** | GE | 8/10 |
| **B — growth/momentum** | **AVGO** | APH | 8/10 |
| **C — quality/moat & irreplaceability** | LRCX | KLAC | 8/10 |
| **D — contrarian/risk skeptic** | MSFT | NVDA | 7/10 |

**Tally: AVGO 4 · LRCX 2 · MSFT 2 · GE 1 · APH 1 · KLAC 1 · NVDA 1.**

**How I adjudicated.** AVGO won on the vote and on the merits: A and B converged on it from opposite
directions — A because it has the only *computable* forward ratio in the field (both halves of the
book-to-bill disclosed for the same period, unlike Nvidia's "$1 trillion" characterization), B because
its forward quarter is a third larger than the delivered one. The decisive question was C's veto. The
protocol makes the trap a near-disqualifier, so I tested it directly: is the disintermediation threat
against *Broadcom* credible and high, or medium? I judged **medium** — the customers who could
graduate must first replicate SerDes, packaging and IP at scale; the contracted programs cover the
entire holding period; and Broadcom gains from the same in-sourcing wave across five other named
programs. That is materially different from Nvidia, whose four largest customers ship direct
substitutes today. D's MSFT is the better risk-adjusted business, but its EV lands at +12.6%, below
the guardrail, and verification weakened its headline growth figure (+32% GAAP → +23% adjusted).
C's LRCX has the stronger moat and ranks #2 overall, but its EV is +12.0% — also short of the bar.
**AVGO was the only one of the panel's four nominees whose expected value cleared +15%.**

## Screen metrics (from `shortlist.json`, 2026-08-04)

`composite_score` 0.701 · `rev_growth` 0.239 · `operatingMargins` 0.490 · `returnOnEquity` 0.372 ·
`net_debt_ebitda` 1.08 · `dist_sma200` +0.140 · `dist_52w_high` −0.130 · `ret_12m` +0.459 ·
`analyst_upside` +0.262 · `forwardPE` 20.1 *(unreliable — see valuation note)* ·
`recommendationKey` strong_buy · `earnings_quality.flags` RECEIVABLES_OUTRUN, INVENTORY_BUILD *(both
resolved benign)*

---

## Disclaimer

**2026-08-04.** This is AI-generated research output for education and personal decision support. It is
**not financial advice**, not a recommendation to buy or sell any security, and not personalized to
anyone's circumstances. Every price target, probability and expected value above is a modeled research
scenario, not a forecast or a guarantee. Figures were verified against primary sources where stated,
but errors are possible and some claims are explicitly marked unverified. Do your own research and
consider consulting a licensed financial adviser.
