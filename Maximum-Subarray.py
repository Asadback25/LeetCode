# LeetCode
# 53. Maximum Subarray / Medium
# Time: O(n), Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        cur = 0

        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            maxSub = max(maxSub, cur)

        return maxSub
