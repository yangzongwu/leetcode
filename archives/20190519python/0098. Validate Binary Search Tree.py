# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_validBST(-2**31-1,root,2**31)
    
    def is_validBST(self,min_value,root,max_value):
        if not root:
            return True
        return min_value<root.val<max_value and self.is_validBST(min_value,root.left,root.val) and self.is_validBST(root.val,root.right,max_value)
