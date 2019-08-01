# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val==key:
            if not root.right:
                return root.left
            else:
                cur=root.left
                root=root.right
                tmp=root
                while tmp.left:
                    tmp=tmp.left
                tmp.left=cur
                return root
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            root.right=self.deleteNode(root.right,key)
        return root
