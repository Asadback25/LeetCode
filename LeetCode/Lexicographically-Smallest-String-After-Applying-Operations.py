# LeetCode
# 1625. Lexicographically Smallest String After Applying Operations / Medium

from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        res = s

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            # Eng kichik lexicografikni yangilaymiz
            if cur < res:
                res = cur

            # 1️⃣ Operation 1: add to odd indices
            chars = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = "".join(chars)

            # 2️⃣ Operation 2: rotate
            rotated = cur[-b:] + cur[:-b]

            # Navbatga yangi holatlarni qo‘shamiz
            q.append(added)
            q.append(rotated)

        return res
