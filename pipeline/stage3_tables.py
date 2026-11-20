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


