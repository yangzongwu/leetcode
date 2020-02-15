class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k=0
        while k<len(nums):
            if nums[k]==k+1 or nums[k]==nums[nums[k]-1]:
                k+=1
            else:
                tmp=nums[k]
                nums[k],nums[tmp-1]=nums[tmp-1],nums[k]
        
        rep=[]
        for k in range(len(nums)):
            if nums[k]!=k+1:
                rep.append(k+1)
        return rep
            
