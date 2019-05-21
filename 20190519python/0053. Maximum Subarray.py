class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        rep=nums[0]
        tmpnums=[nums[0]]
        for num in nums[1:]:
            if tmpnums[-1]<0:
                tmpnums.append(num)
                rep=max(rep,num)
            else:
                tmpnums.append(tmpnums[-1]+num)
                rep=max(rep,tmpnums[-1])
        return rep
