import pandas as pd
from complete import Complete

df = pd.DataFrame(
    data={
        "group": [1, 2, 1, 2],
        "item_id": [1, 2, 2, 3],
        "item_name": ["a", "a", "b", "b"],
        "value1": [1, None, 3, 4],
        "value2": [4, 5, 6, 7],
    }
)

# columns=['group', 'item_id'] 
# columns1=[df['group'], df['item_id']] 

# print(all(isinstance(x, str) for x in columns))

# print(all(isinstance(x, pd.Series) for x in columns1))
# quit()
# series_col = [df[c] for c in columns]



# Cross all possible 'group' values with the unique pairs of
# `(item_id, item_name)` that already exist in the data
# complete(df, group, nesting(item_id, item_name))
c = Complete(df, nest=['item_id', 'item_name'], columns=[df['group']])


print(c.fill_df())