class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rep=[]
        self.get_subsetsWithDup(nums,[],rep)
        return rep
    
    def get_subsetsWithDup(self,nums,res,rep):
        rep.append(res)
        k=0
        while k<len(nums):
            self.get_subsetsWithDup(nums[k+1:],res+[nums[k]],rep)
            i=k+1
            while i<len(nums) and nums[i]==nums[k]:
                i+=1
            k=i
        return
        
