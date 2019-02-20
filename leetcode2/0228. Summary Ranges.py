class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        rep=[]
        k=0
        while k<len(nums):
            j=1
            tmp=[nums[k]]
            while k+j<len(nums) and nums[k+j]==nums[k]+j:
                tmp.append(nums[k+j])
                j+=1
            if len(tmp)==1:
                rep.append(str(tmp[0]))
            else:
                rep.append(str(tmp[0])+'->'+str(tmp[-1]))
            k+=j
        return rep
                
