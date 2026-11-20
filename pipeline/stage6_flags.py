import pandas as pd
from config import WINDOW_CUTOFF_YEAR, MIN_BUNDLE_SIZE

def add_flags(films):
    films = films.copy()
    
    # FIXED: Assert that no dates were lost during coercion
    assert films["year"].notna().all(), "Null years found after date coercion"
    
    size = films.groupby("collection_id")["id"].transform("count")
    films["is_franchise_strict"] = films["collection_id"].notna() & (size >= MIN_BUNDLE_SIZE)
    films["window_2000"] = films["year"] >= WINDOW_CUTOFF_YEAR
    
    return films