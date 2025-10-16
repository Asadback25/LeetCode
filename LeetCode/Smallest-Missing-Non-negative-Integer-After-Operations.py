# LeetCode
# 2598. Smallest Missing Non Negative Integer After Operations / Medium
# Time: O(n), Space: O(n)

class Solution(object):
    def findSmallestInteger(self, nums, value):
        N = len(nums)

        d = collections.Counter()
        for i in range(N):
            d[nums[i] % value] += 1

        i = 0
        while d[(i % value)] > 0:
            d[i % value] -= 1
            i += 1
        return i