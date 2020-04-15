'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
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
        p=ListNode(0)
        tmp=p
        flag=0
        while l1 and l2:
            if l1.val+l2.val+flag>9:
                tmp.next=ListNode(l1.val+l2.val+flag-10)
                flag=1
            else:
                tmp.next=ListNode(l1.val+l2.val+flag)
                flag=0
            tmp=tmp.next
            l1=l1.next
            l2=l2.next
        if flag==0:
            if l1:
                tmp.next=l1
            if l2:
                tmp.next=l2
        else:
            if l1 and not l2:
                tmp.next=self.addflagNumbers(l1,flag)
            if l2 and not l1:
                tmp.next=self.addflagNumbers(l2,flag)
            if not l1 and not l2:
                tmp.next=ListNode(1)
        return p.next
    
    def addflagNumbers(self,l,flag):
        p=ListNode(0)
        tmp=p
        while l:
            if flag==1:
                if l.val+flag>9:
                    tmp.next=ListNode(l.val+flag-10)
                    flag=1
                else:
                    tmp.next=ListNode(l.val+flag)
                    flag=0
                tmp=tmp.next
                l=l.next
            else:
                tmp.next=l
                return p.next
        if flag==1:
            tmp.next=ListNode(1)
        return p.next
##################second time#################################
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
        p=ListNode(0)
        newhead=p
        flag=0
        while l1 and l2:
            if l1.val+l2.val+flag>9:
                newhead.next=ListNode(l1.val+l2.val+flag-10)
                flag=1
            else:
                newhead.next=ListNode(l1.val+l2.val+flag)
                flag=0
            newhead=newhead.next
            l1=l1.next
            l2=l2.next
        while l1:
            if l1.val+flag>9:
                newhead.next=ListNode(l1.val+flag-10)
                flag=1
            else:
                newhead.next=ListNode(l1.val+flag)
                flag=0
            newhead=newhead.next
            l1=l1.next
        while l2:
            if l2.val+flag>9:
                newhead.next=ListNode(l2.val+flag-10)
                flag=1
            else:
                newhead.next=ListNode(l2.val+flag)
                flag=0
            newhead=newhead.next
            l2=l2.next
        if flag==1:
            newhead.next=ListNode(1)
        return p.next
