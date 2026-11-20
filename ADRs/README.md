# StreamVault licensing review: decision notes

Decision owner: Zaydan Abass Adamu. Data as of: **TODO: the latest `fetched_at` date in `cache/`**.
Every number below comes from my own run of the pipeline. Items marked **TODO** still need a number or a choice from me before I submit.

## Index, ranked by risk to the recommendation

| Rank | ADR | Decision | Could it move the recommendation? |
|---|---|---|---|
| 1 | [008](ADR-008-median-headline.md) | Headline statistic is the median, with the mean shown | Yes: the mean flips in one table, because of two films |
| 2 | [005](ADR-005-franchise-definition.md) | Franchise means a collection with 2+ films in the list | Yes: narrows the franchise lead and sets where Jaws sits |
| 3 | [006](ADR-006-time-windows.md) | Both windows shown; 2000 onward leads | Yes: pre-2000 films distort all years, and the shortlists differ |
| 4 | [014](ADR-014-shortlist-ranking.md) | Bundles ranked by weakest film; standalones by ROI | Yes: decides who is on the shortlist |
| 5 | [009](ADR-009-bundle-vs-film.md) | Compare per film and per bundle | Yes: bundles are what Kwame buys |
| 6 | [007](ADR-007-roi-definition.md) | ROI is worldwide revenue against budget, nominal dollars | Possibly: favours big-gross and old, cheap films |
| 7 | [012](ADR-012-bundle-window-by-first-year.md) | A bundle's window is its first film's year | Moderately: decides the recent shortlist |
| 8 | [011](ADR-011-lead-actor.md) | Lead actor is billing order 0 to 2 | Talent read only |
| 9 | [013](ADR-013-talent-rules.md) | Talent needs 3+ films in the window | Talent read only |
| 10 | [004](ADR-004-unverified-404s.md) | Five 404 ids are reported as unverified | Small: about 4% of usable ids |
| 11 | [001](ADR-001-unusable-ids.md), [002](ADR-002-duplicate-ids.md), [003](ADR-003-imdb-id.md) | Id list clean-up | No, but they explain the gap from 127 to 112 |
| 12 | [010](ADR-010-cache-snapshot.md) | The cache is a snapshot | No: governs the rerun |

## Account of the 127 rows

| Where the rows went | Count |
|---|---|
| Blank line, `N/A`, `-1` (ADR-001) | 3 |
| Repeated numeric ids (ADR-002) | 6 |
| IMDb id that is a repeat of 155 (ADR-003) | 1 |
| Returned 404 (ADR-004) | 5 |
| **Analysed** | **112** |
| **Total** | **127** |

## Open items before submitting

1. Data-as-of date (above).
2. ADR-001: add the assert that all 127 rows are accounted for. ADR-003: update the audit outcome for the IMDb row. ADR-004: add `checked_at` to `missing_ids.csv`.
3. ADR-002: check the output for "same title, two ids" and add an ADR if any film appears twice.
4. ADR-006: one named constant for the cut-off year.
5. ADR-009: confirm `len(bundles)`, the `n_films` counts, and add the 2000-onward bundle median.
6. ADR-005, 009 and 014: run the collection completeness check and record the result.
7. ADR-011, 012, 013, 014: confirm, and run the alternatives marked TODO.
8. ADR-010: test the "survives" rows from a clean clone, pick one entry point, confirm `.env.example`.
