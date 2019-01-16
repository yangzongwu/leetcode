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
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rep = [[]]
        self.subsubsets(nums, rep, [])
        return rep

    def subsubsets(self, nums, rep, cur):
        if not nums:
            return
        for k in range(len(nums)):
            rep.append(cur+[nums[k]])
            self.subsubsets(nums[k+1:], rep, cur+[nums[k]])
