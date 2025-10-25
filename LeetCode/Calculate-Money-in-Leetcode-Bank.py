# LeetCode
# 1716. Calculate Money in Leetcode Bank / Easy

class Solution:
    def totalMoney(self, n: int) -> int:
        curr = 0
        total = 0
        for i in range(1, n + 1):
            t = i % 7
            if t % 7 == 0:
                t += 7
            total += curr + t
            if t % 7 == 0:
                curr += 1


        return total