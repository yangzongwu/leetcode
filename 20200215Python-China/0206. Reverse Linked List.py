# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        res=self.reverseList(head.next)
        cur=head
        cur.next=None
        
        p=res
        while p.next:
            p=p.next
        p.next=cur
        
        return res
