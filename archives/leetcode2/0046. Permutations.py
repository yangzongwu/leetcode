class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rep=[]
        
        def dfs(nums,rep,res):
            if not nums:
                rep.append(res)
                return
            for k in range(len(nums)):
                dfs(nums[:k]+nums[k+1:],rep,res+[nums[k]])
        
        dfs(nums,rep,[])
        return rep
