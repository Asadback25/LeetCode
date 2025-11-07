# LeetCode
# 2528. Maximize the Minimum Powered City / Hard

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)

        def good(target):
            needed = 0

            q = collections.deque()

            current = sum(stations[:r + 1])
            if current < target:
                a = target - current
                needed += a
                current += a
                q.append((r, a))

            for i in range(1, N):
                if i + r < N:
                    current += stations[i + r]
                if i - r - 1 >= 0:
                    current -= stations[i - r - 1]
                    if len(q) > 0 and q[0][0] == i - r - 1:
                        _, d = q.popleft()
                        current -= d

                if target > current:
                    a = target - current
                    needed += a
                    current += a
                    q.append((i + r, a))

                if needed > k:
                    return False
            return needed <= k

        left = 0
        right = 10 ** 15

        while left < right:
            mid = (left + right + 1) // 2

            if good(mid):
                left = mid
            else:
                right = mid - 1
        return left