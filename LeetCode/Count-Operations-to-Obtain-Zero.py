# LeetCode
# 2169. Count Operations to Obtain Zero / Easy

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        if num2 > num1:
            num1, num2, = num2, num1

        while num2 > 0:
            num1 -= num2
            if num2 > num1:
                num1, num2 = num2, num1
            count += 1
        return count
