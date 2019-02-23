# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        self.rep=[]
        
        def dfs(A,B):
            if not A or not B:
                return
            left=max(A[0].start,B[0].start)
            right=min(A[0].end,B[0].end)
            if right>=left:
                self.rep.append([left,right])
            if B[0].end>A[0].end:
                dfs(A[1:],B)
            else:
                dfs(A,B[1:])
            
        dfs(A,B)
        return self.rep
