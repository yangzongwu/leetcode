'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and 
conquer approach, which is more subtle.
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        tmp=nums[0]
        i=1
        while i<len(nums):
            if tmp>0:
                max_sum=max(max_sum,tmp)
                tmp+=nums[i]
            else:
                tmp=nums[i]
                max_sum=max(max_sum,tmp)
            i+=1
        return max(max_sum,tmp)
################################seconde################################################
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rep=nums[0]
        maxsum=nums[0]
        for s in nums[1:]:
            if rep>0:
                rep+=s
                maxsum=max(maxsum,rep)
            else:
                rep=s
                maxsum=max(maxsum,rep)
        return maxsum
    ########################################################################3
    class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rep=nums[0]
        maxsubarray=rep
        for s in nums[1:]:
            if rep>0:
                rep+=s
                maxsubarray=max(maxsubarray,rep)
            else:
                rep=s
                maxsubarray=max(maxsubarray,rep)
        return maxsubarray
