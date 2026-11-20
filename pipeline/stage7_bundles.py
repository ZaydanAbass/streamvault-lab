import pandas as pd

from stage6_flags import films
import stage7_kpis  # KPI comparison runs first


# Bundle analysis
def build_bundles(films):
    in_collection = films[films["collection_id"].notna()]
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

bundles = build_bundles(films)
print(f"\n Number of distinct bundles: {len(bundles)}")
print(bundles["n_films"].value_counts().sort_index())

assert bundles["n_films"].sum() == films["collection_id"].notna().sum(), "bundle table lost films"
assert bundles["collection_id"].is_unique

buyable = bundles[bundles["n_films"] >= 2].copy()
print(buyable["roi"].describe())
print(len(buyable))   # expect 23

print("buyable bundles:", len(buyable), "median roi:", buyable["roi"].median())
standalones = films[~films["is_franchise_strict"]]
print("standalone films:", len(standalones), "median roi:", standalones["roi"].median())

shortlist_franchise = buyable.nlargest(3, "worst_roi")[
    ["collection_name", "n_films", "first_year", "worst_roi", "roi"]]
print(shortlist_franchise)

standalones = films[~films["is_franchise_strict"]]
print(standalones.nlargest(5, "roi")[["title", "year", "budget", "revenue", "roi"]])


# Standalone films from 2000 onward
recent = films[films["window_2000"] & ~films["is_franchise_strict"]]
print(f"Recent standalones: {len(recent)}")                                   # standalones from 2000 onward
print(recent.nlargest(5, "roi")[["title", "year", "budget", "revenue", "roi"]])


# Franchise bundles from 2000 onward
recent_bundles = buyable[buyable["first_year"] >= 2000]
print(f"Recent bundles: {len(recent_bundles)}")
print(recent_bundles.nlargest(6, "worst_roi")[
    ["collection_name", "n_films", "first_year", "worst_roi", "roi"]])


# Box 2: like-for-like medians for the 2000-onward window
recent_median = recent_bundles["roi"].median()
print("recent bundles:", len(recent_bundles), "median roi:", recent_median)

recent_standalones = films[films["window_2000"] & ~films["is_franchise_strict"]]
print("recent standalones:", len(recent_standalones),
      "median roi:", recent_standalones["roi"].median())