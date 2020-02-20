'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        dp=[0]*n
        dp[0]=1
        dp[1]=1
        cnt=0
        for k in range(2,n):
            if dp[k]==0:
                cnt+=1
                dp[k]=1
                N=n//k+1
                if n%k==0:
                    N-=1
                for j in range(2,N):
                    dp[k*j]=1
        return cnt
