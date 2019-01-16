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
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        rep=[]
        left,right=0,len(nums)-1
        while right>left:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid
            else:
                left=mid+1
        if nums[right]==target:
            rep.append(right)
        else:
            return [-1,-1]
        
        left,right=left,len(nums)-1
        while right>left:
            mid=(left+right)//2+1
            if nums[mid]<=target:
                left=mid
            else:
                right=mid-1
        rep.append(left)
        return rep
