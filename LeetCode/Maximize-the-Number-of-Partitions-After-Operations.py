# LeetCode
# 3003. Maximize the Number of Partitions After Operations / Hard


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}

        def dfs(i: int, can_change: bool, used_mask: int) -> int:
            if i == n:
                return 0

            key = (i, can_change, used_mask)
            if key in memo:
                return memo[key]

            ch_bit = 1 << (ord(s[i]) - ord('a'))
            res = 0

            # 1️⃣ O‘zgartirmasdan davom etish
            new_mask = used_mask | ch_bit
            if bin(new_mask).count("1") > k:
                res = max(res, 1 + dfs(i + 1, can_change, ch_bit))
            else:
                res = max(res, dfs(i + 1, can_change, new_mask))

            # 2️⃣ Agar hali bitta o‘zgartirish imkonimiz bo‘lsa
            if can_change:
                for j in range(26):
                    bit = 1 << j
                    new_mask2 = used_mask | bit
                    if bin(new_mask2).count("1") > k:
                        res = max(res, 1 + dfs(i + 1, False, bit))
                    else:
                        res = max(res, dfs(i + 1, False, new_mask2))

            memo[key] = res
            return res

        return dfs(0, True, 0) + 1