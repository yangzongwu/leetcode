# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if R<root.val:
            return self.trimBST(root.left,L,R)
        elif L>root.val:
            return self.trimBST(root.right,L,R)
        else:
            root.left=self.trimBST(root.left,L,root.val)
            root.right=self.trimBST(root.right,root.val,R)
            return root
