'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        rep=[]
        firstK=0
        while firstK<len(nums):
            secondK=firstK+1
            while secondK<len(nums):
                thirdK=secondK+1
                fourthK=len(nums)-1
                curgap=target-nums[firstK]-nums[secondK]
                while thirdK<fourthK:
                    if nums[thirdK]+nums[fourthK]==curgap:
                        rep.append([nums[firstK],nums[secondK],nums[thirdK],nums[fourthK]])
                        thirdK+=1
                        while thirdK<len(nums) and nums[thirdK]==nums[thirdK-1]:
                            thirdK+=1
                    elif nums[thirdK]+nums[fourthK]>curgap:
                        fourthK-=1
                    else:
                        thirdK+=1
                secondK+=1
                while secondK<len(nums) and nums[secondK]==nums[secondK-1]:
                    secondK+=1
            firstK+=1
            while firstK<len(nums) and nums[firstK]==nums[firstK-1]:
                    firstK+=1
        return rep
            
            
