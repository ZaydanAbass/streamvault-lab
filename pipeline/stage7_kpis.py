import pandas as pd

def compare(df, group_col):
    return df.groupby(group_col).agg(
        n=("id", "count"),
        median_roi=("roi", "median"),
        mean_roi=("roi", "mean"),
    )

def print_kpis(films):
    windows = {"all years": films, "2000 onward": films[films["window_2000"]]}
    
    print("\n--- KPI COMPARISONS ---")
    for name, frame in windows.items():
        for col in ["is_franchise_strict"]: # Only use the strict flag
            print(f"\n{name} | {col}\n", compare(frame, col))