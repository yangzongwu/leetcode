class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0])+'/'+str(nums[1])
        return str(nums[0])+'/('+self.connectString(nums[1:])+')'
    
    def connectString(self,nums):
        rep=""
        for num in nums:
            rep+=str(num)+'/'
        return rep[:-1]
