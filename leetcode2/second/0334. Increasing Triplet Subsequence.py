class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<4:
            return False
        first=nums[0]
        k=1
        while k<len(nums):
            if nums[k]<=nums[k-1]:
                first=nums[k]
                k+=1
            else:
                break
        if k==len(nums):
            return False
        second=nums[k]
        for i in range(k+1,len(nums)):
            if nums[i]<=first:
                first=nums[i]
            elif nums[i]>second:
                return True
            else:
                second=nums[i]
        return False
