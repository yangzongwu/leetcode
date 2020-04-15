# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if not inorder:
            return None
        
        k=0
        while inorder[k]!=postorder[-1]:
            k=k+1
            
        root=TreeNode(postorder[-1])
        root.left=self.buildTree(inorder[:k],postorder[:k])
        root.right=self.buildTree(inorder[k+1:],postorder[k:-1])
        return root
