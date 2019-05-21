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
        return self.pathSum(root.left,sum)+self.pathSum(root.right,sum)+self.pathRootToSum(root,sum)
    
    def pathRootToSum(self,root,sum):
        if not root:
            return 0
        if root.val==sum:
            return 1+self.pathRootToSum(root.left,sum-root.val)+self.pathRootToSum(root.right,sum-root.val)
        else:
            return self.pathRootToSum(root.left,sum-root.val)+self.pathRootToSum(root.right,sum-root.val)
