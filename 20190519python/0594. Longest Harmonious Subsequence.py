class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict_nums={}
        for num in nums:
            if num not in dict_nums:
                dict_nums[num]=1
            else:
                dict_nums[num]+=1
                
        
        nums=list(set(nums))
        nums.sort()
        
        rep=0
        for k in range(len(nums)-1):
            if nums[k+1]==nums[k]+1:
                rep=max(rep,dict_nums[nums[k]]+dict_nums[nums[k+1]])
        
        return rep
