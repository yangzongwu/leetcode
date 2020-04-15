# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if not preorder:
            return None
        k=0
        while inorder[k]!=preorder[0]:
            k+=1
        root=TreeNode(preorder[0])
        root.left=self.buildTree(preorder[1:k+1],inorder[:k])
        root.right=self.buildTree(preorder[k+1:],inorder[k+1:])
        return root
