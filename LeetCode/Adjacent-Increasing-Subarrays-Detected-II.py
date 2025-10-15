# LeetCode
# 3350. Adjacent Subarrays Detection II / Medium

class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        ans, pre, cur = 0, 0, 0

        n = len(nums)
        for i, x in enumerate(nums):
            cur += 1

            if i == n - 1 or nums[i] >= nums[i + 1]:
                ans = max(ans, cur // 2, min(pre, cur))
                pre = cur
                cur = 0

        return ans
