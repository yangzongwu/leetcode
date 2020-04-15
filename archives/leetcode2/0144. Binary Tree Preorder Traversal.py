# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        root_stack=[root]
        rep=[]
        while root_stack:
            cur_root=root_stack.pop()
            rep.append(cur_root.val)
            if cur_root.right:
                root_stack.append(cur_root.right)
            if cur_root.left:
                root_stack.append(cur_root.left)
        return rep
