class Solution:
    def findPairs(self, nums: 'List[int]', k: 'int') -> 'int':
        dictnums={}
        for num in nums:
            if num not in dictnums:
                dictnums[num]=1
            else:
                dictnums[num]+=1
        rep=0
        if k<0:
            return 0
        if k==0:
            for key in dictnums:
                if dictnums[key]>1:
                    rep+=1
        else:
            for key in dictnums:
                if key+k in dictnums:
                    rep+=1
        return rep
