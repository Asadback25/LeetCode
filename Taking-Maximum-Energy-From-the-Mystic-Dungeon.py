# LeetCode
# 3147. Taking Maximum Energy From the Mystic Dungeon / Medium
# Time: O(n), Space: O(1)

class Solution(object):
    def maximumEnergy(self, energy, k):

        new_energy = -float('inf')
        n = len(energy)

        for i in range(n - k, n):
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                new_energy = max(new_energy, total)
                j -= k
        return new_energy
