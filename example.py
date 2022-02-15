import pandas as pd
from complete import complete

df = pd.DataFrame(
    data={
        "group": [1, 2, 1, 2],
        "item_id": [1, 2, 2, 3],
        "item_name": ["a", "a", "b", "b"],
        "value1": [1, None, 3, 4],
        "value2": [4, 5, 6, 7],
    }
)

# Generate all possible combinations of `group`, `item_id`, and `item_name`
# (whether or not they appear in the data)
# print(complete(df, columns=["group", "item_id", "item_name"]))

# Cross all possible `group` values with the unique pairs of
# `(item_id, item_name)` that already exist in the data
print(complete(df, columns=["group"], nest=["item_id", "item_name"]))


# You can also choose to fill in missing values. By default, both implicit
# (new) and explicit (pre-existing) missing values are filled.
# print(complete(df, columns=["group"], nest=["item_id", "item_name"], fill={"value1": 0, "value2": 99}))
