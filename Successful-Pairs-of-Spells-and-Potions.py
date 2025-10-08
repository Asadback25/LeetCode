# LeetCode
# 2300. Successful Pairs of Spells and Potions / Medium

class Solution(object):
    def successfulPairs(self, spells, potions, success):

        potions.sort()
        n = len(potions)
        res = []

        for spell in spells:
            min_need = (success + spell -1) // spell

            l, r = 0, n - 1
            x = n
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] >= min_need:
                    x = mid
                    r = mid - 1
                else:
                    l = mid + 1
            res.append(n - x)
        return res