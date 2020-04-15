class Solution:
    def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> 'int':
        dictAB={}
        dictCD={}
        for a in A:
            for b in B:
                if a+b not in dictAB:
                    dictAB[a+b]=1
                else:
                    dictAB[a+b]+=1
        for c in C:
            for d in D:
                if c+d not in dictCD:
                    dictCD[c+d]=1
                else:
                    dictCD[c+d]+=1
        
        
        rep=0
        for key in dictAB:
            if -key in dictCD:
                rep+=dictAB[key]*dictCD[-key]
        return rep
