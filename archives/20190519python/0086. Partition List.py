# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node_left,node_right=ListNode(0),ListNode(0)
        p_left,p_right=node_left,node_right
        while head:
            if head.val<x:
                p_left.next=head 
                p_left=p_left.next
            else:
                p_right.next=head
                p_right=p_right.next
            head=head.next
            
        p_right.next=None
        p_left.next=node_right.next
        return node_left.next
