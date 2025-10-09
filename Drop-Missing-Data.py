# LeetCode
# 2883. Drop Missing Data / Easy
# Pandas

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = ['name'])