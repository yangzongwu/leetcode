class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        rep=[]
        def dfs(nums,res,rep):
            rep.append(res)
            for k in range(len(nums)):
                dfs(nums[k+1:],res+[nums[k]],rep)
                
        
        dfs(nums,[],rep)
        return rep
