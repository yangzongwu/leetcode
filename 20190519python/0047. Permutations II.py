class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        rep=[]
        nums.sort()
        self.getpermuteUnique(nums,[],rep)
        return rep
    
    def getpermuteUnique(self,nums,res,rep):
        if not nums:
            rep.append(res)
            return
        
        k=0
        while k<len(nums):
            self.getpermuteUnique(nums[:k]+nums[k+1:],res+[nums[k]],rep)
            target=nums[k]
            k+=1
            while k<len(nums) and nums[k]==target:
                k+=1
                
