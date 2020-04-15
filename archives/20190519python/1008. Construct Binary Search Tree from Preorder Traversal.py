# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        tree=self.buildTree(preorder)
        return tree
        
        
    def buildTree(self,preorder):
        if not preorder:
            return None
        node=TreeNode(preorder[0])
        k=1
        while k<len(preorder) and preorder[k]<preorder[0]:
            k+=1
        node.left=self.buildTree(preorder[1:k])
        node.right=self.buildTree(preorder[k:])
        return node
