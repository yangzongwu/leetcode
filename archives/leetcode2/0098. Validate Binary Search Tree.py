# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return self.subIsVlidBST(root,-2**31-1,2**31)
        
        
    def subIsVlidBST(self,root,left1,right1):
        if not root:
            return True
        return left1<root.val<right1 and self.subIsVlidBST(root.left,left1,root.val) and self.subIsVlidBST(root.right,root.val,right1)
