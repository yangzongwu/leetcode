'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if head and not head.next:
            return TreeNode(head.val)

        node_slow,node_fast=ListNode(0),ListNode(0)
        p_slow,p_fast=node_slow,node_fast
        node_slow.next,node_fast.next=head,head
        while p_fast.next and p_fast.next.next:
            p_slow=p_slow.next
            p_fast=p_fast.next.next
        root=TreeNode(p_slow.next.val)
        root.right=self.sortedListToBST(p_slow.next.next)
        p_slow.next=None
        root.left=self.sortedListToBST(head)
        return root  
