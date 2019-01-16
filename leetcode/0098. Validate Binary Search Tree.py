'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        minval=-2**31-1
        maxval=2**31+1
        return self.subIsValidBST(root,minval,maxval)
    def subIsValidBST(self,root,minval,maxval):
        if not root.left and not root.right:
            return True
        elif root.left and not root.right:
            return minval<root.left.val<root.val and self.subIsValidBST(root.left,minval,root.val)
        elif not root.left and root.right:
            return maxval>root.right.val>root.val and self.subIsValidBST(root.right,root.val,maxval)
        else:
            return minval<root.left.val<root.val<root.right.val<maxval and self.subIsValidBST(root.left,minval,root.val) and self.subIsValidBST(root.right,root.val,maxval)
