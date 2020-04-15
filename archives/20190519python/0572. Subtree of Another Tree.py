# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
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
        if s and not t:
            return False
        return s.val==t.val and self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)
