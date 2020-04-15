# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
     
        if not root:
            return False
        root_list=[root]
        root_sum=[root.val]
        while root_list:
            len_root_list=len(root_list)
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                cur_sum=root_sum.pop(0)
                if not cur_root.left and not cur_root.right:
                    if cur_sum==sum:
                        return True
                else:
                    if cur_root.left:
                        root_list.append(cur_root.left)
                        root_sum.append(cur_sum+cur_root.left.val)
                    if cur_root.right:
                        root_list.append(cur_root.right)
                        root_sum.append(cur_sum+cur_root.right.val)
        return False
                    
