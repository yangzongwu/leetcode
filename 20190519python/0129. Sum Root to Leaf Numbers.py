# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.sumOfNumbers(root,0)
 
    def sumOfNumbers(self,root,res):
        if not root:
            return 0
        if not root.left and not root.right:
            return res*10+root.val
        return self.sumOfNumbers(root.left,10*res+root.val)+self.sumOfNumbers(root.right,10*res+root.val)
