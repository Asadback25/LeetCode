# LeetCode
# 2048. Next Greater Numerically Balanced Number / Easy

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_beautiful(x):
            count = [0] * 10
            s = str(x)
            for d in s:
                count[int(d)] += 1

            for d in s:
                if count[int(d)] != int(d):
                    return False
            return True

        i = n + 1
        while True:
            if is_beautiful(i):
                return i
            i += 1