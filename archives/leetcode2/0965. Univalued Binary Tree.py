# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        root_list=[root]
        target=root.val
        while root_list:
            len_root_list=len(root_list)
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                if cur_root.val!=target:
                    return False
                else:
                    if cur_root.left:
                        root_list.append(cur_root.left)
                    if cur_root.right:
                        root_list.append(cur_root.right)
        return True
