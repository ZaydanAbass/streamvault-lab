# StreamVault: Content Acquisition Analysis

## 1. Problem Statement
Kwame Boateng, VP of Content Acquisition, has $14M to commit at the board's licensing review on 31 October, and no evidence to commit it with. His team is divided:
*   **Half argue** that franchise bundles are the safer buy: built-in audience, bingeable series, and free marketing.
*   **The other half** argue that StreamVault overpays for weak middle entries in bundles and that the company would be better off cherry-picking standalone hits.

The stakes are personal. Two years ago, Kwame championed a trilogy bundle on instinct, and it underperformed. Last quarter, StreamVault passed on a five-film bundle that a competitor is now promoting. Without evidence this cycle, the money moves to originals. 

This repository provides the data, pipeline, and business recommendation to defend a decision.

---

## 2. Project Structure & Deliverables

This repository contains the full analysis and business deliverables for the board review:

*   **`pipeline/`** — The modular Python data pipeline (extracts, cleans, and analyzes data).
*   **`ADRs/`** — 6 Architecture Decision Records detailing the business logic assumptions.
*   **`data_diagnosis.md`** — The audit trail explaining the drop from 127 raw lines to 112 analyzed films.
*   **`recommendation.md`** — The core verdict on Franchises vs. Standalones.
*   **`deal_note.md`** — The specific negotiation advice for *The Lord of the Rings* bundle.
*   **`client_memo.md`** — The formatted, executive summary for Kwame.
*   **`decision_notes.md`** — A summary of key assumptions and what happens if they are wrong.
*   **`spot_check.py`** — Validation script proving cached data matches the live API.

---

## 3. How to Run the Pipeline (For Adjoa)

This pipeline is designed to run top-to-bottom from a clean clone. To reproduce the analysis on your own laptop:

### Step 1: Set Up the Environment
Open your terminal in the root folder of this repository:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
