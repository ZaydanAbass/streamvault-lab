import json
import pandas as pd
from config import CACHE_DIR

def read_cache(kind):
    records = []
    for path in sorted(CACHE_DIR.glob(f"{kind}_*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        data = record["data"]
        data["fetched_at"] = record["fetched_at"]
        records.append(data)
    return records

def build_tables():
    details = read_cache("details")
    credits = read_cache("credits")
    
    films_raw = pd.json_normalize(details, sep="_", max_level=1)
    films = films_raw.rename(columns={
        "belongs_to_collection_id": "collection_id",
        "belongs_to_collection_name": "collection_name",
    })
    films = films[["id", "title", "release_date", "budget", "revenue", "runtime",
                   "collection_id", "collection_name", "fetched_at"]]

    # FIXED: Explicit Schema Contract
    films = films.astype({
        "id": "int64",
        "budget": "int64",
        "revenue": "int64",
        "runtime": "int64",
    })
    
    # FIXED: Parse date strictly. If it fails, raise an error immediately.
    films["release_date"] = pd.to_datetime(films["release_date"], errors="raise")

    cast_raw = pd.json_normalize(credits, record_path="cast", meta=["id"],
                                 meta_prefix="film_", errors="ignore")
    cast = cast_raw.rename(columns={"id": "person_id", "name": "cast_name"})
    cast = cast[["film_id", "person_id", "cast_name", "order"]]
    
    # FIXED: Cast contract for cast table
    cast = cast.astype({"film_id": "int64", "person_id": "int64", "order": "int64"})

    return films, cast