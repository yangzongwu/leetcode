class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        rep=[]
        for k1 in range(len(nums)-3):
            if k1>0 and nums[k1]==nums[k1-1]:
                continue
            for k2 in range(k1+1,len(nums)-2):
                if k2>k1+1 and nums[k2]==nums[k2-1]:
                    continue
                left=k2+1
                right=len(nums)-1
                while left<right:
                    cur=nums[k1]+nums[k2]+nums[left]+nums[right]
                    if cur==target:
                        rep.append([nums[k1],nums[k2],nums[left],nums[right]])
                        left+=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                    elif cur<target:
                        left+=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                    else:
                        right-=1
                        while right>left and nums[right]==nums[right+1]:
                            right-=1
        return rep
                    
