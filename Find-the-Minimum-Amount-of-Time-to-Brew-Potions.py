# LeetCode
# 3494. Find the Minimum Amount Of Time to Brew Potions / Medium
# Time: O(n * m), Space: O(1)

class Solution:
    def minTimeToBrewPotions(self, skill: list[int], mana: list[int]) -> int:
        n, m = len(skill), len(mana)
        total_skill = sum(skill)
        prev_done = total_skill * mana[0]  # time when first potion is done

        for j in range(1, m):
            potion_time = prev_done
            # Adjust backward to simulate overlapping pipelines
            for i in range(n - 2, -1, -1):
                potion_time -= skill[i + 1] * mana[j - 1]
                prev_done = max(potion_time, prev_done - skill[i] * mana[j])
            prev_done += total_skill * mana[j]

        return prev_done
