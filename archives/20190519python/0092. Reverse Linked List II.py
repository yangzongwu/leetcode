# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        node=ListNode(0)
        node.next=head
        p=node
        while m>1:
            p=p.next
            m-=1
            n-=1
        
        p.next=self.reverseToN(p.next,n)
        return node.next
    
    def reverseToN(self,head,n):
        cur=head
        while n>1:
            cur=cur.next
            n-=1
        
        prev=cur.next
        cur.next=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
        
