class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum=0
        right_sum=sum(nums[1:])
        if nums and left_sum==right_sum:
            return 0
        for k in range(1,len(nums)):
            left_sum+=nums[k-1]
            right_sum-=nums[k]
            if left_sum==right_sum:
                return k
        return -1
