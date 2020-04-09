'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums)<s:
            return 0
        cur_sum=0
        rep=len(nums)
        l,r=0,0
        while r<len(nums):
            while r<len(nums) and cur_sum<s:
                cur_sum+=nums[r]
                r+=1
            rep=min(rep,r-l+1)
            while l<r and cur_sum>=s:
                cur_sum-=nums[l]
                l+=1
                rep=min(rep,r-l+1)
        return rep
