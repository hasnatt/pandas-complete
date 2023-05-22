
# Pandas Complete

  

Pandas Complete is a Python library that provides a function to complete missing values in specified columns of a Pandas DataFrame. It supports handling missing values in both regular and nested columns. This replicates the tidyr [complete()](https://www.rdocumentation.org/packages/tidyr/versions/1.3.0/topics/complete) fucntion from the R programming language

  

## Installation

  

You can install Pandas Complete using pip:

  

```

#TODO

```

  

## Usage

  

```python

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
print(complete(df, columns=["group", "item_id", "item_name"]))

# Cross all possible `group` values with the unique pairs of
# `(item_id, item_name)` that already exist in the data
print(complete(df, columns=["group"], nest=["item_id", "item_name"]))


# You can also choose to fill in missing values. By default, both implicit
# (new) and explicit (pre-existing) missing values are filled.
print(
    complete(
        df,
        columns=["group"],
        nest=["item_id", "item_name"],
        fill={"value1": 0, "value2": 99},
    )
)


```

  

## Features

  

- Handles missing values in regular and nested columns

- Supports arbitrary nesting depths for nested columns

- Returns a new DataFrame with completed values

- Supports both numeric and non-numeric data types

  


  

## Contributing

  

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


