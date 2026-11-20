import sys
import os
import traceback
import subprocess
from config import API_KEY

def run_pipeline():
    # Import stages inside the function so they don't execute on import
    from stage3_tables import build_tables
    from stage4_join import join_tables
    from stage5_profile import profile_films
    from stage6_flags import add_flags
    from stage7_kpis import print_kpis
    from stage7_bundles import build_bundles, print_shortlists
    from stage7_talent import print_talent

    try:
        print("=== 1. Building Tables ===")
        films, cast = build_tables()

        print("\n=== 2. Joining Tables ===")
        merged = join_tables(films, cast)

        print("\n=== 3. Profiling Data ===")
        films = profile_films(films)

        print("\n=== 4. Adding Flags ===")
        films = add_flags(films)

        print("\n=== 5. KPI Comparisons ===")
        print_kpis(films)

        print("\n=== 6. Bundle Analysis ===")
        bundles = build_bundles(films)
        print_shortlists(films, bundles)

        print("\n=== 7. Talent Read ===")
        print_talent(films, cast)

        print("\n=== PIPELINE COMPLETE ===")

    except Exception as e:
        print(f"\n[!] PIPELINE FAILED: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Check for the --refresh flag
    if "--refresh" in sys.argv:
        print("=== 0. Refreshing API Cache ===")
        if not API_KEY:
            print("[!] ERROR: Cannot refresh cache without TMDB_API_KEY.", file=sys.stderr)
            sys.exit(1)
            
        print("Running pull.py to fetch new data...")
        # Run pull.py as a subprocess to keep it separate
        result = subprocess.run([sys.executable, "pull.py"], capture_output=False)
        if result.returncode != 0:
            print("[!] ERROR: pull.py failed. Aborting pipeline.", file=sys.stderr)
            sys.exit(1)
        print("Cache refreshed successfully.\n")

    run_pipeline()