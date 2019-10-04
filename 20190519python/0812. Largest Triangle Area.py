class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # s=1/2*[x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)]
        rep=0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    x1,x2,x3=points[i][0],points[j][0],points[k][0]
                    y1,y2,y3=points[i][1],points[j][1],points[k][1]
                    rep=max(rep,abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))))
        return rep
