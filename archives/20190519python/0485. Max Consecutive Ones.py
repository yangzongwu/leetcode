class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        rep=0
        cur=0
        for i in range(len(nums)):
            if nums[i]==1:
                cur+=1
            else:
                rep=max(rep,cur)
                cur=0
        return max(rep,cur)
