# ADR-010: The cache is a snapshot, and the analysis never touches the network

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** None for this year's numbers. It governs the rerun.

## Context

The analysis is rerun quarterly by Adjoa, sometimes live in a meeting, and the list will grow to about 500 titles. TMDb data is community-edited and changes.

## Decision

`pull.py` stores each raw response with a UTC timestamp in `cache/`. The analysis stages read only the cache. Ids already on disk are skipped, so a rerun fetches only what is new.

## Alternatives considered

### Alternative A: refetch everything on each run
- **Why it is attractive:** always current.
- **Why rejected:** about 1,000 calls at 500 titles, slow in a meeting, and results would change between runs.
- **What the recommendation looks like under it:** it could change from one run to the next with no code change.

## Consequences

- **What this buys:** repeatable analysis, and a record of what the source said and when.
- **What this costs:** cached films are never refreshed on their own.
- **What it costs the client if I am wrong:** a corrected budget or revenue on TMDb will not appear until the cache is refreshed.
- **What would make me revisit this:** a spot-check finding that live values differ from the snapshot.

## What this survives

| Survives a rerun on 500 titles | Needs Adjoa's attention |
|---|---|
| Counts are computed, not hardcoded | New ids that return 404 are asked again each run |
| Retry policy, timeouts, key from the environment | A film with budget 0 stops the run until she decides |
| Both windows are code-driven | The standalone group size may change, so the conclusion needs re-reading |
| Run order: `explore.py`, then `pull.py`, then the analysis (`run_all.py`) | She needs her own `.env` with `TMDB_API_KEY` |

**TODO:** keep only the rows you have tested from a clean clone. **TODO:** decide which of `run_all.py` and `analyse.py` is the one entry point (`analyse.py` repeats the stage files), and confirm whether `.env.example` exists.
