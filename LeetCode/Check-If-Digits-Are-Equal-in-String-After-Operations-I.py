# LeetCode
# 3461. Check If Digits Are Equal in String After Operations I / Easy

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(int(x) for x in s)

        while len(s) > 2:
            ns = []

            for x, y in pairwise(s):
                ns.append((x + y) % 10)
            s = ns

        return s[0] == s[1]