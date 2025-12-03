# LeetCode
# 3625. Count Number of Trapezoids II / Hard


from fractions import Fraction


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        N = len(points)

        ys = collections.defaultdict(collections.Counter)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]

                dy = y2 - y1
                dx = x2 - x1

                slope = None
                if dx == 0:
                    # vertical
                    slope = (1, 0)
                    ys[slope][x1] += 1
                elif dy == 0:
                    slope = (0, 1)
                    ys[slope][y1] += 1
                else:
                    # slope = (dy // g, dx // g)

                    """
                    y = mx + b

                    m = slope
                    y1 = slope * x1 + b
                    y1 - slope * x1 = b
                    """
                    slope = Fraction(dy, dx)
                    b = y1 - slope * x1
                    ys[slope][b] += 1

        ans = 0
        for slope in ys.keys():
            if len(ys[slope]) == 1:
                continue
            pairs = 0
            for y in ys[slope].keys():
                count = ys[slope][y]
                pairs += count

            for y in ys[slope].keys():
                count = ys[slope][y]

                current_pairs = count
                ans += (current_pairs * (pairs - current_pairs))

        mid = collections.defaultdict(collections.Counter)
        # double counts parallelograms
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]

                dy = y2 - y1
                dx = x2 - x1

                slope = None
                if dx == 0:
                    # vertical
                    slope = (1, 0)
                elif dy == 0:
                    slope = (0, 1)
                else:
                    if dx < 0:
                        dy *= -1
                        dx *= -1
                    g = gcd(abs(dy), abs(dx))
                    slope = (dy // g, dx // g)

                mx, my = x1 + x2, y1 + y2
                mid[(mx, my)][slope] += 1

        p = 0
        for m in mid.keys():
            if len(mid[m]) == 1:
                continue

            total = 0
            for s in mid[m]:
                total += mid[m][s]

            for s in mid[m]:
                p += mid[m][s] * (total - mid[m][s])

        # print(ans, p)
        return ans // 2 - p // 2