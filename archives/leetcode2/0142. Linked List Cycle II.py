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
        
        node=ListNode(0)
        node.next=head
        pslow,pfast=node,node
        while pfast and pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
            if pslow==pfast:
                pslow=node
                while pslow!=pfast:
                    pslow=pslow.next
                    pfast=pfast.next
                return pslow
        return None
