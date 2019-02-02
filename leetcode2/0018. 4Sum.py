class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        rep=[]
        len_nums=len(nums)
        for k1 in range(len_nums-3):
            if k1>0 and nums[k1]==nums[k1-1]:
                continue
            for k2 in range((k1+1),len_nums-2):
                if k2>k1+1 and nums[k2]==nums[k2-1]:
                    continue
                left=k2+1
                right=len_nums-1
                while left<right:
                    res=nums[k1]+nums[k2]+nums[left]+nums[right]
                    if res==target:
                        rep.append([nums[k1],nums[k2],nums[left],nums[right]])
                        i=1
                        while left+i<right and nums[left+i]==nums[left]:
                            i+=1
                        left+=i
                    elif res<target:
                        i=1
                        while left+i<right and nums[left+i]==nums[left]:
                            i+=1
                        left+=i
                    else:
                        i=1
                        while right-i>left and nums[right-i]==nums[right]:
                            i+=1
                        right-=i
        return rep
            
