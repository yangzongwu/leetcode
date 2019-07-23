# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        rep=[]
        self.getPathSum(root,sum,[],rep)
        return rep
    
    def getPathSum(self,root,target,res,rep):
        if not root.left and not root.right:
            if target==root.val:
                rep.append(res+[root.val])
        elif root.left and not root.right:
            self.getPathSum(root.left,target-root.val,res+[root.val],rep)
        elif not root.left and root.right:        
            self.getPathSum(root.right,target-root.val,res+[root.val],rep)
        else:
            self.getPathSum(root.left,target-root.val,res+[root.val],rep)
            self.getPathSum(root.right,target-root.val,res+[root.val],rep)
