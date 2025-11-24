# LeetCode
# 1018. Binary Prefix Divisible By 5 / Easy

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0

        for num in nums:
            curr = (curr * 2 + num) % 5
            ans.append(curr == 0)

        return ans