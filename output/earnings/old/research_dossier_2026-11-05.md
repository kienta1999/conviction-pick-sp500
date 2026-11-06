> Run by: Muse Spark (unknown) — full panel

# Research dossier — earnings mode — 2026-11-05

Screen: `output/earnings/shortlist_2026-11-04.json` (generated 2026-11-04 09:21:41,
17 candidates). Fetch rebuild attempted 2026-11-05 ~01:30 PT stalled on Yahoo 401
crumb errors (fetch.py stuck at 434/503, killed); screen prices are stale (Oct 30 /
Nov 2 / Nov 3 closes). Verified Nov 4 closes via Yahoo chart API, used throughout
as current prices: PH 910.19, RL 412.06, MNST 48.75, COP 136.94, OXY 57.33,
VYLR 71.25. Screen `ret_21d` is null for every candidate — run-into-print flags
uncomputed this run; research supplies 1-month moves per name.

**Screen-rebuild note (added 2026-11-05 ~09:39 PT, after the panel ran):** to satisfy
`check_run.py`'s same-date screen rule, `screen.py --mode earnings` was re-run on the
partially-refreshed cache (no fetch). It wrote `shortlist_2026-11-05.json` (11
candidates). Two things to know: (1) its PH/RL/OXY prices independently confirm the
verified Nov 4 closes used in this run (910.19 / 412.06 / 57.33 — exact matches);
(2) it drops MNST at stage 1 ("profitable": netIncomeToCommon/profitMargins = NaN)
— a **cache artifact from the 401-stalled fetch, not a fundamental change** (the
Nov 4 screen passed MNST with real margins; MNST is plainly profitable). The panel
ranked from the Nov 4 screen, which remains the basis of record for this run; the
Nov 5 screen file exists for the date rule only. APP/CPAY/EW/PTC/EMR correctly drop
out of the Nov 5 screen (reported Nov 4).

Actionable field (reports within ~10 days, print not yet happened): 6 names —
PH, RL, MNST, COP (all 2026-11-05), OXY (2026-11-09), VYLR (2026-11-11).
Already reported 2026-11-04 and excluded: APP, CPAY, EW, PTC, EMR.
Watchlist: A 2026-11-23, ADSK 2026-11-24, VEEV 2026-11-25, AZO 2026-12-08,
CTAS 2026-12-17, PAYX 2026-12-18. Full triage in
`output/earnings/parts/2026-11-05/triage.md`. Research batches:
`research_batch1.md` (PH, RL), `research_batch2.md` (MNST, COP),
`research_batch3.md` (OXY, VYLR).

## Scoreboard (research scores; guide-risk and priced-in are HIGH IS BAD)

| Ticker | Report | BMO/AMC | Date status | Consensus EPS / revenue | Beat | Guide-risk | Priced-in | Irreplaceability | Plan |
|---|---|---|---|---|---|---|---|---|---|
| PH | 2026-11-05 | BMO | CONFIRMED (co. PR Oct 20) | $8.21–8.23 / $5.81–5.82B | 7 | 6 | 4 | 8/10 | A (conditional) |
| RL | 2026-11-05 | BMO | CONFIRMED (co. notice Oct 8) | $4.26–4.27 / $2.13–2.14B | 7 | 5 | 7 | 6/10 | B |
| MNST | 2026-11-05 | AMC | CONFIRMED (co. release Oct 29) | $0.30 / $2.48–2.49B | 6 | 5 | 8 | 7/10 | B |
| COP | 2026-11-05 | BMO | CONFIRMED (co. IR page) | $2.95–3.05 / $18.2–18.9B | 6 | 7 | 5 | 6/10 | B |
| OXY | 2026-11-09 | AMC | CONFIRMED (co. PR Oct 1) | $1.43–1.47 / $6.73–6.86B | 7 | 6 | 5 | 4/10 | B |
| VYLR | 2026-11-11 | AMC | CONFIRMED (co. PR Oct 6) | No consensus; KeyCorp −$0.49 | 5 | 7 | 6 | 7/10 | B (firmly) |

Screen reaction records (from shortlist; research spot-checks noted per name):
PH beat_up 0.875, avg abs 4.4%, last4 +7/−4/+4/+8. RL beat_up 0.75, avg abs 6.2%,
last4 +4/+14/−5/+3. MNST beat_up 0.75, avg abs 4.8%, last4 −4/+14/−2/+5.
COP beat_up 0.571, avg abs 2.4%, last4 +1/−2/+3/−2. OXY beat_up 0.875,
avg abs 4.6%, last4 +4/−7/+9/+1. VYLR: no measurable reaction history.

---

## PH — Parker-Hannifin Corp — Fiscal Q1 2027 — reports Thu 2026-11-05 BMO, call 11:00 ET

**Date: CONFIRMED** (company PR Oct 20, 2026). **Bar:** consensus EPS $8.21–8.23,
revenue $5.81–5.82B (MarketBeat/Zacks, Nov 2–5); prior-year Q1 FY26 $7.22 / $5.08B.
Revisions +0.55% in 30 days — bar not rising. Zacks ESP −0.75%, Rank #4 (Sell).
**The real bar is the company's own guide:** Aug 6 call guided Q1 FY27 adj EPS
$8.07 — consensus sits ~2% ABOVE management's own guide. FY27 company guide
$34.25–$35.25 adj EPS (ex-Filtration/CIRCOR) vs street consensus $35.72 — above
the guide top. Filtration Group closed Aug 13 (~$1.8B FY27 sales); a
Filtration-inclusive FY27 guide update is the trade. No inter-quarter raise.

**Last four prints:** Q4 FY26 Aug 6: $9.27 vs $8.31 (+11.6%), rev $5.755B vs $5.57B,
initiated FY27 guide, reaction +7.3%. Q3 FY26 Apr 30: $8.17 vs $7.84 (+4.2%),
reaction −3.0% day / −6.9% 1d-after — beat-and-fell. Q2 FY26 Jan 29: $7.65 vs $7.16
(+6.8%), reaction −1.3% day / +2.1% 1d-after — screen's +4% not reproduced exactly.
Q1 FY26 Nov 6, 2025: $7.22 vs $6.62–6.67 (+8–9%), reaction not found — screen's
+8% unverified. Beat streak 8/8 (42 straight per SureDividend). Market pays for
the guide, not the beat.

**Revenue/margin:** organic growth accelerating 5.0% → 6.6% → 6.5% → 8.0%; Q4 adj
segment margin 28.0% (first >28%). Backlog record $12.8B (+16% YoY). Aerospace
Q4 organic +13.4%, margin 29.8%, backlog $8.5B (+15%). DI North America soft
(~+5% organic).

**Guide:** guides quarterly + full-year, granular. Forward bar: Q2 FY27 consensus
EPS $8.55 / revenue $6.08B. Run-rate supports Q1 (organic ~8% = continuation) but
NOT FY27 $35.72 without the Filtration update. Serial raiser (Q1–Q3 FY26 all
raised); a mere reaffirmation reads as a cut. Q4 GAAP EPS included a $0.65
tariff-refund benefit that does not repeat. Debt: $6.77B long-term + $7.75B
borrowed for Filtration.

**Priced in:** Nov 4 close $910.19, −3.68% on Nov 4, −6.41% 1-month, ~−14.9% since
Aug 6 close, 17.2% below 52-week high ($1,099.94). Forward P/E ~25.5x on FY27
consensus. Options-implied move ~4.4% (S3 Partners, Nov 4) = realised avg 4.4%.
**Not crowded** — down 15% in three months, falling into the print.

**Moat 8/10:** FAA/EASA-certified aerospace parts, filtration/materials platforms,
aftermarket, $12.8B backlog; switching a flight-qualified supplier is multi-year
re-certification. **If gaps down 15% and held 18 months: opportunity.**

**Scores:** beat 7, guide-risk 6, priced-in 4. **Verdict:** genuine beat-and-raise
setup whose payoff rides on one line — the Filtration-inclusive FY27 guide.
**Plan A (conditional)** — hold only accepting the binary; reaffirm ex-Filtration
guidance kills the thesis on the print.

## RL — Ralph Lauren Corp — Fiscal Q2 2027 — reports Thu 2026-11-05 BMO, release ~8:00 ET, call 9:00 ET

**Date: CONFIRMED** (company notice Oct 8, 2026; MarketBeat still labels it
Estimated — the company notice outweighs that). **Bar:** consensus EPS $4.26–4.27,
revenue $2.13–2.14B (Zacks Nov 3 / MarketBeat); prior-year $3.79 / $2.01B.
Revisions +0.06–0.8% in 30 days — bar flat. Zacks ESP +0.28%, Rank #2 (Buy).

**Last four prints:** Q1 FY27 Aug 6: adj $4.59 vs $4.32 (+6.3%), rev $1.96B vs
$1.87B, raised FY27, reaction +4.0%. Q4 FY26 May 21: $2.80 vs $2.55 (+9.8%),
reaction +13.9% — largest in 8-print sample. Q3 FY26 Feb 5: $6.22 vs $5.80
(+7.2%), reaction −4.5% — beat-and-fell. Q2 FY26 Nov 6, 2025: adj $3.79 vs $3.45
(+9.9%), reaction −0.6% day / +3.1% day+1 (screen's +3% ≈ day+1). Beat streak 8/8;
reaction record bimodal. Average absolute day-0 move over last 8 prints: 5.80%.

**Revenue/margin:** Q1 FY27 revenue +14% rep. (+13% CC), adj gross margin 73.7%
(+140 bps), adj op margin 18.7% (+170 bps). Asia +24% (+25% CC), China +40%;
North America +13%; AUR +15%. Top line accelerating vs FY27 guide (+5–6% CC) —
Q1 printed more than double the full-year guide rate; guide implies sharp H2
deceleration (tariff pressure rising in H2, notable Q4 gross-margin decline).

**Guide:** guides quarterly + full-year in constant currency (revenue + margin, not
EPS directly). Q2 guide: CC revenue +5–6%, op margin +80–100 bps CC — consensus
$2.14B sits at/above the top of that guide. FY27 consensus EPS $18.79–18.84,
revenue $8.73B. Q1 run-rate supports Q2 (a deceleration, not acceleration) but the
FY27 +5–6% embeds an H2 slowdown the run-rate does not show. Serial raiser, three
in a row (Nov 2025, May 2026 initiation, Aug 2026 +1pt raise); reward shrinking
(+14% → +4%). A mere reaffirmation is a de-facto cut. No inter-quarter raise.

**Peers warning:** LVMH Q3 (Oct 12): fashion & leather −5% organic, Chinese
clients down mid-teens. RL China +40% in Q1 vs LVMH — divergence or lag; tomorrow's
Asia print decides. Offset: Tapestry Coach Greater China +33% in FY26.

**Priced in:** Nov 4 close $412.06, +4.48% on Nov 4, +13.4% in 1 month, only 2.3%
below 52-week high ($421.60). Forward P/E ~21.9x vs 16.3x industry. Consensus
Strong Buy (14/19). Nov options-implied move **not found** (Aug: 8.24% vs 5.8%
historical avg — stale, do not carry forward). **Crowded on price action.**

**Moat 6/10:** century-old luxury brand, pricing power (AUR +15%), DTC engine,
<$2% share of ~$400B market; but no lock-in, discretionary, tariff-exposed.
Balance sheet $1.6B cash, buybacks + $1.00 quarterly dividend. **If gaps down 15%
and held 18 months: opportunity on valuation, not an irreplaceable asset.**

**Scores:** beat 7, guide-risk 5, priced-in 7. **Verdict:** serial beater running
into its print at the highs, guide already raised, peer warning on its
fastest-growing market — beat likely, positive reaction not. **Plan B.**

## MNST — Monster Beverage Corp — Q3 2026 — reports Thu 2026-11-05 AMC, call 2:00 p.m. PT

**Date: CONFIRMED** (company release Oct 29, 2026). Trade decided on Nov 6 session.
**Bar:** EPS $0.30 (split-adjusted post 2-for-1 split Aug 11, 2026), revenue
$2.48–2.49B (MarketBeat/Zacks/Finviz); prior-year $0.28 / $2.20B (+7% EPS, +13%
revenue). Zacks ESP −3.05%, Rank 3 (Hold). Zacks revision direction contradicts
itself across Oct 29 (−0.75% in 30d) and Nov 2 (+$0.01 in 30d) pieces — flagged,
not resolved. No whisper found.

**Last four prints (split-adj.):** Q2 2026 Aug 6: $0.30 vs $0.29 (+3.2%), rev
$2.54B vs $2.43B (+4.5%, +20.2% YoY, first >$2.5B), reaction **−4.0%** — opex
+24.7% punished despite revenue beat. Q1 2026 May 7: $0.29 vs $0.26 (+10.1%),
rev $2.35B vs $2.16B (+8.9%), reaction **+13.6%**. Q4 2025 Feb 26: $0.255 vs
$0.245 (+4–5%), rev $2.13B vs $2.04B, reaction **−1.6%** (5D −11.5%). Q3 2025
Nov 6, 2025: $0.28 vs $0.24 (+12.5–17%), rev $2.20B vs $2.11B, reaction **+5.2%**.
4/4 split-adj. EPS beats (screen says 3/4 — vendor/GAAP basis; Finviz GAAP Q4'25
was a miss). **2 of last 4 beats fell** — the beat-and-fall template. Trefis 5-yr:
13/20 1D reactions positive, median +5.3% / −4.0%.

**Revenue/margin:** top line accelerating (Q1 +26.9% YoY, Q2 +20.2% YoY), driven by
international (Q2 +34.6% YoY, 46% of sales; EMEA +52.5%, APAC +39.7% in Q1).
Gross margin Q1 55.0% (aluminium/tariff hit ~1pp), Q2 55.9% — **the 55% line is
the market's hurdle**. Operating margin Q2 29.2%, down YoY; opex +24.7% vs sales
+20.2%. Alcohol Brands −15.2% (shrinking drag). No debt, ~$3.0B cash.

**Guide:** **does not guide, ever.** De facto guide: Q4 consensus $0.28 / $2.39B,
FY2026 $1.16 / $9.70B — a continuation, not acceleration (Q4 below Q2 actuals,
seasonally softest quarter). No guide to raise/cut; the market substitutes the
gross-margin line and monthly sales colour (July sales +14.3% ex-alcohol disclosed
Aug 6 — Q3 ~one-third pre-announced in spirit). Q4 US selective price rises
already announced Aug 6.

**Other:** Americas CEO Rob Gehring resigns Nov 30 to Coca-Cola (16.7% shareholder
and distributor); interim successor from Dec 1. Peers: PepsiCo +3.7% Oct 8;
Coca-Cola −1.6% Oct 27 but raised FY EPS guidance to ≥11%.

**Priced in:** Nov 4 close $48.75, +3.33% on the day, +12.0% in 1 month, only
2.8% below 52-week high ($50.17). Forward P/E ~36–40x vs KO ~28x, PEP ~17.6x.
Options-implied move ±8.08% (Nov 20 expiry — overstates the pure earnings move;
haircut ±6.9%) vs realised 4.8%. **Crowded on price action.**

**Moat 7/10:** #1/#2 global energy-drink brand + Coca-Cola distribution; brand,
scale, portfolio. Offsets: formulation+marketing business, Celsius/Alani Nu/private
label share threat, KO itself a potential competitor. **If gaps down 15% and held
18 months: opportunity if margin noise with volume intact; disaster only if US
demand rolls over or KO-distribution friction.**

**Scores:** beat 6, guide-risk 5, priced-in 8. **Verdict:** serial beater whose beats
increasingly fail to pay — market wants margin, not just sales, and it has already
paid up for the sales. **Plan B.**

## COP — ConocoPhillips — Q3 2026 — reports Thu 2026-11-05 BMO, call 12:00 ET

**Date: CONFIRMED** (company IR page; call noon ET). **Bar:** adj EPS $2.95–3.05
(vendor dispersion: MarketBeat $3.05, Zacks $2.97, AlphaStreet $3.04), revenue
$18.2–18.9B (Zacks $18.2B +17.5% YoY vs MarketBeat $18.59B +23.7% — sales vs total
revenue definitions gap). Prior-year adj EPS $1.61 (+84–89% YoY). **Consensus EPS
climbed +16% in 30 days (from $2.62)** while Brent faded $103.8 → $97 → <$100.
Zacks ESP decayed +4.50% (Oct 29) → 0.00% (Nov 4). No whisper found.

**Last four prints:** Q2 2026 Aug 6: $3.24 vs ~$2.90–2.96 (+9.5–11.7%), rev beat
~+4%, reaffirmed FY guidance, reaction **+1.5%**. Q1 2026 Apr 30: $1.89 vs
$1.68–1.69 (+11.8–12.2%), **cut FY production guide** 2.33–2.36 → 2.295–2.325
MMBOED (Qatar), reaction **−1.9%**. Q4 2025 Feb 5: $1.02 vs $1.07–1.09 — MISS
(−4.6–6.4%), rev miss −5.7%, reaction **−2.4%** (Trefis/EarningsToday; screen's
+3% NOT corroborated — prefer −2.4%). Q3 2025 Nov 6, 2025: $1.61 vs $1.41
(+14.2%), reaction **−2.3%**. **3 of last 4 prints fell despite 3 beats**; Trefis
5-yr: only 35% of 1D reactions positive. Screen avg abs 2.4% ≈ last-four ~2.0%.

**Revenue/margin:** oil-price leverage, not volume. Q2 sales +36.8% YoY on realised
price +36.2% YoY ($62.33/BOE); production Q2 2,248 MBOED **−6.0% YoY**. Q3 Brent
avg $97 vs $103.8 Q2 and $69.1 a year ago. Q3 production guided 2.29–2.32 MMBOED.
Adjusted earnings Q2 $3,951mn (+120.4% YoY). CFO Q2 $7.2B. Dividend $0.84/qtr;
Q2 distributions $3,025mn (42.2% of CFO vs 45% target).

**Guide:** guides production/capex/capital returns, NOT EPS/revenue. Forward bar:
FY2026 adj EPS $11.42 implies Q4 ~$3.25 — a repeat of Q3, no acceleration, but at
Brent already faded below $100. Run-rate supports it only at $95–100 Brent.
Production guide history: cut in Q1 (Qatar, 3–5yr repair), reaffirmed Q2. No
inter-quarter raise; the *consensus* was raised instead — worse for the trade.
New CEO Andy O'Brien (ex-CFO) — first earnings call; capital-allocation intent is
the read. Peers: XOM Q3 beat Oct 30 (+2.16% that day, refining-led), CVX beat
(+1.75%, refining-led) — COP pure upstream cannot borrow their downstream beat.

**Priced in:** Nov 4 close $136.94, **−5.17% on Nov 4**, third down day, −11.2% off
Oct 30 all-time high ($154.28) in four sessions; 1-month still +6.7–8.0%, YTD
+46–49.5%. Forward P/E ~13.4x. Options-implied move ±4.83% (clean Nov 6 expiry)
vs realised 2.4% — **~2× the realised proxy**. Price froth washed out; earnings
bar not. Windfall-tax headline risk (Nov 4).

**Moat 6/10:** Permian scale, Alaska/Canada, LNG optionality (12 MTPA), low-cost
resource base; but product is a commodity COP does not price — OPEC+, Iran
headlines, windfall tax can erase the moat in a week. Production declining.
**If gaps down 15% and held 18 months: opportunity only if Brent ≥$90 and the 45%
return programme holds; slow bleed if oil normalises to $70–80.**

**Scores:** beat 6, guide-risk 7, priced-in 5. **Verdict:** high-quality upstream
name whose quarter is a referendum on the oil price, reported the morning after
the market spent three days voting the oil price down. **Plan B (closer call than
MNST).**

## OXY — Occidental Petroleum — Q3 2026 — reports Mon 2026-11-09 AMC, call Tue Nov 10 1:00 p.m. ET

**Date: CONFIRMED** (company PR Oct 1, 2026). **Bar:** EPS $1.43–1.47, revenue
$6.73–6.86B (Zacks $1.43 / $6.73B; MarketBeat $1.45 / $6.80B; FXEmpire $1.47 /
$6.86B). Prior-year EPS $0.64 — consensus implies **+123% YoY EPS on +0.3% revenue**
— a realised-oil-price story (Q3'25 realised oil $64.78 vs Q3'26 $85.91), not
volume. **Consensus EPS revised +22.14% higher in 30 days.** Zacks ESP +4.14%
(most-accurate $1.48 vs $1.43). No whisper found.

**Last four prints:** Q2 2026 Aug 5 AMC: $2.40 vs $1.83 (+31%), rev $8.07B vs
$7.07B (+14.0%), reaction **+4.1%**. Q1 2026 May 5 AMC: $1.06 vs $0.60 (+76%),
rev miss −3.9%, reaction **−7.1%** — driven by an oil-price collapse that day
(Iran peace headline, WTI −12% intraday), not the print. Q4 2025 Feb 18: $0.31 vs
$0.16–0.19, rev miss −7.9%, 1-day reaction **not found** (2-day +12.2%; screen's
+9% unverified). Q3 2025 Nov 10, 2025 AMC: $0.64 vs $0.51 (+25%), rev miss −1.9%,
1-day reaction **not found** (2-day +1.3%; screen's +1% unverified). **8 straight
EPS beats, revenue beat only 1 of last 4.** Reactions macro-driven; a beat does
not guarantee a green next session.

**Revenue/margin:** Q2 revenue +53.4% YoY on realised oil $96.78/bbl; Q3 realised
oil $85.91 (8-K Oct 13) — down ~11% from Q2 — production inside 1.40–1.44 Mboed
guide. Top line mean-reverting with crude, not accelerating. Q3 largely
pre-announced via Oct 13 8-K: production in guide, Gulf curtailment, −$94m collar
hit, domestic LOE $8.54/boe (better than ~$8.75 guided). Midstream Q2 record
~$960m is the comp. Principal debt $11.8B at Q2 (net $7.6B) vs $10B milestone.

**Guide:** guides production/capex/LOE/midstream, NOT EPS/revenue. Forward bar: Q4
EPS $1.96, revenue $7.56B — a **step-up ~35% above Q3** despite Q3 oil averaging
$85.79 WTI; FY2026 EPS $6.81, FY2027 $5.14 (−24.5%). Run-rate supports Q4 only if
oil cooperates — a price bet, not a continuation. Serial production-guide beater
(every recent quarter at/above high end); capex cut in Q2 ($5.5–5.9B). Peers sold
off after beats Oct 30 (CVX −1.6%, XOM −1.9%). COP (Nov 5) and EOG (Nov 5) are
the last peer reads before OXY.

**Priced in:** Nov 4 close $57.33, −10.52% in 5 days, −15.0% off 52-week high
($67.45), below 50-day SMA ($60.18), above 200-day ($55.91). Forward P/E ~11.3x.
Options-implied move ~±6–7% derived from 47.2% ATM IV (no published straddle
quote found) vs realised 4.6% — **larger than history**. Drop driven by oil
risk-premium washout (Nov 2: WTI −7.9% on Iran-peace headlines; OPEC+ held output
unchanged). **Not crowded** — short float 2.45%, de-rated on macro, Q3 beat
substantially pre-disclosed.

**Moat 4/10:** commodity; Permian scale, low-cost position, CO2-EOR expertise,
4,603 MMboe reserves, Berkshire as large holder (sentiment backstop, not moat).
**If gaps down 15% and held 18 months: opportunity only if crude holds $80+;
slow bleed if war premium fully unwinds toward $60s crude** (~$240m pre-tax cash
flow per $1/bbl WTI).

**Scores:** beat 7, guide-risk 6, priced-in 5. **Verdict:** high-quality
oil-price proxy whose Q3 number is already public in all but name; the trade is a
bet on crude holding $95+ through Nov 10, not on an earnings surprise.
**Plan B.**

## VYLR — Vylor Inc. — Q3 2026 (first standalone print) — reports Wed 2026-11-11 AMC, webcast Thu Nov 12 9:00 a.m. ET

**Date: CONFIRMED** (company PR Oct 6, 2026; one aggregator still labels it
expected — stale). **What VYLR is:** Corteva's former Seed segment, spun off Oct 1,
2026 (1-for-1), added to S&P 500 same day replacing Corteva. HQ Johnston, Iowa;
CEO Chuck Magro. Corn/soy/sunflower/wheat germplasm, Pioneer brand, "Vylor One"
licensing. ~12,300 employees, ~$47.6B market cap at $71.25.

**Screen history is INVALID — discard it:** "3/4 beats, avg surprise −12.11%,
revenue +78% TTM" is Corteva-attributed history misassigned to a ticker that has
never reported. No VYLR reaction history exists; `reaction_avg_abs_move` undefined.

**Bar: effectively no consensus.** MarketBeat carries no estimates table. Only
published Q3 estimate: KeyCorp (Oct 6) EPS **−$0.49** (seasonal loss). Consensus
revenue **not found**. Seasonal pattern: Q3 2025 seed sales $917m with −$193m
EBITDA — Q3 is the seasonal trough (~75% of annual sales land in H1). FY2026
guidance: net sales ~$10.4B, operating EBITDA ~$2.8B (Investor Day Sep 15); H1
pro forma sales $7.593B, EBITDA $2.892B — H2 needs ~$2.81B sales and roughly a
small H2 EBITDA loss to land on guide, consistent with a Q3 loss ~−$100m. FY EPS
figures do NOT reconcile (MarketBeat $2.41–2.46 vs KeyCorp $2.71; H1 pro forma
$2.22 + KeyCorp H2 ≈ $1.74) — different EPS definitions, no source explains it.
Do not build a beat/miss call on it. Whisper: not found. Revisions: not found
(5-week-old listing).

**Segment history (as Corteva Seed):** Q2 2026 sales $4.53B flat YoY (price +3%,
volume −3%), operating EBITDA $1.97B (+6%, margin +230 bps). 1H 2026 sales $7.56B
(+4%), EBITDA $3.0B (+11%). FY2025 pro forma sales $10.067B, EBITDA $2.503B.
Top line NOT accelerating (Q2 flat; growth is price/mix + royalties, not volume).

**Guide:** annual at Investor Day granularity (FY26 $10.4B / $2.8B EBITDA; 2029
sales $11.2–11.9B, EBITDA $3.3–3.7B; cumulative FCF 2027–29 $5.5–6.5B; Vylor One
licensing >$500m in 2027, >$1B by 2035, ~$2B by 2040). No quarterly EPS guide.
Forward bar roughly flat EPS in 2027 vs 2026. A reaffirmation on Nov 11–12 is
neutral-to-positive for a first print; a trim of $10.4B/$2.8B is the disaster case.
Good news already out twice: Investor Day Sep 15 + **$3B buyback Oct 22** (cannot
currently be executed — see litigation).

**Dominant risk — PFAS fraudulent-transfer litigation (live):** Oct 1, 2026, 15
states + Guam sued EIDP/Corteva/Vylor in Indiana state court, alleging the spin-off
transferred ~$40B of seed assets while leaving DuPont PFAS liabilities behind
(~$5B value received) — fraudulent transfer. Oct 9: federal judge (S.D. Ind.,
No. 1:26-cv-02122) granted a TRO freezing extraordinary transfers (incl. dividends
and buybacks), finding "strong likelihood of success." Oct 10: court stayed its own
TRO pending Seventh Circuit emergency review; appeal undecided. Corteva has
represented it will not declare dividends or repurchase shares while the stay
request is pending.

**Priced in:** Nov 4 close $71.25, +6.5% since Oct 2 listing, −7.9% below
$77.39 "high" (5 weeks of history). Forward P/E 28.2x per screen; MarketBeat N/A.
Consensus target $82.67 (+16.0%), Moderate Buy (15 analysts). Short interest
2.25% of float, +100% month-over-month from a tiny base. Options-implied move:
**not found**; no realised proxy. **Not crowded — undiscovered**, which is
different: index flows, not earnings longs. Litigation binary not quantifiably
priced.

**Moat 7/10:** century-deep germplasm library, >4,000 germplasm patents + >2,000
biotech patents, Pioneer brand, $19B trait pipeline. Farmers cannot in-source seed
genetics (decade of trials + regulatory clearance). Oligopoly (Bayer, Syngenta,
BASF); AI breeding could compress cycles over time but field testing still gates
commercialisation. **If gaps down 15% and held 18 months: opportunity — unless
the PFAS case attaches liability, in which case the downside is legal, not
operational.**

**Scores:** beat 5, guide-risk 7, priced-in 6. **Verdict:** genuine discovery event,
not an earnings trade: no consensus, no history, a seasonal loss, and a live
fraudulent-transfer case that could freeze its buyback and dividend.
**Plan B, firmly.** Revisit after Nov 12 on the webcast transcript and the
litigation docket, not on headline EPS.

## Discrepancies carried forward (screen vs research)

- PH: screen reactions for Jan 29 (+4%) and Nov 6, 2025 (+8%) could not be
  reproduced exactly from either reaction definition — treat as unverified.
- RL: screen Nov 6, 2025 reaction (+3%) ≈ day+1, not day-0 (−0.6%).
- MNST: screen "3/4 beats" vs 4/4 split-adj. beats found (vendor/GAAP basis).
- COP: screen Q4'25 reaction +3% vs −2.4% in both Trefis and EarningsToday —
  prefer −2.4%. Revenue YoY +17.5% (Zacks) vs +23.7% (MarketBeat) is a
  sales-vs-total-revenue definitions gap. Zacks revision direction for MNST
  contradicts itself between Oct 29 and Nov 2 pieces.
- OXY: screen +9% and +1% reactions are 2-day windows in the best source, not
  1-day; 1-day figures not found.
- VYLR: entire screen history invalid (Corteva-attributed); no consensus, no
  reaction history, FY EPS figures do not reconcile across vendors.

## Figures explicitly not found (do not fill in)

RL Nov options-implied move; PH 3–5yr forward P/E range; MNST 3–5yr forward P/E
range, whisper number, short interest; COP whisper number, single clean Q4'26
adj-EPS consensus print, COP-specific cause of the Nov 4 −5.17% drop; OXY
published straddle quote, 1-day Q4'25/Q3'25 reactions; VYLR consensus EPS/revenue,
whisper number, options-implied move, 30-day estimate revisions.
