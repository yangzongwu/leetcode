# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1=head
        p2=s_head=p1.next
        while p1.next and p1.next.next:
            cur=p1.next.next
            p2.next=cur.next
            p1.next=cur
            p2=p2.next
            p1=p1.next
        p1.next=s_head
        return head
        
