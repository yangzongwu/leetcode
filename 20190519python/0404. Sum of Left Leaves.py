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
        right_root_list=[root]
        left_root_list=[]
        rep=0
        while right_root_list or left_root_list:
            if right_root_list:
                cur_right_root=right_root_list.pop()
                if cur_right_root.left:
                    left_root_list.append(cur_right_root.left)
                if cur_right_root.right:
                    right_root_list.append(cur_right_root.right)
            if left_root_list:
                cur_left_root=left_root_list.pop()
                if not cur_left_root.left and not cur_left_root.right:
                    rep+=cur_left_root.val
                if cur_left_root.left:
                    left_root_list.append(cur_left_root.left)
                if cur_left_root.right:
                    right_root_list.append(cur_left_root.right)
        return rep
