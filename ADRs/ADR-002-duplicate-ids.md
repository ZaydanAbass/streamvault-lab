# ADR-002: Count repeated IDs only once

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
Six numeric IDs appeared twice in the list (e.g., 155, 278). The client's list was likely assembled from multiple sources.

## Decision
I kept the first copy of each ID and excluded the duplicates. A film is one title however many times it appears on a spreadsheet.

## Alternatives considered

### Alternative A: Keep every row
- **How it would work:** Analyze the list exactly as provided, including duplicates.
- **Why it is attractive:** It mirrors the client's file exactly.
- **Why rejected:** The same film would count twice in every group size and median, artificially inflating its importance and skewing the averages.

## Consequences
- **What this buys:** Group sizes and ROI medians that reflect actual films, not list entries.
- **What this costs:** Nothing, as long as the repeats really are the same film.
- **What it costs the client if I am wrong:** If a repeat was a typo for a different film, that film is missing from our analysis.
- **What would make me revisit this:** If the client confirms a duplicate ID was intended to be a different movie.

## What this survives
The pipeline automatically deduplicates inputs on every run.