class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        right=len(nums)-1
        while right-1>=0 and nums[right-1]>=nums[right]:
            right-=1
        if right==0:
            nums.reverse()
        else:
            cur=right-1
            right=len(nums)-1
            while right>cur and nums[right]<=nums[cur]:
                right-=1
            nums[cur],nums[right]=nums[right],nums[cur]
            nums[cur+1:]= nums[cur+1:][::-1]
