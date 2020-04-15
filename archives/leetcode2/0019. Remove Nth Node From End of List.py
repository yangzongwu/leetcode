# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node=ListNode(0)
        node.next=head
        p1,p2=node,node
        for _ in range(n):
            p1=p1.next
        while p1.next:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return node.next
