# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSum(root.left,sum)+self.pathSum(root.right,sum)+self.nodePathSum(root,sum)
    
    def nodePathSum(self,root,sum):
        rep=0
        if not root:
            return 0
        if root.val==sum:
            rep+=1
        return rep+self.nodePathSum(root.left,sum-root.val)+self.nodePathSum(root.right,sum-root.val)
        
        
        
