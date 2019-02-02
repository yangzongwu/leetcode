class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                l=self.rightSearch(nums[:mid+1][::-1],target)
                r=self.rightSearch(nums[mid:],target)
                return [mid-l,r+mid]
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]
    
    def rightSearch(self,nums,target):
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]==target:
                left=mid+1
            else:# nums[mid]>target:
                right=mid-1
        return left-1
    
