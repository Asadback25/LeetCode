# LeetCode
# 1161. Maximum Level Sum of a Binary Tree / Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        ans = 0
        level = 0
        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            current_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                current_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < current_sum:
                max_sum = current_sum
                ans = level

        return ans