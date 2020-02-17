'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        rep=0
        right_root=[root]
        left_root=[]
        while right_root or left_root:
            if right_root:
                cur_root=right_root.pop()
                if cur_root.left:
                    left_root.append(cur_root.left)
                if cur_root.right:
                    right_root.append(cur_root.right)
            if left_root:
                cur_root=left_root.pop()
                if not cur_root.left and not cur_root.right:
                    rep+=cur_root.val
                if cur_root.left:
                    left_root.append(cur_root.left)
                if cur_root.right:
                    right_root.append(cur_root.right)
        return rep
