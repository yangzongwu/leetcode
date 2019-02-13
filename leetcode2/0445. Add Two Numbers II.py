# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=0
        while l1:
            a=a*10+l1.val
            l1=l1.next
        b=0
        while l2:
            b=b*10+l2.val
            l2=l2.next
        rep=str(a+b)
        node=ListNode(0)
        p=node
        for s in rep:
            p.next=ListNode(int(s))
            p=p.next
        return node.next
