class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rep=[]
        
        k=0
        while k<len(nums):
            tmp=self.two_sum(nums[k+1:],-nums[k])
            for cur in tmp:
                rep.append([nums[k]]+cur)
            j=k
            while j<len(nums) and nums[j]==nums[k]:
                j+=1
            k=j
        return rep
    
    def two_sum(self,nums,target):
        rep=[]
        left,right=0,len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                rep.append([nums[left],nums[right]])
                k=left
                while k<right and nums[k]==nums[left]:
                    k+=1
                left=k
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                right-=1
        return rep
