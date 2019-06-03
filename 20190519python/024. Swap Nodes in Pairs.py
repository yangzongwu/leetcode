# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node=ListNode(0)
        node.next=head
        p=node
        while p.next and p.next.next:
            first=p.next
            second=p.next.next
            p.next=second
            first.next=second.next
            second.next=first
            
            p=p.next.next
        return node.next
            
            
            
