'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rep=0
        for i in range(len(nums)):
            rep+=self.arraySum(nums[i:],k)
        return rep
    
    def arraySum(self,nums,k):
        rep=0
        cnt=0
        for num in nums:
            rep+=num
            if rep==k:
                cnt+=1
        return cnt
#################################################################
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_num=0
        cnt=0
        dict_sum={0:1}
        for num in nums:
            sum_num+=num
            if sum_num-k in dict_sum:
                cnt+=dict_sum[sum_num-k]
            if sum_num in dict_sum:
                dict_sum[sum_num]+=1
            else:
                dict_sum[sum_num]=1
        return cnt
