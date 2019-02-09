class Solution:
    def numTrees(self, n: 'int') -> 'int':
        '''
        f(0)=1
        f(1)=1
        f(2)=2
        f(3)=f(0)f(3-1-0)+f(1)f(3-1-1)+f(2)f(3-1-2)
        '''
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[1,1]
        
        for i in range(2,n+1):
            rep=0
            for ii in range(i):
                rep+=dp[ii]*dp[i-1-ii]
            dp.append(rep)
        return dp[-1]
