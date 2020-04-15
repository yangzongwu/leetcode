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
        node1,node2=ListNode(0),ListNode(1)
        p1,p2=node1,node2
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
                head=head.next
            else:
                p2.next=head
                p2=p2.next
                head=head.next
        p2.next=None
        p1.next=node2.next
        return node1.next
