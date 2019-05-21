# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSubSymmetric(root.left,root.right)
    
    def isSubSymmetric(self,rootA,rootB):
        if not rootA and not rootB:
            return True
        if rootA and not rootB:
            return False
        if not rootA and rootB:
            return False
        return rootA.val==rootB.val and self.isSubSymmetric(rootA.left,rootB.right) and self.isSubSymmetric(rootA.right,rootB.left)
        
