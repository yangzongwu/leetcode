# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Definition for a binary tree node.
        if not root:
            return 0
        cnt=0
        root_list=[root]
        while root_list:
            cnt+=1
            len_of_rootList=len(root_list)
            for x in range(len_of_rootList):
                cur_root=root_list.pop(0)
                if not cur_root.left and not cur_root.right:
                    return cnt
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
        return cnt
