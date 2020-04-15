# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if not root.left and not root.right:
            return root
        if not root.left and root.right:
            root.right=self.increasingBST(root.right)
            return root
        
        newroot=self.increasingBST(root.left)
        p=newroot
        while p.right:
            p=p.right
        p.right=root
        p=p.right
        
        p.left=None
        p.right=self.increasingBST(root.right)
        return newroot
        
