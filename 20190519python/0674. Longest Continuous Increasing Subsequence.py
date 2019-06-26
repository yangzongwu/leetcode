class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        rep=0
        cnt=1
        for k in range(len(nums)-1):
            if nums[k+1]>nums[k]:
                cnt+=1
            else:
                rep=max(rep,cnt)
                cnt=1
        return max(rep,cnt)
