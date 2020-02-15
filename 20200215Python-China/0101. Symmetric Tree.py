# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricTree(root.left,root.right)
    
    def isSymmetricTree(self,rootA,rootB):
        if not rootA and rootB:
            return False
        if rootA and not rootB:
            return False
        if not rootA and not rootB:
            return True
        return rootA.val==rootB.val and self.isSymmetricTree(rootA.left, rootB.right) and self.isSymmetricTree(rootA.right,rootB.left)
