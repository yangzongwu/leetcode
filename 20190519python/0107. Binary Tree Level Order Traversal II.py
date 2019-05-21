# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        rep=[]
        root_list=[root]
        while root_list:
            cur_list=[]
            len_of_rootList=len(root_list)
            for x in range(len_of_rootList):
                cur_root=root_list.pop(0)
                cur_list.append(cur_root.val)
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
            rep.append(cur_list)
        rep.reverse()
        return rep
