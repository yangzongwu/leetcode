'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack=[root]
        rep=[]
        while stack:
            cur_root=stack.pop()
            rep.append(cur_root.val)
            if cur_root.right:
                stack.append(cur_root.right)
            if cur_root.left:
                stack.append(cur_root.left)
        return rep
