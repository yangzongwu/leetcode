class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        right=len(nums)-1
        while right>=0 and nums[right]==val:
            right-=1
        if right<0:
            return 0
        
        left=0
        while left<=right:
            if nums[left]!=val:
                left+=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                
                while nums[right]==val:
                    right-=1
        return left
