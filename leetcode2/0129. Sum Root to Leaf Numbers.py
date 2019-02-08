# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        
        self.rep=0
        
        def dfs(root,res):
            if not root.left and not root.right:
                self.rep+=res*10+root.val
            else:
                if root.left:
                    dfs(root.left,res*10+root.val)
                if root.right:
                    dfs(root.right,res*10+root.val)
                
        dfs(root,0)
        return self.rep
