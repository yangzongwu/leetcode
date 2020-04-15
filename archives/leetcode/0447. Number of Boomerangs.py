'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) 
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all 
in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
Accepted
'''
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rep=0
        for k in range(len(points)):
            rep=rep+self.subnumberOfBoomerangs(points[:k]+points[k+1:],points[k])
        return rep
    
    def subnumberOfBoomerangs(self,pointlist,pointk):
        dictpointgap={}
        for point in pointlist:
            gap=abs((point[0]-pointk[0])**2+(point[1]-pointk[1])**2)
            if gap not in dictpointgap:
                dictpointgap[gap]=1
            else:
                dictpointgap[gap]+=1
        rep=0
        for keys in dictpointgap:
            if dictpointgap[keys]>1:
                rep+=dictpointgap[keys]*(dictpointgap[keys]-1)
        return rep
