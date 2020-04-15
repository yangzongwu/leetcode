class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        tmp_A=[str(s) for s in A]
        rep=''.join(tmp_A)
        rep=str(int(rep)+K)
        res=[]
        for s in rep:
            res.append(int(s))
        return res
