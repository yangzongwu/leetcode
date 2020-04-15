# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        node=ListNode(0)
        p=node
        while l1 and l2:
            if l1.val<l2.val:
                p.next=l1
                p=p.next
                l1=l1.next
            else:
                p.next=l2
                p=p.next
                l2=l2.next
        if not l1:
            p.next=l2
        if not l2:
            p.next=l1
        return node.next
        
