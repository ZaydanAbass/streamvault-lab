# ADR-008: Use median ROI, not average ROI, for the headline

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
Average ROI is heavily skewed by a few massive outliers (like *Star Wars*), which makes standalones look artificially strong.

## Decision
I report the median ROI because it represents the "typical" film and is not skewed by one or two mega-hits.

## Alternatives considered

### Alternative A: Lead with the Mean (Average)
- **How it would work:** Report the mathematical average.
- **Why it is attractive:** It reflects the potential upside if we land a massive hit.
- **Why rejected:** Two 1970s films distort the standalone average. If we remove *Jaws* and *The Good, the Bad and the Ugly*, the standalone average drops below the franchise average.

## Consequences
- **What this buys:** A stable, resilient recommendation that doesn't swing on one or two films.
- **What this costs:** It hides the scale of a potential mega-hit.
- **What it costs the client if I am wrong:** If the strategy is to swing for the fences on rare hits rather than buy safe bundles, the average is the better guide.
- **What would make me revisit this:** If the data is inflation-adjusted.

## What this survives
The code outputs both median and mean, so Adjoa can see if they diverge again next year.