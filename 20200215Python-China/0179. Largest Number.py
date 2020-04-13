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
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a,b):
            return int(str(b)+str(a))-int(str(a)+str(b))
        if len(nums)==0:
            return ''
        if len(nums)==1:
            return str(nums[0])
        if sum(nums)==0:
            return '0'
        nums.sort(key=functools.cmp_to_key(compare))
        cur=''.join(str(num) for num in nums)
        return cur
