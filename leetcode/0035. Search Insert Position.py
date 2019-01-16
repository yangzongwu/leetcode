'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            if target<=nums[0]:
                return 0
            else:
                return 1
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        left=0
        right=len(nums)-1
        while right>left+1:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid
            else:
                right=mid
        if nums[left]==target:
            return left
        else:
            return left+1
##############################seconde##############################
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0]>=target:
            return 0
        if nums[-1]<target:
            return len(nums)
        if nums[-1]==target:
            return len(nums)-1
        left,right=0,len(nums)-1
        while right>left+1:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid
            else:
                left=mid
        return left+1
        
