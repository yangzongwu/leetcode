class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        rep=[]
        k=0
        left=intervals[0][0]
        while k<len(intervals):
            right=intervals[k][1]
            if k+1<len(intervals) and intervals[k+1][0]<=right:
                while k+1<len(intervals) and intervals[k+1][0]<=right:
                    k+=1
                    right=max(intervals[k][1],right)
            rep.append([left,right])
            k+=1
            if k<len(intervals):
                left=intervals[k][0]        
        return rep
