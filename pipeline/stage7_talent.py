import pandas as pd
from config import MAX_LEAD_ACTOR_ORDER, MIN_TALENT_FILMS
from stage3_tables import read_cache

def build_director_pairs(credits, films):
    crew = pd.json_normalize(credits, record_path="crew", meta=["id"],
                             meta_prefix="film_", errors="ignore")
    directors = (crew.loc[crew["job"] == "Director", ["film_id", "id", "name"]]
                 .rename(columns={"id": "person_id", "name": "person"}))
    pairs = directors.merge(
        films[["id", "roi", "year", "is_franchise_strict"]],
        left_on="film_id", right_on="id",
        how="left", validate="many_to_one", indicator=True,
    )
    assert (pairs["_merge"] == "both").all(), "director rows without a film"
    return pairs

def actors_pairs(cast, films, max_order=MAX_LEAD_ACTOR_ORDER):
    leads = (cast[cast["order"] <= max_order].rename(columns={"cast_name": "person"}))
    pairs = leads.merge(
        films[["id", "roi", "year", "is_franchise_strict"]],
        left_on="film_id", right_on="id",
        how="left", validate="many_to_one", indicator=True,
    )
    assert (pairs["_merge"] == "both").all(), "lead rows without a film"
    return pairs

def talent_summary(pairs, min_films=MIN_TALENT_FILMS):
    return (pairs.groupby(["person_id", "person"])
            .agg(n_films=("film_id", "nunique"),
                 median_roi=("roi", "median"),
                 franchise_share=("is_franchise_strict", "mean"))
            .reset_index()
            .query("n_films >= @min_films")
            .sort_values("median_roi", ascending=False))

def print_talent(films, cast):
    credits = read_cache("credits") # Need the raw credits for directors
    directors = build_director_pairs(credits, films)
    leads = actors_pairs(cast, films)

    print("\n--- TALENT READ ---")
    recent_films = films[films["window_2000"]]
    
    for name, frame in [("all years", films), ("2000 onward", recent_films)]:
        in_window = lambda p: p[p["film_id"].isin(frame["id"])]
        print(f"\nDirectors, {name}:\n", talent_summary(in_window(directors)).head(5))
        print(f"\nLeads, {name}:\n", talent_summary(in_window(leads)).head(5))