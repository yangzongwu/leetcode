# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        rep=[]
        root_list=[]
        while root_list or root:
            if not root:
                root=root_list.pop()
            if root.right:
                root_list.append(root.right)
            rep.append(root.val)
            root=root.left
        return rep
#=============================================================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        rep=[]
        self.sub_preorderTraversal(root,rep)
        return rep
    
    def sub_preorderTraversal(self,root,rep):
        if not root:
            return 
        rep.append(root.val)
        self.sub_preorderTraversal(root.left,rep)
        self.sub_preorderTraversal(root.right,rep)
        return
