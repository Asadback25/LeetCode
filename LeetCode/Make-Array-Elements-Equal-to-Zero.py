# LeetCode
# 3354. Make Array Elements Equal to Zero / Easy

class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        ans = 0

        for x in nums:
            if x == 0:
                # At a zero position: check if starting here works
                if left_sum * 2 == total:
                    # left_sum == right_sum
                    ans += 2
                elif abs(left_sum * 2 - total) == 1:
                    # difference by 1 between left and right sums
                    ans += 1
            # whether zero or not, add non-zero to left_sum AFTER the check
            left_sum += x

        return ans
