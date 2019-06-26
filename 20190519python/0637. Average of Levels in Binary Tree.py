# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        rep=[]
        if not root:
            return rep
        
        root_list=[root]
        while root_list:
            len_root_list=len(root_list)
            cur_sum=0
            for k in range(len_root_list):
                cur_root=root_list.pop(0)
                cur_sum+=cur_root.val
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
            rep.append(cur_sum/len_root_list)
        return rep
