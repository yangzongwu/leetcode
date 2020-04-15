class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        rep=nums[0]+nums[1]+nums[2]
        for k in range(len(nums)-2):
            left=k+1
            right=len(nums)-1
            while left<right:
                total=nums[left]+nums[right]+nums[k]
                if abs(total-target)<abs(rep-target):
                    rep=total
                if total>target:
                    right-=1
                else:
                    left+=1
        return rep
