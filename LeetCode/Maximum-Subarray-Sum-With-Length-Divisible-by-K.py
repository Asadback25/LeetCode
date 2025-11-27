# LeetCode
# 3381. Maximum Subarray Sum With Length Divisible by K / Medium

class Solution:
  def maxSubarraySum(self, nums: list[int], k: int) -> int:
    ans = -math.inf
    prefix = 0
    minPrefix = [math.inf] * k
    minPrefix[k - 1] = 0

    for i, num in enumerate(nums):
      prefix += num
      ans = max(ans, prefix - minPrefix[i % k])
      minPrefix[i % k] = min(minPrefix[i % k], prefix)

    return ans