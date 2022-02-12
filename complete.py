from itertools import product
import pandas as pd
from typing import List


class Complete:
    """ complete function to replication the complete() function in R dplyr """
    def __init__(self, df: pd.DataFrame, nest, columns):
        self.df = df
        self.nest = nest
        self.columns = columns
        self.column_names = [col.name for col in columns]