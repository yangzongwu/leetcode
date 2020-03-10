'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        rep=[]
        root_list=[root]
        while root_list:
            len_root_list=len(root_list)
            res=root_list[0].val
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                res=max(res,cur_root.val)
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
            rep.append(res)
        return rep
