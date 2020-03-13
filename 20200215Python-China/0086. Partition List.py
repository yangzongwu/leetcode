'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node1,node2=ListNode(0),ListNode(0)
        p_larger,p_small=node1,node2
        node1.next,node2.next=head,head
        while head:
            if head.val<x:
                p_small.next=head
                head=head.next
                p_small=p_small.next
            else:
                p_larger.next=head
                head=head.next
                p_larger=p_larger.next
        p_larger.next=None
        p_small.next=node1.next
        return node2.next
