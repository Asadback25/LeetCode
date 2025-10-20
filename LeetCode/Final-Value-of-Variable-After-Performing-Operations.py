# LeetCode
# 2011. Final Value fo Variable After Performing Operations / Easy

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = 0
        for i in operations:
            if i == 'X--' or i == '--X':
                s -= 1
            else:
                s += 1
        return s