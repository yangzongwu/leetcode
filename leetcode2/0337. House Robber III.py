# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: 'TreeNode') -> 'int':
        
        #rob_root = max(rob_L + rob_R , no_rob_L + no_nob_R + root.val)
        #no_rob_root = rob_L + rob_R
        
        def dfs(root):
            if not root:
                return 0,0
            root_l,non_root_l=dfs(root.left)
            root_r,non_root_r=dfs(root.right)
            return max(root_l+root_r,non_root_l+non_root_r+root.val),root_l+root_r
        return max(dfs(root))
        
        
