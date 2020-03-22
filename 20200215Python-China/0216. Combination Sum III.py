'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[i for i in range(1,10)]
        rep=[]
        self.getCombinationSum(nums,k,n,[],rep)
        return rep

    def getCombinationSum(self,nums,k,n,res,rep):
        if n<0:
            return
        if k==0:
            if n==0:
                rep.append(res)
            return
        for i in range(len(nums)):
            self.getCombinationSum(nums[i+1:],k-1,n-nums[i],res+[nums[i]],rep)
