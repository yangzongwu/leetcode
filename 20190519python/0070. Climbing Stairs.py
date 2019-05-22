class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[1,1]
        while n>1:
            dp.append(dp[-1]+dp[-2])
            n-=1
        return dp[-1]
