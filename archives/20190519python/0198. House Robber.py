class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0,nums[0]]
        for num in nums[1:]:
            dp.append(max(dp[-1],dp[-2]+num))
        return dp[-1]
