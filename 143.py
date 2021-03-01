# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def helper(head, n):
            if n == 1:
                outTail = head.next
                head.next = None
                return outTail
            if n == 2:
                outTail = head.next.next
                head.next.next = None
                return outTail
            tail = helper(head.next, n - 2)
            outTail = tail.next
            tail.next = head.next
            head.next = tail
            return outTail
        if not head or not head.next or not head.next:
            return
        n = 0
        p = head
        while p:
            p = p.next
            n+=1
        helper(head, n)
