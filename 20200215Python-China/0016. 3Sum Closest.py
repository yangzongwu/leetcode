'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        gap=abs(sum(nums[:3])-target)
        rep=sum(nums[:3])
        nums.sort()
        for k in range(len(nums)-2):
            l,r=k+1,len(nums)-1
            while l<r:
                cur_sum=nums[k]+nums[l]+nums[r]
                if cur_sum>target:
                    if cur_sum-target<gap:
                        rep=cur_sum
                        gap=cur_sum-target
                    r-=1
                else:
                    if target-cur_sum<gap:
                        rep=cur_sum
                        gap=target-cur_sum
                    l+=1
        return rep

