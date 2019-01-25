class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rep=0
        for num in nums:
            rep^=num
        return rep
