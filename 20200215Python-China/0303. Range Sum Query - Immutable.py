'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.sumList=[]
        cur=0
        for num in nums:
            cur+=num
            self.sumList.append(cur)

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.sumList[j]
        return self.sumList[j]-self.sumList[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
