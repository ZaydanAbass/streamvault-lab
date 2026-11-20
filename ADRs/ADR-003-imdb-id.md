# ADR-003: The IMDb-format id is resolved, and it is a repeat

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Low.

## Context

One entry, `tt0468569`, is an IMDb id, not a TMDb id. TMDb's `/find` lookup is deterministic, so unlike the other unusable entries this one can be resolved without guessing.

## Decision

I resolve it through TMDb's lookup. It returns 155, which is already in the list (my run printed `True` for "resolved id is in the fetch list"). It therefore counts as a repeat across two id systems, and id 155 appears three times in the raw list (twice as a number, once as an IMDb id).

## Alternatives considered

### Alternative A: exclude it as unusable
- **Why it is attractive:** no extra API call.
- **Why rejected:** I would not know whether it was a new film or a repeat, and the account of the 127 would not be provable.
- **What the recommendation looks like under it:** no change in this year's result, since it turned out to be a repeat. For another year's list, a genuine new film could be silently dropped.

## Consequences

- **What this buys:** every row is accounted for with evidence.
- **What this costs:** one extra API call per IMDb id.
- **What it costs the client if I am wrong:** nothing this year.
- **What would make me revisit this:** an IMDb id that resolves to a film not in the list. That must enter the fetch list.

## Evidence and code

`pull.py`: `resolve_imdb`.

## Open items

- **TODO:** `id_audit.csv` still labels this row `imdb_lookup`. Update its outcome after resolution (for example "repeat across id systems"), so the audit says what the note says.
