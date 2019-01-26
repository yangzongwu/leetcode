# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.tilt=0
        
        def sumOfTree(root):
            if not root:
                return 0
            left_sum=sumOfTree(root.left)
            right_sum=sumOfTree(root.right)
            self.tilt+=abs(left_sum-right_sum)
            root.val+=left_sum+right_sum
            return root.val
        
        sumOfTree(root)
        
        return self.tilt
