# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node=ListNode(0)
        node.next=head
        pslow=node
        pfast=node
        while pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
        return pslow.next
