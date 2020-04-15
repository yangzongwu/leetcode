# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.stack=set()
        
        def subfindtwoSum(root,k):
            if not root:
                return False
            if k-root.val not in self.stack:
                self.stack.add(root.val)
                return subfindtwoSum(root.left,k) or subfindtwoSum(root.right,k)
            else:
                return True
        return subfindtwoSum(root,k)
