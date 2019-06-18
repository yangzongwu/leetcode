class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums)==1:
            return ["Gold Medal"]
        if len(nums)==2:
            if nums[0]>nums[1]:
                return["Gold Medal","Silver Medal"]
            else:
                return["Silver Medal","Gold Medal"]
            
        tmp=nums[:]
        tmp.sort(reverse=True)
        dict_nums={}
        dict_nums[tmp[0]]="Gold Medal"
        dict_nums[tmp[1]]="Silver Medal"
        dict_nums[tmp[2]]="Bronze Medal"
        for k in range(3,len(tmp)):
            dict_nums[tmp[k]]=str(k+1)
        
        rep=[]
        for num in nums:
            rep.append(dict_nums[num])
        return rep
