class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_number=min(nums)
        rep=0
        for num in nums:
            rep+=num-min_number
        return rep
