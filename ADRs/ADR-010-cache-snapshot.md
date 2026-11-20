# ADR-010: Save API data locally for reproducible analysis

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
The analysis needs to run quickly and be repeatable in meetings. The database is community-edited and can change.

## Decision
We download and save the data locally. The analysis reads only from these saved files, not from the live internet.

## Alternatives considered

### Alternative A: Fetch live data every time
- **How it would work:** Query the API on every run.
- **Why it is attractive:** The data is always up to the minute.
- **Why rejected:** It would take too long for 500 titles, and the results could change from one meeting to the next if someone edited a movie's budget on Wikipedia.

## Consequences
- **What this buys:** Fast, repeatable, and consistent results.
- **What this costs:** The data is a snapshot and won't reflect updates automatically.
- **What it costs the client if I am wrong:** If a budget was corrected on the database yesterday, our analysis might use the old, incorrect number.
- **What would make me revisit this:** A major error found in the cached data.

## What this survives
Adjoa can just run the fetch script once a quarter to update the cache, and the analysis will run instantly.