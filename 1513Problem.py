class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        l = -1  

        for i, ch in enumerate(s):
            if ch == '0':
                l = i
            ans = (ans + i - l) % MOD
        
        return ans
