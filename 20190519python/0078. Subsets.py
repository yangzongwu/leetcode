class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rep=[[]]
        for k in range(len(nums)):
            self.get_subsets(nums[k+1:],[nums[k]],rep)
        return rep
    
    def get_subsets(self,nums,res,rep):
        rep.append(res)
        if not nums:
            return 
        for k in range(len(nums)):
            self.get_subsets(nums[k+1:],res+[nums[k]],rep)
