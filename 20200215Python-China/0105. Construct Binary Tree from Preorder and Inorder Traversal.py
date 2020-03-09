'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        target=preorder[0]
        k=0
        while inorder[k]!=target:
            k+=1
        root=TreeNode(target)
        root.left=self.buildTree(preorder[1:k+1],inorder[0:k])
        root.right=self.buildTree(preorder[k+1:],inorder[k+1:])
        return root
