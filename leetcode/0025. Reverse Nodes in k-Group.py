'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number 
of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p=ListNode(0)
        p.next=head
        p1=p
        i=0
        while i<k and p1.next:
            p1=p1.next
            i+=1
        if i<k:
            return head
        else:
            prev=self.reverseKGroup(p1.next,k)
            while k>0:
                cur=head
                head=head.next
                cur.next=prev
                prev=cur
                k-=1
            return prev
        
        
