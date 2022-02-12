import pandas as pd

df = pd.DataFrame(
    data={
        "group": [1, 2, 1, 2],
        "item_id": [1, 2, 2, 3],
        "item_name": ["a", "a", "b", "b"],
        "value1": [1, None, 3, 4],
        "value2": [4, 5, 6, 7],
    }
)
