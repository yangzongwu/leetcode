'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
#Time Limit Exceeded
#改进后仍超时，
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<2:
            return 0
        if n==2:
            return 0
        elif n==3:
            return 1
        else:
            primes=[2,3]
            for i in range(4,n):
                flag=0
                for prime in primes:
                    if i%prime==0:
                        flag=1
                        break
                if flag==0:
                    primes.append(i)
            count=0
            for s in primes:
                count+=1
            return count
 ##厄拉多塞筛法
 class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        list_n=[]
        for s in range(n):
            list_n.append(0)
        list_n[0],list_n[1]=1,1
        for s in range(2,int(n**0.5)+1):
            if list_n[s]==0:
                i=2
                while i*s<n:
                    list_n[i*s]=1
                    i+=1
        rep=0
        for s in list_n:
            if s==0:
                rep+=1
        return rep
 ##厄拉多塞筛法（别人写的）
 class Solution(object):
    def countPrimes(self, n):
        if n<3:
            return 0
        list_n=[1]*n
        list_n[0],list_n[1]=0,0
        for s in range(2,int(n**0.5)+1):
            if list_n[s]==1:
                list_n[s*s:n:s]=[0] * len(list_n[s * s: n: s])
        return sum(list_n)
 ##
