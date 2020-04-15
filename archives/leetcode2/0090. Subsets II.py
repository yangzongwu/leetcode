class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums:
            return []
        
        nums.sort()
        self.rep=[]
        
        def dfs(nums,res):
            self.rep.append(res)
            if not nums:
                return
            k=0
            while k<len(nums):
                dfs(nums[k+1:],res+[nums[k]])
                i=0
                while k+i<len(nums) and nums[k]==nums[k+i]:
                    i+=1
                k=k+i
        
        dfs(nums,[])
        return self.rep
