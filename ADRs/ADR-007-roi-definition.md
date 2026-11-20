# ADR-007: ROI is worldwide revenue against production budget, in nominal dollars

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Possible. It favours big-gross titles and old, cheap films.

## Context

The data has `budget` and `revenue` only. All 112 films have both above zero, which I checked and did not assume.

## Decision

ROI is (revenue minus budget) divided by budget, using TMDb's figures as reported. A value of 4 means revenue was five times the budget.

## Alternatives considered

### Alternative A: inflation-adjusted ROI
- **How it would work:** convert each film's money to current dollars using an index.
- **Why it is attractive:** it answers Yaw's objection directly.
- **Why rejected:** it needs outside data the brief does not provide. It is my candidate improvement beyond the brief (deliverable 5).
- **What the recommendation looks like under it:** not computed, so I cannot say. The 1966 to 1980 films would drop most.

### Alternative B: absolute profit in dollars
- **Why it is attractive:** it shows scale, and Kwame has a fixed $14M.
- **Why rejected:** it favours the biggest films and says nothing about price.
- **What the recommendation looks like under it:** **TODO: not run.**

## Consequences

- **What this buys:** a figure that can be recomputed from the cache alone.
- **What this costs:** box office is not what the studio keeps, the budget excludes marketing, and old films have tiny nominal budgets, which inflates their ratios.
- **What it costs the client if I am wrong:** ROI may not predict licensing value, since StreamVault pays a licence fee, not production costs.
- **What would make me revisit this:** a licence-fee or profit field.

## What this survives

The formula is in one place (`add_flags`). `stage7_kpis.py` has an assert that stops the run if any budget is zero, so a rerun cannot divide by zero silently. A zero budget on a new title stops the run until the analyst decides how to treat it.
