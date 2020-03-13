'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow-up:
Can you solve it without using extra space?

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        node_slow,node_fast=ListNode(0),ListNode(0)
        node_slow.next,node_fast.next=head,head
        p_slow,p_fast=node_slow,node_fast

        while p_fast.next and p_fast.next.next:
            p_fast=p_fast.next.next
            p_slow=p_slow.next
            if p_slow==p_fast:
                break
        if not p_fast.next or not p_fast.next.next:
            return None
        
        node_cur=ListNode(0)
        node_cur.next=head
        p_cur=node_cur
        while p_fast!=p_cur:
            p_cur=p_cur.next
            p_fast=p_fast.next
        return p_fast

