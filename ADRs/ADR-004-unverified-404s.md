# ADR-004: Report missing IDs as unverified rather than assuming they don't exist

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
Five valid-looking IDs returned 404 errors (not found) from the database. They may be typos, placeholders, or films the database doesn't hold.

## Decision
I report them as "unverified" and explicitly do not claim they don't exist. They are listed in a separate missing data file for the client to review.

## Alternatives considered

### Alternative A: Drop them silently
- **How it would work:** Ignore the 404s and move on.
- **Why it is attractive:** It makes the final report look cleaner.
- **Why rejected:** The client would not know that 4% of their usable list was never assessed. Transparency is critical.

## Consequences
- **What this buys:** An honest account of the data gap and the ability to pick up late additions if the database updates.
- **What this costs:** Requires the client to manually verify 5 IDs.
- **What it costs the client if I am wrong:** Up to 5 valid films were excluded. If they belong to a single collection, a franchise bundle could be missing from the shortlist.
- **What would make me revisit this:** The client confirming what those five IDs were supposed to be.

## What this survives
The pipeline logs missing IDs and will ask for them again on the next run, ensuring late database additions are caught.