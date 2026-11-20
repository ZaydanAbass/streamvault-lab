import pandas as pd

def join_tables(films, cast):
    merged = films.merge(
        cast,
        left_on="id", right_on="film_id",
        how="left",
        validate="one_to_many",
        indicator=True,
    )
    # FIXED: A left join means every cast row must be matched, 
    # but films without cast will have _merge == 'left_only'.
    assert merged[merged["_merge"] == "right_only"].empty, "cast rows without a film"
    return merged