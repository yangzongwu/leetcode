# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        cnt=0
        root_stack=[root]
        while root_stack:
            cur_root=root_stack.pop()
            cnt+=1
            if cur_root.left:
                root_stack.append(cur_root.left)
            if cur_root.right:
                root_stack.append(cur_root.right)
        return cnt
