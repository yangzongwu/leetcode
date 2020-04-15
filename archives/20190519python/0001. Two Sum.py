class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictnums={}
        i=0
        while(i<len(nums)):
            if(target-nums[i] not in dictnums):
                dictnums[nums[i]]=i
            else:
                return[dictnums[target-nums[i]],i]
            i+=1
            
            
#==================================================================================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictnums={}
        for i,n in enumerate(nums):
            if target-n in dictnums:
                return [dictnums[target-n],i]
            dictnums[n]=i
