class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        if n==1:
            return 1
        dp=[1]*n
        index=[]
        len_primes=len(primes)
        for _ in range(len_primes):
            index.append(0)
        for i in range(1,n):
            dp[i]=min(dp[index[x]]*primes[x] for x in range(len_primes))
            for x in range(len_primes):
                if dp[index[x]]*primes[x]==dp[i]:
                    index[x]+=1
        return dp[-1]
