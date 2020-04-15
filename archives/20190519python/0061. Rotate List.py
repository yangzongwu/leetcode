# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        len_list=0
        p=head
        while p:
            p=p.next
            len_list+=1    
        k=k%len_list
        
        if k==0:
            return head
        
        pfast=head
        while k>0:
            pfast=pfast.next
            k-=1
        pslow=head
        
        
        while pfast.next:
            pfast=pfast.next
            pslow=pslow.next
            
        newhead=pslow.next
        pslow.next=None
        
        cur=newhead
        while cur.next:
            cur=cur.next
        cur.next=head
        return newhead
