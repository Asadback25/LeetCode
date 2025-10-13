# LeetCode
# 2273. Find Result Array After Removing Anagrams / Easy
# Time: O(n), Space(1)

class Solution(object):
    def removeAnagrams(self, words):

        stack = []

        for word in words:
            stack.append(word)

            if len(stack) >= 2 and sorted(stack[-1]) == sorted(stack[-2]):
                stack.pop()

        return stack
