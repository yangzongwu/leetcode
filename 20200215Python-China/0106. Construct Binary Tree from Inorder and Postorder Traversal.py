'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        target=postorder[-1]
        k=0
        while inorder[k]!=target:
            k+=1
        root=TreeNode(target)
        root.left=self.buildTree(inorder[:k],postorder[:k])
        root.right=self.buildTree(inorder[k+1:],postorder[k:-1])
        return root
