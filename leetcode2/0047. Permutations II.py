class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rep=[]
        
        def dfs(nums,rep,res):
            if not nums:
                rep.append(res)
                return
            k=0
            while k<len(nums):
                dfs(nums[:k]+nums[k+1:],rep,res+[nums[k]])
                j=1
                while k+j<len(nums) and nums[k+j]==nums[k]:
                    j+=1
                k+=j
                
        dfs(nums,rep,[])
        return rep
