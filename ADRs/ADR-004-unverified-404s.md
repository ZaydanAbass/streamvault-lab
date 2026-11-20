# ADR-004: Five ids that returned 404 are reported as unverified

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Small: 5 of 117 usable ids (about 4%).

## Context

Five valid-looking ids returned 404: 8471293, 9412887, 8471294, 9412888 and 7733901. They are all seven-digit numbers, and two pairs are consecutive, unlike the rest of the list. I cannot tell whether they are typos, placeholders or films TMDb does not hold.

## Decision

I report them as "returned 404 on the fetch date, could not be verified", and I do not say they do not exist. They are listed in `missing_ids.csv`. 404s are not cached, so a rerun asks again.

## Alternatives considered

### Alternative A: cache the 404 and never ask again
- **Why it is attractive:** fewer API calls on a rerun.
- **Why rejected:** a cached "not found" goes stale silently if TMDb later adds the film.
- **What the recommendation looks like under it:** the same this year, but it could hide late additions in later years.

### Alternative B: drop them without reporting
- **Why rejected:** Kwame would not know that part of the list was never assessed.

## Consequences

- **What this buys:** an honest account, and a rerun that can pick up late additions.
- **What this costs:** five extra calls on each rerun.
- **What it costs the client if I am wrong:** up to 5 of 117 usable ids were never assessed. If they belong to one collection, a bundle could be missing from the shortlist. I have not been able to test this.
- **What would make me revisit this:** the studio desk confirming what those ids were meant to be.

## Evidence and code

`pull.py` output: `fetched 112, not found 5, asked 117`; the assert checks that fetched plus not found equals asked.

## Open items

- **TODO:** `missing_ids.csv` has no date, so the claim "on the fetch date" is not recorded. Add a `checked_at` column.
