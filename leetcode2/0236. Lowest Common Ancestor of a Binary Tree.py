# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p==root or q ==root:
            return root
        
        flag1=self.lowestCommonAncestor(root.left,p,q)
        flag2=self.lowestCommonAncestor(root.right,p,q)
        
        if flag1 and flag2:
            return root
        if flag1:
            return flag1
        if flag2:
            return flag2
