> Run by: Muse Spark (unknown) — full panel

# Final ranking — earnings mode — 2026-11-05

Field: 6 actionable names (reports within ~10 days, print not yet happened). The ranking is the whole field — **never padded** with names the screen didn't produce. Already reported 2026-11-04 (APP, CPAY, EW, PTC, EMR) are excluded; the watchlist is parked in its own table at the end.

Screen: `output/earnings/shortlist_2026-11-04.json` (generated 2026-11-04 09:21:41). Prices below are **verified Nov 4 closes** (Yahoo chart API) — the screen's prices are Oct 30 / Nov 2 / Nov 3 closes and are stale. A fetch rebuild was attempted and stalled on Yahoo 401 crumb errors (fetch.py stuck at 434/503, killed). Screen `ret_21d` is null for every candidate, so the run-into-print flag is uncomputed this run; the researched 1-month move is shown instead. **Post-panel note:** `screen.py` re-run ~09:39 PT on the partially-refreshed cache wrote `shortlist_2026-11-05.json` (11 candidates); it drops MNST at stage 1 on NaN profitability fields — a cache artifact from the stalled fetch, not a fundamental change (Nov 4 screen passed MNST with real margins). The Nov 4 screen remains the basis of record for this ranking; the Nov 5 screen's PH/RL/OXY prices independently confirm the verified Nov 4 closes used here (910.19 / 412.06 / 57.33).

## The ranking

| Rank | Ticker | Company | Sector / sub-industry | Price (Nov 4 close) | Analyst mean target (+upside) | Forward P/E | Beat | Guide-risk | Priced-in | Beat_up_rate | Avg abs move | Run into print | Plan | Report date | Days to print |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PH | Parker-Hannifin | Industrials / Industrial Machinery | \$910.19 | ~\$1,146 (+26%) | ~25.5x | 7 | 6 | 4 | 0.875 | 4.4% | −6.4% / 1 mo | B | 2026-11-05 BMO | 0 |
| 2 | OXY | Occidental Petroleum | Energy / Oil & Gas E&P | \$57.33 | \$67.88–71.85 (+18–25%) | ~11.3x | 7 | 6 | 5 | 0.875 | 4.6% | −1.3% / 1 mo; −10.5% / 5 d | B | 2026-11-09 AMC | 4 |
| 3 | RL | Ralph Lauren | Consumer Disc. / Luxury Apparel | \$412.06 | ~\$447 (+8%) | ~21.9x | 7 | 5 | 7 | 0.75 | 6.2% | +13.4% / 1 mo | B | 2026-11-05 BMO | 0 |
| 4 | MNST | Monster Beverage | Consumer Staples / Beverages | \$48.75 | ~\$71.86 (stale — do not use) | ~36.1x | 6 | 5 | 8 | 0.75 | 4.8% | +12.0% / 1 mo | B | 2026-11-05 AMC | 0 |
| 5 | COP | ConocoPhillips | Energy / Oil & Gas E&P | \$136.94 | \$145–151.56 (+6–11%) | ~13.4x | 6 | 7 | 5 | 0.571 | 2.4% | +6.7–8.0% / 1 mo; −11.2% off high | B | 2026-11-05 BMO | 0 |
| 6 | VYLR | Vylor | Materials / Seed & Genetics | \$71.25 | \$82.67 (+16%) | 28.2x (screen) | 5 | 7 | 6 | n/a | n/a | +5.9% since listing | B | 2026-11-11 AMC | 6 |

Beat / guide-risk / priced-in are the research scores (0–10; guide-risk and priced-in are HIGH IS BAD). Beat_up_rate, avg abs move from the screen's `print_reaction` block. "Run into print" is the researched 1-month move (screen `ret_21d` null). MNST's MarketBeat consensus target (\$71.86) looks stale/pre-split-contaminated — do not use it. VYLR has no measurable reaction history (first standalone print; screen history is invalid Corteva-attributed data).

## Borda tally (4 ballots, rank 1 = 10 pts … rank 6 = 5 pts)

| Ticker | Borda | Appearances | #1 votes | Avg placement |
|---|---|---|---|---|
| PH | 40 | 4/4 | 4 | 1.00 |
| OXY | 31 | 4/4 | 0 | 2.75 |
| RL | 30 | 4/4 | 0 | 3.25 |
| MNST | 28 | 4/4 | 0 | 4.00 |
| COP | 28 | 4/4 | 0 | 4.00 |
| VYLR | 23 | 4/4 | 0 | 4.75 |

**Tie at 28 points (MNST vs COP):** broken on the doctrine, not mechanically. MNST ranks above COP because its revenue is accelerating (+20.2% YoY, international +34.6%) with a 0.75 beat→up rate, while COP's beats are oil-price arithmetic (consensus EPS +16% in 30 days as Brent faded) with the field's worst reaction record (beat_up 0.571, only 35% of 5-year reactions positive). Both lenses that ranked COP above MNST (B and D, 3rd vs 5th) did so on the price washout, not on the earnings doctrine; lenses A and C ranked MNST above COP.

**Per-lens rankings:** A: PH, RL, OXY, MNST, COP, VYLR. B: PH, OXY, COP, RL, MNST, VYLR. C: PH, MNST, VYLR, RL, COP, OXY. D: PH, OXY, COP, RL, MNST, VYLR. Single-pick votes were unanimous: PH 4/4 (convictions 7 / 6 / 7 / 5), all Plan A (conditional) — overruled to Plan B by Gate A1 boxes 2 and 5 (see final_pick).

## Per-name thesis

### 1. PH — Parker-Hannifin (\$910.19, prints today BMO) — Plan B

The record is the field's best joint with OXY (8/8 beats, beat_up 0.875, largest recent surprise +11.6%) and the setup is the field's cleanest: organic growth accelerating to 8.0%, record \$12.8B backlog, and a stock that has fallen ~15% since Aug 6 with an implied move (~4.4%) equal to its realised average. Reaction record: the market pays for the guide — +7.3% on the Q4 beat-and-guide-initiation, −4.0% on the Q3 beat that carried no raise (Phase 3.5 corrected the day-0 figure). Guide risk is the whole trade: FY27 consensus \$35.72 sits above the ex-Filtration guide top \$35.25, so only a Filtration-inclusive raise wins; a reaffirmation is a de-facto cut. Priced-in risk is low on price (4/10). Rough moves: beat-and-raise +6–8% / in-line −4–6% / miss −7–10%. Plan B — Gate A1 boxes 2 and 5 are ticked, so the panel's conditional Plan A does not survive the checklist. Fallback: 8/10 moat, but Gate B EV +9.6% < 15% → **NO SAFE FALLBACK**. Full writeup in `final_pick_2026-11-05.md`.

### 2. OXY — Occidental Petroleum (\$57.33, prints Nov 9 AMC) — Plan B

Eight straight EPS beats with the two latest surprises enormous (Q2 +31%, Q1 +76%) and the most-accurate estimate above consensus (Zacks ESP +4.14%), but the quarter is largely pre-announced via the Oct 13 8-K (realised oil \$85.91, production in guide, Gulf curtailment, −\$94m collar hit) and the bar was revised +22% in 30 days. Reaction record: beat_up 0.875, avg abs 4.6%, last four +4/−7/+9/+1 — but reactions are macro-driven (Q1's −7.1% was an Iran-peace oil collapse that day), and Phase 3.5 corroborated the screen's +9% as a real 1-day move for Q4 2025 (+9.4% on Feb 19). Guide risk: no EPS guide to miss, but the forward bar is a Q4 step-up to \$1.96 (~35% above Q3) that the run-rate supports only if oil cooperates, and the Q2 midstream record (~\$960m) is a hard comp. Priced-in risk is balanced (5/10): the Q3 beat is pre-disclosed, but the stock is −15% off its high at ~11x forward after a −10.5% five-day oil washout. Rough moves: beat-and-hold +4–6% / in-line −1–3% / miss −5–7%. Plan B — a bet on crude holding \$95+ through Nov 10, not on an earnings surprise. Fallback: 4/10 moat (commodity); 12–18mo EV +13.2%, below the guardrail — flagged.

### 3. RL — Ralph Lauren (\$412.06, prints today BMO) — Plan B

Eight of eight beats with surprises of +6.3%, +9.8%, +7.2% and +9.9%, Q1 FY27 revenue +14% (+13% CC) — more than double the full-year guide rate — with Asia +24% and China +40%, AUR +15%, gross margin 73.7% (+140 bps). Reaction record is bimodal and shrinking: +13.9% on Q4 FY26, −4.5% on the Q3 beat, and the reward for the last raise was only +4.0%. Guide risk: Q2 guide is CC revenue +5–6% with op margin +80–100 bps, and consensus \$2.14B sits at/above the top of that guide; the FY27 guide embeds an H2 deceleration the run-rate does not show, so a mere reaffirmation is a de-facto cut — and LVMH just warned (fashion/leather −5% organic, Chinese clients down mid-teens) on the exact market RL printed +40% in. Priced-in risk is high (7/10): +13.4% in a month, 2.3% below the 52-week high, forward P/E premium to the industry, Strong Buy consensus. Rough moves: beat-and-raise +5–8% / in-line −3–5% / miss −7–10%. Plan B — the beat is likely, a positive reaction is not. Fallback: 6/10 moat (brand, no lock-in); 12–18mo EV +3.1%, below the guardrail — flagged.

### 4. MNST — Monster Beverage (\$48.75, prints today AMC) — Plan B

Genuine revenue acceleration (Q1 +26.9% YoY, Q2 +20.2% YoY, first quarter above \$2.5B) and a real distribution moat via Coca-Cola, no debt, ~\$3.0B cash — but its beats increasingly fail to pay: 2 of the last 4 beats fell (Q2 beat −4.0% as opex +24.7% outran sales +20.2%), and the market wants the 55% gross-margin line (Q2 55.9%), not sales. There is no guide to raise or cut, so the de-facto guide is Q4 consensus \$0.28 / \$2.39B plus the margin line. Priced-in risk is the field's highest (8/10): +12.0% in a month, 2.8% below the \$50.17 high, ~36–40x forward, implied move ±8.1% vs 4.8% realised. Americas CEO resigns Nov 30 to Coca-Cola (interim successor). Rough moves: beat +5% / in-line −2–4% / miss −6–9%. Plan B.

### 5. COP — ConocoPhillips (\$136.94, prints today BMO) — Plan B

Can beat (Q2 +9.5–11.7%, Q1 +11.8–12.2%) and the price froth has washed out (−11.2% off the Oct 30 all-time high in four sessions, −5.17% on Nov 4), but it has the field's worst reaction record: beat_up 0.571, 3 of the last 4 prints fell despite 3 beats, only 35% of 5-year reactions positive, avg abs move just 2.4%. Guide risk is the worst kind: consensus EPS climbed +16% in 30 days while Brent faded \$103.8 → \$97 → below \$100, Zacks ESP decayed +4.50% → 0.00%, production declining −6% YoY, and the FY2026 EPS \$11.42 implied Q4 of ~\$3.25 is pure oil arithmetic. New CEO Andy O'Brien's first call. Rough moves: beat-and-reaffirm +1–3% / in-line −1–3% / miss −2–4% — the small realised moves cap both sides. Plan B.

### 6. VYLR — Vylor (\$71.25, prints Nov 11 AMC) — Plan B (firmly)

Not an earnings trade: first standalone print (Corteva seed spin-off, listed Oct 1), no consensus (only KeyCorp −\$0.49 for the seasonal Q3 loss), no reaction history (screen history is invalid Corteva-attributed data), FY EPS figures that do not reconcile across vendors (\$2.41–2.46 vs \$2.71), and a live PFAS fraudulent-transfer case in which a federal judge granted a TRO on Oct 9 finding a "strong likelihood of success" (stayed Oct 10 pending Seventh Circuit review), with the \$3B buyback currently unexecutable. The moat is real (germplasm library, >4,000 germplasm + >2,000 biotech patents, Pioneer brand, \$19B trait pipeline; 7/10) and the FY26 guide (\$10.4B sales / \$2.8B EBITDA) is achievable on the run-rate — but a trim is the disaster case and the print is a discovery event, not a beat/miss event. Revisit after Nov 12 on the webcast transcript and the litigation docket.

## Just-missed names

None — the ranked field is the whole actionable field (6 names). Every name the screen produced for this week that had not already reported is ranked above. The five names that reported Nov 4 (APP, CPAY, EW, PTC, EMR) are not "just missed"; their prints already happened. The watchlist below is the queue, not the just-missed set.

## What the panel revealed

- **Agreement:** all four lenses picked PH as the single pick (convictions 7/6/7/5) and ranked it #1. The de-rating into the print plus the 8/8 beat record plus the record backlog was the one combination no lens could beat.
- **Disagreement:** everything below #1. Lens C (quality) ranked MNST #2 and VYLR #3 on moat; lenses B and D (setup/contrarian) ranked OXY #2 and COP #3 on the price washout; lens A (momentum) ranked RL #2 on the beat record. The split is a lens split, not a data split: the same facts (oil washout, RL's run-up, MNST's margin hurdle) read as opportunity to one lens and as trap to another.
- **The trap-hunter's note (lens B):** three names ran into their prints at or near highs (RL, MNST) or with a raised bar (COP, OXY), one name is unpriceable (VYLR), and one name — PH — fell into its print. PH leads despite its own guide risk because its trap is a single identifiable guide line, not a crowded price.
- **The contrarian's note (lens D):** NO TRADE was considered and rejected — the six guide traps are not equal, and PH is the only one where the price has already paid for the trap.
- **The re-vote problem:** PH was the single pick on 2026-11-03 and 2026-11-04 for this same print. A fourth straight PH pick is the panel re-voting the same trade, not a new decision — flagged by lenses B, C and D in their ballots and by triage. The setup has not changed, which is itself the point: the de-rating is the setup, and it is still there.

## If forced to ONE

**PH.** The strict trap-veto lands on the same name as the Borda #1: PH is the only name where the trap is a guide line on a de-rated stock rather than a crowded price or an unpriceable event. The veto does not move the pick — it confirms it, and it moves the *entry* (Plan B, not the panel's conditional Plan A).

## Return scenarios — top 3 (12–18 month fallback)

Anchored to the analyst mean target in the screen/dossier; every number a research scenario, not a guarantee. The guardrail (+15% EV) blocks *actionable single picks* only — names stay in the ranking with the flag visible.

| Ticker | Bear | Base | Bull | Probabilities (bear/base/bull) | EV | EV vs price |
|---|---|---|---|---|---|---|
| PH | \$750 by 2027-Q2 | \$1,050 by 2027-Q2 | \$1,200 by 2027-Q4 | 0.30 / 0.45 / 0.25 | \$997.50 | +9.6% — **below +15% guardrail (NO SAFE FALLBACK)** |
| OXY | \$48 by 2027-Q2 | \$70 by 2027-Q2 | \$76 by 2027-Q4 | 0.30 / 0.45 / 0.25 | \$64.90 | +13.2% — **below +15% guardrail** |
| RL | \$340 by 2027-Q2 | \$440 by 2027-Q2 | \$500 by 2027-Q4 | 0.30 / 0.45 / 0.25 | \$425.00 | +3.1% — **below +15% guardrail** |

- **PH:** targets carried from the 2026-11-04 panel's fallback build on the identical print/record; EV recomputed at the verified \$910.19. Base = FY27 EPS \$35.72 at ~29.4x; bull = Filtration/CIRCOR fold-in + multiple holds; bear = guide reaffirm + DI collapse + leverage reset at ~21x.
- **OXY:** base \$70 = analyst mean target (\$67.88–71.85, dossier); bull \$76 = Goldman target (Oct 27, Buy); bear \$48 = crude unwinding toward the \$60s (FY27 EPS \$5.14 at ~9.3x). Bear at 30% because the oil fade is live (WTI −7.9% on Nov 2).
- **RL:** targets carried from the 2026-11-04 panel (base \$440 / bull \$500 / bear \$340); EV recomputed at the verified \$412.06. Base ≈ screen mean target (~\$447); bull = beat-and-raise cadence + multiple holds; bear = tariff H2 margin hit + China softness + de-rate.
- **Market-implied scenario:** PH sits closest to bear/base (below the ~\$1,146 mean target); OXY sits below its mean target (bear/base); RL sits closest to base (just below its ~\$447 mean target).

## What was verified

Phase 3.5 verification (`output/earnings/parts/2026-11-05/verification.md`), run before the PH/RL BMO prints. All three report dates confirmed from company sources (PH Thu Nov 5 BMO, call 11:00 ET; OXY Mon Nov 9 AMC, call Tue Nov 10 1:00 p.m. ET; RL Thu Nov 5 BMO, release ~8:00 ET, call 9:00 ET). All consensus ranges, last-quarter surprises, next-quarter bars and core moat numbers check out. **Material corrections carried forward:** (1) PH Q3 FY26 day-0 reaction is **−4.0%** (not −3.0%; day+1 −3.0%, two-day −6.9%) — screen −4% is the correct day-0 figure; (2) PH Q2 FY26 day-0 reaction is **+3.5%** (not −1.3% — the dossier's day-0 sign was wrong; the print ROSE on the day), screen +4% reproducible, confirmed by Aardvark Labs; (3) OXY Q4 2025 reaction **+9.4%** on Feb 19 is a real 1-day move — screen +9% corroborated, dossier's "not found" retired; (4) PH Nov 6, 2025 +8% corroborated by press. **UNVERIFIED (not contradicted):** PH "multi-year re-certification" timeline; OXY exact 4,603 MMboe / ~72% developed (rounded 4.6B BOE confirmed); RL consensus \$4.27 top end not seen (majors show \$4.26). No date moved; no trade-invalidating contradiction. The Q2 PH correction does not change Gate A1 box 2 (Q3 FY26 was a beat that fell, and it is one of the last two prints).

## Risk lens & leverage-safety note

- **Sector concentration:** two of six names are oil price-takers (COP, OXY) whose quarters are referenda on Brent/WTI, not on execution; both printed into a three-day oil selloff. Do not treat them as diversifiers of each other.
- **Highest-risk vs steadiest:** VYLR is the highest-risk name (litigation binary + first print + no consensus); MNST is the most priced-in (8/10); PH is the steadiest compounder on the list (8/10 moat, record backlog) — which is why it leads despite its guide binary.
- **Drawdown reality:** single-session gaps of 10–20% are normal outcomes in this mode. APP's last four reactions include two −20% prints; MNST's implied move is ±8.1%; OXY's Q1 beat fell −7.1% on an oil shock. Leverage-safety is education, not advice: never a specific leverage multiple or position size — this is the mode where leverage is most obviously destructive.
- **Thesis-break / trap triggers to watch:** PH guide reaffirmation ex-Filtration (trigger never fires); RL Asia/China softness after the LVMH warning; MNST gross margin below 55%; COP production guide trim or a soft buyback signal on the new CEO's first call; OXY crude breaking down through Nov 10 or a soft Q4/2027 capex guide; VYLR FY26 guide trim or adverse Seventh Circuit news.

## Watchlist (reports beyond the actionable window)

| Ticker | Report date | Days out | Note |
|---|---|---|---|
| A | 2026-11-23 | 19 | 3/4 beats, beat_up 0.857; RECEIVABLES_OUTRUN flag |
| ADSK | 2026-11-24 | 20 | 4/4 beats, 6.37% avg surprise; RECEIVABLES_OUTRUN flag |
| VEEV | 2026-11-25 | 21 | 4/4 beats; avg abs move 9.1% |
| AZO | 2026-12-08 | 34 | 3/4 beats, beat_up 0.333 — rate NOT judgeable (only 3 measured beats) |
| CTAS | 2026-12-17 | 43 | 4/4 beats, 1.07% avg surprise — beats are rounding errors |
| PAYX | 2026-12-18 | 44 | 4/4 beats, avg move −1.4%; RECEIVABLES_OUTRUN flag |

This queue is the point of screening a whole reporting wave rather than a single week: when one of these dates comes within ~10 days, it enters as an already-screened candidate.

## Disclaimer

This is research output, not financial advice. Dated 2026-11-05. Every number a research scenario, not a guarantee.
