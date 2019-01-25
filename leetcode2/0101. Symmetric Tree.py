# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif root.left and not root.right:
            return False
        elif not root.left and root.right:
            return False
        else:
            return self.sub_isSymmetric(root.left,root.right)
        
    def sub_isSymmetric(self,rootA,rootB):
        if not rootA and not rootB:
            return True
        elif rootA and not rootB:
            return False
        elif not rootA and rootB:
            return False
        else:
            if rootA.val!=rootB.val:
                return False
            else:
                return self.sub_isSymmetric(rootA.left,rootB.right) and self.sub_isSymmetric(rootA.right,rootB.left)
