# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        rep=[]
        self.getValofTree(root,rep)
        res=rep[1]-rep[0]
        for i in range(1,len(rep)):
            res=min(res,rep[i]-rep[i-1])
        return res



    def getValofTree(self,root,rep):
        if root.left:
            self.getValofTree(root.left,rep)
        rep.append(root.val)
        if root.right:
            self.getValofTree(root.right,rep)


    
