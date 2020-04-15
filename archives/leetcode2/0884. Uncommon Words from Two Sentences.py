class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':
        nums=A.split(' ')+B.split(' ')
        dictnums={}
        for s in nums:
            if s not in dictnums:
                dictnums[s]=1
            else:
                dictnums[s]+=1
        rep=[]
        for key in dictnums:
            if dictnums[key]==1:
                rep.append(key)
        return rep
