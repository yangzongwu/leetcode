class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        if sum(nums)==0:
            return '0'
        
        nums=self.subsort(nums)
        return ''.join(str(num) for num in nums)
        
    def subsort(self,nums):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if self.cmp(nums[i],nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
    
    def cmp(self,a,b):
        return int(str(b)+str(a))>int(str(a)+str(b))
