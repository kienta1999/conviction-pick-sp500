---
name: stock-pick-dip-execute
description: Trade the latest dip rank10 basket (top 3, equal weight, META excluded) in IBKR account U27177562 through the free web Client Portal — Playwright drives the logged-in session for positions, quotes and orders; sizing and reconciliation reuse ranker-21d-sp500's execute_picks.py. Use when the user says /stock-pick-dip-execute, or asks to buy / rebalance / place the dip picks in IBKR.
---

# Dip basket → IBKR (no API)

Rebalances account **U27177562** toward `picks/picks_dip_<date>.csv`: POLICY
§6's **three slots**, filled from the newest dip `rank10` run in
`picks/ledger.csv` (the rows the panel wrote from `output/dip/final_ranking.md`)
and the account's current holdings. `/stock-pick-dip` never trades; this skill
is the only thing that does. Read **POLICY.md §6** first; execute it, never
re-argue it.

The mechanics are `ranker-21d-sp500`'s `ibkr-web-trade` skill, pointed at a
different account, picks file and reports dir. Its JS helpers are reused in
place, not copied:

```
RANKER=/home/talekien1710/personal_project/investment_strategy/ranker-21d-sp500
HERE=/home/talekien1710/personal_project/investment_strategy/conviction-pick-sp500
JS=$RANKER/.claude/skills/ibkr-web-trade
```

## Non-negotiables

1. **Never submit an order without the user's explicit go-ahead in chat.**
   Two gates: the plan (step 5) and the final confirmation (step 6b). Never
   per order.
2. The user types their own username/password. Never ask for, store, or type
   credentials.
3. **Account is `U27177562`.** `U26645119` is the ranker's — never trade it
   from here.
4. Cancel working orders **before** reading positions (live mode).
5. Never re-run placement "to be sure" — read the order book back (step 7).
6. Any error → stop and report. No improvising around a failed order.
7. `EXEC_REPORTS_DIR=$HERE/reports` on **every** `execute_picks.py` call.
   Without it the script writes into the ranker's `reports/` and overwrites
   its `live_book.json`.

## Steps

### 1. Parameters

| | default (POLICY.md §6) |
|---|---|
| picks | `scripts/ranking_to_picks.py --held reports/web_account.json [--drop …]` → `picks/picks_dip_<date>.csv` (built in step 4, after the capture) |
| mode | `live` (`whatif` = cost preview only, `print` = plan only) |
| leverage | `1.0` — cash-only, POLICY §2 |
| vol-target | `0.20` — de-risk overlay, can only scale below 1.0 |
| account | `U27177562` |

Run from `$HERE`. Confirm the newest dip `rank10` date in `picks/ledger.csv`
is the run the user means; stop if not.

`FLAGS="--broker web --mode <mode> --leverage 1.0 --vol-target 0.2 --picks $HERE/$PICKS"`
(`$PICKS` is set in step 4). Every script call below is
`EXEC_REPORTS_DIR=$HERE/reports uv run --project $RANKER python $RANKER/scripts/execute_picks.py $FLAGS …`
— call that `$EXEC`.

### 2. Portal session

`browser_navigate`
`https://portal.interactivebrokers.com/portal/?loginType=1&action=ACCT_MGMT_MAIN#/portfolio`
then `browser_evaluate`:

```js
async () => (await fetch('/portal.proxy/v1/portal/iserver/auth/status', {credentials:'include'})).json()
```

Not `authenticated: true` → ask the user to log in (they handle 2FA), wait for
them to say done, re-check.

### 3. Cancel working orders — live only

Read `$JS/cancel_orders.js`, replace `__ACCOUNT__` → `U27177562`, run with
`browser_evaluate`. `still_working` non-empty → stop, report the names.

### 4. Capture the account, then build the slots

Tickers the capture must quote = current holdings ∪ the latest rank10 names
(`awk -F, '$2=="dip"&&$3=="rank10"' picks/ledger.csv | tail -10 | cut -d, -f5`;
held names come from the portal itself). Read `$JS/capture_state.js`, replace
`__ACCOUNT__` and `__TICKERS__` (JS array of those), run with
`browser_evaluate` using `filename: "web_account.json"`, then:

```bash
mv web_account.json reports/web_account.json
python3 -c "import json;d=json.load(open('reports/web_account.json'));print(d['account'],d['equity'],len(d['positions']),'missing:',d['missing'],'working:',d['working_orders'])"
```

`account` must print `U27177562`. Report `equity`, `missing`, `working_orders`.
**Equity 0 or below ~$1,000 → stop**: the account is unfunded; nothing to do
until the user funds it.

Then the slot rule:

```bash
uv run python scripts/scorecard.py --mode dip --check | sed -n '/ALERTS/,$p'   # STOPPED / AT_TARGET / EXPIRED
uv run python scripts/ranking_to_picks.py --held reports/web_account.json --drop <held names in those alerts>
PICKS=$(ls -t picks/picks_dip_*.csv | head -1)
```

Show the user the three slots and the `sold:` line (held names being
outranked while still in the screen, or dropped). A held name absent from
the alerts and from `output/dip/shortlist.csv` is a recovered dip and is
kept on purpose — say so if it happens.

### 5. Plan

```bash
$EXEC
```

Prints the plan (buys/sells/holds) and writes `reports/web_orders.json` in
`whatif`/`live`. Show the table, the buy/sell totals and the picks file, then
**ask whether to continue**. `print` mode ends here. A price-sanity abort
(quote far from cached close) → stop, name the ticker.

Whole-share rounding on a ~$10k / 3-name account leaves cash idle; report the
realized gross, not the target.

### 6. Cost preview, then place

Read `$JS/place_orders.js`; substitute `__ACCOUNT__`, `__ORDERS__` (the
`orders` array from `reports/web_orders.json`, verbatim) and `__WHATIF__`.

**6a — `__WHATIF__ = true`**: IBKR returns commission + margin impact, places
nothing. Summarise. Mode `whatif` → done.

**6b — final confirmation**: show account `U27177562` (LIVE, real money),
order count, gross buy/sell notional, commission. Only a clear yes proceeds.

**6c — `__WHATIF__ = false`**: run again. Report per ticker `order_id` /
status / any `error`.

### 7. Record and report

```bash
$EXEC --record-book          # → $HERE/reports/live_book.json (live only)
```

Read `$JS/final_report.js`, replace `__ACCOUNT__`, run with `browser_evaluate`
using `filename: "web_final.json"`, then `mv web_final.json reports/` and
print NetLiq before/after, gross exposure (realized vs target), positions, and
`unfilled`. Market closed → DAY limits expire unfilled; say so; re-running the
skill reconciles what did not fill.

Finally: for each name **bought**, append the deployed `size_pct`
(= weight × gross, as % of the account) to its `rank10` row in
`picks/ledger.csv` so `scorecard.py` can police exposure. For each name
**sold**, append a `kind=close` row (`exit_reason=rebalance`, or `stop` /
`target` / `expired` per the alert; `exit_price` = fill). Commit `picks/` and
`reports/live_book.json`.

## Notes

- `reports/web_account.json` goes stale fast; live mode refuses it past 60
  minutes — re-run step 4, never edit the timestamp.
- The vol overlay reads the ranker's SPY cache (`$RANKER/data/market`); if the
  script warns it is >7 days old, run `uv run --project $RANKER python
  $RANKER/scripts/data.py` first.
- A bear-stop exit between runs (`scorecard.py --check` alert) is a manual
  sell in the portal plus a `kind=close` row; the slot stays cash until the
  next run.
