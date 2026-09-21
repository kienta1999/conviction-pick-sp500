# Momentum — Final Pick (single-pick mode)
**Run date:** 2026-09-21 · **Mode:** momentum (above 200d SMA + structural shortage doctrine)
**Screen:** `output/momentum/shortlist.json`, generated 2026-09-21 08:33:32 UTC — 50 candidates from 503 S&P 500 members, triaged to 11 for deep research (prices through 9/18 close)
**Panel:** 4 independent subagents, one per lens, dispatched sequentially · **Verification:** independent verifier subagent — all load-bearing figures confirmed, 3 labeling corrections applied, no trap veto on MU

---

## THE PICK: **MU — Micron Technology — $1,015.80 (9/18 close)**

**Tally:** single-pick weighted vote MU 6 (Lenses A, B, D) vs KLAC 2 (Lens C); each lens's ranked #1 matched its single pick, so no runner-up points. Borda #1 at 36/40. Doctrine adjudication: MU's explosive-return case is the strongest in the field — the shortage is physical (HBM needs ~3x the wafer area of standard DRAM), the booked demand is contractual, and the market still prices it as a legacy cyclical at 6.5x forward. No veto conflicts: all four lenses passed the disintermediation test, and the independent verifier independently passed the trap veto.

### Explosive-return thesis
Micron is the doctrine's canonical name: 2026–27 HBM supply is fully contracted, demand "far above" supply into 2028, and 16 strategic customer agreements carry **~$100B of minimum contracted revenue at floor prices through calendar 2030**, backed by ~$18B in customer cash deposits and ~$4B in letters of credit (~$22B total financial commitments). FQ3 FY2026 (Jun 24, 2026): revenue $41.46B (+346% YoY), non-GAAP EPS $25.11, GM ~84.6–84.9%; Q4 guide $50.0B ± $1B revenue, ~86% GM, $31.00 ± $1 EPS — a ~16% raise vs pre-guide consensus. HBM TAM: ~$35B (2025) → ~$100B (2028), possibly crossing $100B in FY2027. The re-rate engine: the market pays 6.5x forward for what it thinks is peak-cycle DRAM; the contracts turn it into a quasi-annuity with price FLOORS (margins targeted "well above" any past-cycle peak). Catalyst: earnings ~Sep 30 (9 days out) — see sizing halving below.

**Verifier corrections incorporated** (they strengthen the case): the "$22B floor-priced agreements" shorthand mislabeled the deposits — the real booked figure is ~$100B minimum contracted revenue; the contracts also carry a price CEILING (near Q2-2026 levels), so upside on covered volume is capped — the explosive case is a multiple re-rate, not unbounded ASP gains. "Demand >2x supply" is dossier-sourced, not independently confirmed; direction confirmed ("no line of sight" to supply catching demand).

**Trap veto: PASS.** Only three firms on earth make HBM commercially (Samsung, SK Hynix, Micron). No hyperscaler operates or has announced a DRAM/HBM fab — Amazon and Google are SIGNING multi-year supply agreements with Micron as locked-in buyers. The only substitute tech (HBF, Sandisk + SK hynix, spec released Aug 2026) is complementary inference-tier memory; samples H2 2026, integration targeted early 2027 — no threat to the training-memory franchise in 2–3 years. Genuine risks are ordinary cyclicality: margins at 84–86% are ASP-spike driven (DRAM ASPs +140% in 9M FY2026), HBM share is #3, and the SCA ceilings cap further ASP upside — all sizing/exit considerations, not vetoes.

### Scenario table (panel-research estimates; price = 9/18 close $1,015.80)
| case | prob | target | by | narrative |
|------|-----:|-------:|----|-----------|
| bear | 0.30 | $660 | 2027-H1 | Cycle turns: ASPs collapse from the +140% spike, HBM share stuck #3, price ceilings cap covered volume. |
| base | 0.50 | $1,422 | 2027-Q3 | Shortage persists through 2027; SCAs execute at floor prices; market partially re-rates from cyclical to contracted-revenue compounder. |
| bull | 0.20 | $1,828 | 2027-Q4 | HBM TAM hits ~$100B, ASPs hold, qualification wins shift share; 11–12x on forward earnings. |
| **EV** | | **$1,274.60** | | **+25.5% vs 9/18 close — clears the +15% actionable single-pick guardrail.** |

Market-implied case: 6.5x forward prices MU as peak-cycle DRAM — it prices the floor, not the contracts. The pick bets the market reprices the contracted floor over the next 12 months.

### Sizing (POLICY.md §1.1, adjustments in order)
- raw = (1,274.60 / 1,015.80 − 1) / (1 − 660 / 1,015.80) = 0.2548 / 0.3503 = **0.727**
- size = min(5%, 2.5 × 0.727) = **1.82%**
- **Earnings halving: next earnings ~2026-09-30, 9 days out → 0.91%** (independently confirmed by research; deterministic earnings cache was stale from the 9/18 endpoint timeout)
- Pilot halving (pilot regime) → **0.45%** of investable capital
- Per-pick cap 5% never binds; system cap 15% across all open system picks observed
- `size_pct` intentionally left empty in the ledger per policy

### Why not the runners-up
- **KLAC (Lens C's pick, Borda #2… actually Borda 4th at 26/40):** the best moat in the field (near-monopoly process control, $12.57B backlog +60% YoY), but at ~48x trailing the 2027 ramp is already paid for; the explosive-return math is weaker (EV ~+17%).
- **NVDA (Borda #2):** FY28 +70% supply-capped growth is real, but the doctrine's fatal trap — hyperscaler custom-ASIC in-sourcing of inference — is already in progress against Nvidia itself; two lenses docked it hard for exactly this.
- **SNDK (Borda #5):** the purest shortage vehicle ($93.9B floor-priced NBM book at >80% margins) at the worst entry timing — +1,650% in 12 months, −35% from the high, peak-cycle earnings.
- **FCX (Borda #6):** the only real structural commodity deficit, but fungible copper gives zero pricing power and the Grasberg restart is execution risk.
