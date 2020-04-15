# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        def subflatten(root):
            if not root:
                return None
            rightroot=subflatten(root.right)
            root.right=subflatten(root.left)
            root.left=None
            
            cur=root
            while cur.right:
                cur=cur.right
            cur.right=rightroot
            return root
        
        subflatten(root)
