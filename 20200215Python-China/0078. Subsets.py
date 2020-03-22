'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rep=[[]]
        self.getSubsets(nums,[],rep)
        return rep

    def getSubsets(self,nums,res,rep):
        if not nums:
            return
        k=0
        while k<len(nums):
            if k==0 or nums[k]!=nums[k-1]:
                rep.append(res+[nums[k]])
                self.getSubsets(nums[k+1:],res+[nums[k]],rep)
            k+=1
