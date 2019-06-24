class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        FN,SN=0,1
        if nums[0]<nums[1]:
            FN=1
            SN=0
        
        for k in range(2,len(nums)):
            if nums[k]>nums[FN]:
                FN,SN=k,FN
            elif nums[k]>nums[SN]:
                SN=k
        
        if nums[FN]>=nums[SN]*2:
            return FN
        return -1
