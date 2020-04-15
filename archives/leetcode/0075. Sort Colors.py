'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color 
are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, 
then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        
        while left<len(nums) and nums[left]==0:
            left+=1
            
        cur=left
        
        while right>=0 and nums[right]==2:
            right-=1
            
        while cur<=right:
            if nums[cur]==0:
                nums[left],nums[cur]=nums[cur],nums[left]
                left+=1
            if nums[cur]==2:
                nums[right],nums[cur]=nums[cur],nums[right]
                right-=1
            else:
                cur+=1
