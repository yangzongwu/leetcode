# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node=ListNode(0)
        node.next=head
        p1=node
        p11=p1
        node1=ListNode(0)
        node1.next=head
        p2=node1
        p22=p2
        while head:
            cur=head
            if cur.val<x:
                p1.next=cur
                p1=p1.next
            else:
                p2.next=cur
                p2=p2.next
            head=head.next
        p2.next=None
        p1.next=p22.next
        return p11.next
