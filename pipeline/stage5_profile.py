import pandas as pd

from stage3_tables import films
import stage4_join  # stage 4 runs first

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

