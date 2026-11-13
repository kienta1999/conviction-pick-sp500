> Run by: Muse Spark — full panel

# Momentum triage — 2026-11-13

Screen reused: `output/momentum/shortlist_2026-11-12.json`, generated 2026-11-12 09:23:27 (<24h old, fresh per protocol Phase 0). 50 candidates. Prices below are the Nov 12 09:23 snapshots and are used as price_at_pick per the protocol.

## Missing-name check (from yesterday's note)

WST / EMR / WAB are again absent from today's shortlist. `scripts/why.py --mode momentum` on each (2026-11-13) returns the identical result as yesterday: dropped at **stage 1 profitable — netIncomeToCommon=NaN; profitMargins=NaN** (Yahoo cache glitch, unchanged). This is a data artifact, not a thesis change. MU, MSFT and LLY are present in today's shortlist.

## Triage table (ordered by composite)

| # | ticker | composite | KEEP/DROP | doctrine score | one-line reason |
|---|--------|-----------|-----------|----------------|-----------------|
| 1 | MU | 0.972 | KEEP | 10 | HBM/memory structural shortage, booked out multi-year; only ~3 firms can make HBM |
| 2 | ANET | 0.856 | KEEP | 9 | #1 AI datacenter switching; AI networking capacity in demand surge |
| 3 | LLY | 0.807 | KEEP | 9 | GLP-1 demand surge, supply-constrained; duopoly with NVO |
| 4 | ABNB | 0.807 | DROP | 2 | Travel platform; no shortage/backlog thesis |
| 5 | NEM | 0.791 | KEEP | 7 | Gold supply flat while price surges; #1 gold miner, fPE 11.9 |
| 6 | EOG | 0.753 | DROP | 4 | Strong growth but oil is well supplied; no backlog/shortage narrative (borderline) |
| 7 | V | 0.722 | DROP | 2 | Payments network compounder; no shortage thesis |
| 8 | MA | 0.716 | DROP | 2 | Same as V; no shortage thesis |
| 9 | COP | 0.697 | DROP | 3 | Oil producer; no structural shortage, commodity price-taker |
| 10 | CF | 0.689 | KEEP | 6 | Nitrogen fertilizer supply tight, pricing power; borderline cyclical |
| 11 | MSFT | 0.679 | KEEP | 5 | Azure AI capacity demand exceeds supply; the in-sourcer, not the supplier — borderline |
| 12 | NUE | 0.660 | KEEP | 5 | #1 US steelmaker; datacenter/grid/reshoring steel demand; borderline |
| 13 | MNST | 0.660 | DROP | 2 | Energy drinks; no shortage thesis |
| 14 | CBOE | 0.655 | DROP | 1 | Exchange; no shortage thesis |
| 15 | STT | 0.647 | DROP | 1 | Custody bank; no shortage thesis; LOW_CASH_CONVERSION flag |
| 16 | AAPL | 0.644 | DROP | 3 | iPhone cycle, no supply shortage; AI phone story unproven |
| 17 | BNY | 0.640 | DROP | 1 | Custody bank; no shortage thesis |
| 18 | HAS | 0.639 | DROP | 1 | Toys/games; no shortage thesis |
| 19 | BLK | 0.616 | DROP | 2 | Asset manager; no shortage thesis |
| 20 | OXY | 0.593 | DROP | 3 | Oil producer; no structural shortage |
| 21 | AMP | 0.587 | DROP | 1 | Wealth manager; no shortage thesis |
| 22 | UNP | 0.575 | KEEP | 5 | Rail capacity-constrained network, pricing power; UNP–NSC merger catalyst; borderline |
| 23 | VRTX | 0.545 | DROP | 4 | CF monopoly but steady demand, no shortage; INVENTORY_BUILD flag (borderline) |
| 24 | ISRG | 0.543 | KEEP | 7 | da Vinci installed-base growth + placement backlog; procedure demand surge |
| 25 | ABBV | 0.529 | DROP | 3 | Skyrizi/Rinvoq growth but no shortage; patent-cliff overhang |
| 26 | EBAY | 0.528 | DROP | 1 | Marketplace; no shortage thesis |
| 27 | EXPE | 0.519 | DROP | 2 | Travel; no shortage thesis |
| 28 | CDNS | 0.504 | KEEP | 8 | EDA duopoly with Synopsys; AI chip-design boom; customers cannot in-source EDA |
| 29 | PM | 0.498 | KEEP | 6 | ZYN nicotine-pouch demand surge, supply-constrained; category leader |
| 30 | EW | 0.497 | DROP | 2 | Heart valves; steady demand, no shortage |
| 31 | MCO | 0.496 | DROP | 1 | Ratings agency; no shortage thesis |
| 32 | PAYX | 0.472 | DROP | 1 | Payroll processor; no shortage thesis |
| 33 | IDXX | 0.470 | DROP | 2 | Vet diagnostics; steady compounder, no shortage |
| 34 | JPM | 0.467 | DROP | 2 | Mega-bank compounder; no shortage thesis |
| 35 | VRSN | 0.467 | DROP | 3 | .com registry monopoly, irreplaceable but no demand surge |
| 36 | CME | 0.464 | DROP | 1 | Derivatives exchange; no shortage thesis |
| 37 | AME | 0.455 | DROP | 3 | Industrial instruments; electrification exposure too diffuse |
| 38 | VEEV | 0.442 | DROP | 2 | Life-sciences cloud; no shortage thesis |
| 39 | JNJ | 0.436 | DROP | 2 | Diversified pharma/medtech; no shortage thesis |
| 40 | SPGI | 0.434 | DROP | 1 | Ratings/data; no shortage thesis |
| 41 | PH | 0.429 | KEEP | 6 | Aerospace hydraulics; commercial aerospace backlog + defense demand |
| 42 | FOXA | 0.427 | DROP | 1 | Media; no shortage thesis |
| 43 | CTAS | 0.426 | DROP | 2 | Uniform rental compounder; no shortage thesis |
| 44 | MRK | 0.410 | DROP | 2 | Keytruda LOE approaching; no shortage thesis |
| 45 | MO | 0.392 | DROP | 2 | Tobacco; no shortage thesis |
| 46 | FOX | 0.379 | DROP | 1 | Media; no shortage thesis |
| 47 | BRO | 0.372 | DROP | 1 | Insurance broker; no shortage thesis |
| 48 | NSC | 0.366 | DROP | 4 | Rail like UNP but UNP is the acquirer in the merger; keep one rail name only |
| 49 | ITW | 0.365 | DROP | 2 | Diversified industrial; no shortage thesis |
| 50 | VLTO | 0.360 | DROP | 2 | Water quality; steady, no shortage thesis |

## Kept (12)

MU, ANET, LLY, NEM, CF, MSFT, NUE, UNP, ISRG, CDNS, PM, PH.

## Borderline calls

- **EOG (dropped, composite #6):** highest-composite drop. Rev growth +28.6% and fPE 9.4 are attractive, but oil has no structural shortage or backlog — the doctrine needs a supply-constrained product, not just cheap energy earnings. RECEIVABLES_OUTRUN flag also noted.
- **VRTX (dropped):** genuine CF monopoly, but demand is steady, not surging, and there is no backlog signal; INVENTORY_BUILD flag.
- **NSC (dropped):** same rail thesis as UNP; UNP kept as the acquirer with the merger catalyst, one rail name is enough.
- **MSFT / NUE / UNP (kept, doctrine 5):** weakest keeps. MSFT is the in-sourcer rather than the supplier, NUE is a commodity cyclical, UNP is a slow compounder — all three are here to test whether the panel finds a shortage angle the screen alone does not show.

## Earnings-quality flags on kept names

- **CDNS:** RECEIVABLES_OUTRUN (recv_rev_divergence 0.242) + INVENTORY_BUILD (inv_rev_divergence 0.348). Research brief must carry the flag-explanation requirement.
- No other kept name carries a flag.
