'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
'''
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
        k=0
        flag=0
        while k+1<len(nums):
            while k+1<len(nums) and nums[k]<=nums[k+1]:
                k=k+1
            if k+1==len(nums):
                return True
            if flag==1:
                return False
            if k==0:
                flag=1
                k+=1
            else:                
                if k+2==len(nums):
                    return True
                else:
                    if nums[k+2]>=nums[k]:
                        flag=1
                        k+=2
                    elif nums[k+1]>nums[k-1]:
                        flag=1
                        k+=1
                    else:
                        return False
        return True
            
