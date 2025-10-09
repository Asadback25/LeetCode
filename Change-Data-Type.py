# LeetCode
# 2886. Change Data Type / Easy
# Pandas

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students