class Solution:
    def findShortestSubArray(self, nums: 'List[int]') -> 'int':
        dictnum={}
        k=0
        while k<len(nums):
            if nums[k] not in dictnum:
                dictnum[nums[k]]=[1,k,k]
            else:
                dictnum[nums[k]][0]+=1
                dictnum[nums[k]][2]=k
            k+=1
            
        rep=[]
        target=0
        for key in dictnum:
            if not rep:
                rep.append(dictnum[key])
                target=dictnum[key][0]
            else:
                if dictnum[key][0]==target:
                    rep.append(dictnum[key])
                elif dictnum[key][0]>target:
                    rep=[dictnum[key]]
                    target=dictnum[key][0]
                    
        res=len(nums)
        for lists in rep:
            res=min(res,lists[2]-lists[1]+1)
        return res
