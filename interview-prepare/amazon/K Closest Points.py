'''
K Closest Points to Origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
'''
class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        points.sort(key=lambda x:x[0]**2+x[1]**2,reverse=False)
        return points[:K]
        

'''
K Closest Points
Description
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are 
same in the x-axis, sorted by y-axis.
Example 1:
Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 
Output: [[1,1],[2,5],[4,4]]
Example 2:
Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]
'''
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        def sortpointfunc(pointx,pointy):
            pathx=(pointx.x-origin.x)**2+(pointx.y-origin.y)**2
            pathy=(pointy.x-origin.x)**2+(pointy.y-origin.y)**2
            if pathx>pathy:
                return 1
            elif pathx<pathy:
                return -1
            else:
                if pointx.x<pointy.x:
                    return -1
                elif pointx.x>pointy.x:
                    return 1
                else:
                    if pointx.y<pointy.x:
                        return -1
                    else:
                        return 1
        def sortpoints(points):
            from functools import cmp_to_key
            points=sorted(points,key=cmp_to_key(sortpointfunc))
            return points[:k]
        
        dictposts={}                
        for point in points:
            tmp=(point.x-origin.x)**2+(point.y-origin.y)**2
            if tmp not in dictposts:
                dictposts[tmp]=[point]
            else:
                dictposts[tmp].append(point)
        rep=[]
        for key in dictposts:
            rep.append(key)
        rep.sort()
        
        result=[]
        cnt=0
        while k>0:
            cur=dictposts[rep[cnt]]
            if len(cur)>1:
                cur=sortpoints(cur)
            if len(cur)<k:
                result+=cur
                k-=len(cur)
            else:
                result+=cur[:k]
                k-=k
            cnt+=1
        return result
                


#==================================Time Limit Exceeded===================================================================

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        def sortpoint(pointx,pointy):
            pathx=(pointx.x-origin.x)**2+(pointx.y-origin.y)**2
            pathy=(pointy.x-origin.x)**2+(pointy.y-origin.y)**2
            if pathx>pathy:
                return 1
            elif pathx<pathy:
                return -1
            else:
                if pointx.x<pointy.x:
                    return -1
                elif pointx.x>pointy.x:
                    return 1
                else:
                    if pointx.y<pointy.y:
                        return -1
                    else:
                        return 1
        from functools import cmp_to_key
        points=sorted(points,key=cmp_to_key(sortpoint))
        return points[:k]

