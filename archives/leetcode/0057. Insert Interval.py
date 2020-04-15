# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda s:s.start)
        i=0
        while i<len(intervals)-1:
            if intervals[i+1].start>intervals[i].end:
                i+=1
            else:
                if intervals[i+1].end<=intervals[i].end:
                    intervals.pop(i+1)
                else:
                    intervals[i].end=intervals[i+1].end
                    intervals.pop(i+1)
        return intervals
    def insert00(self, intervals, newInterval):
        rep = []
        for s in intervals:
            tmp = Interval(s[0], s[1])
            rep.append(tmp)
        intervals = rep
        newInterval = Interval(newInterval[0], newInterval[1])

        rep = []
        if not intervals:
            return [newInterval]
        for interval in intervals:
            if newInterval.start == 'x':
                rep.append(interval)
            else:
                if newInterval.start > interval.end:
                    rep.append(interval)
                elif newInterval.end < interval.start:
                    rep.append(newInterval)
                    rep.append(interval)
                    newInterval.start = 'x'
                else:
                    newInterval.start = min(newInterval.start, interval.start)
                    if newInterval.end <= interval.end:
                        newInterval.end = interval.end
                        rep.append(newInterval)
                        newInterval.start = 'x'
        if newInterval.start != 'x':
            rep.append(newInterval)
        return rep





    def insert01(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        rep=[]
        for s in intervals:
            tmp=Interval(s[0],s[1])
            rep.append(tmp)
        intervals=rep
        newInterval=Interval(newInterval[0],newInterval[1])


        if not intervals:
            return [newInterval]
        if newInterval.start <= intervals[0].start:
            if newInterval.end < intervals[0].start:
                intervals.insert(0, newInterval)
                return intervals
            elif newInterval.end < intervals[0].end:
                intervals[0].start = newInterval.start
                return intervals
            else:
                return self.insert(intervals[1:], newInterval)
        if newInterval.end >= intervals[-1].end:
            if newInterval.start > intervals[-1].end:
                intervals.append(newInterval)
                return intervals
            elif newInterval.start > intervals[-1].start:
                intervals[-1].end = newInterval.end
                return intervals
            else:
                return self.insert(intervals[:-1], newInterval)

        i = 0
        while i < len(intervals):
            if intervals[i].start < newInterval.start:
                i += 1
            else:
                break
        left = i - 1
        return self.subinsert(intervals, newInterval, left)

    def subinsert(self, intervals, newInterval, left):
        if newInterval.start <= intervals[left].end:
            if newInterval.end < intervals[left].end:
                return intervals
            elif newInterval.end < intervals[left + 1].start:
                intervals[left].end = newInterval.end
                return intervals
            elif newInterval.end < intervals[left + 1].end:
                intervals[left].end = intervals[left + 1].end
                intervals.pop(left + 1)
                return intervals
            else:
                intervals.pop(left + 1)
                return self.subinsert(intervals, newInterval, left)
        else:  # newInterval.start>=intervals[left].end
            if newInterval.end < intervals[left + 1].start:
                intervals.insert(left + 1, newInterval)
                return intervals
            elif newInterval.end < intervals[left + 1].end:
                intervals[left + 1].start = newInterval.start
                return intervals
            else:  # newInterval.end>intervals[left+1].end:
                intervals.pop(left + 1)
                return self.subinsert(intervals, newInterval, left)


if __name__=='__main__':
    A=[[1, 2], [3, 5]]
    B=[2, 3]
    Test=Solution()
    print(Test.insert(A,B))
