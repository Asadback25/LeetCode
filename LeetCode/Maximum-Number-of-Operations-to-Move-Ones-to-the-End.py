# LeetCode\
# 3228. Maximum Number of Operations to Move Ones to the End / Medium

class Solution:
    def maxOperations(self, s: str) -> int:
        total = 0
        curr = 0

        for g, t in groupby(s):
            L = len(list(t))
            if g == '0':
                total += curr
            else:
                curr += L

        return total