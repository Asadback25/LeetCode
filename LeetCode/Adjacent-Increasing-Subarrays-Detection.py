# LeetCode
# 3349. Adjacent Increasing Subarrays Detection | / Easy
# Time o(n * k), Space O(1)


class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):

        N = len(nums)

        def good(index):
            streak = 1
            for offset in range(1, k):
                if index + offset < N and nums[index + offset] > nums[index + offset - 1]:
                    streak += 1
                else:
                    return False
            return True

        for i in range(N):
            if good(i) and good(i + k):
                return True
        return False
