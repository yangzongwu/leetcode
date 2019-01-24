class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num={}
        for k in range(len(nums)):
            if target-nums[k] not in dict_num:
                dict_num[nums[k]]=k
            else:
                return [dict_num[target-nums[k]],k]
