# LeetCode
# 3577. Count the Number of Computer Unlocking Permutations / Medium


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7

        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0

        result = 1
        for i in range(1, len(complexity)):
            result = (result * i) % MOD

        return resultA