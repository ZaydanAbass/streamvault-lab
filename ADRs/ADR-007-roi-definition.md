# ADR-007: ROI is theatrical revenue against budget

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
The dataset only provides production budget and box office revenue.

## Decision
ROI is calculated as (Revenue - Budget) / Budget. A result of 4 means the film returned 4 times its budget in profit.

## Alternatives considered

### Alternative A: Absolute Profit
- **How it would work:** Look purely at the dollar amount of profit.
- **Why it is attractive:** It aligns with the $14M scale of the deal.
- **Why rejected:** It favors the biggest films (like Avengers) and says nothing about the efficiency of the investment.

## Consequences
- **What this buys:** A standardized metric to compare a $10M indie film against a $300M blockbuster.
- **What this costs:** Theatrical box office is not the same as licensing value. 
- **What it costs the client if I am wrong:** A film might have been a box-office hit but won't drive subscriptions for StreamVault. ROI is a proxy for audience demand, not a guarantee of streaming success.
- **What would make me revisit this:** The studio providing historical streaming performance data.

## What this survives
The formula is centralized. If we ever get streaming data, we only need to change it in one place.