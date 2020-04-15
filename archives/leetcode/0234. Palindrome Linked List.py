'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p=ListNode(0)
        p.next=head
        p1=p
        p2=p
        while p2.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next
        if p2.next and not p2.next.next:
            p1=p1.next
        
        p1.next=self.reverse(p1.next)
        
        p0=p
        while p1.next:
            if p0.next.val==p1.next.val:
                p0=p0.next
                p1=p1.next
            else:
                return False
        return True
    
    def reverse(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
