'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        rep = [nums[0]]
        for k in range(1, len(nums)):
            reststep = max(rep[k - 1] - 1, nums[k])
            if reststep == 0 and k < len(nums) - 1:
                return False
            rep.append(reststep)
        return rep[-1] >= 0
        
