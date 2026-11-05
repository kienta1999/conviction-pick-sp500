> Run by: Muse Spark (unknown) — full panel

# Momentum triage — 2026-11-05

Screen: `shortlist_2026-11-05.json` (generated 2026-11-05 09:19:42 UTC, 50 candidates).
Shortlist built from cache after `fetch.py` stalled on Yahoo 401 "Invalid Crumb" errors
(killed at 401/503 tickers, ~09:22 UTC). Screen ran clean on the cache.

## Price verification (batch check, Yahoo chart API query2.finance.yahoo.com, 2026-11-05 ~09:25 UTC)

The screen's `price` column is a MIX of Nov 3 and Nov 4 closes — most names still
carry Nov 3 closes; a few (NEM, NUE, OXY) were refreshed to Nov 4 closes by the
partial fetch. Nov 4 was a sharp down day for memory/semis/energy and a strong up
day for mega-cap tech ex-semis. Verified Nov 4 closes below; the panel, the
dossier, scenario math and the ledger `price_at_pick` MUST use these, not the
screen's stale price column. Nothing here is invented — every close below was
returned by the Yahoo chart API.

| ticker | screen price | verified 2026-11-04 close | screen price is |
|---|---|---|---|
| MU | 855.10 | 795.23 | Nov 3 close (stale, −7.0% on Nov 4) |
| LLY | 1409.38 | 1417.99 | Nov 3 close (stale, +0.6%) |
| NEM | 118.11 | 118.11 | Nov 4 close ✓ fresh |
| EOG | 155.17 | 147.06 | Nov 3 close (stale, −5.2%) |
| ANET | 169.91 | 178.48 | Nov 3 close (stale, +5.0%) |
| V | 413.59 | 436.57 | Oct 30 close (stale 2 sessions) |
| MA | 647.18 | 672.68 | Nov 3 close (stale, +3.9%) |
| CF | 116.81 | 111.68 | Nov 3 close (stale, −4.4%) |
| APH | 84.19 | 79.01 | Nov 3 close (stale, −6.2%) |
| HAS | 117.97 | 121.58 | Nov 3 close (stale, +3.1%) |
| STT | 169.77 | 173.41 | Oct 30 close (stale 2 sessions) |
| MSFT | 520.99 | 555.80 | Nov 3 close (stale, +6.7%) |
| BLK | 1161.32 | 1224.37 | Nov 3 close (stale, +5.4%) |
| BNY | 149.31 | 152.72 | Nov 3 close (stale, +2.3%) |
| CBOE | 344.28 | 345.21 | Nov 3 close (stale, +0.3%) |
| NUE | 267.91 | 267.91 | Nov 4 close ✓ fresh |
| FANG | 192.34 | 182.88 | Nov 3 close (stale, −4.9%) |
| AAPL | 331.90 | 349.51 | Nov 3 close (stale, +5.3%) |
| DVN | 47.62 | 44.12 | Nov 3 close (stale, −7.4%) |
| AMP | 504.88 | 527.41 | Nov 3 close (stale, +4.5%) |
| OXY | 57.33 | 57.33 | Nov 4 close ✓ fresh |
| COP | 144.40 | 136.94 | Nov 3 close (stale, −5.2%) |
| NVDA (dropped by screen) | — | 200.13 | Nov 4 close; fell 213.66 → 200.13 since Oct 29 |
| AVGO (dropped by screen) | — | 325.48 | Nov 4 close; fell 345.00 → 325.48 since Oct 29 |

Screen-drop notes (from `drops_2026-11-05.csv`, verified against the closes above):
NVDA dropped at stage 5 (below 200d SMA, dist_sma200 −2.08%) — the drop is real,
not a data artifact: NVDA closed Nov 4 at 200.13, down every session since Oct 29.
AVGO, AMAT, LRCX, KLAC also dropped below their 200d SMAs on the same semi
pullback. PLTR dropped at stage 7 (forwardPE 69.22 > 60). GE dropped at stage 1
(no usable income data). The screen was NOT overridden: no dropped name is
researched or ranked.

Kept: 13 names. Dropped: 37.

## Triage table (ordered by composite)

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|---|---|---|---|---|
| 1 | MU | 0.966 | KEEP | 10 | HBM/memory structural shortage archetype; op margin 80.7%, rev +143.5%; fell 7% Nov 4 — the cycle question is the thesis |
| 2 | LLY | 0.818 | KEEP | 9 | GLP-1 demand far exceeds supply; #1 tirzepatide franchise |
| 3 | NEM | 0.813 | KEEP | 6 | Gold price surge play, not a supply shortage; margin 50%, +9.9% Nov 4 |
| 4 | EOG | 0.741 | DROP | 4 | Shale E&P price-taker; no structural shortage; fell 5.2% Nov 4 |
| 5 | ANET | 0.733 | KEEP | 9 | AI Ethernet switching #1; hyperscaler capex surge; +5.0% Nov 4 |
| 6 | V | 0.727 | DROP | 2 | Payments duopoly, high composite but zero shortage angle |
| 7 | MA | 0.716 | DROP | 2 | Same as V — no shortage angle despite high composite |
| 8 | CF | 0.709 | KEEP | 5 | Nitrogen fertilizer tightness is cyclical, not structural — borderline keep |
| 9 | APH | 0.688 | KEEP | 9 | AI datacenter interconnect #1; rev +51%; fell 6.2% Nov 4 |
| 10 | HAS | 0.677 | DROP | 1 | Toys/games; no shortage thesis |
| 11 | STT | 0.670 | DROP | 1 | Custody bank; no shortage thesis (LOW_CASH_CONVERSION flag moot) |
| 12 | MSFT | 0.666 | DROP | 3 | Hyperscaler = the in-sourcer in the trap; Azure demand is the customer side, not a supplier shortage |
| 13 | BLK | 0.665 | DROP | 1 | Asset manager; no shortage thesis |
| 14 | BNY | 0.659 | DROP | 1 | Custody bank; no shortage thesis |
| 15 | CBOE | 0.654 | DROP | 2 | Exchange; vol-driven, no shortage |
| 16 | NUE | 0.652 | KEEP | 6 | #1 US steel; datacenter/grid/reshoring steel demand; cyclical — borderline keep |
| 17 | FANG | 0.642 | KEEP | 5 | Best-in-class shale; kept as the single energy name on supply-discipline/oil-tightness — borderline |
| 18 | AAPL | 0.623 | DROP | 2 | No shortage angle; +5.3% Nov 4 is a relief move, not a thesis |
| 19 | DVN | 0.622 | DROP | 4 | E&P duplicate of FANG theme; fell 7.4% Nov 4 |
| 20 | AMP | 0.608 | DROP | 1 | Wealth manager; no shortage thesis |
| 21 | OXY | 0.608 | DROP | 4 | E&P duplicate of FANG theme; fell 10.4% over the screen window |
| 22 | COP | 0.579 | DROP | 4 | E&P duplicate of FANG theme; fell 5.2% Nov 4 |
| 23 | EBAY | 0.573 | DROP | 2 | Marketplace; no shortage thesis |
| 24 | UNP | 0.573 | DROP | 3 | Rail; no shortage thesis |
| 25 | WST | 0.567 | KEEP | 7 | Pharma packaging/components; GLP-1 vial/stopper demand surge; #1; RECEIVABLES_OUTRUN flag to explain |
| 26 | EXPE | 0.565 | DROP | 1 | Travel platform; no shortage thesis |
| 27 | ABNB | 0.558 | DROP | 1 | Travel platform; no shortage thesis |
| 28 | ISRG | 0.552 | KEEP | 7 | da Vinci installed-base lock-in + procedure growth; irreplaceable; ret12m −18% is the open question |
| 29 | CSCO | 0.547 | KEEP | 6 | AI networking order backlog + Splunk; legacy drag; INVENTORY_BUILD flag to explain — borderline |
| 30 | FAST | 0.538 | DROP | 2 | Industrial distribution; no shortage thesis |
| 31 | ABBV | 0.532 | DROP | 3 | Pharma; no structural shortage |
| 32 | IDXX | 0.520 | DROP | 3 | Vet diagnostics compounder; no shortage thesis |
| 33 | VRSN | 0.507 | DROP | 4 | .com registry monopoly is irreplaceable but there is no demand surge or shortage — borderline drop |
| 34 | PM | 0.505 | DROP | 2 | Tobacco/RRP; no shortage thesis |
| 35 | MRK | 0.505 | DROP | 3 | Keytruda-led pharma; no shortage thesis |
| 36 | VRTX | 0.497 | DROP | 3 | CF franchise; no shortage thesis |
| 37 | RL | 0.492 | DROP | 1 | Luxury; no shortage thesis |
| 38 | JPM | 0.491 | DROP | 1 | Bank; no shortage thesis |
| 39 | AMGN | 0.486 | DROP | 3 | Biotech; no shortage thesis |
| 40 | CME | 0.484 | DROP | 2 | Derivatives exchange; no shortage thesis |
| 41 | AMZN | 0.471 | DROP | 3 | Hyperscaler = the in-sourcer; AWS demand is the customer side of the trap |
| 42 | PAYX | 0.461 | DROP | 1 | Payroll; no shortage thesis |
| 43 | JNJ | 0.452 | DROP | 3 | Diversified pharma/medtech; no shortage thesis |
| 44 | VEEV | 0.449 | DROP | 3 | Life-sciences software; no shortage thesis |
| 45 | CSX | 0.446 | DROP | 3 | Rail; no shortage thesis |
| 46 | EW | 0.439 | DROP | 4 | TAVR #1 with structural heart growth, but no supply shortage — borderline drop |
| 47 | CTAS | 0.434 | DROP | 2 | Uniforms/facility services; no shortage thesis |
| 48 | AME | 0.426 | KEEP | 5 | AMETEK niche-#1 instruments; aerospace/defense backlog angle — borderline keep |
| 49 | SPGI | 0.420 | DROP | 1 | Ratings/data; no shortage thesis |
| 50 | ROK | 0.409 | KEEP | 6 | Rockwell Automation #1 industrial automation; reshoring/factory-automation backlog — borderline keep |

## Borderline flags

- CF, NUE, FANG, CSCO, AME, ROK are borderline keeps — weak-to-moderate shortage
  narratives; the panel should be ready to rank them low or drop them.
- VRSN and EW are borderline drops — genuine moat/growth but no shortage; the
  panel never sees them, which is the triage risk to note.
- MU is the #1 composite and the doctrine archetype, but its 7% Nov 4 fall and
  the whole semi complex breaking below 200d SMAs (NVDA, AVGO, AMAT, LRCX, KLAC
  all dropped by the screen) is the central question for the panel: shortage
  still intact, or cycle turning?
- High-composite names dropped despite strong screens: V, MA (payments
  duopoly, no shortage), MSFT/AMZN (hyperscalers — the in-sourcing side of the
  trap, not suppliers), STT/BLK/BNY/JPM (financials, no shortage).

## Research batches

- Batch 1: MU, ANET, APH (AI infrastructure)
- Batch 2: LLY, ISRG, WST (healthcare)
- Batch 3: NEM, NUE, CF, FANG (materials/energy)
- Batch 4: CSCO, ROK, AME (industrials/networking)
