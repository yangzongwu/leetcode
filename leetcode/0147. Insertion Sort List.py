'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs 
within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node=ListNode(0)
        node.next=head
        cur=node
        while cur.next and cur.next.next:
            if cur.next.val<=cur.next.next.val:
                cur=cur.next
            else:
                tmp1=cur.next
                tmp2=cur.next.next
                tmp1.next=tmp2.next
                newhead=node
                while newhead.next.val<tmp2.val:
                    newhead=newhead.next
                cur1=newhead.next
                newhead.next=tmp2
                tmp2.next=cur1 
        return node.next
                    
