# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None
        maxnum=max(nums)
        k=0
        while nums[k]!=maxnum:
            k+=1
        root=TreeNode(nums[k])
        root.left=self.constructMaximumBinaryTree(nums[:k])
        root.right=self.constructMaximumBinaryTree(nums[k+1:])
        return root
