'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rep=[]
        self.subcombine(1,n,k,rep,[])
        return rep
    
    def subcombine(self,start,n,k,rep,tmp):
        if k==0:
            rep.append(tmp)
            return
        if start==n+1:
            return
        for i in range(start,n+1):
            self.subcombine(i+1,n,k-1,rep,tmp+[i])
            
            
