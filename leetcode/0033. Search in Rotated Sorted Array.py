'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left=0
        right=len(nums)-1
        while right>left+1:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[right]:
                if nums[mid]<target<=nums[right]:
                    left=mid
                else:
                    right=mid
            if nums[mid]>=nums[left]:
                if nums[mid]>target>=nums[left]:
                    right=mid
                else:
                    left=mid
        if nums[left]==target:return left
        if nums[right]==target:return right
        return -1
        
        
