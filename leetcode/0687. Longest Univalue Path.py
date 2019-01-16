'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0
        self.res = 0
        self.getPath(root)
        return self.res
    
    def getPath(self, root):
        if not root: 
            return 0
        left = self.getPath(root.left)
        right = self.getPath(root.right)
        pl, pr = 1, 1
        if root.left and root.left.val == root.val: 
            pl = 1 + left
        if root.right and root.right.val == root.val: 
            pr = 1 + right
        self.res = max(self.res, pl + pr-2)
        return max(pl, pr)
