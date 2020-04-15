# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_list_root=[]
        right_list_root=[root]
        rep=0
        while right_list_root or left_list_root:
            len_right_list_root=len(right_list_root)
            len_left_list_root=len(left_list_root)
            for _ in range(len_right_list_root):
                cur_root=right_list_root.pop(0)
                if cur_root.left:
                    left_list_root.append(cur_root.left)
                if cur_root.right:
                    right_list_root.append(cur_root.right)
            for _ in range(len_left_list_root):
                cur_root=left_list_root.pop(0)
                if not cur_root.left and not cur_root.right:
                    rep+=cur_root.val
                else:
                    if cur_root.left:
                        left_list_root.append(cur_root.left)
                    if cur_root.right:
                        right_list_root.append(cur_root.right)
        return rep
