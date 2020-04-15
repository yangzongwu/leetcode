class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rep=[0]*len(nums)
        rep[0]=nums[0]
        for k in range(1,len(nums)):
            if rep[k-1]<=0:
                return False
            rep[k]=max(rep[k-1]-1,nums[k])
        return True
