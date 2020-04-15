# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif not p and q:
            return False
        else:
            if p.val!=q.val:
                return False
            else:
                return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)
        
