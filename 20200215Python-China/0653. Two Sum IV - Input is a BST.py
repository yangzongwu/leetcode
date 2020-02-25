'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        root_list=[]
        self.treeToList(root,root_list)
        left=0
        right=len(root_list)-1
        while left<right:
            if root_list[left]+root_list[right]==k:
                return True
            elif root_list[left]+root_list[right]>k:
                right-=1
            else:
                left+=1
        return False

    def treeToList(self,root,rep):
        if not root:
            return 
        self.treeToList(root.left,rep)
        rep.append(root.val)
        self.treeToList(root.right,rep)
