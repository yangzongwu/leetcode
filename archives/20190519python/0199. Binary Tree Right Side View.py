# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        rep=[]
        root_stack=[root]
        while root_stack:
            rep.append(root_stack[-1].val)
            len_root_stack=len(root_stack)
            for k in range(len_root_stack):
                cur_root=root_stack.pop(0)
                if cur_root.left:
                    root_stack.append(cur_root.left)
                if cur_root.right:
                    root_stack.append(cur_root.right)
        return rep
