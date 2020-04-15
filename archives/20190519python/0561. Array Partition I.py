class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        rep=0
        for k in range(0,len(nums),2):
            rep+=nums[k]
        return rep
