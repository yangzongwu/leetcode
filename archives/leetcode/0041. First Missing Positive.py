'''
Given an unsorted integer array, find the smallest missing positive integer.
Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
Note:
Your algorithm should run in O(n) time and uses constant extra space.
'''
class Solution:
    def firstMissingPositive01(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        for k in range(1,len(nums)+2):
            if k not in nums:
                return k

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        k = 0
        while k < len(nums):
            if 0 <= nums[k] < len(nums) and nums[k] != k and nums[k] != nums[nums[k]]:
                tmp = nums[k]
                nums[k], nums[tmp] = nums[tmp], nums[k]
            else:
                k += 1

        for k in range(1, len(nums)):
            if nums[k] != k:
                return k
        if nums[0]==len(nums):
            return len(nums)+1
        return len(nums)

if __name__=='__main__':
    Test=Solution()
    print(Test.firstMissingPositive([3,4,2,1]))
