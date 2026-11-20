import pandas as pd

def profile_films(films):
    films = films.copy()
    
    # FIXED: Filter out zero budgets BEFORE calculating ROI
    zero_budgets = (films["budget"] == 0).sum()
    if zero_budgets > 0:
        print(f"Warning: Dropping {zero_budgets} films with zero budget.")
    films = films[films["budget"] > 0].copy()
    
    films["year"] = films["release_date"].dt.year
    films["roi"] = (films["revenue"] - films["budget"]) / films["budget"]
    
    return films