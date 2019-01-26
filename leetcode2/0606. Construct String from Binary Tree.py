# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val)
        if t.left and not t.right:
            return str(t.val)+'('+self.tree2str(t.left)+')'
        if not t.left and t.right:
            return str(t.val)+'()'+'('+self.tree2str(t.right)+')'
        else:
            return str(t.val)+'('+self.tree2str(t.left)+')'+'('+self.tree2str(t.right)+')'
