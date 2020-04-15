# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif val>=root.val:
            newroot=TreeNode(val)
            newroot.left=root
            return newroot
        else:
            root.right=self.insertIntoMaxTree(root.right,val)
            return root
