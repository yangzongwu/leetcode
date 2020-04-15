# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        k=len(nums)//2
        root=TreeNode(nums[k])
        root.left=self.sortedArrayToBST(nums[:k])
        root.right=self.sortedArrayToBST(nums[k+1:])
        return root
