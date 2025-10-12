# LeetCode
# 3186. Maximum Total Damage With Spell Casting / Medium


class Solution(object):
    def maximumTotalDamage(self, power):

        count = Counter(power)
        values = sorted(count)

        n = len(values)
        dp = [0] * (n + 1)

        # Step 2: DP from right to left
        for i in range(n - 1, -1, -1):
            x = values[i]

            skip = dp[i + 1]

            next_idx = bisect_right(values, x + 2)  # first index > x + 2
            take = x * count[x] + dp[next_idx]

            dp[i] = max(skip, take)

        return dp[0]
