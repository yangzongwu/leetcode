# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node=ListNode(0)
        node.next=head
        pFast,pSlow=node,node
        while pFast.next and pFast.next.next:
            pFast=pFast.next.next
            pSlow=pSlow.next
            if pFast==pSlow:
                return True
        return False
