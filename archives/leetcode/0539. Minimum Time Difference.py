'''
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes 
difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        rep=[]
        for time in timePoints:
            rep.append(int(time[0:2])*60+int(time[3:]))
        rep.sort()
        min_gap=rep[0]-rep[-1]+24*60
        for k in range(len(rep)-1):
            min_gap=min(min_gap,rep[k+1]-rep[k])
        return min_gap
        
