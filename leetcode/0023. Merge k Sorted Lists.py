'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        list_lists=[]
        for l_list in lists:
            while l_list:
                list_lists.append(l_list.val)
                l_list=l_list.next
        list_lists.sort()
        p=ListNode(0)
        tmp=p
        for x in list_lists:
            tmp.next=ListNode(x)
            tmp=tmp.next
        return p.next
        
