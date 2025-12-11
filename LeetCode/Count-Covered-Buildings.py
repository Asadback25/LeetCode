# LeetCode
# 3531. Count Covered Buildings / Medium


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings_by_x = defaultdict(list)
        buildings_by_y = defaultdict(list)

        for x_coord, y_coord in buildings:
            buildings_by_x[x_coord].append(y_coord)
            buildings_by_y[y_coord].append(x_coord)

        for x_coord in buildings_by_x:
            buildings_by_x[x_coord].sort()

        for y_coord in buildings_by_y:
            buildings_by_y[y_coord].sort()

        covered_count = 0

        for x_coord, y_coord in buildings:
            y_coords_at_x = buildings_by_x[x_coord]
            x_coords_at_y = buildings_by_y[y_coord]

            if (x_coords_at_y[0] < x_coord < x_coords_at_y[-1] and
                    y_coords_at_x[0] < y_coord < y_coords_at_x[-1]):
                covered_count += 1

        return covered_count