class Solution:
    def findRelativeRanks(self, nums: 'List[int]') -> 'List[str]':
        rep=[s for s in nums]
        rep.sort()
        rep=rep[::-1]
        dicts={}
        for k in range(len(rep)):
            if k==0:
                dicts[rep[k]]='Gold Medal'
            elif k==1:
                dicts[rep[k]]='Silver Medal'
            elif k==2:
                dicts[rep[k]]='Bronze Medal'
            else:
                dicts[rep[k]]=str(k+1)
        res=[]
        for num in nums:
            res.append(dicts[num])
        return res
                
                
