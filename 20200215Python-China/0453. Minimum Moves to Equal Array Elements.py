class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res=min(nums)
        cnt=0
        for num in nums:
            cnt+=num-res
        return cnt
