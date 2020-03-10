'''
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        root_list=[root]
        res=root.val
        while root_list:
            len_root_list=len(root_list)
            res=root_list[0].val
            for _ in range(len_root_list):
                cur=root_list.pop(0)
                if cur.left:
                    root_list.append(cur.left)
                if cur.right:
                    root_list.append(cur.right)
        return res
