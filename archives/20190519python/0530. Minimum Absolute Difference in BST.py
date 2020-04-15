# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        rep=[]
        self.tree_to_list(root,rep)
        
        result=rep[1]-rep[0]
        for k in range(len(rep)-1):
            result=min(result,rep[k+1]-rep[k])
        return result
    
    def tree_to_list(self,root,rep):
        if not root:
            return
        
        self.tree_to_list(root.left,rep)
        rep.append(root.val)
        self.tree_to_list(root.right,rep)
