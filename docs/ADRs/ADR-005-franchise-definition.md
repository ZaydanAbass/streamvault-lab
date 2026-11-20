# ADR-005: Both windows are always shown; 2000 onward leads

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
About 37% of the films in our dataset (41 of 112) were released before 2000. Budgets and revenues are nominal dollars, meaning older films with tiny production budgets can mathematically produce massive ROI outliers (e.g., *Jaws* at 66x). Finance specifically distrusts pre-2000 box-office figures.

## Decision
I compute both "All Years" and "2000 Onward" and display them side by side. The main business recommendation leads with the **2000 Onward** window because it is less exposed to historical inflation and reporting anomalies.

## Alternatives considered

### Alternative A: All years as the main result
- **Why it is attractive:** It provides the largest possible sample size.
- **Why rejected:** It includes 1960s and 1970s films that dominate the top of the ROI table purely due to nominal inflation, weakening the defensibility of the recommendation.

## Consequences
- **What this buys:** A modern, defensible recommendation that Finance cannot dismiss due to old data.
- **What this costs:** The standalone group becomes smaller (only 12 films).
- **What it costs the client if I am wrong:** If the board values legacy catalog hits as much as modern ones, I have de-emphasized 41 films of evidence.
- **What would make me revisit this:** If the client provides an inflation-adjustment index.

## Does the recommendation change between windows?
**No.** The median franchise bundle wins in both windows (4.53x vs 4.00x all years; 4.08x vs 3.49x post-2000). 