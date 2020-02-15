# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        deep=0
        root_list=[root]
        while root_list:
            deep+=1
            len_of_root_list=len(root_list)
            for i in range(len_of_root_list):
                cur_root=root_list.pop(0)
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
        return deep
