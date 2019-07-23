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
        node=TreeNode(postorder[-1])
        for k in range(len(inorder)):
            if inorder[k]==postorder[-1]:
                node.left=self.buildTree(inorder[:k],postorder[:k])
                node.right=self.buildTree(inorder[k+1:],postorder[k:-1])
                break
        return node
