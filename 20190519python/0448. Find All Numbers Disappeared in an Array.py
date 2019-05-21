class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            if nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                tmp=nums[i]
                nums[i],nums[tmp-1]=nums[tmp-1],nums[i]
            else:
                i+=1
                
        rep=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                rep.append(i+1)
        return rep
