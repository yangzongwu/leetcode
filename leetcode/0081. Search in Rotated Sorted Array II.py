'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return target in set(nums)
###############################################################
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(right+left)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>nums[left]:
                if nums[mid]>target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[left]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:left+=1
                
        return False
