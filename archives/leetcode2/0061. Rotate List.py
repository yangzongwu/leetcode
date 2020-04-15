# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or not head:
            return head
        p=head
        
        len_head=0
        while p:
            p=p.next
            len_head+=1
            
        k=k%len_head
        
        if k==0:
            return head
        
        node=ListNode(0)
        node.next=head
        p1=node
        for _ in range(len_head-k):
            p1=p1.next
        cur=p1.next
        p1.next=None
        
        p2=cur
        while p2.next:
            p2=p2.next
        p2.next=head
        
        return cur
