# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.longestUnivaluePath(root.left),self.longestUnivaluePath(root.right),self.theSameValPath(root.left,root.val)+self.theSameValPath(root.right,root.val))
    
    def theSameValPath(self,root,target):
        if not root or root.val!=target:
            return 0
        return 1+max(self.theSameValPath(root.left,target),self.theSameValPath(root.right,target))
        
