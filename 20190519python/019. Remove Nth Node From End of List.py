# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==0:
            return head
        cur=head
        while n>0:
            cur=cur.next
            n-=1
        
        p=head
        if not cur:
            return head.next
        
        while cur.next:
            cur=cur.next
            p=p.next
        p.next=p.next.next
        
        return head
