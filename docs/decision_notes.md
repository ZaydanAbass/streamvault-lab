# Decision Notes

## 1. Definition of Franchise vs. Standalone
*   **Decision:** We used a "strict" filter (`min_films >= 2`) to define a franchise bundle, and treated anything with 1 film as a standalone.
*   **Why:** The brief warns against looking for "standalone hits" while accidentally grabbing a franchise. *Star Wars* and *Jaws* have massive ROIs but are part of collections. If we pitched them as standalones, the client would look foolish.
*   **Risk:** If we are wrong, we might exclude a single film that TMDb falsely grouped into a collection. However, the strict filter is safer for a boardroom pitch.

## 2. ROI Calculation
*   **Decision:** We calculate ROI as `(revenue - budget) / budget`.
*   **Why:** This shows the *profit* multiple, which is the standard metric for box office success. 
*   **Risk:** We excluded films with a budget of 0 to avoid divide-by-zero errors. If we are wrong, we might miss a low-budget indie hit, but our list is focused on major acquisitions, so this is acceptable.

## 3. The 8.37x Walk-Away Point
*   **Decision:** We anchor the LOTR walk-away point to the ROI of the weakest film in the bundle (8.37x).
*   **Why:** The board's primary fear is paying premium prices for weak middle entries. By guaranteeing we don't pay above the weakest film's return, we guarantee the bundle stays above our typical standalone ROI (4.0x).
*   **Risk:** This is a conservative pricing strategy. If the studio demands a higher premium, we walk away. 

## 4. Scaling to 500 Titles (Survives Adjoa)
*   **Decision:** The pipeline uses a robust caching system (`cache/*.json`) and a scalable data processing script.
*   **Why:** Adjoa will not need to manually edit code. She just updates `id_list.csv` and runs `run_all.py`. The script dynamically handles the new list, retries failed API calls, and drops bad IDs automatically. It will survive the 500-title run without starting over.