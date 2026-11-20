# ADR-001: Exclude unusable and duplicate entries rather than guessing

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu

## Context
The original candidate list contained 127 raw lines. It included blanks, bad text (`N/A`), invalid IDs (`-1`), exact duplicates, and one IMDb ID that resolved to a film already on the list. 

## Decision
I systematically dropped all blank rows, bad inputs, and duplicates. I resolved the IMDb ID and dropped it as a duplicate. I did not guess what the missing IDs were meant to be. The final analysis is built on 112 verified films.

## Alternatives considered

### Alternative A: Guess what the bad entries meant
- **Why it is attractive:** It could recover up to three candidate titles.
- **Why rejected:** It requires inventing data. Guessing introduces fake data into the ROI model.

## Consequences
- **What this buys:** Every row in the analysis is backed by verified data.
- **What this costs:** Up to 15 lines from the original list are not analyzed.
- **What it costs the client if I am wrong:** If one of the bad entries was a high-performing title, it is missing from the shortlist.
- **What would make me revisit this:** The client providing corrected IDs for the bad rows.