# LeedCode
# 2889. Reshape Data: Pivot / Easy
# Pandas

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    new_table = weather.pivot_table(index='month', columns='city', values='temperature', aggfunc='max')
    return new_table