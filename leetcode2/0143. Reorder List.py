# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            node=ListNode(0)
            node.next=head
            pslow,pfast=node,node
            while pfast and pfast.next and pfast.next.next:
                pslow=pslow.next
                pfast=pfast.next.next
            pright=pslow.next
            pslow.next=None
            pleft=node.next
        
            pright=self.reserve(pright)
        
            self.merge(head,pright)
    
    def reserve(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
    
    def merge(self,l1,l2):
        if l2:     
            node=ListNode(0)
            p=node
            while l1 and l2:
                p.next=l1
                p=p.next
                l1=l1.next
                p.next=l2
                p=p.next
                l2=l2.next
            if l1:
                p.next=l1
