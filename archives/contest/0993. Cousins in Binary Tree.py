# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        if not root:
            return False
        rootlist=[root]
        while rootlist:
            level_val=set()
            len_rootlist=len(rootlist)
            for _ in range(len_rootlist):
                cur_root=rootlist.pop(0)
                level_val.add(cur_root.val)
                if cur_root.left and cur_root.right:
                    if (cur_root.left.val==x and cur_root.right.val==y) or (cur_root.left.val==y and cur_root.right.val==x):
                        return False
                if cur_root.left:
                    rootlist.append(cur_root.left)
                if cur_root.right:
                    rootlist.append(cur_root.right)
            
            if x in level_val and y in level_val:
                return True
        return False
