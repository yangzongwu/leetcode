# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        elif not root.left and root.right:
            root.right=self.increasingBST(root.right)
            return root
        else:# root.left:
            newroot=self.increasingBST(root.left)
            cur_root=newroot
            while cur_root.right:
                cur_root=cur_root.right
            root.left=None
            cur_root.right=self.increasingBST(root)
            return newroot
