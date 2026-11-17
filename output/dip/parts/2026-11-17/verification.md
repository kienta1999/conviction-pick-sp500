> Run by: Muse Spark (muse-spark-1.3) — full panel

# Phase 3.5 verification — dip — 2026-11-17

Scope: tentative top 3 from Borda (KLAC 39, AMAT 32, CSCO 31). Verified independently from primary sources and reputable financial press via web search on 2026-11-17. I read only `output/dip/research_dossier_2026-11-17.md` and `output/dip/shortlist_2026-11-16.json`; I did not open any panelist ballots or other runs' final files. Valuation figures (forward P/E, analyst mean target) are screen metrics from `shortlist_2026-11-16.json` (Yahoo-derived, generated 2026-11-16 16:09); I checked them for internal arithmetic consistency rather than against a second live source.

## Summary

| Claim | Verdict |
|---|---|
| KLAC — Q1 FY27 record: revenue $4.14B, +29% YoY, operating margin 46.1% | CONFIRMED |
| KLAC — moat ~50–55% process control, ~80%+ reticle inspection | CONFIRMED (third-party estimates; see caveat) |
| KLAC — Dec-quarter guide ~$4.7B revenue | CONFIRMED |
| KLAC — next print Jan 27–28, 2027 | UNVERIFIED (date not officially announced; estimates split) |
| KLAC — forward P/E ~21.5x; mean target implies ~+44% upside | CONFIRMED (screen arithmetic) |
| AMAT — Q4 FY26 record: revenue $10.41B, +53% YoY, adj. EPS $4.16 | CONFIRMED |
| AMAT — 2027 WFE call raised to >+30% | CONFIRMED |
| AMAT — dip cause: thin beat vs ~$4.20 whisper, +48% YTD into print | CONFIRMED |
| AMAT — 2025 WFE share loss 20.0% → 17.9% | CONFIRMED |
| AMAT — forward P/E ~15.1x; mean target implies ~+59% upside | CONFIRMED (screen arithmetic) |
| CSCO — Q1 FY27 record: revenue $18.52B, +24% YoY, non-GAAP EPS $1.40, +40% vs $1.33 consensus | CONFIRMED |
| CSCO — FY27 guidance raised to revenue $74.8–75.8B, non-GAAP EPS $5.47–5.53 | CONFIRMED |
| CSCO — AI infra target from hyperscalers raised to $9B (from $7.5B) | CONFIRMED |
| CSCO — selloff cause: gross margin fell 250bp to 65.6% on memory costs/hardware mix; product orders +21% vs +35% | CONFIRMED |
| CSCO — forward P/E ~16.1x; mean target implies ~+38% upside | CONFIRMED (screen arithmetic) |

No claim was CONTRADICTED. One claim is UNVERIFIED (KLAC next-print date).

---

## 1. KLAC — KLA Corporation

### 1a. Q1 FY27 record quarter: revenue $4.14B, +29% YoY, operating margin 46.1% — CONFIRMED

- KLA's Q1 FY27 earnings release (Oct 28, 2026, quarter ended Sep 30, 2026): revenue $4.136B, +29% YoY (+13% QoQ), non-GAAP operating margin 46.1% (up 240bp sequentially), non-GAAP diluted EPS $1.22, non-GAAP gross margin 62.7%. CEO on the call: "Revenue was another record at $4.14 billion" and "operating margins above 46% for the first time" in company history. Zacks (Oct 29, 2026) confirms revenue +28.9% YoY to $4.14B, EPS +38.6% YoY, beating the $1.18–1.19 consensus.
- Precision note: 46.1% is the **non-GAAP** operating margin; GAAP operating margin was 45.0%. The dossier states it without the non-GAAP qualifier — the figure itself is correct on the basis the company reports.

### 1b. Moat: ~50–55% share of process control, ~80%+ of reticle inspection — CONFIRMED (with caveat)

- DeepVal moat analysis (Nov 2026): KLA estimated at ~50–55% of process control, first by a wide margin, share roughly flat 50–55% FY2022–FY2026; Applied ~10–12%, ASML ~8–10% in the same table. DeepVal explicitly notes KLA does not publish its own share — these are third-party estimates.
- ravikant.dev sector scan (Jun 2, 2026): KLA "dominant supplier with ~50–60% share of wafer inspection, ~40–50% of metrology, and ~80%+ of reticle (photomask) inspection."
- Corroborating: Ploutos Aureus (Substack) puts KLA at ">56% of the worldwide process control market" and ">85%" in reticle inspection.
- Caveat: the percentages are estimates from third-party analysts, not company-disclosed figures, and the exact boundary of "process control" varies by source (50–56% range). The "quasi-monopoly" characterisation is a judgement, but the dominance the dossier asserts is supported.

### 1c. Catalyst: December-quarter guide ~$4.7B revenue — CONFIRMED

- KLA's Q1 FY27 release and call (Oct 28, 2026): December-quarter (Q2 FY27) guidance revenue $4.7B ± $200M, non-GAAP gross margin 62.5% ± 1%, non-GAAP diluted EPS $1.44 ± $0.11. Confirmed by Motley Fool transcript, Zacks, and the company's earnings deck.

### 1d. Next print Jan 27–28, 2027 — UNVERIFIED

- KLA has **not officially announced** the Q2 FY27 report date. Estimates split: TrendSpider, InTickers and Jason Wheel list Jan 28, 2027 (InTickers: Jan 27, 2027, "estimated… not officially announced"); TipRanks, MarketBeat and FMP-derived sources list Feb 4, 2027 (also "estimated… TBA (Not Confirmed)"). Prior-year Q2 was reported Jan 29, 2026, which supports a late-January date, but the Jan 27–28 window cannot be confirmed and the Feb 4 estimate is equally live. Treat the date as an estimate, not a confirmed fact.

### 1e. Valuation: forward P/E ~21.5x; analyst mean target implies ~+44% upside — CONFIRMED (screen arithmetic)

- Screen (`shortlist_2026-11-16.json`): forward P/E 21.457, target mean $219.62, screen price $152.32. Arithmetic: $219.62 / $152.32 − 1 = +44.2%, matching the screen's analyst_upside of 0.4418. These are the Yahoo consensus snapshot as of Nov 16, 2026; not re-verified against a second live source, and the target predates the Nov 16 SemiAnalysis capex-cut leg (KLAC closed $143.96 on Nov 16 per the dossier).

---

## 2. AMAT — Applied Materials

### 2a. Q4 FY26 record: revenue $10.41B, +53% YoY, adjusted EPS $4.16 — CONFIRMED

- Applied's Q4/FY26 earnings release (Nov 12, 2026; SEC 8-K Ex. 99.1): "Record quarterly revenue $10.41 billion, up 53 percent year over year"; GAAP EPS $3.40, record non-GAAP EPS $4.16, up 92% YoY; record FY26 revenue $34.45B (+21%), record FY26 non-GAAP EPS $12.89 (+37%). AP/Zacks summary: revenue beat ~$10.30B consensus, EPS beat ~$4.06 consensus. Motley Fool transcript confirms the same figures.

### 2b. 2027 WFE call raised to >+30% — CONFIRMED

- Earnings Whispers (Nov 12, 2026): management "issued its first explicit 2027 wafer fab equipment call of more than 30% growth, and expects Applied to outperform that market again." CEO Gary Dickerson on the call: "We expect 2027 to be another record year for the market and Applied" (per Reuters summary cited in the dossier). Q1 FY27 guidance: revenue ~$11.1B ± $500M, non-GAAP EPS ~$4.35 ± $0.20 — also confirmed in the release.

### 2c. Dip's cause: thin beat vs ~$4.20 whisper, +48% YTD run into the print — CONFIRMED

- Earnings Whispers (Nov 12, 2026): non-GAAP EPS $4.16 "topped the $4.06 consensus but missed the $4.20 Earnings Whisper number by 1.0%. Revenue of $10.41 billion beat the $10.30 billion consensus by 1.1%."
- ABC Money (Nov 13, 2026): shares "slid to $380.95 in the session around the print, a fall of roughly 3.6%"; "Applied Materials had already climbed roughly 48% year-to-date heading into the print" (per CoinCentral reporting). The market reaction (down on a beat) supports the dossier's "market did not buy the beat" reading; that reading itself is interpretation, the price action behind it is factual.

### 2d. Open question: 2025 WFE share loss from 20.0% to 17.9% — CONFIRMED

- EuropeSays (Oct 2026), citing proprietary data from The Information Network: "Applied Materials' global WFE market share declined from 20.0% in 2024 to 17.9% in 2025, representing a loss of 2.1 percentage points," while Lam, KLA and ASML gained; AMAT equipment revenue grew only 1.0% in H1 2026 vs double-digit growth at the three major competitors. The same table projects AMAT back to 20.4% in 2026.
- Corroborated by The Inference (Oct/Nov 2026): "Market data from The Information Network… puts Applied's reported WFE share at 20.0 percent in 2024 and 17.9 percent in 2025," and by Vantage Markets citing 24/7 Wall St ("lost 2.1 percentage points of global WFE share in 2025").
- Note: the figures rest on one research firm's (The Information Network's) proprietary estimates, not on company disclosure; the 2.1pp loss is consistently reported across the secondary sources.

### 2e. Valuation: forward P/E ~15.1x; analyst mean target implies ~+59% upside — CONFIRMED (screen arithmetic)

- Screen: forward P/E 15.057, target mean $588.61, screen price $370.50. Arithmetic: $588.61 / $370.50 − 1 = +58.9%, matching the screen's analyst_upside of 0.5887. Yahoo consensus snapshot as of Nov 16, 2026; not re-verified against a second live source. The dossier's own caveat stands: the target embeds the pre-SemiAnalysis-cut WFE outlook.

---

## 3. CSCO — Cisco Systems

### 3a. Q1 FY27 record: revenue $18.52B, +24% YoY, non-GAAP EPS $1.40, +40% vs $1.33 consensus — CONFIRMED

- Cisco Q1 FY27 results (reported after close Nov 12, 2026, quarter ended Oct 24, 2026; PR Newswire via Earnings Whispers): revenue $18.52B (reported as $18.517B), +24% YoY — "its strongest revenue growth in nearly 15 years" and a record; non-GAAP EPS $1.40, +40% YoY, vs $1.33 consensus; GAAP EPS $1.14, +58%. Finnhub lists Q1 FY2027 actual EPS $1.40, revenue $18.517B. Multiple sources (Benzinga/Longbridge, BigGo, Blockonomi) confirm the same figures.

### 3b. FY27 guidance raised to revenue $74.8–75.8B and non-GAAP EPS $5.47–5.53 — CONFIRMED

- Company release: FY27 revenue guidance raised to $74.8–75.8B (from $72.2–73.4B) and non-GAAP EPS to $5.47–5.53 (from $5.05–5.11). Confirmed by Earnings Whispers, Zacks, Motley Fool and the New Street research note (Nov 2026).

### 3c. AI infrastructure revenue target from hyperscalers raised to $9B (from $7.5B) — CONFIRMED

- Company release (Nov 12, 2026): "Raised expectation for AI infrastructure revenue from hyperscalers to $9B in FY27, more than double the total for FY26." Confirmed by AIAgentUpdate, BigGo, Blockonomi and Zacks. Note: $9B is an expectation/target, not booked revenue; FY26 booked was ~$4B.

### 3d. Selloff's cause: gross margin fell 250bp to 65.6% on memory costs and hardware mix; product order growth slowed to +21% from +35% — CONFIRMED

- Zacks (Nov 13, 2026): "Cisco's gross margin falls 250 basis points to 65.6% amid higher hardware exposure and rising memory costs"; "Product orders increased 21%, while networking orders advanced 28%."
- Motley Fool (Nov 14, 2026): "adjusted gross margin… dipped to 65.6% from the year-ago figure of 68.1%" due to "higher costs for memory components and a greater contribution from lower-margin AI networking products"; "Total product orders… rose 21% year over year… well under the 35% in the fourth quarter of 2026."
- AlphaSense earnings summary: non-GAAP gross margin 65.6%, down 250bp YoY; product gross margin 63.7%, down 350bp, "primarily due to hardware mix and higher memory costs"; product orders +21% YoY.
- Price action corroborates a selloff on the print: shares fell more than 6% the following day (PrimexBT/The Jo AI, Nov 13–14, 2026; Finnhub: Nov 13 close $95.64 vs Nov 12 close $102.01).

### 3e. Valuation: forward P/E ~16.1x; analyst mean target implies ~+38% upside — CONFIRMED (screen arithmetic)

- Screen: forward P/E 16.067, target mean $132.17, screen price $95.64. Arithmetic: $132.17 / $95.64 − 1 = +38.2%, matching the screen's analyst_upside of 0.3819. Yahoo consensus snapshot as of Nov 16, 2026; not re-verified against a second live source.

---

## Verifier's notes for the panel

1. **No contradictions found.** Every load-bearing earnings figure in the dossier matches the companies' own releases (KLA Oct 28, AMAT Nov 12, Cisco Nov 12, 2026) and reputable secondary coverage.
2. **One date to treat as an estimate:** KLAC's next print is not officially announced; the Jan 27–28, 2027 window the dossier uses is one of two live estimates (the other is Feb 4, 2027). Do not present it as a confirmed date.
3. **Non-GAAP qualifiers:** KLAC's 46.1% operating margin and Cisco's 65.6% gross margin are non-GAAP figures (GAAP: KLAC 45.0% operating margin; Cisco GAAP gross margin ~63.7%). The dossier's numbers are correct on the basis stated by the companies.
4. **Share figures are estimates, not disclosures:** neither KLA's ~50–55% process-control share nor AMAT's 20.0% → 17.9% WFE share comes from the companies themselves — both rest on third-party research (DeepVal/ravikant.dev; The Information Network). The AMAT share-loss figure is consistently reported across independent secondary sources; the KLAC range varies modestly by source (50–56%).
5. **Valuation targets are stale snapshots:** all three mean-target upsides are Nov 16 screen values and predate the Nov 16 SemiAnalysis-driven leg down; treat them as the screen's consensus, not a post-cut Street view.

Sources checked (2026-11-17): KLA Q1 FY27 release/call (AlphaStreet, Motley Fool, Zacks, securities.io, vlsi.kr, FMP via stockexpertai); AMAT Q4 FY26 release (SEC 8-K Ex. 99.1, Motley Fool transcript, AP, Earnings Whispers, ABC Money, SigmaThesis); Cisco Q1 FY27 release (PR Newswire via Earnings Whispers, Zacks, Motley Fool, AIAgentUpdate, BigGo, New Street, AlphaSense, Finnhub); KLA share (DeepVal, ravikant.dev, KoalaGains, Ploutos Aureus); AMAT share (EuropeSays/The Information Network, The Inference, Vantage Markets/24/7 Wall St); KLAC next-earnings estimates (TrendSpider, InTickers, TipRanks, MarketBeat, FMP).
