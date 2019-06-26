class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict_nums={}
        for k in range(len(nums)):
            if nums[k] not in dict_nums:
                dict_nums[nums[k]]=[1,k,k]
            else:
                dict_nums[nums[k]][0]+=1
                dict_nums[nums[k]][2]=k
        
        cur=nums[0]
        rep=len(nums)
        for k in dict_nums:
            if dict_nums[k][0]>dict_nums[cur][0]:
                rep=dict_nums[k][2]-dict_nums[k][1]
                cur=k
            elif dict_nums[k][0]==dict_nums[cur][0]:
                rep=min(rep,dict_nums[k][2]-dict_nums[k][1])
        return rep+1
