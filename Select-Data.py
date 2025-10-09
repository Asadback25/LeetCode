# LeetCode
# 2880. Select Data / Easy

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    res = students.loc[students['student_id']==101,['name','age']]
    return res