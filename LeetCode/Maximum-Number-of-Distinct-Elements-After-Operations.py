# LeetCode
# 3397. Maximum Number of Distinct Elements After Operations / Medium
# Time: O(n), Space: O(n)

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        INF = 10 ** 20
        count = 0
        nums.sort()
        next_avail = -INF

        for i in nums:
            if i - k >= next_avail:
                next_avail = i - k + 1
                count += 1
                continue

            if i - k < next_avail <= i + k:
                next_avail += 1
                count += 1

        return count
