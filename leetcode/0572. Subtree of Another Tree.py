'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node 
values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's 
descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        if self.isSameTree(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def isSameTree(self,s,t):
        if not s and not t:
            return True
        if not s and t:
            return False
        if not t and s:
            return False
        return s.val==t.val and self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)
        
        
