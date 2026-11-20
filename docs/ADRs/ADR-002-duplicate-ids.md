# ADR-002: Report API 404s as unverified rather than assuming they don't exist

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
Five valid-looking IDs (e.g., `8471293`) returned 404 Not Found errors from the TMDb API. They may be typos, placeholders, or films TMDb does not hold.

## Decision
I report them as "unverified" and explicitly do not claim they don't exist. They are listed in `missing_ids.csv` for the client to review.

## Alternatives considered

### Alternative A: Drop them silently
- **Why it is attractive:** It makes the final report look cleaner.
- **Why rejected:** The client would not know that 4% of their usable list was never assessed.

## Consequences
- **What this buys:** An honest account of the data gap and the ability to pick up late additions.
- **What this costs:** Requires the client to manually verify 5 IDs.
- **What it costs the client if I am wrong:** Up to 5 valid films were excluded. If they belong to a single collection, a franchise bundle could be missing from the shortlist.
- **What would make me revisit this:** The client confirming what those five IDs were supposed to be.