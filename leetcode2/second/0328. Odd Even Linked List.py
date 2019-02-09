# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddnode,evennode=ListNode(0),ListNode(0)
        podd,peven=oddnode,evennode
        while head and head.next:
            podd.next=head
            peven.next=head.next
            podd=podd.next
            peven=peven.next
            head=head.next.next
        if head:
            podd.next=head
            podd=podd.next
        peven.next=None
        podd.next=evennode.next
        return oddnode.next
