'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rep=[]
        nums.sort()
        for k in range(len(nums)-2):
            if k!=0 and nums[k]==nums[k-1]:
                continue
            l,r=k+1,len(nums)-1
            while l<r:
                if nums[k]+nums[l]+nums[r]>0:
                    while r>l and nums[r]==nums[r-1]:
                        r-=1
                    else:
                        r-=1
                else:
                    if nums[k]+nums[l]+nums[r]==0:
                        rep.append([nums[k],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    else:
                        l+=1
        return rep
