class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp=[1]
        for num in nums[:-1]:
            res=max(dp[-1]-1,num)
            if res==0:
                return False
            dp.append(res)
        return True
            
