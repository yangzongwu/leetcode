# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node=ListNode(0)
        node.next=head
        pslow=node
        pfast=node
        while pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
        if pfast.next:
            pslow=pslow.next
            
        p2=self.reverseList(pslow.next)
        pslow.next=None
        p1=node.next
        
        self.mergeList(head,p2)
    
    def reverseList(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
    
    def mergeList(self,l1,l2):
        node=ListNode(0)
        p=node
        while l2:
            p.next=l1
            l1=l1.next
            p=p.next
            p.next=l2
            p=p.next
            l2=l2.next
        if l1:
            p.next=l1
            l1=l1.next
            p=p.next
