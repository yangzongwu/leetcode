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
            return 
        
        self.prev=None
        def subflatten(root):
            if not root:
                return None
            subflatten(root.right)
            subflatten(root.left)
            root.right=self.prev
            root.left=None
            self.prev=root
            
        subflatten(root)
