class Solution:
    def numSquares(self, n: 'int') -> 'int':
        nums=[]
        for x in range(1,n+1):
            if x*x<=n:
                nums.append(x*x)
            else:
                break
        
        dp=[n]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            for num in nums:
                if num==i:
                    dp[i]=1
                elif num<i:
                    dp[i]=min(dp[i],dp[i-num]+1)
                else:
                    break
        return dp[-1]
