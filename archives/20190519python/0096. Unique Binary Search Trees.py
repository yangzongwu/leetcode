class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        
        #f(n)=f(n-1)+f(1)*f(n-2)+...+f(n-2)*f(1)+f(n-1)
        
        dp=[1,1,2]
        
        for i in range(3,n+1):
            cur=0
            for k in range(i):
                cur+=dp[k]*dp[i-1-k]
                
            dp.append(cur)
            
        return dp[-1]
        
