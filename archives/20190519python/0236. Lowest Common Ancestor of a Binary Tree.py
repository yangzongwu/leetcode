# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root==p or root==q:
            return root
        
        flag1=self.lowestCommonAncestor(root.left,p,q)
        flag2=self.lowestCommonAncestor(root.right,p,q)
        
        if flag1 and flag2:
            return root
        elif flag1:
            return flag1
        elif flag2:
            return flag2
