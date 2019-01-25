# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #1-2-2-1
        #1-2-3-2-1
        if not head or not head.next:
            return True
        slow=head
        fast=head.next
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        newhead=self.reverse(slow.next)
        
        while newhead:
            if newhead.val!=head.val:
                return False
            newhead=newhead.next
            head=head.next
        return True
    
    def reverse(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
