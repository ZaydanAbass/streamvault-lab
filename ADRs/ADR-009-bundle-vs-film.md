# ADR-009: Analyze bundles as a whole unit

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
Kwame is buying franchises as complete bundles, not individual films. A franchise with one great film and several weak ones can look fine film-by-film but be a poor purchase.

## Decision
I compute both a film-level table and a bundle-level table. The bundle table combines the total revenue and budget of all films in the collection.

## Alternatives considered

### Alternative A: Per-film only
- **How it would work:** One row per film.
- **Why it is attractive:** It provides larger sample sizes.
- **Why rejected:** It cannot test the "weak middle entries" argument, which is the board's biggest fear.

## Consequences
- **What this buys:** A result that matches the actual purchase unit.
- **What this costs:** Fewer data points (only 23 bundles).
- **What it costs the client if I am wrong:** A bundle's ROI is weighted by budget, so a massive-budget flop could drag down the bundle's score. 
- **What would make me revisit this:** Finding out a bundle in our list is missing films that the studio is actually including.