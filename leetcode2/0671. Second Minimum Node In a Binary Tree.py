# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        rep=-1
        target=root.val
        root_stack=[root]
        
        while root_stack:
            len_root_stack=len(root_stack)
            for _ in range(len_root_stack):
                cur_root=root_stack.pop(0)
                if cur_root.val>target:
                    if rep==-1:
                        rep=cur_root.val
                    else:
                        rep=min(rep,cur_root.val)
                if cur_root.left:
                    root_stack.append(cur_root.left)
                    root_stack.append(cur_root.right)
        return rep
