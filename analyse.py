import json
from pathlib import Path

import pandas as pd

CACHE_DIR = Path("cache")


def read_cache(kind):
    records = []
    for path in sorted(CACHE_DIR.glob(f"{kind}_*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        data = record["data"]
        data["fetched_at"] = record["fetched_at"]
        records.append(data)
    return records


details = read_cache("details")
credits = read_cache("credits")
print(len(details), len(credits))        # expect 112 112

films_raw = pd.json_normalize(details, sep="_", max_level=1)
print(films_raw.shape)
print(films_raw.columns.tolist())


# GRAIN: one row per film.
films = films_raw.rename(columns={
    "belongs_to_collection_id": "collection_id",
    "belongs_to_collection_name": "collection_name",
})
films = films[["id", "title", "release_date", "budget", "revenue", "runtime",
               "collection_id", "collection_name", "fetched_at"]]

print(films.shape)                          # expect 112 rows
print(films["collection_id"].isna().sum())  # standalone films
print(films.head())

print("standalone:", films["collection_id"].isna().sum())
print("in a collection:", films["collection_id"].notna().sum())

collection_sizes = films.groupby("collection_id")["id"].count()
print(collection_sizes.value_counts().sort_index())   # how many collections have 1, 2, 3... films

# Casts
cast_raw = pd.json_normalize(credits, record_path="cast", meta=["id"],
                             meta_prefix="film_", errors="ignore")
print(cast_raw.shape)
print(cast_raw.columns.tolist())

# GRAIN: one row per film per cast member.
cast = cast_raw.rename(columns={"id": "person_id", "name": "cast_name"})
cast = cast[["film_id", "person_id", "cast_name", "order"]]
print(cast.shape)
print(cast.head())

assert len(films) == len(details), "film table lost rows"
assert films["id"].is_unique, "a film appears twice"
assert set(cast["film_id"]) <= set(films["id"]), "cast has films the film table lacks"

films_without_cast = set(films["id"]) - set(cast["film_id"])
print("films with no cast rows:", films_without_cast)


# Merging
merged = films.merge(
    cast,
    left_on="id", right_on="film_id",
    how="left",
    validate="one_to_many",
    indicator=True,
)
print(merged["_merge"].value_counts())


assert len(merged) == len(cast), "join dropped or duplicated cast rows"
assert merged["_merge"].eq("both").all(), "unmatched rows after join"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

print(films[["budget", "revenue", "runtime"]].describe())
print("budget 0:", (films["budget"] == 0).sum())
print("revenue 0:", (films["revenue"] == 0).sum())
print("both nonzero:", ((films["budget"] > 0) & (films["revenue"] > 0)).sum())
print("runtime 0:", (films["runtime"] == 0).sum())

films["year"] = pd.to_datetime(films["release_date"], errors="coerce").dt.year
print("unparseable dates:", films["year"].isna().sum())
print("before 2000:", (films["year"] < 2000).sum())

# Extremes
films["year"] = pd.to_datetime(films["release_date"], errors="coerce").dt.year
print(films["year"].isna().sum(), "unparseable dates")
print(films["year"].describe())

cols = ["title", "year", "budget", "revenue"]
print(films.nlargest(5, "revenue")[cols])
print(films.nsmallest(5, "budget")[cols])

# FAULTS

# Same film with 2 ids
print(f"\n{films[films["title"].duplicated(keep=False)].sort_values("title")[["id", "title", "year"]]}")

# Movies with budget bigger than revenue
films["roi"] = (films["revenue"] - films["budget"]) / films["budget"]
print((films["revenue"] < films["budget"]).sum())
cols = ["title", "year", "budget", "revenue", "roi"]
print(films.nlargest(5, "roi")[cols])
print(films.nsmallest(5, "roi")[cols])

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

# Compare ROI by group
def compare(df, group_col):
    return df.groupby(group_col).agg(
        n=("id", "count"),
        median_roi=("roi", "median"),
        mean_roi=("roi", "mean"),
    )

windows = {"all years": films, "2000 onward": films[films["window_2000"]]}

print(films[["year", "window_2000", "roi", "is_franchise"]].head())
assert films["year"].notna().all(), "unparseable release dates"
assert (films["budget"] > 0).all(), "zero budget: ROI would divide by zero"

for name, frame in windows.items():
    for col in ["is_franchise", "is_franchise_strict"]:
        print(f"\n{name} | {col}\n", compare(frame, col))

# Which movies drive the mean
print(films.nlargest(5, "roi")[["title", "year", "is_franchise", "roi"]])


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
print(len(recent))                                   # standalones from 2000 onward
print(recent.nlargest(5, "roi")[["title", "year", "budget", "revenue", "roi"]])


# Franchise bundles from 2000 onward
recent_bundles = buyable[buyable["first_year"] >= 2000]
print(len(recent_bundles))
print(recent_bundles.nlargest(6, "worst_roi")[
    ["collection_name", "n_films", "first_year", "worst_roi", "roi"]])


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