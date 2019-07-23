# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if not root.left:
            root.right=self.flatten(root.right)
        else:
            node=root
            cur_right=self.flatten(node.right)
            node.right=self.flatten(node.left)
            node.left=None
            while node.right:
                node=node.right
            node.right=cur_right
        return root
