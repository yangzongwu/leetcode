class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rep=nums[0]
        min_nums=1
        max_nums=1
        for num in nums:
            min_nums,max_nums=min(min_nums*num,max_nums*num,num),max(min_nums*num,max_nums*num,num)
            rep=max(rep,max_nums)
        return rep
