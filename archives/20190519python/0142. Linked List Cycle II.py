# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        if not head or not head.next:
            return None
        
        pslow=head.next
        pfast=head.next.next
        while pfast and pfast.next and pfast.next.next and pslow!=pfast:
            pslow=pslow.next
            pfast=pfast.next.next
        
        if  not pfast or not pfast.next or not pfast.next.next:
            return None
        
        pslow=head
        while pslow!=pfast:
            pslow=pslow.next
            pfast=pfast.next
        return pslow
