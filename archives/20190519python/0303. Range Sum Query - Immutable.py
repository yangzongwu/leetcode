class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_nums=[]
        rep=0
        for num in nums:
            rep+=num
            self.sum_nums.append(rep)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.sum_nums[j]
        return self.sum_nums[j]-self.sum_nums[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
