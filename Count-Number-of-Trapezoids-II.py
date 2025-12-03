# LeetCode
# 3625. Count Number of Trapezoids II / Hard


class Solution:
    def flat(self, arr: list, n: int) -> list:
        result = []

        def dfs(current_arr, current_depth):
            for item in current_arr:
                if isinstance(item, list) and current_depth < n:
                    dfs(item, current_depth + 1)
                else:
                    result.append(item)

        dfs(arr, 0)
        return result
