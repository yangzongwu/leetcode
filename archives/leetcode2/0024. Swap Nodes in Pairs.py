# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=ListNode(0)
        node.next=head
        p=node
        while p and p.next and p.next.next:
            tmp=p.next
            tmp2=p.next.next
            tmp.next=tmp2.next
            tmp2.next=tmp
            p.next=tmp2
            p=p.next.next
        return node.next
            
            
