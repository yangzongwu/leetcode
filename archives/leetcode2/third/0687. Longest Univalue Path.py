# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.longestUnivaluePath(root.left),self.longestUnivaluePath(root.right),self.sublongestUnivaluePath(root.left,root.val)+ self.sublongestUnivaluePath(root.right,root.val))
    
    def sublongestUnivaluePath(self,root,target):
        if not root:
            return 0
        if root.val !=target:
            return 0
        else:
            return 1+max(self.sublongestUnivaluePath(root.left,target),self.sublongestUnivaluePath(root.right,target))
