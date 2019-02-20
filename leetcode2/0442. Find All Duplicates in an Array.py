class Solution:
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        rep=set()
    
        k=0
        while k<len(nums):
            if nums[abs(nums[k])-1]<0:
                rep.add(abs(nums[k]))
            else:
                nums[abs(nums[k])-1]=-nums[abs(nums[k])-1]
            k+=1
        return list(rep)
