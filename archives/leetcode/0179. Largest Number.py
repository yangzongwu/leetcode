'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            return int(b+a)-int(a+b)
        if len(nums)==0:
            return ''
        if len(nums)==1:
            return str(nums[0])
        if sum(nums)==0:
            return '0'
        nums=sorted([str(s) for s in nums],cmp=compare)
        cur=''.join(nums)
        return cur
