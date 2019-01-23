'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_nums={}
        for num in nums:
            dict_nums[num]=1
        
        rep=0
        for key in dict_nums:
            if dict_nums[key]==1:
                dict_nums[key]=0
                cur_r=key+1
                while cur_r in dict_nums and dict_nums[cur_r]==1:
                    dict_nums[cur_r]=0
                    cur_r+=1
                cur_l=key-1
                while cur_l in dict_nums and dict_nums[cur_l]==1:
                    dict_nums[cur_l]=0
                    cur_l-=1
                rep=max(rep,cur_r-cur_l-2+1)
        return rep
