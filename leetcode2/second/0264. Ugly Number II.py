class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        if n==1:
            return 1
        dp=[1]
        num2,num3,num5=0,0,0
        for _ in range(1,n):
            target=min(2*dp[num2],3*dp[num3],5*dp[num5])
            dp.append(target)
            if 2*dp[num2]==target:
                num2+=1
            if 3*dp[num3]==target:
                num3+=1
            if 5*dp[num5]==target:
                num5+=1
        return dp[-1]
            
