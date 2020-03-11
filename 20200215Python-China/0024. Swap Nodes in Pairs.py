'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node=ListNode(0)
        p=node
        p.next=head

        while p.next and p.next.next:
            l1=p.next.next.next
            cur=p.next
            p.next=p.next.next
            p.next.next=cur
            cur.next=l1
            p=p.next.next
        
        return node.next
