# LeetCode
# 3347. Maximum Frequency of an Element After Performing Operations II / Hard
# Time: O(n log n)

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        N = len(nums)
        f = collections.Counter(nums)

        def go_on(x):
            lindex = bisect.bisect_left(nums, x - k)
            rindex = bisect.bisect_right(nums, x + k)

            same = f[x]
            change = min((rindex - lindex) - f[x], numOperations)
            return same + change

        events = []

        for x in nums:
            events.append(x)
            events.append(x - k)
            events.append(x + k)

        nums.sort()

        best = 0
        for i in sorted(set(events)):
            best = max(best, go_on(i))

        return best