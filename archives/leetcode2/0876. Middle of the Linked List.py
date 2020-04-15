# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow.next
