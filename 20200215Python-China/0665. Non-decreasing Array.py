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
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True

        flag=False
        k=1
        while k<len(nums):
            if nums[k-1]<=nums[k]:
                k+=1
            else:
                if flag==True:
                    return False
                flag=True
                if k+1==len(nums):
                    return True
                else:
                    if nums[k+1]>=nums[k-1]:
                        k+=1
                    else:
                        if k-2>=0:  
                            if nums[k+1]>=nums[k] and nums[k]>=nums[k-2]:
                                k+=1
                        else:
                            if nums[k+1]>=nums[k]:
                                k+=1
        return True
