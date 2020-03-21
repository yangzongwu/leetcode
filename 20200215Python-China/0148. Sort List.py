'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p_slow=head
        p_fast=head
        while p_fast.next and p_fast.next.next:
            p_slow=p_slow.next
            p_fast=p_fast.next.next
        
        p2=self.sortList(p_slow.next)
        p_slow.next=None
        p1=self.sortList(head)

        return self.mergeTwoSortedList(p1,p2)

    def mergeTwoSortedList(self,l1,l2):
        node=ListNode(0)
        p=node
        while l1 and l2:
            if l1.val<l2.val:
                p.next=l1
                l1=l1.next
            else:
                p.next=l2
                l2=l2.next
            p=p.next
        
        if l1:
            p.next=l1
        if l2:
            p.next=l2

        return node.next


