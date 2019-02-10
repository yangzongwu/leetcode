class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(right+left)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                l=self.rightsearch(nums[:mid+1][::-1],target)
                r=self.rightsearch(nums[mid:],target)
                return [mid-l,mid+r]
        return [-1,-1]
    def rightsearch(self,nums,target):
        i=0
        while i<len(nums) and nums[i]==target:
            i+=1
        return i-1
################################################################################
    def rightsearch(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                left=mid+1
            else:
                right=mid-1
        return left-1
    
