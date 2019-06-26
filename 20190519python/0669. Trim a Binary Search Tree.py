# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return root
        
        if L<=root.val<=R:
            root.left=self.trimBST(root.left,L,R)
            root.right=self.trimBST(root.right,L,R)
            return root
        elif root.val<L:
            return self.trimBST(root.right,L,R)
        else:
            return self.trimBST(root.left,L,R)
