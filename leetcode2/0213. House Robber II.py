class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if len(nums)==1:
            return nums[0]
        rep=0
        dp1=[0,0]
        for num in nums[:-1]:
            dp1.append(max(dp1[-1],dp1[-2]+num))
        
        dp2=[0,0]
        for num in nums[1:]:
            dp2.append(max(dp2[-1],dp2[-2]+num))
            
        return max(dp1[-1],dp2[-1])
