# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),self.heightOfTree(root.left)+self.heightOfTree(root.right))
    
    def heightOfTree(self,root):
        if not root:
            return 0
        return 1+max(self.heightOfTree(root.left),self.heightOfTree(root.right))
                   
