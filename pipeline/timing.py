import contextlib
import csv
import importlib
import io
import os
import platform
import statistics
import sys
import tempfile
import time
import json
from pathlib import Path

import numpy as np
import pandas as pd

STAGES = [
    ("stage3_tables", "read cache + flatten"),
    ("stage4_join", "join"),
    ("stage5_profile", "profile"),
    ("stage6_flags", "flags"),
    ("stage7_kpis", "kpi comparison"),
    ("stage7_bundles", "bundles + shortlists"),
    ("stage7_talent", "talent read"),
]
SIZES = [127, 500, 5000]      # synthetic film counts
WARM_RUNS = 5                 # runs after the first (cold) run; the median is reported
HOME = Path.cwd()


def make_cache(n_films, folder):
    """Write a synthetic cache/ folder shaped like the real one (details + credits per film)."""
    rng = np.random.default_rng(42)
    cache = Path(folder) / "cache"
    cache.mkdir(parents=True, exist_ok=True)

    collection_ids = []                       # ~80% of films sit in collections of 1 to 5
    next_collection = 1
    while len(collection_ids) < n_films:
        if rng.random() < 0.2:
            collection_ids.append(None)
        else:
            size = int(rng.integers(1, 6))
            collection_ids.extend([next_collection] * size)
            next_collection += 1
    collection_ids = collection_ids[:n_films]

    people = max(200, n_films * 3)            # person pool, so people repeat across films
    stamp = "2026-11-20T00:00:00+00:00"
    for i in range(n_films):
        film_id = i + 1
        budget = int(rng.integers(1_000_000, 300_000_000))
        collection = collection_ids[i]
        details = {
            "id": film_id,
            "title": f"Film {film_id}",
            "release_date": f"{int(rng.integers(1966, 2020))}-06-15",
            "budget": budget,
            "revenue": int(budget * rng.uniform(1.2, 12)),
            "runtime": int(rng.integers(80, 200)),
            "belongs_to_collection": (
                None if collection is None
                else {"id": collection, "name": f"Collection {collection}"}
            ),
            "genres": [{"id": 1, "name": "Action"}],
        }
        cast = [{"id": int(rng.integers(1, people)), "name": f"Person {j}", "order": j}
                for j in range(70)]
        crew = [{"id": int(rng.integers(1, people)), "name": "Someone", "job": "Director"},
                {"id": int(rng.integers(1, people)), "name": "Someone", "job": "Writer"}]
        credits = {"id": film_id, "cast": cast, "crew": crew}
        (cache / f"details_{film_id}.json").write_text(
            json.dumps({"fetched_at": stamp, "data": details}), encoding="utf-8")
        (cache / f"credits_{film_id}.json").write_text(
            json.dumps({"fetched_at": stamp, "data": credits}), encoding="utf-8")


def run_once():
    """Run every stage once, in order, and return {stage_file: seconds}."""
    for name, _ in STAGES:
        sys.modules.pop(name, None)           # force a fresh run of each stage
    timings = {}
    for name, _ in STAGES:
        with contextlib.redirect_stdout(io.StringIO()):
            start = time.perf_counter()
            importlib.import_module(name)
            timings[name] = time.perf_counter() - start
    return timings


def measure(label):
    """One cold run, then WARM_RUNS warm runs. Returns (cold, warm_median) per stage."""
    cold = run_once()
    warm_runs = [run_once() for _ in range(WARM_RUNS)]
    warm = {name: statistics.median(r[name] for r in warm_runs) for name, _ in STAGES}
    print(f"measured {label}")
    return cold, warm


def main():
    print("HARDWARE / SOFTWARE (copy into the measurement report)")
    print(f"  machine : {platform.platform()}")
    print(f"  cpu     : {platform.processor() or 'n/a'}, {os.cpu_count()} logical cores")
    print(f"  python  : {platform.python_version()}")
    print(f"  pandas  : {pd.__version__}, numpy {np.__version__}\n")

    results = {}                              # label -> (cold, warm)
    if (HOME / "cache").exists():
        results["real data"] = measure("real data")
    else:
        print("no cache/ folder here, so the real-data run is skipped\n")

    for n in SIZES:
        with tempfile.TemporaryDirectory() as tmp:
            make_cache(n, tmp)
            os.chdir(tmp)                     # the stage files read the relative path 'cache'
            try:
                results[f"{n} synthetic"] = measure(f"{n} synthetic films")
            finally:
                os.chdir(HOME)

    labels = list(results)
    print("\nWARM MEDIAN SECONDS PER STAGE (median of", WARM_RUNS, "runs)")
    print(f"{'stage':<24}" + "".join(f"{label:>16}" for label in labels))
    for name, text in STAGES:
        print(f"{text:<24}" + "".join(f"{results[l][1][name]:>16.4f}" for l in labels))
    totals = {l: sum(results[l][1].values()) for l in labels}
    print(f"{'TOTAL':<24}" + "".join(f"{totals[l]:>16.4f}" for l in labels))
    print(f"{'cold first run (total)':<24}"
          + "".join(f"{sum(results[l][0].values()):>16.4f}" for l in labels))

    print("\nSCALING (warm total). Data x4 should cost about x4 if linear.")
    sized = [f"{n} synthetic" for n in SIZES]
    for a, b in zip(sized, sized[1:]):
        data_ratio = int(b.split()[0]) / int(a.split()[0])
        print(f"  {a} -> {b}: data x{data_ratio:.1f}, time x{totals[b] / totals[a]:.1f}")

    print("\nSCALING PER STAGE, 500 -> 5000 rows (data x10)")
    for name, text in STAGES:
        a, b = results["500 synthetic"][1][name], results["5000 synthetic"][1][name]
        print(f"  {text:<24} x{b / a:.1f}")

    with open("timing_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["dataset", "stage", "cold_seconds", "warm_median_seconds"])
        for label, (cold, warm) in results.items():
            for name, text in STAGES:
                writer.writerow([label, text, f"{cold[name]:.5f}", f"{warm[name]:.5f}"])
    print("\nsaved timing_results.csv")


if __name__ == "__main__":
    main()
