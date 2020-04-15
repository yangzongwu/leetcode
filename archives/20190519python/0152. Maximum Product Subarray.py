class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rep=nums[0]
        min_nums=nums[0]
        max_nums=nums[0]
        for num in nums[1:]:
            min_nums,max_nums=min(min_nums*num,num,max_nums*num),max(min_nums*num,num,max_nums*num)
            rep=max(rep,max_nums)
        return rep
