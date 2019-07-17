# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        nums=[x for x in range(1,n+1)]
        return self.getGenerateTrees(nums)
    
    def getGenerateTrees(self,nums):
        if not nums:
            return [None]
        cur=[]
        for k in range(len(nums)):
            leftnode=self.getGenerateTrees(nums[:k])
            rightnode=self.getGenerateTrees(nums[k+1:])
            for l in leftnode:
                for r in rightnode:
                    node=TreeNode(nums[k])
                    node.left=l
                    node.right=r
                    cur.append(node)
        return cur
        
