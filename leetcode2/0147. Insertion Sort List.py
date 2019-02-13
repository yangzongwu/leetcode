# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        node=ListNode(0)
        node.next=head
        p=node
        
        while p.next and p.next.next:
            if p.next.val<=p.next.next.val:
                p=p.next
            else:
                tmp1=p.next
                tmp2=p.next.next
                tmp1.next=tmp2.next
                cur=node
                while cur.next.val<tmp2.val:
                    cur=cur.next
                tmp2.next=cur.next
                cur.next=tmp2
        return node.next
                
