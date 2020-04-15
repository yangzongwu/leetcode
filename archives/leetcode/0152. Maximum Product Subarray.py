'''
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_product=[nums[0]]
        max_product=[nums[0]]
        for num in nums[1:]:
            cur_min=min_product[-1]
            cur_max=max_product[-1]
            min_product.append(min(num, cur_min * num, cur_max * num))
            max_product.append(max(num, cur_min * num, cur_max * num))
        return max(max_product)
