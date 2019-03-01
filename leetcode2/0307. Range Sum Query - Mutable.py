class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.dp=[]
        rep=0
        for num in nums:
            rep+=num
            self.dp.append(rep)
        
    def update(self, i: int, val: int) -> None:
        gap=val-self.nums[i]
        self.nums[i]=val
        for k in range(i,len(self.dp)):
            self.dp[k]+=gap

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.dp[j]
        return self.dp[j]-self.dp[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
