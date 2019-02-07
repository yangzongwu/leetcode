# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        if not root:
            return []
        def dfs(root,target,res,rep):
            if not root.left and not root.right:
                if target==root.val:
                    rep.append(res+[root.val])
            else:
                if root.left:
                    dfs(root.left,target-root.val,res+[root.val],rep)
                if root.right:
                    dfs(root.right,target-root.val,res+[root.val],rep)
            
        rep=[]
        dfs(root,sum,[],rep)
        return rep
