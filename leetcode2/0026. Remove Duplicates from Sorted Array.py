class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        if len(nums)>1:
            left=0
            right=1
            for right in range(1,len(nums)):
                if nums[right]!=nums[left]:
                    nums[left+1],nums[right]=nums[right],nums[left+1]
                    right+=1
                    left+=1
            return left+1
        
                
