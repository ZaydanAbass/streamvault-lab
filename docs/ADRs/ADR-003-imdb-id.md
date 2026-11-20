# ADR-003: Resolve the IMDb ID and treat it as a duplicate

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
# ADR-003: A franchise requires at least two films in the dataset

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
A single film can belong to a franchise (e.g., *Jaws*), but if we only have one film from that franchise in our dataset, it cannot be purchased as a bundle. 

## Decision
I defined a franchise bundle as a collection with **2 or more films** in our list. Films in single-film collections are treated as standalones.

## Alternatives considered

### Alternative A: Any collection counts as a franchise
- **How it would work:** Rely purely on the database's franchise tag, even if we only have one film.
- **Why it is attractive:** It requires no subjective judgment.
- **Why rejected:** It inflates the franchise numbers with films that cannot actually be bought as bundles.

## Consequences
- **What this buys:** A franchise group that accurately reflects what is actually for sale as a bundle.
- **What this costs:** Films like *Jaws* are mixed into the standalone group.
- **What it costs the client if I am wrong:** If the studio *is* selling bundles for these single films, the franchise advantage is slightly understated.
- **What would make me revisit this:** Confirmation from the studio that single films in our list are actually part of larger available bundles.
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