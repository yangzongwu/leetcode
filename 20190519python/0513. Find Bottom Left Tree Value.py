# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        rep=root.val
        root_stack=[root]
        while root_stack:
            tmp=[]
            rep=root_stack[0].val
            while root_stack:
                cur_root=root_stack.pop(0)
                if cur_root.left:
                    tmp.append(cur_root.left)
                if cur_root.right:
                    tmp.append(cur_root.right)
            root_stack=tmp
        return rep
