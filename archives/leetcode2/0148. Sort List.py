# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        node=ListNode(0)
        node.next=head
        p1=node
        p2=node
        while p2 and p2.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next
        l1=self.sortList(p1.next)
        p1.next=None
        l2=self.sortList(node.next)
        
        return self.mergeList(l1,l2)
    
    def mergeList(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        node=ListNode(0)
        p=node
        while l1 and l2:
            if l1.val<=l2.val:
                p.next=l1
                p=p.next
                l1=l1.next
            else:
                p.next=l2
                p=p.next
                l2=l2.next
        if l1:
            p.next=l1
        if l2:
            p.next=l2
        return node.next
