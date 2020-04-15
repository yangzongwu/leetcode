class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target<=nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left
                
