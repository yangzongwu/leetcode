# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.rep=0
        self.cnt=0
        
        def readKthValue(root,k):
            if not root:
                return
        
            if root.left:
                readKthValue(root.left,k)
            self.cnt+=1
            if self.cnt==k:
                self.rep=root.val
                return
            if root.right:
                readKthValue(root.right,k)
                
        readKthValue(root,k)
        return self.rep
