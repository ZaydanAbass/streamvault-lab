# ADR-012: Classify a bundle by the year its first film was released

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
A franchise can span decades. To run the "2000 Onward" analysis, we need a rule for when a bundle counts as "recent."

## Decision
A bundle is classified as "recent" if its earliest film was released in 2000 or later.

## Alternatives considered

### Alternative A: Use only the 2000+ films from a bundle
- **How it would work:** Chop the bundle in half and only analyze the modern films.
- **Why it is attractive:** It focuses purely on modern data.
- **Why rejected:** The studio sells the bundle as a whole. We cannot buy just the modern films.

## Consequences
- **What this buys:** A simple, testable rule that keeps the bundle intact.
- **What this costs:** A bundle that started in 1999 might be excluded from the modern list, even if it has recent sequels.
- **What it costs the client if I am wrong:** We might miss a strong franchise that straddles the year 2000.
- **What would make me revisit this:** If we find a huge franchise that is being wrongly excluded.