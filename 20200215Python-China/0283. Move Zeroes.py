'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p_0=0
        for k in range(len(nums)):
            if nums[k]!=0:
                while p_0<k:
                    if nums[p_0]==0:
                        nums[p_0],nums[k]=nums[k],0
                        break
                    p_0+=1
