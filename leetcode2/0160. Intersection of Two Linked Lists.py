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
        if not headA or not headB:
            return None
        pA=headA
        pB=headB
        while pA and pB:
            if pA==pB:
                return pA
            else:
                pA=pA.next
                pB=pB.next
        if pA and not pB:
            pAA=headA
            while pA:
                pA=pA.next
                pAA=pAA.next
            pBB=headB
            while pAA:
                if pAA==pBB:
                    return pAA
                else:
                    pAA=pAA.next
                    pBB=pBB.next
            return None
        elif pB and not pA:
            pBB=headB
            while pB:
                pB=pB.next
                pBB=pBB.next
            pAA=headA
            while pBB:
                if pAA==pBB:
                    return pAA
                else:
                    pAA=pAA.next
                    pBB=pBB.next
            return None
        else:
            return None
