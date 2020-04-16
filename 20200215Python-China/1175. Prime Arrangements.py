'''
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100

'''
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        arr=[0]*(n+1)
        arr[0]=1
        arr[1]=1
        for i in range(2,n//2+1):
            if arr[i]==0:
                k=2
                while i*k<n+1:
                    arr[i*k]=1
                    k+=1
        count_prime=0
        count_non_prime=0
        for num in arr[1:]:
            if num==0:
                count_prime+=1
            else:
                count_non_prime+=1
        return (self.permutations(count_prime)*self.permutations(count_non_prime))%(10**9+7)

    def permutations(self,n):
        cnt=1
        for i in range(1,n+1):
            cnt*=i
        return cnt
