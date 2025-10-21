# LeetCode
# 3346. Maximum Frequency of Element After Performing Operation / Medium

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxi=max(nums)
        pre=[0]*(maxi+1)
        prev=ans=0
        for i in nums:
            pre[i]+=1
        cur=sum(pre[:k])
        for num in range(maxi+1):
            cur-=pre[num]
            if num+k<=maxi:
                cur+=pre[num+k]
            if num>0:
                prev+=pre[num-1]
            if num>k+1:
                prev-=pre[num-k-1]
            ans=max(ans,pre[num]+min(numOperations,prev+cur))
        return ans