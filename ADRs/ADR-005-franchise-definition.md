# ADR-005: A franchise requires at least two films in the dataset

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
A single film can belong to a franchise (e.g., *Jaws*), but if we only have one film from that franchise, it cannot be purchased as a bundle.

## Decision
I defined a franchise as a collection with 2 or more films in our list. Films in single-film collections are treated as standalones.

## Alternatives considered

### Alternative A: Any collection counts as a franchise
- **How it would work:** Rely purely on the database's franchise tag, even if we only have one film from it.
- **Why it is attractive:** It requires no subjective judgment.
- **Why rejected:** It inflates the franchise numbers with films that cannot actually be bought as bundles. It would make bundles look artificially better than they are.

## Consequences
- **What this buys:** A franchise group that accurately reflects what is actually for sale as a bundle.
- **What this costs:** Films like *Jaws* are mixed into the standalone group.
- **What it costs the client if I am wrong:** If the studio *is* selling bundles for these single films, the franchise advantage is slightly understated.
- **What would make me revisit this:** Confirmation from the studio that single films in our list are actually part of larger available bundles.

## What this survives
The logic is parameterized; changing the threshold to 3 or 4 films next year is a one-line change.