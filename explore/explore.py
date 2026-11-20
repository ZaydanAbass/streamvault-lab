import pandas as pd
import numpy as np

ids = pd.read_csv("id_list.csv", dtype={"tmdb_id": str}, keep_default_na=False, skip_blank_lines=False)

print(f"Head: \n{ids.head()}")
print(f"\ninfo: \n{ids.info()}")
print(f"\ndesc: \n{ids.describe()}")
print(f"\nmissing: \n{ids.isnull().sum()}")
print(f"\nunique inputs: \n{ids["tmdb_id"].nunique()}")
print(f"\ntotal rows: {len(ids)}")
print(f"\nduplicate rows: {ids[ids["tmdb_id"].duplicated(keep=False)]}")

text = ids["tmdb_id"].str.strip()
number = pd.to_numeric(text, errors="coerce")

is_blank = text.isna() | (text == "")

is_repeat = number.notna() & number.duplicated()    # 2nd and later copies only

print(f"\nblank rows: {is_blank.sum()}")
print(f"\nrepeat rows: {is_repeat.sum()}")


is_imdb = text.str.match(r"^tt\d+$", na=False)           # tt followed by digits
is_bad_text = number.isna() & ~is_blank & ~is_imdb 
is_blank = text == ""                           # drop the text.isna() part
is_bad_text = number.isna() & ~is_blank & ~is_imdb          # catches "N/A"
is_nonpositive = number.notna() & (number <= 0)             # catches -1
is_repeat = number.notna() & ~is_nonpositive & number.duplicated()      # anything still unexplained

print(f"\nimdb rows: {is_imdb.sum()}")
print(f"bad text rows: {is_bad_text.sum()}")

outcome = np.select(
    [is_blank, is_imdb, is_bad_text, is_nonpositive, is_repeat],
    ["blank", "imdb_lookup", "bad_text", "invalid_id", "repeat"],
    default="fetch",
)

audit = pd.DataFrame({
    "file_row": ids.index + 2,        # +2 matches the spreadsheet row (line 1 is the header)
    "raw_value": ids["tmdb_id"],
    "outcome": outcome,
})

print("\n", audit["outcome"].value_counts())



ids_to_fetch = number[audit["outcome"] == "fetch"].astype("int64").reset_index(drop=True)
imdb_ids = text[audit["outcome"] == "imdb_lookup"].tolist()

print(f"\nids to fetch: {len(ids_to_fetch)}")
print(f"imdb ids to resolve later: {imdb_ids}")

audit.to_csv("id_audit.csv", index=False)
ids_to_fetch.to_csv("ids_to_fetch.csv", index=False, header=["tmdb_id"])

print(audit[audit["outcome"] != "fetch"])      # every excluded row