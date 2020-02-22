'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

'''
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        cnt=0
        for k in range(len(points)):
            dict_dis={}
            i=0
            while i<len(points):
                if i==k:
                    i+=1
                    continue
                tmp=(points[i][0]-points[k][0])**2+(points[i][1]-points[k][1])**2
                if tmp not in dict_dis:
                    dict_dis[tmp]=1
                else:
                    dict_dis[tmp]+=1
                i+=1
            for key in dict_dis:
                if dict_dis[key]>1:
                    cnt+=dict_dis[key]*(dict_dis[key]-1)
        return cnt

