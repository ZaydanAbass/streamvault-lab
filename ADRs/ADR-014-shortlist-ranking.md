# ADR-014: Rank franchise bundles by their weakest film, and standalones by ROI

- **Status:** Proposed (drafted from your code; **TODO: confirm**)
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** High. It decides who is on the shortlist and which bundle is "strongest".

## Context

Kwame asked for his three strongest franchise targets and five strongest standalones, each with the reason it made the cut. One camp argues that StreamVault overpays for the weak middle entries of a franchise.

## Decision

- **Franchise:** among bundles with 2+ films, take the top 3 by the ROI of the bundle's weakest film (`worst_roi`). The bundle ROI is shown beside it.
- **Standalones:** among strict standalones, take the top 5 by ROI.
- Both are produced once for each window.

## Alternatives considered

### Alternative A: rank bundles by the bundle's combined ROI
- **Why it is attractive:** it is the figure the deal would earn overall.
- **Why rejected:** it hides a weak entry behind strong ones, which is exactly the team's worry.
- **What the recommendation looks like under it:** Lord of the Rings stays first (its 9.96 is the highest of the 23 bundles). **TODO: ranks 2 and 3 not checked.**

### Alternative B: rank standalones by profit or revenue
- **Why rejected:** it favours the biggest films, not the best value.
- **What the recommendation looks like under it:** **TODO: not run.**

## Consequences

- **What this buys:** a shortlist that survives the "weak middle entries" argument.
- **What this costs:** one bad film in an otherwise excellent bundle sinks it.
- **What it costs the client if I am wrong:** a strong bundle could be left off the list. Ranking standalones by ROI favours cheap films (see ADR-007).
- **What would make me revisit this:** the completeness check showing that the weakest film in a bundle belongs to a larger collection I only partly hold.

## Flag

The all-years standalone list includes Jaws, which TMDb places in a collection. Under ADR-005 it counts as a standalone only because one Jaws film is in my list. Check this in the memo.
