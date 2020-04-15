class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        dp=[1]
        k=1
        while k<len(nums):
            rep=1
            for i in range(k):
                if nums[k]>nums[i]:
                    rep=max(rep,dp[i]+1)
            dp.append(rep)
            k+=1
        return max(dp)
