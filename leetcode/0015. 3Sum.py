'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums)<3:
            return []
        rep=[]
        cur=0
        while cur<len(nums)-1:
            left=cur+1
            right=len(nums)-1
            while right > left:
                if nums[cur]+nums[left]+nums[right]>0:
                    right-=1
                elif nums[cur]+nums[left]+nums[right]<0:
                    left+=1
                else: #nums[cur]+nums[left]+nums[right]==0:
                    rep.append([nums[cur],nums[left],nums[right]])
                    i=0
                    while left+i<right and nums[left+i]==nums[left]:
                        i+=1
                    left=left+i
            i=1
            while cur+i<len(nums)-1 and nums[cur+i]==nums[cur]:
                i+=1
            cur+=i
        return rep
