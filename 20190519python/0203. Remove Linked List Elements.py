# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node=ListNode(0)
        node.next=head
        p=node
        while p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return node.next
