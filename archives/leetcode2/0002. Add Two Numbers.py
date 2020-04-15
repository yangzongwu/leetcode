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
        if not l1:
            return l2
        if not l2:
            return l1
        
        node=ListNode(0)
        p=node
        
        flag=0
        while l1 and l2:
            if l1.val+l2.val+flag>9:
                p.next=ListNode(l1.val+l2.val+flag-10)
                flag=1
            else:
                p.next=ListNode(l1.val+l2.val+flag)
                flag=0
            p=p.next
            l1=l1.next
            l2=l2.next
        if flag==0:
            if l1:
                p.next=l1
            if l2:
                p.next=l2
        else:
            while l1:
                if l1.val+flag>9:
                    p.next=ListNode(l1.val+flag-10)
                    flag=1
                else:
                    p.next=ListNode(l1.val+flag)
                    flag=0
                p=p.next
                l1=l1.next
            while l2:
                if l2.val+flag>9:
                    p.next=ListNode(l2.val+flag-10)
                    flag=1
                else:
                    p.next=ListNode(l2.val+flag)
                    flag=0
                p=p.next
                l2=l2.next
        if flag==1:
            p.next=ListNode(1)
        return node.next
