'''
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every 
element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
'''
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dictnums = {}
        for num in nums:
            if num not in dictnums:
                dictnums[num] = num
            else:
                dictnums[num] += num
        nums=list(set(nums))
        nums.sort()
        return self.subdeleteAndEarn(nums, dictnums)

    def subdeleteAndEarn(self, nums, dictnums):
        if not nums:
            return 0
        if len(nums) == 1:
            return dictnums[nums[0]]
        elif len(nums) == 2:
            if nums[1] == nums[0] + 1:
                return max(dictnums[nums[0]], dictnums[nums[1]])
            else:
                return dictnums[nums[0]] + dictnums[nums[1]]
        else:
            if nums[1] > nums[0] + 1:
                return dictnums[nums[0]] + self.subdeleteAndEarn(nums[1:], dictnums)
            else:  # nums[1]==nums[0]+1:
                if nums[2] > nums[1] + 1:
                    x1 = max(dictnums[nums[0]], dictnums[nums[1]])
                    x2 = self.subdeleteAndEarn(nums[2:], dictnums)
                    return x1 + x2
                else:
                    x1 = dictnums[nums[0]]+self.subdeleteAndEarn(nums[2:], dictnums)
                    x2 = dictnums[nums[1]]+self.subdeleteAndEarn(nums[3:], dictnums)
                    return max(x1, x2)
    ############################################################
    class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dictnums = {}
        for num in nums:
            if num not in dictnums:
                dictnums[num] = num
            else:
                dictnums[num] += num
        nums=list(set(nums))
        nums.sort()
        rep=[dictnums[nums[0]]]
        if nums[1]  and nums[1]-nums[0]==1:
            rep.append(max(dictnums[nums[0]],dictnums[nums[1]]))
        else:
            rep.append(dictnums[nums[0]]+dictnums[nums[1]])
        for k in range(2,len(nums)):
            if nums[k]-nums[k-1]==1:
                rep.append(max(dictnums[nums[k]]+rep[k-2],rep[k-1]))
            else:
                rep.append(dictnums[nums[k]]+rep[k-1])
        return rep[-1]
