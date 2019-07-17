class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rep=[]
        self.getpermute(nums,[],rep)
        return rep
    
    def getpermute(self,nums,res,rep):
        if not nums:
            rep.append(res)
            return
        for k in range(len(nums)):
            self.getpermute(nums[:k]+nums[k+1:],res+[nums[k]],rep)
