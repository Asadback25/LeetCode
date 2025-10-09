# LeedCode
# 2879. Display the First Three Rows / Easy

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)