'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while right<len(nums):
            while left<len(nums) and nums[left]!=0:
                left+=1
            right=left+1
            while right<len(nums) and nums[right]==0:
                right+=1
            if right<len(nums):
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right=left
#########################################
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while right<len(nums):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1
############################################
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left=0
        while left<len(nums):
            while left<len(nums) and nums[left]!=0:
                left+=1
            if left==len(nums):
                break
            right=left+1
            while right<len(nums) and nums[right]==0:
                right+=1
            if right==len(nums):
                break
            else:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
