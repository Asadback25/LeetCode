# LeetCode
# 3217. Delete Nodes From Linked List Present in Array / Easy
# Time: O(n), Space: O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)

        newHead = ListNode(-1, head)
        curr = newHead

        while curr.next is not None:
            if curr.next.val in s:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return newHead.next