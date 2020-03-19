'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums)
        if nums[0]<nums[-1]:
            return nums[0]

        if nums[len(nums)//2]>nums[0]:
            return self.findMin(nums[len(nums)//2:])
        else:
            return self.findMin(nums[:len(nums)//2+1])

        
