class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        len_nums=len(nums)
        rep=nums[0]+nums[1]+nums[2]
        gap=abs(nums[0]+nums[1]+nums[2]-target)
        for k in range(len(nums)):
            if k>1 and nums[k]==nums[k-1]:
                continue
            left=k+1
            right=len_nums-1
            while right>left:
                res=nums[k]+nums[left]+nums[right]
                if res==target:
                    return target
                else:
                    if abs(res-target)<gap:
                        gap=abs(res-target)
                        rep=res
                    if res>target:
                        right-=1
                    else:
                        left+=1
        return rep
                
