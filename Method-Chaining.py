# LeetCode
# 2891. Method Chaining / Easy
# Pandas

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    new_table = animals[animals['weight'] > 100].sort_values(by="weight", ascending=False)
    return pd.DataFrame(new_table['name'])