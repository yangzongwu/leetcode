# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        root_list=[root]
        cnt=0
        while root_list:
            cnt+=1
            len_root_list=len(root_list)
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                if not cur_root.left and not cur_root.right:
                    return cnt
                else:
                    if cur_root.left:
                        root_list.append(cur_root.left)
                    if cur_root.right:
                        root_list.append(cur_root.right)
                    
