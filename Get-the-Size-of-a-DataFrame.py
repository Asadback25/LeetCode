# LeetCode
# 2878. Get the Size of a DataFrame / Easy
# Pandas

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row, col = players.shape
    return [row, col]