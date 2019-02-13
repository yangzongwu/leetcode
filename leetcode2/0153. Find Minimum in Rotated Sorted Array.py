class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 2**31-1
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums)
        
        k=(0+len(nums)-1)//2
        if nums[k]>nums[0]:
            return min(nums[0],self.findMin(nums[k+1:]))
        else:
            return self.findMin(nums[:k+1])
