'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
'''
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
