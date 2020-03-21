'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        node1,node2=ListNode(0),ListNode(0)
        p_slow,p_fast=node1,node2
        node1.next,node2.next=head,head
        while p_fast.next and p_fast.next.next:
            p_slow=p_slow.next
            p_fast=p_fast.next.next
        if p_fast.next:
            p_slow=p_slow.next

        p2=self.reserveList(p_slow.next)
        p_slow.next=None

        return self.mergeTwoSortedList(head,p2)

    def reserveList(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev

    def mergeTwoSortedList(self,l1,l2):
        node=l1
        while l2:
            cur=l1.next
            l1.next=l2
            l2=l2.next
            l1.next.next=cur
            l1=l1.next.next
        return node

            



