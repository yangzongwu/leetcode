'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p=ListNode(0)
        p.next=head
        tmp=p
        while tmp.next:
            if tmp.next.val==val:
                tmp.next=tmp.next.next
            else:
                tmp=tmp.next
        return p.next
