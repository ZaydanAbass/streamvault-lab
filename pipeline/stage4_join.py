import pandas as pd

from stage3_tables import films, cast


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

