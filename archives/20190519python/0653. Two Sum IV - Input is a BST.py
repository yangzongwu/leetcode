# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        rep=[]
        self.root_to_list(root,rep)
        
        left,right=0,len(rep)-1
        while left<right:
            cur=rep[left]+rep[right]
            if cur==k:
                return True
            elif cur>k:
                right-=1
            else:
                left+=1
        return False
        
    def root_to_list(self,root,rep):
        if not root:
            return
        
        self.root_to_list(root.left,rep)
        rep.append(root.val)
        self.root_to_list(root.right,rep)
