class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0,0]
        for num in nums:
            dp.append(max(dp[-2]+num,dp[-1]))
        return dp[-1]
