'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node=ListNode(0)
        p=node
        p.next=head
        while p.next and p.next.next:
            if p.next.val==p.next.next.val:
                cur=p.next
                while cur and cur.next and cur.val==cur.next.val:
                    cur=cur.next
                if cur and not cur.next:
                    cur.next=None
                p.next=cur.next
            else:
                p=p.next
        return node.next
