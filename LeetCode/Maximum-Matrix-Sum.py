# LeetCode
# 1975. Maximum Matrix Sum / Medium

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        neg_count = 0

        for r in matrix:
            for v in r:
                total += abs(v)
                if v < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(v))

        if neg_count % 2 != 0:
            total -= 2 * min_abs

        return total