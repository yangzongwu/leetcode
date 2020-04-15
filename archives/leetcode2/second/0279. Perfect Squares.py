class Solution:
    def numSquares(self, n: 'int') -> 'int':
        num=set()
        for i in range(1,n//2+1):
            if i*i<=n:
                num.add(i*i)
            else:
                break
        
        dp=[0]
        for i in range(1,n+1):
            if i in num:
                dp.append(1)
            else:
                dp.append(self.subNumSquares(list(num),i,dp))
        return dp[-1]
    
    def subNumSquares(self,nums,i,dp):
        rep=i
        for num in nums:
            if num<i:
                rep=min(rep,dp[i-num]+1)
        return rep
