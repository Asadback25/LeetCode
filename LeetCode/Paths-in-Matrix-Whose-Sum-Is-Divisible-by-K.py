# LeetCode
# 2435. Paths in Matrix Whose Sum Is Divisible by K / Hard


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[i][j][r] = ways to reach (i,j) with sum % k == r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for r in range(k):
                    ways = dp[i][j][r]
                    if ways == 0:
                        continue

                    # move down -> add value of the destination cell
                    if i + 1 < m:
                        nr = (r + grid[i+1][j]) % k
                        dp[i+1][j][nr] = (dp[i+1][j][nr] + ways) % MOD

                    # move right -> add value of the destination cell
                    if j + 1 < n:
                        nr = (r + grid[i][j+1]) % k
                        dp[i][j+1][nr] = (dp[i][j+1][nr] + ways) % MOD

        return dp[m-1][n-1][0]
