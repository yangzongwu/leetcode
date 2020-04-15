# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        
        rep=str(t.val)
        if t.left and t.right:
            rep+='('+self.tree2str(t.left)+')'
            rep+='('+self.tree2str(t.right)+')'
        elif not t.left and t.right:
            rep+='()'
            rep+='('+self.tree2str(t.right)+')'
        elif t.left and not t.right:
            rep+='('+self.tree2str(t.left)+')'
            
        return rep
