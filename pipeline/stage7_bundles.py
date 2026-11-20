import pandas as pd
from config import WINDOW_CUTOFF_YEAR

def build_bundles(films):
    # FIXED: Only group collections that are strict franchises (2+ films)
    # This prevents single-film collections from being treated as "bundles"
    in_collection = films[films["is_franchise_strict"] == True]
    
    bundles = in_collection.groupby("collection_id").agg(
        collection_name=("collection_name", "first"),
        n_films=("id", "count"),
        first_year=("year", "min"),
        budget=("budget", "sum"),
        revenue=("revenue", "sum"),
        best_roi=("roi", "max"),
        worst_roi=("roi", "min"),
    )
    bundles["roi"] = (bundles["revenue"] - bundles["budget"]) / bundles["budget"]
    return bundles.reset_index()

def print_shortlists(films, bundles):
    buyable = bundles[bundles["n_films"] >= 2].copy()
    
    print("\n--- BUNDLE SHORTLIST ---")
    shortlist_franchise = buyable.nlargest(3, "worst_roi")[
        ["collection_name", "n_films", "first_year", "worst_roi", "roi"]]
    print("\nTop 3 Franchises (by weakest film):")
    print(shortlist_franchise)

    recent_bundles = buyable[buyable["first_year"] >= WINDOW_CUTOFF_YEAR]
    print(f"\nNumber of recent bundles: {len(recent_bundles)}")
    print(f"Median ROI for recent bundles: {recent_bundles['roi'].median():.2f}")

    # FIXED: Use the strict flag to ensure we don't include single-film collections
    recent_standalones = films[films["window_2000"] & ~films["is_franchise_strict"]]
    print(f"\nTop 5 Standalones (2000 Onward) - Total: {len(recent_standalones)}")
    print(f"Median ROI for recent standalones: {recent_standalones['roi'].median():.2f}")
    print(recent_standalones.nlargest(5, "roi")[["title", "year", "budget", "revenue", "roi"]])