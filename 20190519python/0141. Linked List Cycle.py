# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        pslow=head
        pfast=head.next
        while pfast and pfast.next and pfast.next.next:
            if pslow!=pfast:
                pslow=pslow.next
                pfast=pfast.next.next
            else:
                return True
        return False
