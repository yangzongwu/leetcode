'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p=ListNode(0)
        p.next=head
        tmp=p
        while tmp and tmp.next and tmp.next.val<x:
            tmp=tmp.next
        if not tmp.next:
            return head
        cur=tmp
        newhead=cur.next
        while cur.next:
            if cur.next.val<x:
                tmp.next=cur.next
                cur.next=cur.next.next
                tmp=tmp.next
            else:
                cur=cur.next
        tmp.next=newhead
        return p.next
