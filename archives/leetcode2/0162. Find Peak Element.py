class Solution:
    def findPeakElement(self, nums: 'List[int]') -> 'int':
        if len(nums)==1:
            return 0
        if nums[1]<nums[0]:return 0
        if nums[-2]<nums[-1]:return len(nums)-1
        
        k=1
        while k<len(nums)-1:
            if nums[k]<nums[k+1]:
                k+=1
            else:
                return k
