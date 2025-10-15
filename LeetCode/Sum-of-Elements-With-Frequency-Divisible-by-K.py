# LeetCode
# 3712. Sum of Elements With Frequency by K / Easy
# Time: O(n), Space: O(n)

class Solution(object):
    def sumDivisibleByK(self, nums, k):
        f = collections.Counter(nums)
        total = 0
        for key, v in f.items():
            if v % k == 0:
                total += key * v
        return total