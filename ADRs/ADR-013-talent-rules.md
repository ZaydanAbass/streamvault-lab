# ADR-013: Talent needs at least three films in the window to be reported

- **Status:** Proposed (drafted from your code; **TODO: confirm**)
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Affects only the talent read.

## Context

Kwame's negotiators use talent as a lever, so a name must rest on enough films to be a signal.

## Decision

- A director is a crew member whose job is "Director". A film with two directors gives two rows.
- A person is reported only with `n_films >= 3` in that window (`min_films=3` in `talent_summary`), ranked by median ROI.
- The film count and the share of the person's films that are strict franchise films (`franchise_share`) are shown beside every figure. A director known for franchises may be showing the franchise effect, not their own.
- Each window uses only the films in that window.

## Alternatives considered

### Alternative A: lower or raise the minimum (2 or 5 films)
- **Why rejected:** two films is a pair, not a track record; five would leave almost nobody in the 2000-onward window.
- **What the recommendation looks like under it:** **TODO: re-run with 2 and 5 and note which names appear or vanish.**

## Consequences

- **What this buys:** fewer, steadier names.
- **What this costs:** a rising director with two hits is hidden.
- **What it costs the client if I am wrong:** negotiators lean on a name that rests on three films.
- **What would make me revisit this:** an obvious name missing from the list.
