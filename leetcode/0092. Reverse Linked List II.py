'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p=ListNode(0)
        p.next=head
        tmp=p
        while m>1:
            tmp=tmp.next
            m-=1
            n-=1
        tmp.next=self.reverseList(tmp.next,n)
        return p.next
    
    def reverseList(self,head,k):
        if k<=1:
            return head
        prev=None
        for k in range(k):
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
            
        tmp=prev
        while tmp.next:
            tmp=tmp.next
        tmp.next=head
        
        return prev
            
