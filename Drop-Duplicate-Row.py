# LeetCode
# 2882. Drop Duplicate Row / Easy
# Pandas

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])