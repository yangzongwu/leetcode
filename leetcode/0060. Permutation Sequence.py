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
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nlist=[i for i in range(1,n+1)]
        rep=''
        return self.subgetPermutation(nlist,n,k,rep)
        
    def subgetPermutation(self,nlist,n,k,rep):
        if nlist==[]:
            return rep
        cal_n=self.calculaten(n-1)
        if k%cal_n==0:
            tmp=k//cal_n-1
            return self.subgetPermutation(nlist[:tmp]+nlist[tmp+1:],n-1,cal_n,rep+str(nlist[tmp]))
        else:
            
            tmp1=k//cal_n
            tmp2=k%cal_n
            tmp=tmp1
            return self.subgetPermutation(nlist[:tmp]+nlist[tmp+1:],n-1,tmp2,rep+str(nlist[tmp]))
        
            
    def calculaten(self,n):
        rep=1
        for i in range(1,n+1):
            rep*=i
        return rep
