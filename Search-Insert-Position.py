# LeetCode Questions
# 35. Search Insert Position / Easy

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (R + L) // 2
            guess = nums[mid]
            if guess == target:
                return nums.index(target)
            elif guess > target:
                R = mid - 1
            else:
                L = mid + 1
        return L