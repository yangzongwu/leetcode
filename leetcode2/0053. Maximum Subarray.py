class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        subsum=nums[0]
        cur=1
        for cur in range(1,len(nums)):
            if subsum<0:
                subsum=nums[cur]
            else:
                subsum+=nums[cur]
            max_sum=max(max_sum,subsum)
        return max_sum
