# ADR-006: Both windows are always shown; 2000 onward leads

- **Status:** Accepted (**TODO: confirm that you want 2000 onward to lead**)
- **Date:** 2026-11-20
- **Decision owner:** Zaydan Abass Adamu
- **Risk to the recommendation:** High. Pre-2000 films distort the all-years mean and the standalone shortlist.

## Context

41 of 112 films (about 37%) were released before 2000, and 71 from 2000 onward. Budgets and revenues are nominal dollars, and box-office reporting differs by era. Yaw in Finance distrusts pre-2000 figures. The brief requires both windows and asks me to say loudly if the recommendation changes. Window sizes depend on the franchise definition (ADR-005); the strict figures are 12 standalone and 59 franchise from 2000 onward, and 25 and 87 across all years.

## Decision

Both windows are computed by the same code and shown side by side. The 2000-onward window is the main result because it is less exposed to Yaw's objection. It is still nominal dollars, so it is less exposed, not immune.

## Alternatives considered

### Alternative A: all years as the main result
- **Why it is attractive:** the most data and the largest standalone group (25 strict).
- **Why rejected:** it includes the 1966 to 1980 films that dominate the top of the ROI table.
- **What the recommendation looks like under it:** the median still favours franchise (4.53 against 4.00 strict, a gap of 0.53), but the mean flips to standalone (9.48 against 6.94). The headline would be much weaker and less stable (see ADR-008).

## Does the recommendation change between windows?

**Say it plainly in the memo.** On the median, franchise leads in all four tables (strict and loose, both windows), so the headline holds. The shortlist does change:
- Franchise: Lord of the Rings is first in both windows. The all-years third place is Back to the Future (1985), and from 2000 onward it is The Avengers.
- Standalones: the two five-film lists do not overlap at all. All years: Jaws, The Good, the Bad and the Ugly, Pulp Fiction, The Lion King, Schindler's List. From 2000 onward: Spirited Away, The Incredibles, Inception, The Smurfs, Monsters, Inc.

## Consequences

- **What this buys:** a result Yaw can engage with.
- **What this costs:** the standalone group is small from 2000 onward (12 strict, 8 loose).
- **What it costs the client if I am wrong:** if pre-2000 films are as relevant as recent ones, I have de-emphasised 41 films of evidence.
- **What would make me revisit this:** inflation-adjusted figures for the pre-2000 films.

## What this survives

Both windows are code-driven. **TODO:** the cut-off year is a bare `2000` in two places (`add_flags` in `stage6_flags.py` and `recent_bundles` in `stage7_bundles.py`), not one named constant. Make it one constant before the rerun.
