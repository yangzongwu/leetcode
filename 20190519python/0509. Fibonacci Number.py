class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        if N==1:
            return 1
        dp=[0,1]
        for i in range(2,N+1):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]
