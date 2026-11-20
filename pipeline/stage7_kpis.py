import pandas as pd

from stage6_flags import films, windows


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


