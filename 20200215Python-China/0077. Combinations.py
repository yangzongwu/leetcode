'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
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
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[i for i in range(1,n+1)]
        rep=[]
        self.getCombine(nums,k,[],rep)
        return rep

    def getCombine(self,nums,k,res,rep):
        if k==0:
            rep.append(res)
            return
        if not nums:
            return 
        for i in range(len(nums)):
            self.getCombine(nums[i+1:],k-1,res+[nums[i]],rep)


    
