# ADR-005: A franchise film belongs to a collection with at least two films in my list

- **Status:** Accepted
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** High. It narrows the franchise lead and decides which group the 1975 film Jaws sits in.

## Context

TMDb marks a franchise film with a non-null `belongs_to_collection`. The brief says franchises are sold as bundles ("all six or none"), but a collection with a single film in my list is not a bundle Kwame can buy from that list. Nine films sit in single-film collections.

Results from my run (n / median ROI / mean ROI):

| Window | Group | Loose (any collection) | Strict (2+ films in list) |
|---|---|---|---|
| All years | Standalone | 16 / 2.84 / 7.28 | 25 / 4.00 / 9.48 |
| All years | Franchise | 96 / 4.62 / 7.54 | 87 / 4.53 / 6.94 |
| 2000 onward | Standalone | 8 / 2.84 / 3.90 | 12 / 3.49 / 3.89 |
| 2000 onward | Franchise | 63 / 4.05 / 4.41 | 59 / 4.05 / 4.45 |

Jaws (1975, ROI 66.2) is marked as part of a collection, but only one Jaws film is in my list. Under the strict definition it is a standalone. About 55% of the combined ROI of the nine reclassified films is Jaws alone.

## Decision

The main definition is strict: 2+ films in the candidate list. The loose definition is computed as well and reported beside it. The flag is one function with a `min_films` parameter (`flag_franchise`).

## Alternatives considered

### Alternative A: any collection counts as a franchise
- **How it would work:** non-null collection means franchise.
- **Why it is attractive:** it is TMDb's own label, with no judgement from me.
- **Why rejected:** it counts nine films as bundle members when nothing in my list could be bought as a bundle.
- **What the recommendation looks like under it:** franchise wins more clearly. The median gap is 1.78 (all years) and 1.21 (2000 onward), against 0.53 and 0.56 under strict. The mean flip disappears (franchise 7.54 against standalone 7.28).

## Consequences

- **What this buys:** a franchise group that matches what is for sale in my list, and the more cautious comparison for franchise.
- **What this costs:** the nine single-film-collection films move into the "standalone" group, which then mixes true standalones with them.
- **What it costs the client if I am wrong:** if the loose definition is the right one (the studio sells more films per collection than my list holds), I understate the franchise lead by about 0.64 median points from 2000 onward and about 1.25 across all years.
- **What would make me revisit this:** the completeness check showing that single-film collections in my list have more films on offer (Jaws is the test case).

## Evidence and code

`stage6_flags.py`: `flag_franchise(films, min_films)`; `stage7_kpis.py`: `compare`.

## What this survives

On 500 titles the number of single-film collections may rise, so this choice must be re-read on the rerun.
