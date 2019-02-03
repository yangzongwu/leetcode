# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=ListNode(0)
        node.next=head
        p=node
        while p and p.next and p.next.next:
            if p.next.val!=p.next.next.val:
                p=p.next
            else:
                while p.next.next and p.next.next.val==p.next.val:
                    p.next=p.next.next
                p.next=p.next.next
        return node.next
