# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)<=1:
            return intervals
        
        intervals.sort(key=lambda x : x.start)
        
        k=0
        while k<len(intervals)-1:
            intervals[k].start
            
            if intervals[k].end<intervals[k+1].start:
                k+=1
            elif intervals[k+1].start<=intervals[k].end<=intervals[k+1].end:
                intervals[k].end=intervals[k+1].end
                intervals.pop(k+1)
            else: # intervals[k].end>intervals[k+1].end:
                intervals.pop(k+1)
        return intervals
