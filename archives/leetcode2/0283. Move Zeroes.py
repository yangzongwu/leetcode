class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        right=len(nums)-1
        left=0
        cur=left
        while right>=cur:
            while left<len(nums) and nums[left]!=0:
                left+=1
            if left==len(nums):
                break
            cur=left+1
            while cur<len(nums) and nums[cur]==0:
                cur+=1
            if cur==len(nums):
                break
            nums[left],nums[cur]=nums[cur],nums[left]
            left+=1
            cur+=1
            
