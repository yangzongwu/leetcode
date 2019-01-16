'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] 
is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra 
space for the purpose of space complexity analysis.)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        tmp=1
        for s in nums:
            result.append(tmp)
            tmp*=s
        tmp=1
        for k in range(len(nums)-1,-1,-1):
            result[k]=result[k]*tmp
            tmp*=nums[k]
        return result
