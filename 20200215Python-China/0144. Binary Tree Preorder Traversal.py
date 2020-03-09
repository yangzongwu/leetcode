'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.rep=[]

        def dfs(root):
            if not root:
                return
            self.rep.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return self.rep
#---------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        rep=[]
        root_list=[root]
        while root_list:
            cur=root_list.pop()
            rep.append(cur.val)
            if cur.right:
                root_list.append(cur.right)
            if cur.left:
                root_list.append(cur.left)
        return rep
