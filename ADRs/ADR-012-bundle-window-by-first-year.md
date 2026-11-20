# ADR-012: A bundle belongs to a window by its first film's release year

- **Status:** Proposed (drafted from your code; **TODO: confirm it is what you intend**)
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Moderate. It decides which bundles appear in the 2000-onward shortlist.

## Context

A bundle can span decades, so one window assignment is arbitrary. This resolves the open note in the earlier draft.

## Decision

`first_year` is the earliest release year among the bundle's films in my list, and `recent_bundles` keeps bundles with `first_year >= 2000`. A bundle is then counted whole, with all its films, in the 2000-onward window.

## Alternatives considered

### Alternative A: use only the 2000+ films of each bundle
- **Why it is attractive:** the window is purely about film dates.
- **Why rejected:** it breaks the bundle, which is sold whole.
- **What the recommendation looks like under it:** **TODO: not run.**

### Alternative B: use the last film's year
- **Why rejected:** it would let a 1980s bundle with one 2000s sequel into the recent window.

## Consequences

- **What this buys:** a simple, testable rule that keeps bundles whole.
- **What this costs:** a bundle that starts in 1999 with later films is out of the recent window entirely.
- **What it costs the client if I am wrong:** a strong straddling bundle could be missed from the recent shortlist.
- **What would make me revisit this:** **TODO:** list the bundles with films on both sides of 2000 and see how many there are.
