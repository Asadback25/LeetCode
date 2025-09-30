# LeetCode Questions
# 9. Palindrome Number / Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]