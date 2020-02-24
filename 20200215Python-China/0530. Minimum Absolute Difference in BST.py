'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        tree_list=[]
        self.treeToList(root,tree_list)
        gap=tree_list[1]-tree_list[0]
        for k in range(1,len(tree_list)):
            gap=min(gap,tree_list[k]-tree_list[k-1])
        return gap


    def treeToList(self,root,rep):
        if not root:
            return 
        if root.left:
            self.treeToList(root.left,rep)
        rep.append(root.val)
        self.treeToList(root.right,rep)
