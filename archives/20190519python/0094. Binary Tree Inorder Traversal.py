# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        rep=[]
        self.getInorderTraversal(root,rep)
        return rep
    
    def getInorderTraversal(self,root,rep):
        if not root:
            return
        if root.left:
            self.getInorderTraversal(root.left,rep)
        rep.append(root.val)
        if root.right:
            self.getInorderTraversal(root.right,rep)
            
#===========================================================================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        rep=[]
        root_list=[]
        while root or root_list:  
            while root:
                root_list.append(root)
                root=root.left
            root=root_list.pop()
            rep.append(root.val)
            root=root.right
            
        return rep
