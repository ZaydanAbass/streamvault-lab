# ADR-002: Repeated ids are counted once

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Low.

## Context

Six numeric ids appear twice: 155, 278, 550, 603, 680 and 1891. The list was assembled from three sources, so overlap is expected.

## Decision

I keep the first copy of each and exclude the second. A film is one title however many sources listed it.

## Alternatives considered

### Alternative A: keep every row
- **Why it is attractive:** it mirrors the list exactly.
- **Why rejected:** the same film would count twice in every group size and median.
- **What the recommendation looks like under it:** not computed. Six films would be double counted, and group sizes such as the 25 standalones would shift.

## Consequences

- **What this buys:** group sizes that count films, not list entries.
- **What this costs:** nothing, as long as the repeats really are the same film.
- **What it costs the client if I am wrong:** if a repeat was a typo for a different film, that film is missing.
- **What would make me revisit this:** the list owners saying a repeat was a typo.

## Evidence and code

`explore.py`: repeat rows 6.

