# LeetCode
# 14. Longest Common Refix / Easy
# Time: O(n + m), Space: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):

        result = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result