# LettCode
# 28. Find the Index of the First Occurrence in a String / Easy
# Time: O(n * m), Space: O(1)

class Solution(object):
    def strStr(self, haystack, needle):

        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

