'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        root_list=[root]
        rep=[]
        flag=True
        while root_list:
            len_root_list=len(root_list)
            res=[]
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                res.append(cur_root.val)
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
            if flag==True:
                rep.append(res)
                flag=False
            else:
                rep.append(res[::-1])
                flag=True
        return rep
