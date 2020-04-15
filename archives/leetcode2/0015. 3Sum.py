class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rep=[]
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            left=k+1
            right=len(nums)-1
            while left<right:
                if nums[k]+nums[left]+nums[right]==0:
                    rep.append([nums[k],nums[left],nums[right]])
                    i=1
                    while left+i<right and nums[left]==nums[left+i]:
                        i+=1
                    left+=i
                elif nums[k]+nums[left]+nums[right]<0:
                    i=1
                    while left+i<right and nums[left]==nums[left+i]:
                        i+=1
                    left+=i
                else:
                    i=1
                    while right-i>left and nums[right]==nums[right-i]:
                        i+=1
                    right-=i
        return rep
