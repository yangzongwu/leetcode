# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.getLeaf(root1)==self.getLeaf(root2)
    
    def getLeaf(self,root):
        if not root:
            return []
        rep=[]
        
        root_list=[]
        while root_list or root:
            if not root:
                root=root_list.pop()
            if not root.left and not root.right:
                rep.append(root.val)
            if root.right:
                root_list.append(root.right)
            root=root.left       
        return rep
