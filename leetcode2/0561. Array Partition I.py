class Solution:
    def arrayPairSum(self, nums: 'List[int]') -> 'int':
        nums.sort()
        rep=0
        for num in range(0,len(nums),2):
            rep+=nums[num]
        return rep
