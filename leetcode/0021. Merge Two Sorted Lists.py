'''
Merge two sorted linked lists and return it as a new list. The new list should be made by 
splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
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
        p=ListNode(0)
        tmp=p
        while l1 and l2:
            if l1.val>l2.val:
                tmp.next=l2
                l2=l2.next
                tmp=tmp.next
            else:
                tmp.next=l1
                l1=l1.next
                tmp=tmp.next
        if l1:
            tmp.next=l1
        if l2:
            tmp.next=l2
        return p.next
