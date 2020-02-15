# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val==head.next.val
        
        pslow=head
        pfast=head
        
        while pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
            
        return self.isSubList(head,pslow.next)
    
    
    def isSubList(self,headA,headB):
        headB=self.reverseList(headB)
        while headB:
            if headA.val!=headB.val:
                return False
            headA=headA.next
            headB=headB.next
        return True
        
        
        
    def reverseList(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
