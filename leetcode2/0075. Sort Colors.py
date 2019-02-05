class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        while left<len(nums) and nums[left]==0:
            left+=1
        right=len(nums)-1
        while right>=0 and nums[right]==2:
            right-=1
        cur=left
        while cur<=right:
            if nums[cur]==0:
                nums[left],nums[cur]=nums[cur],nums[left]
                left+=1
                cur+=1
            elif nums[cur]==2:
                nums[right],nums[cur]=nums[cur],nums[right]
                right-=1
            else:
                cur+=1
