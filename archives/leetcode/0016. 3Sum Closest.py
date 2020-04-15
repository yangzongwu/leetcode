'''
Given an array nums of n integers and an integer target, find three integers in nums 
such that the sum is closest to target. Return the sum of the three integers. You may 
assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        rep=[]
        gap=nums[0]+nums[1]+nums[2]
        for k in range(len(nums)-2):
            left=k+1
            right=len(nums)-1
            while right>left:
                cursum=nums[k]+nums[left]+nums[right]
                if cursum==target:
                    return cursum
                else:
                    if abs(cursum-target)<abs(gap-target):
                            gap=cursum
                    if cursum>target:
                        right-=1
                    else: 
                        left+=1
        return gap
                    
            
