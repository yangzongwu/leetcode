# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.flag=0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        def dfs(root):
            if not root:
                return
            if root.right:
                dfs(root.right)
            root.val+=self.flag
            self.flag=root.val
            if root.left:
                dfs(root.left)
        dfs(root)
        
        
        
        return root
            
            
            
            
            
            
