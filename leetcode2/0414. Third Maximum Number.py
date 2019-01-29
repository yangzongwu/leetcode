class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        if len(nums)==1:
            return nums[0]
        if len(nums)<3:
            return max(nums)
        rep=[nums[0],nums[1],nums[2]]
        rep.sort()
        for num in nums[3:]:
            if num<rep[0]:
                continue
            elif rep[0]<num<rep[1]:
                rep[0]=num
            elif rep[1]<num<rep[2]:
                rep[0],rep[1]=rep[1],num
            else:
                rep[0],rep[1],rep[2]=rep[1],rep[2],num
        return rep[0]
