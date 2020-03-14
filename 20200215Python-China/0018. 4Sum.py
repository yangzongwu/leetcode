'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        rep=[]
        for k1 in range(len(nums)-3):
            if k1!=0 and nums[k1]==nums[k1-1]:
                continue
            for k2 in range(k1+1,len(nums)-2):
                if k2!=k1+1 and nums[k2]==nums[k2-1]:
                    continue
                k3=k2+1
                k4=len(nums)-1
                while k3<k4:
                    cur=nums[k1]+nums[k2]+nums[k3]+nums[k4]
                    if cur>target:
                        while k4>k3 and nums[k4]==nums[k4-1]:
                            k4-=1
                        else:
                            k4-=1
                    else:
                        if cur==target:
                            rep.append([nums[k1],nums[k2],nums[k3],nums[k4]])
                        while k3<k4 and nums[k3+1]==nums[k3]:
                            k3+=1
                        else:
                            k3+=1
        return rep
