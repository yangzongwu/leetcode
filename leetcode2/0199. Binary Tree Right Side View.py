# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Definition for a binary tree node.

        if not root:
            return []
        
        root_stack=[root]
        rep=[]
        while root_stack:
            len_root_stack=len(root_stack)
            rep.append(root_stack[-1].val)
            for _ in range(len_root_stack):
                cur_root=root_stack.pop(0)
                if cur_root.left:
                    root_stack.append(cur_root.left)
                if cur_root.right:
                    root_stack.append(cur_root.right)
                
        return rep
