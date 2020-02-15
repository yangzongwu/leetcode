# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        rep=[]
        root_list=[root]
        while root_list:
            len_of_root_list=len(root_list)
            cur_list=[]
            for i in range(len_of_root_list):
                cur_root=root_list.pop(0)
                cur_list.append(cur_root.val)
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
            rep.insert(0,cur_list)
        return rep
        
