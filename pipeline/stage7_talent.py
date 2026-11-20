import pandas as pd

from stage3_tables import credits, cast
from stage6_flags import films
import stage7_bundles  # bundles and shortlists run first


# Talent Read (directors, actors)
def build_director_pairs(credits, films):
    """GRAIN: one row per film per director. ROI comes from the film table (many_to_one)."""
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


def actors_pairs(cast, films, max_order=2):
    """GRAIN: one row per film per lead actor (billing order 0 to max_order). See ADR-011."""
    leads = (cast[cast["order"] <= max_order]
             .rename(columns={"cast_name": "person"}))
    pairs = leads.merge(
        films[["id", "roi", "year", "is_franchise_strict"]],
        left_on="film_id", right_on="id",
        how="left", validate="many_to_one", indicator=True,
    )
    assert (pairs["_merge"] == "both").all(), "lead rows without a film"
    return pairs


def talent_summary(pairs, min_films=3):
    """One row per person, with the film count beside every statistic."""
    return (pairs.groupby(["person_id", "person"])
            .agg(n_films=("film_id", "nunique"),
                 median_roi=("roi", "median"),
                 franchise_share=("is_franchise_strict", "mean"))
            .reset_index()
            .query("n_films >= @min_films")
            .sort_values("median_roi", ascending=False))


directors = build_director_pairs(credits, films)
leads = actors_pairs(cast, films)

for name, frame in [("all years", films), ("2000 onward", films[films["window_2000"]])]:
    in_window = lambda p: p[p["film_id"].isin(frame["id"])]
    print(f"\nDirectors, {name}\n", talent_summary(in_window(directors)).head(8))
    print(f"\nLeads, {name}\n", talent_summary(in_window(leads)).head(8))

print("overall median ROI:", films["roi"].median())

recent_films = films[films["window_2000"]]
print("2000-onward median ROI:", recent_films["roi"].median())

nolan = directors[directors["person"] == "Christopher Nolan"]
nolan = nolan[nolan["film_id"].isin(recent_films["id"])]
print(nolan.merge(films[["id", "title"]], left_on="film_id", right_on="id")
      [["title", "year", "is_franchise_strict", "roi"]].sort_values("roi"))