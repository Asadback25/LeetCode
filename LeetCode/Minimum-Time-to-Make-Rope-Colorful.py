# LeetCode
# 1578. Minimum Time to Make Rope Colorful / Medium

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        arr = []
        for c, t in zip(colors, neededTime):
            arr.append((c, t))

        used = 0
        for g, t in groupby(arr, key = lambda item: item[0]):
            ct = list(nt for _, nt in t)
            m = max(ct)
            total = sum(ct)
            used += (total - m)
        return used