class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        dp=[0,1]
        flag=[1 for _ in primes]
        for k in range(2,n+1):
            
            target=primes[0]*dp[flag[0]]
            for i in range(len(primes)):
                target=min(target,primes[i]*dp[flag[i]])
            dp.append(target)
            
            for i in range(len(primes)):
                if target==primes[i]*dp[flag[i]]:
                    flag[i]+=1
        return dp[-1]
