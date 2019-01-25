# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        rep=[]
        list_root=[root]
        tmp=[root.val]
        while list_root:
            rep.append(tmp)
            tmp=[]
            len_list_root=len(list_root)
            for _ in range(len_list_root):
                cur_root=list_root.pop(0)
                if cur_root.left:
                    list_root.append(cur_root.left)
                    tmp.append(cur_root.left.val)
                if cur_root.right:
                    list_root.append(cur_root.right)
                    tmp.append(cur_root.right.val)
        return rep[::-1]
