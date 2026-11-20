# ADR-008: Lead with the median ROI, and show the mean beside it

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** High. The mean flips in one table.

## Context

The median and mean disagree in one table: all years, strict definition. Standalone mean is 9.48 against franchise 6.94, but the median favours franchise (4.53 against 4.00). The five highest ROIs are all from 1966 to 1980 (Star Wars 69.5, Jaws 66.2, The Godfather 39.8, The Good, the Bad and the Ugly 31.4, The Empire Strikes Back 28.9).

Two standalone films account for the flip. Jaws and The Good, the Bad and the Ugly together supply about 3.9 points of the standalone mean (Jaws about 2.6 and the other about 1.3). Without both, the standalone mean of the remaining 23 films is about 6.06, below the franchise 6.94. Removing The Good, the Bad and the Ugly alone does not undo the flip (the mean stays about 8.57).

## Decision

I lead with the median ROI and show the mean and the group size (n) beside it in every table.

## Alternatives considered

### Alternative A: lead with the mean
- **How it would work:** report average ROI per group.
- **Why it is attractive:** it reflects the big wins, which are what a licensing deal hopes for.
- **Why rejected:** two 1960s and 1970s films with tiny nominal budgets drive it, and the standalone groups have only 8 to 25 films.
- **What the recommendation looks like under it:** franchise still wins the mean in three of the four tables (all years loose 7.54 against 7.28, 2000 onward loose 4.41 against 3.90, 2000 onward strict 4.45 against 3.89). It flips to standalone only in all years strict. From 2000 onward, mean and median agree.

## Consequences

- **What this buys:** a figure that does not swing on one or two films.
- **What this costs:** it hides how large a typical big win can be.
- **What it costs the client if I am wrong:** if Kwame's strategy depends on landing a rare mega-hit, the mean is the better guide, and he would undervalue standalones.
- **What would make me revisit this:** inflation-adjusted ROI, or a larger standalone group.

## What this survives

On 500 titles the code computes both statistics, so the disagreement shows again. The conclusion needs re-reading on the rerun, not just re-running.
