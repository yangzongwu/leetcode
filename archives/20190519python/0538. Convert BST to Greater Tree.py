# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.ans=0
        
        def subconvertBST(root):
            if not root:
                return
            subconvertBST(root.right)
            root.val+=self.ans
            self.ans=root.val
            subconvertBST(root.left)
            
        subconvertBST(root)
        return root
