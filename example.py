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

# print(df.index.levels[0])

# df = df.set_index(['group', 'item_id', 'item_name'])
# mux = pd.MultiIndex.from_product([df.index.levels[0], df.index.levels[1],df.index.levels[2]],names=['group', 'item_id', 'item_name'])
# df = df.reindex(mux).reset_index()
# print (df)

# quit()

# Cross all possible 'group' values with the unique pairs of
# `(item_id, item_name)` that already exist in the data
# complete(df, group, nesting(item_id, item_name))
# c = Complete(df,columns=['group','value1'], nest=['item_id','item_name'])
# c1 = Complete(df, nest=['item_id', 'item_name'], columns=['group'])
c = Complete(df,columns=['group','item_id', 'item_name'])
x = c.fill_df_2()
print(x)
