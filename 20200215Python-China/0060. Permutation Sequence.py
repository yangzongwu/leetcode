'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[str(x) for x in range(1,n+1)]
        rep=self.getPermutationFromList(nums,k,[])
        return ''.join(rep)

    def getPermutationFromList(self,nums,k,rep):
        if k==1:
            return rep+nums
        n=self.getProduct(len(nums)-1)
        if k%n==0:
            return rep+[nums[k//n-1]]+(nums[:(k//n-1)]+nums[(k//n):])[::-1] 
        else:
            return self.getPermutationFromList(nums[:(k//n)]+nums[(k//n+1):],k-n*(k//n),rep+[nums[k//n]])


    def getProduct(self,n):
        if n==1:
            return 1
        return n*self.getProduct(n-1)
