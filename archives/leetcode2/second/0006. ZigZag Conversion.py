class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows==1:
            return s
        rep=[[] for _ in range(numRows) ]
        i=0
        for ss in s:
            if i==2*numRows-2:
                i=0
            if i<numRows:
                rep[i].append(ss)
                i+=1
            elif numRows<=i<2*numRows-2:
                rep[numRows-1-(i-(numRows-1))].append(ss)
                i+=1
        res=''
        for lists in rep:
            tmp=''
            for ss in lists:
                tmp+=ss
            res+=tmp
        return res
