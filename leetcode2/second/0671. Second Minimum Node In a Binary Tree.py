# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        return self.findbigVal(root,root.val)
    
    def findbigVal(self,root,target):
        if not root:
            return -1
        if root.val!=target:
            return root.val
        if root.val==target:
            left=self.findbigVal(root.left,target)
            right=self.findbigVal(root.right,target)
            if left==-1 and right==-1:
                return -1
            elif left!=-1 and right==-1:
                return left
            elif left==-1 and right!=-1:
                return right
            else:
                return min(left,right)
                
