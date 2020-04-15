class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        dp=[0]*n
        dp[0]=1
        dp[1]=1
        for i in range(2,n):
            j=2
            while i*j<n:
                dp[i*j]=1
                j+=1
        
        rep=0
        for i in range(2,n):
            if dp[i]==0:
                rep+=1
                
        return rep
