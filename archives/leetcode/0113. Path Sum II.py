'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return[]
        
        rep=[]
        self.subpathSum(root,sum,rep,[])
        return rep
        
    def subpathSum(self,root,target,rep,tmp):
        if not root.left and not root.right:
            if target==root.val:
                rep.append(tmp+[root.val])
        else:
            if root.left:
                self.subpathSum(root.left,target-root.val,rep,tmp+[root.val])
            if root.right:
                self.subpathSum(root.right,target-root.val,rep,tmp+[root.val])
