class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        prefix = [[0] * (n + 1) for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2 + 1):
                prefix[i][col1] += 1
                prefix[i][col2 + 1] -= 1

        for i in range(n):
            s = 0
            for j in range(n):
                s += prefix[i][j]
                ans[i][j] = s
        
        return ans
