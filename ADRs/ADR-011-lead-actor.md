# ADR-011: A lead actor is one of the three top-billed cast members

- **Status:** Accepted (**TODO: confirm**)
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** Affects only the talent read.

## Context

A cast list holds about 70 people per film (7,827 rows over 112 films). Kwame wants to know which lead actors signal a worthwhile title.

## Decision

A lead has billing `order` 0, 1 or 2 (`max_order=2` in `actors_pairs`).

## Alternatives considered

### Alternative A: only the top-billed actor
- **Why it is attractive:** one clear lead per film.
- **Why rejected:** many films are ensembles, and one name misses them.
- **What the recommendation looks like under it:** **TODO: run with `max_order=0` and note which names survive.**

## Consequences

- **What this buys:** more films per actor, so counts are less fragile.
- **What this costs:** a supporting actor can count as a lead.
- **What it costs the client if I am wrong:** negotiators may give weight to an actor who is a minor draw.
- **What would make me revisit this:** a talent read with very few films per name.

## What this survives

The cut-off is one parameter, and the film count sits beside every actor.
