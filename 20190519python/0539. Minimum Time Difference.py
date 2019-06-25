class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort(key=lambda x:[int(x[:2]),int(x[3:])])
        
        rep=24*60
        for k in range(len(timePoints)-1):
            h=(int(timePoints[k+1][:2])-int(timePoints[k][:2]))*60
            m=int(timePoints[k+1][3:])-int(timePoints[k][3:])
            rep=min(rep,h+m)
        
        h=(int(timePoints[-1][:2])-int(timePoints[0][:2]))*60
        m=int(timePoints[-1][3:])-int(timePoints[0][3:])
        rep=min(rep,24*60-h-m)
        
        return rep
