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
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rep=[]
        self.getPermuteUique(nums,[],rep)
        return rep

    def getPermuteUique(self,nums,res,rep):
        if not nums:
            rep.append(res)
        k=0
        while k<len(nums):
            if k==0 or nums[k]!=nums[k-1]:
                self.getPermuteUique(nums[:k]+nums[k+1:],res+[nums[k]],rep)
            k+=1
