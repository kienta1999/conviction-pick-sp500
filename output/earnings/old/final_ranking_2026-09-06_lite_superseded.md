# stock-pick-earnings 2026-09-06 — lite, the whole field (one agent, 5 searches, no panel, no verifier)

**Plan B only, and nothing is actionable this week.** Lite never recommends holding through a print — it has
no verifier, so checklist box 4 (date confirmed on the company's IR page) is ticked for every name by
construction. It also writes no ledger row and therefore **no `event_pred_*` pre-registration**: this run
makes no falsifiable call. Both are reasons to run the full `/stock-pick-earnings` on anything you would
actually trade.

**The calendar, not the screen, decided this run.** The nearest print in the field is CTAS on Sep 23 — 17
days out. The actionable window is ~10 days, so the **actionable set is zero** and all 13 names are
watchlist. That is a mid-quarter week working correctly, not a failed run. What this produces is a
pre-vetted queue: when these dates come inside 10 days, they enter already screened.

Screen: 502 → 13 (profitable 451 → US → growing 409 → leverage 292 → **reports ≤45d 58** → mktcap ≥$20B 52 →
record gate 47 → **beat→up rate >50% 31** → margin leader 14 → earnings quality 13). The reaction gate did
the most interesting work: it dropped **ADBE** (beats rose 12% of the time), **GE** (25%), **COST** (29%),
**MU**, **TER**, **MRSH** (38%), and **ACN, MMM, MCO, NKE, UAL, STLD, VLTO** (50%) — all names with intact
beat streaks that the market does not pay for.

Regime (reused from today's dip run): 10-year ~4.78%, near its highest since Nov 2023; a strong payrolls
print put September hike odds ~58% into the Sep 15-16 FOMC. Every date below sits *after* that meeting, so
the rate question resolves before any of these trades open.

## The disqualifier checklist, run mechanically

Box 4 — **date not confirmed on the IR page — is ticked for all 13.** Lite has no verifier; the dates below
come from the cached Yahoo calendar. (FAST is the one exception found incidentally: the company has
announced Oct 14, 6:00am CT.) The other five boxes, with numbers:

| ticker | 1: ran >15% in | 2: recent beat sold | 3: guide raised between qtrs | 5: move inside its own abs move | 6: consensus implies unshown accel |
|---|---|---|---|---|---|
| GS | clear (+1.1%) | clear (+9%, +2%) | clear | clear (20.5% avg beat vs 3.5% abs) | clear — but revenue decelerating (−4.7pp) |
| BAC | clear (−0.0%) | clear (+2%, +2%) | clear | clear (7.7% vs 2.5%) | clear |
| BNY | clear (+3.8%) | clear (+5%, +2%) | clear | clear (10.1% vs 3.0%) | clear |
| MS | clear (+1.9%) | **TICKED** — last print beat, stock −4% | clear | clear (19.1% vs 4.1%) | clear |
| KO | clear (+1.4%) | clear (+5%, +4%) | clear (raise came *at* Q2, not between) | clear (4.5% vs 2.9%) | clear |
| ISRG | clear (−1.9%) | **TICKED** — last print beat, stock −14% | clear | clear (15.7% vs 6.7%) | clear |
| WAB | clear (−4.1%) | clear (+10%, +3%) | clear (raise came at Q2) | **TICKED** (4.1% vs 5.2%) | clear |
| PM | clear (−2.9%) | clear (+3%, +7%) | **TICKED** — FY EPS *cut* to $8.36-8.51 | clear (7.1% vs 5.9%) | clear |
| CTAS | clear (−0.6%) | **TICKED** — a beat sold −5% | clear (FY27 guide came at Q4) | **TICKED** (1.1% vs 4.4%) | clear |
| VRT | clear (+1.9%) | **TICKED** — last print beat, stock −17% | clear (raise came at Q1) | clear (13.0% vs 9.6%) | clear |
| CME | clear (+6.4%) | clear (+5%, +0%) | clear | **TICKED** (1.4% vs 1.6%) | **TICKED** (revenue +0.8%, decel −4.8pp) |
| JNJ | clear (+7.6%) | **TICKED** — last print beat, stock −3% | clear | **TICKED** (1.0% vs 1.8%) | clear |
| FAST | clear (−2.4%) | **TICKED** — three of last four sold | clear | **TICKED** (0.11% vs 5.5%) | **TICKED** (decel −2.2pp) |

A ticked box is not argued with: it drops the name out of `buy`/`alt` regardless of how good the prose is.

## The ranking

| # | ticker | company | date | days | react | beat | guide | priced | fall | wtd | up-rate | avg abs move | fwdPE | bucket |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GS** | Goldman Sachs | 2026-10-13 | 37 | 9 | 9 | 8 | 7 | 7 | **8.20** | 88% (8) | 3.5% | 14.0 | buy |
| 2 | **BAC** | Bank of America | 2026-10-14 | 38 | 8 | 7 | 8 | 7 | 8 | **7.60** | 75% (8) | 2.5% | 11.8 | buy |
| 3 | **BNY** | BNY Mellon | 2026-10-15 | 39 | 9 | 7 | 7 | 6 | 7 | **7.40** | 88% (8) | 3.0% | 16.1 | buy |
| 4 | **MS** | Morgan Stanley | 2026-10-14 | 38 | 7 | 9 | 8 | 6 | 7 | **7.40** | 75% (8) | 4.1% | 16.0 | watch |
| 5 | **KO** | Coca-Cola | 2026-10-20 | 44 | 8 | 6 | 7 | 5 | 8 | **6.80** | 75% (8) | 2.9% | 25.0 | buy |
| 6 | **ISRG** | Intuitive Surgical | 2026-10-20 | 44 | 5 | 8 | 6 | 7 | 9 | **6.60** | 63% (8) | 6.7% | 30.4 | watch |
| 7 | **WAB** | Wabtec | 2026-10-21 | 45 | 5 | 6 | 7 | 7 | 7 | **6.20** | 57% (7) | 5.2% | 22.7 | watch |
| 8 | **PM** | Philip Morris | 2026-10-21 | 45 | 7 | 6 | 5 | 6 | 6 | **6.10** | 71% (7) | 5.9% | 19.9 | watch |
| 9 | **CTAS** | Cintas | 2026-09-23 | 17 | 7 | 4 | 7 | 5 | 8 | **6.10** | 75% (8) | 4.4% | 32.8 | watch |
| 10 | **VRT** | Vertiv | 2026-10-21 | 45 | 5 | 8 | 7 | **3** | 6 | **5.70** | 63% (8) | 9.6% | 30.8 | **avoid** |
| 11 | **CME** | CME Group | 2026-10-21 | 45 | 6 | 4 | 6 | 4 | 8 | **5.40** | 100% (6)* | 1.6% | 21.8 | watch |
| 12 | **JNJ** | Johnson & Johnson | 2026-10-13 | 37 | 4 | 4 | 6 | 4 | 8 | **4.80** | 57% (7) | 1.8% | 22.4 | watch |
| 13 | **FAST** | Fastenal | 2026-10-14 | 38 | 4 | 3 | 6 | 4 | 7 | **4.50** | 67% (6) | 5.5% | 35.4 | watch |

\* CME's 100% rests on 3 measured beats out of 6 prints — thin. Unproven, not vindicated.

## Why each one

1. **GS** — the best reaction record in the field and the tightest downside: beats rose 88% of the time over
   8 measured prints, average +3.0%, **worst reaction −2.0%**. Beats average +20.5% and are getting *larger*
   (surprise trend +11.4). IB revenue rose 24% in H1 to $61.4B and BofA's analysts expect all eight large
   banks to beat consensus. At 14.0× forward, none of that is an expensive assumption. The one blemish:
   revenue growth decelerated 4.7pp, so the beat is being made on mix, not on acceleration.
2. **BAC** — the cheapest name here at 11.8× with an 8-print record of small, reliably positive reactions
   (avg +1.3%, avg absolute 2.5%, worst −3.8%). It barely moves, which cuts both ways: the fallback is the
   best in the field, the payoff is thin.
3. **BNY** — 88% up-rate, worst reaction −2.0%, beats averaging +10%. Held below GS only because the sell
   side sees +1.5% upside to its mean target — the *stock*, not the record, is what's priced.
4. **MS** — the biggest beats in the field (+19.1% average) and a strong backdrop, but its most recent print
   was a beat the stock fell 4% on, and the surprise trend is *shrinking* (−6.6). Box 2 ticked, so it sits
   out of the buy bucket despite the score.
5. **KO** — the most boringly reliable reaction pattern on the board: last four prints +5%, +4%, +2%, +4%.
   Q2 delivered volume +5% and revenue +7% and the FY guide went up. The problem is that the raise already
   happened and 25× forward for a staple with +7.5% analyst upside is where the payoff goes to die.
6. **ISRG** — today's dip-run pick, and the two doctrines disagree in a useful way. As a *business* it's the
   best fallback here (score 9). As an *event* it is poor: 63% up-rate, average absolute move 6.7%, worst
   −14.1%, and the most recent print was a beat that fell 14%. Own it, don't trade its print.
7. **WAB** — raised FY26 to ~$12.5B revenue and $10.60-10.90 EPS, organic growth accelerating 2.3% → 8.5%,
   multiyear backlog >$30B (+42%). The fundamentals are the best story in the bottom half; the reaction
   record (57%, avg +0.4%) says the market doesn't pay for them.
8. **PM** — the only name whose forward number was *cut* between quarters: FY26 EPS to $8.36-8.51 on Zyn
   competition and FDA delays, with ZYN shipments up just 1.8%. A lower bar is easier to clear, but box 3 is
   ticked for the wrong reason — the guide came down because the business got harder.
9. **CTAS** — the first date on the calendar (Sep 23) and *not* the best name, which is the whole argument
   for screening a 45-day wave instead of a week. Record margins (51% gross), FY27 guided to $12.1-12.25B,
   but the beats average 1.09% — a company managing to the decimal — against a 4.4% typical move.
10. **VRT — AVOID, the trap fired.** Everything fundamental is excellent: backlog $12.45B (+80% YoY),
    FY26 guidance raised to $13.5-14.0B, beats averaging +13%. And the market's answer to the most recent
    beat was **−17%**, after a +64% YTD run, at 30.8× forward. That is the priced-in print by revealed
    behaviour, not by argument. `priced = 3` triggers the veto.
11. **CME** — a 1.6% average absolute move means there is almost nothing to win, its up-rate rests on three
    measured beats, revenue is flat (+0.8%) and decelerating, and it trades at its analyst mean target.
12. **JNJ** — moves 1.8% on a print, beats by 0.95%, sits at its mean target, and ran 7.6% into the window.
13. **FAST** — three of the last four prints were sold, beats average 0.11% (a rounding error) against a
    5.5% typical move, at 35.4× forward. The screen's reaction gate let it through on a 67% rate computed
    over six prints; the last four say otherwise.

## Deviations from the weighted score

- **BNY ranked above MS** (both 7.40): MS beats by far more, but BNY's reaction record is cleaner (88% vs
  75%, worst −2.0% vs −4.5%) and MS's most recent beat was sold. In an event trade the reaction record is
  the tradeable variable, so the tie breaks toward BNY.
- **CTAS at 9 despite being the nearest date.** Deliberate: the calendar is not a tiebreaker when two boxes
  are ticked.
- **VRT would rank 6th on raw score** and is nonetheless the only `avoid`. The veto is doing exactly what it
  exists for — refusing the best story in the field because the market has already paid for it.

**Buy (when their dates come inside 10 days):** GS, BAC, BNY, KO
**Watch:** MS, ISRG, WAB, PM, CTAS, CME, JNJ, FAST   **Avoid:** VRT
**Actionable today:** none.

## The Plan B trigger, for the four buys

Identical for each — no position before the print, ever, in lite:
enter only if **(a)** it beats on EPS *and* revenue, **(b)** the next-quarter guide is raised or set above
consensus (merely "in line" does not count), and **(c)** the first full session after the print **closes up**.
Entry on the session after that reaction session. Hold the drift **20-40 sessions**. The drift thesis is dead
the moment the stock closes back below its reaction-day close — that is an exit, not a dip to add to.

Dates to come back for: **GS Oct 13**, **BAC + MS Oct 14**, **BNY Oct 15**, **KO Oct 20**. Confirm each
against the company's IR page first — lite did not.

## Watchlist beyond the window

All 13 are watchlist this run; the table above is the queue, sorted by score rather than by date. The next
name to become actionable is CTAS on ~Sep 13 (10 days before its Sep 23 print), and it is a `watch`, not a buy.

## Sources

- Big-bank Q3 setup, IB revenue +24% H1 to $61.4B, BofA expecting eight beats — CNBC, Yahoo Finance,
  Benzinga, Proactive, Jul 2026
- Vertiv Q1/Q2 2026 backlog $12.45B (+80%), FY26 guide $13.5-14.0B, +64% YTD — Simply Wall St, Yahoo
  Finance, Techjack, Alphastreet, Apr-May 2026
- Coca-Cola Q2 2026 volume +5%, revenue +7%, FY guidance raised — KO investor release, FoodNavigator, Jul 28 2026
- Philip Morris FY26 EPS cut to $8.36-8.51, ZYN shipments +1.8% — PM 8-K, 2Firsts, ChartMill, Q2 2026
- Cintas FY27 guide $12.1-12.25B / EPS $5.36-5.50, Q4 organic +8.4%, 51% gross margin — Seeking Alpha,
  Motley Fool transcript, Jul 22 2026
- Wabtec FY26 raise (~$12.5B, EPS $10.60-10.90), organic 2.3% → 8.5%, multiyear backlog >$30B; Fastenal
  daily sales +14.7%, Q3 date Oct 14 — Investing.com, Seeking Alpha, Fastenal IR, Jul 2026
- Rates / FOMC / S&P level — CNBC and Yahoo Finance recaps, Sep 1-4 2026 (reused from today's dip run)

Reaction figures, beat records, `ret_21d` and the run-into-print flags come from `output/earnings/shortlist.csv`
(screen generated 2026-09-06 23:47). Every claim above traces to a row here or to that file — lite has no
dossier and no verifier, so this list is the audit trail.

**Not done in lite:** independent per-lens scoring (one head scored all five), IR-page date confirmation,
consensus EPS/revenue figures for the quarters being reported, options-implied moves, the next-quarter
consensus numbers the guides will be judged against, bear/base/bull scenarios, the EV gates, and the ledger
row with its pre-registered prediction. Ledger check: `picks/ledger.csv` contains **no earnings rows at all** —
this mode has never recorded a pick, so nothing is open and unclosed.

*Research output, not financial advice. 2026-09-06.*
