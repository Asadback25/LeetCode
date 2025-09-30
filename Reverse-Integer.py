# LeetCode Questions
# 7. Reverse Integer / Medium

class Solution:
    def reverse(self, x: int) -> int:
        min, max = -2**31, 2**31 - 1


        s = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1]) * s


        if result < min or result > max:
            return 0
        return result