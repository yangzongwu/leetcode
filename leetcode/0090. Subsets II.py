'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rep=[]
        self.subSubsetsWithDup(nums,rep,[])
        return rep
    
    def subSubsetsWithDup(self,nums,rep,tmp):
        rep.append(tmp)
        if not nums:
            return
        i=0
        while i<len(nums):
            self.subSubsetsWithDup(nums[i+1:],rep,tmp+[nums[i]])    
            j=1
            while i+j<len(nums) and nums[i+j]==nums[i]:
                j+=1
            i+=j
