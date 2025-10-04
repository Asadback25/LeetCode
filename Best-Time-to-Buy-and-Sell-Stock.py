# LeetCode
# 121. Best Time To Buy And Sell Stock / Easy
# Time: O(n), Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        maxx = 0
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxx = max(maxx, profit)
            else:
                L = R
            R += 1
        return maxx



