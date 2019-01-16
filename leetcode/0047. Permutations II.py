'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums)==1:
            return [nums]
        nums.sort()
        rep=[]
        self.subpermuteUnique(nums,rep,[])
        return rep
        
    def subpermuteUnique(self,nums,rep,tmp):
        if not nums:
            rep.append(tmp)
        i=0
        while i<len(nums):
            self.subpermuteUnique(nums[:i]+nums[i+1:],rep,tmp+[nums[i]])
            j=0
            while i+j<len(nums) and nums[i+j]==nums[i]:
                j=j+1
            i=i+j
            
            
