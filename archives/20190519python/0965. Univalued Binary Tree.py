# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.sub_isUnivalTree(root,root.val)
    
    def sub_isUnivalTree(self,root,target):
        if not root:
            return True
        return root.val==target and self.sub_isUnivalTree(root.left,target) and self.sub_isUnivalTree(root.right,target)
