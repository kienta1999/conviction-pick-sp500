# Final Ranking — Momentum Mode — 2026-10-01

**Consensus top 3 (5-run window):** MU, LRCX, SNDK — computed by `scripts/consensus.py --mode momentum --asof 2026-10-01 --write` (see `consensus_2026-10-01.md`).

## Today's Borda tally (rank1=10 pts … rank10=1; tie-break: #1 votes, then avg placement)

| # | ticker | Borda | #1 votes | ballots top-10 | screen composite |
|---|---|---|---|---|---|
| 1 | MU | 37 | 2 | 4/4 | 0.916 |
| 2 | KEYS | 32 | 1 | 4/4 | 0.619 |
| 3 | SNDK | 28 | 1 | 4/4 | 0.938 |
| 4 | LRCX | 25 | 0 | 4/4 | 0.706 |
| 5 | APH | 24 | 0 | 4/4 | 0.666 |
| 6 | AMAT | 22 | 0 | 4/4 | 0.657 |
| 7 | FCX | 21 | 0 | 4/4 | 0.316 |
| 8 | LLY | 12 | 0 | 4/4 | 0.808 |
| 9 | ANET | 8 | 0 | 4/4 | 0.788 |
| 10 | CAT | 7 | 0 | 3/4 | 0.592 |
| — | AME | 4 | 0 | 1/4 | 0.393 |
| — | CSCO | 0 | 0 | 0/4 | 0.536 |

## Ballots

- **A (supply-chain):** MU, APH, SNDK, KEYS, FCX, AMAT, LRCX, ANET, CAT, LLY — left out CSCO, AME
- **B (growth/momentum):** SNDK, MU, APH, KEYS, LRCX, AMAT, LLY, FCX, CAT, ANET — left out CSCO, AME
- **C (quality/moat):** MU, LRCX, KEYS, AMAT, LLY, FCX, AME, APH, ANET, SNDK — left out CSCO, CAT
- **D (contrarian):** KEYS, SNDK, MU, FCX, LRCX, AMAT, APH, CAT, ANET, LLY — left out CSCO, AME

**Unanimous in all four top-10s:** MU, KEYS, SNDK, LRCX, APH, AMAT, FCX, LLY, ANET. CSCO appeared in zero.

## Overlap vs 2026-09-30 Borda top 10

9/30: MU, LRCX, AMAT, SNDK, APH, FCX, NVDA, MSFT, CAT, LLY. Today's top 10 keeps **8/10** (MU, LRCX, AMAT, SNDK, APH, FCX, CAT, LLY). New: KEYS, ANET. Out: NVDA, MSFT — both fell out of today's deterministic screen entirely, so no panelist could rank them.

## Verifier note

Phase 3.5 verified the top-3 headline claims (MU $150B RPO / $12.3B deposits / FQ1 guide; KEYS record backlog / supply-constrained AI demand; SNDK $42B NBM contracts / 2026 sold out / NAND price path): **10/10 CONFIRMED**, 0 contradicted. Two non-blocking caveats: KEYS ~$2.8B backlog figure dates to Q1 FY26 coverage (Q3 record confirmed, amount undisclosed); MU consensus EPS base varies by source (~$35.07 vs ~$36.0–36.1), direction above consensus unambiguous.

---

*Research output, not financial advice. Ballot files: parts/2026-10-01/ballot_{A1,B1,C1,D1}.md.*
