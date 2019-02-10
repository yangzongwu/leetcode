# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None(
#         self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if n==0:
            return []
        
        nums=[x for x in range(1,n+1)]
        
        def dfs(nums):
            if not nums:
                return [None]
            rep=[]
            for k in range(len(nums)):
                l_list=dfs(nums[:k])
                r_list=dfs(nums[k+1:])
                for l in l_list:
                    for r in r_list:
                        root=TreeNode(nums[k])
                        root.left=l
                        root.right=r
                        rep.append(root)
            return rep
        
        return dfs(nums)
