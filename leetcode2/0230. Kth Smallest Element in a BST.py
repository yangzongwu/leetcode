# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.rep=[]
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.rep.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        return self.rep[k-1]
