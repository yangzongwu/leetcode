# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        else:
            rep=self.pathSum(root.left,sum)+self.pathSum(root.right,sum)+self.allPathSum(root,sum)
            return rep
        
    def allPathSum(self,root,target):
        if not root:
            return 0
        else:
            rep=0
            if target==root.val:rep+=1
            rep+=self.allPathSum(root.left,target-root.val)+self.allPathSum(root.right,target-root.val)
            return rep
