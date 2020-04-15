class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        lo,hi=0,0
        rep=[0]
        for s in S:
            if s=='I':
                hi+=1
                rep.append(hi)
            elif s=='D':
                lo-=1
                rep.append(lo)
        for k in range(len(rep)):
            rep[k]+=-lo
        return rep
