# LeetCode
# 2512. Minimum Operations to Make Array Sum Divisible by K / Easy

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        total = sum(nums)
        return total % k
