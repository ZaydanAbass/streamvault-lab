# ADR-001: Exclude unusable list entries rather than guessing their intent

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
The candidate list contained formatting errors, specifically blank rows, the text `N/A`, and an invalid ID (`-1`). These cannot be fetched from the database.

## Decision
I excluded the blank row, the text `N/A`, and the ID `-1`, and recorded each in an audit file. 

## Alternatives considered

### Alternative A: Guess what the unusable entries meant
- **How it would work:** Attempt to manually identify which films the client meant based on context.
- **Why it is attractive:** It could recover up to three candidate titles.
- **Why rejected:** It requires inventing data. I would be choosing which film the client meant, which could skew the ROI analysis.

## Consequences
- **What this buys:** Every row in the analysis is backed by verified data.
- **What this costs:** Up to three candidate titles are never identified.
- **What it costs the client if I am wrong:** If one of the three was a real, high-performing title, it is missing from the shortlist. 
- **What would make me revisit this:** The client providing corrected IDs for those specific rows.

## What this survives
The automated pipeline will always drop these bad inputs and log them, so a 500-title list will be cleaned the same way.