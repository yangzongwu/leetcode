'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element 
in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
######################################################################
import random
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=[]
        right=[]
        target=random.choice(nums)
        for num in nums:
            if num<target:
                left.append(num)
            elif num>target:
                right.append(num)
        if len(right)>=k:
            return self.findKthLargest(right,k)
        elif len(nums)-len(left)<k:
            return self.findKthLargest(left,k-(len(nums)-len(left)))
        return target
