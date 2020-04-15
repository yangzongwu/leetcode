# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        if root.right:
            self.bstToGst(root.right)
            
            cur=root.right
            while cur.left:
                cur=cur.left
            root.val+=cur.val
            
        if root.left:
            cur=root.left
            while cur.right:
                cur=cur.right
            cur.val+=root.val
            self.bstToGst(root.left)
        return root
            
