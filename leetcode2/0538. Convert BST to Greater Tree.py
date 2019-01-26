# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.flag=0
        
        def subconvertBST(root):
            if not root:return
            subconvertBST(root.right)
            root.val+=self.flag
            self.flag=root.val
            subconvertBST(root.left)
            
        subconvertBST(root)
        
        return root
