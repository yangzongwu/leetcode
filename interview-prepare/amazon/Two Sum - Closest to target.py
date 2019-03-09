'''
Description
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
Return the difference between the sum of the two integers and the target.
Example
Given array nums = [-1, 2, 1, -4], and target = 4.
The minimum difference is 1. (4 - (2 + 1) = 1).
Challenge
Do it in O(nlogn) time complexity
'''
#Author:YZW
def twoSumClosest(nums,target):
    nums.sort()
    minsum=nums[0]+nums[1]-target
    left,right=0,len(nums)-1
    while left<right:
        rep=nums[right]+nums[left]-target
        if rep==0:
            return 0
        else:
            if abs(rep)<abs(minsum):
                minsum=rep
            if rep>0:
                right-=1
            else:
                left+=+1
    return abs(minsum)

print(twoSumClosest([-1, 2, 1, -4],4))
