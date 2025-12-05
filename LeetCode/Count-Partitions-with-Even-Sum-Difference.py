# LeetCode
# 3432. Count Partitions with Even Sum Difference / Easy

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        count = 0

        for num in nums[:-1]:
            left += num
            right -= num

            count += (left - right) % 2 == 0
        return count