# LeetCode
# 1611. Minimum One Bit Operations to Make Integers Zero / Hard

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def f(x):
            if x == 0:
                return 0

            for i in range(31, -1, -1):
                if (x & (1 << i)) > 0:
                    return pow(2, i + 1) - 1 - f(x ^ (1 << i))

        return f(n)