'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)
        p.next=head
        tmp=p
        while tmp.next and tmp.next.next:
            if tmp.next.val!=tmp.next.next.val:
                tmp=tmp.next
            else:
                cur=tmp.next
                while cur.next and cur.next.next:
                    if cur.next.next.val==cur.val:
                        cur=cur.next
                    else:
                        tmp.next=cur.next.next
                        break
                else:
                    tmp.next=None
        return p.next
 ##############################################################
class Solution(object):
    def deleteDuplicates(self, head):
        p=ListNode(0)
        p.next=head
        tmp=p
        while tmp.next and tmp.next.next:
            if tmp.next.val!=tmp.next.next.val:
                tmp=tmp.next
            else:
                cur=tmp.next
                while cur.next and cur.next.next:
                    if cur.next.next.val==cur.val:
                        cur=cur.next
                    else:
                        break
                tmp.next=cur.next.next
        return p.next
            
