# ADR-001: Three unusable entries in the id list are excluded, not guessed

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Low (housekeeping), but it explains part of the gap from 127 rows to 112 films.

## Context

`id_list.csv` has 127 data rows. Pandas, by default, skips an empty line and reads the text `N/A` as a missing value, so my first look showed fewer than 127 rows and hid two of the bad entries. I read the file as text with those defaults switched off, so nothing is hidden.

## Decision

I exclude the blank line, the text `N/A`, and `-1`. None of them can be fetched, and `-1` would otherwise have been sent to the API as an id. Each excluded row is recorded in `id_audit.csv` with its spreadsheet row number (`file_row`).

## Alternatives considered

### Alternative A: guess what the unusable entries meant
- **Why it is attractive:** it could recover up to three candidate titles.
- **Why rejected:** I would be choosing which film the client meant.
- **What the recommendation looks like under it:** not computable. At most three more films out of 127 would be assessed.

## Consequences

- **What this buys:** every row has exactly one outcome.
- **What this costs:** up to three candidate titles are never identified.
- **What it costs the client if I am wrong:** if one of the three was a real title, it is missing from the shortlist.
- **What would make me revisit this:** the owners of the list identifying those entries.

## Evidence and code

`explore.py`: outcome counts blank 1, bad_text 1, invalid_id 1.

## What this survives

The counts are computed on each run, not hardcoded, and `id_audit.csv` is rewritten each time.

