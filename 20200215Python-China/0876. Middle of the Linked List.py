# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        pslow=head
        pfast=head
        
        while pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
        
        if pfast.next:
            return pslow.next
        return pslow
