# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None(
#         self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if n==0:
            return []
        return self.subcreateTree(1,n+1)
    
    def subcreateTree(self,start,end):
        if start==end:
            return [None]
        rep=[]
        for i in range(start,end):
            root_left=self.subcreateTree(start,i)
            root_right=self.subcreateTree(i+1,end)
            for l in root_left:
                for r in root_right:
                    newroot=TreeNode(i)
                    newroot.left=l
                    newroot.right=r
                    rep.append(newroot)
        return rep
                    
        
        
        
