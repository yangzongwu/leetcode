# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        root_list=[root]
        rep=[]
        while root_list:
            cur=root_list.pop()
            if not cur.left and not cur.right:
                rep.append(cur.val)
            else:
                if cur.right:
                    root_list.append(cur.right)
                root_list.append(TreeNode(cur.val))
                if cur.left:
                    root_list.append(cur.left)
        return rep
