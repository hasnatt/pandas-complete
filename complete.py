from itertools import product
import pandas as pd
from typing import List


class Complete:
    """complete function to replication the complete() function in R dplyr"""

    def __init__(self, df: pd.DataFrame, nest, columns):
        self.df = df
        self.nest = nest
        if all(isinstance(x, str) for x in columns):
            self.columns = [self.df[c] for c in columns]
            self.column_names = columns
        elif all(isinstance(x, pd.Series) for x in columns):
            self.columns = columns
            self.column_names = [col.name for col in columns]  

    def nesting(self):
        """
        """

        return self.df[self.nest].drop_duplicates(keep="first").values.tolist()

    def get_product(self):
        """

        """
        product_list = []
        product_list.append(self.nesting())
        for series in self.columns:
            product_list.append(list(set(series)))

        col_list = ["nest"] + (self.column_names)

        df = pd.DataFrame(list(product(*product_list)), columns=col_list)
        return df

    def fill_df(self):
        """
        """
    
        all_headers = self.nest + self.column_names
        complete_df = self.get_product()

        complete_df2 = pd.DataFrame(
            complete_df["nest"].values.tolist(),
            columns=self.nest)

        complete_df2[self.column_names] = complete_df[self.column_names] 
        del complete_df   
        df_full = pd.merge(
                complete_df2,
                self.df,
                how="left",
                on=all_headers)
    
        return df_full

