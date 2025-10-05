# LeetCode
# 217. Contains Duplicate / Easy
# Time: O(n), Space: O(n)

# 1st way
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

# 2nd way

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        return True
