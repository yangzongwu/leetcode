class Solution:
    def numTrees(self, n: 'int') -> 'int':
        if n==0:return 0
        if n==1:return 1
        
        #f(n)=f(n-1)*f(0)+f(n-2)*f(1)+f(n-3)*f(2)
        
        dp=[1,1]
        
        for i in range(2,n+1):
            rep=0
            for k in range(i):
                rep+=dp[k]*dp[i-1-k]
            dp.append(rep)
        return dp[-1]
