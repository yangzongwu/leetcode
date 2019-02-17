# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        i,j=0,0
        rep=[]
        while i<len(A) and j<len(B):
            lo=max(A[i].start,B[j].start)
            ro=min(A[i].end,B[j].end)
            if lo<=ro:
                rep.append([lo,ro])
            if A[i].end>B[j].end:
                j+=1
            else:
                i+=1
        return rep
