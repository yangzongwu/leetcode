'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)==1:
            return [nums]
        
        rep=[]
        for k in range(len(nums)):
            for cur_nums in self.permute(nums[:k]+nums[k+1:]):
                rep.append([nums[k]]+cur_nums)
        
        return rep
