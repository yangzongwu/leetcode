# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res=ListNode(0)
        res.next=head
        p=res
        while p.next and p.next.next:
            if p.next.val==p.next.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return res.next
