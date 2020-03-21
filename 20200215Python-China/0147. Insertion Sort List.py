'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

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
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur=None
        while head:
            nexthead=head.next
            head.next=None
            cur=self.insertionHeadSortList(cur,head)
            head=nexthead
        return cur

    def insertionHeadSortList(self,headA,headB):
        if not headA:
            headA=headB
            headB.next=None
            return headA
        
        node=headA
        if headB.val<headA.val:
            headB.next=headA
            return headB
        while headA.next and headB.val>headA.next.val:
            headA=headA.next
        cur=headA.next
        headA.next=headB
        headB.next=cur
        return node
