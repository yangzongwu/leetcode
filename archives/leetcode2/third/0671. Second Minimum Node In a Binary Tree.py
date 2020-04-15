# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left:
            return -1
        flag=root.val
        rep=2**31
        root_list=[root]
        while root_list:
            cur_root=root_list.pop()
            if flag<cur_root.val<rep:
                rep=cur_root.val
            if cur_root.left:
                root_list.append(cur_root.left)
                root_list.append(cur_root.right)
        if rep==2**31:
            return -1
        else:
            return rep
                
