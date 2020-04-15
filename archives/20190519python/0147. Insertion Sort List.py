# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node=ListNode(0)
        node.next=head
        p=node
        while p.next and p.next.next:
            if p.next.val<=p.next.next.val:
                p=p.next
            else:
                cur=p.next.next
                p.next.next=cur.next
                #p=p.next
                tmp=node
                while tmp.next.val<cur.val:
                    tmp=tmp.next
                cur.next=tmp.next
                tmp.next=cur
        return node.next
