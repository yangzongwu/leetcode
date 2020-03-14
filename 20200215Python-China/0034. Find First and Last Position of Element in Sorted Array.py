'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                l0=self.leftSideSearch(nums[:mid+1],target)
                r0=self.rightSideSearch(nums[mid:],target)+mid
                return [l0,r0]
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return [-1,-1]
    
    def leftSideSearch(self,nums,target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return r+1

    def rightSideSearch(self,nums,target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return l-1
