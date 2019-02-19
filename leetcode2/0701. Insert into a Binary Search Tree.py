# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        if val<root.val:
            if not root.left:
                root.left=TreeNode(val)
            else:
                root.left=self.insertIntoBST(root.left,val)
        else:# val>root.val:
            if not root.right:
                root.right=TreeNode(val)
            else:
                root.right=self.insertIntoBST(root.right,val)
        return root
