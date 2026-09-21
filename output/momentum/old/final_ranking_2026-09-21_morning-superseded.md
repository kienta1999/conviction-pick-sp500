# Momentum — Final Ranked Top 10
**Run date:** 2026-09-21 · **Mode:** momentum (above 200d SMA + structural shortage doctrine) · **N = 10, R = 1**
**Screen:** `output/momentum/shortlist.json`, generated 2026-09-21 08:33:32 UTC — 50 candidates from 503 S&P 500 members, triaged to 11 for deep research (prices through 9/18 close)
**Panel:** 4 independent subagents, one per lens, dispatched sequentially · **Verification:** independent verifier subagent — all load-bearing figures confirmed, 3 labeling corrections applied (see §Verification), no trap veto on MU

**Borda tally (10 pts for #1 → 1 pt for #10; excluded name = 0):**
| Borda | Ticker | A | B | C | D | total/40 |
|------:|--------|---|---|---|---|---------|
| 1 | MU | 10 | 10 | 6 | 10 | 36 |
| 2 | NVDA | 7 | 9 | 7 | 9 | 32 |
| 3 | AMAT | 6 | 8 | 9 | 4 | 27 |
| 4 | KLAC | 5 | 5 | 10 | 6 | 26 |
| 5 | SNDK | 9 | 4 | 1 | 7 | 21 |
| 6 | FCX | 8 | 0 | 4 | 8 | 20 |
| 7 | ANET | 4 | 7 | 3 | 1 | 15 |
| 8 | VRTX | 0 | 3 | 8 | 3 | 14 |
| 9 | EMR | 2 | 1 | 5 | 5 | 13 |
| 10 | APH | 3 | 6 | 0 | 2 | 11 |
| — | AME | 1 | 2 | 2 | 0 | 5 (excluded from top 10) |

Lens A = supply-chain/shortage, B = growth/momentum, C = quality/moat/irreplaceability, D = contrarian/risk/valuation. Lens B excluded FCX, Lens C excluded APH, Lens A excluded VRTX — genuine independent ballots, 0 points given.

---

## Ranked scenarios (top 3)

Scenario numbers are panel-research estimates (not measurements). Prices are the 9/18/2026 closes. Probabilities sum to 1.0.

### 1. MU — Micron Technology — $1,015.80 (Borda 36/40; 3 of 4 lenses' single pick)
One-line thesis: the doctrine's canonical name — 2026–27 HBM supply fully contracted with 16 strategic customer agreements carrying ~$100B of minimum contracted revenue at floor prices through 2030 (~$18B cash deposits + ~$4B letters of credit), priced at 6.5x forward as a legacy cyclical. Verifier corrections applied: the "$22B" figure is customer deposits/commitments, NOT the contracted supply value (the real booked figure is the ~$100B); "demand >2x supply" is dossier-sourced, not independently confirmed (direction confirmed: "no line of sight" to supply catching demand). CEO quote (FQ3 call, Jun 24, 2026): "We currently do not have line of sight as to when memory supply will be able to catch up with demand."

| case | prob | target | by | narrative |
|------|-----:|-------:|----|-----------|
| bear | 0.30 | $660 | 2027-H1 | Memory cycle turns: ASPs collapse from the +140% DRAM spike, HBM share stuck at #3 behind SK Hynix/Samsung, SCA price ceilings cap the upside on covered volume. |
| base | 0.50 | $1,422 | 2027-Q3 | Shortage persists through 2027; SCAs execute at floor prices, margins hold, market partially re-rates from cyclical to contracted-revenue compounder. |
| bull | 0.20 | $1,828 | 2027-Q4 | HBM TAM runs to ~$100B, ASPs hold at spike levels, qualification wins shift share; 11–12x on forward earnings. |
| **EV** | | **$1,274.60 (+25.5%)** | | Market-implied case: at 6.5x forward, the market prices MU as peak-cycle DRAM — i.e., it prices the floor, not the contracts. |

### 2. NVDA — Nvidia — $222.27 (Borda 32/40)
One-line thesis: Q2 FY2027 $96.22B (+106% YoY) with the first-ever FY2028 guide at ~70% growth, explicitly supply-constrained — "Even though our demand is much greater than 70%, our supply allows us to confidently deliver 70%." Verifier correction: the "$279B future supply-chain commitments" figure is NVIDIA's own BUY-side purchase obligations (mostly memory procurement), not a customer order backlog — the signal (demand confidence) stands, the label was wrong. Trap flag: hyperscaler custom-ASIC in-sourcing of inference is already in progress — the doctrine's named disintermediation threat, live against this name.

| case | prob | target | by | narrative |
|------|-----:|-------:|----|-----------|
| bear | 0.30 | $160 | 2027-H1 | AI capex pause + ASIC bypass erodes pricing power; the supply-constraint premium evaporates. |
| base | 0.50 | $280 | 2027-Q3 | FY28 70% supply-capped growth delivers; CUDA lock-in holds the datacenter franchise. |
| bull | 0.20 | $360 | 2027-Q4 | "Demand doubling" forces faster supply unlock; rack-scale systems re-accelerate share. |
| **EV** | | **$260.00 (+17.0%)** | | Market-implied case: 14.2x forward for a 70% grower prices partial ASIC-cannibalization already. |

### 3. AMAT — Applied Materials — $444.57 (Borda 27/40)
One-line thesis: world's #1 WFE supplier with record FQ3 FY2026 revenue $9.12B (+25% YoY) into a +51% YoY FQ4 guide ($10.25B ±$0.5B), WFE outlook raised twice to >30%. Verifier correction: the "eight-quarter backlog" is rolling eight-quarter customer demand-FORECAST visibility, not a contractual booked backlog like Micron's SCAs. Trap flag (Lens B/D): the stock falls on double beats and FCF collapsed to ~$210M — the market may have already priced the extension.

| case | prob | target | by | narrative |
|------|-----:|-------:|----|-----------|
| bear | 0.30 | $320 | 2027-H1 | WFE digestion year; China/tariff overhang; the priced-in extension unwinds. |
| base | 0.50 | $560 | 2027-Q3 | FQ4 guide and 2027 ramp execute; doubling-output-by-2028 plan tracks. |
| bull | 0.20 | $720 | 2027-Q4 | AI fab supercycle runs past 2028; equipment scarcity mirrors the memory shortage. |
| **EV** | | **$520.00 (+17.0%)** | | Market-implied case: ~24x forward prices flawless 2027 execution; little room for a miss. |

### 4–10 — one-line theses
- **4. KLAC $176.99 (26/40)** — near-monopoly process control (56–58% share), record $12.57B backlog +60% YoY; fabs cannot in-source inspection, but the multiple (~48x trailing) already pays for the 2027 ramp. Lens C's single pick.
- **5. SNDK $1,791.82 (21/40)** — $93.9B floor-priced NBM book at >80% margins on a genuine NAND shortage; but +1,650% in 12 months, −35% from the high, peak-cycle earnings at 6.8x forward — the purest shortage vehicle at the worst entry timing.
- **6. FCX $71.54 (20/40)** — the one real structural commodity deficit (600kt copper gap, mine supply's first decline since 2017, 10+ year mine timelines); but a fungible commodity with zero pricing power vs the screen price, Grasberg restart execution risk.
- **7. ANET $199.39 (15/40)** — purchase commitments tripled to $9.7B, third FY raise to $12.6B (~40% growth); but Nvidia now holds the #1 datacenter-Ethernet slot and bundles networking with the GPUs — disintermediation is in motion.
- **8. VRTX $508.34 (14/40)** — virtual CF monopoly (patents to ~2040), 10/10 moat; but no shortage thesis — this is a pipeline-readout bet (Alyftrek/Casgevy/Journavx), momentum cooling.
- **9. EMR $149.92 (13/40)** — $8.2B backlog, automation levered to power/AI capex; but 1.0 book-to-bill says the backlog engine is decelerating — a compounder, not momentum.
- **10. APH $77.55 (11/40)** — record $10.7B orders, 1.23x book-to-bill, AI datacom quadrupled in two years; but #2 in a commoditizable connector market, 43% AI-exposed sales at 23.7x forward.

---

## Verification summary
Independent verifier re-tallied Borda (matches exactly) and confirmed every load-bearing number from dated primary sources. **Three labeling corrections applied** (they do not weaken any thesis; none changes a rank): (1) MU's "$22B" is customer deposits/commitments (~$18B cash + ~$4B LC) — the agreements' minimum contracted revenue value is ~$100B at floor prices; (2) NVDA's $279B is NVIDIA's own buy-side purchase obligations, not customer backlog; (3) AMAT's "eight-quarter backlog" is rolling eight-quarter customer forecast visibility. **Trap veto on MU: PASS** — no hyperscaler operates or has announced a DRAM/HBM fab; Amazon/Google are signing multi-year supply agreements with Micron as locked-in buyers; the only substitute tech (HBF, Sandisk + SK hynix) is complementary inference-tier memory, not a threat to the training-memory franchise in 2–3 years. Genuine MU risks are ordinary cyclicality (ASP-driven margins at 84–86%) and HBM #3 share — a sizing/exit question, not a veto. Full writeup: `output/momentum/parts/2026-09-21/verification.md`.
