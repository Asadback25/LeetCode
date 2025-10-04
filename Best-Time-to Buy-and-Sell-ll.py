# LeetCode
# 121. Best Time To Buy And Sell Stock 2 / Medium
# Time: O(n), Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
        return profit