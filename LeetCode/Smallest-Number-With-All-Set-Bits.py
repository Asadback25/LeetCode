# LeetCode
# 3370. Smallest Number With All Set Bits / Easy
# Time: O(log n), Space: O(1)


class Solution:
    def smallestNumber(self, n: int) -> int:
        curr = 1
        while curr < n:
            curr *= 2
            curr += 1
        return curr
