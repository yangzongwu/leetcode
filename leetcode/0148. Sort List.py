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
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pslow=head
        pfast=head
        while pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
        cur=pslow.next
        pslow.next=None
        
        return self.mergeTwoSortedList(self.sortList(head),self.sortList(cur))
    
    def mergeTwoSortedList(self,headA,headB):
        node=ListNode(0)
        cur=node
        while headA and headB:
            if headA.val<headB.val:
                cur.next=headA
                headA=headA.next
            else:
                cur.next=headB
                headB=headB.next
            cur=cur.next
        if headA:
            cur.next=headA
        if headB:
            cur.next=headB
        return node.next
