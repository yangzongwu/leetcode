class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        FN=sum(nums)-sum(set(nums))
        SN=(1+len(nums))*len(nums)//2-sum(set(nums))
        return [FN,SN]
