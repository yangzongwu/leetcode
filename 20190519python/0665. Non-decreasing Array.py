class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return True
        flag=True
        for k in range(1,len(nums)):
            if nums[k]<nums[k-1]:
                if flag==False:
                    return False
                elif k==len(nums)-1 or nums[k+1]>nums[k-1] or k==1 or nums[k]>nums[k-2]:
                    flag=False
                    continue
                else:
                    return False
        return True
