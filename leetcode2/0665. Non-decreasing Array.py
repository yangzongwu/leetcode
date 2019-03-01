class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':
        if len(nums)<2:
            return True
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                if self.subcheckPossibility(nums[:i-1]+[nums[i],nums[i]]+nums[i+1:]) or self.subcheckPossibility(nums[:i-1]+[nums[i-1],nums[i-1]]+nums[i+1:]):
                    return True
                else:
                    return False
        return True
    
    def subcheckPossibility(self,nums):
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                return False
        return True
