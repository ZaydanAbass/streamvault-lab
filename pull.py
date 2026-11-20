import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

load_dotenv()
API_KEY = os.environ["TMDB_API_KEY"]          # [] on purpose: no key, stop immediately
BASE_URL = "https://api.themoviedb.org/3"
CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

session = requests.Session()
retry = Retry(total=5, backoff_factor=1,
              status_forcelist=[429, 500, 502, 503, 504],
              respect_retry_after_header=True)
session.mount("https://", HTTPAdapter(max_retries=retry))

ids_to_fetch = pd.read_csv("ids_to_fetch.csv", dtype={"tmdb_id": "int64"})["tmdb_id"]
assert ids_to_fetch.is_unique and (ids_to_fetch > 0).all(), "bad fetch list"
print(len(ids_to_fetch))  

def fetch_cached(session, kind, tmdb_id):
    path = CACHE_DIR / f"{kind}_{tmdb_id}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))["data"]

    suffix = "" if kind == "details" else "/credits"
    r = session.get(f"{BASE_URL}/movie/{tmdb_id}{suffix}",
                    params={"api_key": API_KEY}, timeout=(3.05, 10))
    if r.status_code == 404:
        return None
    r.raise_for_status()

    record = {"fetched_at": datetime.now(timezone.utc).isoformat(), "data": r.json()}
    path.write_text(json.dumps(record), encoding="utf-8")
    return record["data"]

film = fetch_cached(session, "details", 155)
print(film["title"])                                    # a film title
print(fetch_cached(session, "details", 155)["title"])   


missing = []
fetched = 0

for tmdb_id in ids_to_fetch:
    details = fetch_cached(session, "details", tmdb_id)
    if details is None:
        missing.append(tmdb_id)               # no point asking for credits
        continue
    fetch_cached(session, "credits", tmdb_id)
    fetched += 1

pd.DataFrame({"tmdb_id": missing}).to_csv("missing_ids.csv", index=False)
print(f"fetched {fetched}, not found {len(missing)}, asked {len(ids_to_fetch)}")
assert fetched + len(missing) == len(ids_to_fetch), "ids unaccounted for"

def resolve_imdb(session, imdb_id):
    """Return the TMDb movie id for an IMDb id, or None if TMDb has no match."""
    r = session.get(
        f"{BASE_URL}/find/{imdb_id}",
        params={"api_key": API_KEY, "external_source": "imdb_id"},
        timeout=(3.05, 10),
    )
    r.raise_for_status()
    results = r.json().get("movie_results", [])
    return results[0]["id"] if results else None


resolved = resolve_imdb(session, "tt0468569")
print(resolved)
print(resolved in set(ids_to_fetch))

missing = pd.DataFrame(missing, columns=["tmdb_id"])
missing.to_csv("missing_ids.csv", index=False)   # True means it was a hidden repeat