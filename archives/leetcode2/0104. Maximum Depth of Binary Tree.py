# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cnt=0
        list_root=[root]
        while list_root:
            cnt+=1
            len_list_root=len(list_root)
            for _ in range(len_list_root):
                cur_root=list_root.pop(0)
                if cur_root.left:
                    list_root.append(cur_root.left)
                if cur_root.right:
                    list_root.append(cur_root.right)
        return cnt
