# LEetCode
# 3289. The Two Sneaky Numbers of Digitville / Easy
# Time: O(n log n), Space: O(!)

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                res.append(nums[i])
        return res