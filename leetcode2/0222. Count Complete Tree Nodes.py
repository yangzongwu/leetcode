# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Definition for a binary tree node.

        if not root:
            return 0
        
        root_stack=[root]
        cnt=0
        while root_stack:
            cur_root=root_stack.pop()
            cnt+=1
            if cur_root.right:
                root_stack.append(cur_root.right)
            if cur_root.left:
                root_stack.append(cur_root.left)
        return cnt
