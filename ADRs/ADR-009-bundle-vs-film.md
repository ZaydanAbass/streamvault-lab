# ADR-009: Compare per film and per bundle

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** High. Bundles are what Kwame buys.

## Context

The film-level tables compare individual films. Kwame buys franchises as bundles, so a franchise with one strong film and several weak ones can look fine film by film and still be a poor purchase.

## Decision

I report both views. The bundle table has one row per collection, with totals summed from the film table only (never from the cast table, which would inflate revenue). A bundle's ROI is its combined revenue minus combined budget, divided by combined budget.

## Alternatives considered

### Alternative A: per film only
- **How it would work:** one row per film, as in the first tables.
- **Why it is attractive:** simpler, and larger groups.
- **Why rejected:** it is not the purchase unit, and it cannot test the "weak middle entries" argument.
- **What the recommendation looks like under it:** the same direction on the median (franchise 4.53 against standalone 4.00, strict, all years), but with no way to say anything about a bundle's weakest film.

## Consequences

- **What this buys:** a result in the unit Kwame buys.
- **What this costs:** fewer rows. 23 bundles have 2+ films, with sizes 3 films (11 bundles), 4 (7), 5 (2), 6 (1), 8 (1), and one with 2 films (as seen on screen). **TODO: confirm from your own print:** the single-film collections (9 by my arithmetic, 96 minus 87), so 32 bundles in total, and the exact `n_films` counts.
- **What it costs the client if I am wrong:** a bundle's ROI is weighted by budget, so a large-budget film dominates it. Comparing the bundle median (4.55 over 23 bundles) with a median of single films (4.00 over 25) compares unlike measures. The gap between them is small against the spread of bundles (standard deviation 2.39).
- **What would make me revisit this:** the completeness check showing that a bundle in my list is missing films.

## Evidence and code

`stage7_bundles.py`: `build_bundles`. The asserts below it (every film with a collection lands in exactly one bundle, and bundle ids are unique) sit outside the function, so keep them in the run.

## What this survives

A rerun cannot drop or double a film silently, because of those asserts.

## Open items

- **TODO:** print the median ROI of the 2000-onward bundles with their count, beside the standalone median (3.49, 12 films).
