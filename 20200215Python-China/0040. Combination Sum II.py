'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        rep=[]
        self.getCombinationSum(candidates,target,[],rep)
        return rep

    def getCombinationSum(self,candidates,target,res,rep):
        if target==0:
            rep.append(res)
            return
        if not candidates or target<0:
            return
        
        k=0
        while k<len(candidates):
            if k==0 or candidates[k]!=candidates[k-1]:
                self.getCombinationSum(candidates[k+1:],target-candidates[k],res+[candidates[k]],rep)
            k+=1
