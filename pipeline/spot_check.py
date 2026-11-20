import json
import os
import random
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
CACHE_DIR = Path("cache")

if not API_KEY:
    raise ValueError("No TMDB_API_KEY found. Cannot run live spot check.")

def check_live_vs_cached(tmdb_id):
    """Fetches live details from TMDb and compares to cached JSON."""
    cache_path = CACHE_DIR / f"details_{tmdb_id}.json"
    
    if not cache_path.exists():
        return False, f"ID {tmdb_id}: No cache file found."

    cached_data = json.loads(cache_path.read_text(encoding="utf-8"))["data"]
    r = requests.get(f"{BASE_URL}/movie/{tmdb_id}", params={"api_key": API_KEY}, timeout=10)
    
    if r.status_code != 200:
        return False, f"ID {tmdb_id}: Live API returned {r.status_code}."
        
    live_data = r.json()
    fields = ["title", "budget", "revenue", "release_date"]
    fails = []
    
    for f in fields:
        if cached_data.get(f) != live_data.get(f):
            fails.append(f"{f} (Cache:{cached_data.get(f)} vs Live:{live_data.get(f)})")
            
    # Check collection
    c_coll = cached_data.get("belongs_to_collection") or {}
    l_coll = live_data.get("belongs_to_collection") or {}
    if c_coll.get("id") != l_coll.get("id"):
        fails.append("collection_id")

    if not fails:
        return True, f"ID {tmdb_id}: PASS ({cached_data['title']})"
    else:
        return False, f"ID {tmdb_id}: FAIL -> {', '.join(fails)}"

def main():
    print("=== SPOT CHECK: LIVE API vs CACHE ===\n")
    print("Sampling 15 records across 4 data slices...\n")
    
    # 1. Load the film data
    try:
        details = []
        for path in sorted(CACHE_DIR.glob("details_*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            data = record["data"]
            details.append(data)
        films = pd.json_normalize(details, sep="_")
        films["year"] = pd.to_datetime(films["release_date"], errors="coerce").dt.year
    except Exception as e:
        print(f"Error loading cache for sampling: {e}")
        return

    # 2. Define the 4 Slices (Fixed logic)
    # We check if the column exists and if the value is not null
    has_collection = films["belongs_to_collection_id"].notna() if "belongs_to_collection_id" in films.columns else pd.Series(False, index=films.index)
    
    slices = {
        "Franchise (2000+)": films[has_collection & (films["year"] >= 2000)],
        "Franchise (Pre-2000)": films[has_collection & (films["year"] < 2000)],
        "Standalone (2000+)": films[~has_collection & (films["year"] >= 2000)],
        "Standalone (Pre-2000)": films[~has_collection & (films["year"] < 2000)]
    }

    # 3. Sample and Check
    sample_size = 4
    passed = 0
    failed = 0

    for slice_name, df in slices.items():
        print(f"--- Slice: {slice_name} (Total: {len(df)}) ---")
        if df.empty:
            print("  (No films in this slice)\n")
            continue
            
        sample_ids = df["id"].sample(n=min(sample_size, len(df)), random_state=42).tolist()
        
        for tmdb_id in sample_ids:
            success, msg = check_live_vs_cached(tmdb_id)
            print(f"  [{ 'OK' if success else 'X' }] {msg}")
            if success:
                passed += 1
            else:
                failed += 1
        print("")

    print("=== RESULTS ===")
    print(f"Passed: {passed} | Failed: {failed}")
    if failed == 0:
        print("SUCCESS: All sampled records match the live API.")

if __name__ == "__main__":
    main()