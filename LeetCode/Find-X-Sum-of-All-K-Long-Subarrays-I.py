# LeetCode
# 3318. Find X-Sum of All K-Long Subarrays I / Easy

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)

        ans = []
        for i in range(n - k + 1):
            f = collections.Counter(nums[i:i + k])

            vs = list(sorted(f.items(), key=lambda x: (-x[1], -x[0])))[:x]
            total = sum(k * v for k, v in vs)
            ans.append(total)
        return ans