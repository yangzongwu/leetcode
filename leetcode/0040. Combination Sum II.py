'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        rep = []
        self.dfs(candidates, target, rep, [])
        return rep

    def dfs(self, candidates, target, rep, tmp):
        if target == 0:
            rep.append(tmp)
        else:
            i = 0
            while i < len(candidates):
                if candidates[i] <= target:
                    self.dfs(candidates[i + 1:], target - candidates[i], rep, tmp + [candidates[i]])
                k = 0
                while i + k < len(candidates) and candidates[i] == candidates[i + k]:
                    k += 1
                i = i + k
