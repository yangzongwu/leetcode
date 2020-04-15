class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        node=ListNode(0)
        node.next=head
        p=node
        for _ in range(m-1):
            p=p.next
        p.next=self.reverse(p.next,n-m+1)
        return node.next
    def reverse(self,head,k):
        p=head
        for _ in range(k):
            p=p.next
        
        prev=p
        for _ in range(k):
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
