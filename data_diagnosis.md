# Data Diagnosis

## 1. Candidate List Accounting (127 down to 112)
*   **Total raw lines in file:** 127 (including header)
*   **Blank rows dropped:** 1 (Line 71 in the file)
*   **Remaining input rows:** 126
*   **Dropped by `explore.py` (9 rows):**
    *   6 exact duplicate TMDb IDs removed.
    *   1 invalid ID (`-1`) removed.
    *   1 bad text (`N/A`) removed.
    *   1 IMDb ID (`tt0468569`) was resolved to TMDb ID 155. Because ID 155 was already in the list, this became a hidden duplicate.
*   **Sent to API:** 117 unique valid IDs.
*   **API Failures:** 5 IDs were not found on TMDb (404 errors).
*   **Final Analysis Set:** **112 films**.
*   *Cost to Kwame:* 15 lines from the original file are missing from the final analysis due to bad data, duplicates, API failures, or blank rows.

## 2. Problems Found (Ranked by Risk)
*   **High Risk: Defining Standalones.** The highest ROI films on the list (*Star Wars*, *Jaws*, *The Godfather*) are technically part of collections. If we mistakenly pitch these as "standalone hits," the board will catch the error. We applied a strict filter (`is_franchise_strict`) to ensure the standalones are truly independent titles.
*   **High Risk: Box Office vs. StreamVault Revenue.** ROI is calculated on theatrical box office vs. production budget. This does not reflect actual licensing value. *Effect:* We can use it to rank relative appeal, but not as a direct price ceiling.
*   **Medium Risk: Missing Studio Bundle Data.** Our data has 3 films for LOTR. If the studio's bundle has 5, the math changes. 
*   **Low Risk: Zero Budgets & Dates.** The code correctly drops films with zero budget to prevent divide-by-zero errors. All 112 films have parseable dates.