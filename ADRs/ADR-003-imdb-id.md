# ADR-003: Resolve the IMDb ID and treat it as a duplicate

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
One entry on the list (`tt0468569`) was an IMDb ID rather than the standard database ID. 

## Decision
I looked up the IMDb ID and found it corresponded to ID 155 (The Dark Knight), which was already in the list. Therefore, it was excluded as a duplicate.

## Alternatives considered

### Alternative A: Exclude it as unusable
- **How it would work:** Drop the row without looking it up.
- **Why it is attractive:** It saves one API call.
- **Why rejected:** I would not know whether it was a new film or a repeat, and the audit trail would be incomplete. For future lists, a genuine new film could be silently dropped.

## Consequences
- **What this buys:** Complete data integrity. Every row is accounted for.
- **What this costs:** Negligible time for one database lookup.
- **What it costs the client if I am wrong:** Nothing this year, as it was a duplicate.
- **What would make me revisit this:** An IMDb ID in a future list that resolves to a film *not* already on the list. That new film must enter the analysis.

## What this survives
The pipeline automatically resolves IMDb IDs and cross-checks them against the rest of the list.