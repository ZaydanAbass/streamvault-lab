# ADR-006: Lead with the 2000-onward window

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
About 37% of the films were released before 2000. Older films have distorted box-office reporting and tiny nominal budgets, which artificially inflates their ROI. 

## Decision
I compute both "All Years" and "2000 Onward" and lead the recommendation with 2000 Onward, as it is less exposed to historical inflation.

## Alternatives considered

### Alternative A: Use All Years as the main result
- **How it would work:** Rely on the full 112-film dataset.
- **Why it is attractive:** It provides a larger sample size.
- **Why rejected:** It includes 1960s/70s films that dominate the top ROI list purely due to inflation, weakening the reliability of the recommendation.

## Consequences
- **What this buys:** A modern, defensible recommendation that Finance cannot dismiss due to old data.
- **What this costs:** The standalone group becomes smaller (only 12 films).
- **What it costs the client if I am wrong:** If the board values legacy catalog hits as much as modern ones, I have de-emphasized 41 films of evidence.
- **What would make me revisit this:** If we acquire an inflation-adjustment index.

## What this survives
The script runs both windows automatically. However, the cutoff year (2000) is hardcoded and should be moved to a configuration file before next year.
