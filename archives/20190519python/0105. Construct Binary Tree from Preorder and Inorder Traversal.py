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
        node=TreeNode(preorder[0])
        for k in range(len(inorder)):
            if inorder[k]==preorder[0]:
                node.left=self.buildTree(preorder[1:k+1],inorder[0:k])
                node.right=self.buildTree(preorder[k+1:],inorder[k+1:])
                break
        return node
