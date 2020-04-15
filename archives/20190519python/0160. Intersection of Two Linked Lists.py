# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA=headA
        pB=headB
        while pA and pB:
            pA=pA.next
            pB=pB.next
        
        if pA:
            while pA:
                pA=pA.next
                headA=headA.next
            while headA:
                if headA==headB:
                    return headA
                else:
                    headA=headA.next
                    headB=headB.next
        if pB:
            while pB:
                pB=pB.next
                headB=headB.next
            while headB:
                if headA==headB:
                    return headA
                else:
                    headA=headA.next
                    headB=headB.next
        if not pA and not pB:
            while headA:
                if headA==headB:
                    return headA
                else:
                    headA=headA.next
                    headB=headB.next
            
