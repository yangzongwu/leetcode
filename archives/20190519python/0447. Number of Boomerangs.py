class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        rep=0
        for i in range(len(points)):
            rep+=self.calNumberOfBoomerangs(points[i],points[:i]+points[i+1:])
        return rep
    
    def calNumberOfBoomerangs(self,point,points):
        dict_distance=dict()
        for pointA in points:
            cur=(pointA[0]-point[0])**2+(pointA[1]-point[1])**2
            if cur in dict_distance:
                dict_distance[cur]+=1
            else:
                dict_distance[cur]=1
                
        rep=0
        for k in dict_distance:
            rep+=dict_distance[k]*(dict_distance[k]-1)
        return rep
    
