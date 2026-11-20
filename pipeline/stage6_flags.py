import pandas as pd

from stage5_profile import films


# Group sizes
def flag_franchise(films, min_films=1):
    size = films.groupby("collection_id")["id"].transform("count")
    return films["collection_id"].notna() & (size >= min_films)

films["is_franchise"] = flag_franchise(films, min_films=1)    # loose: any collection
films["is_franchise_strict"] = flag_franchise(films, min_films=2)    # a bundle needs 2+ films

print(films["is_franchise"].sum(), films["is_franchise_strict"].sum())

def add_flags(films):
    return films.assign(
        year=lambda d: pd.to_datetime(d["release_date"], errors="coerce").dt.year,
        window_2000=lambda d: d["year"] >= 2000,
        roi=lambda d: (d["revenue"] - d["budget"]) / d["budget"],
        is_franchise=lambda d: d["collection_id"].notna(),
    )

films = add_flags(films)
windows = {"all years": films, "2000 onward": films[films["window_2000"]]}

