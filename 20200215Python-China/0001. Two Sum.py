class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums={}
        rep=[]
        for k in range(0,len(nums)):
            if target-nums[k] not in dict_nums:
                dict_nums[nums[k]]=k
            else:
                rep=[dict_nums[target-nums[k]],k]
                break
        return rep
