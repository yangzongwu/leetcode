# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif not root.left and root.right:
            return self.height(root.right)<=1
        elif root.left and not root.right:
            return self.height(root.left)<=1
        else:
            return abs(self.height(root.right)-self.height(root.left))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self,root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
